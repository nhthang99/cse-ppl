
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
                global_envi.append(self.visit(x, (global_envi, False)))
            elif isinstance(x, FuncDecl):
                global_envi.append(self.visit(x, global_envi))

    def visitVarDecl(self, ast, envi):
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
