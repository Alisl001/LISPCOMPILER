from antlr4 import *
from LispLexer import LispLexer

def main():
    # Load the Lisp code from a file
    with open('example.lisp', 'r') as file:
        input_stream = InputStream(file.read())

    # Initialize the lexer
    lexer = LispLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Iterate through tokens
    lexer.reset()
    while True:
        token = lexer.nextToken()
        if token.type == Token.EOF:
            break
        print(f'Token Type: {lexer.symbolicNames[token.type]}, Token Text: {token.text}')

if __name__ == '__main__':
    main()
