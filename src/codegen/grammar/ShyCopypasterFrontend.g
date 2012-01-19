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
    : arbitrary_token + NEWLINE
    | INDENT NEWLINE block + DEDENT NEWLINE
    | COPY NEWLINE INDENT NEWLINE block + DEDENT NEWLINE
      PASTE REPLACE ID WITH block
      -> COPY block + PASTE REPLACE ID WITH block
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
