grammar Frontend ;

options 
{
    language = Python ;
    output = AST ;
    ASTLabelType = object ;
}

start : module * ;
module : 'module' ID NEWLINE -> ^( 'module' ID ) ;
ID : ( 'a' .. 'z' | '0' .. '9' ) + ;
NEWLINE : '\r' ? '\n' ;
WHITESPACE : ' ' + { self . skip ( ) } ;
