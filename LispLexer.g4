lexer grammar LispLexer;

// Define tokens for Lisp language

// Numbers (integers and floats)
NUMBER : [0-9]+('.'[0-9]+)?;

// Reserved keywords
DEFUN : 'defun';
IF    : 'if';
COND  : 'cond';
LET   : 'let';
QUOTE : 'quote';
PRINT : 'print';

// Identifiers
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_-]*;

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
STRING : '"' (ESC_SEQ | ~["\\\r\n])* '"' ; // Match strings with escape sequences
fragment ESC_SEQ : '\\' [btnr"'\\] ; // Defines valid escape characters: \b, \t, \n, \r, ", '

// Boolean values
TRUE  : 'true';
FALSE : 'false';

// Comments (start with a semicolon and continue to the end of the line)
// COMMENT : ';' .*? '\n' -> skip;
COMMENT : ';' .*? '\n' ;

// Whitespace (spaces, tabs, newlines)
WS : [ \t\r\n]+ -> skip;

// Catch all for unrecognized characters
ERROR : . ;
