# update: 16/07/2018
from abc import ABC
from dataclasses import dataclass
import AST

class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        return "Function"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass
@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str # name of identifier
    
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n
@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str # name of identifier
    
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n

@dataclass
class TypeMismatchInExpression(StaticError):
    exp: AST.Expr

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)
@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: AST.Stmt
    
    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)

@dataclass
class FunctionNotReturn(StaticError):
    m: str # the name of the function

    def __str__(self):
        return "Function "+ self.m + " Not Return "

class BreakNotInLoop(StaticError):
    def __str__(self):
        return "Break Not In Loop"

class ContinueNotInLoop(StaticError):
    def __str__(self):
        return "Continue Not In Loop"

class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"

@dataclass
class UnreachableFunction(StaticError):
    m: str  # the name of the unreachable function
    def __str__(self):
        return "Unreachable Function: "+ self.m 

@dataclass
class NotLeftValue(StaticError):
    exp: AST.Expr  
    def __str__(self):
        return "Not Left Value: "+ str(self.exp)

@dataclass
class UnreachableStatement(StaticError):
    stmt: AST.Stmt   
    def __str__(self):
        return "Unreachable Statement: "+ str(self.stmt)

@dataclass
class IndexOutOfRange(StaticError):
    exp: AST.ArrayCell
    def __str__(self):
        return "Index Out Of Range: "+ str(self.exp) 

@dataclass
class UninitializedVariable(StaticError):
    var: str # the name of the uninitialzed variable
    def __str__(self):
        return "Uninitialized Variable: "+ self.var 