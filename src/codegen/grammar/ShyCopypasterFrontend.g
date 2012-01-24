parser grammar ShyCopypasterFrontend ;

options 
{
    language = Python ;
    tokenVocab = ShyLexer ;
    output = AST ;
    ASTLabelType = object ;
}

@ header
{
    class ShyCopypasterFrontendException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ members
{
    def emitErrorMessage ( self , msg ) :
        raise ShyCopypasterFrontendException ( msg )
}

start : block * ;

block
    :   arbitrary_token + NEWLINE
    |   INDENT NEWLINE block + DEDENT NEWLINE
    |   COPY copy_body copy_paste + -> ^( TREE_COPY copy_body copy_paste + ) 
    ;

pure_block
    :   arbitrary_token + NEWLINE
    |   INDENT NEWLINE pure_block + DEDENT NEWLINE
    ;

copy_body
    :   NEWLINE INDENT NEWLINE pure_block + DEDENT NEWLINE -> pure_block +
    |   arbitrary_token + NEWLINE
    ;

copy_paste
    :   PASTE paste
        -> ^( TREE_COPY_PASTE paste )
    |   PASTE NEWLINE INDENT NEWLINE paste + DEDENT NEWLINE
        -> ^( TREE_COPY_PASTE paste + )
    ;

paste
    :   REPLACE paste_replace WITH paste_with
        -> ^( TREE_PASTE paste_replace paste_with )
    ;

paste_replace
    :   ID -> ^( TREE_PASTE_REPLACE ID )
    ;

paste_with
    :   arbitrary_token + NEWLINE 
        -> ^( TREE_PASTE_WITH arbitrary_token + )
    |   NEWLINE INDENT NEWLINE pure_block + DEDENT NEWLINE
        -> ^( TREE_PASTE_WITH pure_block + )
    ;

arbitrary_token
    :   ARGS
    |   CONSTS
    |   IF
    |   MODULE
    |   OPS
    |   PROC
    |   STATELESS
    |   TYPES
    |   VARS
    |   WITH

    |   ARROW_LEFT
    |   ARROW_RIGHT
    |   CURLY_OPEN
    |   CURLY_CLOSE
    |   DIVIDE
    |   MINUS
    |   UNDERSCORE
    |   ID
    |   NUMBER
    |   EXPRESSION
    |   STRING
    ;
