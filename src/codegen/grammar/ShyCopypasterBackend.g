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
    @ init { $value = list ( ) }
    :   arbitrary_tokens
            { $value += $arbitrary_tokens.value }
        NEWLINE
            { $value += [ $NEWLINE.text ] }
    |   INDENT nl1 = NEWLINE
            { $value += [ $INDENT.text , $nl1.text ] }
        ( b1 = block
            { $value += $b1.value }
        ) + 
        DEDENT nl2 = NEWLINE
            { $value += [ $DEDENT.text , $nl2.text ] }
    |   copy { $value += $copy.value }
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

pure_blocks
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( pure_block
            { $value += $pure_block.value }
        ) +
    ;

copy
    returns [ value ]
    :   ^( TREE_COPY copy_body copy_pastes )
        {
            $value = [ { 'copy' : $copy_body.value
                       , 'paste' : $copy_pastes.value } ]
        }
    ;

copy_body
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( pure_block { $value += $pure_block.value } ) +
    ;

copy_pastes
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( copy_paste { $value . append ( $copy_paste.value ) } ) +
    ;

copy_paste
    returns [ value ]
    :   ^( TREE_COPY_PASTE pastes ) { $value = $pastes.value }
    ;

pastes
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( paste { $value . update ( $paste.value ) } ) +
    ;

paste
    returns [ value ]
    :   ^( TREE_PASTE paste_replace paste_with )
        { $value = { $paste_replace.value : $paste_with.value } }
    ;

paste_replace
    returns [ value ]
    :   ^( TREE_PASTE_REPLACE ID ) { $value = $ID.text }
    ;

paste_with
    returns [ value ]
    :   ^( TREE_PASTE_WITH arbitrary_tokens )
        { $value = $arbitrary_tokens.value }
    |   ^( TREE_PASTE_WITH pure_blocks )
        { $value = $pure_blocks.value }
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
    :   ARGS { $value = $ARGS.text }
    |   CONSTS { $value = $CONSTS.text }
    |   MODULE { $value = $MODULE.text }
    |   PROC { $value = $PROC.text }
    |   STATELESS { $value = $STATELESS.text }
    |   TYPES { $value = $TYPES.text }
    |   VARS { $value = $VARS.text }
    |   WITH { $value = $WITH.text }

    |   ARROW_LEFT { $value = $ARROW_LEFT.text }
    |   ARROW_RIGHT { $value = $ARROW_RIGHT.text }
    |   CURLY_OPEN { $value = $CURLY_OPEN.text }
    |   CURLY_CLOSE { $value = $CURLY_CLOSE.text }
    |   DIVIDE { $value = $DIVIDE.text }
    |   MINUS { $value = $MINUS.text }
    |   UNDERSCORE { $value = $UNDERSCORE.text }
    |   ID { $value = $ID.text }
    |   NUMBER { $value = $NUMBER.text }
    |   EXPRESSION { $value = $EXPRESSION.text }
    |   STRING { $value = $STRING.text }
    ;
