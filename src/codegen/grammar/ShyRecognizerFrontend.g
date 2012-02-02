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

start : ( module | stateless | consts | types | messages | vars | trace ) * ;

module
    :   MODULE ID NEWLINE INDENT NEWLINE
        module_queue ?
        proc *
        receive *
        request *
        DEDENT NEWLINE
        ->  ^( TREE_MODULE ID
                module_queue ?
                proc *
                receive *
                request *
            )
    ;

module_queue
    :   MODULE_QUEUE ID NEWLINE
        ->  ^( TREE_MODULE_QUEUE ID )
    ;

trace
    :   TRACE ID NEWLINE ( INDENT NEWLINE proc + DEDENT NEWLINE ) ?
        ->  ^( TREE_TRACE ID proc * )
    ;

stateless
    :   STATELESS ID NEWLINE ( INDENT NEWLINE proc + DEDENT NEWLINE ) ?
        ->  ^( TREE_STATELESS ID proc * )
    ;

request
    :   REQUEST ID NEWLINE
        ->  ^( TREE_REQUEST ID )
    |   REQUEST ID statement
        ->  ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) )
    |   REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
        ->  ^( TREE_REQUEST ID statements )
    |   REQUEST ID NEWLINE INDENT NEWLINE
            local_vars ? local_ops ?
        DEDENT NEWLINE
        ->  ^( TREE_REQUEST ID local_vars ? local_ops ? )
    ;

receive
    :   RECEIVE ID NEWLINE
        ->  ^( TREE_RECEIVE ID )
    |   RECEIVE ID statement
        ->  ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) )
    |   RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
        ->  ^( TREE_RECEIVE ID statements )
    |   RECEIVE ID NEWLINE INDENT NEWLINE
            local_vars ? local_ops ?
        DEDENT NEWLINE
        ->  ^( TREE_RECEIVE ID local_vars ? local_ops ? )
    ;

proc
    :   PROC ID NEWLINE
        ->  ^( TREE_PROC ID )
    |   PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
        ->  ^( TREE_PROC ID statements )
    |   PROC ID NEWLINE INDENT NEWLINE
            proc_args ? local_vars ? local_ops ?
        DEDENT NEWLINE
        ->  ^( TREE_PROC ID proc_args ? local_vars ? local_ops ? )
    ;

proc_args
    :   ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints )
    ;

local_vars
    :   VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints )
    ;

local_ops
    :   OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
        -> statements
    |   OPS statement
        ->  ^( TREE_STATEMENTS statement )
    ;

statement
    :   statement_call_single_line NEWLINE
            -> statement_call_single_line
    |   statement_call_multi_line
    |   statement_if
    |   statement_assign
    |   statement_while
    |   statement_with
    ;

statements
    :   statement +
        ->  ^( TREE_STATEMENTS statement + )
    ;

statement_with
    :   WITH ID NEWLINE
        INDENT NEWLINE statements DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_WITH ID statements )
    ;

statement_assign
    :   ID + ARROW_LEFT arbitrary_value + NEWLINE
        ->  ^( TREE_STATEMENT_ASSIGN arbitrary_value +
                TREE_STATEMENT_ASSIGN_TO ID + )
    |   ID + ARROW_LEFT NEWLINE INDENT NEWLINE
        ( arbitrary_value + NEWLINE ) + DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_ASSIGN arbitrary_value +
                TREE_STATEMENT_ASSIGN_TO ID + )
    |   arbitrary_value + ARROW_RIGHT ID + NEWLINE
        ->  ^( TREE_STATEMENT_ASSIGN arbitrary_value +
                TREE_STATEMENT_ASSIGN_TO ID + )
    |   arbitrary_value + ARROW_RIGHT NEWLINE INDENT NEWLINE
        ( ID + NEWLINE ) + DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_ASSIGN arbitrary_value +
                TREE_STATEMENT_ASSIGN_TO ID + )
    ;

statement_while
    :   WHILE condition NEWLINE ? DO NEWLINE
            INDENT NEWLINE statements DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_WHILE condition statements )
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
            INDENT NEWLINE statements DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_ELIF condition statements )
    ;

