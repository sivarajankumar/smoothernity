parser grammar ShyCopypasterFrontend ;

options 
{
    language = Python ;
    tokenVocab = ShyLexer ;
    output = AST ;
    ASTLabelType = object ;
}

start
    : ( CONSTS
      | DEDENT
      | INDENT
      | MODULE
      | TYPES

      | CURLY_OPEN
      | CURLY_CLOSE
      | DIVIDE
      | MINUS
      | UNDERSCORE
      | NEWLINE
      | ID
      | NUMBER
      | EXPRESSION
      ) *
    ;
