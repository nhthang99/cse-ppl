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
    
    def test_valid_identifier4(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
abc ABC aBC __abcd 
KK __abc___________________d ABC___1 AC90 
AB thang b c
            """,

            "abc,ABC,aBC,__abcd,KK,__abc___________________d,ABC___1,AC90,AB,thang,b,c,<EOF>",
            104
        ))
    
    def test_valid_identifier5(self):
        """ Test Valid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
ac cb KL Ab Abc_abc
 ANKD______ccs abc_____________abc____________abc 
 abc__ab abc______________________c dsa
            """,
            "ac,cb,KL,Ab,Abc_abc,ANKD______ccs,abc_____________abc____________abc,abc__ab,abc______________________c,dsa,<EOF>",
            105
        ))
        
    def test_invalid_identifier(self):
        """Test Invalid Identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            r"""
id-1 id&1  
            """,
            "id,-,1,id,Error Token &",
            106
        ))

    def test_invalid_identifier2(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
123abc 123_abc 00000123_123abc
id_id 1id 321id 1321_id 89________________id
id___2 90___abc__ads___sba____abc____dba ds&a
            """,

            "123,abc,123,_abc,00000123,_123abc,id_id,1,id,321,id,1321,_id,89,________________id,id___2,90,___abc__ads___sba____abc____dba,ds,Error Token &",
            107
        ))
    
    def test_invalid_identifier3(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
thang__hip_hop thang___dep________trai
thang##thang nguyen&huu&thang id_d
            """,

            "thang__hip_hop,thang___dep________trai,thang,Error Token #",
            108
        ))

    def test_inline_comment(self):
        """Test Inline Comment"""
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// inline comment  
// This is inline comment
            """,
            "<EOF>",
            109
        ))
    
    def test_inline_comment2(self):
        """Test Inline Comment"""
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// -------------------------
// This is the comment body.
// -------------------------
            """,
            "<EOF>",
            110
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
            111
        ))
    
    def test_block_comment2(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
/* This is another way to do it, also in C.
 ** It is easier to do in editors that do not automatically indent the second
 ** through last lines of the comment one space from the first.
 ** It is also used in Holub's book, in rule 31.
 */
            """,

            "<EOF>",
            112
        ))
    
    def test_block_comment3(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
/***************************\
*                           *
* This is the comment body. *
* Variation Two.            *
*                           *
\***************************/
            """,

            "<EOF>",
            113
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
            114
        ))
    
    def test_mix_comment2(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
/* This is the style recommended by Holub for C and C++.
* It is demonstrated in ''Enough Rope'', in rule 29.
*/
// This is inline comment
//                                    
/**/
/*                          */
// This is comment

            """,

            "<EOF>",
            115
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
            116
        ))
    
    def test_invalid_comment2(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
            """,

            "Error Token #",
            117
        ))

    def test_invalid_comment3(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
<!-- begin: wsf_resource_nodes -->
<!-- end: wsf_resource_nodes -->
            """,

            "<,!,-,-,begin,Error Token :",
            118
        ))
    
    def test_invalid_comment4(self):
        """ Test Invalid Comments """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
!* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
!* All characters after an exclamation mark are considered as comments *
!* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            """,

            "!,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,!,*,All,characters,after,an,exclamation,mark,are,considered,as,comments,*,!,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,<EOF>",
            119
        ))
    
    def test_valid_int_lit(self):
        """ Test Valid Integer Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
0 1 2 3 4 123 123456789 001 0x123
            """,

            "0,1,2,3,4,123,123456789,001,0,x123,<EOF>",
            120
        ))
    
    def test_valid_int_lit2(self):
        """ Test Valid Integer Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
0001321 00000031231 000312312 
00312 0 123 132 012 1 2 3 8912 
0000000000000000000000000000000001 
09132 321 00000000000000000000000000000000000000000001
            """,

            "0001321,00000031231,000312312,00312,0,123,132,012,1,2,3,8912,0000000000000000000000000000000001,09132,321,00000000000000000000000000000000000000000001,<EOF>",
            121
        ))
    
    def test_invalid_int_lit2(self):
        """ Test Invalid Integer Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
0x131321 0X89ABC 0xffffff 
0xABC 0X2132
            """,
            "0,x131321,0,X89ABC,0,xffffff,0,xABC,0,X2132,<EOF>",
            122
        ))

    def test_bool_lit(self):
        """ Test Boolean Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
true false
            """,
            "true,false,<EOF>",
            123
        ))
    
    def test_invalid_bool_lit(self):
        """ Test Invalid Boolean Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
TRUE True TRue TRUe falSe 
falSE FAlse FAlsE
truE False FAlSE
            """,
            "TRUE,True,TRue,TRUe,falSe,falSE,FAlse,FAlsE,truE,False,FAlSE,<EOF>",
            124
        )) 

    def test_float_lit(self):
        """ Test Float Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
12.     .05     12.05 1e-5      1.5e-6  0.0005e3   2e21
            """,

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            125
        ))

    def test_float_lit2(self):
        """ Test Float Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42 1e-12 143e1
            """,

            "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,1e-12,143e1,<EOF>",
            126
        ))
    
    def test_float_leading_zero(self):
        """ Test Float Leading Zero """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
