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
    :   ^( ID num_whole )
            { $name , $value = $ID.text , $num_whole.value }
    |   ^( ID num_fract )
            { $name , $value = $ID.text , $num_fract.value }
    |   ^( ID EXPRESSION )
            { $name , $value = $ID.text , $EXPRESSION.text }
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

