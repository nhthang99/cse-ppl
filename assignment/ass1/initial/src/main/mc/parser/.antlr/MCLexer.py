# Generated from /home/thang/Dropbox/ppl/assignment/ass1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01a3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\17\3\20\3\20\5\20\u00cf\n\20\3\21\3\21\7\21\u00d3\n")
        buf.write("\21\f\21\16\21\u00d6\13\21\3\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\7!\u0133\n!\f!\16!\u0136\13")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\7\"\u013e\n\"\f\"\16\"\u0141\13")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\7#\u014b\n#\f#\16#\u014e")
        buf.write("\13#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\6;\u0185\n")
        buf.write(";\r;\16;\u0186\3;\3;\3<\3<\7<\u018d\n<\f<\16<\u0190\13")
        buf.write("<\3<\5<\u0193\n<\3<\3<\3=\3=\7=\u0199\n=\f=\16=\u019c")
        buf.write("\13=\3=\3=\3=\3>\3>\3>\3\u013f\2?\3\2\5\2\7\2\t\2\13\2")
        buf.write("\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\3\35\4\37\5!\6#")
        buf.write("\7%\b\'\t)\n+\13-\f/\r\61\16\63\17\65\20\67\219\22;\23")
        buf.write("=\24?\25A\26C\27E\30G\31I\32K\33M\34O\35Q\36S\37U W!Y")
        buf.write("\"[#]$_%a&c\'e(g)i*k+m,o-q.s/u\60w\61y\62{\63\3\2\r\3")
        buf.write("\2\62;\5\2C\\aac|\3\2\63;\3\2c|\3\2C\\\t\2$$^^ddhhppt")
        buf.write("tvv\6\2\n\f\16\17$$^^\4\2GGgg\4\2\f\f\17\17\5\2\13\f\16")
        buf.write("\17\"\"\6\3\n\f\16\17$$^^\2\u01ac\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\3}\3\2\2\2\5\177\3\2\2\2\7\u0081\3\2\2\2\t\u0083\3\2")
        buf.write("\2\2\13\u0085\3\2\2\2\r\u0087\3\2\2\2\17\u0089\3\2\2\2")
        buf.write("\21\u008e\3\2\2\2\23\u0092\3\2\2\2\25\u0094\3\2\2\2\27")
        buf.write("\u0097\3\2\2\2\31\u00b8\3\2\2\2\33\u00bb\3\2\2\2\35\u00ca")
        buf.write("\3\2\2\2\37\u00ce\3\2\2\2!\u00d0\3\2\2\2#\u00da\3\2\2")
        buf.write("\2%\u00de\3\2\2\2\'\u00e4\3\2\2\2)\u00eb\3\2\2\2+\u00f3")
        buf.write("\3\2\2\2-\u00f8\3\2\2\2/\u00fe\3\2\2\2\61\u0107\3\2\2")
        buf.write("\2\63\u010c\3\2\2\2\65\u0110\3\2\2\2\67\u0113\3\2\2\2")
        buf.write("9\u011a\3\2\2\2;\u011d\3\2\2\2=\u0123\3\2\2\2?\u0128\3")
        buf.write("\2\2\2A\u012e\3\2\2\2C\u0139\3\2\2\2E\u0147\3\2\2\2G\u014f")
        buf.write("\3\2\2\2I\u0151\3\2\2\2K\u0153\3\2\2\2M\u0155\3\2\2\2")
        buf.write("O\u0157\3\2\2\2Q\u0159\3\2\2\2S\u015b\3\2\2\2U\u015d\3")
        buf.write("\2\2\2W\u015f\3\2\2\2Y\u0161\3\2\2\2[\u0163\3\2\2\2]\u0165")
        buf.write("\3\2\2\2_\u0167\3\2\2\2a\u0169\3\2\2\2c\u016b\3\2\2\2")
        buf.write("e\u016e\3\2\2\2g\u0171\3\2\2\2i\u0174\3\2\2\2k\u0177\3")
        buf.write("\2\2\2m\u0179\3\2\2\2o\u017b\3\2\2\2q\u017e\3\2\2\2s\u0181")
        buf.write("\3\2\2\2u\u0184\3\2\2\2w\u018a\3\2\2\2y\u0196\3\2\2\2")
        buf.write("{\u01a0\3\2\2\2}~\t\2\2\2~\4\3\2\2\2\177\u0080\t\3\2\2")
        buf.write("\u0080\6\3\2\2\2\u0081\u0082\t\4\2\2\u0082\b\3\2\2\2\u0083")
        buf.write("\u0084\t\5\2\2\u0084\n\3\2\2\2\u0085\u0086\t\6\2\2\u0086")
        buf.write("\f\3\2\2\2\u0087\u0088\7\60\2\2\u0088\16\3\2\2\2\u0089")
        buf.write("\u008a\7$\2\2\u008a\20\3\2\2\2\u008b\u008c\7^\2\2\u008c")
        buf.write("\u008f\n\7\2\2\u008d\u008f\7^\2\2\u008e\u008b\3\2\2\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\22\3\2\2\2\u0090\u0093\n\b")
        buf.write("\2\2\u0091\u0093\5\25\13\2\u0092\u0090\3\2\2\2\u0092\u0091")
        buf.write("\3\2\2\2\u0093\24\3\2\2\2\u0094\u0095\7^\2\2\u0095\u0096")
        buf.write("\t\7\2\2\u0096\26\3\2\2\2\u0097\u0099\t\t\2\2\u0098\u009a")
        buf.write("\7/\2\2\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009c\3\2\2\2\u009b\u009d\5\3\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3")
        buf.write("\2\2\2\u009f\30\3\2\2\2\u00a0\u00a2\5\3\2\2\u00a1\u00a0")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a9\7\60\2")
        buf.write("\2\u00a6\u00a8\5\3\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00b9\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ae\5\3\2\2")
        buf.write("\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3")
        buf.write("\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b2\u00b4\7\60\2\2\u00b3\u00b5\5\3\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00a1\3")
        buf.write("\2\2\2\u00b8\u00af\3\2\2\2\u00b9\32\3\2\2\2\u00ba\u00bc")
        buf.write("\5\3\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\34\3\2\2\2\u00bf")
        buf.write("\u00c1\5\31\r\2\u00c0\u00c2\5\27\f\2\u00c1\u00c0\3\2\2")
        buf.write("\2\u00c1\u00c2\3\2\2\2\u00c2\u00cb\3\2\2\2\u00c3\u00c5")
        buf.write("\5\3\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00c9\5\27\f\2\u00c9\u00cb\3\2\2\2\u00ca\u00bf")
        buf.write("\3\2\2\2\u00ca\u00c4\3\2\2\2\u00cb\36\3\2\2\2\u00cc\u00cf")
        buf.write("\5=\37\2\u00cd\u00cf\5? \2\u00ce\u00cc\3\2\2\2\u00ce\u00cd")
        buf.write("\3\2\2\2\u00cf \3\2\2\2\u00d0\u00d4\5\17\b\2\u00d1\u00d3")
        buf.write("\5\23\n\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\3\2\2\2")
        buf.write("\u00d6\u00d4\3\2\2\2\u00d7\u00d8\5\17\b\2\u00d8\u00d9")
        buf.write("\b\21\2\2\u00d9\"\3\2\2\2\u00da\u00db\7k\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7v\2\2\u00dd$\3\2\2\2\u00de\u00df")
        buf.write("\7h\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2")
        buf.write("\7c\2\2\u00e2\u00e3\7v\2\2\u00e3&\3\2\2\2\u00e4\u00e5")
        buf.write("\7u\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7i\2\2\u00ea(\3")
        buf.write("\2\2\2\u00eb\u00ec\7d\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7q\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7c\2\2\u00f1\u00f2\7p\2\2\u00f2*\3\2\2\2\u00f3\u00f4")
        buf.write("\7x\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7")
        buf.write("\7f\2\2\u00f7,\3\2\2\2\u00f8\u00f9\7d\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd")
        buf.write("\7m\2\2\u00fd.\3\2\2\2\u00fe\u00ff\7e\2\2\u00ff\u0100")
        buf.write("\7q\2\2\u0100\u0101\7p\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7k\2\2\u0103\u0104\7p\2\2\u0104\u0105\7w\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\60\3\2\2\2\u0107\u0108\7g\2\2\u0108\u0109")
        buf.write("\7n\2\2\u0109\u010a\7u\2\2\u010a\u010b\7g\2\2\u010b\62")
        buf.write("\3\2\2\2\u010c\u010d\7h\2\2\u010d\u010e\7q\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\64\3\2\2\2\u0110\u0111\7k\2\2\u0111\u0112")
        buf.write("\7h\2\2\u0112\66\3\2\2\2\u0113\u0114\7t\2\2\u0114\u0115")
        buf.write("\7g\2\2\u0115\u0116\7v\2\2\u0116\u0117\7w\2\2\u0117\u0118")
        buf.write("\7t\2\2\u0118\u0119\7p\2\2\u01198\3\2\2\2\u011a\u011b")
        buf.write("\7f\2\2\u011b\u011c\7q\2\2\u011c:\3\2\2\2\u011d\u011e")
        buf.write("\7y\2\2\u011e\u011f\7j\2\2\u011f\u0120\7k\2\2\u0120\u0121")
        buf.write("\7n\2\2\u0121\u0122\7g\2\2\u0122<\3\2\2\2\u0123\u0124")
        buf.write("\7v\2\2\u0124\u0125\7t\2\2\u0125\u0126\7w\2\2\u0126\u0127")
        buf.write("\7g\2\2\u0127>\3\2\2\2\u0128\u0129\7h\2\2\u0129\u012a")
        buf.write("\7c\2\2\u012a\u012b\7n\2\2\u012b\u012c\7u\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d@\3\2\2\2\u012e\u012f\7\61\2\2\u012f\u0130")
        buf.write("\7\61\2\2\u0130\u0134\3\2\2\2\u0131\u0133\n\n\2\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\u0136\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\u0137\3\2\2\2\u0136\u0134\3")
        buf.write("\2\2\2\u0137\u0138\b!\3\2\u0138B\3\2\2\2\u0139\u013a\7")
        buf.write("\61\2\2\u013a\u013b\7,\2\2\u013b\u013f\3\2\2\2\u013c\u013e")
        buf.write("\13\2\2\2\u013d\u013c\3\2\2\2\u013e\u0141\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0142\3\2\2\2")
        buf.write("\u0141\u013f\3\2\2\2\u0142\u0143\7,\2\2\u0143\u0144\7")
        buf.write("\61\2\2\u0144\u0145\3\2\2\2\u0145\u0146\b\"\3\2\u0146")
        buf.write("D\3\2\2\2\u0147\u014c\5\5\3\2\u0148\u014b\5\5\3\2\u0149")
        buf.write("\u014b\5\3\2\2\u014a\u0148\3\2\2\2\u014a\u0149\3\2\2\2")
        buf.write("\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014d\3")
        buf.write("\2\2\2\u014dF\3\2\2\2\u014e\u014c\3\2\2\2\u014f\u0150")
        buf.write("\7*\2\2\u0150H\3\2\2\2\u0151\u0152\7+\2\2\u0152J\3\2\2")
        buf.write("\2\u0153\u0154\7}\2\2\u0154L\3\2\2\2\u0155\u0156\7\177")
        buf.write("\2\2\u0156N\3\2\2\2\u0157\u0158\7]\2\2\u0158P\3\2\2\2")
        buf.write("\u0159\u015a\7_\2\2\u015aR\3\2\2\2\u015b\u015c\7=\2\2")
        buf.write("\u015cT\3\2\2\2\u015d\u015e\7.\2\2\u015eV\3\2\2\2\u015f")
        buf.write("\u0160\7-\2\2\u0160X\3\2\2\2\u0161\u0162\7/\2\2\u0162")
        buf.write("Z\3\2\2\2\u0163\u0164\7,\2\2\u0164\\\3\2\2\2\u0165\u0166")
        buf.write("\7\61\2\2\u0166^\3\2\2\2\u0167\u0168\7\'\2\2\u0168`\3")
        buf.write("\2\2\2\u0169\u016a\7#\2\2\u016ab\3\2\2\2\u016b\u016c\7")
        buf.write("~\2\2\u016c\u016d\7~\2\2\u016dd\3\2\2\2\u016e\u016f\7")
        buf.write("(\2\2\u016f\u0170\7(\2\2\u0170f\3\2\2\2\u0171\u0172\7")
        buf.write("#\2\2\u0172\u0173\7?\2\2\u0173h\3\2\2\2\u0174\u0175\7")
        buf.write("?\2\2\u0175\u0176\7?\2\2\u0176j\3\2\2\2\u0177\u0178\7")
        buf.write(">\2\2\u0178l\3\2\2\2\u0179\u017a\7@\2\2\u017an\3\2\2\2")
        buf.write("\u017b\u017c\7>\2\2\u017c\u017d\7?\2\2\u017dp\3\2\2\2")
        buf.write("\u017e\u017f\7@\2\2\u017f\u0180\7?\2\2\u0180r\3\2\2\2")
        buf.write("\u0181\u0182\7?\2\2\u0182t\3\2\2\2\u0183\u0185\t\13\2")
        buf.write("\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184")
        buf.write("\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u0189\b;\3\2\u0189v\3\2\2\2\u018a\u018e\5\17\b\2\u018b")
        buf.write("\u018d\5\23\n\2\u018c\u018b\3\2\2\2\u018d\u0190\3\2\2")
        buf.write("\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0193\t\f\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195\b<\4\2")
        buf.write("\u0195x\3\2\2\2\u0196\u019a\5\17\b\2\u0197\u0199\5\23")
        buf.write("\n\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019d\u019e\5\21\t\2\u019e\u019f\b=\5\2")
        buf.write("\u019fz\3\2\2\2\u01a0\u01a1\13\2\2\2\u01a1\u01a2\b>\6")
        buf.write("\2\u01a2|\3\2\2\2\32\2\u008e\u0092\u0099\u009e\u00a3\u00a9")
        buf.write("\u00af\u00b6\u00b8\u00bd\u00c1\u00c6\u00ca\u00ce\u00d4")
        buf.write("\u0134\u013f\u014a\u014c\u0186\u018e\u0192\u019a\7\3\21")
        buf.write("\2\b\2\2\3<\3\3=\4\3>\5")
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
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
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
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "Digit", "NonDigit", "NonZeroDigit", "LowerCase", "UpperCase", 
                  "Dot", "DoubleQuote", "IllegalString", "StringChar", "EscapeSequence", 
                  "ExponentPart", "FractionalPart", "INTLIT", "FLOATLIT", 
                  "BOOLLIT", "STRLIT", "INTTYPE", "FLOATTYPE", "STRTYPE", 
                  "BOOLTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "ELSE", "FOR", 
                  "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", "LINE_CMT", 
                  "BLOCK_CMT", "ID", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "SM", "CM", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
                  "OR", "AND", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", 
                  "ASSIGN", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[58] = self.UNCLOSE_STRING_action 
            actions[59] = self.ILLEGAL_ESCAPE_action 
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
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    illegal_str = str(self.text)
                    raise IllegalEscape(illegal_str[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise ErrorToken(self.text)
                
     