00001.1101010101000
0e-432
000000001e-542400
000313121.e00031321132
            """,

            "00001.1101010101000,0e-432,000000001e-542400,000313121.e00031321132,<EOF>",
            127
        )) 
    
    def test_invalid_float_lit(self):
        """ Test Invalid Float Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1e 123e e123 e-132 -e123 123e1
1.e3 1.e^10 
            """,

            "1,e,123,e,e123,e,-,132,-,e123,123e1,1.e3,1.,e,Error Token ^",
            128
        ))

    def test_invalid_float_lit2(self):
        """ Test Invalid Float Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
e-12 e12 1e 12e 12.05e .05e ee e01 .
""",

            "e,-,12,e12,1,e,12,e,12.05,e,.05,e,ee,e01,Error Token .",
            129
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
            130
        ))
    
    def test_invalid_string_lit(self):
        """ Test Invalid String Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
""
"string"
'string'
"string'
'string"
            """,

            ",string,Error Token '",
            131
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
            132
        ))

    def test_mix_lit2(self):
        """ Test Mix Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"multiple string"
1233 13290.31321 true12 true false12.131
.0 .112
.00000000000000000000001 00000000000000000000001 
0" "
            """,

            "multiple string,1233,13290.31321,true12,true,false12,.131,.0,.112,.00000000000000000000001,00000000000000000000001,0, ,<EOF>",
            133
        ))    

    def test_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.checkLexeme(
            r""" 
" hello lexer
            """,

            "Unclosed String:  hello lexer",
            134
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
            135
        ))

    def test_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\"abc
            """,

            r"""Unclosed String: \"abc""",
            136
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
            137
        ))
        
    def test_escape1(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \n xyz "
" abc \\n xyz "
""",

            r""" abc \n xyz , abc \\n xyz ,<EOF>""",
            138
        ))

    def test_escape2(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" hello lexer \t \b \n \""     asdf 
""",

            r""" hello lexer \t \b \n \",asdf,<EOF>""",
            139
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
            140
        ))    

    def test_illegal1(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Illegal"\a"
            """,

            r"""Illegal,Illegal Escape In String: \a""",
            141
        ))

    def test_illegal2(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \c \d "
            """,

            "Illegal Escape In String:  Hi Hi \c",
            142
        ))

    def test_illegal3(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \s\d\\f "
            """,

            "Illegal Escape In String:  Hi Hi \s",
            143
        ))  

    def test_illegal4(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \ xyz"
            """,

            "abc - xyz,Illegal Escape In String: abc \ ",
            144
        ))
    def test_illegal5(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \yyz"
            """,

            "abc - xyz,Illegal Escape In String: abc \y",
            145
        ))

    def test_illegal6(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc\mabc"
            """,

            r"""Illegal Escape In String: abc\m""",
            146
        ))

    def test_illegal7(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\a"
            """,

            r"""Illegal Escape In String: \a""",
            147
        ))
    
    def test_illegal8(self):
        """ Test Illegal String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"2.dasd1f21.da1.24@%761!809!@808132)318()^*&*13\o"
            """,

            r"""Illegal Escape In String: 2.dasd1f21.da1.24@%761!809!@808132)318()^*&*13\o""",
            148
        ))

    def test_illegal9(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r""" 
"#$%\t\n^&*$$*&^%$#\=))*768" 
            """,
            r"""Illegal Escape In String: #$%\t\n^&*$$*&^%$#\="""
            ,149
        ))

    def test_illegal10(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r""" 
"&*&(^(#!\4))"
            """,
            r"""Illegal Escape In String: &*&(^(#!\4"""
            ,150
        ))

    def test_err_tok1(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
!== != & ^ % $ # ... \
            """,

            "!=,=,!=,Error Token &",
            151
        ))        

    def test_err_tok2(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a = a ~ 1
            """,

            "a,=,a,Error Token ~",
            152
        ))

    def test_err_tok3(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
'a = 5
            """,

            "Error Token '",
            153
        ))

    def test_err_tok4(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
abc#
            """,

            "abc,Error Token #",
            154
        ))

    def test_err_tok5(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            "aAajskjkwscsVN hgSVnxx%**/*/*hg?dajkj",
            "aAajskjkwscsVN,hgSVnxx,%,*,*,/,*,/,*,hg,Error Token ?",
            155
        ))
    
    def test_err_tok6(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            "*(*)()_+_+)(()$)",
            "*,(,*,),(,),_,+,_,+,),(,(,),Error Token $",
            156
        ))
    
    def test_err_tok7(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            "hakasjdklsajdkla*()*)%!++(+)|*()",
            "hakasjdklsajdkla,*,(,),*,),%,!,+,+,(,+,),Error Token |",
            157
        ))
    
    def test_err_tok8(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            " ;,[](){}%+-=====*/@asnakncslka&*))(_h",
            ";,,,[,],(,),{,},%,+,-,==,==,=,*,/,Error Token @",
            158
        ))

    def test_keyword(self):
        """ Test Keyword """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
