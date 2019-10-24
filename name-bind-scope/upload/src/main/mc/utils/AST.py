from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List
from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class Type(AST):
    __metaclass__ = ABCMeta
    pass

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

class BoolType(Type):
    def __str__(self):
        return "BoolType"

    def accept(self, v, param):
        return v.visitBoolType(self, param)

class StringType(Type):
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return v.visitStringType(self, param)

class VoidType(Type):
    def __str__(self):
        return "VoidType"

    def accept(self, v, param):
        return v.visitVoidType(self, param)

@dataclass
class ArrayType(Type):
    dimen:int
    eleType:Type
        
    def __str__(self):
        return "ArrayType(" + str(self.eleType) + "," + str(self.dimen) + ")"

    def accept(self, v, param):
        return v.visitArrayType(self, param)

@dataclass
class ArrayPointerType(Type):
    eleType:Type
        
    def __str__(self):
        return "ArrayTypePointer(" + str(self.eleType) + ")"

    def accept(self, v, param):
        return v.visitArrayPointerType(self, param)

class BlockMember(AST):
    __metaclass__ = ABCMeta
    pass

class Stmt(BlockMember):
    __metaclass__ = ABCMeta
    pass

class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass

class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

@dataclass
class Id(LHS):
    name : str

    def __str__(self):
        return  "Id(" + self.name + ")" 

    def accept(self, v, param):
        return v.visitId(self, param)

@dataclass
class ArrayCell(LHS):
    arr:Expr
    idx:Expr

    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

    def accept(self, v, param):
        return v.visitArrayCell(self, param)

@dataclass
class BinaryOp(Expr):
    op:str
    left:Expr
    right:Expr

    def __str__(self):
        return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)
@dataclass
class UnaryOp(Expr):
    op:str
    body:Expr

    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

    def accept(self, v, param):
        return v.visitUnaryOp(self, param)

@dataclass
class CallExpr(Expr):
    method:Id
    param:List[Expr]

    def __str__(self):
        return "CallExpr(" + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

    def accept(self, v, param):
        return v.visitCallExpr(self, param)

class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

@dataclass
class IntLiteral(Literal):
    value:int

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

@dataclass
class FloatLiteral(Literal):
    value:float

    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)
@dataclass
class StringLiteral(Literal):
    value:str

    def __str__(self):
        return "StringLiteral(" + self.value + ")"

    def accept(self, v, param):
        return v.visitStringLiteral(self, param)
@dataclass
class BooleanLiteral(Literal):
    value:bool

    def __str__(self):
        return "BooleanLiteral(" + str(self.value).lower() + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)

@dataclass
class Block(Stmt):
    member:List[BlockMember]

    def __str__(self):
        return "Block([" + ','.join(str(i) for i in self.member)  + "])"

    def accept(self, v, param):
        return v.visitBlock(self, param)

@dataclass
class If(Stmt):
    expr:Expr
    thenStmt:Stmt
    elseStmt:Stmt

    def __str__(self):
        return "If(" + str(self.expr) + "," + str(self.thenStmt) + ("" if (self.elseStmt is None) else "," + str(self.elseStmt)) + ")"

    def accept(self, v, param):
        return v.visitIf(self, param)

@dataclass
class For(Stmt):
    expr1:Expr
    expr2:Expr
    expr3:Expr
    loop:Stmt

    def __str__(self):
        return "For(" + str(self.expr1) + ";" + str(self.expr2) + ";" + str(self.expr3) + ";" + str(self.loop) + ")"

    def accept(self, v, param):
        return v.visitFor(self, param)

class Break(Stmt):
    def __str__(self):
        return "Break()"

    def accept(self, v, param):
        return v.visitBreak(self, param)
    
class Continue(Stmt):
    def __str__(self):
        return "Continue()"

    def accept(self, v, param):
        return v.visitContinue(self, param)

@dataclass
class Return(Stmt):
    expr:Expr

    def __str__(self):
        return "Return(" + ("" if (self.expr is None) else str(self.expr)) + ")"

    def accept(self, v, param):
        return v.visitReturn(self, param)

@dataclass
class Dowhile(Stmt):
    sl:List[Stmt]
    exp: Expr

    def __str__(self):
        return "Dowhile([" + ','.join(str(i) for i in self.sl) + "]," + str(self.exp) + ")"

    def accept(self, v, param):
        return v.visitDowhile(self, param)

@dataclass    
class VarDecl(Decl,BlockMember):
    variable : str
    varType : Type

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)

@dataclass
class FuncDecl(Decl):
    name: Id
    param: List[VarDecl]
    returnType: Type
    body: Block

    def __str__(self):
        return "FuncDecl(" + str(self.name) + ",[" +  ','.join(str(i) for i in self.param) + "]," + str(self.returnType) + "," + str(self.body) + ")"
    
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)

@dataclass
class Program(AST):
    decl : List[Decl]

    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)


