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
    |   COPY NEWLINE INDENT NEWLINE block + DEDENT NEWLINE
        ( PASTE REPLACE paste_replace WITH paste_with ) +
        ->
            ^( TREE_COPY block + 
                ^( TREE_PASTE
                    ^( TREE_PASTE_REPLACE paste_replace )
                    ^( TREE_PASTE_WITH paste_with )
                ) +
            )
    ;

paste_replace : ID ;
paste_with : arbitrary_token + NEWLINE -> arbitrary_token + ;

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
