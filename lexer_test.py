from antlr4 import *
from LispLexer import LispLexer
from LispParser import LispParser

def main():
    # Load the Lisp code from a file
    with open('testLisp.lisp', 'r', encoding='utf-8') as file:
        input_stream = InputStream(file.read())
    
    # Initialize lexer and token stream
    lexer = LispLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Initialize parser
    parser = LispParser(token_stream)
    
    # Parse the program (root rule)
    tree = parser.program()
    
    # Print the parse tree (you can replace this with more sophisticated processing)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
