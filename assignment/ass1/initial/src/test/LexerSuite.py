import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_valid_identifier1(self):
        """Test Valid Identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            r"""
id ID _id 89id 89ID 89_id
            """,
            "id,ID,_id,89,id,89,ID,89,_id,<EOF>",
            101
        ))

    def test_valid_identifier2(self):
        """Test Valid Identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            r"""
id boolean_id float_id int_id string_id void_id 
            """,
            "id,boolean_id,float_id,int_id,string_id,void_id,<EOF>",
            102
        ))

    def test_valid_identifier3(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
_ _abc _123 _abc123 _abc_123 _123_abc
__ ____ ____123____
abc ABC aBC Abc _ABC __ABc __123ABc
hdad_adsajdk_hf__T_
            """,

            "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,hdad_adsajdk_hf__T_,<EOF>",
            103
        ))
        
    def test_invalid_identifier(self):
        """Test Invalid Identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            r"""
id-1 id&1  
            """,
            "id,-,1,id,Error Token &",
            104
        ))

    def test_invalid_id(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
123abc 123_abc 00000123_123abc
            """,

            "123,abc,123,_abc,00000123,_123abc,<EOF>",
            105
        ))

    def test_inline_comment(self):
        """Test Inline Comment"""
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// inline comment  
// This is inline comment
            """,
            "<EOF>",
            106
        ))

    def test_block_comment(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
/* Comment with multiple lines
    Hello comments
    This is block comment
*/
            """,

            "<EOF>",
            107
        ))

    def test_mix_comment(self):
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
            108
        ))

    def test_invalid_comment(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// inline comment \b \t
    is multiple lines
// inline comment
""",

            "is,multiple,lines,<EOF>",
            109
        ))
    
    def test_int_lit(self):
        """ Test Integer Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
0 1 2 3 4 123 123456789 001 0x123
            """,

            "0,1,2,3,4,123,123456789,001,0,x123,<EOF>",
            110
        ))

    def test_bool_lit(self):
        """ Test Boolean Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
true false
            """,

            "true,false,<EOF>",
            111
        ))   

    def test_float_lit(self):
        """ Test Float Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
            """,

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            112
        ))

    def test_string_lit(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
""
"String"
" "
"?"
"-"
"#"
"Mulitiple Characters"
            """,

            ",String, ,?,-,#,Mulitiple Characters,<EOF>",
            113
        ))
    
    def test_mix_lit(self):
        """ Test Mix Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
""
12 32.43 43.E12 4e-1 true "false" false "012" 1.32 1. .0
"String"
            """,

            ",12,32.43,43.E12,4e-1,true,false,false,012,1.32,1.,.0,String,<EOF>",
            114
        ))
        
    def test_invalid_float(self):
        """ Test Invalid Float Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
e-12 e12 1e 12e 12.05e .05e ee e01 .
""",

            "e,-,12,e12,1,e,12,e,12.05,e,.05,e,ee,e01,Error Token .",
            115
        ))      

    def test_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.checkLexeme(
            r""" 
" hello lexer
            """,

            "Unclosed String:  hello lexer",
            116
        ))
        
    def test_escape1(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \n xyz "
" abc \\n xyz "
""",

            r""" abc \n xyz , abc \\n xyz ,<EOF>""",
            117
        ))

    def test_escape2(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" hello lexer \t \b \n \""     asdf 
""",

            r""" hello lexer \t \b \n \",asdf,<EOF>""",
            118
        ))

    def test_escape3(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Backspace  \b"
"Formfeed   \f"
"Return     \r"
"Newline    \n"
"Tab        \t"
"Double quote       \""
"Backslash  \\ "
            """,

            r"""Backspace  \b,Formfeed   \f,Return     \r,Newline    \n,Tab        \t,Double quote       \",Backslash  \\ ,<EOF>""",
            119
        ))    

    def test_unclose_multi_lines(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Newline
    multiple lines
"           
            """,

            r"""Unclosed String: Newline""",
            120
        ))

    def test_illegal1(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Illegal"\a"
""",

            r"""Illegal,Illegal Escape In String: \a""",
            121
        ))

    def test_illegal2(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \c \d "
            """,

            "Illegal Escape In String:  Hi Hi \c",
            122
        ))

    def test_illegal3(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \s\d\\f "
            """,

            "Illegal Escape In String:  Hi Hi \s",
            123
        ))  

    def test_illegal4(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \ xyz"
            """,

            "abc - xyz,Illegal Escape In String: abc \ ",
            124
        ))
    def test_illegal5(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \yyz"
            """,

            "abc - xyz,Illegal Escape In String: abc \y",
            125
        ))

    def test_keyword(self):
        """ Test Keyword """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int float string void true false boolean if else for do while break continue return  
            """,
            "int,float,string,void,true,false,boolean,if,else,for,do,while,break,continue,return,<EOF>",
            126
        ))   

    def test_err_tok1(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
!== != & ^ % $ # ... \
            """,

            "!=,=,!=,Error Token &",
            127
        ))        

    def test_err_tok2(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a = a & 1
            """,

            "a,=,a,Error Token &",
            128
        ))

    def test_err_tok3(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
$a = 5
            """,

            "Error Token $",
            129
        ))

    def test_err_tok4(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
abc#
            """,

            "abc,Error Token #",
            130
        ))

    def test_int_leading_zero(self):
        """ Test Int Leading Zero """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1234 00003132234 00002132123
            """,

            "1234,00003132234,00002132123,<EOF>",
            131
        ))  
    
    def test_float_leading_zero2(self):
        """ Test Float Leading Zero """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
