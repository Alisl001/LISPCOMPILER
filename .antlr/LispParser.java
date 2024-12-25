// Generated from c:/antlr/LispCompiler/LispParser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LispParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		STRING=1, NUMBER=2, DEFUN=3, IF=4, COND=5, LET=6, QUOTE=7, PRINT=8, DEFPARAMETER=9, 
		LAMBDA=10, FORMAT=11, AND=12, OR=13, NOT=14, ELSE=15, IDENTIFIER=16, PLUS=17, 
		MINUS=18, DIV=19, MOD=20, GREATER_EQUAL=21, LESS_EQUAL=22, GREATER=23, 
		LESS=24, EQUAL=25, LPAREN=26, RPAREN=27, TRUE=28, FALSE=29, COMMENT=30, 
		WS=31, ERROR=32, MULT=33;
	public static final int
		RULE_program = 0, RULE_expression = 1, RULE_funcall = 2, RULE_operation = 3, 
		RULE_lambda = 4, RULE_conditional = 5, RULE_condClause = 6, RULE_formatCall = 7, 
		RULE_params = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "expression", "funcall", "operation", "lambda", "conditional", 
			"condClause", "formatCall", "params"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'defun'", "'if'", "'cond'", "'let'", "'quote'", "'print'", 
			"'defparameter'", "'lambda'", "'format'", "'and'", "'or'", "'not'", "'else'", 
			null, "'+'", "'-'", "'/'", "'%'", "'>='", "'<='", "'>'", "'<'", "'='", 
			"'('", "')'", "'true'", "'false'", null, null, null, "'*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "STRING", "NUMBER", "DEFUN", "IF", "COND", "LET", "QUOTE", "PRINT", 
			"DEFPARAMETER", "LAMBDA", "FORMAT", "AND", "OR", "NOT", "ELSE", "IDENTIFIER", 
			"PLUS", "MINUS", "DIV", "MOD", "GREATER_EQUAL", "LESS_EQUAL", "GREATER", 
			"LESS", "EQUAL", "LPAREN", "RPAREN", "TRUE", "FALSE", "COMMENT", "WS", 
			"ERROR", "MULT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
	public String getGrammarFileName() { return "LispParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


	  from ASTNodes import *

	  def build_program(self, expressions):
	      program = ProgramNode()
	      for expr in expressions:
	          program.add_child(expr)
	      return program

	public LispParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public ASTNode node;
		public ExpressionContext expression;
		public List<ExpressionContext> exprs = new ArrayList<ExpressionContext>();
		public TerminalNode EOF() { return getToken(LispParser.EOF, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 67174406L) != 0)) {
				{
				{
				setState(18);
				((ProgramContext)_localctx).expression = expression();
				((ProgramContext)_localctx).exprs.add(((ProgramContext)_localctx).expression);
				}
				}
				setState(23);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(24);
			match(EOF);
			 ((ProgramContext)_localctx).node =  self.build_program(((ProgramContext)_localctx).exprs); 
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

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ASTNode node;
		public Token STRING;
		public Token NUMBER;
		public Token IDENTIFIER;
		public LambdaContext lambda;
		public FuncallContext funcall;
		public ConditionalContext conditional;
		public OperationContext operation;
		public FormatCallContext formatCall;
		public TerminalNode STRING() { return getToken(LispParser.STRING, 0); }
		public TerminalNode NUMBER() { return getToken(LispParser.NUMBER, 0); }
		public TerminalNode IDENTIFIER() { return getToken(LispParser.IDENTIFIER, 0); }
		public LambdaContext lambda() {
			return getRuleContext(LambdaContext.class,0);
		}
		public FuncallContext funcall() {
			return getRuleContext(FuncallContext.class,0);
		}
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public FormatCallContext formatCall() {
			return getRuleContext(FormatCallContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expression);
		try {
			setState(48);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				((ExpressionContext)_localctx).STRING = match(STRING);
				 ((ExpressionContext)_localctx).node =  LiteralNode((((ExpressionContext)_localctx).STRING!=null?((ExpressionContext)_localctx).STRING.getText():null)); 
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				((ExpressionContext)_localctx).NUMBER = match(NUMBER);
				 ((ExpressionContext)_localctx).node =  LiteralNode((((ExpressionContext)_localctx).NUMBER!=null?((ExpressionContext)_localctx).NUMBER.getText():null)); 
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(31);
				((ExpressionContext)_localctx).IDENTIFIER = match(IDENTIFIER);
				 ((ExpressionContext)_localctx).node =  IdentifierNode((((ExpressionContext)_localctx).IDENTIFIER!=null?((ExpressionContext)_localctx).IDENTIFIER.getText():null)); 
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(33);
				((ExpressionContext)_localctx).lambda = lambda();
				 ((ExpressionContext)_localctx).node =  ((ExpressionContext)_localctx).lambda.node; 
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(36);
				((ExpressionContext)_localctx).funcall = funcall();
				 ((ExpressionContext)_localctx).node =  ((ExpressionContext)_localctx).funcall.node; 
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(39);
				((ExpressionContext)_localctx).conditional = conditional();
				 ((ExpressionContext)_localctx).node =  ((ExpressionContext)_localctx).conditional.node; 
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(42);
				((ExpressionContext)_localctx).operation = operation();
				 ((ExpressionContext)_localctx).node =  ((ExpressionContext)_localctx).operation.node; 
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(45);
				((ExpressionContext)_localctx).formatCall = formatCall();
				 ((ExpressionContext)_localctx).node =  ((ExpressionContext)_localctx).formatCall.node; 
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

	@SuppressWarnings("CheckReturnValue")
	public static class FuncallContext extends ParserRuleContext {
		public ASTNode node;
		public Token IDENTIFIER;
		public ExpressionContext expression;
		public List<ExpressionContext> exprs = new ArrayList<ExpressionContext>();
		public TerminalNode LPAREN() { return getToken(LispParser.LPAREN, 0); }
		public TerminalNode IDENTIFIER() { return getToken(LispParser.IDENTIFIER, 0); }
		public TerminalNode RPAREN() { return getToken(LispParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FuncallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcall; }
	}

	public final FuncallContext funcall() throws RecognitionException {
		FuncallContext _localctx = new FuncallContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_funcall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(LPAREN);
			setState(51);
			((FuncallContext)_localctx).IDENTIFIER = match(IDENTIFIER);
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 67174406L) != 0)) {
				{
				{
				setState(52);
				((FuncallContext)_localctx).expression = expression();
				((FuncallContext)_localctx).exprs.add(((FuncallContext)_localctx).expression);
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(58);
			match(RPAREN);

			        func = FunctionCallNode((((FuncallContext)_localctx).IDENTIFIER!=null?((FuncallContext)_localctx).IDENTIFIER.getText():null))
			        for expr in ((FuncallContext)_localctx).exprs:
			            func.add_child(expr)
			        ((FuncallContext)_localctx).node =  func;
			    
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

	@SuppressWarnings("CheckReturnValue")
	public static class OperationContext extends ParserRuleContext {
		public ASTNode node;
		public Token op;
		public ExpressionContext expression;
		public List<ExpressionContext> exprs = new ArrayList<ExpressionContext>();
		public TerminalNode LPAREN() { return getToken(LispParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(LispParser.RPAREN, 0); }
		public TerminalNode PLUS() { return getToken(LispParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(LispParser.MINUS, 0); }
		public TerminalNode MULT() { return getToken(LispParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(LispParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(LispParser.MOD, 0); }
		public TerminalNode GREATER_EQUAL() { return getToken(LispParser.GREATER_EQUAL, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(LispParser.LESS_EQUAL, 0); }
		public TerminalNode GREATER() { return getToken(LispParser.GREATER, 0); }
		public TerminalNode LESS() { return getToken(LispParser.LESS, 0); }
		public TerminalNode EQUAL() { return getToken(LispParser.EQUAL, 0); }
		public TerminalNode AND() { return getToken(LispParser.AND, 0); }
		public TerminalNode OR() { return getToken(LispParser.OR, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_operation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(LPAREN);
			setState(62);
			((OperationContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8656924672L) != 0)) ) {
				((OperationContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(64); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(63);
				((OperationContext)_localctx).expression = expression();
				((OperationContext)_localctx).exprs.add(((OperationContext)_localctx).expression);
				}
				}
				setState(66); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 67174406L) != 0) );
			setState(68);
			match(RPAREN);

			        operation = OperationNode((((OperationContext)_localctx).op!=null?((OperationContext)_localctx).op.getText():null))
			        for expr in ((OperationContext)_localctx).exprs:
			            operation.add_child(expr)
			        ((OperationContext)_localctx).node =  operation;
			    
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

	@SuppressWarnings("CheckReturnValue")
	public static class LambdaContext extends ParserRuleContext {
		public ASTNode node;
		public ParamsContext params;
		public ExpressionContext expression;
		public List<TerminalNode> LPAREN() { return getTokens(LispParser.LPAREN); }
		public TerminalNode LPAREN(int i) {
			return getToken(LispParser.LPAREN, i);
		}
		public TerminalNode LAMBDA() { return getToken(LispParser.LAMBDA, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public List<TerminalNode> RPAREN() { return getTokens(LispParser.RPAREN); }
		public TerminalNode RPAREN(int i) {
			return getToken(LispParser.RPAREN, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LambdaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lambda; }
	}

	public final LambdaContext lambda() throws RecognitionException {
		LambdaContext _localctx = new LambdaContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_lambda);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(LPAREN);
			setState(72);
			match(LAMBDA);
			setState(73);
			match(LPAREN);
			setState(74);
			((LambdaContext)_localctx).params = params();
			setState(75);
			match(RPAREN);
			setState(76);
			((LambdaContext)_localctx).expression = expression();
			setState(77);
			match(RPAREN);

			        lambda_node = LambdaNode()
			        if ((LambdaContext)_localctx).params.node:
			            lambda_node.add_child(((LambdaContext)_localctx).params.node)
			        lambda_node.add_child(((LambdaContext)_localctx).expression.node)
			        ((LambdaContext)_localctx).node =  lambda_node;
			    
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

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionalContext extends ParserRuleContext {
		public ASTNode node;
		public ExpressionContext test;
		public ExpressionContext then;
		public ExpressionContext else_;
		public CondClauseContext condClause;
		public List<CondClauseContext> clauses = new ArrayList<CondClauseContext>();
		public TerminalNode LPAREN() { return getToken(LispParser.LPAREN, 0); }
		public TerminalNode IF() { return getToken(LispParser.IF, 0); }
		public TerminalNode RPAREN() { return getToken(LispParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode COND() { return getToken(LispParser.COND, 0); }
		public List<CondClauseContext> condClause() {
			return getRuleContexts(CondClauseContext.class);
		}
		public CondClauseContext condClause(int i) {
			return getRuleContext(CondClauseContext.class,i);
		}
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_conditional);
		int _la;
		try {
			setState(100);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(80);
				match(LPAREN);
				setState(81);
				match(IF);
				setState(82);
				((ConditionalContext)_localctx).test = expression();
				setState(83);
				((ConditionalContext)_localctx).then = expression();
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 67174406L) != 0)) {
					{
					setState(84);
					((ConditionalContext)_localctx).else_ = expression();
					}
				}

				setState(87);
				match(RPAREN);

				        conditional_node = ConditionalNode("if")
				        conditional_node.add_child(((ConditionalContext)_localctx).test.node)
				        conditional_node.add_child(((ConditionalContext)_localctx).then.node)
				        if (((ConditionalContext)_localctx).else_.node != null) {
				            conditional_node.add_child(((ConditionalContext)_localctx).else_.node);
				        }
				        ((ConditionalContext)_localctx).node =  conditional_node;
				    
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(90);
				match(LPAREN);
				setState(91);
				match(COND);
				setState(93); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(92);
					((ConditionalContext)_localctx).condClause = condClause();
					((ConditionalContext)_localctx).clauses.add(((ConditionalContext)_localctx).condClause);
					}
					}
					setState(95); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LPAREN );
				setState(97);
				match(RPAREN);

				        cond_node = ConditionalNode("cond")
				        for clause in ((ConditionalContext)_localctx).clauses:
				            cond_node.add_child(clause.node)
				        ((ConditionalContext)_localctx).node =  cond_node;
				    
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

	@SuppressWarnings("CheckReturnValue")
	public static class CondClauseContext extends ParserRuleContext {
		public ASTNode node;
		public ExpressionContext test;
		public ExpressionContext result;
		public TerminalNode LPAREN() { return getToken(LispParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(LispParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public CondClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condClause; }
	}

	public final CondClauseContext condClause() throws RecognitionException {
		CondClauseContext _localctx = new CondClauseContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_condClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(LPAREN);
			setState(103);
			((CondClauseContext)_localctx).test = expression();
			setState(104);
			((CondClauseContext)_localctx).result = expression();
			setState(105);
			match(RPAREN);

			        clause_node = CondClauseNode()
			        clause_node.add_child(((CondClauseContext)_localctx).test.node)
			        clause_node.add_child(((CondClauseContext)_localctx).result.node)
			        ((CondClauseContext)_localctx).node =  clause_node;
			    
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

	@SuppressWarnings("CheckReturnValue")
	public static class FormatCallContext extends ParserRuleContext {
		public ASTNode node;
		public ExpressionContext format_string;
		public ExpressionContext expression;
		public List<ExpressionContext> args = new ArrayList<ExpressionContext>();
		public TerminalNode LPAREN() { return getToken(LispParser.LPAREN, 0); }
		public TerminalNode FORMAT() { return getToken(LispParser.FORMAT, 0); }
		public TerminalNode RPAREN() { return getToken(LispParser.RPAREN, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FormatCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formatCall; }
	}

	public final FormatCallContext formatCall() throws RecognitionException {
		FormatCallContext _localctx = new FormatCallContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_formatCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(LPAREN);
			setState(109);
			match(FORMAT);
			setState(110);
			((FormatCallContext)_localctx).format_string = expression();
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 67174406L) != 0)) {
				{
				{
				setState(111);
				((FormatCallContext)_localctx).expression = expression();
				((FormatCallContext)_localctx).args.add(((FormatCallContext)_localctx).expression);
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(117);
			match(RPAREN);

			        format_node = FormatCallNode()
			        format_node.add_child(((FormatCallContext)_localctx).format_string.node)
			        for arg in ((FormatCallContext)_localctx).args:
			            format_node.add_child(arg.node)  // Ensure access to `node`
			        ((FormatCallContext)_localctx).node =  format_node;
			    
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

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public ASTNode node;
		public Token IDENTIFIER;
		public List<Token> ids = new ArrayList<Token>();
		public List<TerminalNode> IDENTIFIER() { return getTokens(LispParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(LispParser.IDENTIFIER, i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(120);
				((ParamsContext)_localctx).IDENTIFIER = match(IDENTIFIER);
				((ParamsContext)_localctx).ids.add(((ParamsContext)_localctx).IDENTIFIER);
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}

			        params_node = ParameterListNode()
			        for id in ((ParamsContext)_localctx).ids:
			            params_node.add_child(IdentifierNode(id.text))
			        ((ParamsContext)_localctx).node =  params_node;
			    
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

	public static final String _serializedATN =
		"\u0004\u0001!\u0081\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0001\u0000\u0005\u0000\u0014\b\u0000\n\u0000\f\u0000\u0017"+
		"\t\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u00011\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005"+
		"\u00026\b\u0002\n\u0002\f\u00029\t\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0004\u0003A\b\u0003\u000b"+
		"\u0003\f\u0003B\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0003\u0005V\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0004\u0005^\b\u0005\u000b\u0005\f\u0005"+
		"_\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005e\b\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0005\u0007q\b\u0007\n\u0007\f\u0007"+
		"t\t\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0005\bz\b\b\n\b"+
		"\f\b}\t\b\u0001\b\u0001\b\u0001\b\u0000\u0000\t\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0000\u0001\u0003\u0000\f\r\u0011\u0019!!\u0086\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u00020\u0001\u0000\u0000\u0000\u00042\u0001"+
		"\u0000\u0000\u0000\u0006=\u0001\u0000\u0000\u0000\bG\u0001\u0000\u0000"+
		"\u0000\nd\u0001\u0000\u0000\u0000\ff\u0001\u0000\u0000\u0000\u000el\u0001"+
		"\u0000\u0000\u0000\u0010{\u0001\u0000\u0000\u0000\u0012\u0014\u0003\u0002"+
		"\u0001\u0000\u0013\u0012\u0001\u0000\u0000\u0000\u0014\u0017\u0001\u0000"+
		"\u0000\u0000\u0015\u0013\u0001\u0000\u0000\u0000\u0015\u0016\u0001\u0000"+
		"\u0000\u0000\u0016\u0018\u0001\u0000\u0000\u0000\u0017\u0015\u0001\u0000"+
		"\u0000\u0000\u0018\u0019\u0005\u0000\u0000\u0001\u0019\u001a\u0006\u0000"+
		"\uffff\uffff\u0000\u001a\u0001\u0001\u0000\u0000\u0000\u001b\u001c\u0005"+
		"\u0001\u0000\u0000\u001c1\u0006\u0001\uffff\uffff\u0000\u001d\u001e\u0005"+
		"\u0002\u0000\u0000\u001e1\u0006\u0001\uffff\uffff\u0000\u001f \u0005\u0010"+
		"\u0000\u0000 1\u0006\u0001\uffff\uffff\u0000!\"\u0003\b\u0004\u0000\""+
		"#\u0006\u0001\uffff\uffff\u0000#1\u0001\u0000\u0000\u0000$%\u0003\u0004"+
		"\u0002\u0000%&\u0006\u0001\uffff\uffff\u0000&1\u0001\u0000\u0000\u0000"+
		"\'(\u0003\n\u0005\u0000()\u0006\u0001\uffff\uffff\u0000)1\u0001\u0000"+
		"\u0000\u0000*+\u0003\u0006\u0003\u0000+,\u0006\u0001\uffff\uffff\u0000"+
		",1\u0001\u0000\u0000\u0000-.\u0003\u000e\u0007\u0000./\u0006\u0001\uffff"+
		"\uffff\u0000/1\u0001\u0000\u0000\u00000\u001b\u0001\u0000\u0000\u0000"+
		"0\u001d\u0001\u0000\u0000\u00000\u001f\u0001\u0000\u0000\u00000!\u0001"+
		"\u0000\u0000\u00000$\u0001\u0000\u0000\u00000\'\u0001\u0000\u0000\u0000"+
		"0*\u0001\u0000\u0000\u00000-\u0001\u0000\u0000\u00001\u0003\u0001\u0000"+
		"\u0000\u000023\u0005\u001a\u0000\u000037\u0005\u0010\u0000\u000046\u0003"+
		"\u0002\u0001\u000054\u0001\u0000\u0000\u000069\u0001\u0000\u0000\u0000"+
		"75\u0001\u0000\u0000\u000078\u0001\u0000\u0000\u00008:\u0001\u0000\u0000"+
		"\u000097\u0001\u0000\u0000\u0000:;\u0005\u001b\u0000\u0000;<\u0006\u0002"+
		"\uffff\uffff\u0000<\u0005\u0001\u0000\u0000\u0000=>\u0005\u001a\u0000"+
		"\u0000>@\u0007\u0000\u0000\u0000?A\u0003\u0002\u0001\u0000@?\u0001\u0000"+
		"\u0000\u0000AB\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BC\u0001"+
		"\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000DE\u0005\u001b\u0000\u0000"+
		"EF\u0006\u0003\uffff\uffff\u0000F\u0007\u0001\u0000\u0000\u0000GH\u0005"+
		"\u001a\u0000\u0000HI\u0005\n\u0000\u0000IJ\u0005\u001a\u0000\u0000JK\u0003"+
		"\u0010\b\u0000KL\u0005\u001b\u0000\u0000LM\u0003\u0002\u0001\u0000MN\u0005"+
		"\u001b\u0000\u0000NO\u0006\u0004\uffff\uffff\u0000O\t\u0001\u0000\u0000"+
		"\u0000PQ\u0005\u001a\u0000\u0000QR\u0005\u0004\u0000\u0000RS\u0003\u0002"+
		"\u0001\u0000SU\u0003\u0002\u0001\u0000TV\u0003\u0002\u0001\u0000UT\u0001"+
		"\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000"+
		"WX\u0005\u001b\u0000\u0000XY\u0006\u0005\uffff\uffff\u0000Ye\u0001\u0000"+
		"\u0000\u0000Z[\u0005\u001a\u0000\u0000[]\u0005\u0005\u0000\u0000\\^\u0003"+
		"\f\u0006\u0000]\\\u0001\u0000\u0000\u0000^_\u0001\u0000\u0000\u0000_]"+
		"\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000"+
		"\u0000ab\u0005\u001b\u0000\u0000bc\u0006\u0005\uffff\uffff\u0000ce\u0001"+
		"\u0000\u0000\u0000dP\u0001\u0000\u0000\u0000dZ\u0001\u0000\u0000\u0000"+
		"e\u000b\u0001\u0000\u0000\u0000fg\u0005\u001a\u0000\u0000gh\u0003\u0002"+
		"\u0001\u0000hi\u0003\u0002\u0001\u0000ij\u0005\u001b\u0000\u0000jk\u0006"+
		"\u0006\uffff\uffff\u0000k\r\u0001\u0000\u0000\u0000lm\u0005\u001a\u0000"+
		"\u0000mn\u0005\u000b\u0000\u0000nr\u0003\u0002\u0001\u0000oq\u0003\u0002"+
		"\u0001\u0000po\u0001\u0000\u0000\u0000qt\u0001\u0000\u0000\u0000rp\u0001"+
		"\u0000\u0000\u0000rs\u0001\u0000\u0000\u0000su\u0001\u0000\u0000\u0000"+
		"tr\u0001\u0000\u0000\u0000uv\u0005\u001b\u0000\u0000vw\u0006\u0007\uffff"+
		"\uffff\u0000w\u000f\u0001\u0000\u0000\u0000xz\u0005\u0010\u0000\u0000"+
		"yx\u0001\u0000\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000"+
		"\u0000{|\u0001\u0000\u0000\u0000|~\u0001\u0000\u0000\u0000}{\u0001\u0000"+
		"\u0000\u0000~\u007f\u0006\b\uffff\uffff\u0000\u007f\u0011\u0001\u0000"+
		"\u0000\u0000\t\u001507BU_dr{";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}