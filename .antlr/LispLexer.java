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
		FORMAT=10, IDENTIFIER=11, PLUS=12, MINUS=13, DIV=14, MOD=15, LPAREN=16, 
		RPAREN=17, TRUE=18, FALSE=19, COMMENT=20, WS=21, ERROR=22, MULT=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"STRING", "ESC_SEQ", "NUMBER", "DEFUN", "IF", "COND", "LET", "QUOTE", 
			"PRINT", "DEFPARAMETER", "FORMAT", "IDENTIFIER", "PLUS", "MINUS", "MULT", 
			"DIV", "MOD", "LPAREN", "RPAREN", "TRUE", "FALSE", "COMMENT", "WS", "ERROR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'defun'", "'if'", "'cond'", "'let'", "'quote'", "'print'", 
			"'defparameter'", "'format'", null, "'+'", "'-'", "'/'", "'%'", "'('", 
			"')'", "'true'", "'false'", null, null, null, "'*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "STRING", "NUMBER", "DEFUN", "IF", "COND", "LET", "QUOTE", "PRINT", 
			"DEFPARAMETER", "FORMAT", "IDENTIFIER", "PLUS", "MINUS", "DIV", "MOD", 
			"LPAREN", "RPAREN", "TRUE", "FALSE", "COMMENT", "WS", "ERROR", "MULT"
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
		"\u0004\u0000\u0017\u00b3\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u00005\b\u0000\n\u0000\f\u0000"+
		"8\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0004\u0002@\b\u0002\u000b\u0002\f\u0002A\u0001\u0002\u0001"+
		"\u0002\u0004\u0002F\b\u0002\u000b\u0002\f\u0002G\u0003\u0002J\b\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0005\u000b\u0080\b\u000b\n\u000b\f\u000b\u0083\t\u000b"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0005\u0015\u00a2\b\u0015\n"+
		"\u0015\f\u0015\u00a5\t\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0016\u0004\u0016\u00ac\b\u0016\u000b\u0016\f\u0016\u00ad"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u00a3\u0000\u0018"+
		"\u0001\u0001\u0003\u0000\u0005\u0002\u0007\u0003\t\u0004\u000b\u0005\r"+
		"\u0006\u000f\u0007\u0011\b\u0013\t\u0015\n\u0017\u000b\u0019\f\u001b\r"+
		"\u001d\u0017\u001f\u000e!\u000f#\u0010%\u0011\'\u0012)\u0013+\u0014-\u0015"+
		"/\u0016\u0001\u0000\u0006\u0002\u0000\"\"\\\\\u0007\u0000\"\"\'\'\\\\"+
		"bbnnrrtt\u0001\u000009\u0003\u0000AZ__az\u0006\u0000**--09AZ__az\u0003"+
		"\u0000\t\n\r\r  \u00b9\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000"+
		"\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001"+
		"\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000"+
		"\u0000\u00011\u0001\u0000\u0000\u0000\u0003;\u0001\u0000\u0000\u0000\u0005"+
		"?\u0001\u0000\u0000\u0000\u0007K\u0001\u0000\u0000\u0000\tQ\u0001\u0000"+
		"\u0000\u0000\u000bT\u0001\u0000\u0000\u0000\rY\u0001\u0000\u0000\u0000"+
		"\u000f]\u0001\u0000\u0000\u0000\u0011c\u0001\u0000\u0000\u0000\u0013i"+
		"\u0001\u0000\u0000\u0000\u0015v\u0001\u0000\u0000\u0000\u0017}\u0001\u0000"+
		"\u0000\u0000\u0019\u0084\u0001\u0000\u0000\u0000\u001b\u0086\u0001\u0000"+
		"\u0000\u0000\u001d\u0088\u0001\u0000\u0000\u0000\u001f\u008c\u0001\u0000"+
		"\u0000\u0000!\u008e\u0001\u0000\u0000\u0000#\u0090\u0001\u0000\u0000\u0000"+
		"%\u0092\u0001\u0000\u0000\u0000\'\u0094\u0001\u0000\u0000\u0000)\u0099"+
		"\u0001\u0000\u0000\u0000+\u009f\u0001\u0000\u0000\u0000-\u00ab\u0001\u0000"+
		"\u0000\u0000/\u00b1\u0001\u0000\u0000\u000016\u0005\"\u0000\u000025\u0003"+
		"\u0003\u0001\u000035\b\u0000\u0000\u000042\u0001\u0000\u0000\u000043\u0001"+
		"\u0000\u0000\u000058\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u0000"+
		"67\u0001\u0000\u0000\u000079\u0001\u0000\u0000\u000086\u0001\u0000\u0000"+
		"\u00009:\u0005\"\u0000\u0000:\u0002\u0001\u0000\u0000\u0000;<\u0005\\"+
		"\u0000\u0000<=\u0007\u0001\u0000\u0000=\u0004\u0001\u0000\u0000\u0000"+
		">@\u0007\u0002\u0000\u0000?>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000"+
		"\u0000A?\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000BI\u0001\u0000"+
		"\u0000\u0000CE\u0005.\u0000\u0000DF\u0007\u0002\u0000\u0000ED\u0001\u0000"+
		"\u0000\u0000FG\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000GH\u0001"+
		"\u0000\u0000\u0000HJ\u0001\u0000\u0000\u0000IC\u0001\u0000\u0000\u0000"+
		"IJ\u0001\u0000\u0000\u0000J\u0006\u0001\u0000\u0000\u0000KL\u0005d\u0000"+
		"\u0000LM\u0005e\u0000\u0000MN\u0005f\u0000\u0000NO\u0005u\u0000\u0000"+
		"OP\u0005n\u0000\u0000P\b\u0001\u0000\u0000\u0000QR\u0005i\u0000\u0000"+
		"RS\u0005f\u0000\u0000S\n\u0001\u0000\u0000\u0000TU\u0005c\u0000\u0000"+
		"UV\u0005o\u0000\u0000VW\u0005n\u0000\u0000WX\u0005d\u0000\u0000X\f\u0001"+
		"\u0000\u0000\u0000YZ\u0005l\u0000\u0000Z[\u0005e\u0000\u0000[\\\u0005"+
		"t\u0000\u0000\\\u000e\u0001\u0000\u0000\u0000]^\u0005q\u0000\u0000^_\u0005"+
		"u\u0000\u0000_`\u0005o\u0000\u0000`a\u0005t\u0000\u0000ab\u0005e\u0000"+
		"\u0000b\u0010\u0001\u0000\u0000\u0000cd\u0005p\u0000\u0000de\u0005r\u0000"+
		"\u0000ef\u0005i\u0000\u0000fg\u0005n\u0000\u0000gh\u0005t\u0000\u0000"+
		"h\u0012\u0001\u0000\u0000\u0000ij\u0005d\u0000\u0000jk\u0005e\u0000\u0000"+
		"kl\u0005f\u0000\u0000lm\u0005p\u0000\u0000mn\u0005a\u0000\u0000no\u0005"+
		"r\u0000\u0000op\u0005a\u0000\u0000pq\u0005m\u0000\u0000qr\u0005e\u0000"+
		"\u0000rs\u0005t\u0000\u0000st\u0005e\u0000\u0000tu\u0005r\u0000\u0000"+
		"u\u0014\u0001\u0000\u0000\u0000vw\u0005f\u0000\u0000wx\u0005o\u0000\u0000"+
		"xy\u0005r\u0000\u0000yz\u0005m\u0000\u0000z{\u0005a\u0000\u0000{|\u0005"+
		"t\u0000\u0000|\u0016\u0001\u0000\u0000\u0000}\u0081\u0007\u0003\u0000"+
		"\u0000~\u0080\u0007\u0004\u0000\u0000\u007f~\u0001\u0000\u0000\u0000\u0080"+
		"\u0083\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081"+
		"\u0082\u0001\u0000\u0000\u0000\u0082\u0018\u0001\u0000\u0000\u0000\u0083"+
		"\u0081\u0001\u0000\u0000\u0000\u0084\u0085\u0005+\u0000\u0000\u0085\u001a"+
		"\u0001\u0000\u0000\u0000\u0086\u0087\u0005-\u0000\u0000\u0087\u001c\u0001"+
		"\u0000\u0000\u0000\u0088\u0089\u0005*\u0000\u0000\u0089\u008a\u0001\u0000"+
		"\u0000\u0000\u008a\u008b\u0006\u000e\u0000\u0000\u008b\u001e\u0001\u0000"+
		"\u0000\u0000\u008c\u008d\u0005/\u0000\u0000\u008d \u0001\u0000\u0000\u0000"+
		"\u008e\u008f\u0005%\u0000\u0000\u008f\"\u0001\u0000\u0000\u0000\u0090"+
		"\u0091\u0005(\u0000\u0000\u0091$\u0001\u0000\u0000\u0000\u0092\u0093\u0005"+
		")\u0000\u0000\u0093&\u0001\u0000\u0000\u0000\u0094\u0095\u0005t\u0000"+
		"\u0000\u0095\u0096\u0005r\u0000\u0000\u0096\u0097\u0005u\u0000\u0000\u0097"+
		"\u0098\u0005e\u0000\u0000\u0098(\u0001\u0000\u0000\u0000\u0099\u009a\u0005"+
		"f\u0000\u0000\u009a\u009b\u0005a\u0000\u0000\u009b\u009c\u0005l\u0000"+
		"\u0000\u009c\u009d\u0005s\u0000\u0000\u009d\u009e\u0005e\u0000\u0000\u009e"+
		"*\u0001\u0000\u0000\u0000\u009f\u00a3\u0005;\u0000\u0000\u00a0\u00a2\t"+
		"\u0000\u0000\u0000\u00a1\u00a0\u0001\u0000\u0000\u0000\u00a2\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a3\u00a1\u0001"+
		"\u0000\u0000\u0000\u00a4\u00a6\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001"+
		"\u0000\u0000\u0000\u00a6\u00a7\u0005\n\u0000\u0000\u00a7\u00a8\u0001\u0000"+
		"\u0000\u0000\u00a8\u00a9\u0006\u0015\u0001\u0000\u00a9,\u0001\u0000\u0000"+
		"\u0000\u00aa\u00ac\u0007\u0005\u0000\u0000\u00ab\u00aa\u0001\u0000\u0000"+
		"\u0000\u00ac\u00ad\u0001\u0000\u0000\u0000\u00ad\u00ab\u0001\u0000\u0000"+
		"\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae\u00af\u0001\u0000\u0000"+
		"\u0000\u00af\u00b0\u0006\u0016\u0001\u0000\u00b0.\u0001\u0000\u0000\u0000"+
		"\u00b1\u00b2\t\u0000\u0000\u0000\u00b20\u0001\u0000\u0000\u0000\t\u0000"+
		"46AGI\u0081\u00a3\u00ad\u0002\u0003\u0000\u0000\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}