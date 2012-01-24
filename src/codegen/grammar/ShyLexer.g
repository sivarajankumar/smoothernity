lexer grammar ShyLexer ;

options 
{
    language = Python ;
}

@ header
{
    class ShyLexerException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ members
{
    def emitErrorMessage ( self , msg ) :
        raise ShyLexerException ( msg )
}

ARGS : 'args' ;
CONSTS : 'consts' ;
COPY : 'copy' ;
DEDENT : 'dedent' ;
DO : 'do' ;
ELIF : 'elif' ;
ELSE : 'else' ;
IF : 'if' ;
INDENT : 'indent' ;
MODULE : 'module' ;
OPS : 'ops' ;
PASTE : 'paste' ;
PROC : 'proc' ;
REPLACE : 'replace' ;
STATELESS : 'stateless' ;
TYPES : 'types' ;
VARS : 'vars' ;
WITH : 'with' ;

ARROW_LEFT : '<-' ;
ARROW_RIGHT : '->' ;
CURLY_OPEN : '{' ;
CURLY_CLOSE : '}' ;
DIVIDE : '/' ;
MINUS : '-' ;
UNDERSCORE : '_' ;
NEWLINE : '\n' ;
ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
WHITESPACE : ' ' + { self . skip ( ) } ;
EXPRESSION : '[' . * ']' ;
STRING : '\'' . * '\'' ;

TREE_ARBITRARY_TOKEN : 'TREE_ARBITRARY_TOKEN' ;
TREE_CONDITION_ANY : 'TREE_COND_ANY' ;
TREE_CONSTS : 'TREE_CONSTS' ;
TREE_COPY : 'TREE_COPY' ;
TREE_COPY_PASTE : 'TREE_COPY_PASTE' ;
TREE_EXPRESSION : 'TREE_EXPRESSION' ;
TREE_HINT : 'TREE_HINT' ;
TREE_HINT_NONE : 'TREE_HINT_NONE' ;
TREE_MODULE : 'TREE_MODULE' ;
TREE_NUM_FRACT : 'TREE_NUM_FRACT' ;
TREE_NUM_WHOLE : 'TREE_NUM_WHOLE' ;
TREE_PASTE : 'TREE_PASTE' ;
TREE_PASTE_REPLACE : 'TREE_PASTE_REPLACE' ;
TREE_PASTE_WITH : 'TREE_PASTE_WITH' ;
TREE_PROC : 'TREE_PROC' ;
TREE_PROC_ARGS : 'TREE_PROC_ARGS' ;
TREE_PROC_VARS : 'TREE_PROC_VARS' ;
TREE_STATELESS : 'TREE_STATELESS' ;
TREE_STATEMENT_CALL : 'TREE_STATEMENT_CALL' ;
TREE_STATEMENT_CALL_ARGS : 'TREE_STATEMENT_CALL_ARGS' ;
TREE_STATEMENT_ELIF : 'TREE_STATEMENT_ELIF' ;
TREE_STATEMENT_ELSE : 'TREE_STATEMENT_ELSE' ;
TREE_STATEMENT_IF : 'TREE_STATEMENT_IF' ;
TREE_STATEMENTS : 'TREE_STATEMENTS' ;
TREE_TYPES : 'TREE_TYPES' ;
TREE_TYPES_ITEM : 'TREE_TYPES_ITEM' ;
TREE_VAR : 'TREE_VAR' ;
TREE_VAR_HINT : 'TREE_VAR_HINT' ;
TREE_VARS_HINT : 'TREE_VARS_HINT' ;
