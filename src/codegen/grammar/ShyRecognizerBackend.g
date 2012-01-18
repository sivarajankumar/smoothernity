tree grammar ShyRecognizerBackend ;

options
{
    language = Python ;
    tokenVocab = ShyLexer ;
    ASTLabelType = object ;
}

@ header
{
    from fractions import Fraction
}

start
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( module 
            {
                if 'module' not in $value :
                    $value [ 'module' ] = dict ( )
                $value [ 'module' ] [ $module.value ] = dict ( )
            }
        | consts
            {
                if 'consts' not in $value :
                    $value [ 'consts' ] = dict ( )
                $value [ 'consts' ] [ $consts.title ] = $consts.content
            }
        | types
            {
                if 'types' not in $value :
                    $value [ 'types' ] = dict ( )
                $value [ 'types' ] [ $types.title ] = $types.content
            }
        ) *
    ;

module
    returns [ value ]
    :   ^( TREE_MODULE ID ) { $value = $ID.text }
    ;

consts
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_CONSTS ID consts_items )
            { $title , $content = $ID.text , $consts_items.value }
    ;

consts_items
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( consts_item
            { $value [ $consts_item.name ] = $consts_item.value }
        ) +
    ;

consts_item
    returns [ name , value ]
    :   ^( TREE_NUM_WHOLE ID num_whole )
            { $name , $value = $ID.text , $num_whole.value }
    |   ^( TREE_NUM_FRACT ID num_fract )
            { $name , $value = $ID.text , $num_fract.value }
    |   ^( TREE_EXPRESSION ID EXPRESSION )
            { $name , $value = $ID.text , $EXPRESSION.text }
    ;

types
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_TYPES ID types_items )
            { $title , $content = $ID.text , $types_items.value }
    ;

types_items
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( types_item
            { $value [ $types_item.name ] = $types_item.value }
        ) +
    ;

types_item
    returns [ name , value ]
    :   ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints )
            { $name , $value = $ID.text , $types_item_hints.value }
    |   ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS )
            { $name , $value = $ID.text , dict ( ) }
    ;

types_item_hints
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( types_item_hint { $value . update ( $types_item_hint.value ) } ) +
    ;

types_item_hint
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr
            { $value [ $types_item_attr.value ] = dict ( ) }
        ) + )
    |   ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr
            { $value [ $types_item_attr.value ] = $hint.value }
        ) + )
    ;

types_item_attr
    returns [ value ]
    :   ^( TREE_TYPES_ITEM_ATTR ID ) { $value = $ID.text }
    ;

hint
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ^( TREE_HINT ID )
            { $value [ $ID.text ] = list ( ) }
    |   ^( TREE_HINT ID hint_args )
            { $value [ $ID.text ] = $hint_args.value }
    ;

hint_args
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( hint_arg { $value . append ( $hint_arg.value ) } ) +
    ;

hint_arg
    returns [ value ]
    :   ID { $value = $ID.text }
    |   UNDERSCORE { $value = $UNDERSCORE.text }
    ;

num_whole
    returns [ value ]
    :   ( MINUS NUMBER )
            { $value = int ( $MINUS.text + $NUMBER.text ) }
    |   ( NUMBER )
            { $value = int ( $NUMBER.text ) }
    ;

num_fract
    returns [ value ]
    :   ( MINUS n = NUMBER DIVIDE d = NUMBER )
            {
                $value = Fraction ( int ( $MINUS.text + $n.text ) ,
                    int ( $d.text ) )
            }
    |   ( n = NUMBER DIVIDE d = NUMBER )
            { $value = Fraction ( int ( $n.text ) , int ( $d.text ) ) }
    ;

