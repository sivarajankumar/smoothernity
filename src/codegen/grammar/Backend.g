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
                $value [ 'module' ] [ $module.value ] = { }
            }
        ) *
    ;

module
    returns [ value ]
    :   ^( 'module' ID ) { $value = $ID.text }
    ;

