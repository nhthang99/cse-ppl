from abc import ABC

class Expr(ABC):
    pass

class Var(Expr):
    def __init__(self, name):
        self.name = str(name)

class Number(Expr):
    def __init__(self, num):
        self.num = float(num)
    
    def print(self):
        print(self.num)

class UpOp(Expr):
    def __init__(self, operator, arg):
        self.operator = str(operator)
        self.arg = arg

class BinOp(Expr):
    def __init__(self, operator, left, right):
        self.operator = str(operator)
        self.left = left
        self.right = right

var v = Var("x")
