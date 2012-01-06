grammar Frontend ;

options 
{
    language = Python ;
    output = AST ;
    ASTLabelType = object ;
}

@parser::members
{
    def emitErrorMessage ( msg ) :
        raise Exception ( msg )
}

@lexer::members
{
    def emitErrorMessage ( msg ) :
        raise Exception ( msg )
}

start : module * ;
module : 'module' ID NEWLINE -> ^( 'module' ID ) ;
ID : ( 'a' .. 'z' | '0' .. '9' ) + ;
NEWLINE : '\r' ? '\n' ;
WHITESPACE : ' ' + { self . skip ( ) } ;
