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
		TRUE=17, FALSE=18, COMMENT=19, WS=20;
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
			"TRUE", "FALSE", "COMMENT", "WS"
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
			"TRUE", "FALSE", "COMMENT", "WS"
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
		"\u0004\u0000\u0014\u008d\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0004\u0000"+
		"+\b\u0000\u000b\u0000\f\u0000,\u0001\u0000\u0001\u0000\u0004\u00001\b"+
		"\u0000\u000b\u0000\f\u00002\u0003\u00005\b\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0005\u0007W\b\u0007\n\u0007\f\u0007Z\t\u0007\u0001\b\u0001\b\u0001\t"+
		"\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0005\u000f"+
		"l\b\u000f\n\u000f\f\u000fo\t\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0005\u0012\u0080\b\u0012\n\u0012\f\u0012\u0083\t\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0004\u0013\u0088\b\u0013\u000b\u0013\f\u0013\u0089"+
		"\u0001\u0013\u0001\u0013\u0001\u0081\u0000\u0014\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\'\u0014\u0001\u0000\u0005\u0001\u000009\u0003\u0000AZ_"+
		"_az\u0005\u0000--09AZ__az\u0003\u0000\n\n\r\r\"\"\u0003\u0000\t\n\r\r"+
		"  \u0093\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000"+
		"!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001"+
		"\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0001*\u0001\u0000"+
		"\u0000\u0000\u00036\u0001\u0000\u0000\u0000\u0005<\u0001\u0000\u0000\u0000"+
		"\u0007?\u0001\u0000\u0000\u0000\tD\u0001\u0000\u0000\u0000\u000bH\u0001"+
		"\u0000\u0000\u0000\rN\u0001\u0000\u0000\u0000\u000fT\u0001\u0000\u0000"+
		"\u0000\u0011[\u0001\u0000\u0000\u0000\u0013]\u0001\u0000\u0000\u0000\u0015"+
		"_\u0001\u0000\u0000\u0000\u0017a\u0001\u0000\u0000\u0000\u0019c\u0001"+
		"\u0000\u0000\u0000\u001be\u0001\u0000\u0000\u0000\u001dg\u0001\u0000\u0000"+
		"\u0000\u001fi\u0001\u0000\u0000\u0000!r\u0001\u0000\u0000\u0000#w\u0001"+
		"\u0000\u0000\u0000%}\u0001\u0000\u0000\u0000\'\u0087\u0001\u0000\u0000"+
		"\u0000)+\u0007\u0000\u0000\u0000*)\u0001\u0000\u0000\u0000+,\u0001\u0000"+
		"\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000\u0000-4\u0001"+
		"\u0000\u0000\u0000.0\u0005.\u0000\u0000/1\u0007\u0000\u0000\u00000/\u0001"+
		"\u0000\u0000\u000012\u0001\u0000\u0000\u000020\u0001\u0000\u0000\u0000"+
		"23\u0001\u0000\u0000\u000035\u0001\u0000\u0000\u00004.\u0001\u0000\u0000"+
		"\u000045\u0001\u0000\u0000\u00005\u0002\u0001\u0000\u0000\u000067\u0005"+
		"d\u0000\u000078\u0005e\u0000\u000089\u0005f\u0000\u00009:\u0005u\u0000"+
		"\u0000:;\u0005n\u0000\u0000;\u0004\u0001\u0000\u0000\u0000<=\u0005i\u0000"+
		"\u0000=>\u0005f\u0000\u0000>\u0006\u0001\u0000\u0000\u0000?@\u0005c\u0000"+
		"\u0000@A\u0005o\u0000\u0000AB\u0005n\u0000\u0000BC\u0005d\u0000\u0000"+
		"C\b\u0001\u0000\u0000\u0000DE\u0005l\u0000\u0000EF\u0005e\u0000\u0000"+
		"FG\u0005t\u0000\u0000G\n\u0001\u0000\u0000\u0000HI\u0005q\u0000\u0000"+
		"IJ\u0005u\u0000\u0000JK\u0005o\u0000\u0000KL\u0005t\u0000\u0000LM\u0005"+
		"e\u0000\u0000M\f\u0001\u0000\u0000\u0000NO\u0005p\u0000\u0000OP\u0005"+
		"r\u0000\u0000PQ\u0005i\u0000\u0000QR\u0005n\u0000\u0000RS\u0005t\u0000"+
		"\u0000S\u000e\u0001\u0000\u0000\u0000TX\u0007\u0001\u0000\u0000UW\u0007"+
		"\u0002\u0000\u0000VU\u0001\u0000\u0000\u0000WZ\u0001\u0000\u0000\u0000"+
		"XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Y\u0010\u0001\u0000"+
		"\u0000\u0000ZX\u0001\u0000\u0000\u0000[\\\u0005+\u0000\u0000\\\u0012\u0001"+
		"\u0000\u0000\u0000]^\u0005-\u0000\u0000^\u0014\u0001\u0000\u0000\u0000"+
		"_`\u0005*\u0000\u0000`\u0016\u0001\u0000\u0000\u0000ab\u0005/\u0000\u0000"+
		"b\u0018\u0001\u0000\u0000\u0000cd\u0005%\u0000\u0000d\u001a\u0001\u0000"+
		"\u0000\u0000ef\u0005(\u0000\u0000f\u001c\u0001\u0000\u0000\u0000gh\u0005"+
		")\u0000\u0000h\u001e\u0001\u0000\u0000\u0000im\u0005\"\u0000\u0000jl\b"+
		"\u0003\u0000\u0000kj\u0001\u0000\u0000\u0000lo\u0001\u0000\u0000\u0000"+
		"mk\u0001\u0000\u0000\u0000mn\u0001\u0000\u0000\u0000np\u0001\u0000\u0000"+
		"\u0000om\u0001\u0000\u0000\u0000pq\u0005\"\u0000\u0000q \u0001\u0000\u0000"+
		"\u0000rs\u0005t\u0000\u0000st\u0005r\u0000\u0000tu\u0005u\u0000\u0000"+
		"uv\u0005e\u0000\u0000v\"\u0001\u0000\u0000\u0000wx\u0005f\u0000\u0000"+
		"xy\u0005a\u0000\u0000yz\u0005l\u0000\u0000z{\u0005s\u0000\u0000{|\u0005"+
		"e\u0000\u0000|$\u0001\u0000\u0000\u0000}\u0081\u0005;\u0000\u0000~\u0080"+
		"\t\u0000\u0000\u0000\u007f~\u0001\u0000\u0000\u0000\u0080\u0083\u0001"+
		"\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000\u0081\u007f\u0001"+
		"\u0000\u0000\u0000\u0082\u0084\u0001\u0000\u0000\u0000\u0083\u0081\u0001"+
		"\u0000\u0000\u0000\u0084\u0085\u0005\n\u0000\u0000\u0085&\u0001\u0000"+
		"\u0000\u0000\u0086\u0088\u0007\u0004\u0000\u0000\u0087\u0086\u0001\u0000"+
		"\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000"+
		"\u0000\u0000\u0089\u008a\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000"+
		"\u0000\u0000\u008b\u008c\u0006\u0013\u0000\u0000\u008c(\u0001\u0000\u0000"+
		"\u0000\b\u0000,24Xm\u0081\u0089\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}