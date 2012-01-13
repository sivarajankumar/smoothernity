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

module : MODULE ID NEWLINE -> ^( MODULE ID ) ;

consts
    : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( CONSTS ID consts_items )
    ;
consts_items : consts_item + ;
consts_item
    : ID num_whole NEWLINE -> ^( ID num_whole )
    | ID num_fract NEWLINE -> ^( ID num_fract )
    | ID EXPRESSION NEWLINE -> ^( ID EXPRESSION )
    ;

types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TYPES ID types_items ) ;
types_items : types_item + ;
types_item
    : ID types_item_attrs_oneline NEWLINE
      -> ^( ID types_item_attrs_oneline )
    | ID NEWLINE INDENT NEWLINE types_item_attrs_multiline DEDENT NEWLINE
      -> ^( ID types_item_attrs_multiline )
    ;
types_item_attrs_oneline : types_item_attr_oneline + ;
types_item_attr_oneline : ID -> ID ;
types_item_attrs_multiline : types_item_attr_multiline + ;
types_item_attr_multiline : ID NEWLINE -> ID ;

num_whole : MINUS ? NUMBER ;
num_fract : MINUS ? NUMBER DIVIDE NUMBER ;

CONSTS : 'consts' ;
DEDENT : 'dedent' ;
INDENT : 'indent' ;
MODULE : 'module' ;
TYPES : 'types' ;
DIVIDE : '/' ;
MINUS : '-' ;
NEWLINE : '\n' ;
ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
WHITESPACE : ' ' + { self . skip ( ) } ;
EXPRESSION : '[' .* ']' ;
