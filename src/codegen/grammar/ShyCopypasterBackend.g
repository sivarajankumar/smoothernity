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
    : ( chunk { $value . append ( $chunk.value ) } ) *
    ;

chunk
    returns [ value ]
    : ^( TREE_ARBITRARY_TOKEN arbitrary_token ) { $value = [ $arbitrary_token.value ] }
    | copy_paste { $value = $copy_paste.value }
    ;

copy_paste
    returns [ value ]
    : ^( TREE_COPY_PASTE copy pastes )
        { $value = { 'copy' : $copy.value , 'paste' : $pastes.value } }
    ;

copy
    returns [ value ]
    : ^( TREE_COPY arbitrary_tokens ) { $value = $arbitrary_tokens.value }
    ;

pastes
    returns [ value ]
    @ init { $value = list ( ) }
    : ( paste { $value . append ( $paste.value ) } ) +
    ;

paste
    returns [ value ]
    : ^( TREE_PASTE paste_replace paste_with )
        { $value = { 'replace' : $paste_replace.value , 'with' : $paste_with.value } }
    ;

paste_replace
    returns [ value ]
    : ^( TREE_PASTE_REPLACE ID ) { $value = $ID.text }
    ;

paste_with
    returns [ value ]
    : ^( TREE_PASTE_WITH arbitrary_tokens ) { $value = $arbitrary_tokens.value }
    ;

arbitrary_tokens
    returns [ value ]
    @ init { $value = list ( ) }
    : ( arbitrary_token { $value . append ( $arbitrary_token.value ) } ) +
    ;

arbitrary_token
    returns [ value ]
    : CONSTS { $value = $CONSTS.text }
    | DEDENT { $value = $DEDENT.text }
    | INDENT { $value = $INDENT.text }
    | MODULE { $value = $MODULE.text }
    | TYPES { $value = $TYPES.text }

    | CURLY_OPEN { $value = $CURLY_OPEN.text }
    | CURLY_CLOSE { $value = $CURLY_CLOSE.text }
    | DIVIDE { $value = $DIVIDE.text }
    | MINUS { $value = $MINUS.text }
    | UNDERSCORE { $value = $UNDERSCORE.text }
    | NEWLINE { $value = $NEWLINE.text }
    | ID { $value = $ID.text }
    | NUMBER { $value = $NUMBER.text }
    | EXPRESSION { $value = $EXPRESSION.text }
    ;
