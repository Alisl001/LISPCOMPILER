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
		IDENTIFIER=1, NUMBER=2, PLUS=3, MINUS=4, MULT=5, DIV=6, MOD=7, LPAREN=8, 
		RPAREN=9, STRING=10, TRUE=11, FALSE=12, DEFUN=13, IF=14, COND=15, LET=16, 
		QUOTE=17, COMMENT=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"IDENTIFIER", "NUMBER", "PLUS", "MINUS", "MULT", "DIV", "MOD", "LPAREN", 
			"RPAREN", "STRING", "TRUE", "FALSE", "DEFUN", "IF", "COND", "LET", "QUOTE", 
			"COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", null, 
			"'true'", "'false'", "'defun'", "'if'", "'cond'", "'let'", "'quote'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IDENTIFIER", "NUMBER", "PLUS", "MINUS", "MULT", "DIV", "MOD", 
			"LPAREN", "RPAREN", "STRING", "TRUE", "FALSE", "DEFUN", "IF", "COND", 
			"LET", "QUOTE", "COMMENT", "WS"
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
		"\u0004\u0000\u0013\u0087\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0005\u0000*\b\u0000"+
		"\n\u0000\f\u0000-\t\u0000\u0001\u0001\u0004\u00010\b\u0001\u000b\u0001"+
		"\f\u00011\u0001\u0001\u0001\u0001\u0004\u00016\b\u0001\u000b\u0001\f\u0001"+
		"7\u0003\u0001:\b\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0005\tL\b\t"+
		"\n\t\f\tO\t\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0005\u0011"+
		"x\b\u0011\n\u0011\f\u0011{\t\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0004\u0012\u0082\b\u0012\u000b\u0012\f\u0012"+
		"\u0083\u0001\u0012\u0001\u0012\u0001y\u0000\u0013\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0012%\u0013\u0001\u0000\u0005\u0003\u0000AZ__az\u0005\u0000--09AZ_"+
		"_az\u0001\u000009\u0003\u0000\n\n\r\r\"\"\u0003\u0000\t\n\r\r  \u008d"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0001\'\u0001\u0000\u0000\u0000\u0003/\u0001\u0000\u0000\u0000"+
		"\u0005;\u0001\u0000\u0000\u0000\u0007=\u0001\u0000\u0000\u0000\t?\u0001"+
		"\u0000\u0000\u0000\u000bA\u0001\u0000\u0000\u0000\rC\u0001\u0000\u0000"+
		"\u0000\u000fE\u0001\u0000\u0000\u0000\u0011G\u0001\u0000\u0000\u0000\u0013"+
		"I\u0001\u0000\u0000\u0000\u0015R\u0001\u0000\u0000\u0000\u0017W\u0001"+
		"\u0000\u0000\u0000\u0019]\u0001\u0000\u0000\u0000\u001bc\u0001\u0000\u0000"+
		"\u0000\u001df\u0001\u0000\u0000\u0000\u001fk\u0001\u0000\u0000\u0000!"+
		"o\u0001\u0000\u0000\u0000#u\u0001\u0000\u0000\u0000%\u0081\u0001\u0000"+
		"\u0000\u0000\'+\u0007\u0000\u0000\u0000(*\u0007\u0001\u0000\u0000)(\u0001"+
		"\u0000\u0000\u0000*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000"+
		"+,\u0001\u0000\u0000\u0000,\u0002\u0001\u0000\u0000\u0000-+\u0001\u0000"+
		"\u0000\u0000.0\u0007\u0002\u0000\u0000/.\u0001\u0000\u0000\u000001\u0001"+
		"\u0000\u0000\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000\u0000"+
		"29\u0001\u0000\u0000\u000035\u0005.\u0000\u000046\u0007\u0002\u0000\u0000"+
		"54\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000075\u0001\u0000\u0000"+
		"\u000078\u0001\u0000\u0000\u00008:\u0001\u0000\u0000\u000093\u0001\u0000"+
		"\u0000\u00009:\u0001\u0000\u0000\u0000:\u0004\u0001\u0000\u0000\u0000"+
		";<\u0005+\u0000\u0000<\u0006\u0001\u0000\u0000\u0000=>\u0005-\u0000\u0000"+
		">\b\u0001\u0000\u0000\u0000?@\u0005*\u0000\u0000@\n\u0001\u0000\u0000"+
		"\u0000AB\u0005/\u0000\u0000B\f\u0001\u0000\u0000\u0000CD\u0005%\u0000"+
		"\u0000D\u000e\u0001\u0000\u0000\u0000EF\u0005(\u0000\u0000F\u0010\u0001"+
		"\u0000\u0000\u0000GH\u0005)\u0000\u0000H\u0012\u0001\u0000\u0000\u0000"+
		"IM\u0005\"\u0000\u0000JL\b\u0003\u0000\u0000KJ\u0001\u0000\u0000\u0000"+
		"LO\u0001\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000"+
		"\u0000NP\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PQ\u0005\"\u0000"+
		"\u0000Q\u0014\u0001\u0000\u0000\u0000RS\u0005t\u0000\u0000ST\u0005r\u0000"+
		"\u0000TU\u0005u\u0000\u0000UV\u0005e\u0000\u0000V\u0016\u0001\u0000\u0000"+
		"\u0000WX\u0005f\u0000\u0000XY\u0005a\u0000\u0000YZ\u0005l\u0000\u0000"+
		"Z[\u0005s\u0000\u0000[\\\u0005e\u0000\u0000\\\u0018\u0001\u0000\u0000"+
		"\u0000]^\u0005d\u0000\u0000^_\u0005e\u0000\u0000_`\u0005f\u0000\u0000"+
		"`a\u0005u\u0000\u0000ab\u0005n\u0000\u0000b\u001a\u0001\u0000\u0000\u0000"+
		"cd\u0005i\u0000\u0000de\u0005f\u0000\u0000e\u001c\u0001\u0000\u0000\u0000"+
		"fg\u0005c\u0000\u0000gh\u0005o\u0000\u0000hi\u0005n\u0000\u0000ij\u0005"+
		"d\u0000\u0000j\u001e\u0001\u0000\u0000\u0000kl\u0005l\u0000\u0000lm\u0005"+
		"e\u0000\u0000mn\u0005t\u0000\u0000n \u0001\u0000\u0000\u0000op\u0005q"+
		"\u0000\u0000pq\u0005u\u0000\u0000qr\u0005o\u0000\u0000rs\u0005t\u0000"+
		"\u0000st\u0005e\u0000\u0000t\"\u0001\u0000\u0000\u0000uy\u0005;\u0000"+
		"\u0000vx\t\u0000\u0000\u0000wv\u0001\u0000\u0000\u0000x{\u0001\u0000\u0000"+
		"\u0000yz\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000z|\u0001\u0000"+
		"\u0000\u0000{y\u0001\u0000\u0000\u0000|}\u0005\n\u0000\u0000}~\u0001\u0000"+
		"\u0000\u0000~\u007f\u0006\u0011\u0000\u0000\u007f$\u0001\u0000\u0000\u0000"+
		"\u0080\u0082\u0007\u0004\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000\u0000"+
		"\u0085\u0086\u0006\u0012\u0000\u0000\u0086&\u0001\u0000\u0000\u0000\b"+
		"\u0000+179My\u0083\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}