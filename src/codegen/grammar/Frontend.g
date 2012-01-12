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

start : ( module | consts | types ) * ;

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

types : TYPES ID INDENT types_items DEDENT -> ^( TYPES ID types_items ) ;
types_items : types_item + ;
types_item : ID INDENT types_item_attrs DEDENT -> ^( ID types_item_attrs ) ;
types_item_attrs : types_item_attr + ;
types_item_attr : ID ;

num_whole : MINUS ? NUMBER ;
num_fract : MINUS ? NUMBER DIVIDE NUMBER ;

CONSTS : 'consts' ;
DEDENT : 'dedent' ;
INDENT : 'indent' ;
MODULE : 'module' ;
TYPES : 'types' ;
DIVIDE : '/' ;
MINUS : '-' ;
ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
WHITESPACE : ' ' + { self . skip ( ) } ;
EXPRESSION : '[' .* ']' ;
