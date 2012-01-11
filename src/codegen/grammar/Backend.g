tree grammar Backend ;

options
{
    language = Python ;
    tokenVocab = Frontend ;
    ASTLabelType = object ;
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
    :   ^( CONSTS ID )
            { $title , $content = $ID.text , dict ( ) }
    |   ^( CONSTS ID consts_values )
            { $title , $content = $ID.text , $consts_values.value }
    ;

consts_values
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( consts_value { $value [ $consts_value.name ] = $consts_value.value } ) +
    ;

consts_value
    returns [ name , value ]
    :   ^( ID NUMBER ) { $name , $value = $ID.text , int ( $NUMBER.text ) }
    ;
