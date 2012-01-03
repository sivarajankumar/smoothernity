def setup ( lexer ) :
    lexer . set_eol_token ( 'eol' )
    lexer . set_eof_token ( 'eof' )
    lexer . set_indent_tokens ( 'indent' , 'dedent' )
    lexer . set_token_patterns (
        [ ( kw , r'\b%s\b' % kw ) for kw in
            [ 'system' , 'machine' , 'state' , 'consts' , 'on' , 'to' , 'is'
            , 'command' , 'if' , 'do' , 'input' , 'entry' , 'exit' , 'initial'
            , 'discard' , 'vars' , 'ops' , 'receive' , 'request' , 'module'
            , 'trace' , 'with' , 'else' , 'while' , 'args' , 'proc' , 'init'
            , 'done' , 'copy' , 'paste' , 'replace' , 'module_name' , 'types'
            , 'reply' , 'messages' , 'stateless' , 'elif' , 'module_queue'
            , 'any' , 'all' , 'send' ] ] +
        [ ( 'underscore' , r'_' )
        , ( 'curly_open' , r'{' )
        , ( 'curly_close' , r'}' )
        , ( 'paren_open' , r'\(' )
        , ( 'paren_close' , r'\)' )
        , ( 'left_arrow' , r'<-' )
        , ( 'right_arrow' , r'->' )
        , ( 'number_fract' , r'-? *[0-9]+ *\/ *[0-9]+' )
        , ( 'number_whole' , r'-? *[0-9]+' )
        , ( 'number_whole' , r'\b(true|false)\b' )
        , ( 'string' , r"'[^']*'" )
        , ( 'expression' , r'\[[^\]]*\]' )
        , ( 'id' , r'[a-z][a-z0-9_]*' ) ] )
