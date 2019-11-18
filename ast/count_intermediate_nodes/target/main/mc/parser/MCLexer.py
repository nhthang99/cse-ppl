# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6\6\64\n\6")
        buf.write("\r\6\16\6\65\3\7\6\79\n\7\r\7\16\7:\3\b\3\b\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\6\fF\n\f\r\f\16\fG\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\5\4\2")
        buf.write("C\\c|\3\2\62;\5\2\13\f\17\17\"\"\2S\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3")
        buf.write("\37\3\2\2\2\5%\3\2\2\2\7(\3\2\2\2\t,\3\2\2\2\13\63\3\2")
        buf.write("\2\2\r8\3\2\2\2\17<\3\2\2\2\21>\3\2\2\2\23@\3\2\2\2\25")
        buf.write("B\3\2\2\2\27E\3\2\2\2\31K\3\2\2\2\33M\3\2\2\2\35O\3\2")
        buf.write("\2\2\37 \7c\2\2 !\7t\2\2!\"\7t\2\2\"#\7c\2\2#$\7{\2\2")
        buf.write("$\4\3\2\2\2%&\7q\2\2&\'\7h\2\2\'\6\3\2\2\2()\7k\2\2)*")
        buf.write("\7p\2\2*+\7v\2\2+\b\3\2\2\2,-\7h\2\2-.\7n\2\2./\7q\2\2")
        buf.write("/\60\7c\2\2\60\61\7v\2\2\61\n\3\2\2\2\62\64\t\2\2\2\63")
        buf.write("\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2")
        buf.write("\66\f\3\2\2\2\679\t\3\2\28\67\3\2\2\29:\3\2\2\2:8\3\2")
        buf.write("\2\2:;\3\2\2\2;\16\3\2\2\2<=\7]\2\2=\20\3\2\2\2>?\7_\2")
        buf.write("\2?\22\3\2\2\2@A\7.\2\2A\24\3\2\2\2BC\7=\2\2C\26\3\2\2")
        buf.write("\2DF\t\4\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H")
        buf.write("I\3\2\2\2IJ\b\f\2\2J\30\3\2\2\2KL\13\2\2\2L\32\3\2\2\2")
        buf.write("MN\13\2\2\2N\34\3\2\2\2OP\13\2\2\2P\36\3\2\2\2\6\2\65")
        buf.write(":G\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY = 1
    OF = 2
    INTTYPE = 3
    FLOATTYPE = 4
    ID = 5
    INTLIT = 6
    LB = 7
    RB = 8
    COMMA = 9
    SEMI = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'of'", "'int'", "'float'", "'['", "']'", "','", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAY", "OF", "INTTYPE", "FLOATTYPE", "ID", "INTLIT", "LB", 
            "RB", "COMMA", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ARRAY", "OF", "INTTYPE", "FLOATTYPE", "ID", "INTLIT", 
                  "LB", "RB", "COMMA", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


