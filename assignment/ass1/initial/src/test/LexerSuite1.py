#Le Cong Linh
#1711948

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_ID_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a a123a","a,a123a,<EOF>",101))

    def test_ID_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_ __ _1_","_,__,_1_,<EOF>",102))

    def test_ID_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("123a123 _a_b_c__1_33_1","123,a123,_a_b_c__1_33_1,<EOF>",103))        

    def test_ID_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_abc_123_ _ABC __a1234_","_abc_123_,_ABC,__a1234_,<EOF>",104))

    def test_ID_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_abc_123. ABC_123","_abc_123,Error Token .",105))        

    def test_ID_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_123_ ABC_123 string_id void_id","_123_,ABC_123,string_id,void_id,<EOF>",106))        

    def test_ID_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("123.123ABC123","123.123,ABC123,<EOF>",107))        

    def test_ID_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("123. ABC_123 id-1 id&1","123.,ABC_123,id,-,1,id,Error Token &",108))                

    def test_ID_9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("12eabc_ 12e2abc","12,eabc_,12e2,abc,<EOF>",109))        

    def test_ID_10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc+=_abc aA?sVN","abc,+,=,_abc,aA,Error Token ?",110))  

    def test_COMMENT_11(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("/* Comment with multiple lines \\nHello comments \\nThis is block comment*/","<EOF>",111))                                

    def test_COMMENT_12(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This // is // \t\b\n #$%^&* dhsj comment */","<EOF>",112))

    def test_COMMENT_13(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This /*abc*/ is //aAsVN?!@#$%^& comment */","is,<EOF>",113))

    def test_COMMENT_14(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("//This is line comment /*tsnxy*/","<EOF>",114))                

    def test_COMMENT_15(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("/* This is comment ","/,*,This,is,comment,<EOF>",115))        

    def test_KEYWORD_16(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("for false breaks","for,false,breaks,<EOF>",116))               

    def test_KEYWORD_17(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("true TRUE tRUe","true,TRUE,tRUe,<EOF>",117))  

    def test_KEYWORD_18(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("if ifelse else int[] for()","if,ifelse,else,int,[,],for,(,),<EOF>",118))   

    def test_WRONG_TOKEN_19(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme("aA?sVN hgSVnxx%**/*/*hg","aA,Error Token ?",119))               

    def test_WRONG_TOKEN_20(self):
        """test wrong token"""
        self.assertTrue(TestLexer.checkLexeme(" ;,[](){}%+-=====*/@45678gh",";,,,[,],(,),{,},%,+,-,==,==,=,*,/,Error Token @",120))

    def test_OPERATOR_21(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("/+-*%= &&&& ||%% ","/,+,-,*,%,=,&&,&&,||,%,%,<EOF>",121))                                              

    def test_OPERATOR_22(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme("/ghjkl__+1234-*%= >>==<<==<","/,ghjkl__,+,1234,-,*,%,=,>,>=,=,<,<=,=,<,<EOF>",122))                                                      

    def test_OPERATOR_23(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme(" >>>======<<==> for(i!=6) if(a==b || c!=d) { x=y;} ",">,>,>=,==,==,=,<,<=,=,>,for,(,i,!=,6,),if,(,a,==,b,||,c,!=,d,),{,x,=,y,;,},<EOF>",123))

    def test_OPERATOR_24(self):
        """test wrong operator"""
        self.assertTrue(TestLexer.checkLexeme(" >>=<<||| >><< 45*34=12",">,>=,<,<,||,Error Token |",124)) 

    def test_OPERATOR_25(self):
        """test wrong operator"""
        self.assertTrue(TestLexer.checkLexeme(" 45*34=12 if(a==b & c==d) x=y","45,*,34,=,12,if,(,a,==,b,Error Token &",125))

    def test_OPERATOR_26(self):
        """test wrong operator"""
        self.assertTrue(TestLexer.checkLexeme(" !xyz 45**34=12 a<>b+2^3 c-=d) x=y","!,xyz,45,*,*,34,=,12,a,<,>,b,+,2,Error Token ^",126)) 

    def test_OPERATOR_27(self):
        """test wrong operator"""
        self.assertTrue(TestLexer.checkLexeme(" income+=salary.12*12+month#3","income,+,=,salary,.12,*,12,+,month,Error Token #",127))
      
    def test_OPERATOR_28(self):
        """test wrong operator"""
        self.assertTrue(TestLexer.checkLexeme("if(count?=12) count-=1;","if,(,count,Error Token ?",128))

    def test_OPERATOR_29(self):
        """test wrong operator"""
        self.assertTrue(TestLexer.checkLexeme(">>>===><<===>>++==_!-!;%%%%*/&&||||&||&*;",">,>,>=,==,>,<,<=,==,>,>,+,+,==,_,!,-,!,;,%,%,%,%,*,/,&&,||,||,Error Token &",129))        

    def test_OPERATOR_30(self):
        """test wrong operator"""
        self.assertTrue(TestLexer.checkLexeme("def test_OPERATOR_30(self): OK","def,test_OPERATOR_30,(,self,),Error Token :",130))                

    def test_SPACE_31(self):
        """test word space"""
        self.assertTrue(TestLexer.checkLexeme("               s  p  ace  ","s,p,ace,<EOF>",131))                

    def test_SPACE_32(self):
        """test word space"""
        self.assertTrue(TestLexer.checkLexeme(" \t\t\t      this    is\t\ttab  ","this,is,tab,<EOF>",132))

    def test_SPACE_33(self):
        """test word space"""
        self.assertTrue(TestLexer.checkLexeme(" this\nis\tspace   \t\ttest ","this,is,space,test,<EOF>",133))      

    def test_INTLIT_34(self):
        """test integers literal"""
        self.assertTrue(TestLexer.checkLexeme("0 1 2 3 4 123 123456789 001 x123","0,1,2,3,4,123,123456789,001,x123,<EOF>",134))                           

    def test_INTLIT_35(self):
        """test integers literal"""
        self.assertTrue(TestLexer.checkLexeme(""" 000124 0 00 0adgh0 0023 usd213 432%^& ""","000124,0,00,0,adgh0,0023,usd213,432,%,Error Token ^",135))

    def test_INTLIT_36(self):
        """test integers and operator"""
        self.assertTrue(TestLexer.checkLexeme(""" 00__00 19876567 00053_23443!0596=7 ""","00,__00,19876567,00053,_23443,!,0596,=,7,<EOF>",136))

    def test_INTLIT_37(self):
        """test integers and operator"""
        self.assertTrue(TestLexer.checkLexeme(""" 1711948 645/6567*001%21 00000076t_6598g00443 foo+=23324 ""","1711948,645,/,6567,*,001,%,21,00000076,t_6598g00443,foo,+,=,23324,<EOF>",137))

    def test_INTLIT_38(self):
        """test integers, ID and separator"""
        self.assertTrue(TestLexer.checkLexeme(""" count-=23324 && 00%0_!=002 ;;[,;450984-354];%%;,(,,______ __0sv__ {_+aSv} ""","count,-,=,23324,&&,00,%,0,_,!=,002,;,;,[,,,;,450984,-,354,],;,%,%,;,,,(,,,,,______,__0sv__,{,_,+,aSv,},<EOF>",138))        
      
    def test_BOOLLIT_39(self):
        """test boolean literal"""
        self.assertTrue(TestLexer.checkLexeme("true True FALSE false","true,True,FALSE,false,<EOF>",139))

    def test_BOOLLIT_40(self):
        """test boolean literal"""
        self.assertTrue(TestLexer.checkLexeme("TRUES True !true FaLSE fal?se truE","TRUES,True,!,true,FaLSE,fal,Error Token ?",140))

    def test_FLOATLIT_41(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.E2 1.e2 4.E-32","1.E2,1.e2,4.E-32,<EOF>",141))

    def test_FLOATLIT_42(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.2 1. .1 1e2 1.2E-2","1.2,1.,.1,1e2,1.2E-2,<EOF>",142))        

    def test_FLOATLIT_43(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.2e-2 .1E2 9.0","1.2e-2,.1E2,9.0,<EOF>",143))

    def test_FLOATLIT_44(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("12e8 0.33E-3 128e-42","12e8,0.33E-3,128e-42,<EOF>",144))        

    def test_FLOATLIT_45(self):
        """test float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42 12. .05 12.05 1e-5 1.5e-6  0.0005e3 2e21","1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.,.05,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",145))         

    def test_FLOATLIT_46(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.checkLexeme("1.2e-2 .1E2 E-12","1.2e-2,.1E2,E,-,12,<EOF>",146))

    def test_FLOATLIT_47(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.checkLexeme("143e 564E 765E. E-12","143,e,564,E,765,E,Error Token .",147))

    def test_FLOATLIT_48(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.checkLexeme("1e-12 000.E0 00.e-0 001.00 00005.e-0004 000..","1e-12,000.E0,00.e-0,001.00,00005.e-0004,000.,Error Token .",148))        

    def test_FLOATLIT_49(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.checkLexeme("e-12 e12 1e 12e 12.05e .05e ee e01","e,-,12,e12,1,e,12,e,12.05,e,.05,e,ee,e01,<EOF>",149))

    def test_FLOATLIT_50(self):
        """test invalid float literal"""
        self.assertTrue(TestLexer.checkLexeme("ee-12 eEE12 -1e 1.2e +12.05e .0099e eEe e01","ee,-,12,eEE12,-,1,e,1.2,e,+,12.05,e,.0099,e,eEe,e01,<EOF>",150))

    def test_STRLIT_51(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" "abc123aabc" ""","""abc123aabc,<EOF>""",151))

    def test_STRLIT_52(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" "//This is comment in a string" ""","""//This is comment in a string,<EOF>""",152))        

    def test_STRLIT_53(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" 123AbC874-536"count=89-79=10" ""","""123,AbC874,-,536,count=89-79=10,<EOF>""",153))

    def test_STRLIT_54(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" "" "String" " ""?""-""#""Mulitiple Characters" """,""",String, ,?,-,#,Mulitiple Characters,<EOF>""",154))

    def test_STRLIT_55(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" "" 12 32.43 43.E12 4e-1 true "false" false "012" 1.32 1. .0"String" """,""",12,32.43,43.E12,4e-1,true,false,false,012,1.32,1.,.0,String,<EOF>""",155))

    def test_STRLIT_56(self):
        """ Test escape in String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" " hello lexer \\t \\b\\n\\""     asdf  """,""" hello lexer \\t \\b\\n\\",asdf,<EOF>""",156))

    def test_STRLIT_57(self):
        """ Test escape in String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" "   Test\""escape\\" in \\tString"\" Literal\\""   __rtcvbn  ""","""   Test,escape\\" in \\tString, Literal\\",__rtcvbn,<EOF>""",157))

    def test_STRLIT_58(self):
        """ Test escape in String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" 123"   Test\"\"escape\"\"\\t\\f\\r\\"\\b\\n\" in "\\tString"\" Literal\\""   ""","""123,   Test,escape,\\t\\f\\r\\"\\b\\n,in,\\tString, Literal\\",<EOF>""",158))

    def test_STRLIT_59(self):
        """ Test escape in String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" "Backspace\\b""Formfeed\\f""Return\\r\"\"Newline\\n""Tab\\t""Double quote\\"" "Backslash\\\\ "  ""","""Backspace\\b,Formfeed\\f,Return\\r,Newline\\n,Tab\\t,Double quote\\",Backslash\\\\ ,<EOF>""",159))

    def test_STRLIT_60(self):
        """ Test mixed String Literal """
        self.assertTrue(TestLexer.checkLexeme(""" /* This is comment */"@#$%^&*@#$%^&*#$%^&?  36 dhh%^&*???\\t\\b /* This is comment */ "   ""","""@#$%^&*@#$%^&*#$%^&?  36 dhh%^&*???\\t\\b /* This is comment */ ,<EOF>""",160))

    def test_STRLIT_61(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "abc123a\\mabc" ""","""Illegal Escape In String: abc123a\\m""",161))

    def test_STRLIT_62(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" 123-4"abc123a\\b\\iasVm" ""","""123,-,4,Illegal Escape In String: abc123a\\b\\i""",162))

    def test_STRLIT_63(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "Hi, this is abc \\h\\n\\t " ""","""Illegal Escape In String: Hi, this is abc \\h""",163))

    def test_STRLIT_64(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" " abc\\s  " "vbnMHHj" ""","""Illegal Escape In String:  abc\\s""",164))

    def test_STRLIT_65(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme("""  "@#$// This is comment%^&*@#$%^&*#$\\j%^&?  36 dhh%^&*???\\t\\b /* This is comment */ "   ""","""Illegal Escape In String: @#$// This is comment%^&*@#$%^&*#$\\j""",165))

    def test_STRLIT_66(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme("""  // This is comment    "%^&*@#$%^&*#$\\n%^&?  36 dhh%^&*???\\t\\b /* This is comment */ "   ""","""<EOF>""",166))        

    def test_STRLIT_67(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" Illegal"\\b\\a" ""","""Illegal,Illegal Escape In String: \\b\\a""",167))

    def test_STRLIT_68(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" " Hi Hi \\c \\d " ""","""Illegal Escape In String:  Hi Hi \\c""",168))

    def test_STRLIT_69(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "ABC-abc+xYz \\ "" " ""","""Illegal Escape In String: ABC-abc+xYz \\ """,169))

    def test_STRLIT_70(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "  " ABC-abc+xYz "\\"\\ " ""","""  ,ABC,-,abc,+,xYz,Illegal Escape In String: \\"\\ """,170))

    def test_STRLIT_71(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "     " "" "" "\\t\\b\\g" ""","""     ,,,Illegal Escape In String: \\t\\b\\g""",171))

    def test_STRLIT_72(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "     " "" "" "     " ""","""     ,,,     ,<EOF>""",172))

    def test_STRLIT_73(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "abc - xYz""count=123\\456" ""","""abc - xYz,Illegal Escape In String: count=123\\4""",173))

    def test_STRLIT_74(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "X=004*0875.E-2\\087.02" ""","""Illegal Escape In String: X=004*0875.E-2\\0""",174))

    def test_STRLIT_75(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "#$%\\t\\n^&*((*&^%$#\\?))*768" ""","""Illegal Escape In String: #$%\\t\\n^&*((*&^%$#\\?""",175))

    def test_STRLIT_76(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "#$342%\\t\\#^&*((*&^%$#\\"))*768" ""","""Illegal Escape In String: #$342%\\t\\#""",176))

    def test_STRLIT_77(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "..... "3.05 ""","""..... ,3.05,<EOF>""",177))

    def test_STRLIT_78(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "" " " "__ " """,""", ,__ ,<EOF>""",178))

    def test_STRLIT_79(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" !== != "&"& "^ % $ # ... \\b" ""","""!=,=,!=,&,Error Token &""",179))        

    def test_STRLIT_80(self):
        """ Test Illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "   *&^\\bjgd\\[76] " ""","""Illegal Escape In String:    *&^\\bjgd\\[""",180))        

    def test_STRLIT_81(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "Test Unclosed String ""","""Unclosed String: Test Unclosed String """,181))

    def test_STRLIT_82(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" Test Unclosed String" ""","""Test,Unclosed,String,Unclosed String:  """,182))

    def test_STRLIT_83(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" " " "" " """,""" ,,Unclosed String:  """,183))        

    def test_STRLIT_84(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "kfghj "aaaa "***" "hello!@#$%^ ""","""kfghj ,aaaa,***,Unclosed String: hello!@#$%^ """,184))

    def test_STRLIT_85(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "(*&^%$#@#$%^)     ""","""Unclosed String: (*&^%$#@#$%^)     """,185))

    def test_STRLIT_86(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "\\"abc\\" ""","""Unclosed String: \\"abc\\" """,186))

    def test_STRLIT_87(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" string="string ""","""string,=,Unclosed String: string """,187))

    def test_STRLIT_88(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" int a=9;"string\"\"char\\" ""","""int,a,=,9,;,string,Unclosed String: char\\" """,188))

    def test_STRLIT_89(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "%^&*(\\t||b6783\\")&* ""","""Unclosed String: %^&*(\\t||b6783\\")&* """,189))

    def test_STRLIT_90(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "%^&*(\\t"|"|b6783\\")&* ""","""%^&*(\\t,Error Token |""",190))

    def test_STRLIT_91(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "%^&*(\n"|"|b6783\\")&* ""","""Unclosed String: %^&*(""",191))        

    def test_STRLIT_92(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "%^&*(\\n\\"|\\"|b6783\\")&*""","""Unclosed String: %^&*(\\n\\"|\\"|b6783\\")&*""",192))

    def test_STRLIT_93(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "\\"" "''''''""","""\\",Unclosed String: ''''''""",193))

    def test_STRLIT_94(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "Newline\n ""","""Unclosed String: Newline""",194))

    def test_STRLIT_95(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "Newline\\n ""","""Unclosed String: Newline\\n """,195))        

    def test_STRLIT_96(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "|||&&&&&\n****&^%" ""","""Unclosed String: |||&&&&&""",196))

    def test_STRLIT_97(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "Line1\\n Line2 \n****&^%" ""","""Unclosed String: Line1\\n Line2 """,197))        

    def test_STRLIT_98(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "Test \n Unclosed String" ""","""Unclosed String: Test """,198)) 

    def test_STRLIT_99(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" "Test Unclosed String\\" \n" ""","""Unclosed String: Test Unclosed String\\" """,199))

    def test_STRLIT_100(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(""" 123.e-13-546+ABC"\n" " " ""","""123.e-13,-,546,+,ABC,Unclosed String: """,200)) 