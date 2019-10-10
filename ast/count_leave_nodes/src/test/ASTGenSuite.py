import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """array[1]of int a,b;"""
        expect = "11"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_int_program(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = "4"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_float_program_1(self):
        """Simple program: int main() {} """
        input = """float b;"""
        expect = "4"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_hard_program(self):
        """Simple program: int main() {} """
        input = """int a; float b;"""
        expect = "7"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_all_program(self):
        """Simple program: int main() {} """
        input = """array[1]of int a,b; int c; float d;"""
        expect = "17"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))



    
