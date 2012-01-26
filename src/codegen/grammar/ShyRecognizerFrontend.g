parser grammar ShyRecognizerFrontend ;

options 
{
    language = Python ;
    tokenVocab = ShyLexer ;
    output = AST ;
    ASTLabelType = object ;
}

@ header
{
    class ShyRecognizerFrontendException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ members
{
    def emitErrorMessage ( self , msg ) :
        raise ShyRecognizerFrontendException ( msg )
}

start : ( module | stateless | consts | types ) * ;

module
    :   MODULE ID NEWLINE -> ^( TREE_MODULE ID )
    ;

stateless
    :   STATELESS ID NEWLINE ( INDENT NEWLINE proc + DEDENT NEWLINE ) ?
        -> ^( TREE_STATELESS ID proc * )
    ;

proc
    :   PROC ID NEWLINE
        -> ^( TREE_PROC ID )
    |   PROC ID NEWLINE INDENT NEWLINE
            proc_args ? proc_vars ? proc_ops ?
        DEDENT NEWLINE
        -> ^( TREE_PROC ID proc_args ? proc_vars ? proc_ops ? )
    ;

proc_args
    :   ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint )
    ;

proc_vars
    :   VARS vars_hint -> ^( TREE_PROC_VARS vars_hint )
    ;

proc_ops
    :   OPS NEWLINE INDENT NEWLINE statement + DEDENT NEWLINE
        -> ^( TREE_STATEMENTS statement + )
    ;

statement
    :   statement_call_single_line NEWLINE
            -> statement_call_single_line
    |   statement_call_multi_line
    |   statement_if
    ;

statement_if
    :   statement_if_head
        statement_elif *
        statement_else ?
        ->  ^( TREE_STATEMENT_IF
                statement_if_head
                statement_elif *
                statement_else ?
            )
    ;

statement_if_head
    :   IF statement_elif_body
        ->  statement_elif_body
    ;

statement_elif
    :   ELIF statement_elif_body
        ->  statement_elif_body
    ;

statement_elif_body
    :   condition NEWLINE ? DO NEWLINE
            INDENT NEWLINE statement + DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_ELIF
                condition
                ^( TREE_STATEMENTS statement + )
            )
    ;

statement_else
    :   ELSE NEWLINE
            INDENT NEWLINE statement + DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_ELSE
                ^( TREE_STATEMENTS statement + )
            )
    ;

condition
    :   condition_call
        ->  ^( TREE_CONDITION_ANY condition_call )
    |   ANY condition_calls
        ->  ^( TREE_CONDITION_ANY condition_calls )
    |   ALL condition_calls
        ->  ^( TREE_CONDITION_ALL condition_calls )
    ;

condition_calls
    :   condition_call
    |   NEWLINE INDENT NEWLINE condition_call_line + DEDENT NEWLINE
        ->  condition_call_line +
    ;

condition_call
    :   statement_call_single_line
    |   statement_call_multi_line
    ;

condition_call_line
    :   statement_call_single_line NEWLINE
            -> statement_call_single_line
    |   statement_call_multi_line
    ;

statement_call_single_line
    :   ID statement_call_args ?
        ->  ^( TREE_STATEMENT_CALL ID
                TREE_STATEMENT_CALL_ARGS statement_call_args ? )
    ;

statement_call_multi_line
    :   ID statement_call_args ? NEWLINE
        INDENT NEWLINE ( statement_call_args NEWLINE ) + DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_CALL ID
                TREE_STATEMENT_CALL_ARGS statement_call_args * )
    ;

statement_call_args : statement_call_arg + ;

statement_call_arg
    :   ID
    |   EXPRESSION
    |   num_whole
    |   num_fract
    ;

consts
    :   CONSTS ID NEWLINE
        INDENT NEWLINE consts_items DEDENT NEWLINE
        -> ^( TREE_CONSTS ID consts_items )
    ;
consts_items : consts_item + ;
consts_item
    :   ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole )
    |   ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract )
    |   ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION )
    ;

types
    :   TYPES ID NEWLINE
        INDENT NEWLINE types_items DEDENT NEWLINE
        -> ^( TREE_TYPES ID types_items )
    ;
types_items : types_item + ;
types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;

vars_hint
    :   var_hint ? NEWLINE
        ( INDENT NEWLINE ( var_hint NEWLINE ) + DEDENT NEWLINE ) ?
        -> TREE_VARS_HINT var_hint *
    ;
var_hint 
    :   var + 
        -> ^( TREE_VAR_HINT TREE_HINT_NONE var + )
    |   hint var +
        -> ^( TREE_VAR_HINT hint var + )
    |   hint NEWLINE INDENT NEWLINE ( var + NEWLINE ) + DEDENT
        -> ^( TREE_VAR_HINT hint var + )
    ;
var : ID -> ^( TREE_VAR ID ) ;

hint
    :   CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID )
    |   CURLY_OPEN ID hint_arg + CURLY_CLOSE -> ^( TREE_HINT ID hint_arg + )
    ;
hint_arg : ID | UNDERSCORE ;

num_whole : MINUS ? NUMBER ;
num_fract : MINUS ? NUMBER DIVIDE NUMBER ;
