// Generated from c:/antlr/LispCompiler/LispLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class LispLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		STRING=1, NUMBER=2, DEFUN=3, IF=4, COND=5, LET=6, QUOTE=7, PRINT=8, DEFPARAMETER=9, 
		IDENTIFIER=10, PLUS=11, MINUS=12, DIV=13, MOD=14, LPAREN=15, RPAREN=16, 
		TRUE=17, FALSE=18, COMMENT=19, WS=20, ERROR=21, MULT=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"STRING", "ESC_SEQ", "NUMBER", "DEFUN", "IF", "COND", "LET", "QUOTE", 
			"PRINT", "DEFPARAMETER", "IDENTIFIER", "PLUS", "MINUS", "MULT", "DIV", 
			"MOD", "LPAREN", "RPAREN", "TRUE", "FALSE", "COMMENT", "WS", "ERROR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'defun'", "'if'", "'cond'", "'let'", "'quote'", "'print'", 
			"'defparameter'", null, "'+'", "'-'", "'/'", "'%'", "'('", "')'", "'true'", 
			"'false'", null, null, null, "'*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "STRING", "NUMBER", "DEFUN", "IF", "COND", "LET", "QUOTE", "PRINT", 
			"DEFPARAMETER", "IDENTIFIER", "PLUS", "MINUS", "DIV", "MOD", "LPAREN", 
			"RPAREN", "TRUE", "FALSE", "COMMENT", "WS", "ERROR", "MULT"
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


	public LispLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "LispLexer.g4"; }

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
		"\u0004\u0000\u0016\u00aa\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0005\u00003\b\u0000\n\u0000\f\u00006\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0004\u0002"+
		">\b\u0002\u000b\u0002\f\u0002?\u0001\u0002\u0001\u0002\u0004\u0002D\b"+
		"\u0002\u000b\u0002\f\u0002E\u0003\u0002H\b\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0005\nw\b\n\n\n\f\nz\t\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0005\u0014"+
		"\u0099\b\u0014\n\u0014\f\u0014\u009c\t\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0015\u0004\u0015\u00a3\b\u0015\u000b\u0015\f"+
		"\u0015\u00a4\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u009a"+
		"\u0000\u0017\u0001\u0001\u0003\u0000\u0005\u0002\u0007\u0003\t\u0004\u000b"+
		"\u0005\r\u0006\u000f\u0007\u0011\b\u0013\t\u0015\n\u0017\u000b\u0019\f"+
		"\u001b\u0016\u001d\r\u001f\u000e!\u000f#\u0010%\u0011\'\u0012)\u0013+"+
		"\u0014-\u0015\u0001\u0000\u0006\u0002\u0000\"\"\\\\\u0007\u0000\"\"\'"+
		"\'\\\\bbnnrrtt\u0001\u000009\u0003\u0000AZ__az\u0006\u0000**--09AZ__a"+
		"z\u0003\u0000\t\n\r\r  \u00b0\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0001/"+
		"\u0001\u0000\u0000\u0000\u00039\u0001\u0000\u0000\u0000\u0005=\u0001\u0000"+
		"\u0000\u0000\u0007I\u0001\u0000\u0000\u0000\tO\u0001\u0000\u0000\u0000"+
		"\u000bR\u0001\u0000\u0000\u0000\rW\u0001\u0000\u0000\u0000\u000f[\u0001"+
		"\u0000\u0000\u0000\u0011a\u0001\u0000\u0000\u0000\u0013g\u0001\u0000\u0000"+
		"\u0000\u0015t\u0001\u0000\u0000\u0000\u0017{\u0001\u0000\u0000\u0000\u0019"+
		"}\u0001\u0000\u0000\u0000\u001b\u007f\u0001\u0000\u0000\u0000\u001d\u0083"+
		"\u0001\u0000\u0000\u0000\u001f\u0085\u0001\u0000\u0000\u0000!\u0087\u0001"+
		"\u0000\u0000\u0000#\u0089\u0001\u0000\u0000\u0000%\u008b\u0001\u0000\u0000"+
		"\u0000\'\u0090\u0001\u0000\u0000\u0000)\u0096\u0001\u0000\u0000\u0000"+
		"+\u00a2\u0001\u0000\u0000\u0000-\u00a8\u0001\u0000\u0000\u0000/4\u0005"+
		"\"\u0000\u000003\u0003\u0003\u0001\u000013\b\u0000\u0000\u000020\u0001"+
		"\u0000\u0000\u000021\u0001\u0000\u0000\u000036\u0001\u0000\u0000\u0000"+
		"42\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u000057\u0001\u0000\u0000"+
		"\u000064\u0001\u0000\u0000\u000078\u0005\"\u0000\u00008\u0002\u0001\u0000"+
		"\u0000\u00009:\u0005\\\u0000\u0000:;\u0007\u0001\u0000\u0000;\u0004\u0001"+
		"\u0000\u0000\u0000<>\u0007\u0002\u0000\u0000=<\u0001\u0000\u0000\u0000"+
		">?\u0001\u0000\u0000\u0000?=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000"+
		"\u0000@G\u0001\u0000\u0000\u0000AC\u0005.\u0000\u0000BD\u0007\u0002\u0000"+
		"\u0000CB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000EC\u0001\u0000"+
		"\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0001\u0000\u0000\u0000GA\u0001"+
		"\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000H\u0006\u0001\u0000\u0000"+
		"\u0000IJ\u0005d\u0000\u0000JK\u0005e\u0000\u0000KL\u0005f\u0000\u0000"+
		"LM\u0005u\u0000\u0000MN\u0005n\u0000\u0000N\b\u0001\u0000\u0000\u0000"+
		"OP\u0005i\u0000\u0000PQ\u0005f\u0000\u0000Q\n\u0001\u0000\u0000\u0000"+
		"RS\u0005c\u0000\u0000ST\u0005o\u0000\u0000TU\u0005n\u0000\u0000UV\u0005"+
		"d\u0000\u0000V\f\u0001\u0000\u0000\u0000WX\u0005l\u0000\u0000XY\u0005"+
		"e\u0000\u0000YZ\u0005t\u0000\u0000Z\u000e\u0001\u0000\u0000\u0000[\\\u0005"+
		"q\u0000\u0000\\]\u0005u\u0000\u0000]^\u0005o\u0000\u0000^_\u0005t\u0000"+
		"\u0000_`\u0005e\u0000\u0000`\u0010\u0001\u0000\u0000\u0000ab\u0005p\u0000"+
		"\u0000bc\u0005r\u0000\u0000cd\u0005i\u0000\u0000de\u0005n\u0000\u0000"+
		"ef\u0005t\u0000\u0000f\u0012\u0001\u0000\u0000\u0000gh\u0005d\u0000\u0000"+
		"hi\u0005e\u0000\u0000ij\u0005f\u0000\u0000jk\u0005p\u0000\u0000kl\u0005"+
		"a\u0000\u0000lm\u0005r\u0000\u0000mn\u0005a\u0000\u0000no\u0005m\u0000"+
		"\u0000op\u0005e\u0000\u0000pq\u0005t\u0000\u0000qr\u0005e\u0000\u0000"+
		"rs\u0005r\u0000\u0000s\u0014\u0001\u0000\u0000\u0000tx\u0007\u0003\u0000"+
		"\u0000uw\u0007\u0004\u0000\u0000vu\u0001\u0000\u0000\u0000wz\u0001\u0000"+
		"\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000y\u0016"+
		"\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000{|\u0005+\u0000\u0000"+
		"|\u0018\u0001\u0000\u0000\u0000}~\u0005-\u0000\u0000~\u001a\u0001\u0000"+
		"\u0000\u0000\u007f\u0080\u0005*\u0000\u0000\u0080\u0081\u0001\u0000\u0000"+
		"\u0000\u0081\u0082\u0006\r\u0000\u0000\u0082\u001c\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0005/\u0000\u0000\u0084\u001e\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0005%\u0000\u0000\u0086 \u0001\u0000\u0000\u0000\u0087\u0088\u0005"+
		"(\u0000\u0000\u0088\"\u0001\u0000\u0000\u0000\u0089\u008a\u0005)\u0000"+
		"\u0000\u008a$\u0001\u0000\u0000\u0000\u008b\u008c\u0005t\u0000\u0000\u008c"+
		"\u008d\u0005r\u0000\u0000\u008d\u008e\u0005u\u0000\u0000\u008e\u008f\u0005"+
		"e\u0000\u0000\u008f&\u0001\u0000\u0000\u0000\u0090\u0091\u0005f\u0000"+
		"\u0000\u0091\u0092\u0005a\u0000\u0000\u0092\u0093\u0005l\u0000\u0000\u0093"+
		"\u0094\u0005s\u0000\u0000\u0094\u0095\u0005e\u0000\u0000\u0095(\u0001"+
		"\u0000\u0000\u0000\u0096\u009a\u0005;\u0000\u0000\u0097\u0099\t\u0000"+
		"\u0000\u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0099\u009c\u0001\u0000"+
		"\u0000\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009a\u0098\u0001\u0000"+
		"\u0000\u0000\u009b\u009d\u0001\u0000\u0000\u0000\u009c\u009a\u0001\u0000"+
		"\u0000\u0000\u009d\u009e\u0005\n\u0000\u0000\u009e\u009f\u0001\u0000\u0000"+
		"\u0000\u009f\u00a0\u0006\u0014\u0001\u0000\u00a0*\u0001\u0000\u0000\u0000"+
		"\u00a1\u00a3\u0007\u0005\u0000\u0000\u00a2\u00a1\u0001\u0000\u0000\u0000"+
		"\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000"+
		"\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000"+
		"\u00a6\u00a7\u0006\u0015\u0001\u0000\u00a7,\u0001\u0000\u0000\u0000\u00a8"+
		"\u00a9\t\u0000\u0000\u0000\u00a9.\u0001\u0000\u0000\u0000\t\u000024?E"+
		"Gx\u009a\u00a4\u0002\u0003\u0000\u0000\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}