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
    :   ( block { $value += $block.value } ) *
    ;

block
    returns [ value ]
    :   pure_block { $value = $pure_block.value }
    |   copy { $value = $copy.value }
    ;

pure_block
    returns [ value ]
    @ init { $value = list ( ) }
    :   arbitrary_tokens
            { $value += $arbitrary_tokens.value }
        NEWLINE
            { $value += [ $NEWLINE.text ] }
    |   INDENT nl1 = NEWLINE
            { $value += [ $INDENT.text , $nl1.text ] }
        ( pb1 = pure_block
            { $value += $pb1.value }
        ) + 
        DEDENT nl2 = NEWLINE
            { $value += [ $DEDENT.text , $nl2.text ] }
    ;

copy
    returns [ value ]
    :   ^( TREE_COPY copy_body pastes )
        { $value = [ { 'copy' : $copy_body.value , 'paste' : $pastes.value } ] }
    ;

copy_body
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( pure_block { $value += $pure_block.value } ) +
    ;

pastes
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( paste { $value . append ( $paste.value ) } ) +
    ;

paste
    returns [ value ]
    :   ^( TREE_PASTE paste_replace paste_with )
        { $value = [ $paste_replace.value , $paste_with.value ] }
    ;

paste_replace
    returns [ value ]
    :   ^( TREE_PASTE_REPLACE ID ) { $value = $ID.text }
    ;

paste_with
    returns [ value ]
    :   ^( TREE_PASTE_WITH arbitrary_tokens )
        { $value = $arbitrary_tokens.value }
    ;

arbitrary_tokens
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( arbitrary_token
            { $value . append ( $arbitrary_token.value ) }
        ) +
    ;

arbitrary_token
    returns [ value ]
    :   CONSTS { $value = $CONSTS.text }
    |   MODULE { $value = $MODULE.text }
    |   TYPES { $value = $TYPES.text }

    |   CURLY_OPEN { $value = $CURLY_OPEN.text }
    |   CURLY_CLOSE { $value = $CURLY_CLOSE.text }
    |   DIVIDE { $value = $DIVIDE.text }
    |   MINUS { $value = $MINUS.text }
    |   UNDERSCORE { $value = $UNDERSCORE.text }
    |   ID { $value = $ID.text }
    |   NUMBER { $value = $NUMBER.text }
    |   EXPRESSION { $value = $EXPRESSION.text }
    ;
