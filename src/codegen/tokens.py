def setup ( lexer ) :
    lexer . set_eol_token ( 'eol' )
    lexer . set_eof_token ( 'eof' )
    lexer . set_indent_tokens ( 'indent' , 'dedent' )
    lexer . set_token_patterns (
        [ ( 'keyword' , 'copy|paste|replace' )
        , ( 'keyword' , 'initial' )
        , ( 'keyword' , 'init|done' )
        , ( 'keyword' , 'consts|types|messages|trace|stateless|vars' )
        , ( 'keyword' , 'module_queue|module_name' )
        , ( 'keyword' , 'module' )
        , ( 'keyword' , 'system|machine|state|input|entry|exit' )
        , ( 'keyword' , 'command|discard|on|to|is|do' )
        , ( 'keyword' , 'proc|args|ops' )
        , ( 'keyword' , 'if|elif|else|any|all|while' )
        , ( 'keyword' , 'receive|request|reply|send' )
        , ( 'keyword' , 'with' )
        , ( 'underscore' , '_' )
        , ( 'curly_open' , '{' )
        , ( 'curly_close' , '}' )
        , ( 'paren_open' , '\(' )
        , ( 'paren_close' , '\)' )
        , ( 'left_arrow' , '<-' )
        , ( 'right_arrow' , '->' )
        , ( 'number_fract' , '-? *[0-9]+ *\/ *[0-9]+' )
        , ( 'number_whole' , '-? *[0-9]+' )
        , ( 'number_whole' , 'true|false' )
        , ( 'string' , "'[^']*'" )
        , ( 'expression' , '\[[^\]]*\]' )
        , ( 'id' , '[a-z][a-z0-9_]*' ) ] )
