# Generated from /home/thang/ppl/syntax_analysis/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u00ad\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\5\4")
        buf.write(">\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\5\7J\n\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\nX")
        buf.write("\n\n\3\13\3\13\3\13\3\13\5\13^\n\13\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\5\16j\n\16\3\17\3\17\5\17n\n")
        buf.write("\17\3\20\3\20\3\20\3\21\3\21\3\21\5\21v\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\5\24")
        buf.write("\u0084\n\24\3\25\3\25\3\25\3\25\5\25\u008a\n\25\3\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0095\n\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u009d\n\27\f\27\16")
        buf.write("\27\u00a0\13\27\3\30\3\30\3\30\3\30\3\30\5\30\u00a7\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\2\3,\32\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\2\4\3\2\b\t\3\2\24\25")
        buf.write("\2\u00a6\2\62\3\2\2\2\49\3\2\2\2\6=\3\2\2\2\b?\3\2\2\2")
        buf.write("\nC\3\2\2\2\fI\3\2\2\2\16K\3\2\2\2\20P\3\2\2\2\22W\3\2")
        buf.write("\2\2\24]\3\2\2\2\26_\3\2\2\2\30b\3\2\2\2\32i\3\2\2\2\34")
        buf.write("m\3\2\2\2\36o\3\2\2\2 u\3\2\2\2\"w\3\2\2\2${\3\2\2\2&")
        buf.write("\u0083\3\2\2\2(\u0089\3\2\2\2*\u008b\3\2\2\2,\u0094\3")
        buf.write("\2\2\2.\u00a6\3\2\2\2\60\u00a8\3\2\2\2\62\63\5\4\3\2\63")
        buf.write("\64\7\2\2\3\64\3\3\2\2\2\65\66\5\6\4\2\66\67\5\4\3\2\67")
        buf.write(":\3\2\2\28:\5\6\4\29\65\3\2\2\298\3\2\2\2:\5\3\2\2\2;")
        buf.write(">\5\b\5\2<>\5\16\b\2=;\3\2\2\2=<\3\2\2\2>\7\3\2\2\2?@")
        buf.write("\5\n\6\2@A\5\f\7\2AB\7\17\2\2B\t\3\2\2\2CD\t\2\2\2D\13")
        buf.write("\3\2\2\2EF\7\3\2\2FG\7\20\2\2GJ\5\f\7\2HJ\7\3\2\2IE\3")
        buf.write("\2\2\2IH\3\2\2\2J\r\3\2\2\2KL\5\n\6\2LM\7\3\2\2MN\5\20")
        buf.write("\t\2NO\5\30\r\2O\17\3\2\2\2PQ\7\r\2\2QR\5\22\n\2RS\7\16")
        buf.write("\2\2S\21\3\2\2\2TU\5\26\f\2UV\5\24\13\2VX\3\2\2\2WT\3")
        buf.write("\2\2\2WX\3\2\2\2X\23\3\2\2\2YZ\7\17\2\2Z[\5\26\f\2[\\")
        buf.write("\5\24\13\2\\^\3\2\2\2]Y\3\2\2\2]^\3\2\2\2^\25\3\2\2\2")
        buf.write("_`\5\n\6\2`a\5\f\7\2a\27\3\2\2\2bc\7\13\2\2cd\5\32\16")
        buf.write("\2de\7\f\2\2e\31\3\2\2\2fg\5\34\17\2gh\5\32\16\2hj\3\2")
        buf.write("\2\2if\3\2\2\2ij\3\2\2\2j\33\3\2\2\2kn\5\b\5\2ln\5\36")
        buf.write("\20\2mk\3\2\2\2ml\3\2\2\2n\35\3\2\2\2op\5 \21\2pq\7\17")
        buf.write("\2\2q\37\3\2\2\2rv\5\"\22\2sv\5$\23\2tv\5*\26\2ur\3\2")
        buf.write("\2\2us\3\2\2\2ut\3\2\2\2v!\3\2\2\2wx\7\3\2\2xy\7\21\2")
        buf.write("\2yz\5,\27\2z#\3\2\2\2{|\7\3\2\2|}\7\r\2\2}~\5&\24\2~")
        buf.write("\177\7\16\2\2\177%\3\2\2\2\u0080\u0081\5,\27\2\u0081\u0082")
        buf.write("\5(\25\2\u0082\u0084\3\2\2\2\u0083\u0080\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\'\3\2\2\2\u0085\u0086\7\20\2\2\u0086")
        buf.write("\u0087\5,\27\2\u0087\u0088\5(\25\2\u0088\u008a\3\2\2\2")
        buf.write("\u0089\u0085\3\2\2\2\u0089\u008a\3\2\2\2\u008a)\3\2\2")
        buf.write("\2\u008b\u008c\7\n\2\2\u008c\u008d\5,\27\2\u008d+\3\2")
        buf.write("\2\2\u008e\u008f\b\27\1\2\u008f\u0095\5.\30\2\u0090\u0091")
        buf.write("\5.\30\2\u0091\u0092\7\23\2\2\u0092\u0093\5.\30\2\u0093")
        buf.write("\u0095\3\2\2\2\u0094\u008e\3\2\2\2\u0094\u0090\3\2\2\2")
        buf.write("\u0095\u009e\3\2\2\2\u0096\u0097\f\5\2\2\u0097\u0098\t")
        buf.write("\3\2\2\u0098\u009d\5,\27\6\u0099\u009a\f\3\2\2\u009a\u009b")
        buf.write("\7\22\2\2\u009b\u009d\5,\27\3\u009c\u0096\3\2\2\2\u009c")
        buf.write("\u0099\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f-\3\2\2\2\u00a0\u009e\3\2\2")
        buf.write("\2\u00a1\u00a7\7\4\2\2\u00a2\u00a7\7\7\2\2\u00a3\u00a7")
        buf.write("\7\3\2\2\u00a4\u00a7\5$\23\2\u00a5\u00a7\5\60\31\2\u00a6")
        buf.write("\u00a1\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7/\3\2\2")
        buf.write("\2\u00a8\u00a9\7\r\2\2\u00a9\u00aa\5,\27\2\u00aa\u00ab")
        buf.write("\7\16\2\2\u00ab\61\3\2\2\2\209=IW]imu\u0083\u0089\u0094")
        buf.write("\u009c\u009e\u00a6")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'int'", "'float'", "'return'", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "ID", "INTLIT", "Float", "FloatEx", "FLOATLIT", 
                      "INT", "FLOAT", "RETURN", "LB", "RB", "LP", "RP", 
                      "SM", "CM", "EQ", "ADD", "SUB", "MUL", "DIV", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_manydcls = 1
    RULE_dcls = 2
    RULE_vardcls = 3
    RULE_type = 4
    RULE_idlist = 5
    RULE_funcdcls = 6
    RULE_paradcls = 7
    RULE_paralist = 8
    RULE_paratail = 9
    RULE_para = 10
    RULE_body = 11
    RULE_vardcl_stmt_list = 12
    RULE_vardcl_stmt = 13
    RULE_stmt = 14
    RULE_stmt_type = 15
    RULE_assign = 16
    RULE_call = 17
    RULE_explist = 18
    RULE_exptail = 19
    RULE_return = 20
    RULE_exp = 21
    RULE_operand = 22
    RULE_subexp = 23

    ruleNames =  [ "program", "manydcls", "dcls", "vardcls", "type", "idlist", 
                   "funcdcls", "paradcls", "paralist", "paratail", "para", 
                   "body", "vardcl_stmt_list", "vardcl_stmt", "stmt", "stmt_type", 
                   "assign", "call", "explist", "exptail", "return", "exp", 
                   "operand", "subexp" ]

    EOF = Token.EOF
    ID=1
    INTLIT=2
    Float=3
    FloatEx=4
    FLOATLIT=5
    INT=6
    FLOAT=7
    RETURN=8
    LB=9
    RB=10
    LP=11
    RP=12
    SM=13
    CM=14
    EQ=15
    ADD=16
    SUB=17
    MUL=18
    DIV=19
    WS=20
    ERROR_CHAR=21
    UNCLOSE_STRING=22
    ILLEGAL_ESCAPE=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manydcls(self):
            return self.getTypedRuleContext(MCParser.ManydclsContext,0)


        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def getRuleIndex(self):
            return MCParser.RULE_program




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.manydcls()
            self.state = 49
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ManydclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dcls(self):
            return self.getTypedRuleContext(MCParser.DclsContext,0)


        def manydcls(self):
            return self.getTypedRuleContext(MCParser.ManydclsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_manydcls




    def manydcls(self):

        localctx = MCParser.ManydclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydcls)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.dcls()
                self.state = 52
                self.manydcls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.dcls()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardcls(self):
            return self.getTypedRuleContext(MCParser.VardclsContext,0)


        def funcdcls(self):
            return self.getTypedRuleContext(MCParser.FuncdclsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_dcls




    def dcls(self):

        localctx = MCParser.DclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dcls)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.vardcls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.funcdcls()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(MCParser.TypeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(MCParser.IdlistContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_vardcls




    def vardcls(self):

        localctx = MCParser.VardclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardcls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.type()
            self.state = 62
            self.idlist()
            self.state = 63
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MCParser.FLOAT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_type




    def type(self):

        localctx = MCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not(_la==MCParser.INT or _la==MCParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def CM(self):
            return self.getToken(MCParser.CM, 0)

        def idlist(self):
            return self.getTypedRuleContext(MCParser.IdlistContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_idlist




    def idlist(self):

        localctx = MCParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idlist)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(MCParser.ID)
                self.state = 68
                self.match(MCParser.CM)
                self.state = 69
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(MCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(MCParser.TypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def paradcls(self):
            return self.getTypedRuleContext(MCParser.ParadclsContext,0)


        def body(self):
            return self.getTypedRuleContext(MCParser.BodyContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcdcls




    def funcdcls(self):

        localctx = MCParser.FuncdclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdcls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.type()
            self.state = 74
            self.match(MCParser.ID)
            self.state = 75
            self.paradcls()
            self.state = 76
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParadclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def paralist(self):
            return self.getTypedRuleContext(MCParser.ParalistContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_paradcls




    def paradcls(self):

        localctx = MCParser.ParadclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paradcls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MCParser.LP)
            self.state = 79
            self.paralist()
            self.state = 80
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self):
            return self.getTypedRuleContext(MCParser.ParaContext,0)


        def paratail(self):
            return self.getTypedRuleContext(MCParser.ParatailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_paralist




    def paralist(self):

        localctx = MCParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.INT or _la==MCParser.FLOAT:
                self.state = 82
                self.para()
                self.state = 83
                self.paratail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParatailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def para(self):
            return self.getTypedRuleContext(MCParser.ParaContext,0)


        def paratail(self):
            return self.getTypedRuleContext(MCParser.ParatailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_paratail




    def paratail(self):

        localctx = MCParser.ParatailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paratail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.SM:
                self.state = 87
                self.match(MCParser.SM)
                self.state = 88
                self.para()
                self.state = 89
                self.paratail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(MCParser.TypeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(MCParser.IdlistContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_para




    def para(self):

        localctx = MCParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.type()
            self.state = 94
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def vardcl_stmt_list(self):
            return self.getTypedRuleContext(MCParser.Vardcl_stmt_listContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_body




    def body(self):

        localctx = MCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MCParser.LB)
            self.state = 97
            self.vardcl_stmt_list()
            self.state = 98
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vardcl_stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardcl_stmt(self):
            return self.getTypedRuleContext(MCParser.Vardcl_stmtContext,0)


        def vardcl_stmt_list(self):
            return self.getTypedRuleContext(MCParser.Vardcl_stmt_listContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardcl_stmt_list




    def vardcl_stmt_list(self):

        localctx = MCParser.Vardcl_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vardcl_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.ID) | (1 << MCParser.INT) | (1 << MCParser.FLOAT) | (1 << MCParser.RETURN))) != 0):
                self.state = 100
                self.vardcl_stmt()
                self.state = 101
                self.vardcl_stmt_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vardcl_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardcls(self):
            return self.getTypedRuleContext(MCParser.VardclsContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardcl_stmt




    def vardcl_stmt(self):

        localctx = MCParser.Vardcl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_vardcl_stmt)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INT, MCParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.vardcls()
                pass
            elif token in [MCParser.ID, MCParser.RETURN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_type(self):
            return self.getTypedRuleContext(MCParser.Stmt_typeContext,0)


        def SM(self):
            return self.getToken(MCParser.SM, 0)

        def getRuleIndex(self):
            return MCParser.RULE_stmt




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.stmt_type()
            self.state = 110
            self.match(MCParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Stmt_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(MCParser.AssignContext,0)


        def call(self):
            return self.getTypedRuleContext(MCParser.CallContext,0)


        def return(self):
            return self.getTypedRuleContext(MCParser.ReturnContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt_type




    def stmt_type(self):

        localctx = MCParser.Stmt_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt_type)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.return()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def EQ(self):
            return self.getToken(MCParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_assign




    def assign(self):

        localctx = MCParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(MCParser.ID)
            self.state = 118
            self.match(MCParser.EQ)
            self.state = 119
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def explist(self):
            return self.getTypedRuleContext(MCParser.ExplistContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_call




    def call(self):

        localctx = MCParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(MCParser.ID)
            self.state = 122
            self.match(MCParser.LP)
            self.state = 123
            self.explist()
            self.state = 124
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExplistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def exptail(self):
            return self.getTypedRuleContext(MCParser.ExptailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_explist




    def explist(self):

        localctx = MCParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_explist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.LP))) != 0):
                self.state = 126
                self.exp(0)
                self.state = 127
                self.exptail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExptailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self):
            return self.getToken(MCParser.CM, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def exptail(self):
            return self.getTypedRuleContext(MCParser.ExptailContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exptail




    def exptail(self):

        localctx = MCParser.ExptailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exptail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.CM:
                self.state = 131
                self.match(MCParser.CM)
                self.state = 132
                self.exp(0)
                self.state = 133
                self.exptail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return




    def return(self):

        localctx = MCParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(MCParser.RETURN)
            self.state = 138
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.OperandContext)
            else:
                return self.getTypedRuleContext(MCParser.OperandContext,i)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 141
                self.operand()
                pass

            elif la_ == 2:
                self.state = 142
                self.operand()
                self.state = 143
                self.match(MCParser.SUB)
                self.state = 144
                self.operand()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 154
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = MCParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 148
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 149
                        _la = self._input.LA(1)
                        if not(_la==MCParser.MUL or _la==MCParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 150
                        self.exp(4)
                        pass

                    elif la_ == 2:
                        localctx = MCParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 151
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 152
                        self.match(MCParser.ADD)
                        self.state = 153
                        self.exp(1)
                        pass

             
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def call(self):
            return self.getTypedRuleContext(MCParser.CallContext,0)


        def subexp(self):
            return self.getTypedRuleContext(MCParser.SubexpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_operand




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.match(MCParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.subexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_subexp




    def subexp(self):

        localctx = MCParser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(MCParser.LP)
            self.state = 167
            self.exp(0)
            self.state = 168
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




