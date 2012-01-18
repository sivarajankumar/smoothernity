parser grammar ShyRecognizerFrontend ;

options 
{
    language = Python ;
    tokenVocab = ShyLexer ;
    output = AST ;
    ASTLabelType = object ;
}

@ header
{
    class ShyRecognizerFrontendException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ members
{
    def emitErrorMessage ( self , msg ) :
        raise ShyRecognizerFrontendException ( msg )
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
