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
        4,1,29,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,3,1,3,4,3,39,8,3,11,3,12,
        3,40,1,3,1,3,1,4,1,4,1,4,1,4,3,4,49,8,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,60,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,4,7,71,
        8,7,11,7,12,7,72,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,5,9,84,8,9,
        10,9,12,9,87,9,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,3,0,1,2,
        12,12,24,25,90,0,21,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,36,1,0,0,
        0,8,44,1,0,0,0,10,59,1,0,0,0,12,61,1,0,0,0,14,67,1,0,0,0,16,76,1,
        0,0,0,18,81,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,
        21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,0,25,33,3,4,2,0,26,33,3,6,3,
        0,27,33,3,8,4,0,28,33,3,10,5,0,29,33,3,16,8,0,30,33,3,12,6,0,31,
        33,3,14,7,0,32,25,1,0,0,0,32,26,1,0,0,0,32,27,1,0,0,0,32,28,1,0,
        0,0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,
        7,0,0,0,35,5,1,0,0,0,36,38,5,22,0,0,37,39,3,2,1,0,38,37,1,0,0,0,
        39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,5,
        23,0,0,43,7,1,0,0,0,44,45,5,3,0,0,45,46,5,12,0,0,46,48,5,22,0,0,
        47,49,3,18,9,0,48,47,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,51,5,
        23,0,0,51,52,3,2,1,0,52,9,1,0,0,0,53,54,5,9,0,0,54,55,5,12,0,0,55,
        60,3,2,1,0,56,57,5,6,0,0,57,58,5,12,0,0,58,60,3,2,1,0,59,53,1,0,
        0,0,59,56,1,0,0,0,60,11,1,0,0,0,61,62,5,10,0,0,62,63,5,22,0,0,63,
        64,3,18,9,0,64,65,5,23,0,0,65,66,3,2,1,0,66,13,1,0,0,0,67,68,5,12,
        0,0,68,70,5,22,0,0,69,71,3,2,1,0,70,69,1,0,0,0,71,72,1,0,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,23,0,0,75,15,1,0,
        0,0,76,77,5,4,0,0,77,78,3,2,1,0,78,79,3,2,1,0,79,80,3,2,1,0,80,17,
        1,0,0,0,81,85,5,12,0,0,82,84,5,12,0,0,83,82,1,0,0,0,84,87,1,0,0,
        0,85,83,1,0,0,0,85,86,1,0,0,0,86,19,1,0,0,0,87,85,1,0,0,0,7,23,32,
        40,48,59,72,85
    ]

