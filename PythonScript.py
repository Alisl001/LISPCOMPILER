# PythonScript.py
from antlr4 import *
from antlr4.tree.Trees import Trees
from LispLexer import LispLexer
from LispParser import LispParser
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
from Interpreter import Interpreter


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax Error: line {line}:{column} {msg}")

def print_ast(ast, level=0):
    """Recursively print the AST."""
    print("  " * level + str(ast.node_type))
    for child in ast.children:
        print_ast(child, level + 1)

def main():
    # Load the Lisp code from a file
    with open('testLisp.lisp', 'r', encoding='utf-8') as file:
        input_stream = InputStream(file.read())
    
    # Initialize lexer and parser
    lexer = LispLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LispParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())
    
    # Parse the program and construct the AST
    ast = parser.program().node
    
    # Print the AST
    print("\nAbstract Syntax Tree:")
    print_ast(ast)

    # After parsing
    interpreter = Interpreter()
    result = interpreter.evaluate(ast)
    print("\nExecution Result:")
    print(result)

if __name__ == '__main__':
    main()
