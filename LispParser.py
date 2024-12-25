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
        4,1,33,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,2,1,2,1,2,5,2,54,8,2,10,2,12,2,57,
        9,2,1,2,1,2,1,2,1,3,1,3,1,3,4,3,65,8,3,11,3,12,3,66,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,86,8,
        5,1,5,1,5,1,5,1,5,1,5,1,5,4,5,94,8,5,11,5,12,5,95,1,5,1,5,1,5,3,
        5,101,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,113,8,7,10,
        7,12,7,116,9,7,1,7,1,7,1,7,1,8,5,8,122,8,8,10,8,12,8,125,9,8,1,8,
        1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,3,0,12,13,17,25,33,33,134,
        0,21,1,0,0,0,2,48,1,0,0,0,4,50,1,0,0,0,6,61,1,0,0,0,8,71,1,0,0,0,
        10,100,1,0,0,0,12,102,1,0,0,0,14,108,1,0,0,0,16,123,1,0,0,0,18,20,
        3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,
        22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,26,6,0,-1,0,26,1,1,
        0,0,0,27,28,5,1,0,0,28,49,6,1,-1,0,29,30,5,2,0,0,30,49,6,1,-1,0,
        31,32,5,16,0,0,32,49,6,1,-1,0,33,34,3,8,4,0,34,35,6,1,-1,0,35,49,
        1,0,0,0,36,37,3,4,2,0,37,38,6,1,-1,0,38,49,1,0,0,0,39,40,3,10,5,
        0,40,41,6,1,-1,0,41,49,1,0,0,0,42,43,3,6,3,0,43,44,6,1,-1,0,44,49,
        1,0,0,0,45,46,3,14,7,0,46,47,6,1,-1,0,47,49,1,0,0,0,48,27,1,0,0,
        0,48,29,1,0,0,0,48,31,1,0,0,0,48,33,1,0,0,0,48,36,1,0,0,0,48,39,
        1,0,0,0,48,42,1,0,0,0,48,45,1,0,0,0,49,3,1,0,0,0,50,51,5,26,0,0,
        51,55,5,16,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,57,1,0,0,0,55,53,1,
        0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,27,0,0,59,
        60,6,2,-1,0,60,5,1,0,0,0,61,62,5,26,0,0,62,64,7,0,0,0,63,65,3,2,
        1,0,64,63,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,68,
        1,0,0,0,68,69,5,27,0,0,69,70,6,3,-1,0,70,7,1,0,0,0,71,72,5,26,0,
        0,72,73,5,10,0,0,73,74,5,26,0,0,74,75,3,16,8,0,75,76,5,27,0,0,76,
        77,3,2,1,0,77,78,5,27,0,0,78,79,6,4,-1,0,79,9,1,0,0,0,80,81,5,26,
        0,0,81,82,5,4,0,0,82,83,3,2,1,0,83,85,3,2,1,0,84,86,3,2,1,0,85,84,
        1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,27,0,0,88,89,6,5,-1,
        0,89,101,1,0,0,0,90,91,5,26,0,0,91,93,5,5,0,0,92,94,3,12,6,0,93,
        92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,
        0,97,98,5,27,0,0,98,99,6,5,-1,0,99,101,1,0,0,0,100,80,1,0,0,0,100,
        90,1,0,0,0,101,11,1,0,0,0,102,103,5,26,0,0,103,104,3,2,1,0,104,105,
        3,2,1,0,105,106,5,27,0,0,106,107,6,6,-1,0,107,13,1,0,0,0,108,109,
        5,26,0,0,109,110,5,11,0,0,110,114,3,2,1,0,111,113,3,2,1,0,112,111,
        1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,
        1,0,0,0,116,114,1,0,0,0,117,118,5,27,0,0,118,119,6,7,-1,0,119,15,
        1,0,0,0,120,122,5,16,0,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,
        6,8,-1,0,127,17,1,0,0,0,9,21,48,55,66,85,95,100,114,123
    ]

