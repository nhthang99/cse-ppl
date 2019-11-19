import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """array[1]of int a,b;"""
        expect = "6"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_int_program(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = "5"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_float_program_1(self):
        """Simple program: int main() {} """
        input = """float b;"""
        expect = "5"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_hard_program(self):
        """Simple program: int main() {} """
        input = """int a; float b;"""
        expect = "9"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))


    
