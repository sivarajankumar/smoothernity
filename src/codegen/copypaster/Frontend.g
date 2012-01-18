grammar Frontend ;

options 
{
    language = Python ;
    output = AST ;
    ASTLabelType = object ;
}

start : ( INDENT | DEDENT | NEWLINE | CHARS ) * ;

DEDENT : 'dedent' ;
INDENT : 'indent' ;
NEWLINE : '\n' ;
WHITESPACE : ' ' + { self . skip ( ) } ;
CHARS : ( 'a' .. 'z' | '0' .. '9' ) * ;
