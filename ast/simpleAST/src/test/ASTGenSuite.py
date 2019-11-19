import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_int_program(self):
        input = """int a,b"""
        expect = """Program([VarDecl(IntType,['a', 'b'])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    
    def test_float_program(self):
        input = """float a,b"""
        expect = """Program([VarDecl(FloatType,['a', 'b'])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_medium_program(self):
        input = """int a float b,c"""
        expect = """Program([VarDecl(IntType,['a']),VarDecl(FloatType,['b', 'c'])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_array_program(self):
        input = """int a, c float b"""
        expect = """Program([VarDecl(IntType,['a', 'c']),VarDecl(FloatType,['b'])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_hard_program(self):
        input = """int a, c float b int d, e float f"""
        expect = """Program([VarDecl(IntType,['a', 'c']),VarDecl(FloatType,['b']),VarDecl(IntType,['d', 'e']),VarDecl(FloatType,['f'])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
