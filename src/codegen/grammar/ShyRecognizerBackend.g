tree grammar ShyRecognizerBackend ;

options
{
    language = Python ;
    tokenVocab = ShyLexer ;
    ASTLabelType = object ;
}

@ header
{
    from utils import merge
    from fractions import Fraction
}

start
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( module 
            {
                $value = merge ( $value , { 'module' :
                    { $module.title : $module.content } } )
            }
        | stateless 
            {
                $value = merge ( $value , { 'stateless' :
                    { $stateless.title : $stateless.content } } )
            }
        | trace 
            {
                $value = merge ( $value , { 'trace' :
                    { $trace.title : $trace.content } } )
            }
        | consts
            {
                $value = merge ( $value , { 'consts' :
                    { $consts.title : $consts.content } } )
            }
        | types
            {
                $value = merge ( $value , { 'types' :
                    { $types.title : $types.content } } )
            }
        | messages
            {
                $value = merge ( $value , { 'messages' :
                    { $messages.title : $messages.content } } )
            }
        | vars
            {
                $value = merge ( $value , { 'vars' :
                    { $vars.title : $vars.content } } )
            }
        ) *
    ;

trace
    returns [ title , content ]
    :   ^( TREE_TRACE ID
            { $title , $content = $ID.text , dict ( ) }
            ( trace_item
                { $content = merge ( $content , $trace_item.value ) }
            ) *
        )
    ;

trace_item
    returns [ value ]
    :   proc
            { $value = { 'proc' : { $proc.title : $proc.content } } }
    ;

stateless
    returns [ title , content ]
    :   ^( TREE_STATELESS ID
            { $title , $content = $ID.text , dict ( ) }
            ( stateless_item
                { $content = merge ( $content , $stateless_item.value ) }
            ) *
        )
    ;

stateless_item
    returns [ value ]
    :   proc
            { $value = { 'proc' : { $proc.title : $proc.content } } }
    ;

module
    returns [ title , content ]
    :   ^( TREE_MODULE ID
            { $title , $content = $ID.text , dict ( ) }
            ( module_item
                { $content = merge ( $content , $module_item.value ) }
            ) *
        )
    ;

module_item
    returns [ value ]
    :   module_queue 
            { $value = { 'module_queue' : $module_queue.value } }
    |   proc
            { $value = { 'proc' : { $proc.title : $proc.content } } }
    |   receive
            { $value = { 'receive' : { $receive.title : $receive.content } } }
    |   request
            { $value = { 'request' : { $request.title : $request.content } } }
    ;

module_queue
    returns [ value ]
    :   ^( TREE_MODULE_QUEUE ID ) { $value = $ID.text }
    ;

request
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_REQUEST
            ID
                { $title = $ID.text }
            ( local_vars
                { $content [ 'vars' ] = $local_vars.value }
            ) ?
            ( statements
                { $content [ 'ops' ] = $statements.value }
            ) ?
        )
    ;

receive
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_RECEIVE
            ID
                { $title = $ID.text }
            ( local_vars
                { $content [ 'vars' ] = $local_vars.value }
            ) ?
            ( statements
                { $content [ 'ops' ] = $statements.value }
            ) ?
        )
    ;

proc
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_PROC
            ID
                { $title = $ID.text }
            ( proc_args
                { $content [ 'args' ] = $proc_args.value }
            ) ?
            ( local_vars
                { $content [ 'vars' ] = $local_vars.value }
            ) ?
            ( statements
                { $content [ 'ops' ] = $statements.value }
            ) ?
        )
    ;

proc_args
    returns [ value ]
    :   ^( TREE_PROC_ARGS attrs_hints )
            { $value = $attrs_hints.value }
    ;

local_vars
    returns [ value ]
    :   ^( TREE_LOCAL_VARS attrs_hints )
            { $value = $attrs_hints.value }
    ;

statements
    returns [ value ]
    @ init { $value = list ( ) }
    :   ^( TREE_STATEMENTS ( statement 
            { $value . append ( $statement.value ) }
        ) + )
    ;

statement
    returns [ value ]
    :   statement_call
            { $value = $statement_call.value }
    |   statement_send
            { $value = $statement_send.value }
    |   statement_if
            { $value = $statement_if.value }
    |   statement_assign
            { $value = $statement_assign.value }
    |   statement_with
            { $value = $statement_with.value }
    |   statement_while
            { $value = $statement_while.value }
    ;

statement_with
    returns [ value ]
    :   ^( TREE_STATEMENT_WITH ID statements )
        { $value = { 'with' : { $ID.text : $statements.value } } }
    ;

statement_assign
    returns [ value ]
    @ init { $value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } }
    :   ^( TREE_STATEMENT_ASSIGN
            ( arbitrary_value
                {
                    $value [ 'assign' ] [ 'from' ] . append (
                        $arbitrary_value.value )
                }
            ) +
            TREE_STATEMENT_ASSIGN_TO
            ( ID
                {
                    $value [ 'assign' ] [ 'to' ] . append (
                        $ID.text )
                }
            ) +
        )
    ;

statement_if
    returns [ value ]
    @ init { $value = { 'if' : [ ] } }
    :   ^( TREE_STATEMENT_IF
            ( ^( TREE_STATEMENT_ELIF conditional_ops )
                { $value [ 'if' ] . append ( $conditional_ops.value ) }
            ) +
            ( ^( TREE_STATEMENT_ELSE statements )
                { $value [ 'else' ] = $statements.value }
            ) ?
        )
    ;

statement_while
    returns [ value ]
    :   ^( TREE_STATEMENT_WHILE conditional_ops )
            { $value = { 'while' : $conditional_ops.value } }
    ;

