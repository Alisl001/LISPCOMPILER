# Generated from LispParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LispParser import LispParser
else:
    from LispParser import LispParser

# This class defines a complete generic visitor for a parse tree produced by LispParser.

class LispParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LispParser#program.
    def visitProgram(self, ctx:LispParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#defparameter.
    def visitDefparameter(self, ctx:LispParser.DefparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#defun.
    def visitDefun(self, ctx:LispParser.DefunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#params.
    def visitParams(self, ctx:LispParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#body.
    def visitBody(self, ctx:LispParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#expression.
    def visitExpression(self, ctx:LispParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#lambda.
    def visitLambda(self, ctx:LispParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#funcall.
    def visitFuncall(self, ctx:LispParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#operation.
    def visitOperation(self, ctx:LispParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#conditional.
    def visitConditional(self, ctx:LispParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LispParser#formatCall.
    def visitFormatCall(self, ctx:LispParser.FormatCallContext):
        return self.visitChildren(ctx)



del LispParser