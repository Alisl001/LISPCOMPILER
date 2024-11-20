lexer grammar LispLexer;

// Define tokens for Lisp language

// Strings (enclosed in double quotes)
STRING : '"' (ESC_SEQ | ~["\\])* '"' ; // Match strings with escape sequences and handle newlines
fragment ESC_SEQ : '\\' [btnr"'\\] ; // Defines valid escape characters: \b, \t, \n, \r, ", '

// Numbers (integers and floats)
NUMBER : [0-9]+('.'[0-9]+)?;

// Reserved keywords
DEFUN        : 'defun';
IF           : 'if';
COND         : 'cond';
LET          : 'let';
QUOTE        : 'quote';
PRINT        : 'print';
DEFPARAMETER : 'defparameter'; 

// Identifiers (allow *, -, _ in identifiers, but not as standalone tokens)
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_*-]*;

// Operators
PLUS  : '+';
MINUS : '-';
MULT  : '*' -> more; // Handle * in IDENTIFIER if part of it
DIV   : '/';
MOD   : '%';

// Parentheses for Lisp expressions
LPAREN : '(';
RPAREN : ')';

// Boolean values
TRUE  : 'true';
FALSE : 'false';

// Comments (start with a semicolon and continue to the end of the line)
COMMENT : ';' .*? '\n' -> skip;

// Whitespace (spaces, tabs, newlines)
WS : [ \t\r\n]+ -> skip;

// Catch all for unrecognized characters
ERROR : . ;
