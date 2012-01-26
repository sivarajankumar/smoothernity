tree grammar ShyRecognizerBackend ;

options
{
    language = Python ;
    tokenVocab = ShyLexer ;
    ASTLabelType = object ;
}

@ header
{
    from fractions import Fraction

    def update_start_dict ( res , part , name , value ) :
        if part not in res :
            res [ part ] = dict ( )
        if name not in res [ part ] :
            res [ part ] [ name ] = dict ( )
        res [ part ] [ name ] . update ( value )
}

start
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( module 
            {
                update_start_dict ( $value , 'module' ,
                    $module.value , dict ( ) )
            }
        | stateless 
            {
                update_start_dict ( $value , 'stateless' ,
                    $stateless.title , $stateless.content )
            }
        | consts
            {
                update_start_dict ( $value , 'consts' ,
                    $consts.title , $consts.content )
            }
        | types
            {
                update_start_dict ( $value , 'types' ,
                    $types.title , $types.content )
            }
        ) *
    ;

module
    returns [ value ]
    :   ^( TREE_MODULE ID ) { $value = $ID.text }
    ;

stateless
    returns [ title , content ]
    :   ^( TREE_STATELESS ID )
            { $title , $content = $ID.text , dict ( ) }
    |   ^( TREE_STATELESS ID procs )
            { $title , $content = $ID.text , $procs.value }
    ;

procs
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ( proc { $value [ $proc.title ] = $proc.content } ) +
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
            ( proc_vars
                { $content [ 'vars' ] = $proc_vars.value }
            ) ?
            ( statements
                { $content [ 'ops' ] = $statements.value }
            ) ?
        )
    ;

proc_args
    returns [ value ]
    :   ^( TREE_PROC_ARGS vars_hint )
            { $value = $vars_hint.value }
    ;

proc_vars
    returns [ value ]
    :   ^( TREE_PROC_VARS vars_hint )
            { $value = $vars_hint.value }
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
    |   statement_if
            { $value = $statement_if.value }
    ;

statement_if
    returns [ value ]
    @ init { $value = { 'if' : [ ] } }
    :   ^( TREE_STATEMENT_IF
            ( statement_elif
                { $value [ 'if' ] . append ( $statement_elif.value ) }
            ) +
            ( statement_else
                { $value [ 'else' ] = $statement_else.value }
            ) ?
        )
    ;

statement_elif
    returns [ value ]
    :   ^( TREE_STATEMENT_ELIF condition_any statements )
            { $value = {
                'any' : $condition_any.value ,
                'ops' : $statements.value }
            }
    |   ^( TREE_STATEMENT_ELIF condition_all statements )
            { $value = {
                'all' : $condition_all.value ,
                'ops' : $statements.value }
            }
    ;

statement_else
    returns [ value ]
    :   ^( TREE_STATEMENT_ELSE statements )
            { $value = $statements.value }
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
    :   ( statement_call_arg
            { $value . append ( $statement_call_arg.value ) }
        ) *
    ;

statement_call_arg
    returns [ value ]
    :   ID { $value = $ID.text }
    |   EXPRESSION { $value = $EXPRESSION.text }
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
    :   ^( TREE_TYPES_ITEM ID vars_hint )
            { $name , $value = $ID.text , $vars_hint.value }
    ;

vars_hint
    returns [ value ]
    @ init { $value = dict ( ) }
    :   TREE_VARS_HINT ( var_hint { $value . update ( $var_hint.value ) } ) *
    ;

var_hint
    returns [ value ]
    @ init { $value = dict ( ) }
    :   ^( TREE_VAR_HINT TREE_HINT_NONE ( var
            { $value [ $var.value ] = dict ( ) }
        ) + )
    |   ^( TREE_VAR_HINT hint ( var
            { $value [ $var.value ] = $hint.value }
        ) + )
    ;

var
    returns [ value ]
    :   ^( TREE_VAR ID ) { $value = $ID.text }
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

