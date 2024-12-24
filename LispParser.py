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
        4,1,32,124,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,2,42,8,2,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,5,3,51,8,3,10,3,12,3,54,9,3,1,4,5,4,
        57,8,4,10,4,12,4,60,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,69,8,5,1,
        6,1,6,1,6,1,6,3,6,75,8,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,84,8,7,
        10,7,12,7,87,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,96,8,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,4,8,107,8,8,11,8,12,8,108,1,8,1,8,3,
        8,113,8,8,1,9,1,9,1,9,4,9,118,8,9,11,9,12,9,119,1,9,1,9,1,9,0,0,
        10,0,2,4,6,8,10,12,14,16,18,0,1,2,0,16,24,32,32,131,0,25,1,0,0,0,
        2,30,1,0,0,0,4,36,1,0,0,0,6,48,1,0,0,0,8,58,1,0,0,0,10,68,1,0,0,
        0,12,70,1,0,0,0,14,80,1,0,0,0,16,112,1,0,0,0,18,114,1,0,0,0,20,24,
        3,10,5,0,21,24,3,2,1,0,22,24,3,4,2,0,23,20,1,0,0,0,23,21,1,0,0,0,
        23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,
        0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,31,5,25,0,0,31,
        32,5,9,0,0,32,33,5,15,0,0,33,34,3,10,5,0,34,35,5,26,0,0,35,3,1,0,
        0,0,36,37,5,25,0,0,37,38,5,3,0,0,38,39,5,15,0,0,39,41,5,25,0,0,40,
        42,3,6,3,0,41,40,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,5,26,
        0,0,44,45,5,1,0,0,45,46,3,8,4,0,46,47,5,26,0,0,47,5,1,0,0,0,48,52,
        5,15,0,0,49,51,5,15,0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,
        0,52,53,1,0,0,0,53,7,1,0,0,0,54,52,1,0,0,0,55,57,3,10,5,0,56,55,
        1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,9,1,0,0,0,60,
        58,1,0,0,0,61,69,5,1,0,0,62,69,5,2,0,0,63,69,5,15,0,0,64,69,3,12,
        6,0,65,69,3,14,7,0,66,69,3,16,8,0,67,69,3,18,9,0,68,61,1,0,0,0,68,
        62,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,0,68,65,1,0,0,0,68,66,1,0,0,
        0,68,67,1,0,0,0,69,11,1,0,0,0,70,71,5,25,0,0,71,72,5,10,0,0,72,74,
        5,25,0,0,73,75,3,6,3,0,74,73,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,
        76,77,5,26,0,0,77,78,3,10,5,0,78,79,5,26,0,0,79,13,1,0,0,0,80,81,
        5,25,0,0,81,85,5,15,0,0,82,84,3,10,5,0,83,82,1,0,0,0,84,87,1,0,0,
        0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,
        5,26,0,0,89,15,1,0,0,0,90,91,5,25,0,0,91,92,5,4,0,0,92,93,3,10,5,
        0,93,95,3,10,5,0,94,96,3,10,5,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,
        1,0,0,0,97,98,5,26,0,0,98,113,1,0,0,0,99,100,5,25,0,0,100,106,5,
        5,0,0,101,102,5,25,0,0,102,103,3,10,5,0,103,104,3,10,5,0,104,105,
        5,26,0,0,105,107,1,0,0,0,106,101,1,0,0,0,107,108,1,0,0,0,108,106,
        1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,111,5,26,0,0,111,113,
        1,0,0,0,112,90,1,0,0,0,112,99,1,0,0,0,113,17,1,0,0,0,114,115,5,25,
        0,0,115,117,7,0,0,0,116,118,3,10,5,0,117,116,1,0,0,0,118,119,1,0,
        0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,122,5,26,
        0,0,122,19,1,0,0,0,12,23,25,41,52,58,68,74,85,95,108,112,119
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
    RULE_operation = 9

    ruleNames =  [ "program", "defparameter", "defun", "params", "body", 
                   "expression", "lambda", "funcall", "conditional", "operation" ]

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                self.state = 23
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 20
                    self.expression()
                    pass

                elif la_ == 2:
                    self.state = 21
                    self.defparameter()
                    pass

                elif la_ == 3:
                    self.state = 22
                    self.defun()
                    pass


                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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
            self.state = 30
            self.match(LispParser.LPAREN)
            self.state = 31
            self.match(LispParser.DEFPARAMETER)
            self.state = 32
            self.match(LispParser.IDENTIFIER)
            self.state = 33
            self.expression()
            self.state = 34
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
            self.state = 36
            self.match(LispParser.LPAREN)
            self.state = 37
            self.match(LispParser.DEFUN)
            self.state = 38
            self.match(LispParser.IDENTIFIER)
            self.state = 39
            self.match(LispParser.LPAREN)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 40
                self.params()


            self.state = 43
            self.match(LispParser.RPAREN)
            self.state = 44
            self.match(LispParser.STRING)
            self.state = 45
            self.body()
            self.state = 46
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
            self.state = 48
            self.match(LispParser.IDENTIFIER)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 49
                self.match(LispParser.IDENTIFIER)
                self.state = 54
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
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                self.state = 55
                self.expression()
                self.state = 60
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
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(LispParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(LispParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(LispParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.lambda_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.funcall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.operation()
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
            self.state = 70
            self.match(LispParser.LPAREN)
            self.state = 71
            self.match(LispParser.LAMBDA)
            self.state = 72
            self.match(LispParser.LPAREN)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 73
                self.params()


            self.state = 76
            self.match(LispParser.RPAREN)
            self.state = 77
            self.expression()
            self.state = 78
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
            self.state = 80
            self.match(LispParser.LPAREN)
            self.state = 81
            self.match(LispParser.IDENTIFIER)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                self.state = 82
                self.expression()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(LispParser.LPAREN)
                self.state = 91
                self.match(LispParser.IF)
                self.state = 92
                self.expression()
                self.state = 93
                self.expression()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0):
                    self.state = 94
                    self.expression()


                self.state = 97
                self.match(LispParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(LispParser.LPAREN)
                self.state = 100
                self.match(LispParser.COND)
                self.state = 106 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 101
                    self.match(LispParser.LPAREN)
                    self.state = 102
                    self.expression()
                    self.state = 103
                    self.expression()
                    self.state = 104
                    self.match(LispParser.RPAREN)
                    self.state = 108 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==25):
                        break

                self.state = 110
                self.match(LispParser.RPAREN)
                pass


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
        self.enterRule(localctx, 18, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(LispParser.LPAREN)
            self.state = 115
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4328456192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.expression()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 33587206) != 0)):
                    break

            self.state = 121
            self.match(LispParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





