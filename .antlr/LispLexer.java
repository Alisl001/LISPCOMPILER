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
		NUMBER=1, DEFUN=2, IF=3, COND=4, LET=5, QUOTE=6, PRINT=7, IDENTIFIER=8, 
		PLUS=9, MINUS=10, MULT=11, DIV=12, MOD=13, LPAREN=14, RPAREN=15, STRING=16, 
		TRUE=17, FALSE=18, COMMENT=19, WS=20, ERROR=21;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMBER", "DEFUN", "IF", "COND", "LET", "QUOTE", "PRINT", "IDENTIFIER", 
			"PLUS", "MINUS", "MULT", "DIV", "MOD", "LPAREN", "RPAREN", "STRING", 
			"ESC_SEQ", "TRUE", "FALSE", "COMMENT", "WS", "ERROR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'defun'", "'if'", "'cond'", "'let'", "'quote'", "'print'", 
			null, "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", null, "'true'", 
			"'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUMBER", "DEFUN", "IF", "COND", "LET", "QUOTE", "PRINT", "IDENTIFIER", 
			"PLUS", "MINUS", "MULT", "DIV", "MOD", "LPAREN", "RPAREN", "STRING", 
			"TRUE", "FALSE", "COMMENT", "WS", "ERROR"
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
		"\u0004\u0000\u0015\u0097\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0004\u0000/\b\u0000\u000b\u0000"+
		"\f\u00000\u0001\u0000\u0001\u0000\u0004\u00005\b\u0000\u000b\u0000\f\u0000"+
		"6\u0003\u00009\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0005\u0007[\b\u0007"+
		"\n\u0007\f\u0007^\t\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000fq\b\u000f"+
		"\n\u000f\f\u000ft\t\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0005\u0013\u0088\b\u0013\n\u0013\f\u0013\u008b"+
		"\t\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0004\u0014\u0090\b\u0014"+
		"\u000b\u0014\f\u0014\u0091\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015"+
		"\u0001\u0089\u0000\u0016\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0000#\u0011%\u0012\'"+
		"\u0013)\u0014+\u0015\u0001\u0000\u0006\u0001\u000009\u0003\u0000AZ__a"+
		"z\u0005\u0000--09AZ__az\u0004\u0000\n\n\r\r\"\"\\\\\u0007\u0000\"\"\'"+
		"\'\\\\bbnnrrtt\u0003\u0000\t\n\r\r  \u009d\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000"+
		"\u001f\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001"+
		"\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000"+
		"\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0001.\u0001\u0000\u0000\u0000"+
		"\u0003:\u0001\u0000\u0000\u0000\u0005@\u0001\u0000\u0000\u0000\u0007C"+
		"\u0001\u0000\u0000\u0000\tH\u0001\u0000\u0000\u0000\u000bL\u0001\u0000"+
		"\u0000\u0000\rR\u0001\u0000\u0000\u0000\u000fX\u0001\u0000\u0000\u0000"+
		"\u0011_\u0001\u0000\u0000\u0000\u0013a\u0001\u0000\u0000\u0000\u0015c"+
		"\u0001\u0000\u0000\u0000\u0017e\u0001\u0000\u0000\u0000\u0019g\u0001\u0000"+
		"\u0000\u0000\u001bi\u0001\u0000\u0000\u0000\u001dk\u0001\u0000\u0000\u0000"+
		"\u001fm\u0001\u0000\u0000\u0000!w\u0001\u0000\u0000\u0000#z\u0001\u0000"+
		"\u0000\u0000%\u007f\u0001\u0000\u0000\u0000\'\u0085\u0001\u0000\u0000"+
		"\u0000)\u008f\u0001\u0000\u0000\u0000+\u0095\u0001\u0000\u0000\u0000-"+
		"/\u0007\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000"+
		"\u00000.\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u000018\u0001\u0000"+
		"\u0000\u000024\u0005.\u0000\u000035\u0007\u0000\u0000\u000043\u0001\u0000"+
		"\u0000\u000056\u0001\u0000\u0000\u000064\u0001\u0000\u0000\u000067\u0001"+
		"\u0000\u0000\u000079\u0001\u0000\u0000\u000082\u0001\u0000\u0000\u0000"+
		"89\u0001\u0000\u0000\u00009\u0002\u0001\u0000\u0000\u0000:;\u0005d\u0000"+
		"\u0000;<\u0005e\u0000\u0000<=\u0005f\u0000\u0000=>\u0005u\u0000\u0000"+
		">?\u0005n\u0000\u0000?\u0004\u0001\u0000\u0000\u0000@A\u0005i\u0000\u0000"+
		"AB\u0005f\u0000\u0000B\u0006\u0001\u0000\u0000\u0000CD\u0005c\u0000\u0000"+
		"DE\u0005o\u0000\u0000EF\u0005n\u0000\u0000FG\u0005d\u0000\u0000G\b\u0001"+
		"\u0000\u0000\u0000HI\u0005l\u0000\u0000IJ\u0005e\u0000\u0000JK\u0005t"+
		"\u0000\u0000K\n\u0001\u0000\u0000\u0000LM\u0005q\u0000\u0000MN\u0005u"+
		"\u0000\u0000NO\u0005o\u0000\u0000OP\u0005t\u0000\u0000PQ\u0005e\u0000"+
		"\u0000Q\f\u0001\u0000\u0000\u0000RS\u0005p\u0000\u0000ST\u0005r\u0000"+
		"\u0000TU\u0005i\u0000\u0000UV\u0005n\u0000\u0000VW\u0005t\u0000\u0000"+
		"W\u000e\u0001\u0000\u0000\u0000X\\\u0007\u0001\u0000\u0000Y[\u0007\u0002"+
		"\u0000\u0000ZY\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000\u0000\\Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\u0010\u0001\u0000\u0000"+
		"\u0000^\\\u0001\u0000\u0000\u0000_`\u0005+\u0000\u0000`\u0012\u0001\u0000"+
		"\u0000\u0000ab\u0005-\u0000\u0000b\u0014\u0001\u0000\u0000\u0000cd\u0005"+
		"*\u0000\u0000d\u0016\u0001\u0000\u0000\u0000ef\u0005/\u0000\u0000f\u0018"+
		"\u0001\u0000\u0000\u0000gh\u0005%\u0000\u0000h\u001a\u0001\u0000\u0000"+
		"\u0000ij\u0005(\u0000\u0000j\u001c\u0001\u0000\u0000\u0000kl\u0005)\u0000"+
		"\u0000l\u001e\u0001\u0000\u0000\u0000mr\u0005\"\u0000\u0000nq\u0003!\u0010"+
		"\u0000oq\b\u0003\u0000\u0000pn\u0001\u0000\u0000\u0000po\u0001\u0000\u0000"+
		"\u0000qt\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000rs\u0001\u0000"+
		"\u0000\u0000su\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000uv\u0005"+
		"\"\u0000\u0000v \u0001\u0000\u0000\u0000wx\u0005\\\u0000\u0000xy\u0007"+
		"\u0004\u0000\u0000y\"\u0001\u0000\u0000\u0000z{\u0005t\u0000\u0000{|\u0005"+
		"r\u0000\u0000|}\u0005u\u0000\u0000}~\u0005e\u0000\u0000~$\u0001\u0000"+
		"\u0000\u0000\u007f\u0080\u0005f\u0000\u0000\u0080\u0081\u0005a\u0000\u0000"+
		"\u0081\u0082\u0005l\u0000\u0000\u0082\u0083\u0005s\u0000\u0000\u0083\u0084"+
		"\u0005e\u0000\u0000\u0084&\u0001\u0000\u0000\u0000\u0085\u0089\u0005;"+
		"\u0000\u0000\u0086\u0088\t\u0000\u0000\u0000\u0087\u0086\u0001\u0000\u0000"+
		"\u0000\u0088\u008b\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000\u0000"+
		"\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a\u008c\u0001\u0000\u0000"+
		"\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008c\u008d\u0005\n\u0000\u0000"+
		"\u008d(\u0001\u0000\u0000\u0000\u008e\u0090\u0007\u0005\u0000\u0000\u008f"+
		"\u008e\u0001\u0000\u0000\u0000\u0090\u0091\u0001\u0000\u0000\u0000\u0091"+
		"\u008f\u0001\u0000\u0000\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092"+
		"\u0093\u0001\u0000\u0000\u0000\u0093\u0094\u0006\u0014\u0000\u0000\u0094"+
		"*\u0001\u0000\u0000\u0000\u0095\u0096\t\u0000\u0000\u0000\u0096,\u0001"+
		"\u0000\u0000\u0000\t\u0000068\\pr\u0089\u0091\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}