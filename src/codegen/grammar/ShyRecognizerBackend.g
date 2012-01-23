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

    def update_start_dict ( res , part , name , value ) :
        if part not in res :
            res [ part ] = dict ( )
        if name not in res [ part ] :
            res [ part ] [ name ] = dict ( )
        res [ part ] [ name ] . update ( value )
}

start
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( module 
            {
                update_start_dict ( $value , 'module' ,
                    $module.value , dict ( ) )
            }
        | stateless 
            {
                update_start_dict ( $value , 'stateless' ,
                    $stateless.title , $stateless.content )
            }
        | consts
            {
                update_start_dict ( $value , 'consts' ,
                    $consts.title , $consts.content )
            }
        | types
            {
                update_start_dict ( $value , 'types' ,
                    $types.title , $types.content )
            }
        ) *
    ;

module
    returns [ value ]
    :   ^( TREE_MODULE ID ) { $value = $ID.text }
    ;

stateless
    returns [ title , content ]
    :   ^( TREE_STATELESS ID )
            { $title , $content = $ID.text , dict ( ) }
    |   ^( TREE_STATELESS ID procs )
            { $title , $content = $ID.text , $procs.value }
    ;

procs
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( proc { $value [ $proc.title ] = $proc.content } ) +
    ;

proc
    returns [ title , content ]
    :   ^( TREE_PROC ID )
            { $title , $content = $ID.text , dict ( ) }
    |   ^( TREE_PROC ID proc_args )
            { $title , $content = $ID.text , { 'args' : $proc_args.value } }
    ;

proc_args
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ^( TREE_PROC_ARGS ( ID { $value [ $ID.text ] = dict ( ) } ) + )
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

