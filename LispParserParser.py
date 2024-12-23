# Generated from LispParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,55,8,1,1,
        2,1,2,1,3,1,3,1,3,3,3,62,8,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,70,8,3,
        1,4,1,4,1,4,5,4,75,8,4,10,4,12,4,78,9,4,1,5,1,5,1,5,5,5,83,8,5,10,
        5,12,5,86,9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,
        8,100,8,8,10,8,12,8,103,9,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,
        10,113,8,10,10,10,12,10,116,9,10,1,10,1,10,1,10,1,11,1,11,1,11,1,
        12,1,12,1,12,3,12,127,8,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,3,15,146,8,15,1,
        15,3,15,149,8,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,0,4,2,0,11,13,26,27,1,0,16,17,1,0,14,15,1,0,19,23,155,0,35,
        1,0,0,0,2,54,1,0,0,0,4,56,1,0,0,0,6,69,1,0,0,0,8,71,1,0,0,0,10,79,
        1,0,0,0,12,87,1,0,0,0,14,91,1,0,0,0,16,96,1,0,0,0,18,104,1,0,0,0,
        20,109,1,0,0,0,22,120,1,0,0,0,24,123,1,0,0,0,26,131,1,0,0,0,28,136,
        1,0,0,0,30,145,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,
        35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,
        0,0,1,39,1,1,0,0,0,40,55,3,6,3,0,41,55,3,12,6,0,42,55,3,14,7,0,43,
        55,3,18,9,0,44,55,3,20,10,0,45,55,3,22,11,0,46,55,3,24,12,0,47,55,
        3,26,13,0,48,55,3,4,2,0,49,55,3,28,14,0,50,51,5,24,0,0,51,52,3,2,
        1,0,52,53,5,25,0,0,53,55,1,0,0,0,54,40,1,0,0,0,54,41,1,0,0,0,54,
        42,1,0,0,0,54,43,1,0,0,0,54,44,1,0,0,0,54,45,1,0,0,0,54,46,1,0,0,
        0,54,47,1,0,0,0,54,48,1,0,0,0,54,49,1,0,0,0,54,50,1,0,0,0,55,3,1,
        0,0,0,56,57,7,0,0,0,57,5,1,0,0,0,58,59,5,13,0,0,59,61,5,24,0,0,60,
        62,3,10,5,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,70,5,25,
        0,0,64,65,5,10,0,0,65,66,5,24,0,0,66,67,3,8,4,0,67,68,5,25,0,0,68,
        70,1,0,0,0,69,58,1,0,0,0,69,64,1,0,0,0,70,7,1,0,0,0,71,76,3,2,1,
        0,72,73,5,1,0,0,73,75,3,2,1,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,
        1,0,0,0,76,77,1,0,0,0,77,9,1,0,0,0,78,76,1,0,0,0,79,84,3,2,1,0,80,
        81,5,1,0,0,81,83,3,2,1,0,82,80,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,
        0,84,85,1,0,0,0,85,11,1,0,0,0,86,84,1,0,0,0,87,88,5,3,0,0,88,89,
        5,13,0,0,89,90,3,2,1,0,90,13,1,0,0,0,91,92,5,2,0,0,92,93,5,13,0,
        0,93,94,3,16,8,0,94,95,3,2,1,0,95,15,1,0,0,0,96,101,5,13,0,0,97,
        98,5,1,0,0,98,100,5,13,0,0,99,97,1,0,0,0,100,103,1,0,0,0,101,99,
        1,0,0,0,101,102,1,0,0,0,102,17,1,0,0,0,103,101,1,0,0,0,104,105,5,
        4,0,0,105,106,3,2,1,0,106,107,3,2,1,0,107,108,3,2,1,0,108,19,1,0,
        0,0,109,110,5,6,0,0,110,114,5,24,0,0,111,113,3,12,6,0,112,111,1,
        0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,1,
        0,0,0,116,114,1,0,0,0,117,118,5,25,0,0,118,119,3,2,1,0,119,21,1,
        0,0,0,120,121,5,7,0,0,121,122,3,2,1,0,122,23,1,0,0,0,123,124,5,9,
        0,0,124,126,5,24,0,0,125,127,3,16,8,0,126,125,1,0,0,0,126,127,1,
        0,0,0,127,128,1,0,0,0,128,129,5,25,0,0,129,130,3,2,1,0,130,25,1,
        0,0,0,131,132,5,8,0,0,132,133,5,24,0,0,133,134,3,2,1,0,134,135,5,
        25,0,0,135,27,1,0,0,0,136,137,3,4,2,0,137,138,3,30,15,0,138,29,1,
        0,0,0,139,140,7,1,0,0,140,146,3,4,2,0,141,142,7,2,0,0,142,146,3,
        4,2,0,143,144,7,3,0,0,144,146,3,4,2,0,145,139,1,0,0,0,145,141,1,
        0,0,0,145,143,1,0,0,0,146,148,1,0,0,0,147,149,3,30,15,0,148,147,
        1,0,0,0,148,149,1,0,0,0,149,31,1,0,0,0,11,35,54,61,69,76,84,101,
        114,126,145,148
    ]

