from antlr4 import *
from LispLexer import LispLexer
from antlr4.error.Errors import RecognitionException

def main():
    # Load the Lisp code from a file
    with open('testLisp.lisp', 'r', encoding='utf-8') as file:
        input_stream = InputStream(file.read())

    # Initialize the lexer
    lexer = LispLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Process each token
    lexer.reset()
    while True:
        token = lexer.nextToken()
        
        if token.type == Token.EOF:
            break
        
        # Get token line, column, and type info
        line = token.line
        column = token.column
        token_type = lexer.symbolicNames[token.type]
        token_value = token.text
        
        # Handle lexical errors
        if token_type == "ERROR":
            print(f"Lexical Error: Unrecognized input at line {line}, column {column}: {token_value}")
        else:
            print(f"Token Index: Line: {line}, Column: {column}, Type: {token_type}, Value: {token_value}")

if __name__ == '__main__':
    main()
