tree grammar Backend ;

options
{
    language = Python ;
    tokenVocab = Frontend ;
    ASTLabelType = object ;
}

start
    returns [ value ]
    @init { $value = dict ( ) }
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
                $value [ 'consts' ] [ $consts.value ] = dict ( )
            }
        ) *
    ;

module
    returns [ value ]
    :   ^( 'module' ID ) { $value = $ID.text }
    ;

consts
    returns [ value ]
    :   ^( 'consts' ID ) { $value = $ID.text }
    ;
