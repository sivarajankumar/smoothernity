def setup ( lexer ) :
    lexer . set_eol_token ( 'eol' )
    lexer . set_eof_token ( 'eof' )
    lexer . set_indent_tokens ( 'indent' , 'dedent' )
    lexer . set_token_patterns (
        [ ( 'underscore' , r'_' )
        , ( 'left_arrow' , r'<-' )
        , ( 'right_arrow' , r'->' )
        , ( 'number_fract' , r'-? *[0-9]+ *\/ *[0-9]+' )
        , ( 'number_whole' , r'-? *[0-9]+' )
        , ( 'id' , r'[a-z][a-z0-9_]*' ) 
        , ( 'string' , r"'[^']*'" ) ] )
