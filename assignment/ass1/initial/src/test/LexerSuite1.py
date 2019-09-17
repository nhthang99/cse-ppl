import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
            '//Hello\n/*Hi\nYay*///?!@#$%^//',
            '<EOF>',101))
    def test_id(self):
        self.assertTrue(TestLexer.checkLexeme(
            "_ _1 x X aA1_",
            "_,_1,x,X,aA1_,<EOF>",102))
    def test_keyword(self):
        self.assertTrue(TestLexer.checkLexeme(
            'break continue else for if return do while',
            'break,continue,else,for,if,return,do,while,<EOF>',103))
    def test_operator(self):
        self.assertTrue(TestLexer.checkLexeme(
            '+ - * / % ! || && != == < > <= >= =',
            '+,-,*,/,%,!,||,&&,!=,==,<,>,<=,>=,=,<EOF>',104))
    def test_bracket(self):
        self.assertTrue(TestLexer.checkLexeme(
            '[ ] { } ( ) ; ,',
            '[,],{,},(,),;,,,<EOF>',105))
    def test_int(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1 2 3 4 5 6 7 8 9 0 01 10 000',
            '1,2,3,4,5,6,7,8,9,0,01,10,000,<EOF>',106))
    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1. .1 1.e1 1E-2 1.0e1 3.14',
            '1.,.1,1.e1,1E-2,1.0e1,3.14,<EOF>',107))
    def test_escape(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "Compiler" "Escape\n" "\f\r\n\t\"\\" ''',
            r'''Compiler,Escape\n,\f\r\n\t\"\\,<EOF>''',108))
    def test_unclosed_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "abc ''',
            r'''Unclosed String: abc ''',109))
    def test_illegal_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "Hi, this is illegall escape \i" ''',
            r'''Illegal Escape In String: Hi, this is illegall escape \i''' ,110))
    def test_error_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            '1>2?3',
            '1,>,2,Error Token ?',111))
    def test_mul_bracket(self):
        self.assertTrue(TestLexer.checkLexeme(
            '{{{{{{{{{int a= 10;}}}}}}}}}',
            '{,{,{,{,{,{,{,{,{,int,a,=,10,;,},},},},},},},},},<EOF>',112))
    def test_var_dcls(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''int a = (int) 12.6;''',
            'int,a,=,(,int,),12.6,;,<EOF>',113))
    def test_print_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' printf("Hello World"); ''',
            r'''printf,(,Hello World,),;,<EOF>''',114))
    def test_for_loop(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' for(int i = 0; i < n; i = i +1) {printf("");} ''',
            r'''for,(,int,i,=,0,;,i,<,n,;,i,=,i,+,1,),{,printf,(,,),;,},<EOF>''',115))
    def test_while_loop(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' float a; while(a < 10) {a = a - 1;} ''',
            r'''float,a,;,while,(,a,<,10,),{,a,=,a,-,1,;,},<EOF>''',116))
    def test_comment_in_comment(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' /* /*  */ */ ''',
            r'''*,/,<EOF>''',117))
    def test_while_hard_expr(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' while(1<2<3>4>5) {ok();} ''',
            r'''while,(,1,<,2,<,3,>,4,>,5,),{,ok,(,),;,},<EOF>''',118))
    def test_if_else(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' if(m % 2 == 0) return true;''',
            r'''if,(,m,%,2,==,0,),return,true,;,<EOF>''',119))
    def test_if_else(self):
        self.assertTrue(TestLexer.checkLexeme(
            r''' "abc \\t m ''',
            r'''== ''',120))
    
    