class LispParser ( Parser ):

    grammarFileName = "LispParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'defun'", "'if'", 
                     "'cond'", "'let'", "'quote'", "'print'", "'defparameter'", 
                     "'lambda'", "'format'", "<INVALID>", "'+'", "'-'", 
                     "'/'", "'%'", "'>='", "'<='", "'>'", "'<'", "'='", 
                     "'('", "')'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "STRING", "NUMBER", "DEFUN", "IF", "COND", 
                      "LET", "QUOTE", "PRINT", "DEFPARAMETER", "LAMBDA", 
                      "FORMAT", "IDENTIFIER", "PLUS", "MINUS", "DIV", "MOD", 
                      "GREATER_EQUAL", "LESS_EQUAL", "GREATER", "LESS", 
                      "EQUAL", "LPAREN", "RPAREN", "TRUE", "FALSE", "COMMENT", 
                      "WS", "ERROR", "MULT" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_atom = 2
    RULE_list = 3
    RULE_functionDefinition = 4
    RULE_variableDefinition = 5
    RULE_lambdaDefinition = 6
    RULE_functionCall = 7
    RULE_conditional = 8
    RULE_parameterList = 9

    ruleNames =  [ "program", "expression", "atom", "list", "functionDefinition", 
                   "variableDefinition", "lambdaDefinition", "functionCall", 
                   "conditional", "parameterList" ]

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
    IDENTIFIER=12
    PLUS=13
    MINUS=14
    DIV=15
    MOD=16
    GREATER_EQUAL=17
    LESS_EQUAL=18
    GREATER=19
    LESS=20
    EQUAL=21
    LPAREN=22
    RPAREN=23
    TRUE=24
    FALSE=25
    COMMENT=26
    WS=27
    ERROR=28
    MULT=29

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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.expression()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 54531678) != 0)):
                    break

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

        def atom(self):
            return self.getTypedRuleContext(LispParser.AtomContext,0)


        def list_(self):
            return self.getTypedRuleContext(LispParser.ListContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(LispParser.FunctionDefinitionContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(LispParser.VariableDefinitionContext,0)


        def conditional(self):
            return self.getTypedRuleContext(LispParser.ConditionalContext,0)


        def lambdaDefinition(self):
            return self.getTypedRuleContext(LispParser.LambdaDefinitionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(LispParser.FunctionCallContext,0)


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
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.list_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.functionDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.variableDefinition()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.conditional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.lambdaDefinition()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 31
                self.functionCall()
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
            return self.getToken(LispParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(LispParser.STRING, 0)

        def TRUE(self):
            return self.getToken(LispParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LispParser.FALSE, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LispParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = LispParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 50335750) != 0)):
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


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = LispParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(LispParser.LPAREN)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.expression()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 54531678) != 0)):
                    break

            self.state = 42
            self.match(LispParser.RPAREN)
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
            return self.getToken(LispParser.DEFUN, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParser.ExpressionContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(LispParser.ParameterListContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = LispParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(LispParser.DEFUN)
            self.state = 45
            self.match(LispParser.IDENTIFIER)
            self.state = 46
            self.match(LispParser.LPAREN)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 47
                self.parameterList()


            self.state = 50
            self.match(LispParser.RPAREN)
            self.state = 51
            self.expression()
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

        def DEFPARAMETER(self):
            return self.getToken(LispParser.DEFPARAMETER, 0)

        def IDENTIFIER(self):
            return self.getToken(LispParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParser.ExpressionContext,0)


        def LET(self):
            return self.getToken(LispParser.LET, 0)

        def getRuleIndex(self):
            return LispParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)




    def variableDefinition(self):

        localctx = LispParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDefinition)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(LispParser.DEFPARAMETER)
                self.state = 54
                self.match(LispParser.IDENTIFIER)
                self.state = 55
                self.expression()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(LispParser.LET)
                self.state = 57
                self.match(LispParser.IDENTIFIER)
                self.state = 58
                self.expression()
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


    class LambdaDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LAMBDA(self):
            return self.getToken(LispParser.LAMBDA, 0)

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(LispParser.ParameterListContext,0)


        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LispParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LispParser.RULE_lambdaDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaDefinition" ):
                listener.enterLambdaDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaDefinition" ):
                listener.exitLambdaDefinition(self)




    def lambdaDefinition(self):

        localctx = LispParser.LambdaDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lambdaDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LispParser.LAMBDA)
            self.state = 62
            self.match(LispParser.LPAREN)
            self.state = 63
            self.parameterList()
            self.state = 64
            self.match(LispParser.RPAREN)
            self.state = 65
            self.expression()
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
            return self.getToken(LispParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LispParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = LispParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(LispParser.IDENTIFIER)
            self.state = 68
            self.match(LispParser.LPAREN)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.expression()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 54531678) != 0)):
                    break

            self.state = 74
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

        def IF(self):
            return self.getToken(LispParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(LispParser.IF)
            self.state = 77
            self.expression()
            self.state = 78
            self.expression()
            self.state = 79
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
                return self.getTokens(LispParser.IDENTIFIER)
            else:
                return self.getToken(LispParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LispParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = LispParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(LispParser.IDENTIFIER)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 82
                self.match(LispParser.IDENTIFIER)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





