# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2%\n\2\3\3\6\3(\n\3")
        buf.write("\r\3\16\3)\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\69\n\6\3\7\3\7\3\b\3\b\3\b\3\b\5\bA\n\b\3\t")
        buf.write("\3\t\3\n\6\nF\n\n\r\n\16\nG\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\3\2\5\3\2\62;\4\2>>@@\5\2\13\f\17")
        buf.write("\17\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\3$\3\2\2\2\5\'\3\2\2\2\7+\3\2\2\2\t-\3\2\2\2\138\3\2")
        buf.write("\2\2\r:\3\2\2\2\17@\3\2\2\2\21B\3\2\2\2\23E\3\2\2\2\25")
        buf.write("K\3\2\2\2\27M\3\2\2\2\31O\3\2\2\2\33\34\7v\2\2\34\35\7")
        buf.write("t\2\2\35\36\7w\2\2\36%\7g\2\2\37 \7h\2\2 !\7c\2\2!\"\7")
        buf.write("n\2\2\"#\7u\2\2#%\7g\2\2$\33\3\2\2\2$\37\3\2\2\2%\4\3")
        buf.write("\2\2\2&(\t\2\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2")
        buf.write("\2\2*\6\3\2\2\2+,\7*\2\2,\b\3\2\2\2-.\7+\2\2.\n\3\2\2")
        buf.write("\2/9\t\3\2\2\60\61\7@\2\2\619\7?\2\2\62\63\7>\2\2\639")
        buf.write("\7?\2\2\64\65\7?\2\2\659\7?\2\2\66\67\7#\2\2\679\7?\2")
        buf.write("\28/\3\2\2\28\60\3\2\2\28\62\3\2\2\28\64\3\2\2\28\66\3")
        buf.write("\2\2\29\f\3\2\2\2:;\7`\2\2;\16\3\2\2\2<=\7(\2\2=A\7(\2")
        buf.write("\2>?\7~\2\2?A\7~\2\2@<\3\2\2\2@>\3\2\2\2A\20\3\2\2\2B")
        buf.write("C\7=\2\2C\22\3\2\2\2DF\t\4\2\2ED\3\2\2\2FG\3\2\2\2GE\3")
        buf.write("\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\b\n\2\2J\24\3\2\2\2KL\13")
        buf.write("\2\2\2L\26\3\2\2\2MN\13\2\2\2N\30\3\2\2\2OP\13\2\2\2P")
        buf.write("\32\3\2\2\2\b\2$)8@G\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLIT = 1
    INTLIT = 2
    LB = 3
    RB = 4
    COMPARE = 5
    EXPONENT = 6
    ANDOR = 7
    SEMI = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'^'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLIT", "INTLIT", "LB", "RB", "COMPARE", "EXPONENT", "ANDOR", 
            "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOLIT", "INTLIT", "LB", "RB", "COMPARE", "EXPONENT", 
                  "ANDOR", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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


