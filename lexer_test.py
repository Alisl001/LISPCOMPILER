from antlr4 import *
from antlr4.tree.Trees import Trees
from LispLexer import LispLexer
from LispParser import LispParser
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax Error: line {line}:{column} {msg}")


def pretty_print_tree(tree, parser, level=0):
    if tree.getChildCount() == 0:
        print("  " * level + str(tree))
    else:
        print("  " * level + parser.ruleNames[tree.getRuleIndex()])
        for i in range(tree.getChildCount()):
            pretty_print_tree(tree.getChild(i), parser, level + 1)


def main():
    # Load the Lisp code from a file
    with open('testLisp.lisp', 'r', encoding='utf-8') as file:
        input_stream = InputStream(file.read())
    
    # Initialize lexer and token stream
    lexer = LispLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Initialize parser
    parser = LispParser(token_stream)
    parser.removeErrorListeners()  # Remove default error listeners
    parser.addErrorListener(MyErrorListener())  # Add custom error listener
    
    # Parse the program
    tree = parser.program()
    
    # Pretty print the parse tree
    print("\nParse Tree:")
    pretty_print_tree(tree, parser)


if __name__ == '__main__':
    main()