conditional_ops
    returns [ value ]
    :   condition_any statements
            { $value = {
                'any' : $condition_any.value ,
                'ops' : $statements.value }
            }
    |   condition_all statements
            { $value = {
                'all' : $condition_all.value ,
                'ops' : $statements.value }
            }
    ;

condition_any
    returns [ value ]
    @ init { $value = list ( ) }
    :   ^( TREE_CONDITION_ANY
            ( statement_call
                { $value . append ( $statement_call.value ) }
            ) + )
    ;

condition_all
    returns [ value ]
    @ init { $value = list ( ) }
    :   ^( TREE_CONDITION_ALL
            ( statement_call
                { $value . append ( $statement_call.value ) }
            ) + )
    ;

statement_call
    returns [ value ]
    :   ^( TREE_STATEMENT_CALL statement_call_args )
            { $value = { 'call' : $statement_call_args.value } }
    ;

statement_call_args
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( arbitrary_value
            { $value . append ( $arbitrary_value.value ) }
        ) *
    ;

statement_send
    returns [ value ]
    :   ^( TREE_STATEMENT_SEND statement_send_args )
            { $value = { 'send' : $statement_send_args.value } }
    ;

statement_send_args
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( arbitrary_value
            { $value . append ( $arbitrary_value.value ) }
        ) *
    ;

arbitrary_value
    returns [ value ]
    :   ID { $value = $ID.text }
    |   EXPRESSION { $value = $EXPRESSION.text }
    |   STRING { $value = $STRING.text }
    |   num_whole { $value = $num_whole.value }
    |   num_fract { $value = $num_fract.value }
    ;

consts
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_CONSTS ID consts_items )
            { $title , $content = $ID.text , $consts_items.value }
    ;

consts_items
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( consts_item
            { $value [ $consts_item.name ] = $consts_item.value }
        ) +
    ;

consts_item
    returns [ name , value ]
    :   ^( TREE_NUM_WHOLE ID num_whole )
            { $name , $value = $ID.text , $num_whole.value }
    |   ^( TREE_NUM_FRACT ID num_fract )
            { $name , $value = $ID.text , $num_fract.value }
    |   ^( TREE_EXPRESSION ID EXPRESSION )
            { $name , $value = $ID.text , $EXPRESSION.text }
    ;

types
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_TYPES ID types_items )
            { $title , $content = $ID.text , $types_items.value }
    ;

types_items
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( types_item
            { $value [ $types_item.name ] = $types_item.value }
        ) +
    ;

types_item
    returns [ name , value ]
    :   ^( TREE_TYPES_ITEM ID attrs_hints )
            { $name , $value = $ID.text , $attrs_hints.value }
    ;

messages
    returns [ title , content ]
    @ init { $content = dict ( ) }
    :   ^( TREE_MESSAGES ID messages_items )
            { $title , $content = $ID.text , $messages_items.value }
    ;

messages_items
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( messages_item
            { $value = merge ( $value, $messages_item.value ) }
        ) +
    ;

messages_item
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ^( TREE_MESSAGES_ITEM ID
            ( TREE_MESSAGES_ITEM_RECEIVE a = attrs_hints
                {
                    $value = merge ( $value ,
                        { 'receive' : { $ID.text : $a.value } } )
                }
            ) ?
            ( TREE_MESSAGES_ITEM_REQUEST c = attrs_hints
                {
                    $value = merge ( $value ,
                        { 'request' : { $ID.text : $c.value } } )
                }
            ) ?
            ( TREE_MESSAGES_ITEM_REPLY b = attrs_hints
                {
                    $value = merge ( $value ,
                        { 'reply' : { $ID.text : $b.value } } )
                }
            ) ?
        )
    ;

vars
    returns [ title , content ]
    :   ^( TREE_VARS ID attrs_hints )
            { $title , $content = $ID.text , $attrs_hints.value }
    ;

attrs_hints
    returns [ value ]
    @ init { $value = list ( ) }
    :   TREE_ATTRS_HINTS ( attr_hint { $value += $attr_hint.value } ) *
    ;

attr_hint
    returns [ value ]
    @ init { $value = list ( ) }
    :   ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID )
            { $value . append ( { $ID.text : dict ( ) } ) }
        ) + )
    |   ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID )
            { $value . append ( { $ID.text : $hint.value } ) }
        ) + )
    ;

hint
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ^( TREE_HINT ID )
            { $value [ $ID.text ] = list ( ) }
    |   ^( TREE_HINT ID hint_args )
            { $value [ $ID.text ] = $hint_args.value }
    ;

hint_args
    returns [ value ]
    @ init { $value = list ( ) }
    :   ( hint_arg { $value . append ( $hint_arg.value ) } ) +
    ;

hint_arg
    returns [ value ]
    :   ID { $value = $ID.text }
    |   UNDERSCORE { $value = $UNDERSCORE.text }
    ;

num_whole
    returns [ value ]
    :   ( MINUS NUMBER )
            { $value = int ( $MINUS.text + $NUMBER.text ) }
    |   ( NUMBER )
            { $value = int ( $NUMBER.text ) }
    ;

num_fract
    returns [ value ]
    :   ( MINUS n = NUMBER DIVIDE d = NUMBER )
            {
                $value = Fraction ( int ( $MINUS.text + $n.text ) ,
                    int ( $d.text ) )
            }
    |   ( n = NUMBER DIVIDE d = NUMBER )
            { $value = Fraction ( int ( $n.text ) , int ( $d.text ) ) }
    ;

