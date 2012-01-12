grammar Frontend ;

options 
{
    language = Python ;
    output = AST ;
    ASTLabelType = object ;
}

@ parser :: header
{
    class FrontendParserException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ lexer :: header
{
    class FrontendLexerException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ parser :: members
{
    def emitErrorMessage ( self , msg ) :
        raise FrontendParserException ( msg )
}

@ lexer :: members
{
    def emitErrorMessage ( self , msg ) :
        raise FrontendLexerException ( msg )
}

start : ( module | consts ) * ;

module : MODULE ID -> ^( MODULE ID ) ;

consts
    : CONSTS ID INDENT consts_items DEDENT -> ^( CONSTS ID consts_items )
    ;
consts_items : consts_item + ;
consts_item
    : ID num_whole -> ^( ID num_whole )
    | ID num_fract -> ^( ID num_fract )
    | ID EXPRESSION -> ^( ID EXPRESSION )
    ;

num_whole : MINUS ? NUMBER ;
num_fract : MINUS ? NUMBER DIVIDE NUMBER ;

CONSTS : 'consts' ;
MODULE : 'module' ;
INDENT : 'indent' ;
DEDENT : 'dedent' ;
DIVIDE : '/' ;
MINUS : '-' ;
ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
WHITESPACE : ' ' + { self . skip ( ) } ;
EXPRESSION : '[' .* ']' ;
