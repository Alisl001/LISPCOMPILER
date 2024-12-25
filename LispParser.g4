// LispParser.g4
parser grammar LispParser;

options {
  tokenVocab = LispLexer;
}

@parser::members {
  from ASTNodes import *

  def build_program(self, expressions):
      program = ProgramNode()
      for expr in expressions:
          program.add_child(expr)
      return program
}

program returns [ASTNode node]
    : exprs+=expression* EOF { $node = self.build_program($exprs); }
    ;

expression returns [ASTNode node]
    : STRING       { $node = LiteralNode($STRING.text); }
    | NUMBER       { $node = LiteralNode($NUMBER.text); }
    | IDENTIFIER   { $node = IdentifierNode($IDENTIFIER.text); }
    | lambda       { $node = $lambda.node; }
    | funcall      { $node = $funcall.node; }
    | conditional  { $node = $conditional.node; }
    | operation    { $node = $operation.node; }
    | formatCall   { $node = $formatCall.node; }
    ;

funcall returns [ASTNode node]
    : LPAREN IDENTIFIER exprs+=expression* RPAREN {
        func = FunctionCallNode($IDENTIFIER.text)
        for expr in $exprs:
            func.add_child(expr)
        $node = func;
    }
    ;

operation returns [ASTNode node]
    : LPAREN op=(PLUS | MINUS | MULT | DIV | MOD | GREATER_EQUAL | LESS_EQUAL | GREATER | LESS | EQUAL | AND | OR) exprs+=expression+ RPAREN {
        operation = OperationNode($op.text)
        for expr in $exprs:
            operation.add_child(expr)
        $node = operation;
    }
    ;

lambda returns [ASTNode node]
    : LPAREN LAMBDA LPAREN params RPAREN expression RPAREN {
        lambda_node = LambdaNode()
        if $params.node:
            lambda_node.add_child($params.node)
        lambda_node.add_child($expression.node)
        $node = lambda_node;
    }
    ;

conditional returns [ASTNode node]
    : LPAREN IF test=expression then=expression else_=expression? RPAREN {
        conditional_node = ConditionalNode("if")
        conditional_node.add_child($test.node)
        conditional_node.add_child($then.node)
        if ($else_.node != null) {
            conditional_node.add_child($else_.node);
        }
        $node = conditional_node;
    }
    | LPAREN COND clauses+=condClause+ RPAREN {
        cond_node = ConditionalNode("cond")
        for clause in $clauses:
            cond_node.add_child(clause.node)
        $node = cond_node;
    }
    ;

condClause returns [ASTNode node]
    : LPAREN test=expression result=expression RPAREN {
        clause_node = CondClauseNode()
        clause_node.add_child($test.node)
        clause_node.add_child($result.node)
        $node = clause_node;
    }
    ;


formatCall returns [ASTNode node]
    : LPAREN FORMAT format_string=expression args+=expression* RPAREN {
        format_node = FormatCallNode()
        format_node.add_child($format_string.node)
        for arg in $args:
            format_node.add_child(arg.node)  // Ensure access to `node`
        $node = format_node;
    }
    ;

params returns [ASTNode node]
    : ids+=IDENTIFIER* {
        params_node = ParameterListNode()
        for id in $ids:
            params_node.add_child(IdentifierNode(id.text))
        $node = params_node;
    }
    ;
