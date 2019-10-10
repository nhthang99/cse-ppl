import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_and_exp(self):
        input = """true && false"""
        expect = str(Binary('&&',BoolLit(True),BoolLit(False)))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    def test_or_exp(self):
        input = """true || false"""
        expect = str(Binary('||',BoolLit(True),BoolLit(False)))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_exponent_exp(self):
        input = """true ^ false"""
        expect = str(Binary('^',BoolLit(True),BoolLit(False)))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_medium_exp(self):
        input = """true && false || true"""
        expect = """Binary(||,Binary(&&,BoolLit(True),BoolLit(False)),BoolLit(True))"""
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_hard_exp(self):
        input = """true && false ^ 100"""
        expect = """Binary(^,Binary(&&,BoolLit(True),BoolLit(False)),IntLit(100))"""
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

       