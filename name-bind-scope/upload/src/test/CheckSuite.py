import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_global_environment(self):
    #     """Global Environment """
    #     input = Program([
    #         VarDecl('abc', VoidType(),
    #         FuncDecl(Id("main"),[],VoidType(),Block([])),
    #         VarDecl('abc', VoidType())
    #     ])
    #     expect = "['main', 'abc']"
    #     self.assertTrue(TestChecker.test(input,expect,400))
    
    # def test_redeclared(self):
    #     """Global Environment """
    #     input = Program([
    #         FuncDecl(Id("main"),[],VoidType(),Block([])),
    #         FuncDecl(Id("main"),[],VoidType(),Block([])),
    #         FuncDecl(Id("main"),[],VoidType(),Block([])),
    #         VarDecl('abc', IntType()),
    #         VarDecl('abc', VoidType())
    #     ])
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_para(self):
        """Global Environment """
        input = Program([
            FuncDecl(Id("main"),[VarDecl('a', IntType()), VarDecl('a', IntType())],VoidType(),Block([])),
        ])
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclared_local(self):
        """Global Environment """
        input = Program([
            FuncDecl(Id("main"),
            [VarDecl('a', IntType()), VarDecl('b', IntType())]
            ,VoidType(),
            Block([
                VarDecl('c', IntType()),
                VarDecl('c', IntType())
                ])),
        ])
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_redeclared_local_para(self):
        """Global Environment """
        input = Program([
            FuncDecl(Id("main"),
            [VarDecl('a', IntType()), VarDecl('b', IntType())]
            ,VoidType(),
            Block([
                VarDecl('a', IntType()),
                VarDecl('c', IntType())
                ])),
        ])
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))
    