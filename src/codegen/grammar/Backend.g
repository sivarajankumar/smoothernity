tree grammar Backend ;

options
{
    language = Python ;
    tokenVocab = Frontend ;
    ASTLabelType = object ;
}

@header
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
    :   ^( MODULE ID ) { $value = $ID.text }
    ;

consts
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( CONSTS ID consts_items )
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
    :   ^( TYPES ID types_items )
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
    :   ^( ID types_item_attrs )
            { $name , $value = $ID.text , $types_item_attrs.value }
    ;

types_item_attrs
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( types_item_attr
            { $value [ $types_item_attr.name ] = $types_item_attr.value }
        ) +
    ;

types_item_attr
    returns [ name , value ]
    :   ID { $name , $value = $ID.text , dict ( ) }
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

