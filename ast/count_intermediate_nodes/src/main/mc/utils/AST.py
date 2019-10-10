from abc import ABC, abstractmethod, ABCMeta
from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Program(AST):
    #decl:list(Decl)
    def __init__(self, decl):
        self.decl = decl
    
    def __str__(self):
        return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    
    def accept(self, v: Visitor, param):
        return v.visitProgram(self, param)

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class BlockMember(AST):
    __metaclass__ = ABCMeta
    pass
    
class VarDecl(Decl,BlockMember):
    #variable:string
    #varType: Type
    def __init__(self, variable, varType):
        self.variable = variable
        self.varType = varType

    def __str__(self):
        return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"

    def accept(self, v, param):
        return v.visitVarDecl(self, param)

class FuncDecl(Decl):
    #name: Id
    #param: list(VarDecl)
    #returnType: Type
    #body: Block
    def __init__(self, name, param, returnType, body):
        self.name = name
        self.param = param
        self.returnType = returnType
        self.body = body

    def __str__(self):
        return "FuncDecl(" + str(self.name) + ",[" +  ','.join(str(i) for i in self.param) + "]," + str(self.returnType) + "," + str(self.body) + ")"
    
    def accept(self, v, param):
        return v.visitFuncDecl(self, param)

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

class ArrayType(Type):
    #dimen:int
    #eleType:Type
    def __init__(self, dimen, eleType):
        self.dimen = dimen
        self.eleType = eleType
        
    def __str__(self):
        return "ArrayType(" + str(self.eleType) + "," + str(self.dimen) + ")"

    def accept(self, v, param):
        return v.visitArrayType(self, param)

class ArrayPointerType(Type):
    #eleType:Type
    def __init__(self, eleType):
        self.eleType = eleType
        
    def __str__(self):
        return "ArrayTypePointer(" + str(self.eleType) + ")"

    def accept(self, v, param):
        return v.visitArrayPointerType(self, param)

class Stmt(BlockMember):
    __metaclass__ = ABCMeta
    pass

class Expr(Stmt):
    __metaclass__ = ABCMeta
    pass

class BinaryOp(Expr):
    #op:string
    #left:Expr
    #right:Expr
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitBinaryOp(self, param)

class UnaryOp(Expr):
    #op:string
    #body:Expr
    def __init__(self, op, body):
        self.op = op
        self.body = body

    def __str__(self):
        return "UnaryOp(" + self.op + "," + str(self.body) + ")"

    def accept(self, v, param):
        return v.visitUnaryOp(self, param)

class CallExpr(Expr):
    #method:Id
    #param:list(Expr)
    def __init__(self, method, param):
        self.method = method
        self.param = param

    def __str__(self):
        return "CallExpr(" + str(self.method) + ",[" +  ','.join(str(i) for i in self.param) + "])"

    def accept(self, v, param):
        return v.visitCallExpr(self, param)



class LHS(Expr):
    __metaclass__ = ABCMeta
    pass

class Id(LHS):
    #name:string
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return  "Id(" + self.name + ")" 

    def accept(self, v, param):
        return v.visitId(self, param)

class ArrayCell(LHS):
    #arr:Expr
    #idx:Expr
    def __init__(self, arr, idx):
        self.arr = arr
        self.idx = idx

    def __str__(self):
        return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"

    def accept(self, v, param):
        return v.visitArrayCell(self, param)

class Block(Stmt):
    #decl:list(BlockMember)
    def __init__(self, member):
        self.member = member

    def __str__(self):
        return "Block([" + ','.join(str(i) for i in self.member)  + "])"

    def accept(self, v, param):
        return v.visitBlock(self, param)

class If(Stmt):
    #expr:Expr
    #thenStmt:Stmt
    #elseStmt:Stmt
    def __init__(self, expr, thenStmt, elseStmt=None):
        self.expr = expr
        self.thenStmt = thenStmt
        self.elseStmt = elseStmt

    def __str__(self):
        return "If(" + str(self.expr) + "," + str(self.thenStmt) + ("" if (self.elseStmt is None) else "," + str(self.elseStmt)) + ")"

    def accept(self, v, param):
        return v.visitIf(self, param)

class For(Stmt):
    #expr1,expr2,expr3:Expr
    #loop:Stmt
    def __init__(self, expr1, expr2, expr3, loop):
        self.expr1 = expr1
        self.expr2 = expr2
        self.expr3 = expr3
        self.loop = loop

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

class Return(Stmt):
    #expr:Expr
    def __init__(self, expr = None):
        self.expr = expr

    def __str__(self):
        return "Return(" + ("" if (self.expr is None) else str(self.expr)) + ")"

    def accept(self, v, param):
        return v.visitReturn(self, param)

class Dowhile(Stmt):
    #sl:list(Stmt)
    #exp: Expr
    def __init__(self, sl, exp):
        self.sl = sl
        self.exp = exp

    def __str__(self):
        return "Dowhile([" + ','.join(str(i) for i in self.sl) + "]," + str(self.exp) + ")"

    def accept(self, v, param):
        return v.visitDowhile(self, param)


class Literal(Expr):
    __metaclass__ = ABCMeta
    pass

class IntLiteral(Literal):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class FloatLiteral(Literal):
    #value:float
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "FloatLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitFloatLiteral(self, param)

class StringLiteral(Literal):
    #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "StringLiteral(" + self.value + ")"

    def accept(self, v, param):
        return v.visitStringLiteral(self, param)

class BooleanLiteral(Literal):
    #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value).lower() + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)
