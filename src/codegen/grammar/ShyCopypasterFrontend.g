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
    :   pure_block
    |   COPY copy_body paste + -> ^( TREE_COPY copy_body paste + ) 
    ;

pure_block
    :   arbitrary_token + NEWLINE
    |   INDENT NEWLINE pure_block + DEDENT NEWLINE
    ;

copy_body
    :   NEWLINE INDENT NEWLINE pure_block + DEDENT NEWLINE -> pure_block +
    ;

paste
    :   PASTE REPLACE paste_replace WITH paste_with
        -> ^( TREE_PASTE paste_replace paste_with )
    ;

paste_replace
    :   ID -> ^( TREE_PASTE_REPLACE ID )
    ;

paste_with
    :   arbitrary_token + NEWLINE -> ^( TREE_PASTE_WITH arbitrary_token + )
    ;

arbitrary_token
    :   CONSTS
    |   MODULE
    |   TYPES

    |   CURLY_OPEN
    |   CURLY_CLOSE
    |   DIVIDE
    |   MINUS
    |   UNDERSCORE
    |   ID
    |   NUMBER
    |   EXPRESSION
    ;
