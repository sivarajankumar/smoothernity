grammar RecognizerFrontend ;

options 
{
    language = Python ;
    output = AST ;
    ASTLabelType = object ;
}

@ parser :: header
{
    class RecognizerFrontendParserException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ lexer :: header
{
    class RecognizerFrontendLexerException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ parser :: members
{
    def emitErrorMessage ( self , msg ) :
        raise RecognizerFrontendParserException ( msg )
}

@ lexer :: members
{
    def emitErrorMessage ( self , msg ) :
        raise RecognizerFrontendLexerException ( msg )
}

start : ( module | consts | types ) * ;

module : MODULE ID NEWLINE -> ^( TREE_MODULE ID ) ;

consts
    : CONSTS ID NEWLINE
      INDENT NEWLINE consts_items DEDENT NEWLINE
      -> ^( TREE_CONSTS ID consts_items )
    ;
consts_items : consts_item + ;
consts_item
    : ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole )
    | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract )
    | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION )
    ;

types
    : TYPES ID NEWLINE
      INDENT NEWLINE types_items DEDENT NEWLINE
      -> ^( TREE_TYPES ID types_items )
    ;
types_items : types_item + ;
types_item
    : ID types_item_hint ? NEWLINE
      ( INDENT NEWLINE ( types_item_hint NEWLINE ) + DEDENT NEWLINE ) ?
      -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hint * )
    ;
types_item_hint 
    : types_item_attr + 
      -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE types_item_attr + )
    | hint types_item_attr +
      -> ^( TREE_TYPES_ITEM_HINT hint types_item_attr + )
    | hint NEWLINE INDENT NEWLINE 
        ( types_item_attr + NEWLINE ) + DEDENT
      -> ^( TREE_TYPES_ITEM_HINT hint types_item_attr + )
    ;
types_item_attr : ID -> ^( TREE_TYPES_ITEM_ATTR ID ) ;

hint
    : CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID )
    | CURLY_OPEN ID hint_arg + CURLY_CLOSE -> ^( TREE_HINT ID hint_arg + )
    ;
hint_arg : ID | UNDERSCORE ;

num_whole : MINUS ? NUMBER ;
num_fract : MINUS ? NUMBER DIVIDE NUMBER ;

CONSTS : 'consts' ;
DEDENT : 'dedent' ;
INDENT : 'indent' ;
MODULE : 'module' ;
TYPES : 'types' ;

CURLY_OPEN : '{' ;
CURLY_CLOSE : '}' ;
DIVIDE : '/' ;
MINUS : '-' ;
UNDERSCORE : '_' ;
NEWLINE : '\n' ;
ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
WHITESPACE : ' ' + { self . skip ( ) } ;
EXPRESSION : '[' . * ']' ;

TREE_CONSTS : 'TREE_CONSTS' ;
TREE_EXPRESSION : 'TREE_EXPRESSION' ;
TREE_HINT : 'TREE_HINT' ;
TREE_HINT_NONE : 'TREE_HINT_NONE' ;
TREE_MODULE : 'TREE_MODULE' ;
TREE_NUM_FRACT : 'TREE_NUM_FRACT' ;
TREE_NUM_WHOLE : 'TREE_NUM_WHOLE' ;
TREE_TYPES : 'TREE_TYPES' ;
TREE_TYPES_ITEM : 'TREE_TYPES_ITEM' ;
TREE_TYPES_ITEM_ATTR : 'TREE_TYPES_ITEM_ATTR' ;
TREE_TYPES_ITEM_HINT : 'TREE_TYPES_ITEM_HINT' ;
TREE_TYPES_ITEM_HINTS : 'TREE_TYPES_ITEM_HINTS' ;
