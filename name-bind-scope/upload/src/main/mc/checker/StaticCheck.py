
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
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        # print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        return [self.visit(x, c) for x in ast.decl]

    def visitFuncDecl(self,ast, c):
        if self.lookup(ast.name.name, c, lambda x: x):
            return Redeclared(Function(), ast.name.name)
        else:
            c.append(ast.name.name)
            return ast.name.name

    def visitVarDecl(self, ast, c):
        pass
    
    def visitParam(self, ast, c):
        pass
        
