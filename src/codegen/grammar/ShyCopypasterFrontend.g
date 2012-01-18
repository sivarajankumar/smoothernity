parser grammar ShyCopypasterFrontend ;

options 
{
    language = Python ;
    tokenVocab = ShyLexer ;
    output = AST ;
    ASTLabelType = object ;
}

start : block * ;

block
    : arbitrary_token + NEWLINE
    | INDENT NEWLINE block + DEDENT NEWLINE
    ;

arbitrary_token
    : CONSTS
    | MODULE
    | TYPES

    | CURLY_OPEN
    | CURLY_CLOSE
    | DIVIDE
    | MINUS
    | UNDERSCORE
    | ID
    | NUMBER
    | EXPRESSION
    ;
