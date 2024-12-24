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
        4,1,32,138,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        3,2,44,8,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,5,3,53,8,3,10,3,12,3,56,9,
        3,1,4,5,4,59,8,4,10,4,12,4,62,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,72,8,5,1,6,1,6,1,6,1,6,3,6,78,8,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,5,7,87,8,7,10,7,12,7,90,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,
        99,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,4,8,110,8,8,11,8,12,8,
        111,1,8,1,8,3,8,116,8,8,1,9,1,9,1,9,1,9,5,9,122,8,9,10,9,12,9,125,
        9,9,1,9,1,9,1,10,1,10,1,10,4,10,132,8,10,11,10,12,10,133,1,10,1,
        10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,1,2,0,16,24,32,32,146,
        0,27,1,0,0,0,2,32,1,0,0,0,4,38,1,0,0,0,6,50,1,0,0,0,8,60,1,0,0,0,
        10,71,1,0,0,0,12,73,1,0,0,0,14,83,1,0,0,0,16,115,1,0,0,0,18,117,
        1,0,0,0,20,128,1,0,0,0,22,26,3,10,5,0,23,26,3,2,1,0,24,26,3,4,2,
        0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,
        1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,1,
        31,1,1,0,0,0,32,33,5,25,0,0,33,34,5,9,0,0,34,35,5,15,0,0,35,36,3,
        10,5,0,36,37,5,26,0,0,37,3,1,0,0,0,38,39,5,25,0,0,39,40,5,3,0,0,
        40,41,5,15,0,0,41,43,5,25,0,0,42,44,3,6,3,0,43,42,1,0,0,0,43,44,
        1,0,0,0,44,45,1,0,0,0,45,46,5,26,0,0,46,47,5,1,0,0,47,48,3,8,4,0,
        48,49,5,26,0,0,49,5,1,0,0,0,50,54,5,15,0,0,51,53,5,15,0,0,52,51,
        1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,
        54,1,0,0,0,57,59,3,10,5,0,58,57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,
        0,0,60,61,1,0,0,0,61,9,1,0,0,0,62,60,1,0,0,0,63,72,5,1,0,0,64,72,
        5,2,0,0,65,72,5,15,0,0,66,72,3,12,6,0,67,72,3,14,7,0,68,72,3,16,
        8,0,69,72,3,20,10,0,70,72,3,18,9,0,71,63,1,0,0,0,71,64,1,0,0,0,71,
        65,1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,71,68,1,0,0,0,71,69,1,0,0,
        0,71,70,1,0,0,0,72,11,1,0,0,0,73,74,5,25,0,0,74,75,5,10,0,0,75,77,
        5,25,0,0,76,78,3,6,3,0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,
        79,80,5,26,0,0,80,81,3,10,5,0,81,82,5,26,0,0,82,13,1,0,0,0,83,84,
        5,25,0,0,84,88,5,15,0,0,85,87,3,10,5,0,86,85,1,0,0,0,87,90,1,0,0,
        0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,92,
        5,26,0,0,92,15,1,0,0,0,93,94,5,25,0,0,94,95,5,4,0,0,95,96,3,10,5,
        0,96,98,3,10,5,0,97,99,3,10,5,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,
        1,0,0,0,100,101,5,26,0,0,101,116,1,0,0,0,102,103,5,25,0,0,103,109,
        5,5,0,0,104,105,5,25,0,0,105,106,3,10,5,0,106,107,3,10,5,0,107,108,
        5,26,0,0,108,110,1,0,0,0,109,104,1,0,0,0,110,111,1,0,0,0,111,109,
        1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,5,26,0,0,114,116,
        1,0,0,0,115,93,1,0,0,0,115,102,1,0,0,0,116,17,1,0,0,0,117,118,5,
        25,0,0,118,119,5,11,0,0,119,123,3,10,5,0,120,122,3,10,5,0,121,120,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,
        1,0,0,0,125,123,1,0,0,0,126,127,5,26,0,0,127,19,1,0,0,0,128,129,
        5,25,0,0,129,131,7,0,0,0,130,132,3,10,5,0,131,130,1,0,0,0,132,133,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,
        5,26,0,0,136,21,1,0,0,0,13,25,27,43,54,60,71,77,88,98,111,115,123,
        133
    ]

