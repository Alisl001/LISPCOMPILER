lexer grammar LispLexer;

// Define tokens for Lisp language

// Identifiers
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_-]*;

// Numbers (integers and floats)
NUMBER : [0-9]+('.'[0-9]+)?;

// Operators
PLUS  : '+';
MINUS : '-';
MULT  : '*';
DIV   : '/';
MOD   : '%';

// Parentheses for Lisp expressions
LPAREN : '(';
RPAREN : ')';

// Strings (enclosed in double quotes)
STRING : '"' (~["\r\n])* '"';

// Boolean values
TRUE  : 'true';
FALSE : 'false';

// Reserved keywords
DEFUN : 'defun';
IF    : 'if';
COND  : 'cond';
LET   : 'let';
QUOTE : 'quote';

// Comments (start with a semicolon and continue to the end of the line)
COMMENT : ';' .*? '\n' -> skip;

// Whitespace (spaces, tabs, newlines)
WS : [ \t\r\n]+ -> skip;
