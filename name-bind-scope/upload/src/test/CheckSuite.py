import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        """Simple program: int main() {} """
        input = Program([
            FuncDecl(Id("main"),[],VoidType(),Block([]))
        ])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))
    