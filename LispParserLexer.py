# Generated from LispParser.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,30,213,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,4,10,124,8,10,11,10,12,10,125,1,
        10,1,10,4,10,130,8,10,11,10,12,10,131,3,10,134,8,10,1,11,1,11,1,
        11,5,11,139,8,11,10,11,12,11,142,9,11,1,11,1,11,1,12,1,12,1,12,1,
        13,1,13,5,13,151,8,13,10,13,12,13,154,9,13,1,14,1,14,1,15,1,15,1,
        16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,
        21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,
        26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,5,28,197,8,
        28,10,28,12,28,200,9,28,1,28,1,28,1,29,4,29,205,8,29,11,29,12,29,
        206,1,29,1,29,1,30,1,30,1,30,0,0,31,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,0,27,13,29,14,31,15,33,16,35,17,
        37,18,39,19,41,20,43,21,45,22,47,23,49,24,51,25,53,26,55,27,57,28,
        59,29,61,30,1,0,7,1,0,48,57,2,0,34,34,92,92,7,0,34,34,39,39,92,92,
        98,98,110,110,114,114,116,116,3,0,65,90,95,95,97,122,6,0,42,42,45,
        45,48,57,65,90,95,95,97,122,1,0,10,10,3,0,9,10,13,13,32,32,219,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,
        0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,
        0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,
        0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,1,63,1,
        0,0,0,3,65,1,0,0,0,5,71,1,0,0,0,7,84,1,0,0,0,9,87,1,0,0,0,11,92,
        1,0,0,0,13,96,1,0,0,0,15,102,1,0,0,0,17,108,1,0,0,0,19,115,1,0,0,
        0,21,123,1,0,0,0,23,135,1,0,0,0,25,145,1,0,0,0,27,148,1,0,0,0,29,
        155,1,0,0,0,31,157,1,0,0,0,33,159,1,0,0,0,35,161,1,0,0,0,37,163,
        1,0,0,0,39,165,1,0,0,0,41,168,1,0,0,0,43,171,1,0,0,0,45,173,1,0,
        0,0,47,175,1,0,0,0,49,177,1,0,0,0,51,179,1,0,0,0,53,181,1,0,0,0,
        55,186,1,0,0,0,57,192,1,0,0,0,59,204,1,0,0,0,61,210,1,0,0,0,63,64,
        5,44,0,0,64,2,1,0,0,0,65,66,5,100,0,0,66,67,5,101,0,0,67,68,5,102,
        0,0,68,69,5,117,0,0,69,70,5,110,0,0,70,4,1,0,0,0,71,72,5,100,0,0,
        72,73,5,101,0,0,73,74,5,102,0,0,74,75,5,112,0,0,75,76,5,97,0,0,76,
        77,5,114,0,0,77,78,5,97,0,0,78,79,5,109,0,0,79,80,5,101,0,0,80,81,
        5,116,0,0,81,82,5,101,0,0,82,83,5,114,0,0,83,6,1,0,0,0,84,85,5,105,
        0,0,85,86,5,102,0,0,86,8,1,0,0,0,87,88,5,99,0,0,88,89,5,111,0,0,
        89,90,5,110,0,0,90,91,5,100,0,0,91,10,1,0,0,0,92,93,5,108,0,0,93,
        94,5,101,0,0,94,95,5,116,0,0,95,12,1,0,0,0,96,97,5,113,0,0,97,98,
        5,117,0,0,98,99,5,111,0,0,99,100,5,116,0,0,100,101,5,101,0,0,101,
        14,1,0,0,0,102,103,5,112,0,0,103,104,5,114,0,0,104,105,5,105,0,0,
        105,106,5,110,0,0,106,107,5,116,0,0,107,16,1,0,0,0,108,109,5,108,
        0,0,109,110,5,97,0,0,110,111,5,109,0,0,111,112,5,98,0,0,112,113,
        5,100,0,0,113,114,5,97,0,0,114,18,1,0,0,0,115,116,5,102,0,0,116,
        117,5,111,0,0,117,118,5,114,0,0,118,119,5,109,0,0,119,120,5,97,0,
        0,120,121,5,116,0,0,121,20,1,0,0,0,122,124,7,0,0,0,123,122,1,0,0,
        0,124,125,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,133,1,0,0,
        0,127,129,5,46,0,0,128,130,7,0,0,0,129,128,1,0,0,0,130,131,1,0,0,
        0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,127,1,0,0,
        0,133,134,1,0,0,0,134,22,1,0,0,0,135,140,5,34,0,0,136,139,3,25,12,
        0,137,139,8,1,0,0,138,136,1,0,0,0,138,137,1,0,0,0,139,142,1,0,0,
        0,140,138,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,140,1,0,0,
        0,143,144,5,34,0,0,144,24,1,0,0,0,145,146,5,92,0,0,146,147,7,2,0,
        0,147,26,1,0,0,0,148,152,7,3,0,0,149,151,7,4,0,0,150,149,1,0,0,0,
        151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,28,1,0,0,0,154,
        152,1,0,0,0,155,156,5,43,0,0,156,30,1,0,0,0,157,158,5,45,0,0,158,
        32,1,0,0,0,159,160,5,42,0,0,160,34,1,0,0,0,161,162,5,47,0,0,162,
        36,1,0,0,0,163,164,5,37,0,0,164,38,1,0,0,0,165,166,5,62,0,0,166,
        167,5,61,0,0,167,40,1,0,0,0,168,169,5,60,0,0,169,170,5,61,0,0,170,
        42,1,0,0,0,171,172,5,62,0,0,172,44,1,0,0,0,173,174,5,60,0,0,174,
        46,1,0,0,0,175,176,5,61,0,0,176,48,1,0,0,0,177,178,5,40,0,0,178,
        50,1,0,0,0,179,180,5,41,0,0,180,52,1,0,0,0,181,182,5,116,0,0,182,
        183,5,114,0,0,183,184,5,117,0,0,184,185,5,101,0,0,185,54,1,0,0,0,
        186,187,5,102,0,0,187,188,5,97,0,0,188,189,5,108,0,0,189,190,5,115,
        0,0,190,191,5,101,0,0,191,56,1,0,0,0,192,193,5,59,0,0,193,194,5,
        59,0,0,194,198,1,0,0,0,195,197,8,5,0,0,196,195,1,0,0,0,197,200,1,
        0,0,0,198,196,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,198,1,
        0,0,0,201,202,6,28,0,0,202,58,1,0,0,0,203,205,7,6,0,0,204,203,1,
        0,0,0,205,206,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,208,1,
        0,0,0,208,209,6,29,0,0,209,60,1,0,0,0,210,211,9,0,0,0,211,212,6,
        30,1,0,212,62,1,0,0,0,9,0,125,131,133,138,140,152,198,206,2,6,0,
        0,1,30,0
    ]

class LispParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    DEFUN = 2
    DEFparameter = 3
    IF = 4
    CONDITION = 5
    LET = 6
    QUOTE = 7
    PRINT = 8
    LAMBDA = 9
    FORMAT = 10
    NUMBER = 11
    STRING = 12
    IDENTIFIER = 13
    PLUS = 14
    MINUS = 15
    MULT = 16
    DIV = 17
    MOD = 18
    GREATER_EQUAL = 19
    LESS_EQUAL = 20
    GREATER = 21
    LESS = 22
    EQUAL = 23
    LPAREN = 24
    RPAREN = 25
    TRUE = 26
    FALSE = 27
    COMMENT = 28
    WS = 29
    ERROR = 30

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'defun'", "'defparameter'", "'if'", "'cond'", "'let'", 
            "'quote'", "'print'", "'lambda'", "'format'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'>='", "'<='", "'>'", "'<'", "'='", "'('", 
            "')'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "DEFUN", "DEFparameter", "IF", "CONDITION", "LET", "QUOTE", 
            "PRINT", "LAMBDA", "FORMAT", "NUMBER", "STRING", "IDENTIFIER", 
            "PLUS", "MINUS", "MULT", "DIV", "MOD", "GREATER_EQUAL", "LESS_EQUAL", 
            "GREATER", "LESS", "EQUAL", "LPAREN", "RPAREN", "TRUE", "FALSE", 
            "COMMENT", "WS", "ERROR" ]

    ruleNames = [ "T__0", "DEFUN", "DEFparameter", "IF", "CONDITION", "LET", 
                  "QUOTE", "PRINT", "LAMBDA", "FORMAT", "NUMBER", "STRING", 
                  "ESC_SEQ", "IDENTIFIER", "PLUS", "MINUS", "MULT", "DIV", 
                  "MOD", "GREATER_EQUAL", "LESS_EQUAL", "GREATER", "LESS", 
                  "EQUAL", "LPAREN", "RPAREN", "TRUE", "FALSE", "COMMENT", 
                  "WS", "ERROR" ]

    grammarFileName = "LispParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[30] = self.ERROR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             System.err.println("Invalid character: " + _input.getText(_start, _input.index())); 
     


