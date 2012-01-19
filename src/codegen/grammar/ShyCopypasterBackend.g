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
    :   ( arbitrary_token
            { $value . append ( $arbitrary_token.value ) }
        ) +
        NEWLINE
            { $value += [ $NEWLINE.text ] }
    |   INDENT nl1 = NEWLINE
            { $value += [ $INDENT.text , $nl1.text ] }
        ( b1 = block
            { $value += $b1.value }
        ) + 
        DEDENT nl2 = NEWLINE
            { $value += [ $DEDENT.text , $nl2.text ] }
    |   { _copy , _paste = list ( ) , list ( ) }
        ^( TREE_COPY
            ( b2 = block 
                { _copy += $b2.value }
            ) +
        ( ^( TREE_PASTE
            ^( TREE_PASTE_REPLACE pr = paste_replace )
            ^( TREE_PASTE_WITH pw = paste_with )
                { _paste += [ [ $pr.value , $pw.value ] ] }
        ) ) + )
            { $value . append ( { 'copy' : _copy , 'paste' : _paste } ) }
    ;

paste_replace
    returns [ value ]
    :   ID { $value = $ID.text }
    ;

paste_with
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
