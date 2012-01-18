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
    : ( CONSTS { $value . append ( $CONSTS.text ) }
      | DEDENT { $value . append ( $DEDENT.text ) }
      | INDENT { $value . append ( $INDENT.text ) }
      | MODULE { $value . append ( $MODULE.text ) }
      | TYPES { $value . append ( $TYPES.text ) }

      | CURLY_OPEN { $value . append ( $CURLY_OPEN.text ) }
      | CURLY_CLOSE { $value . append ( $CURLY_CLOSE.text ) }
      | DIVIDE { $value . append ( $DIVIDE.text ) }
      | MINUS { $value . append ( $MINUS.text ) }
      | UNDERSCORE { $value . append ( $UNDERSCORE.text ) }
      | NEWLINE { $value . append ( $NEWLINE.text ) }
      | ID { $value . append ( $ID.text ) }
      | NUMBER { $value . append ( $NUMBER.text ) }
      | EXPRESSION { $value . append ( $EXPRESSION.text ) }
      ) *
    ;