class LispParser ( Parser ):

    grammarFileName = "LispParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'defun'", "'if'", 
                     "'cond'", "'let'", "'quote'", "'print'", "'defparameter'", 
                     "'lambda'", "'format'", "'and'", "'or'", "'not'", "<INVALID>", 
                     "'+'", "'-'", "'/'", "'%'", "'>='", "'<='", "'>'", 
                     "'<'", "'='", "'('", "')'", "'true'", "'false'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "STRING", "NUMBER", "DEFUN", "IF", "COND", 
                      "LET", "QUOTE", "PRINT", "DEFPARAMETER", "LAMBDA", 
                      "FORMAT", "AND", "OR", "NOT", "IDENTIFIER", "PLUS", 
                      "MINUS", "DIV", "MOD", "GREATER_EQUAL", "LESS_EQUAL", 
                      "GREATER", "LESS", "EQUAL", "LPAREN", "RPAREN", "TRUE", 
                      "FALSE", "COMMENT", "WS", "ERROR", "MULT" ]

    RULE_program = 0
    RULE_defparameter = 1
    RULE_defun = 2
    RULE_params = 3
    RULE_body = 4
    RULE_expression = 5
    RULE_lambda = 6
    RULE_funcall = 7
    RULE_conditional = 8
    RULE_formatCall = 9
    RULE_operation = 10

    ruleNames =  [ "program", "defparameter", "defun", "params", "body", 
                   "expression", "lambda", "funcall", "conditional", "formatCall", 
                   "operation" ]

    EOF = Token.EOF
    STRING=1
    NUMBER=2
    DEFUN=3
    IF=4
    COND=5
    LET=6
    QUOTE=7
    PRINT=8
    DEFPARAMETER=9
    LAMBDA=10
    FORMAT=11
    AND=12
    OR=13
    NOT=14
    IDENTIFIER=15
    PLUS=16
    MINUS=17
    DIV=18
    MOD=19
    GREATER_EQUAL=20
    LESS_EQUAL=21
    GREATER=22
    LESS=23
    EQUAL=24
    LPAREN=25
    RPAREN=26
    TRUE=27
    FALSE=28
    COMMENT=29
    WS=30
    ERROR=31
    MULT=32

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
            return self.getToken(LispParser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def defparameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.DefparameterContext)
            else:
                return self.getTypedRuleContext(LispParser.DefparameterContext,i)


        def defun(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.DefunContext)
            else:
                return self.getTypedRuleContext(LispParser.DefunContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = LispParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.expression()
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.defparameter()
                    pass

                elif la_ == 3:
                    self.state = 24
                    self.defun()
                    pass


                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(LispParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefparameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def DEFPARAMETER(self):
            return self.getToken(LispParser.DEFPARAMETER, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def getRuleIndex(self):
            return LispParser.RULE_defparameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefparameter" ):
                listener.enterDefparameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefparameter" ):
                listener.exitDefparameter(self)




    def defparameter(self):

        localctx = LispParser.DefparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_defparameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(LispParser.LPAREN)
            self.state = 33
            self.match(LispParser.DEFPARAMETER)
            self.state = 34
            self.match(LispParser.IDENTIFIER)
            self.state = 35
            self.expression()
            self.state = 36
            self.match(LispParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefunContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.LPAREN)
            else:
                return self.getToken(LispParser.LPAREN, i)

        def DEFUN(self):
            return self.getToken(LispParser.DEFUN, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParser.IDENTIFIER, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.RPAREN)
            else:
                return self.getToken(LispParser.RPAREN, i)

        def STRING(self):
            return self.getToken(LispParser.STRING, 0)

        def body(self):
            return self.getTypedRuleContext(LispParser.BodyContext,0)


        def params(self):
            return self.getTypedRuleContext(LispParser.ParamsContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_defun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefun" ):
                listener.enterDefun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefun" ):
                listener.exitDefun(self)




    def defun(self):

        localctx = LispParser.DefunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_defun)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(LispParser.LPAREN)
            self.state = 39
            self.match(LispParser.DEFUN)
            self.state = 40
            self.match(LispParser.IDENTIFIER)
            self.state = 41
            self.match(LispParser.LPAREN)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 42
                self.params()


            self.state = 45
            self.match(LispParser.RPAREN)
            self.state = 46
            self.match(LispParser.STRING)
            self.state = 47
            self.body()
            self.state = 48
            self.match(LispParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.IDENTIFIER)
            else:
                return self.getToken(LispParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LispParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = LispParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(LispParser.IDENTIFIER)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 51
                self.match(LispParser.IDENTIFIER)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = LispParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                self.state = 57
                self.expression()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def STRING(self):
            return self.getToken(LispParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(LispParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParser.IDENTIFIER, 0)

        def lambda_(self):
            return self.getTypedRuleContext(LispParser.LambdaContext,0)


        def funcall(self):
            return self.getTypedRuleContext(LispParser.FuncallContext,0)


        def conditional(self):
            return self.getTypedRuleContext(LispParser.ConditionalContext,0)


        def operation(self):
            return self.getTypedRuleContext(LispParser.OperationContext,0)


        def formatCall(self):
            return self.getTypedRuleContext(LispParser.FormatCallContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LispParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(LispParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(LispParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(LispParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.lambda_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.funcall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.operation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.formatCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.LPAREN)
            else:
                return self.getToken(LispParser.LPAREN, i)

        def LAMBDA(self):
            return self.getToken(LispParser.LAMBDA, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.RPAREN)
            else:
                return self.getToken(LispParser.RPAREN, i)

        def expression(self):
            return self.getTypedRuleContext(LispParser.ExpressionContext,0)


        def params(self):
            return self.getTypedRuleContext(LispParser.ParamsContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_lambda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambda" ):
                listener.enterLambda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambda" ):
                listener.exitLambda(self)




    def lambda_(self):

        localctx = LispParser.LambdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lambda)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(LispParser.LPAREN)
            self.state = 74
            self.match(LispParser.LAMBDA)
            self.state = 75
            self.match(LispParser.LPAREN)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 76
                self.params()


            self.state = 79
            self.match(LispParser.RPAREN)
            self.state = 80
            self.expression()
            self.state = 81
            self.match(LispParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParser.IDENTIFIER, 0)

        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_funcall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncall" ):
                listener.enterFuncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncall" ):
                listener.exitFuncall(self)




    def funcall(self):

        localctx = LispParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(LispParser.LPAREN)
            self.state = 84
            self.match(LispParser.IDENTIFIER)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                self.state = 85
                self.expression()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(LispParser.RPAREN)
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

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.LPAREN)
            else:
                return self.getToken(LispParser.LPAREN, i)

        def IF(self):
            return self.getToken(LispParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.RPAREN)
            else:
                return self.getToken(LispParser.RPAREN, i)

        def COND(self):
            return self.getToken(LispParser.COND, 0)

        def getRuleIndex(self):
            return LispParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = LispParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(LispParser.LPAREN)
                self.state = 94
                self.match(LispParser.IF)
                self.state = 95
                self.expression()
                self.state = 96
                self.expression()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                    self.state = 97
                    self.expression()


                self.state = 100
                self.match(LispParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(LispParser.LPAREN)
                self.state = 103
                self.match(LispParser.COND)
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 104
                    self.match(LispParser.LPAREN)
                    self.state = 105
                    self.expression()
                    self.state = 106
                    self.expression()
                    self.state = 107
                    self.match(LispParser.RPAREN)
                    self.state = 111 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==25):
                        break

                self.state = 113
                self.match(LispParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def FORMAT(self):
            return self.getToken(LispParser.FORMAT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def getRuleIndex(self):
            return LispParser.RULE_formatCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormatCall" ):
                listener.enterFormatCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormatCall" ):
                listener.exitFormatCall(self)




    def formatCall(self):

        localctx = LispParser.FormatCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_formatCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(LispParser.LPAREN)
            self.state = 118
            self.match(LispParser.FORMAT)
            self.state = 119
            self.expression()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                self.state = 120
                self.expression()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(LispParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def PLUS(self):
            return self.getToken(LispParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(LispParser.MINUS, 0)

        def MULT(self):
            return self.getToken(LispParser.MULT, 0)

        def DIV(self):
            return self.getToken(LispParser.DIV, 0)

        def MOD(self):
            return self.getToken(LispParser.MOD, 0)

        def GREATER_EQUAL(self):
            return self.getToken(LispParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(LispParser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(LispParser.GREATER, 0)

        def LESS(self):
            return self.getToken(LispParser.LESS, 0)

        def EQUAL(self):
            return self.getToken(LispParser.EQUAL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)




    def operation(self):

        localctx = LispParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(LispParser.LPAREN)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4328456192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.expression()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0)):
                    break

            self.state = 135
            self.match(LispParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





