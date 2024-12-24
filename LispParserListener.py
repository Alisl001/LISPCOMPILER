# Generated from LispParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete listener for a parse tree produced by LispParser.
class LispParserListener(ParseTreeListener):

    # Enter a parse tree produced by LispParser#program.
    def enterProgram(self, ctx:LispParser.ProgramContext):
        pass

    # Exit a parse tree produced by LispParser#program.
    def exitProgram(self, ctx:LispParser.ProgramContext):
        pass


    # Enter a parse tree produced by LispParser#defparameter.
    def enterDefparameter(self, ctx:LispParser.DefparameterContext):
        pass

    # Exit a parse tree produced by LispParser#defparameter.
    def exitDefparameter(self, ctx:LispParser.DefparameterContext):
        pass


    # Enter a parse tree produced by LispParser#defun.
    def enterDefun(self, ctx:LispParser.DefunContext):
        pass

    # Exit a parse tree produced by LispParser#defun.
    def exitDefun(self, ctx:LispParser.DefunContext):
        pass


    # Enter a parse tree produced by LispParser#params.
    def enterParams(self, ctx:LispParser.ParamsContext):
        pass

    # Exit a parse tree produced by LispParser#params.
    def exitParams(self, ctx:LispParser.ParamsContext):
        pass


    # Enter a parse tree produced by LispParser#body.
    def enterBody(self, ctx:LispParser.BodyContext):
        pass

    # Exit a parse tree produced by LispParser#body.
    def exitBody(self, ctx:LispParser.BodyContext):
        pass


    # Enter a parse tree produced by LispParser#expression.
    def enterExpression(self, ctx:LispParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LispParser#expression.
    def exitExpression(self, ctx:LispParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LispParser#lambda.
    def enterLambda(self, ctx:LispParser.LambdaContext):
        pass

    # Exit a parse tree produced by LispParser#lambda.
    def exitLambda(self, ctx:LispParser.LambdaContext):
        pass


    # Enter a parse tree produced by LispParser#funcall.
    def enterFuncall(self, ctx:LispParser.FuncallContext):
        pass

    # Exit a parse tree produced by LispParser#funcall.
    def exitFuncall(self, ctx:LispParser.FuncallContext):
        pass


    # Enter a parse tree produced by LispParser#conditional.
    def enterConditional(self, ctx:LispParser.ConditionalContext):
        pass

    # Exit a parse tree produced by LispParser#conditional.
    def exitConditional(self, ctx:LispParser.ConditionalContext):
        pass


    # Enter a parse tree produced by LispParser#operation.
    def enterOperation(self, ctx:LispParser.OperationContext):
        pass

    # Exit a parse tree produced by LispParser#operation.
    def exitOperation(self, ctx:LispParser.OperationContext):
        pass



del LispParser