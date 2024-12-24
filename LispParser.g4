parser grammar LispParser;

options {
  tokenVocab = LispLexer;
}

// The root rule for a Lisp program
program: (expression | defparameter | defun)* EOF;

// Define a parameter declaration
defparameter: LPAREN DEFPARAMETER IDENTIFIER expression RPAREN;

// Define a function declaration
defun: LPAREN DEFUN IDENTIFIER LPAREN params? RPAREN STRING body RPAREN;

// Define function parameters
params: IDENTIFIER (IDENTIFIER)*;

// Define a function body (multiple expressions)
body: (expression)*;

// Expressions in Lisp
expression
    : STRING
    | NUMBER
    | IDENTIFIER
    | lambda
    | funcall
    | conditional
    | operation
    ;

// Lambda expressions
lambda: LPAREN LAMBDA LPAREN params? RPAREN expression RPAREN;

// Function calls (generic)
funcall: LPAREN IDENTIFIER (expression)* RPAREN;

// Conditional expressions (if and cond)
conditional
    : LPAREN IF expression expression expression? RPAREN
    | LPAREN COND (LPAREN expression expression RPAREN)+ RPAREN
    ;

// Arithmetic and logical operations
operation
    : LPAREN (PLUS | MINUS | MULT | DIV | MOD | GREATER_EQUAL | LESS_EQUAL | GREATER | LESS | EQUAL) (expression)+ RPAREN
    ;
