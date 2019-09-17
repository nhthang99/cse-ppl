import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a?","a,Error Token ?",101))

    def test_4_inline_comment(self):
        """ Test Inline Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// This is a line comment
""",

            "<EOF>",
            104
        ))
    def test_1_valid_lowercase_keywords(self):
        """ Test Valid Lowercase Keywords """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
function procedure
begin end
true false
if then else
for while with do to downto
return break continue
integer string real boolean
array
var of
and then
or else
and         then
or          else
div mod not and or
""",
            r"function,procedure,begin,end,true,false,if,then,else,for,while,with,do,to,downto,return,break,continue,integer,string,real,boolean,array,var,of,and,then,or,else,and,then,or,else,div,mod,not,and,or,<EOF>",
            101
        ))
        

    def test_2_valid_keywords(self):
        """ Test Valid Keywords """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
FuNctiOn prOceDure
Begin END
True FalSE
IF thEn ELSE
fOR While with DO To downTo
RETURN break COntiNue
integer string REAL BOOLean
ARRAY
VAR Of
anD Then
or eLse
AND             THeN   OR   elSE
dIV mOd NOT and OR
""",

            "FuNctiOn,prOceDure,Begin,END,True,FalSE,IF,thEn,ELSE,fOR,While,with,DO,To,downTo,RETURN,break,COntiNue,integer,string,REAL,BOOLean,ARRAY,VAR,Of,anD,Then,or,eLse,AND,THeN,OR,elSE,dIV,mOd,NOT,and,OR,<EOF>",
            102
        ))
    def test_3_valid_specific_characters(self):
        """ Test Specific Characters """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
+ - * / == <= >= <> = < >
( ) [ ] ; ,  ,
""",

            "+,-,*,/,==,<=,>=,<,>,=,<,>,(,),[,],;,,,,,<EOF>",
            103
        ))
    def test_5_block_comment(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
/* Comment with multiple lines
    Hello comments
*/
""",

            "<EOF>",
            105
        ))
        

    def test_7_mix_comment(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
/* This is a block comment */
// This is a line comment
/* Comment with multiple lines
    Hello comments
*/
/*
    Comment multiple lines
*/
/* nest comments
    // inline comment 
// inline comment
*/
""",

            "<EOF>",
            107
        ))
    def test_8_int_lit(self):
        """ Test Integer Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
0 1 2 3 4 123 123456789
""",

            "0,1,2,3,4,123,123456789,<EOF>",
            108
        ))
        

    def test_9_real_lit(self):
        """ Test Real Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
""",

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            109
        ))
    def test_10_string_lit(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
""      "A"     
"Mulitiple Characters"
""",

            ',A,Mulitiple Characters,<EOF>',
            110
        ))
        

    def test_11_id(self):
        """ Test Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
_ _abc _123 _abc123 _abc_123 _123_abc
__ ____ ____123____
abc ABC aBC Abc _ABC __ABc __123ABc
h98f394__VWT_b5_VT_YGU87udhf__T_
""",

            "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,h98f394__VWT_b5_VT_YGU87udhf__T_,<EOF>",
            111
        ))
    def test_12_invalid_id(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
123abc 123_abc 00000123_123abc
""",

            "123,abc,123,_abc,00000123,_123abc,<EOF>",
            112
        ))
        

    def test_13_invalid_comment(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// inline comment but
    is multiple lines
""",

            "is,multiple,lines,<EOF>",
            113
        ))
    def test_14_invalid_real(self):
        """ Test Invalid Real Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
e-12 e12 . 1e 12e 12.05e .05e ee e01
""",

            "e,-,12,e12,Error Token .",
            114
        ))      

    def test_16_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.checkLexeme(
            r"""  " hello lexer """,

            "Unclosed String:  hello lexer ",
            116
        ))
    def test_17_unclose_with_endline(self):
        """ Test Unclose String with endline """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abcxyz
""",

            r"""Unclosed String:  abcxyz""",
            117
        ))
        

    def test_18_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \n xyz "
" abc \\n xyz "
""",

            r''' abc \n xyz , abc \\n xyz ,<EOF>''',
            118
        ))
    def test_19_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" hello lexer \t "     asdf 
""",

            r' hello lexer \t ,asdf,<EOF>',
            119
        ))
        

    def test_20_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Backspace  \b"
""",

            r'Backspace  \b,<EOF>',
            120
        ))
    def test_21_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Formfeed   \f"
""",

            r'Formfeed   \f,<EOF>',
            121
        ))
        

    def test_22_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Return     \r"
""",

            r'''Return     \r,<EOF>''',
            122
        ))
    def test_23_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Newline    \n"
""",

            r'''Newline    \n,<EOF>''',
            123
        ))
    def test_25_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Tab        \t"
""",

            r'Tab        \t,<EOF>',
            125
        ))
        

    def test_26_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Backslash  \\ "
""",

            r"Backslash  \\ ,<EOF>",
            126
        ))
        

    def test_24_unclose_multi_lines(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Newline
    multiple lines
"           """,

            r'''Unclosed String: Newline''',
            124
        ))
    def test_27_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Illegal"\a"
