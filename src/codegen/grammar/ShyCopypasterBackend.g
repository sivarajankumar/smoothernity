tree grammar ShyCopypasterBackend ;

options
{
    language = Python ;
    tokenVocab = ShyLexer ;
    ASTLabelType = object ;
}

start
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( INDENT { $value . append ( $INDENT.text ) }
        | DEDENT { $value . append ( $DEDENT.text ) }
        | NEWLINE { $value . append ( $NEWLINE.text ) }
        | ID { $value . append ( $ID.text ) }
        ) +
    ;

