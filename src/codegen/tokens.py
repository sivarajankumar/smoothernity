def setup ( lexer ) :
    lexer . set_eol_token ( 'eol' )
    lexer . set_eof_token ( 'eof' )
    lexer . set_token_patterns (
        [ { 'underscore' : [ r'_' ]
          , 'number_whole' : [ r'-? *[0-9]+' ]
          , 'id' : [ r'[a-z][a-z0-9_]*' ] } ] )
