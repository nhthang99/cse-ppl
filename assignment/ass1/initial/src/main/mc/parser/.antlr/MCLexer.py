# Generated from /home/thang/Dropbox/ppl/assignment/ass1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01a7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\5\t\u008f\n\t\3")
        buf.write("\n\3\n\5\n\u0093\n\n\3\13\3\13\3\13\3\f\3\f\5\f\u009a")
        buf.write("\n\f\3\f\6\f\u009d\n\f\r\f\16\f\u009e\3\r\6\r\u00a2\n")
        buf.write("\r\r\r\16\r\u00a3\3\r\3\r\7\r\u00a8\n\r\f\r\16\r\u00ab")
        buf.write("\13\r\3\r\7\r\u00ae\n\r\f\r\16\r\u00b1\13\r\3\r\3\r\6")
        buf.write("\r\u00b5\n\r\r\r\16\r\u00b6\5\r\u00b9\n\r\3\16\6\16\u00bc")
        buf.write("\n\16\r\16\16\16\u00bd\3\17\3\17\5\17\u00c2\n\17\3\17")
        buf.write("\6\17\u00c5\n\17\r\17\16\17\u00c6\3\17\3\17\5\17\u00cb")
        buf.write("\n\17\3\20\3\20\5\20\u00cf\n\20\3\21\3\21\3\21\7\21\u00d4")
        buf.write("\n\21\f\21\16\21\u00d7\13\21\5\21\u00d9\n\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\7!\u0136\n!\f")
        buf.write("!\16!\u0139\13!\3!\3!\3\"\3\"\3\"\3\"\7\"\u0141\n\"\f")
        buf.write("\"\16\"\u0144\13\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\7#\u014e")
        buf.write("\n#\f#\16#\u0151\13#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39\39\3:\3")
        buf.write(":\3;\6;\u0188\n;\r;\16;\u0189\3;\3;\3<\3<\3<\7<\u0191")
        buf.write("\n<\f<\16<\u0194\13<\3<\3<\3<\3=\3=\7=\u019b\n=\f=\16")
        buf.write("=\u019e\13=\3=\5=\u01a1\n=\3=\3=\3>\3>\3>\3\u0142\2?\3")
        buf.write("\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2")
        buf.write("\33\3\35\4\37\5!\6#\7%\b\'\t)\n+\13-\f/\r\61\16\63\17")
        buf.write("\65\20\67\219\22;\23=\24?\25A\26C\27E\30G\31I\32K\33M")
        buf.write("\34O\35Q\36S\37U W!Y\"[#]$_%a&c\'e(g)i*k+m,o-q.s/u\60")
        buf.write("w\61y\62{\63\3\2\16\3\2\62;\5\2C\\aac|\3\2\63;\3\2c|\3")
        buf.write("\2C\\\t\2$$^^ddhhppttvv\6\2\n\f\16\17$$^^\4\2GGgg\3\2")
        buf.write("$$\4\2\f\f\17\17\5\2\13\f\17\17\"\"\6\3\n\f\16\17$$^^")
        buf.write("\2\u01b2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3}\3\2\2\2\5\177\3\2\2\2")
        buf.write("\7\u0081\3\2\2\2\t\u0083\3\2\2\2\13\u0085\3\2\2\2\r\u0087")
        buf.write("\3\2\2\2\17\u0089\3\2\2\2\21\u008e\3\2\2\2\23\u0092\3")
        buf.write("\2\2\2\25\u0094\3\2\2\2\27\u0097\3\2\2\2\31\u00b8\3\2")
        buf.write("\2\2\33\u00bb\3\2\2\2\35\u00ca\3\2\2\2\37\u00ce\3\2\2")
        buf.write("\2!\u00d0\3\2\2\2#\u00dd\3\2\2\2%\u00e1\3\2\2\2\'\u00e7")
        buf.write("\3\2\2\2)\u00ee\3\2\2\2+\u00f6\3\2\2\2-\u00fb\3\2\2\2")
        buf.write("/\u0101\3\2\2\2\61\u010a\3\2\2\2\63\u010f\3\2\2\2\65\u0113")
        buf.write("\3\2\2\2\67\u0116\3\2\2\29\u011d\3\2\2\2;\u0120\3\2\2")
        buf.write("\2=\u0126\3\2\2\2?\u012b\3\2\2\2A\u0131\3\2\2\2C\u013c")
        buf.write("\3\2\2\2E\u014a\3\2\2\2G\u0152\3\2\2\2I\u0154\3\2\2\2")
        buf.write("K\u0156\3\2\2\2M\u0158\3\2\2\2O\u015a\3\2\2\2Q\u015c\3")
        buf.write("\2\2\2S\u015e\3\2\2\2U\u0160\3\2\2\2W\u0162\3\2\2\2Y\u0164")
        buf.write("\3\2\2\2[\u0166\3\2\2\2]\u0168\3\2\2\2_\u016a\3\2\2\2")
        buf.write("a\u016c\3\2\2\2c\u016e\3\2\2\2e\u0171\3\2\2\2g\u0174\3")
        buf.write("\2\2\2i\u0177\3\2\2\2k\u017a\3\2\2\2m\u017c\3\2\2\2o\u017e")
        buf.write("\3\2\2\2q\u0181\3\2\2\2s\u0184\3\2\2\2u\u0187\3\2\2\2")
        buf.write("w\u018d\3\2\2\2y\u0198\3\2\2\2{\u01a4\3\2\2\2}~\t\2\2")
        buf.write("\2~\4\3\2\2\2\177\u0080\t\3\2\2\u0080\6\3\2\2\2\u0081")
        buf.write("\u0082\t\4\2\2\u0082\b\3\2\2\2\u0083\u0084\t\5\2\2\u0084")
        buf.write("\n\3\2\2\2\u0085\u0086\t\6\2\2\u0086\f\3\2\2\2\u0087\u0088")
        buf.write("\7\60\2\2\u0088\16\3\2\2\2\u0089\u008a\7$\2\2\u008a\20")
        buf.write("\3\2\2\2\u008b\u008c\7^\2\2\u008c\u008f\n\7\2\2\u008d")
        buf.write("\u008f\7^\2\2\u008e\u008b\3\2\2\2\u008e\u008d\3\2\2\2")
        buf.write("\u008f\22\3\2\2\2\u0090\u0093\n\b\2\2\u0091\u0093\5\25")
        buf.write("\13\2\u0092\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\24")
        buf.write("\3\2\2\2\u0094\u0095\7^\2\2\u0095\u0096\t\7\2\2\u0096")
        buf.write("\26\3\2\2\2\u0097\u0099\t\t\2\2\u0098\u009a\7/\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2")
        buf.write("\u009b\u009d\5\3\2\2\u009c\u009b\3\2\2\2\u009d\u009e\3")
        buf.write("\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\30")
        buf.write("\3\2\2\2\u00a0\u00a2\5\3\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a5\3\2\2\2\u00a5\u00a9\7\60\2\2\u00a6\u00a8")
        buf.write("\5\3\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9")
        buf.write("\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00b9\3\2\2\2")
        buf.write("\u00ab\u00a9\3\2\2\2\u00ac\u00ae\5\3\2\2\u00ad\u00ac\3")
        buf.write("\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2")
        buf.write("\u00b4\7\60\2\2\u00b3\u00b5\5\3\2\2\u00b4\u00b3\3\2\2")
        buf.write("\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7")
        buf.write("\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00a1\3\2\2\2\u00b8")
        buf.write("\u00af\3\2\2\2\u00b9\32\3\2\2\2\u00ba\u00bc\5\3\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\34\3\2\2\2\u00bf\u00c1\5\31")
        buf.write("\r\2\u00c0\u00c2\5\27\f\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00cb\3\2\2\2\u00c3\u00c5\5\3\2\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\5")
        buf.write("\27\f\2\u00c9\u00cb\3\2\2\2\u00ca\u00bf\3\2\2\2\u00ca")
        buf.write("\u00c4\3\2\2\2\u00cb\36\3\2\2\2\u00cc\u00cf\5=\37\2\u00cd")
        buf.write("\u00cf\5? \2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write(" \3\2\2\2\u00d0\u00d8\5\17\b\2\u00d1\u00d9\n\n\2\2\u00d2")
        buf.write("\u00d4\5\23\n\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7\3\2\2")
        buf.write("\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d9")
        buf.write("\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d1\3\2\2\2\u00d8")
        buf.write("\u00d5\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\5\17\b")
        buf.write("\2\u00db\u00dc\b\21\2\2\u00dc\"\3\2\2\2\u00dd\u00de\7")
        buf.write("k\2\2\u00de\u00df\7p\2\2\u00df\u00e0\7v\2\2\u00e0$\3\2")
        buf.write("\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6\7v\2\2\u00e6&\3")
        buf.write("\2\2\2\u00e7\u00e8\7u\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7i\2\2\u00ed(\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3")
        buf.write("\7g\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7p\2\2\u00f5*\3")
        buf.write("\2\2\2\u00f6\u00f7\7x\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7f\2\2\u00fa,\3\2\2\2\u00fb\u00fc")
        buf.write("\7d\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7m\2\2\u0100.\3\2\2\2\u0101\u0102")
        buf.write("\7e\2\2\u0102\u0103\7q\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7v\2\2\u0105\u0106\7k\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7w\2\2\u0108\u0109\7g\2\2\u0109\60\3\2\2\2\u010a\u010b")
        buf.write("\7g\2\2\u010b\u010c\7n\2\2\u010c\u010d\7u\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e\62\3\2\2\2\u010f\u0110\7h\2\2\u0110\u0111")
        buf.write("\7q\2\2\u0111\u0112\7t\2\2\u0112\64\3\2\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7h\2\2\u0115\66\3\2\2\2\u0116\u0117")
        buf.write("\7t\2\2\u0117\u0118\7g\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7w\2\2\u011a\u011b\7t\2\2\u011b\u011c\7p\2\2\u011c8\3")
        buf.write("\2\2\2\u011d\u011e\7f\2\2\u011e\u011f\7q\2\2\u011f:\3")
        buf.write("\2\2\2\u0120\u0121\7y\2\2\u0121\u0122\7j\2\2\u0122\u0123")
        buf.write("\7k\2\2\u0123\u0124\7n\2\2\u0124\u0125\7g\2\2\u0125<\3")
        buf.write("\2\2\2\u0126\u0127\7v\2\2\u0127\u0128\7t\2\2\u0128\u0129")
        buf.write("\7w\2\2\u0129\u012a\7g\2\2\u012a>\3\2\2\2\u012b\u012c")
        buf.write("\7h\2\2\u012c\u012d\7c\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7u\2\2\u012f\u0130\7g\2\2\u0130@\3\2\2\2\u0131\u0132")
        buf.write("\7\61\2\2\u0132\u0133\7\61\2\2\u0133\u0137\3\2\2\2\u0134")
        buf.write("\u0136\n\13\2\2\u0135\u0134\3\2\2\2\u0136\u0139\3\2\2")
        buf.write("\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b\b!\3\2\u013b")
        buf.write("B\3\2\2\2\u013c\u013d\7\61\2\2\u013d\u013e\7,\2\2\u013e")
        buf.write("\u0142\3\2\2\2\u013f\u0141\13\2\2\2\u0140\u013f\3\2\2")
        buf.write("\2\u0141\u0144\3\2\2\2\u0142\u0143\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145")
        buf.write("\u0146\7,\2\2\u0146\u0147\7\61\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0149\b\"\3\2\u0149D\3\2\2\2\u014a\u014f\5\5\3")
        buf.write("\2\u014b\u014e\5\5\3\2\u014c\u014e\5\3\2\2\u014d\u014b")
        buf.write("\3\2\2\2\u014d\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150F\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0152\u0153\7*\2\2\u0153H\3\2\2\2\u0154")
        buf.write("\u0155\7+\2\2\u0155J\3\2\2\2\u0156\u0157\7}\2\2\u0157")
        buf.write("L\3\2\2\2\u0158\u0159\7\177\2\2\u0159N\3\2\2\2\u015a\u015b")
        buf.write("\7]\2\2\u015bP\3\2\2\2\u015c\u015d\7_\2\2\u015dR\3\2\2")
        buf.write("\2\u015e\u015f\7=\2\2\u015fT\3\2\2\2\u0160\u0161\7.\2")
        buf.write("\2\u0161V\3\2\2\2\u0162\u0163\7-\2\2\u0163X\3\2\2\2\u0164")
        buf.write("\u0165\7/\2\2\u0165Z\3\2\2\2\u0166\u0167\7,\2\2\u0167")
        buf.write("\\\3\2\2\2\u0168\u0169\7\61\2\2\u0169^\3\2\2\2\u016a\u016b")
        buf.write("\7\'\2\2\u016b`\3\2\2\2\u016c\u016d\7#\2\2\u016db\3\2")
        buf.write("\2\2\u016e\u016f\7~\2\2\u016f\u0170\7~\2\2\u0170d\3\2")
        buf.write("\2\2\u0171\u0172\7(\2\2\u0172\u0173\7(\2\2\u0173f\3\2")
        buf.write("\2\2\u0174\u0175\7#\2\2\u0175\u0176\7?\2\2\u0176h\3\2")
        buf.write("\2\2\u0177\u0178\7?\2\2\u0178\u0179\7?\2\2\u0179j\3\2")
        buf.write("\2\2\u017a\u017b\7>\2\2\u017bl\3\2\2\2\u017c\u017d\7@")
        buf.write("\2\2\u017dn\3\2\2\2\u017e\u017f\7>\2\2\u017f\u0180\7?")
        buf.write("\2\2\u0180p\3\2\2\2\u0181\u0182\7@\2\2\u0182\u0183\7?")
        buf.write("\2\2\u0183r\3\2\2\2\u0184\u0185\7?\2\2\u0185t\3\2\2\2")
        buf.write("\u0186\u0188\t\f\2\2\u0187\u0186\3\2\2\2\u0188\u0189\3")
        buf.write("\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b")
        buf.write("\3\2\2\2\u018b\u018c\b;\3\2\u018cv\3\2\2\2\u018d\u0192")
        buf.write("\5\17\b\2\u018e\u0191\5\23\n\2\u018f\u0191\5\21\t\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191\u0194\3\2\2\2")
        buf.write("\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3")
        buf.write("\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196\5\17\b\2\u0196")
        buf.write("\u0197\b<\4\2\u0197x\3\2\2\2\u0198\u019c\5\17\b\2\u0199")
        buf.write("\u019b\5\23\n\2\u019a\u0199\3\2\2\2\u019b\u019e\3\2\2")
        buf.write("\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a0")
        buf.write("\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a1\t\r\2\2\u01a0")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\b=\5\2")
        buf.write("\u01a3z\3\2\2\2\u01a4\u01a5\13\2\2\2\u01a5\u01a6\b>\6")
        buf.write("\2\u01a6|\3\2\2\2\34\2\u008e\u0092\u0099\u009e\u00a3\u00a9")
        buf.write("\u00af\u00b6\u00b8\u00bd\u00c1\u00c6\u00ca\u00ce\u00d5")
        buf.write("\u00d8\u0137\u0142\u014d\u014f\u0189\u0190\u0192\u019c")
        buf.write("\u01a0\7\3\21\2\b\2\2\3<\3\3=\4\3>\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLLIT = 3
    STRLIT = 4
    INTTYPE = 5
    FLOATTYPE = 6
    STRTYPE = 7
    BOOLTYPE = 8
    VOIDTYPE = 9
    BREAK = 10
    CONTINUE = 11
    ELSE = 12
    FOR = 13
    IF = 14
    RETURN = 15
    DO = 16
    WHILE = 17
    TRUE = 18
    FALSE = 19
    LINE_CMT = 20
    BLOCK_CMT = 21
    ID = 22
    LP = 23
    RP = 24
    LCB = 25
    RCB = 26
    LSB = 27
    RSB = 28
    SM = 29
    CM = 30
    ADD = 31
    SUB = 32
    MUL = 33
    DIV = 34
    MOD = 35
    NOT = 36
    OR = 37
    AND = 38
    NOT_EQUAL = 39
    EQUAL = 40
    LT = 41
    GT = 42
    LE = 43
    GE = 44
    ASSIGN = 45
    WS = 46
    ILLEGAL_ESCAPE = 47
    UNCLOSE_STRING = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'string'", "'boolean'", "'void'", "'break'", 
            "'continue'", "'else'", "'for'", "'if'", "'return'", "'do'", 
            "'while'", "'true'", "'false'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'!'", "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", "'<='", 
            "'>='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", "INTTYPE", "FLOATTYPE", 
            "STRTYPE", "BOOLTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "ELSE", 
            "FOR", "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", "LINE_CMT", 
            "BLOCK_CMT", "ID", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SM", 
            "CM", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "OR", "AND", 
            "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", "ASSIGN", "WS", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "Digit", "NonDigit", "NonZeroDigit", "LowerCase", "UpperCase", 
                  "Dot", "DoubleQuote", "IllegalString", "StringChar", "EscapeSequence", 
                  "ExponentPart", "FractionalPart", "INTLIT", "FLOATLIT", 
                  "BOOLLIT", "STRLIT", "INTTYPE", "FLOATTYPE", "STRTYPE", 
                  "BOOLTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "ELSE", "FOR", 
                  "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", "LINE_CMT", 
                  "BLOCK_CMT", "ID", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "SM", "CM", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "OR", "AND", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", 
                  "ASSIGN", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[15] = self.STRLIT_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    result = str(self.text)
                    self.text = result[1:-1]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    illegal_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    backslash = illegal_str.find('\\')
                    if illegal_str[backslash:backslash + 2] not in possible:
                        raise IllegalEscape(illegal_str[1:backslash + 2])
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise ErrorToken(self.text)
                
     


