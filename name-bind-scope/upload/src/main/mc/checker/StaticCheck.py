
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

    global_envi = []
            
    
    def __init__(self,ast):
        # print(ast)
        #print(ast)
        #print()
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

# Problem 1
    # def visitProgram(self, ast, c):
    #     return [self.visit(x, c) for x in ast.decl]

    # def visitFuncDecl(self, ast, c):
    #     return ast.name.name
    
    # def visitVarDecl(self, ast, c):
    #     return ast.variable

# Problem 2
    # def visitProgram(self, ast, c):
    #     for decl in ast.decl:
    #         c.append(self.visit(decl, c))
    #     return c

    # def visitFuncDecl(self, ast, c):
    #     if ast.name.name in c:
    #         raise Redeclared(Function(), ast.name.name)
    #     else:
    #         return ast.name.name
    
    # def visitVarDecl(self, ast, c):
    #     if ast.variable in c:
    #         raise Redeclared(Variable(), ast.variable)
    #     else:
    #         return ast.variable
    
# Problem 3
    def visitProgram(self, ast, c):
        for decl in ast.decl:
            c.append(self.visit(decl, c))
        return c

    def visitFuncDecl(self, ast, c):
        # c: decl list
        if ast.name.name in c:
            raise Redeclared(Function(), ast.name.name)
        else:
            para = []
            for x in ast.param:
                if x.variable in para:
                    raise Redeclared(Parameter(), x.variable)
                else:
                    para.append(self.visit(x, para))
            body = self.visit(ast.body, para)
            return ast.name.name

    def visitBlock(self, ast, c):
        for x in ast.member:
            c.append(self.visit(x, c))
    
    def visitVarDecl(self, ast, c):
        if ast.variable in c:
            raise Redeclared(Variable(), ast.variable)
        else:
            return ast.variable

