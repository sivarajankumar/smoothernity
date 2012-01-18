lexer grammar ShyLexer ;

options 
{
    language = Python ;
}

@ header
{
    class ShyLexerException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ members
{
    def emitErrorMessage ( self , msg ) :
        raise ShyLexerException ( msg )
}

CONSTS : 'consts' ;
COPY : 'copy' ;
DEDENT : 'dedent' ;
INDENT : 'indent' ;
MODULE : 'module' ;
PASTE : 'paste' ;
REPLACE : 'replace' ;
TYPES : 'types' ;
WITH : 'with' ;

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

TREE_ARBITRARY_TOKEN : 'TREE_ARBITRARY_TOKEN' ;
TREE_CONSTS : 'TREE_CONSTS' ;
TREE_COPY : 'TREE_COPY' ;
TREE_COPY_PASTE : 'TREE_COPY_PASTE' ;
TREE_EXPRESSION : 'TREE_EXPRESSION' ;
TREE_HINT : 'TREE_HINT' ;
TREE_HINT_NONE : 'TREE_HINT_NONE' ;
TREE_MODULE : 'TREE_MODULE' ;
TREE_NUM_FRACT : 'TREE_NUM_FRACT' ;
TREE_NUM_WHOLE : 'TREE_NUM_WHOLE' ;
TREE_PASTE : 'TREE_PASTE' ;
TREE_PASTE_REPLACE : 'TREE_PASTE_REPLACE' ;
TREE_PASTE_WITH : 'TREE_PASTE_WITH' ;
TREE_TYPES : 'TREE_TYPES' ;
TREE_TYPES_ITEM : 'TREE_TYPES_ITEM' ;
TREE_TYPES_ITEM_ATTR : 'TREE_TYPES_ITEM_ATTR' ;
TREE_TYPES_ITEM_HINT : 'TREE_TYPES_ITEM_HINT' ;
TREE_TYPES_ITEM_HINTS : 'TREE_TYPES_ITEM_HINTS' ;
