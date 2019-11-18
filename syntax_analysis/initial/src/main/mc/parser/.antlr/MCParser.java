// Generated from /home/thang/Dropbox/ppl/syntax_analysis/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ID=1, INTLIT=2, Float=3, FloatEx=4, FLOATLIT=5, INT=6, FLOAT=7, RETURN=8, 
		LB=9, RB=10, LP=11, RP=12, SM=13, CM=14, EQ=15, ADD=16, SUB=17, MUL=18, 
		DIV=19, WS=20, ERROR_CHAR=21, UNCLOSE_STRING=22, ILLEGAL_ESCAPE=23;
	public static final int
		RULE_program = 0, RULE_manydcls = 1, RULE_dcls = 2, RULE_vardcls = 3, 
		RULE_type = 4, RULE_idlist = 5, RULE_funcdcls = 6, RULE_paradcls = 7, 
		RULE_paralist = 8, RULE_paratail = 9, RULE_para = 10, RULE_body = 11, 
		RULE_vardcl_stmt_list = 12, RULE_vardcl_stmt = 13, RULE_stmt = 14, RULE_assign = 15, 
		RULE_call = 16, RULE_explist = 17, RULE_exptail = 18, RULE_return_t = 19, 
		RULE_exp = 20, RULE_operand = 21, RULE_subexp = 22;
	public static final String[] ruleNames = {
		"program", "manydcls", "dcls", "vardcls", "type", "idlist", "funcdcls", 
		"paradcls", "paralist", "paratail", "para", "body", "vardcl_stmt_list", 
		"vardcl_stmt", "stmt", "assign", "call", "explist", "exptail", "return_t", 
		"exp", "operand", "subexp"
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

	@Override
	public String getGrammarFileName() { return "MC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public ManydclsContext manydcls() {
			return getRuleContext(ManydclsContext.class,0);
		}
		public TerminalNode EOF() { return getToken(MCParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			manydcls();
			setState(47);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ManydclsContext extends ParserRuleContext {
		public DclsContext dcls() {
			return getRuleContext(DclsContext.class,0);
		}
		public ManydclsContext manydcls() {
			return getRuleContext(ManydclsContext.class,0);
		}
		public ManydclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_manydcls; }
	}

	public final ManydclsContext manydcls() throws RecognitionException {
		ManydclsContext _localctx = new ManydclsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_manydcls);
		try {
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				dcls();
				setState(50);
				manydcls();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				dcls();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DclsContext extends ParserRuleContext {
		public VardclsContext vardcls() {
			return getRuleContext(VardclsContext.class,0);
		}
		public FuncdclsContext funcdcls() {
			return getRuleContext(FuncdclsContext.class,0);
		}
		public DclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dcls; }
	}

	public final DclsContext dcls() throws RecognitionException {
		DclsContext _localctx = new DclsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_dcls);
		try {
			setState(57);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				vardcls();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				funcdcls();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardclsContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public TerminalNode SM() { return getToken(MCParser.SM, 0); }
		public VardclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardcls; }
	}

	public final VardclsContext vardcls() throws RecognitionException {
		VardclsContext _localctx = new VardclsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vardcls);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			type();
			setState(60);
			idlist();
			setState(61);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MCParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(MCParser.FLOAT, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdlistContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode CM() { return getToken(MCParser.CM, 0); }
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public IdlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idlist; }
	}

	public final IdlistContext idlist() throws RecognitionException {
		IdlistContext _localctx = new IdlistContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_idlist);
		try {
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				match(ID);
				setState(66);
				match(CM);
				setState(67);
				idlist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(68);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdclsContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public ParadclsContext paradcls() {
			return getRuleContext(ParadclsContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public FuncdclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdcls; }
	}

	public final FuncdclsContext funcdcls() throws RecognitionException {
		FuncdclsContext _localctx = new FuncdclsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_funcdcls);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			type();
			setState(72);
			match(ID);
			setState(73);
			paradcls();
			setState(74);
			body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParadclsContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(MCParser.LP, 0); }
		public ParalistContext paralist() {
			return getRuleContext(ParalistContext.class,0);
		}
		public TerminalNode RP() { return getToken(MCParser.RP, 0); }
		public ParadclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paradcls; }
	}

	public final ParadclsContext paradcls() throws RecognitionException {
		ParadclsContext _localctx = new ParadclsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_paradcls);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(LP);
			setState(77);
			paralist();
			setState(78);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParalistContext extends ParserRuleContext {
		public ParaContext para() {
			return getRuleContext(ParaContext.class,0);
		}
		public ParatailContext paratail() {
			return getRuleContext(ParatailContext.class,0);
		}
		public ParalistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paralist; }
	}

	public final ParalistContext paralist() throws RecognitionException {
		ParalistContext _localctx = new ParalistContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_paralist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INT || _la==FLOAT) {
				{
				setState(80);
				para();
				setState(81);
				paratail();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParatailContext extends ParserRuleContext {
		public TerminalNode SM() { return getToken(MCParser.SM, 0); }
		public ParaContext para() {
			return getRuleContext(ParaContext.class,0);
		}
		public ParatailContext paratail() {
			return getRuleContext(ParatailContext.class,0);
		}
		public ParatailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paratail; }
	}

	public final ParatailContext paratail() throws RecognitionException {
		ParatailContext _localctx = new ParatailContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_paratail);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SM) {
				{
				setState(85);
				match(SM);
				setState(86);
				para();
				setState(87);
				paratail();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParaContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public ParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para; }
	}

	public final ParaContext para() throws RecognitionException {
		ParaContext _localctx = new ParaContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_para);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			type();
			setState(92);
			idlist();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BodyContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(MCParser.LB, 0); }
		public Vardcl_stmt_listContext vardcl_stmt_list() {
			return getRuleContext(Vardcl_stmt_listContext.class,0);
		}
		public TerminalNode RB() { return getToken(MCParser.RB, 0); }
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(LB);
			setState(95);
			vardcl_stmt_list();
			setState(96);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Vardcl_stmt_listContext extends ParserRuleContext {
		public Vardcl_stmtContext vardcl_stmt() {
			return getRuleContext(Vardcl_stmtContext.class,0);
		}
		public Vardcl_stmt_listContext vardcl_stmt_list() {
			return getRuleContext(Vardcl_stmt_listContext.class,0);
		}
		public Vardcl_stmt_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardcl_stmt_list; }
	}

	public final Vardcl_stmt_listContext vardcl_stmt_list() throws RecognitionException {
		Vardcl_stmt_listContext _localctx = new Vardcl_stmt_listContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_vardcl_stmt_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << INT) | (1L << FLOAT) | (1L << RETURN))) != 0)) {
				{
				setState(98);
				vardcl_stmt();
				setState(99);
				vardcl_stmt_list();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Vardcl_stmtContext extends ParserRuleContext {
		public VardclsContext vardcls() {
			return getRuleContext(VardclsContext.class,0);
		}
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public Vardcl_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardcl_stmt; }
	}

	public final Vardcl_stmtContext vardcl_stmt() throws RecognitionException {
		Vardcl_stmtContext _localctx = new Vardcl_stmtContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_vardcl_stmt);
		try {
			setState(105);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				vardcls();
				}
				break;
			case ID:
			case RETURN:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public TerminalNode SM() { return getToken(MCParser.SM, 0); }
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public Return_tContext return_t() {
			return getRuleContext(Return_tContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_stmt);
		try {
			setState(116);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(107);
				assign();
				setState(108);
				match(SM);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(110);
				call();
				setState(111);
				match(SM);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(113);
				return_t();
				setState(114);
				match(SM);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode EQ() { return getToken(MCParser.EQ, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(ID);
			setState(119);
			match(EQ);
			setState(120);
			exp(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LP() { return getToken(MCParser.LP, 0); }
		public ExplistContext explist() {
			return getRuleContext(ExplistContext.class,0);
		}
		public TerminalNode RP() { return getToken(MCParser.RP, 0); }
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(ID);
			setState(123);
			match(LP);
			setState(124);
			explist();
			setState(125);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExplistContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public ExptailContext exptail() {
			return getRuleContext(ExptailContext.class,0);
		}
		public ExplistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_explist; }
	}

	public final ExplistContext explist() throws RecognitionException {
		ExplistContext _localctx = new ExplistContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_explist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << INTLIT) | (1L << FLOATLIT) | (1L << LP))) != 0)) {
				{
				setState(127);
				exp(0);
				setState(128);
				exptail();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExptailContext extends ParserRuleContext {
		public TerminalNode CM() { return getToken(MCParser.CM, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public ExptailContext exptail() {
			return getRuleContext(ExptailContext.class,0);
		}
		public ExptailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exptail; }
	}

	public final ExptailContext exptail() throws RecognitionException {
		ExptailContext _localctx = new ExptailContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_exptail);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CM) {
				{
				setState(132);
				match(CM);
				setState(133);
				exp(0);
				setState(134);
				exptail();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_tContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(MCParser.RETURN, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Return_tContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_t; }
	}

	public final Return_tContext return_t() throws RecognitionException {
		Return_tContext _localctx = new Return_tContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_return_t);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(RETURN);
			setState(139);
			exp(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public List<OperandContext> operand() {
			return getRuleContexts(OperandContext.class);
		}
		public OperandContext operand(int i) {
			return getRuleContext(OperandContext.class,i);
		}
		public TerminalNode SUB() { return getToken(MCParser.SUB, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public TerminalNode MUL() { return getToken(MCParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(MCParser.DIV, 0); }
		public TerminalNode ADD() { return getToken(MCParser.ADD, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		return exp(0);
	}

	private ExpContext exp(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpContext _localctx = new ExpContext(_ctx, _parentState);
		ExpContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_exp, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(142);
				operand();
				}
				break;
			case 2:
				{
				setState(143);
				operand();
				setState(144);
				match(SUB);
				setState(145);
				operand();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(157);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(155);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
					case 1:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(149);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(150);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(151);
						exp(4);
						}
						break;
					case 2:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(152);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(153);
						match(ADD);
						setState(154);
						exp(1);
						}
						break;
					}
					} 
				}
				setState(159);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class OperandContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(MCParser.INTLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(MCParser.FLOATLIT, 0); }
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public SubexpContext subexp() {
			return getRuleContext(SubexpContext.class,0);
		}
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_operand);
		try {
			setState(165);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(160);
				match(INTLIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(161);
				match(FLOATLIT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(162);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(163);
				call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(164);
				subexp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubexpContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(MCParser.LP, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RP() { return getToken(MCParser.RP, 0); }
		public SubexpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subexp; }
	}

	public final SubexpContext subexp() throws RecognitionException {
		SubexpContext _localctx = new SubexpContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_subexp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(LP);
			setState(168);
			exp(0);
			setState(169);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 20:
			return exp_sempred((ExpContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp_sempred(ExpContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31\u00ae\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\3\5\38\n\3\3\4\3\4\5\4<\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3"+
		"\7\3\7\3\7\3\7\5\7H\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\5\nV\n\n\3\13\3\13\3\13\3\13\5\13\\\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3"+
		"\r\3\16\3\16\3\16\5\16h\n\16\3\17\3\17\5\17l\n\17\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\5\20w\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22"+
		"\3\22\3\22\3\23\3\23\3\23\5\23\u0085\n\23\3\24\3\24\3\24\3\24\5\24\u008b"+
		"\n\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0096\n\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\7\26\u009e\n\26\f\26\16\26\u00a1\13\26\3\27"+
		"\3\27\3\27\3\27\3\27\5\27\u00a8\n\27\3\30\3\30\3\30\3\30\3\30\2\3*\31"+
		"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\2\4\3\2\b\t\3\2\24\25"+
		"\2\u00a8\2\60\3\2\2\2\4\67\3\2\2\2\6;\3\2\2\2\b=\3\2\2\2\nA\3\2\2\2\f"+
		"G\3\2\2\2\16I\3\2\2\2\20N\3\2\2\2\22U\3\2\2\2\24[\3\2\2\2\26]\3\2\2\2"+
		"\30`\3\2\2\2\32g\3\2\2\2\34k\3\2\2\2\36v\3\2\2\2 x\3\2\2\2\"|\3\2\2\2"+
		"$\u0084\3\2\2\2&\u008a\3\2\2\2(\u008c\3\2\2\2*\u0095\3\2\2\2,\u00a7\3"+
		"\2\2\2.\u00a9\3\2\2\2\60\61\5\4\3\2\61\62\7\2\2\3\62\3\3\2\2\2\63\64\5"+
		"\6\4\2\64\65\5\4\3\2\658\3\2\2\2\668\5\6\4\2\67\63\3\2\2\2\67\66\3\2\2"+
		"\28\5\3\2\2\29<\5\b\5\2:<\5\16\b\2;9\3\2\2\2;:\3\2\2\2<\7\3\2\2\2=>\5"+
		"\n\6\2>?\5\f\7\2?@\7\17\2\2@\t\3\2\2\2AB\t\2\2\2B\13\3\2\2\2CD\7\3\2\2"+
		"DE\7\20\2\2EH\5\f\7\2FH\7\3\2\2GC\3\2\2\2GF\3\2\2\2H\r\3\2\2\2IJ\5\n\6"+
		"\2JK\7\3\2\2KL\5\20\t\2LM\5\30\r\2M\17\3\2\2\2NO\7\r\2\2OP\5\22\n\2PQ"+
		"\7\16\2\2Q\21\3\2\2\2RS\5\26\f\2ST\5\24\13\2TV\3\2\2\2UR\3\2\2\2UV\3\2"+
		"\2\2V\23\3\2\2\2WX\7\17\2\2XY\5\26\f\2YZ\5\24\13\2Z\\\3\2\2\2[W\3\2\2"+
		"\2[\\\3\2\2\2\\\25\3\2\2\2]^\5\n\6\2^_\5\f\7\2_\27\3\2\2\2`a\7\13\2\2"+
		"ab\5\32\16\2bc\7\f\2\2c\31\3\2\2\2de\5\34\17\2ef\5\32\16\2fh\3\2\2\2g"+
		"d\3\2\2\2gh\3\2\2\2h\33\3\2\2\2il\5\b\5\2jl\5\36\20\2ki\3\2\2\2kj\3\2"+
		"\2\2l\35\3\2\2\2mn\5 \21\2no\7\17\2\2ow\3\2\2\2pq\5\"\22\2qr\7\17\2\2"+
		"rw\3\2\2\2st\5(\25\2tu\7\17\2\2uw\3\2\2\2vm\3\2\2\2vp\3\2\2\2vs\3\2\2"+
		"\2w\37\3\2\2\2xy\7\3\2\2yz\7\21\2\2z{\5*\26\2{!\3\2\2\2|}\7\3\2\2}~\7"+
		"\r\2\2~\177\5$\23\2\177\u0080\7\16\2\2\u0080#\3\2\2\2\u0081\u0082\5*\26"+
		"\2\u0082\u0083\5&\24\2\u0083\u0085\3\2\2\2\u0084\u0081\3\2\2\2\u0084\u0085"+
		"\3\2\2\2\u0085%\3\2\2\2\u0086\u0087\7\20\2\2\u0087\u0088\5*\26\2\u0088"+
		"\u0089\5&\24\2\u0089\u008b\3\2\2\2\u008a\u0086\3\2\2\2\u008a\u008b\3\2"+
		"\2\2\u008b\'\3\2\2\2\u008c\u008d\7\n\2\2\u008d\u008e\5*\26\2\u008e)\3"+
		"\2\2\2\u008f\u0090\b\26\1\2\u0090\u0096\5,\27\2\u0091\u0092\5,\27\2\u0092"+
		"\u0093\7\23\2\2\u0093\u0094\5,\27\2\u0094\u0096\3\2\2\2\u0095\u008f\3"+
		"\2\2\2\u0095\u0091\3\2\2\2\u0096\u009f\3\2\2\2\u0097\u0098\f\5\2\2\u0098"+
		"\u0099\t\3\2\2\u0099\u009e\5*\26\6\u009a\u009b\f\3\2\2\u009b\u009c\7\22"+
		"\2\2\u009c\u009e\5*\26\3\u009d\u0097\3\2\2\2\u009d\u009a\3\2\2\2\u009e"+
		"\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0+\3\2\2\2"+
		"\u00a1\u009f\3\2\2\2\u00a2\u00a8\7\4\2\2\u00a3\u00a8\7\7\2\2\u00a4\u00a8"+
		"\7\3\2\2\u00a5\u00a8\5\"\22\2\u00a6\u00a8\5.\30\2\u00a7\u00a2\3\2\2\2"+
		"\u00a7\u00a3\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6"+
		"\3\2\2\2\u00a8-\3\2\2\2\u00a9\u00aa\7\r\2\2\u00aa\u00ab\5*\26\2\u00ab"+
		"\u00ac\7\16\2\2\u00ac/\3\2\2\2\20\67;GU[gkv\u0084\u008a\u0095\u009d\u009f"+
		"\u00a7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}