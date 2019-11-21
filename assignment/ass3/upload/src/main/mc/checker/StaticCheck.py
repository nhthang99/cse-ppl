
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
        Symbol("getInt", MType([], IntType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType], VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self,ast, global_envi): 
        global_envi = global_envi[:]
        self.func_unused = []
        # Check whether main function exist or not
        is_main_func_defined = False
        for x in ast.decl:
            if isinstance(x, FuncDecl) and x.name.name == 'main':
                is_main_func_defined = True
                break
        if not is_main_func_defined:
            raise NoEntryPoint()
        
        # Check Redeclare
        for x in ast.decl:
            if isinstance(x, VarDecl):
                global_envi.append(self.visit(x, global_envi))

            elif isinstance(x, FuncDecl):
                rettype = self.visit(x.returnType, None)
                func = Symbol(
                    x.name.name, 
                    MType([x.varType for x in x.param], rettype)
                )
                for i in global_envi:
                    if i.name == func.name:
                        raise Redeclared(Function(), func.name)
    
                global_envi.append(func)
                
                if func.name != 'main':
                    self.func_unused.append(func)
        
        for decl in ast.decl:
            if isinstance(decl, FuncDecl):
                self.visit(decl, global_envi)
        
        if self.func_unused:
            raise UnreachableFunction(self.func_unused[0].name)

    def visitVarDecl(self, ast, envi):
        is_redeclare = self.lookup(ast.variable, envi, lambda x: x.name)
        if is_redeclare:
            raise Redeclared(Variable(), ast.variable)

        else:
            return Symbol(ast.variable, MType(None, ast.varType))
    
    def visitFuncDecl(self, ast, global_envi):
        local_envi = []
        para_list = []

        for param in ast.param:
            if param.variable in para_list:
                raise Redeclared(Parameter(), param.variable)

            else:
                para_list.append(param.variable)
                local_envi.append(self.visit(param, local_envi))
        
        return_type = self.visit(ast.returnType, None)
        is_return = self.visit(ast.body, (global_envi, local_envi, False, return_type))
        
        if not is_return and not isinstance(return_type, VoidType):
            raise FunctionNotReturn(ast.name.name)

    def visitBlock(self, ast, c):
        global_envi = c[0]
        local_envi = c[1]
        is_in_loop = c[2]
        return_type = c[3]
        is_return = False
        var_decl_in_block = []
        for stmt in ast.member:
            if isinstance(stmt, VarDecl):
                var_decl = self.visit(stmt, local_envi)
                for x in global_envi:
                    if x.name == var_decl.name:
                        global_envi.remove(x)
                        global_envi.append(var_decl)
                local_envi.append(var_decl)
                var_decl_in_block.append(var_decl)
            
            elif isinstance(stmt, Expr):
                self.visit(stmt, global_envi + local_envi)

            elif isinstance(stmt, Block):
                is_return = self.visit(stmt, (global_envi + local_envi, [], is_in_loop, return_type))
        
            else:
                is_return = self.visit(stmt, (global_envi, local_envi, is_in_loop, return_type))
                
        for x in var_decl_in_block:
            local_envi.remove(x)
        
        return is_return

    # def visitStmt(self, ast, c):
    #     global_envi = c[0]
    #     local_envi = c[1]
    #     is_in_loop = c[2]
    #     return_type = c[3]
    #     if isinstance(ast, Expr):
    #         self.visit(ast, global_envi + local_envi)
    #     else:
    #         return self.visit(ast, (global_envi, local_envi, is_in_loop, return_type))
    
    def visitUnaryOp(self, ast, c):
        expr = self.visit(ast.body, c)
        if ast.op == '!':
            if isinstance(expr, BoolType):
                return expr
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op == '-':
            if isinstance(expr, (IntType, FloatType)):
                return expr
            else:
                raise TypeMismatchInExpression(ast)
        
    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        
        def check_type(accept_type,return_type=None):
            if not isinstance(left,accept_type) or not isinstance(right,accept_type):
                raise TypeMismatchInExpression(ast)

            if return_type:
                return return_type

            elif isinstance(left,IntType) and isinstance(right,FloatType):
                return right

            elif isinstance(left,FloatType) and isinstance(right,IntType):
                return left

            elif isinstance(left, type(right)):
                return left

            else:
                raise TypeMismatchInExpression(ast)

        if ast.op == '=':
            if not type(ast.left) in (CallExpr, Id, ArrayCell):
                raise NotLeftValue(ast.left)

            elif isinstance(left, (VoidType, ArrayType, ArrayPointerType)):
                raise TypeMismatchInExpression(ast)

            elif isinstance(left, FloatType):
                if not isinstance(right, (IntType, FloatType)):
                    raise TypeMismatchInExpression(ast)

            elif not isinstance(left, type(right)):
                raise TypeMismatchInExpression(ast)

            return left
        elif ast.op in ['+', '-', '*', '/']:
            return check_type((IntType, FloatType))

        elif ast.op == '%':
            return check_type(IntType, IntType())

        elif ast.op in ['!=', '==']:
            return check_type((IntType, BoolType), BoolType())

        elif ast.op in ['<', '<=', '>', '>=']:
            return check_type((IntType, FloatType), BoolType())

        elif ast.op in ['&&', '||']:
            return check_type(BoolType, BoolType())

    def visitId(self, ast, c):
        is_declare = self.lookup(ast.name, c, lambda x: x.name)
        if not is_declare:
            raise Undeclared(Identifier(), ast.name)

        elif not isinstance(is_declare.mtype, MType):
            return is_declare.mtype

        else:
            return is_declare.mtype.rettype


    def visitIf(self, ast, c):
        envi = c[0] + c[1]
        expr_type = self.visit(ast.expr, envi)
        if not isinstance(expr_type, BoolType):
            raise TypeMismatchInStatement(ast)

        is_return_if = False
        is_return_else = False

        if not isinstance(ast.thenStmt, Expr):
            self.visit(ast.thenStmt, c)
        else:
            is_return_if = self.visit(ast.thenStmt, envi)

        if ast.elseStmt:
            if not isinstance(ast.elseStmt, Expr):
                self.visit(ast.elseStmt, c)

            else:
                is_return_else = self.visit(ast.elseStmt, envi)
        
        return is_return_if and is_return_else

    def visitDowhile(self, ast, c):
        envi = c[0] + c[1]
        expr_type = self.visit(ast.exp, envi)
        if not isinstance(expr_type, BoolType):
            raise TypeMismatchInStatement(ast)
        
        is_return = False
        for stmt in ast.sl:
            if not isinstance(stmt, Expr):
                is_in_loop = True
                is_return = self.visit(stmt, (c[0], c[1], is_in_loop, c[-1]))

            else:
                self.visit(stmt, envi)
        return is_return
    
    def visitFor(self, ast, c):
        envi = c[0] + c[1]
        expr1_type = self.visit(ast.expr1, envi)
        expr2_type = self.visit(ast.expr2, envi)
        expr3_type = self.visit(ast.expr3, envi)

        is_match = isinstance(expr1_type, IntType) \
            and isinstance(expr2_type, BoolType) \
            and isinstance(expr3_type, IntType)

        if not is_match:
            raise TypeMismatchInStatement(ast)

        if not isinstance(ast.loop, Expr):
            is_in_loop = True
            is_return = self.visit(ast.loop, (c[0], c[1], is_in_loop, c[-1]))
            return is_return

        else:
            self.visit(ast.loop, envi)

    def visitReturn(self, ast, c):
        return_type = c[-1]
        if not ast.expr:
            if not isinstance(return_type, VoidType):
                raise TypeMismatchInStatement(ast)

        elif isinstance(return_type, VoidType):
            raise TypeMismatchInStatement(ast)

        else:
            envi = c[0] + c[1]
            rlt_expr = self.visit(ast.expr, envi)
            if isinstance(return_type, ArrayPointerType):

                if isinstance(rlt_expr, (ArrayPointerType, ArrayType)):
                    if not isinstance(rlt_expr.eleType, type(return_type.eleType)):
                        raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)

            elif isinstance(return_type, FloatType):
                if not isinstance(rlt_expr, (IntType, FloatType)):
                    raise TypeMismatchInStatement(ast)

            elif not isinstance(rlt_expr, type(return_type)):
                raise TypeMismatchInStatement(ast)
        return True # function have returned

    def visitCallExpr(self, ast, c):
        para_list = [self.visit(x, c) for x in ast.param]
        
        res = self.lookup(ast.method.name, c, lambda x: x.name)
        if not res:
            raise Undeclared(Function(), ast.method.name)

        elif not isinstance(res.mtype, MType) or len(res.mtype.partype) != len(para_list):
            raise TypeMismatchInExpression(ast)

        else:
            for i in range(0, len(para_list)):
                if isinstance(res.mtype.partype[i],ArrayPointerType):
                    if isinstance(para_list[i],(ArrayType,ArrayPointerType)):
                        if not isinstance(res.mtype.partype[i].eleType,type(para_list[i].eleType)):
                            raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInExpression(ast)

                elif isinstance(res.mtype.partype[i],FloatType) and isinstance(para_list[i],(FloatType,IntType)) \
                    or isinstance(res.mtype.partype[i],type(para_list[i])):
                    continue

                else: 
                    raise TypeMismatchInExpression(ast)

        for x in self.func_unused:
            if x.name == ast.method.name:
                self.func_unused.remove(x)
        return res.mtype.rettype

    def visitArrayCell(self, ast, envi):
        arr = self.visit(ast.arr, envi)
        idx = self.visit(ast.idx, envi)

        if not isinstance(idx, IntType):
            raise TypeMismatchInExpression(ast)

        elif not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)

        return arr.eleType

    def visitBreak(self, ast, c):
        is_in_loop = c[2]
        if not is_in_loop:
            raise BreakNotInLoop()

    def visitContinue(self, ast, c):
        is_in_loop = c[2]
        if not is_in_loop:
            raise ContinueNotInLoop()

    def visitIntType(self,ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitBoolType(self, ast, c):
        return BoolType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitArrayType(self, ast, c):
        ele_type= self.visit(ast.eleType, c)
        return ArrayType(ast.dimen, ele_type)
        
    def visitArrayPointerType(self, ast, c):
        ele_type= self.visit(ast.eleType, c)
        return ArrayPointerType(ele_type)

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()
    
