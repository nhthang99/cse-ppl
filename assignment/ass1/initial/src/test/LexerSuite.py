import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme("aAsVN","aAsVN,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",104))
    def test_float(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("1.0 1. .1","1.0,1.,.1,<EOF>",105))
        self.assertTrue(TestLexer.checkLexeme("1e10 1e-10 1.9e1 1.e1 .5e1","1e10,1e-10,1.9e1,1.e1,.5e1,<EOF>",106))
