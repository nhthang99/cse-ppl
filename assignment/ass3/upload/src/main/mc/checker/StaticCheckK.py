
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):
    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putInt",MType([IntType()],VoidType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([],FloatType())),
    Symbol("putFloat",MType([FloatType()],VoidType())),
    Symbol("putFloatLn",MType([FloatType()],VoidType())),
    Symbol("putBool",MType([BoolType()],VoidType())),
    Symbol("putBoolLn",MType([BoolType()],VoidType())),
    Symbol("putString",MType([StringType()],VoidType())),
    Symbol("putStringLn",MType([StringType()],VoidType())),
    Symbol("putLn",MType([],VoidType()))
    ]
    
              
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        # Check no main function
        entry_point=False
        for decl in ast.decl:
            if isinstance(decl,FuncDecl):
                if decl.name.name=='main':
                    entry_point=True; break
        if entry_point == False:
            raise NoEntryPoint()

        self.func_list=[]; prog_envi=c[:]
        for decl in ast.decl:
            if isinstance(decl,VarDecl):
                # Check redeclared variable
                prog_envi.append(self.visitVarDecl(decl,prog_envi))
            elif isinstance(decl,FuncDecl):
                # Check redeclared function            
                if not self.lookup(decl.name.name,prog_envi,lambda x: x.name) is None:
                    raise Redeclared(Function(),decl.name.name)             
                # Update global enviroment and unused functon list
                return_type= self.visit(decl.returnType,prog_envi)
                param_type=[self.visit(param.varType,None) for param in decl.param]
                fucntion = Symbol(decl.name.name,MType(param_type,return_type))
                self.func_list.append(fucntion); prog_envi.append(fucntion)

        # Search next node and raise another error
        self.func_call= None
        for decl in ast.decl:
            if isinstance(decl,FuncDecl):
                self.func_call = decl.name.name
                self.visitFuncDecl(decl,prog_envi)

        # Check unreachable function
        if len(self.func_list) != 1:
            raise UnreachableFunction(self.func_list[0].name)        

    def visitVarDecl(self,ast,c):
        if self.lookup(ast.variable,c,lambda x: x.name) is None:
            varType= self.visit(ast.varType,c)
            return Symbol(ast.variable,varType)
        else:
            raise Redeclared(Variable(),ast.variable)
        
    def visitFuncDecl(self,ast, c): 
      
        local_envi=[]
        # Check redeclared parameter
        for param in ast.param:
            if self.lookup(param.variable,local_envi,lambda x: x.name) is None:
                local_envi.append(self.visit(param,[]))
            else:
                raise Redeclared(Parameter(),param.variable)

        # Check Function is not return
        return_type= self.visit(ast.returnType,c)
        if isinstance(return_type,VoidType):
            for member in ast.body.member:
                if isinstance(member,VarDecl):
                    local_envi+= [self.visitVarDecl(member,local_envi)]
                elif isinstance(member,Expr):
                    self.visit(member,[local_envi,c])
                else:
                    self.visit(member,[[local_envi,c],False,return_type])
        else:
            func_return=False
            for x in ast.body.member:
                if isinstance(x,VarDecl):
                    local_envi+= [self.visitVarDecl(x,local_envi)]
                elif isinstance(x,Expr):
                    self.visit(x,[local_envi,c])
                else:
                    ref_envi=[local_envi,c]
                    if self.visit(x,[ref_envi,False,return_type]) == True : func_return = True
            if not func_return: raise FunctionNotReturn(ast.name.name)
        
    def visitBlock(self,ast,c):
        trigger=False; block_envi=[]
        for x in ast.member:
            if isinstance(x,VarDecl):
                block_envi += [self.visit(x,block_envi)]
            elif isinstance(x,Expr):
                self.visit(x,[block_envi]+c[0])
            else:
                ref_block=[[block_envi]+c[0],c[1],c[2]]
                if self.visit(x,ref_block) == True : trigger = True

        return trigger
        
    def visitDowhile(self,ast,c):
        # check dowhile expression
        expr= self.visit(ast.exp,c[0])
        if not isinstance(expr,BoolType):
            raise TypeMismatchInStatement(ast)
        
        # check function not return
        trigger= False; block_envi=[]

        for x in ast.sl:
            if isinstance(x,VarDecl):
                block_envi += [self.visit(x,block_envi)] 
            elif isinstance(x,Expr):
                self.visit(x,[block_envi]+c[0])
            else:
                ref_block=[[block_envi]+c[0],True,c[2]]
                if self.visit(x,ref_block) == True : trigger = True

        return trigger

    def visitIf(self,ast,c):
        # check if expression type
        expr= self.visit(ast.expr,c[0])
        if not isinstance(expr,BoolType):
            raise TypeMismatchInStatement(ast)
        
        # check function not return in then stmt
        return_if = return_else = True
        if isinstance(ast.thenStmt,(Return,Block,If,Dowhile)):
            return_if= self.visit(ast.thenStmt,c)
        else:
            if isinstance(ast.thenStmt,(For,Break,Continue)):
                self.visit(ast.thenStmt,c)
            else:
                self.visit(ast.thenStmt,c[0])
            return_if= False
        # check function not return in else stmt
        if ast.elseStmt is None:
            return_else= False
        else:
            if isinstance(ast.elseStmt,(Return,Block,If,Dowhile)):
                return_else= self.visit(ast.elseStmt,c)
            else: 
                if isinstance(ast.elseStmt,(For,Break,Continue)):
                    self.visit(ast.elseStmt,c)
                else:
                    self.visit(ast.elseStmt,c[0])
                return_else= False

        return True if return_if==True and return_else==True else False

    def visitFor(self,ast,c):
        expr1= self.visit(ast.expr1,c[0])
        expr2= self.visit(ast.expr2,c[0])
        expr3= self.visit(ast.expr3,c[0])

        # Check for expression type
        if not isinstance(expr1,IntType) or\
           not isinstance(expr2,BoolType) or\
           not isinstance(expr3,IntType):
           raise TypeMismatchInStatement(ast)
        
        if type(ast.loop) in (BinaryOp,UnaryOp,CallExpr,Id,ArrayCell,Literal):
            self.visit(ast.loop,c[0])    
        else:
            self.visit(ast.loop,[c[0],True,c[2]])

    def visitReturn(self,ast,c):
        # check void function
        if bool(ast.expr is None) != bool(isinstance(c[-1],VoidType)):
            raise TypeMismatchInStatement(ast)
        
        # check return function
        if  not ast.expr is None:
            res = self.visit(ast.expr,c[0])

            if isinstance(c[-1],ArrayPointerType):
                if isinstance(res,(ArrayPointerType,ArrayType)):
                    if not isinstance(res.eleType,type(c[-1].eleType)):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            elif isinstance(c[-1],FloatType):
                if not isinstance(res,(IntType,FloatType)):
                    raise TypeMismatchInStatement(ast)
            else:
                if not isinstance(res,type(c[-1])):
                    raise TypeMismatchInStatement(ast)

        return True

    def visitBreak(self,ast,c):
        if c[1] == False:
            raise BreakNotInLoop()

    def visitContinue(self,ast,c):
        if c[1] == False:
            raise ContinueNotInLoop()
    
    def visitCallExpr(self, ast, c): 

        attr = [self.visit(x,c) for x in ast.param]

        # Check Undeclared Function
        for lst in c:
            res = self.lookup(ast.method.name,lst,lambda x: x.name)
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(Function(),ast.method.name)

        
        if len(res.mtype.partype) != len(attr):
            raise TypeMismatchInExpression(ast)
        else:
            # Check function parameter type
            for i in range(0,len(attr)):
                if isinstance(res.mtype.partype[i],ArrayPointerType):
                    if isinstance(attr[i],(ArrayType,ArrayPointerType)):
                        if not isinstance(res.mtype.partype[i].eleType,type(attr[i].eleType)):
                            raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                elif isinstance(res.mtype.partype[i],FloatType) and isinstance(attr[i],(FloatType,IntType)):
                    continue
                elif isinstance(res.mtype.partype[i],type(attr[i])):
                    continue
                else: 
                    raise TypeMismatchInExpression(ast)
            # Check unreachable function
            if self.func_call != res.name:
                x= self.lookup(res.name,self.func_list,lambda x: x.name)
                if not x is None:
                    self.func_list.remove(res)

        return res.mtype.rettype

    def visitId(self,ast,c):
        for lst in c:
            res = self.lookup(ast.name,lst,lambda x: x.name)
            if not res is None: break

        if res is None:
            raise Undeclared(Identifier(),ast.name)
        else:
            if not type(res.mtype) is MType:
                return res.mtype
            else:
                return res.mtype.rettype

    def visitArrayCell(self,ast,c):
        arr= self.visit(ast.arr,c)
        idx= self.visit(ast.idx,c)

        if not isinstance(arr,(ArrayType,ArrayPointerType)):
            raise TypeMismatchInExpression(ast)
        if not isinstance(idx,IntType):
            raise TypeMismatchInExpression(ast)

        return arr.eleType

    def visitUnaryOp(self,ast,c):
        op=ast.op
        expr=self.visit(ast.body,c)

        if op == '!':
            if isinstance(expr,BoolType):
                return BoolType()
            else: 
                raise TypeMismatchInExpression(ast)
        
        if op == '-':
            if isinstance(expr,(IntType,FloatType)):
                return expr
            else:
                raise TypeMismatchInExpression(ast)

    def visitBinaryOp(self,ast,c):
        op=ast.op
        left=self.visit(ast.left,c)
        right=self.visit(ast.right,c)

        def checkType(acceptType, returnType=None):
            if not isinstance(left, acceptType) or\
               not isinstance(right, acceptType):
                raise TypeMismatchInExpression(ast)

        if op in ['+','-','*','/']:
            checkType((IntType, FloatType))
            if isinstance(left, IntType) and\
               isinstance(right, IntType):
                return IntType()
            else:
                return FloatType()
        elif op == '%':
            checkType(IntType)
            return IntType()
        elif op in ['!=', '==']:
            checkType((IntType,BoolType))
            return BoolType()
        elif op in ['<', '<=', '>', '>=']:
            checkType((IntType, FloatType))
            return BoolType()
        elif op in ['&&', '||']:
            checkType(BoolType)
            return BoolType()
        elif op == '=':
            if not type(ast.left) in (Id,ArrayCell):
                raise NotLeftValue(ast.left)

            if isinstance(left,(VoidType,ArrayType,ArrayPointerType)):
                raise TypeMismatchInExpression(ast)
            if isinstance(left,FloatType):
                if not isinstance(right,(IntType,FloatType)):
                    raise TypeMismatchInExpression(ast)
            elif not isinstance(left,type(right)):
                raise TypeMismatchInExpression(ast)
            else:
                return left
        
    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitIntType(self,ast,c):
        return IntType()

    def visitFloatType(self,ast,c):
        return FloatType()

    def visitStringType(self,ast,c):
        return StringType()

    def visitBoolType(self,ast,c):
        return BoolType()

    def visitVoidType(self,ast,c):
        return VoidType()
        
    def visitArrayType(self,ast,c):
        eleType= self.visit(ast.eleType,c)
        return ArrayType(ast.dimen,eleType)

    def visitArrayPointerType(self,ast,c):
        eleType= self.visit(ast.eleType,c)
        return ArrayPointerType(eleType)