statement_else
    :   ELSE NEWLINE
            INDENT NEWLINE statements DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_ELSE statements )
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
        ->  ^( TREE_STATEMENT_CALL ID statement_call_args ? )
    ;

statement_call_multi_line
    :   ID statement_call_args ? NEWLINE
        INDENT NEWLINE ( statement_call_args NEWLINE ) + DEDENT NEWLINE
        ->  ^( TREE_STATEMENT_CALL ID statement_call_args * )
    ;

statement_call_args : arbitrary_value + ;

arbitrary_value
    :   ID
    |   EXPRESSION
    |   STRING
    |   num_whole
    |   num_fract
    ;

consts
    :   CONSTS ID NEWLINE
        INDENT NEWLINE consts_items DEDENT NEWLINE
        ->  ^( TREE_CONSTS ID consts_items )
    ;
consts_items : consts_item + ;
consts_item
    :   ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole )
    |   ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract )
    |   ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION )
    ;

types
    :   TYPES ID NEWLINE
        INDENT NEWLINE types_item + DEDENT NEWLINE
        ->  ^( TREE_TYPES ID types_item + )
    ;
types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;

messages
    :   MESSAGES ID NEWLINE
        INDENT NEWLINE messages_item + DEDENT NEWLINE
        ->  ^( TREE_MESSAGES ID messages_item + )
    ;

messages_item
    :   ID attrs_hints
        ->  ^( TREE_MESSAGES_ITEM ID
                TREE_MESSAGES_ITEM_RECEIVE attrs_hints
            )
    |   ID REPLY attrs_hints
        ->  ^( TREE_MESSAGES_ITEM ID
                TREE_MESSAGES_ITEM_REPLY attrs_hints
            )
    |   ID REQUEST attrs_hints
        ->  ^( TREE_MESSAGES_ITEM ID
                TREE_MESSAGES_ITEM_REQUEST attrs_hints
            )
    |   ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE
        ->  ^( TREE_MESSAGES_ITEM ID
                TREE_MESSAGES_ITEM_REPLY attrs_hints
            )
    |   ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE
        ->  ^( TREE_MESSAGES_ITEM ID
                TREE_MESSAGES_ITEM_REQUEST attrs_hints
            )
    |   ID NEWLINE INDENT NEWLINE
            REQUEST attrs_hints
            REPLY attrs_hints
        DEDENT NEWLINE
        ->  ^( TREE_MESSAGES_ITEM ID
                TREE_MESSAGES_ITEM_REQUEST attrs_hints
                TREE_MESSAGES_ITEM_REPLY attrs_hints
            )
    ;

vars
    :   VARS ID attrs_hints
        ->  ^( TREE_VARS ID attrs_hints )
    ;

attrs_hints
    :   attr_hint NEWLINE
        ->  TREE_ATTRS_HINTS attr_hint
    |   NEWLINE
        ( INDENT NEWLINE ( attr_hint NEWLINE ) + DEDENT NEWLINE )
        ->  TREE_ATTRS_HINTS attr_hint +
    |   attr_hint NEWLINE
        ( INDENT NEWLINE ( attr_hint NEWLINE ) + DEDENT NEWLINE )
        ->  TREE_ATTRS_HINTS attr_hint +
    ;
attr_hint 
    :   ID + 
        ->  ^( TREE_ATTR_HINT TREE_HINT_NONE ^( TREE_ATTR ID ) + )
    |   hint ID +
        ->  ^( TREE_ATTR_HINT hint ^( TREE_ATTR ID ) + )
    |   hint NEWLINE INDENT NEWLINE ( ID + NEWLINE ) + DEDENT
        ->  ^( TREE_ATTR_HINT hint ^( TREE_ATTR ID ) + )
    ;

hint
    :   CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID )
    |   CURLY_OPEN ID hint_arg + CURLY_CLOSE -> ^( TREE_HINT ID hint_arg + )
    ;
hint_arg : ID | UNDERSCORE ;

num_whole : MINUS ? NUMBER ;
num_fract : MINUS ? NUMBER DIVIDE NUMBER ;
