# Generated from LispParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LispParserParser import LispParserParser
else:
    from LispParserParser import LispParserParser

# This class defines a complete listener for a parse tree produced by LispParserParser.
class LispParserListener(ParseTreeListener):

    # Enter a parse tree produced by LispParserParser#program.
    def enterProgram(self, ctx:LispParserParser.ProgramContext):
        pass

    # Exit a parse tree produced by LispParserParser#program.
    def exitProgram(self, ctx:LispParserParser.ProgramContext):
        pass


    # Enter a parse tree produced by LispParserParser#expression.
    def enterExpression(self, ctx:LispParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LispParserParser#expression.
    def exitExpression(self, ctx:LispParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LispParserParser#atom.
    def enterAtom(self, ctx:LispParserParser.AtomContext):
        pass

    # Exit a parse tree produced by LispParserParser#atom.
    def exitAtom(self, ctx:LispParserParser.AtomContext):
        pass


    # Enter a parse tree produced by LispParserParser#functionCall.
    def enterFunctionCall(self, ctx:LispParserParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by LispParserParser#functionCall.
    def exitFunctionCall(self, ctx:LispParserParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by LispParserParser#formatArguments.
    def enterFormatArguments(self, ctx:LispParserParser.FormatArgumentsContext):
        pass

    # Exit a parse tree produced by LispParserParser#formatArguments.
    def exitFormatArguments(self, ctx:LispParserParser.FormatArgumentsContext):
        pass


    # Enter a parse tree produced by LispParserParser#argumentList.
    def enterArgumentList(self, ctx:LispParserParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by LispParserParser#argumentList.
    def exitArgumentList(self, ctx:LispParserParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by LispParserParser#variableDefinition.
    def enterVariableDefinition(self, ctx:LispParserParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by LispParserParser#variableDefinition.
    def exitVariableDefinition(self, ctx:LispParserParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by LispParserParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:LispParserParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by LispParserParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:LispParserParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by LispParserParser#parameterList.
    def enterParameterList(self, ctx:LispParserParser.ParameterListContext):
        pass

    # Exit a parse tree produced by LispParserParser#parameterList.
    def exitParameterList(self, ctx:LispParserParser.ParameterListContext):
        pass


    # Enter a parse tree produced by LispParserParser#conditional.
    def enterConditional(self, ctx:LispParserParser.ConditionalContext):
        pass

    # Exit a parse tree produced by LispParserParser#conditional.
    def exitConditional(self, ctx:LispParserParser.ConditionalContext):
        pass


    # Enter a parse tree produced by LispParserParser#letExpression.
    def enterLetExpression(self, ctx:LispParserParser.LetExpressionContext):
        pass

    # Exit a parse tree produced by LispParserParser#letExpression.
    def exitLetExpression(self, ctx:LispParserParser.LetExpressionContext):
        pass


    # Enter a parse tree produced by LispParserParser#quoteExpression.
    def enterQuoteExpression(self, ctx:LispParserParser.QuoteExpressionContext):
        pass

    # Exit a parse tree produced by LispParserParser#quoteExpression.
    def exitQuoteExpression(self, ctx:LispParserParser.QuoteExpressionContext):
        pass


    # Enter a parse tree produced by LispParserParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:LispParserParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by LispParserParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:LispParserParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by LispParserParser#printExpression.
    def enterPrintExpression(self, ctx:LispParserParser.PrintExpressionContext):
        pass

    # Exit a parse tree produced by LispParserParser#printExpression.
    def exitPrintExpression(self, ctx:LispParserParser.PrintExpressionContext):
        pass


    # Enter a parse tree produced by LispParserParser#binaryExpression.
    def enterBinaryExpression(self, ctx:LispParserParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by LispParserParser#binaryExpression.
    def exitBinaryExpression(self, ctx:LispParserParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by LispParserParser#binaryTail.
    def enterBinaryTail(self, ctx:LispParserParser.BinaryTailContext):
        pass

    # Exit a parse tree produced by LispParserParser#binaryTail.
    def exitBinaryTail(self, ctx:LispParserParser.BinaryTailContext):
        pass



del LispParserParser