""",

            r"""Illegal,Illegal Escape In String: \a""",
            127
        ))
        

    def test_28_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \c \d "
""",

            "Illegal Escape In String:  Hi Hi \c",
            128
        ))
    def test_29_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \m\n\c\s\d\\f "
""",

            "Illegal Escape In String:  Hi Hi \m",
            129
        ))
        

    def test_30_nevermind(self):
        """ Test Nevermind :) """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" asdf ` asdf"
""",

            " asdf ` asdf,<EOF>",
            130
        ))
    def test_31_err_str(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc ' xyz "
""",

            " abc ' xyz ,<EOF>",
            131
        ))
        

    def test_32_escape_doublequote(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \" xyz "
""",

            r" abc \" xyz ,<EOF>",
            132
        ))
    def test_33_escape_doublequote(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \" xyz " ghi
""",

            r" abc \" xyz ,ghi,<EOF>",
            133
        ))
    def test_35_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
!== != & ^ % $ # ... \
""",

            "!=,=,!=,Error Token &",
            135
        ))
        

    def test_36_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
if a != b then
""",

            "if,a,!=,b,then,<EOF>",
            136
        ))
        

    def test_34_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc" 123 __123 "abc xyz"
" abc\m "
""",

            "abc,123,__123,abc xyz,Illegal Escape In String:  abc\m",
            134
        ))
    def test_37_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a = a & 1
""",

            "a,=,a,Error Token &",
            137
        ))
        

    def test_38_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
xyz
$a = 5
""",

            "xyz,Error Token $",
            138
        ))
    def test_39_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
#define for 1
""",

            "Error Token #",
            139
        ))
        

    def test_40_num_leading_0(self):
        """ Test Number leading 0 """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1234 0000001234 0000043123
""",

            "1234,0000001234,0000043123,<EOF>",
            140
        ))  
    def test_41_num_leading_0(self):
        """ Test Real Leading 0 """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
00001.1111000000
0e-4
000000001e-40000
""",

            "00001.1111000000,0e-4,000000001e-40000,<EOF>",
            141
        ))
        

    def test_42_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            142
        ))
    def test_43_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            143
        ))
        

    def test_44_escape_backsplash_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc \\ xyz"
""",

            r"abc \\ xyz,<EOF>",
            144
        ))
    def test_45_escape_backsplash_trim(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\\"
""",

            r'''\\,<EOF>''',
            145
        ))
        

    def test_46_escape_backsplash_tail_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\\ "
""",

            r"\\ ,<EOF>",
            146
        ))
    def test_47_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\"
""",

            r"""Unclosed String: \"""",
            147
        ))
        

    def test_48_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\""
""",

            r"""\",<EOF>""",
            148
        ))
    def test_49_unclose_with_invalid_close(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
s = "string           
"a = 4
g = 9
""",

            r'''s,=,Unclosed String: string           ''',
            149
        ))
        

    def test_50_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
float a, b, c;
boolean x, y, z;
int g, h, y;
float function nty();
int x, y, z;
begin
    readLine();
    // This is readLine()
    fs = readStdin();
    
    with int i; do begin
        for i = 4 downto -5 do h = 6;
        if i > 6 then return 0;
    end
    return 1;
end
int q, w;
string a;
begin 
    /*
        =======================================
        Comment here
        =======================================
    */
end
""",

            r"float,a,,,b,,,c,;,boolean,x,,,y,,,z,;,int,g,,,h,,,y,;,float,function,nty,(,),;,int,x,,,y,,,z,;,begin,readLine,(,),;,fs,=,readStdin,(,),;,with,int,i,;,do,begin,for,i,=,4,downto,-,5,do,h,=,6,;,if,i,>,6,then,return,0,;,end,return,1,;,end,int,q,,,w,;,string,a,;,begin,end,<EOF>",
            150
        ))
    def test_51_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
procedure foo();
begin
    while i do begin
        ok()
    end
end
""",

            r"procedure,foo,(,),;,begin,while,i,do,begin,ok,(,),end,end,<EOF>",
            151
        ))
        

    def test_52_unclose_eof(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
s = "abc""",

            r"s,=,Unclosed String: abc",
            152
        ))
    def test_53_unclose_newline(self):
        """ Test Unclosed """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
s = "abc                   ;
a = "xyz"
""",

            r"""s,=,Unclosed String: abc                   ;""",
            153
        ))
        

    def test_54_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
procedure foo();
begin
    while 1<2<3<4<5 do ok();
end
""",

            r"procedure,foo,(,),;,begin,while,1,<,2,<,3,<,4,<,5,do,ok,(,),;,end,<EOF>",
            154
        ))
    def test_55_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
procedure foo();
begin
    with sring a; do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,sring,a,;,do,ok,(,),;,end,<EOF>",
            155
        ))
        

    def test_56_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
procedure foo();
begin
    with string a,b,c,d; int f do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,string,a,,,b,,,c,,,d,;,int,f,do,ok,(,),;,end,<EOF>",
            156
        ))
    def test_as(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int main()
{
  int x;
 
  printf("Input an integer\n");
  scanf("%d", &x); // %d is used for an integer
 
  printf("The integer is: %d\n", x);
 
  return 0;
}
            """
        , r"int,main,(,),{,int,x,;,printf,(,Input an integer\n,),;,scanf,(,%d,,,Error Token &"
        , 157
        ))