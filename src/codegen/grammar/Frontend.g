grammar Frontend ;

options 
{
    language = Python ;
    output = AST ;
    ASTLabelType = object ;
}

@parser::header
{
    class FrontendParserException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@lexer::header
{
    class FrontendLexerException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@parser::members
{
    def emitErrorMessage ( self , msg ) :
        raise FrontendParserException ( msg )
}

@lexer::members
{
    def emitErrorMessage ( self , msg ) :
        raise FrontendLexerException ( msg )
}

start : ( module | consts ) * ;
module : 'module' ID NEWLINE -> ^( 'module' ID ) ;
consts : 'consts' ID NEWLINE -> ^( 'consts' ID )
       | 'consts' ID NEWLINE consts_values -> ^( 'consts' ID consts_values )
       ;
consts_values : consts_value + ;
consts_value : ID NUMBER NEWLINE -> ^( ID NUMBER ) ;
ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
NEWLINE : '\r' ? '\n' ;
WHITESPACE : ' ' + { self . skip ( ) } ;
