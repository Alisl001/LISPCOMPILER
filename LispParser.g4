grammar LispParser;

// Parser rules

program
    : expression* EOF
    ;

expression
    : functionCall
    | variableDefinition
    | functionDefinition
    | conditional
    | letExpression
    | quoteExpression
    | lambdaExpression
    | printExpression
    | atom
    | binaryExpression
    | '(' expression ')'
    ;

atom
    : NUMBER
    | STRING
    | TRUE
    | FALSE
    | IDENTIFIER
    ;

functionCall
    : IDENTIFIER LPAREN argumentList? RPAREN
    | FORMAT LPAREN formatArguments RPAREN
    ;

formatArguments
    : expression (',' expression)*
    ;

argumentList
    : expression (',' expression)*
    ;

variableDefinition
    : DEFparameter IDENTIFIER expression
    ;

functionDefinition
    : DEFUN IDENTIFIER parameterList expression
    ;

parameterList
    : IDENTIFIER (',' IDENTIFIER)*
    ;

conditional
    : IF expression expression expression
    ;

letExpression
    : LET LPAREN (variableDefinition)* RPAREN expression
    ;

quoteExpression
    : QUOTE expression
    ;

lambdaExpression
    : LAMBDA LPAREN parameterList? RPAREN expression
    ;

printExpression
    : PRINT LPAREN expression RPAREN
    ;

binaryExpression
    : atom binaryTail
    ;

binaryTail
    : ( (MULT | DIV) atom
      | (PLUS | MINUS) atom
      | (GREATER_EQUAL | LESS_EQUAL | GREATER | LESS | EQUAL) atom
    ) binaryTail?
    ;

// Lexer rules

DEFUN        : 'defun';
DEFparameter : 'defparameter';
IF           : 'if';
CONDITION    : 'cond';
LET          : 'let';
QUOTE        : 'quote';
PRINT        : 'print';
LAMBDA       : 'lambda';
FORMAT       : 'format';

NUMBER : [0-9]+('.'[0-9]+)?;

STRING : '"' (ESC_SEQ | ~["\\])* '"';
fragment ESC_SEQ : '\\' [btnr"'\\];

IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_*-]*;

PLUS  : '+';
MINUS : '-';
MULT  : '*';
DIV   : '/';
MOD   : '%';
GREATER_EQUAL: '>='; 
LESS_EQUAL: '<='; 
GREATER: '>'; 
LESS: '<'; 
EQUAL: '=';

LPAREN : '(';
RPAREN : ')';

TRUE  : 'true';
FALSE : 'false';

COMMENT : ';;' ~[\n]* -> skip;

WS : [ \t\r\n]+ -> skip;

ERROR : . { System.err.println("Invalid character: " + _input.getText(_start, _input.index())); } ;
