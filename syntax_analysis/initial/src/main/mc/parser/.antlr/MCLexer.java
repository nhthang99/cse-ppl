// Generated from /home/thang/Dropbox/ppl/syntax_analysis/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MCLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, INTLIT=2, Float=3, FloatEx=4, FLOATLIT=5, INT=6, FLOAT=7, RETURN=8, 
		LB=9, RB=10, LP=11, RP=12, SM=13, CM=14, EQ=15, ADD=16, SUB=17, MUL=18, 
		DIV=19, WS=20, ERROR_CHAR=21, UNCLOSE_STRING=22, ILLEGAL_ESCAPE=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"NonDigit", "Digit", "NonZeroDigit", "Sign", "Dot", "Quote", "ID", "INTLIT", 
		"Float", "FloatEx", "FLOATLIT", "INT", "FLOAT", "RETURN", "LB", "RB", 
		"LP", "RP", "SM", "CM", "EQ", "ADD", "SUB", "MUL", "DIV", "WS", "ERROR_CHAR", 
		"UNCLOSE_STRING", "ILLEGAL_ESCAPE"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, "'int'", "'float'", "'return'", "'('", 
		"')'", "'{'", "'}'", "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "ID", "INTLIT", "Float", "FloatEx", "FLOATLIT", "INT", "FLOAT", 
		"RETURN", "LB", "RB", "LP", "RP", "SM", "CM", "EQ", "ADD", "SUB", "MUL", 
		"DIV", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MCLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31\u00c8\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\7\bM\n\b\f\b\16\bP\13\b"+
		"\3\t\3\t\3\t\7\tU\n\t\f\t\16\tX\13\t\5\tZ\n\t\3\n\7\n]\n\n\f\n\16\n`\13"+
		"\n\3\n\3\n\6\nd\n\n\r\n\16\ne\3\n\6\ni\n\n\r\n\16\nj\3\n\3\n\7\no\n\n"+
		"\f\n\16\nr\13\n\5\nt\n\n\3\13\6\13w\n\13\r\13\16\13x\3\13\3\13\6\13}\n"+
		"\13\r\13\16\13~\3\f\3\f\6\f\u0083\n\f\r\f\16\f\u0084\3\f\5\f\u0088\n\f"+
		"\3\f\3\f\5\f\u008c\n\f\3\f\6\f\u008f\n\f\r\f\16\f\u0090\5\f\u0093\n\f"+
		"\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\6\33\u00bd\n\33"+
		"\r\33\16\33\u00be\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\2\2\37\3\2\5"+
		"\2\7\2\t\2\13\2\r\2\17\3\21\4\23\5\25\6\27\7\31\b\33\t\35\n\37\13!\f#"+
		"\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31\3\2\6\5\2"+
		"C\\aac|\3\2\62;\3\2\63;\5\2\13\f\17\17\"\"\2\u00d2\2\17\3\2\2\2\2\21\3"+
		"\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2"+
		"\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2"+
		"\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2"+
		"\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\3=\3\2\2\2\5?\3\2"+
		"\2\2\7A\3\2\2\2\tC\3\2\2\2\13E\3\2\2\2\rG\3\2\2\2\17I\3\2\2\2\21Y\3\2"+
		"\2\2\23s\3\2\2\2\25v\3\2\2\2\27\u0092\3\2\2\2\31\u0094\3\2\2\2\33\u0098"+
		"\3\2\2\2\35\u009e\3\2\2\2\37\u00a5\3\2\2\2!\u00a7\3\2\2\2#\u00a9\3\2\2"+
		"\2%\u00ab\3\2\2\2\'\u00ad\3\2\2\2)\u00af\3\2\2\2+\u00b1\3\2\2\2-\u00b3"+
		"\3\2\2\2/\u00b5\3\2\2\2\61\u00b7\3\2\2\2\63\u00b9\3\2\2\2\65\u00bc\3\2"+
		"\2\2\67\u00c2\3\2\2\29\u00c4\3\2\2\2;\u00c6\3\2\2\2=>\t\2\2\2>\4\3\2\2"+
		"\2?@\t\3\2\2@\6\3\2\2\2AB\t\4\2\2B\b\3\2\2\2CD\7/\2\2D\n\3\2\2\2EF\7\60"+
		"\2\2F\f\3\2\2\2GH\7)\2\2H\16\3\2\2\2IN\5\3\2\2JM\5\3\2\2KM\5\5\3\2LJ\3"+
		"\2\2\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\20\3\2\2\2PN\3\2\2\2Q"+
		"Z\7\62\2\2RV\5\7\4\2SU\5\5\3\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2"+
		"WZ\3\2\2\2XV\3\2\2\2YQ\3\2\2\2YR\3\2\2\2Z\22\3\2\2\2[]\5\5\3\2\\[\3\2"+
		"\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_a\3\2\2\2`^\3\2\2\2ac\5\13\6\2bd\5"+
		"\5\3\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2ft\3\2\2\2gi\5\5\3\2hg\3"+
		"\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3\2\2\2lp\5\13\6\2mo\5\5\3\2nm"+
		"\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qt\3\2\2\2rp\3\2\2\2s^\3\2\2\2s"+
		"h\3\2\2\2t\24\3\2\2\2uw\5\5\3\2vu\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2"+
		"\2yz\3\2\2\2z|\5\13\6\2{}\5\5\3\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3"+
		"\2\2\2\177\26\3\2\2\2\u0080\u0093\5\23\n\2\u0081\u0083\5\5\3\2\u0082\u0081"+
		"\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085"+
		"\u0088\3\2\2\2\u0086\u0088\5\25\13\2\u0087\u0082\3\2\2\2\u0087\u0086\3"+
		"\2\2\2\u0088\u0089\3\2\2\2\u0089\u008b\7g\2\2\u008a\u008c\5\t\5\2\u008b"+
		"\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008f\5\5"+
		"\3\2\u008e\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2\u0090"+
		"\u0091\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u0080\3\2\2\2\u0092\u0087\3\2"+
		"\2\2\u0093\30\3\2\2\2\u0094\u0095\7k\2\2\u0095\u0096\7p\2\2\u0096\u0097"+
		"\7v\2\2\u0097\32\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a\7n\2\2\u009a\u009b"+
		"\7q\2\2\u009b\u009c\7c\2\2\u009c\u009d\7v\2\2\u009d\34\3\2\2\2\u009e\u009f"+
		"\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7w\2\2\u00a2"+
		"\u00a3\7t\2\2\u00a3\u00a4\7p\2\2\u00a4\36\3\2\2\2\u00a5\u00a6\7*\2\2\u00a6"+
		" \3\2\2\2\u00a7\u00a8\7+\2\2\u00a8\"\3\2\2\2\u00a9\u00aa\7}\2\2\u00aa"+
		"$\3\2\2\2\u00ab\u00ac\7\177\2\2\u00ac&\3\2\2\2\u00ad\u00ae\7=\2\2\u00ae"+
		"(\3\2\2\2\u00af\u00b0\7.\2\2\u00b0*\3\2\2\2\u00b1\u00b2\7?\2\2\u00b2,"+
		"\3\2\2\2\u00b3\u00b4\7-\2\2\u00b4.\3\2\2\2\u00b5\u00b6\7/\2\2\u00b6\60"+
		"\3\2\2\2\u00b7\u00b8\7,\2\2\u00b8\62\3\2\2\2\u00b9\u00ba\7\61\2\2\u00ba"+
		"\64\3\2\2\2\u00bb\u00bd\t\5\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2"+
		"\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1"+
		"\b\33\2\2\u00c1\66\3\2\2\2\u00c2\u00c3\13\2\2\2\u00c38\3\2\2\2\u00c4\u00c5"+
		"\13\2\2\2\u00c5:\3\2\2\2\u00c6\u00c7\13\2\2\2\u00c7<\3\2\2\2\24\2LNVY"+
		"^ejpsx~\u0084\u0087\u008b\u0090\u0092\u00be\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}