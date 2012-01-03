import unittest
import lexer

class lexer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . l = lexer . lexer ( )
        self . l . set_eol_token ( 'eol' )
        self . l . set_eof_token ( 'eof' )
        self . l . set_indent_tokens ( 'indent' , 'dedent' )
    def test_sequences ( self ) :
        self . l . set_token_patterns (
            [ ( 'double' , r'test test' )
            , ( 'single' , r'test' )
            ] )
        self . assertEqual ( self . l . parse ( 
            [ ' ' . join ( [ 'test' ] * 5 ) ] ) ,
            [ { 'type' : 'double' , 'value' : 'test test' }
            , { 'type' : 'double' , 'value' : 'test test' }
            , { 'type' : 'single' , 'value' : 'test' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
    def test_tokens ( self ) :
        self . l . set_token_patterns (
            [ ( 'id' , r'[a-z][a-z0-9_]*' )
            , ( 'number' , r'[-]? *[0-9]+' ) ] )
        self . assertEqual ( self . l . parse (
            [ 'test1 test_2 - 22 33'
            , ''
            , '  test3'
            , '    '
            , '      test4'
            , '      test5'
            , '    test6' ] ) ,
            [ { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'id' , 'value' : 'test_2' }
            , { 'type' : 'number' , 'value' : '- 22' }
            , { 'type' : 'number' , 'value' : '33' } 
            , { 'type' : 'eol' }
            , { 'type' : 'indent' , 'delta' : 2 }
            , { 'type' : 'id' , 'value' : 'test3' }
            , { 'type' : 'eol' }
            , { 'type' : 'indent' , 'delta' : 4 }
            , { 'type' : 'id' , 'value' : 'test4' }
            , { 'type' : 'eol' }
            , { 'type' : 'id' , 'value' : 'test5' }
            , { 'type' : 'eol' }
            , { 'type' : 'dedent' , 'delta' : - 4 }
            , { 'type' : 'indent' , 'delta' : 2 }
            , { 'type' : 'id' , 'value' : 'test6' }
            , { 'type' : 'eol' }
            , { 'type' : 'dedent' , 'delta' : - 2 }
            , { 'type' : 'dedent' , 'delta' : - 2 }
            , { 'type' : 'eof' } ] )
        self . assertEqual ( self . l . parse ( [ ] ) , [ { 'type' : 'eof' } ] )
        self . assertEqual ( self . l . parse ( [ '' ] ) , [ { 'type' : 'eof' } ] )
        self . assertRaises ( lexer . token_exception , self . l . parse , [ 'A' ] )
        self . assertRaises ( lexer . whitespace_exception , self . l . parse , [ '2test' ] )
        self . assertRaises ( lexer . indent_exception , self . l . parse ,
            [ '  test1'
            , 'test2' ] )

if __name__ == '__main__' :
    unittest . main ( )