class LispParser ( Parser ):

    grammarFileName = "LispParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'defun'", "'if'", 
                     "'cond'", "'let'", "'quote'", "'print'", "'defparameter'", 
                     "'lambda'", "'format'", "'and'", "'or'", "'not'", "'else'", 
                     "<INVALID>", "'+'", "'-'", "'/'", "'%'", "'>='", "'<='", 
                     "'>'", "'<'", "'='", "'('", "')'", "'true'", "'false'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'" ]

    symbolicNames = [ "<INVALID>", "STRING", "NUMBER", "DEFUN", "IF", "COND", 
                      "LET", "QUOTE", "PRINT", "DEFPARAMETER", "LAMBDA", 
                      "FORMAT", "AND", "OR", "NOT", "ELSE", "IDENTIFIER", 
                      "PLUS", "MINUS", "DIV", "MOD", "GREATER_EQUAL", "LESS_EQUAL", 
                      "GREATER", "LESS", "EQUAL", "LPAREN", "RPAREN", "TRUE", 
                      "FALSE", "COMMENT", "WS", "ERROR", "MULT" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_funcall = 2
    RULE_operation = 3
    RULE_lambda = 4
    RULE_conditional = 5
    RULE_condClause = 6
    RULE_formatCall = 7
    RULE_params = 8

    ruleNames =  [ "program", "expression", "funcall", "operation", "lambda", 
                   "conditional", "condClause", "formatCall", "params" ]

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
    ELSE=15
    IDENTIFIER=16
    PLUS=17
    MINUS=18
    DIV=19
    MOD=20
    GREATER_EQUAL=21
    LESS_EQUAL=22
    GREATER=23
    LESS=24
    EQUAL=25
    LPAREN=26
    RPAREN=27
    TRUE=28
    FALSE=29
    COMMENT=30
    WS=31
    ERROR=32
    MULT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



      from ASTNodes import *

      def build_program(self, expressions):
          program = ProgramNode()
          for expr in expressions:
              program.add_child(expr)
          return program



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self._expression = None # ExpressionContext
            self.exprs = list() # of ExpressionContexts

        def EOF(self):
            return self.getToken(LispParser.EOF, 0)

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67174406) != 0):
                self.state = 18
                localctx._expression = self.expression()
                localctx.exprs.append(localctx._expression)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(LispParser.EOF)
             localctx.node =  self.build_program(localctx.exprs) 
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
            self.node = None
            self._STRING = None # Token
            self._NUMBER = None # Token
            self._IDENTIFIER = None # Token
            self._lambda = None # LambdaContext
            self._funcall = None # FuncallContext
            self._conditional = None # ConditionalContext
            self._operation = None # OperationContext
            self._formatCall = None # FormatCallContext

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
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                localctx._STRING = self.match(LispParser.STRING)
                 localctx.node =  LiteralNode((None if localctx._STRING is None else localctx._STRING.text)) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                localctx._NUMBER = self.match(LispParser.NUMBER)
                 localctx.node =  LiteralNode((None if localctx._NUMBER is None else localctx._NUMBER.text)) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                localctx._IDENTIFIER = self.match(LispParser.IDENTIFIER)
                 localctx.node =  IdentifierNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                localctx._lambda = self.lambda_()
                 localctx.node =  localctx._lambda.node 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 36
                localctx._funcall = self.funcall()
                 localctx.node =  localctx._funcall.node 
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                localctx._conditional = self.conditional()
                 localctx.node =  localctx._conditional.node 
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 42
                localctx._operation = self.operation()
                 localctx.node =  localctx._operation.node 
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 45
                localctx._formatCall = self.formatCall()
                 localctx.node =  localctx._formatCall.node 
                pass


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
            self.node = None
            self._IDENTIFIER = None # Token
            self._expression = None # ExpressionContext
            self.exprs = list() # of ExpressionContexts

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
        self.enterRule(localctx, 4, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(LispParser.LPAREN)
            self.state = 51
            localctx._IDENTIFIER = self.match(LispParser.IDENTIFIER)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67174406) != 0):
                self.state = 52
                localctx._expression = self.expression()
                localctx.exprs.append(localctx._expression)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(LispParser.RPAREN)

                    func = FunctionCallNode((None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text))
                    for expr in localctx.exprs:
                        func.add_child(expr)
                    localctx.node =  func
                
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
            self.node = None
            self.op = None # Token
            self._expression = None # ExpressionContext
            self.exprs = list() # of ExpressionContexts

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

        def AND(self):
            return self.getToken(LispParser.AND, 0)

        def OR(self):
            return self.getToken(LispParser.OR, 0)

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
        self.enterRule(localctx, 6, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LispParser.LPAREN)
            self.state = 62
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8656924672) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                localctx._expression = self.expression()
                localctx.exprs.append(localctx._expression)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67174406) != 0)):
                    break

            self.state = 68
            self.match(LispParser.RPAREN)

                    operation = OperationNode((None if localctx.op is None else localctx.op.text))
                    for expr in localctx.exprs:
                        operation.add_child(expr)
                    localctx.node =  operation
                
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
            self.node = None
            self._params = None # ParamsContext
            self._expression = None # ExpressionContext

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.LPAREN)
            else:
                return self.getToken(LispParser.LPAREN, i)

        def LAMBDA(self):
            return self.getToken(LispParser.LAMBDA, 0)

        def params(self):
            return self.getTypedRuleContext(LispParser.ParamsContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(LispParser.RPAREN)
            else:
                return self.getToken(LispParser.RPAREN, i)

        def expression(self):
            return self.getTypedRuleContext(LispParser.ExpressionContext,0)


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
        self.enterRule(localctx, 8, self.RULE_lambda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(LispParser.LPAREN)
            self.state = 72
            self.match(LispParser.LAMBDA)
            self.state = 73
            self.match(LispParser.LPAREN)
            self.state = 74
            localctx._params = self.params()
            self.state = 75
            self.match(LispParser.RPAREN)
            self.state = 76
            localctx._expression = self.expression()
            self.state = 77
            self.match(LispParser.RPAREN)

                    lambda_node = LambdaNode()
                    if localctx._params.node:
                        lambda_node.add_child(localctx._params.node)
                    lambda_node.add_child(localctx._expression.node)
                    localctx.node =  lambda_node
                
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
            self.node = None
            self.test = None # ExpressionContext
            self.then = None # ExpressionContext
            self.else_ = None # ExpressionContext
            self._condClause = None # CondClauseContext
            self.clauses = list() # of CondClauseContexts

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def IF(self):
            return self.getToken(LispParser.IF, 0)

        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


        def COND(self):
            return self.getToken(LispParser.COND, 0)

        def condClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.CondClauseContext)
            else:
                return self.getTypedRuleContext(LispParser.CondClauseContext,i)


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
        self.enterRule(localctx, 10, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(LispParser.LPAREN)
                self.state = 81
                self.match(LispParser.IF)
                self.state = 82
                localctx.test = self.expression()
                self.state = 83
                localctx.then = self.expression()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67174406) != 0):
                    self.state = 84
                    localctx.else_ = self.expression()


                self.state = 87
                self.match(LispParser.RPAREN)

                        conditional_node = ConditionalNode("if")
                        conditional_node.add_child(localctx.test.node)
                        conditional_node.add_child(localctx.then.node)
                        if (localctx.else_.node != null) {
                            conditional_node.add_child(localctx.else_.node);
                        }
                        localctx.node =  conditional_node
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(LispParser.LPAREN)
                self.state = 91
                self.match(LispParser.COND)
                self.state = 93 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 92
                    localctx._condClause = self.condClause()
                    localctx.clauses.append(localctx._condClause)
                    self.state = 95 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==26):
                        break

                self.state = 97
                self.match(LispParser.RPAREN)

                        cond_node = ConditionalNode("cond")
                        for clause in localctx.clauses:
                            cond_node.add_child(clause.node)
                        localctx.node =  cond_node
                    
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.node = None
            self.test = None # ExpressionContext
            self.result = None # ExpressionContext

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
            return LispParser.RULE_condClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondClause" ):
                listener.enterCondClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondClause" ):
                listener.exitCondClause(self)




    def condClause(self):

        localctx = LispParser.CondClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(LispParser.LPAREN)
            self.state = 103
            localctx.test = self.expression()
            self.state = 104
            localctx.result = self.expression()
            self.state = 105
            self.match(LispParser.RPAREN)

                    clause_node = CondClauseNode()
                    clause_node.add_child(localctx.test.node)
                    clause_node.add_child(localctx.result.node)
                    localctx.node =  clause_node
                
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
            self.node = None
            self.format_string = None # ExpressionContext
            self._expression = None # ExpressionContext
            self.args = list() # of ExpressionContexts

        def LPAREN(self):
            return self.getToken(LispParser.LPAREN, 0)

        def FORMAT(self):
            return self.getToken(LispParser.FORMAT, 0)

        def RPAREN(self):
            return self.getToken(LispParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LispParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LispParser.ExpressionContext,i)


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
        self.enterRule(localctx, 14, self.RULE_formatCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(LispParser.LPAREN)
            self.state = 109
            self.match(LispParser.FORMAT)
            self.state = 110
            localctx.format_string = self.expression()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67174406) != 0):
                self.state = 111
                localctx._expression = self.expression()
                localctx.args.append(localctx._expression)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self.match(LispParser.RPAREN)

                    format_node = FormatCallNode()
                    format_node.add_child(localctx.format_string.node)
                    for arg in localctx.args:
                        format_node.add_child(arg.node)  // Ensure access to `node`
                    localctx.node =  format_node
                
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
            self.node = None
            self._IDENTIFIER = None # Token
            self.ids = list() # of Tokens

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
        self.enterRule(localctx, 16, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 120
                localctx._IDENTIFIER = self.match(LispParser.IDENTIFIER)
                localctx.ids.append(localctx._IDENTIFIER)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)


                    params_node = ParameterListNode()
                    for id in localctx.ids:
                        params_node.add_child(IdentifierNode(id.text))
                    localctx.node =  params_node
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





