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
    : ( block { $value += $block.value } ) *
    ;

block
    returns [ value ]
    @ init { $value = list ( ) }
    : ( arbitrary_token { $value . append ( $arbitrary_token.value ) } ) +
      NEWLINE { $value += [ $NEWLINE.text ] }
    | INDENT a = NEWLINE { $value += [ $INDENT.text , $a.text ] }
      ( b = block { $value += $b.value } ) + 
      DEDENT c = NEWLINE { $value += [ $DEDENT.text , $c.text ] }
    | COPY block + PASTE REPLACE ID WITH block
    ;

arbitrary_token
    returns [ value ]
    : CONSTS { $value = $CONSTS.text }
    | MODULE { $value = $MODULE.text }
    | TYPES { $value = $TYPES.text }

    | CURLY_OPEN { $value = $CURLY_OPEN.text }
    | CURLY_CLOSE { $value = $CURLY_CLOSE.text }
    | DIVIDE { $value = $DIVIDE.text }
    | MINUS { $value = $MINUS.text }
    | UNDERSCORE { $value = $UNDERSCORE.text }
    | ID { $value = $ID.text }
    | NUMBER { $value = $NUMBER.text }
    | EXPRESSION { $value = $EXPRESSION.text }
    ;
