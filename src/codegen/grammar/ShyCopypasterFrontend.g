parser grammar ShyCopypasterFrontend ;

options 
{
    language = Python ;
    tokenVocab = ShyLexer ;
    output = AST ;
    ASTLabelType = object ;
}

start : chunk * ;

chunk
    : arbitrary_token -> ^( TREE_ARBITRARY_TOKEN arbitrary_token )
    //| copy_paste
    ;
/*
copy_paste
    : COPY NEWLINE INDENT NEWLINE copy DEDENT NEWLINE paste + 
        -> ^( TREE_COPY_PASTE copy paste + )
    ;

copy
    : arbitrary_tokens -> ^( TREE_COPY arbitrary_tokens )
    ;

paste
    : REPLACE paste_replace WITH paste_with NEWLINE
        -> ^( TREE_PASTE paste_replace paste_with )
    ;

paste_replace
    : ID -> ^( TREE_PASTE_REPLACE ID )
    ;

paste_with
    : arbitrary_tokens -> ^( TREE_PASTE_WITH arbitrary_tokens )
    ;
*/
arbitrary_tokens : arbitrary_token + ;

arbitrary_token
    : CONSTS
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
    ;