00001.1101010101000
0e-432
000000001e-542400
000313121.e00031321132
            """,

            "00001.1101010101000,0e-432,000000001e-542400,000313121.e00031321132,<EOF>",
            132
        ))    

    def test_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\"abc
            """,

            r"""Unclosed String: \"abc""",
            133
        ))
        
    def test_unclose_with_invalid_close(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
s = "string          '
"a = 4
g = 9
            """,

            r"""s,=,Unclosed String: string          '""",
            134
        ))
    
    def test_illegal6(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc\mabc"
            """,

            r"""Illegal Escape In String: abc\m""",
            135
        ))

    def test_illegal7(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\a"
            """,

            r"""Illegal Escape In String: \a""",
            136
        ))
    
    def test_illegal8(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"2.dasd1f21.da1.24@%761!809!@808132)318()^*&*13\o"
            """,

            r"""Illegal Escape In String: 2.dasd1f21.da1.24@%761!809!@808132)318()^*&*13\o""",
            137
        ))

    def test_operator(self):
        """ Test Operator """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
+ - * / ! % || && != == <= >= > < =
            """,

            "+,-,*,/,!,%,||,&&,!=,==,<=,>=,>,<,=,<EOF>",
            138
        ))
    
    def test_float(self):
        """ Test Float Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42 e-12 143e
            """,

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,e,-,12,143,e,<EOF>",
            138
        ))
        
    def test_complex_program1(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
float a, b, c;
boolean x, y, z;
int g, h, y;
float nty();
int x, y, z;
int q, w;
string a; 
    /*
        =======================================
        Comment here
        =======================================
    */
""",

            r"float,a,,,b,,,c,;,boolean,x,,,y,,,z,;,int,g,,,h,,,y,;,float,nty,(,),;,int,x,,,y,,,z,;,int,q,,,w,;,string,a,;,<EOF>",
            180
        ))

    def test_complex_program2(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int sum(int num1, int num2){
   int num3 = num1+num2;
   return num3;
}
            """,

            r"int,sum,(,int,num1,,,int,num2,),{,int,num3,=,num1,+,num2,;,return,num3,;,},<EOF>",
            181
        ))

    def test_complex_program3(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int plusFuncInt(int x, int y) {
  return x + y;
}

double plusFuncDouble(double x, double y) {
  return x + y;
}
            """,

            r"int,plusFuncInt,(,int,x,,,int,y,),{,return,x,+,y,;,},double,plusFuncDouble,(,double,x,,,double,y,),{,return,x,+,y,;,},<EOF>",
            182
        ))        

    def test_complex_program4(self):
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
        , 183
        ))

    def test_complex_program5(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int i = 0;
do
  print("\n");
  i++;
while (i < 5);
            """,

            r"int,i,=,0,;,do,print,(,\n,),;,i,+,+,;,while,(,i,<,5,),;,<EOF>",
            184
        )) 
    
    def test_complex_program6(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int time = 22;
if (time < 10)
    print("Good morning.");
if (time < 20) {
    print("Good day.");
else
    print("Good evening.");
// Outputs "Good evening."
            """,

            r"int,time,=,22,;,if,(,time,<,10,),print,(,Good morning.,),;,if,(,time,<,20,),{,print,(,Good day.,),;,else,print,(,Good evening.,),;,<EOF>",
            185
        ))
    
    def test_complex_program7(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
for (i = 0; i < 10; i = i + 1) {
  if (i == 4)
    continue;
  print("%d\n", i);
}
            """,
            r"""for,(,i,=,0,;,i,<,10,;,i,=,i,+,1,),{,if,(,i,==,4,),continue,;,print,(,%d\n,,,i,),;,},<EOF>""",
            186
        ))

    def test_complex_program8(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int main()
{
    printf("\n\n\t\tLexer - Best place to practice\n\n\n");
    int num;
    printf("\nHello world!\nWelcome to Lexer: Best place to practice\n");
    printf("\n\n\t\t\tCoding is Fun !\n\n\n");
    return 0;
}
            """,
            r"""int,main,(,),{,printf,(,\n\n\t\tLexer - Best place to practice\n\n\n,),;,int,num,;,printf,(,\nHello world!\nWelcome to Lexer: Best place to practice\n,),;,printf,(,\n\n\t\t\tCoding is Fun !\n\n\n,),;,return,0,;,},<EOF>""",
            187
        ))
    
    def test_complex_program9(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int fibonacci (int n)  
{
    if (n==0)
        return 0;
    if (n == 1)   
        return 1;
    else  
        return fibonacci(n-1)+fibonacci(n-2);
}  
            """,
            r"""int,fibonacci,(,int,n,),{,if,(,n,==,0,),return,0,;,if,(,n,==,1,),return,1,;,else,return,fibonacci,(,n,-,1,),+,fibonacci,(,n,-,2,),;,},<EOF>""",
            188
        ))

    def test_complex_program10(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int main()
{
  printf("Main function.\n");
 
  my_function();  // Calling the function
 
  printf("Back in function main.\n");
 
  return 0;
}
 
// Defining the function
void my_function()
{
  printf("Welcome to my function. Feel at home.\n");
}
            """,
            r"""int,main,(,),{,printf,(,Main function.\n,),;,my_function,(,),;,printf,(,Back in function main.\n,),;,return,0,;,},void,my_function,(,),{,printf,(,Welcome to my function. Feel at home.\n,),;,},<EOF>""",
            189
        ))
    
    def test_complex_program11(self):
        """ Test Complex Program """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int [] foo ( int b[] ) {
int a[ 1 ] ;
if ( ) return a ;
else return b ;
}
            """,
            r"""int,[,],foo,(,int,b,[,],),{,int,a,[,1,],;,if,(,),return,a,;,else,return,b,;,},<EOF>""",
            190
        ))