import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_main_func_defined(self):
        """ Main Function Defined """
        input = Program([
                FuncDecl(Id("main"), [], VoidType(), Block([])),
                ])
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_main_func_undefined(self):
        """ Main Function Undefined """
        input = Program([
            FuncDecl(Id("main1"), [], VoidType(), Block([])),
            ])
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_var_redeclare1(self):
        """ Variable Declare"""
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            VarDecl("a", IntType()),
            VarDecl("a", IntType())
            ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_var_redeclare2(self):
        """ Variable Declare"""
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            VarDecl("a", IntType()),
            VarDecl("a", VoidType())
            ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_func_redeclare1(self):
        """ Function Declare"""
        input = Program([
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            FuncDecl(Id("main"), [], VoidType(), Block([])),
            ])
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_param_redeclare1(self):
        """ Parameter Declare"""
        input = Program([
            FuncDecl(Id("main"), [VarDecl("a", IntType()), VarDecl("a", IntType())], VoidType(), Block([])),
            ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))