class LispParserParser ( Parser ):

    grammarFileName = "LispParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'defun'", "'defparameter'", "'if'", 
                     "'cond'", "'let'", "'quote'", "'print'", "'lambda'", 
                     "'format'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'>='", "'<='", 
                     "'>'", "'<'", "'='", "'('", "')'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "DEFUN", "DEFparameter", 
                      "IF", "CONDITION", "LET", "QUOTE", "PRINT", "LAMBDA", 
                      "FORMAT", "NUMBER", "STRING", "IDENTIFIER", "PLUS", 
                      "MINUS", "MULT", "DIV", "MOD", "GREATER_EQUAL", "LESS_EQUAL", 
                      "GREATER", "LESS", "EQUAL", "LPAREN", "RPAREN", "TRUE", 
                      "FALSE", "COMMENT", "WS", "ERROR" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_atom = 2
    RULE_functionCall = 3
    RULE_formatArguments = 4
    RULE_argumentList = 5
    RULE_variableDefinition = 6
    RULE_functionDefinition = 7
    RULE_parameterList = 8
    RULE_conditional = 9
    RULE_letExpression = 10
    RULE_quoteExpression = 11
    RULE_lambdaExpression = 12
    RULE_printExpression = 13
    RULE_binaryExpression = 14
    RULE_binaryTail = 15

    ruleNames =  [ "program", "expression", "atom", "functionCall", "formatArguments", 
                   "argumentList", "variableDefinition", "functionDefinition", 
                   "parameterList", "conditional", "letExpression", "quoteExpression", 
                   "lambdaExpression", "printExpression", "binaryExpression", 
                   "binaryTail" ]

    EOF = Token.EOF
    T__0=1
    DEFUN=2
    DEFparameter=3
    IF=4
    CONDITION=5
    LET=6
    QUOTE=7
    PRINT=8
    LAMBDA=9
    FORMAT=10
    NUMBER=11
    STRING=12
    IDENTIFIER=13
    PLUS=14
    MINUS=15
    MULT=16
    DIV=17
    MOD=18
    GREATER_EQUAL=19
    LESS_EQUAL=20
    GREATER=21
    LESS=22
    EQUAL=23
    LPAREN=24
    RPAREN=25
    TRUE=26
    FALSE=27
    COMMENT=28
    WS=29
    ERROR=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LispParserParser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = LispParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 218120156) != 0):
                self.state = 32
                self.expression()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(LispParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(LispParserParser.FunctionCallContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(LispParserParser.VariableDefinitionContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(LispParserParser.FunctionDefinitionContext,0)


        def conditional(self):
            return self.getTypedRuleContext(LispParserParser.ConditionalContext,0)


        def letExpression(self):
            return self.getTypedRuleContext(LispParserParser.LetExpressionContext,0)


        def quoteExpression(self):
            return self.getTypedRuleContext(LispParserParser.QuoteExpressionContext,0)


        def lambdaExpression(self):
            return self.getTypedRuleContext(LispParserParser.LambdaExpressionContext,0)


        def printExpression(self):
            return self.getTypedRuleContext(LispParserParser.PrintExpressionContext,0)


        def atom(self):
            return self.getTypedRuleContext(LispParserParser.AtomContext,0)


        def binaryExpression(self):
            return self.getTypedRuleContext(LispParserParser.BinaryExpressionContext,0)


        def LPAREN(self):
            return self.getToken(LispParserParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParserParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LispParserParser.RPAREN, 0)

        def getRuleIndex(self):
            return LispParserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LispParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.functionCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.variableDefinition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.conditional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.letExpression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.quoteExpression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.lambdaExpression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 47
                self.printExpression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 48
                self.atom()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 49
                self.binaryExpression()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 50
                self.match(LispParserParser.LPAREN)
                self.state = 51
                self.expression()
                self.state = 52
                self.match(LispParserParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LispParserParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(LispParserParser.STRING, 0)

        def TRUE(self):
            return self.getToken(LispParserParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LispParserParser.FALSE, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParserParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LispParserParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = LispParserParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 201340928) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LispParserParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(LispParserParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LispParserParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(LispParserParser.ArgumentListContext,0)


        def FORMAT(self):
            return self.getToken(LispParserParser.FORMAT, 0)

        def formatArguments(self):
            return self.getTypedRuleContext(LispParserParser.FormatArgumentsContext,0)


        def getRuleIndex(self):
            return LispParserParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = LispParserParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(LispParserParser.IDENTIFIER)
                self.state = 59
                self.match(LispParserParser.LPAREN)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 218120156) != 0):
                    self.state = 60
                    self.argumentList()


                self.state = 63
                self.match(LispParserParser.RPAREN)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(LispParserParser.FORMAT)
                self.state = 65
                self.match(LispParserParser.LPAREN)
                self.state = 66
                self.formatArguments()
                self.state = 67
                self.match(LispParserParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParserParser.RULE_formatArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatArguments" ):
                listener.enterFormatArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatArguments" ):
                listener.exitFormatArguments(self)




    def formatArguments(self):

        localctx = LispParserParser.FormatArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formatArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.expression()
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 72
                self.match(LispParserParser.T__0)
                self.state = 73
                self.expression()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParserParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = LispParserParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.expression()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 80
                self.match(LispParserParser.T__0)
                self.state = 81
                self.expression()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFparameter(self):
            return self.getToken(LispParserParser.DEFparameter, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParserParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LispParserParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)




    def variableDefinition(self):

        localctx = LispParserParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(LispParserParser.DEFparameter)
            self.state = 88
            self.match(LispParserParser.IDENTIFIER)
            self.state = 89
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFUN(self):
            return self.getToken(LispParserParser.DEFUN, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParserParser.IDENTIFIER, 0)

        def parameterList(self):
            return self.getTypedRuleContext(LispParserParser.ParameterListContext,0)


        def expression(self):
            return self.getTypedRuleContext(LispParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LispParserParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = LispParserParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(LispParserParser.DEFUN)
            self.state = 92
            self.match(LispParserParser.IDENTIFIER)
            self.state = 93
            self.parameterList()
            self.state = 94
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LispParserParser.IDENTIFIER)
            else:
                return self.getToken(LispParserParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LispParserParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = LispParserParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(LispParserParser.IDENTIFIER)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 97
                self.match(LispParserParser.T__0)
                self.state = 98
                self.match(LispParserParser.IDENTIFIER)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LispParserParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParserParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = LispParserParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(LispParserParser.IF)
            self.state = 105
            self.expression()
            self.state = 106
            self.expression()
            self.state = 107
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(LispParserParser.LET, 0)

        def LPAREN(self):
            return self.getToken(LispParserParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LispParserParser.RPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParserParser.ExpressionContext,0)


        def variableDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParserParser.VariableDefinitionContext)
            else:
                return self.getTypedRuleContext(LispParserParser.VariableDefinitionContext,i)


        def getRuleIndex(self):
            return LispParserParser.RULE_letExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetExpression" ):
                listener.enterLetExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetExpression" ):
                listener.exitLetExpression(self)




    def letExpression(self):

        localctx = LispParserParser.LetExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_letExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(LispParserParser.LET)
            self.state = 110
            self.match(LispParserParser.LPAREN)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 111
                self.variableDefinition()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.match(LispParserParser.RPAREN)
            self.state = 118
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuoteExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTE(self):
            return self.getToken(LispParserParser.QUOTE, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LispParserParser.RULE_quoteExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoteExpression" ):
                listener.enterQuoteExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoteExpression" ):
                listener.exitQuoteExpression(self)




    def quoteExpression(self):

        localctx = LispParserParser.QuoteExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_quoteExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(LispParserParser.QUOTE)
            self.state = 121
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LAMBDA(self):
            return self.getToken(LispParserParser.LAMBDA, 0)

        def LPAREN(self):
            return self.getToken(LispParserParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LispParserParser.RPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParserParser.ExpressionContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(LispParserParser.ParameterListContext,0)


        def getRuleIndex(self):
            return LispParserParser.RULE_lambdaExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpression" ):
                listener.enterLambdaExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpression" ):
                listener.exitLambdaExpression(self)




    def lambdaExpression(self):

        localctx = LispParserParser.LambdaExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_lambdaExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(LispParserParser.LAMBDA)
            self.state = 124
            self.match(LispParserParser.LPAREN)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 125
                self.parameterList()


            self.state = 128
            self.match(LispParserParser.RPAREN)
            self.state = 129
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(LispParserParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(LispParserParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParserParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LispParserParser.RPAREN, 0)

        def getRuleIndex(self):
            return LispParserParser.RULE_printExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpression" ):
                listener.enterPrintExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpression" ):
                listener.exitPrintExpression(self)




    def printExpression(self):

        localctx = LispParserParser.PrintExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_printExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(LispParserParser.PRINT)
            self.state = 132
            self.match(LispParserParser.LPAREN)
            self.state = 133
            self.expression()
            self.state = 134
            self.match(LispParserParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(LispParserParser.AtomContext,0)


        def binaryTail(self):
            return self.getTypedRuleContext(LispParserParser.BinaryTailContext,0)


        def getRuleIndex(self):
            return LispParserParser.RULE_binaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpression" ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpression" ):
                listener.exitBinaryExpression(self)




    def binaryExpression(self):

        localctx = LispParserParser.BinaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_binaryExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.atom()
            self.state = 137
            self.binaryTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(LispParserParser.AtomContext,0)


        def MULT(self):
            return self.getToken(LispParserParser.MULT, 0)

        def DIV(self):
            return self.getToken(LispParserParser.DIV, 0)

        def PLUS(self):
            return self.getToken(LispParserParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LispParserParser.MINUS, 0)

        def GREATER_EQUAL(self):
            return self.getToken(LispParserParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(LispParserParser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(LispParserParser.GREATER, 0)

        def LESS(self):
            return self.getToken(LispParserParser.LESS, 0)

        def EQUAL(self):
            return self.getToken(LispParserParser.EQUAL, 0)

        def binaryTail(self):
            return self.getTypedRuleContext(LispParserParser.BinaryTailContext,0)


        def getRuleIndex(self):
            return LispParserParser.RULE_binaryTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryTail" ):
                listener.enterBinaryTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryTail" ):
                listener.exitBinaryTail(self)




    def binaryTail(self):

        localctx = LispParserParser.BinaryTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_binaryTail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17]:
                self.state = 139
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self.atom()
                pass
            elif token in [14, 15]:
                self.state = 141
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 142
                self.atom()
                pass
            elif token in [19, 20, 21, 22, 23]:
                self.state = 143
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16252928) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 144
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16498688) != 0):
                self.state = 147
                self.binaryTail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





