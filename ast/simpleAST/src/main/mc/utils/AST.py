from abc import ABC, abstractmethod, ABCMeta
from typing import List
from Visitor import Visitor

class AST(ABC):
    pass

class Type(AST):
    pass


class VarDecl(AST):
    # typ:Type
    # id:List[str]
    def __init__(self, varType, variable):
            self.variable = variable
            self.varType = varType

    def __str__(self):
        return "VarDecl("  + str(self.varType) + ","  + str(self.variable)  + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)

class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class IntType(Type):
    def __str__(self):
        return "IntType"

    def accept(self, v, param):
        return v.visitIntType(self, param)

class FloatType(Type):
    def __str__(self):
        return "FloatType"

    def accept(self, v, param):
        return v.visitFloatType(self, param)



