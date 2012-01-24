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
        -> ^( TREE_PROC_OPS statement + )
    ;

statement
    :   statement_call
    ;

statement_call
    :   ID statement_call_args ? NEWLINE 
        ( INDENT NEWLINE ( statement_call_args NEWLINE ) + DEDENT NEWLINE ) ?
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
