from abc import ABC
from dataclasses import dataclass

class Expr(ABC):
    pass

@dataclass
class Var(Expr):
    def __init__(self, name):
        self.name = str(name)

@dataclass
class Number(Expr):
    def __init__(self, num):
        self.num = float(num)
    
    def print(self):
        print(self.num)

@dataclass
class UpOp(Expr):
    def __init__(self, operator, arg):
        self.operator = str(operator)
        self.arg = arg

@dataclass
class BinOp(Expr):
    def __init__(self, operator, left, right):
        self.operator = str(operator)
        self.left = left
        self.right = right

var v = Var("x")
