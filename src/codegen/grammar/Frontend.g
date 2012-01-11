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
consts : CONSTS ID INDENT consts_values DEDENT -> ^( CONSTS ID consts_values )
       ;
consts_values : consts_value + ;
consts_value : ID NUMBER -> ^( ID NUMBER ) ;

CONSTS : 'consts' ;
MODULE : 'module' ;
INDENT : 'indent' ;
DEDENT : 'dedent' ;
ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
WHITESPACE : ' ' + { self . skip ( ) } ;
