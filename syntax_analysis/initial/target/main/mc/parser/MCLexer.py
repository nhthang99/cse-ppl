# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("\u00b1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n")
        buf.write("\7\nM\n\n\f\n\16\nP\13\n\3\13\6\13S\n\13\r\13\16\13T\3")
        buf.write("\f\7\fX\n\f\f\f\16\f[\13\f\3\f\3\f\6\f_\n\f\r\f\16\f`")
        buf.write("\3\f\6\fd\n\f\r\f\16\fe\3\f\3\f\7\fj\n\f\f\f\16\fm\13")
        buf.write("\f\5\fo\n\f\3\r\6\rr\n\r\r\r\16\rs\3\r\3\r\6\rx\n\r\r")
        buf.write("\r\16\ry\3\16\3\16\6\16~\n\16\r\16\16\16\177\3\16\5\16")
        buf.write("\u0083\n\16\3\16\3\16\5\16\u0087\n\16\3\16\6\16\u008a")
        buf.write("\n\16\r\16\16\16\u008b\5\16\u008e\n\16\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u0094\n\17\f\17\16\17\u0097\13\17\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\6\25\u00a6\n\25\r\25\16\25\u00a7\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\2\2\31\3\3\5\4\7\5\t\2\13\2\r\2\17")
        buf.write("\2\21\2\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r#\16%\17")
        buf.write("\'\20)\21+\22-\23/\24\3\2\6\3\2c|\3\2\62;\3\2))\5\2\13")
        buf.write("\f\17\17\"\"\2\u00bd\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\66\3\2\2\2\7:\3")
        buf.write("\2\2\2\t?\3\2\2\2\13A\3\2\2\2\rC\3\2\2\2\17E\3\2\2\2\21")
        buf.write("G\3\2\2\2\23I\3\2\2\2\25R\3\2\2\2\27n\3\2\2\2\31q\3\2")
        buf.write("\2\2\33\u008d\3\2\2\2\35\u008f\3\2\2\2\37\u009a\3\2\2")
        buf.write("\2!\u009c\3\2\2\2#\u009e\3\2\2\2%\u00a0\3\2\2\2\'\u00a2")
        buf.write("\3\2\2\2)\u00a5\3\2\2\2+\u00ab\3\2\2\2-\u00ad\3\2\2\2")
        buf.write("/\u00af\3\2\2\2\61\62\7o\2\2\62\63\7c\2\2\63\64\7k\2\2")
        buf.write("\64\65\7p\2\2\65\4\3\2\2\2\66\67\7k\2\2\678\7p\2\289\7")
        buf.write("v\2\29\6\3\2\2\2:;\7x\2\2;<\7q\2\2<=\7k\2\2=>\7f\2\2>")
        buf.write("\b\3\2\2\2?@\t\2\2\2@\n\3\2\2\2AB\t\3\2\2B\f\3\2\2\2C")
        buf.write("D\7/\2\2D\16\3\2\2\2EF\7\60\2\2F\20\3\2\2\2GH\7)\2\2H")
        buf.write("\22\3\2\2\2IN\5\t\5\2JM\5\t\5\2KM\5\13\6\2LJ\3\2\2\2L")
        buf.write("K\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\24\3\2\2\2PN")
        buf.write("\3\2\2\2QS\t\3\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2")
        buf.write("\2\2U\26\3\2\2\2VX\5\13\6\2WV\3\2\2\2X[\3\2\2\2YW\3\2")
        buf.write("\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\^\5\17\b\2]_\5\13")
        buf.write("\6\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ao\3\2\2\2")
        buf.write("bd\5\13\6\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2fg")
        buf.write("\3\2\2\2gk\5\17\b\2hj\5\13\6\2ih\3\2\2\2jm\3\2\2\2ki\3")
        buf.write("\2\2\2kl\3\2\2\2lo\3\2\2\2mk\3\2\2\2nY\3\2\2\2nc\3\2\2")
        buf.write("\2o\30\3\2\2\2pr\5\13\6\2qp\3\2\2\2rs\3\2\2\2sq\3\2\2")
        buf.write("\2st\3\2\2\2tu\3\2\2\2uw\5\17\b\2vx\5\13\6\2wv\3\2\2\2")
        buf.write("xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\32\3\2\2\2{\u008e\5\27")
        buf.write("\f\2|~\5\13\6\2}|\3\2\2\2~\177\3\2\2\2\177}\3\2\2\2\177")
        buf.write("\u0080\3\2\2\2\u0080\u0083\3\2\2\2\u0081\u0083\5\31\r")
        buf.write("\2\u0082}\3\2\2\2\u0082\u0081\3\2\2\2\u0083\u0084\3\2")
        buf.write("\2\2\u0084\u0086\7g\2\2\u0085\u0087\5\r\7\2\u0086\u0085")
        buf.write("\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088")
        buf.write("\u008a\5\13\6\2\u0089\u0088\3\2\2\2\u008a\u008b\3\2\2")
        buf.write("\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e")
        buf.write("\3\2\2\2\u008d{\3\2\2\2\u008d\u0082\3\2\2\2\u008e\34\3")
        buf.write("\2\2\2\u008f\u0095\5\21\t\2\u0090\u0091\7)\2\2\u0091\u0094")
        buf.write("\7)\2\2\u0092\u0094\n\4\2\2\u0093\u0090\3\2\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3")
        buf.write("\2\2\2\u0098\u0099\5\21\t\2\u0099\36\3\2\2\2\u009a\u009b")
        buf.write("\7*\2\2\u009b \3\2\2\2\u009c\u009d\7+\2\2\u009d\"\3\2")
        buf.write("\2\2\u009e\u009f\7}\2\2\u009f$\3\2\2\2\u00a0\u00a1\7\177")
        buf.write("\2\2\u00a1&\3\2\2\2\u00a2\u00a3\7=\2\2\u00a3(\3\2\2\2")
        buf.write("\u00a4\u00a6\t\5\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a7\3")
        buf.write("\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00aa\b\25\2\2\u00aa*\3\2\2\2\u00ab\u00ac")
        buf.write("\13\2\2\2\u00ac,\3\2\2\2\u00ad\u00ae\13\2\2\2\u00ae.\3")
        buf.write("\2\2\2\u00af\u00b0\13\2\2\2\u00b0\60\3\2\2\2\25\2LNTY")
        buf.write("`eknsy\177\u0082\u0086\u008b\u008d\u0093\u0095\u00a7\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    Float = 6
    FloatEx = 7
    FLOATLIT = 8
    STRLIT = 9
    LB = 10
    RB = 11
    LP = 12
    RP = 13
    SEMI = 14
    WS = 15
    ERROR_CHAR = 16
    UNCLOSE_STRING = 17
    ILLEGAL_ESCAPE = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "Float", "FloatEx", "FLOATLIT", 
            "STRLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "Letter", "Digit", "Sign", 
                  "Dot", "Quote", "ID", "INTLIT", "Float", "FloatEx", "FLOATLIT", 
                  "STRLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


