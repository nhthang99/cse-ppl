
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
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self,ast, global_envi): 
        global_envi = global_envi[:]
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
<<<<<<< HEAD
                global_envi.append(self.visit(x, global_envi))
=======
                global_envi.append(self.visit(x, (global_envi, False)))
>>>>>>> f0636bc072d14da81fc4a4d9076a1e339dce4144
            elif isinstance(x, FuncDecl):
                global_envi.append(self.visit(x, global_envi))

    def visitVarDecl(self, ast, envi):
<<<<<<< HEAD
        is_redeclare = self.lookup(ast.variable, envi, lambda x: x.name)
        if is_redeclare:
            raise Redeclared(Variable(), ast.variable)
        else:
            return Symbol(ast.variable, MType(None, ast.varType))
    
    def visitFuncDecl(self, ast, global_envi):
        is_redeclare = self.lookup(ast.name.name, global_envi, lambda x: x.name)
        if is_redeclare:
            raise Redeclared(Function(), ast.name.name)

        local_envi = []
        para_list = []
        for param in ast.param:
            if param.variable in para_list:
                raise Redeclared(Parameter(), param.variable)
            else:
                para_list.append(param.variable)
                local_envi.append(self.visit(param, local_envi))
        
        return_type = self.visit(ast.returnType, None)
        for stmt in ast.body.member:
            if isinstance(stmt, VarDecl):
                local_envi.append(self.visit(stmt, local_envi))
            elif isinstance(stmt, Expr):
                self.visit(stmt, global_envi + local_envi)
            elif isinstance(stmt, Stmt):
                self.visit(stmt, None)

        return Symbol(ast.name.name, MType([para.variable for para in ast.param], return_type))
    
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
                raise NotLeftValue(ast)
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
        expr_type = self.visit(ast.expr, c[0])
        if not isinstance(expr_type, BoolType):
            raise TypeMismatchInStatement(ast)

    def visitDowhile(self, ast, c):
        expr_type = self.visit(ast.exp, c[0])
        if not isinstance(expr_type, BoolType):
            raise TypeMismatchInStatement(ast)
    
    def visitFor(self, ast, c):
        expr1_type = self.visit(ast.expr1, c[0])
        expr2_type = self.visit(ast.expr2, c[0])
        expr3_type = self.visit(ast.expr3, c[0])

        match = isinstance(expr1_type, IntType) and isinstance(expr2_type, BoolType) and isinstance(expr3_type, IntType)
        if not match:
            raise TypeMismatchInStatement(ast)

    def visitReturn(self, ast, c):
        return_type = c[1]
        if not ast.expr:
            if not isinstance(return_type, VoidType):
                raise TypeMismatchInStatement(ast)
        elif isinstance(return_type, VoidType):
            raise TypeMismatchInStatement(ast)
        else:
            pass

    def visitIntType(self,ast, c):
        return IntType()

    def visitFloatType(self, ast, c):
        return FloatType()

    def visitStringType(self, ast, c):
        return StringType()

    def visitBooleanType(self, ast, c):
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
    
=======
        sb = Symbol(ast.variable, MType(None, ast.varType))
        name_global_envi_lst = (x.name for x in envi[0])
        if sb.name in name_global_envi_lst:
            is_param = envi[1]
            if is_param:
                raise Redeclared(Parameter(), sb.name)
            else:
                raise Redeclared(Variable(), sb.name)
        else:
            return sb
    
    def visitFuncDecl(self, ast, global_envi):
        sb = Symbol(ast.name.name, MType([para.variable for para in ast.param], ast.returnType))
        name_global_envi_lst = (x.name for x in global_envi)
        if sb.name in name_global_envi_lst:
            raise Redeclared(Function(), sb.name)
        else:
            local_envi = []
            for param in ast.param:
                local_envi.append(self.visit(param, (local_envi, True)))
            return sb
>>>>>>> f0636bc072d14da81fc4a4d9076a1e339dce4144
