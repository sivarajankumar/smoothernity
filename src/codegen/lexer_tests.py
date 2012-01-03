import unittest
import lexer

class lexer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . l = lexer . lexer ( )
        self . l . set_eol_token ( 'eol' )
        self . l . set_eof_token ( 'eof' )
        self . l . set_indent_tokens ( 'indent' , 'dedent' )
        self . l . set_token_patterns (
            [ ( 'id' , r'[a-z][a-z0-9_]*' )
            , ( 'number' , r'[-]? *[0-9]+' ) ] )
    def test_generate ( self ) :
        g = self . l . generate
        ae = self . assertEqual
        ae ( g (
            [ { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'id' , 'value' : 'test2' }
            , { 'type' : 'eol' }
            , { 'type' : 'indent' , 'delta' : 4 }
            , { 'type' : 'id' , 'value' : 'test3' }
            , { 'type' : 'eol' }
            , { 'type' : 'id' , 'value' : 'test4' }
            , { 'type' : 'eol' }
            , { 'type' : 'dedent' , 'delta' : - 4 }
            , { 'type' : 'indent' , 'delta' : 2 }
            , { 'type' : 'id' , 'value' : 'test5' }
            , { 'type' : 'eol' }
            , { 'type' : 'dedent' , 'delta' : - 2 }
            , { 'type' : 'eof' } ] ) ,
            [ 'test1 test2'
            , '    test3'
            , '    test4'
            , '  test5' ] )
    def test_generate_eof ( self ) :
        g = self . l . generate
        ae = self . assertEqual
        ae ( g (
            [ { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' }
            , { 'type' : 'id' , 'value' : 'test2' } ] ) , 
            [ 'test1' ] )
    def test_generate_eol ( self ) :
        g = self . l . generate
        ae = self . assertEqual
        ae ( g ( [ { 'type' : 'id' , 'value' : 'test1' } ] ) , [ ] )
    def test_generate_invalid_indent ( self ) :
        g = self . l . generate
        ar = self . assertRaises
        ar ( lexer . generate_indent_exception , g ,
            [ { 'type' : 'indent' , 'delta' : 0 } ] )
        ar ( lexer . generate_indent_exception , g ,
            [ { 'type' : 'indent' , 'delta' : - 1 } ] )
    def test_generate_invalid_dedent ( self ) :
        g = self . l . generate
        ar = self . assertRaises
        ar ( lexer . generate_dedent_exception , g ,
            [ { 'type' : 'indent' , 'delta' : 4 }
            , { 'type' : 'dedent' , 'delta' : - 5 } ] )
    def test_parse ( self ) :
        p = self . l . parse
        ae = self . assertEqual
        ae ( p (
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
    def test_parse_sequences ( self ) :
        self . l . set_token_patterns (
            [ ( 'double' , r'test test' )
            , ( 'single' , r'test' )
            ] )
        p = self . l . parse
        ae = self . assertEqual
        ae ( p ( 
            [ ' ' . join ( [ 'test' ] * 5 ) ] ) ,
            [ { 'type' : 'double' , 'value' : 'test test' }
            , { 'type' : 'double' , 'value' : 'test test' }
            , { 'type' : 'single' , 'value' : 'test' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
    def test_parse_eof ( self ) :
        p = self . l . parse
        ae = self . assertEqual
        ae ( p ( [ ] ) , [ { 'type' : 'eof' } ] )
        ae ( p ( [ '' ] ) , [ { 'type' : 'eof' } ] )
    def test_parse_invalid_token ( self ) :
        p = self . l . parse
        ar = self . assertRaises
        ar ( lexer . parse_token_exception , p , [ 'A' ] )
    def test_parse_no_whitespace ( self ) :
        p = self . l . parse
        ar = self . assertRaises
        ar ( lexer . parse_whitespace_exception , p , [ '2test' ] )
    def test_parse_invalid_indent ( self ) :
        p = self . l . parse
        ar = self . assertRaises
        ar ( lexer . parse_indent_exception , p , [ '  test1' , 'test2' ] )

if __name__ == '__main__' :
    unittest . main ( )
