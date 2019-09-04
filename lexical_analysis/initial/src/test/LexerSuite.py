import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        self.assertTrue(TestLexer.checkLexeme("abdc21","abdc21,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme("acas1","acas1,<EOF>",103))
    def test_integer(self):
        """test integers"""
    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("0.000000001 12 1.0e-12 1e-12 1. .1","0.000000001,12,1.0e-12,1e-12,1.,.1,<EOF>",104))
    def test_string(self):
        self.assertTrue(TestLexer.checkLexeme("'dads\n'","'dads\n',<EOF>",105));