int float string void true false boolean if else for do while break continue return  
            """,
            "int,float,string,void,true,false,boolean,if,else,for,do,while,break,continue,return,<EOF>",
            159
        ))
    def test_invalid_keyword(self):
        """ Test Invalid Keyword """
        self.assertTrue(TestLexer.checkLexeme(
            "BOOLEAN int 1.12INTEGER sTRIng not 12and",
            "BOOLEAN,int,1.12,INTEGER,sTRIng,not,12,and,<EOF>",
            160
        ))

    def test_invalid_keyword2(self):
        """ Test Invalid Keyword """
        self.assertTrue(TestLexer.checkLexeme(
            "BOOLean Int INTeger STRING whiLE If foR Float Void VOID Break BREAK CONtinue CONTINUE True TRUE FALSE",
            "BOOLean,Int,INTeger,STRING,whiLE,If,foR,Float,Void,VOID,Break,BREAK,CONtinue,CONTINUE,True,TRUE,FALSE,<EOF>",
            161
        ))  

    def test_operator(self):
        """ Test Operator """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
+ - * / ! % || && != == <= >= > < =
            """,

            "+,-,*,/,!,%,||,&&,!=,==,<=,>=,>,<,=,<EOF>",
            162
        ))
    
    def test_invalid_operator2(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
*= /= %= ^
            """,

            "*,=,/,=,%,=,Error Token ^",
            163
        ))
    
    
    
    def test_invalid_operator(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
++ -- += -= & ^ |
            """,

            "+,+,-,-,+,=,-,=,Error Token &",
            164
        ))

    def test_invalid_operator3(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.checkLexeme(
            " !xyz 45**4290=12 a<>b+2^3 c-=d) x=y",
            "!,xyz,45,*,*,4290,=,12,a,<,>,b,+,2,Error Token ^",
            165
        ))
    
    def test_invalid_operator4(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.checkLexeme(
            "   income+=salary.12*12+month#3",
            "income,+,=,salary,.12,*,12,+,month,Error Token #",
            166
        ))

    def test_invalid_operator5(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.checkLexeme(
            "   x = (4 + 3i)(2 + 5i).i^2",
            "x,=,(,4,+,3,i,),(,2,+,5,i,),Error Token .",
            167
        ))
    
    def test_invalid_operator6(self):
        """ Test Invalid Operator """
        self.assertTrue(TestLexer.checkLexeme(
            "cost = sum((y - h(i))**2)",
            "cost,=,sum,(,(,y,-,h,(,i,),),*,*,2,),<EOF>",
            168
        ))
        
    def test_case_sensitive_keyword(self):
        """ Test Case Sensitive Keyword """
        self.assertTrue(TestLexer.checkLexeme(
            "truE TRUE tRUe",
            "truE,TRUE,tRUe,<EOF>",
            169
        )) 
    
    def test_case_sensitive_keyword2(self):
        """ Test Case Sensitive Keyword """
        self.assertTrue(TestLexer.checkLexeme(
            "false FALse FOR FOr If iF While WHILE contiNue CONTInue Break break",
            "false,FALse,FOR,FOr,If,iF,While,WHILE,contiNue,CONTInue,Break,break,<EOF>",
            170
        )) 
    
    def test_unclose_string(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.checkLexeme(
            "38n\"[#Ffs?0ED\"0.\"T`#!7n",
            "38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n",
            171
        ))
    
    def test_unclose_string2(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.checkLexeme(
            "{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1",
            "{,SRs,},Nk8U;,rA,@Y3*,oV,Unclosed String: bh1",
            172
        ))
    
    def test_unclose_string3(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.checkLexeme(
            "\"o|F&)LqX\"+>X+\"#Fft",
            "o|F&)LqX,+,>,X,+,Unclosed String: #Fft",
            173
        ))
    
    def test_unclose_string4(self):
        """ Test Unclose String """
        self.assertTrue(TestLexer.checkLexeme(
            "a+11.2+\"mam.123\" 12 \"%^&",
            "a,+,11.2,+,mam.123,12,Unclosed String: %^&",
            174
        ))
    
    def test_operator2(self):
        """ Test Operator """
        self.assertTrue(TestLexer.checkLexeme(
            "not<>=and>=mod<=-and!=or&&^^",
            "not,<,>=,and,>=,mod,<=,-,and,!=,or,&&,Error Token ^",
            175
        ))
    
    def test_operator3(self):
        """ Test Operator """
        self.assertTrue(TestLexer.checkLexeme(
            "+-*/%*()/*//$#",
            "+,-,*,/,%,*,(,),/,*,<EOF>",
            176
        ))
    
    def test_operator4(self):
        """ Test Operator """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            a + b = c
            a * b = c ** 2
            a / 2 = 5
            a % 2 = 6
            a // 2 = 0.6
            a && a == 1
            """,
            "a,+,b,=,c,a,*,b,=,c,*,*,2,a,/,2,=,5,a,%,2,=,6,a,a,&&,a,==,1,<EOF>",
            177
        ))

    def test_random1(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            // \f abc
            /* // */ acc
            a++;
            string a = "a";
            """,
            "acc,a,+,+,;,string,a,=,a,;,<EOF>",
            178
        ))
    
    def test_random2(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            for (int a ; b = 2 && c = 2; 2**2)
            break
            """,
            "for,(,int,a,;,b,=,2,&&,c,=,2,;,2,*,*,2,),break,<EOF>",
            179
        ))
    
    def test_random3(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            int a,b       ,c ,a                   b;
            float a = b (abc).12;
            str abc[] = {1,2,3};
            """,
            "int,a,,,b,,,c,,,a,b,;,float,a,=,b,(,abc,),.12,;,str,abc,[,],=,{,1,,,2,,,3,},;,<EOF>",
            180
        ))
    
    def test_random4(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            """
            "t \\\\x efg"
            """,
            "t \\\\x efg,<EOF>",
            181
        ))

    def test_random5(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            INT abc = 12;
            abc = "";
            float = 2.e2
            char = ''
            """,
            "INT,abc,=,12,;,abc,=,,;,float,=,2.e2,char,=,Error Token '",
            182
        ))
    
    def test_random6(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            """
            "t \{abcd}\\x efg"
            """,
            "Illegal Escape In String: t \{",
            183
        ))

    def test_random7(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// ],],* ae0bc not mod,return,,
{} < + Qefbe and ; of o366c false array else < > and for J4981 : <> return = for if ..
(* of break h80bb,or,bfa18 ) W6bd3,float,<*)
            """,
            "{,},<,+,Qefbe,and,;,of,o366c,false,array,else,<,>,and,for,J4981,Error Token :",
            184
        ))
    
    def test_random8(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// and,<=,return v415f ( division,and,or
+ , or b328b = <= ) G39be ? else break / * = [ Qd057 ] float[] break * >= do >
(* end , b60f1,>=,dd28e , dd3ab,string,of*)
            """,
            "+,,,or,b328b,=,<=,),G39be,Error Token ?",
            185
        ))
    
    def test_random9(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// >=,<=,for of8ae * :=,then,>=
- + false P4366 ; * , l84bc , > : flaot true [ / while Va93a boolean and integer function - , false
(* new , Wbffd,),y6349 else w7e53,(,)*)
            """,
            "-,+,false,P4366,;,*,,,l84bc,,,>,Error Token :",
            186
        ))
    
    def test_random10(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// [,<>,( k6301 with begin,],true
+ - integer N0699 + > then L09e7 >= float > >= , ] <> * eb142 > integer / while boolean procedure false
(* false for Z2262,do,G9a7c continue e46e2,+,break*)
            """,
            "+,-,integer,N0699,+,>,then,L09e7,>=,float,>,>=,,,],<,>,*,eb142,>,integer,/,while,boolean,procedure,false,(,*,false,for,Z2262,,,do,,,G9a7c,continue,e46e2,,,+,,,break,*,),<EOF>",
            187
        ))
    
    def test_random11(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            """ " """"" " " " a""",
            """Unclosed String:    a""",
            188
        ))
    
    def test_random12(self):
        """ Test Random """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
if (discriminant > 0)
    {
    // sqrt() function returns square root
        root1 = (-b+sqrt(discriminant))/(2*a);
        root2 = (-b-sqrt(discriminant))/(2*a);
        printf("root1 = %.2lf and root2 = %.2lf",root1 , root2);
    }
            """,
            "if,(,discriminant,>,0,),{,root1,=,(,-,b,+,sqrt,(,discriminant,),),/,(,2,*,a,),;,root2,=,(,-,b,-,sqrt,(,discriminant,),),/,(,2,*,a,),;,printf,(,root1 = %.2lf and root2 = %.2lf,,,root1,,,root2,),;,},<EOF>",
            189
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
            190
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
            191
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
            192
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
        , 193
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
            194
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
            195
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
            196
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
            197
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
            198
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
            199
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
            200
        ))