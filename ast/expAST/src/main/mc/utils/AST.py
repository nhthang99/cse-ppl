from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass

class Exp(ABC):
    pass

@dataclass
class Binary(Exp):
    op:str
    left:Exp
    right:Exp
    def __str__(self):
        return "Binary(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"

@dataclass
class IntLit(Exp):
    val:int
    def __str__(self):
        return "IntLit(" + str(self.val) + ")"

@dataclass
class BoolLit(Exp):
    val:bool
    def __str__(self):
        return "BoolLit(" + str(self.val) + ")"



