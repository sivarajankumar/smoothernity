tree grammar Backend ;

options
{
    language = Python ;
    tokenVocab = Frontend ;
    ASTLabelType = object ;
}

start
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( INDENT { $value . append ( $INDENT.text ) }
        | DEDENT { $value . append ( $DEDENT.text ) }
        | NEWLINE { $value . append ( $NEWLINE.text ) }
        | CHARS { $value . append ( $CHARS.text ) }
        ) +
    ;
