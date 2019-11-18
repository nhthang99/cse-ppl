# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\7\6\36\n\6\f\6\16\6!\13\6\3\6\2\2\7\2\4\6\b\n\2")
        buf.write("\3\3\2\3\4\2\37\2\f\3\2\2\2\4\23\3\2\2\2\6\25\3\2\2\2")
        buf.write("\b\30\3\2\2\2\n\32\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3\16")
        buf.write("\3\3\2\2\2\17\20\5\6\4\2\20\21\5\4\3\2\21\24\3\2\2\2\22")
        buf.write("\24\5\6\4\2\23\17\3\2\2\2\23\22\3\2\2\2\24\5\3\2\2\2\25")
        buf.write("\26\5\b\5\2\26\27\5\n\6\2\27\7\3\2\2\2\30\31\t\2\2\2\31")
        buf.write("\t\3\2\2\2\32\37\7\5\2\2\33\34\7\6\2\2\34\36\7\5\2\2\35")
        buf.write("\33\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \13")
        buf.write("\3\2\2\2!\37\3\2\2\2\4\23\37")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'float'", "'int'", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "FLOATTYPE", "INTTYPE", "ID", "COMMA", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardecls = 1
    RULE_vardecl = 2
    RULE_mctype = 3
    RULE_ids = 4

    ruleNames =  [ "program", "vardecls", "vardecl", "mctype", "ids" ]

    EOF = Token.EOF
    FLOATTYPE=1
    INTTYPE=2
    ID=3
    COMMA=4
    WS=5
    ERROR_CHAR=6
    UNCLOSE_STRING=7
    ILLEGAL_ESCAPE=8

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            _la = self._input.LA(1)
            if not(_la==MCParser.FLOATTYPE or _la==MCParser.INTTYPE):
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
            self.state = 24
            self.match(MCParser.ID)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 25
                self.match(MCParser.COMMA)
                self.state = 26
                self.match(MCParser.ID)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





