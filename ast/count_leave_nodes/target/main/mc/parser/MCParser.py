# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5\"\n\5\3\6\3\6\3\6\7\6\'\n\6")
        buf.write("\f\6\16\6*\13\6\3\6\2\2\7\2\4\6\b\n\2\2\2*\2\f\3\2\2\2")
        buf.write("\4\23\3\2\2\2\6\25\3\2\2\2\b!\3\2\2\2\n#\3\2\2\2\f\r\5")
        buf.write("\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17\20\5\6\4\2\20\21\5")
        buf.write("\4\3\2\21\24\3\2\2\2\22\24\5\6\4\2\23\17\3\2\2\2\23\22")
        buf.write("\3\2\2\2\24\5\3\2\2\2\25\26\5\b\5\2\26\27\5\n\6\2\27\30")
        buf.write("\7\f\2\2\30\7\3\2\2\2\31\"\7\5\2\2\32\"\7\6\2\2\33\34")
        buf.write("\7\3\2\2\34\35\7\t\2\2\35\36\7\b\2\2\36\37\7\n\2\2\37")
        buf.write(" \7\4\2\2 \"\5\b\5\2!\31\3\2\2\2!\32\3\2\2\2!\33\3\2\2")
        buf.write("\2\"\t\3\2\2\2#(\7\7\2\2$%\7\13\2\2%\'\7\7\2\2&$\3\2\2")
        buf.write("\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\13\3\2\2\2*(\3\2\2")
        buf.write("\2\5\23!(")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'array'", "'of'", "'int'", "'float'", 
                     "<INVALID>", "<INVALID>", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "ARRAY", "OF", "INTTYPE", "FLOATTYPE", 
                      "ID", "INTLIT", "LB", "RB", "COMMA", "SEMI", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecls = 1
    RULE_vardecl = 2
    RULE_mctype = 3
    RULE_ids = 4

    ruleNames =  [ "program", "vardecls", "vardecl", "mctype", "ids" ]

    EOF = Token.EOF
    ARRAY=1
    OF=2
    INTTYPE=3
    FLOATTYPE=4
    ID=5
    INTLIT=6
    LB=7
    RB=8
    COMMA=9
    SEMI=10
    WS=11
    ERROR_CHAR=12
    UNCLOSE_STRING=13
    ILLEGAL_ESCAPE=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecls(self):
            return self.getTypedRuleContext(MCParser.VardeclsContext,0)


        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.vardecls()
            self.state = 11
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def vardecls(self):
            return self.getTypedRuleContext(MCParser.VardeclsContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecls" ):
                return visitor.visitVardecls(self)
            else:
                return visitor.visitChildren(self)




    def vardecls(self):

        localctx = MCParser.VardeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardecls)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.vardecl()
                self.state = 14
                self.vardecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def ids(self):
            return self.getTypedRuleContext(MCParser.IdsContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.mctype()
            self.state = 20
            self.ids()
            self.state = 21
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MctypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def ARRAY(self):
            return self.getToken(MCParser.ARRAY, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def OF(self):
            return self.getToken(MCParser.OF, 0)

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mctype)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INTTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(MCParser.INTTYPE)
                pass
            elif token in [MCParser.FLOATTYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(MCParser.FLOATTYPE)
                pass
            elif token in [MCParser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(MCParser.ARRAY)
                self.state = 26
                self.match(MCParser.LB)
                self.state = 27
                self.match(MCParser.INTLIT)
                self.state = 28
                self.match(MCParser.RB)
                self.state = 29
                self.match(MCParser.OF)
                self.state = 30
                self.mctype()
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


    class IdsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.ID)
            else:
                return self.getToken(MCParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = MCParser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(MCParser.ID)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 34
                self.match(MCParser.COMMA)
                self.state = 35
                self.match(MCParser.ID)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





