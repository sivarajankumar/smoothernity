import unittest
import lexer

class lexer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . l = lexer . lexer ( )
    def tearDown ( self ) :
        pass
    def test_empty ( self ) :
        self . assertEqual ( self . l . parse ( [ ] ) , [ ] )
    def test_tokens ( self ) :
        self . l . set_token_patterns ( [ 
            { 'id' : [ r'[a-z][a-z0-9_]*' ]
            , 'number' : [ r'[-]? *[0-9]+' ] } ] )
        self . assertEqual ( self . l . parse (
            [ 'test1 test_2 - 22 33' ] ) ,
            [ { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'id' , 'value' : 'test_2' }
            , { 'type' : 'number' , 'value' : '- 22' }
            , { 'type' : 'number' , 'value' : '33' } ] )
        self . assertRaises ( lexer . token_exception , self . l . parse , [ 'A' ] )
        self . assertRaises ( lexer . whitespace_exception , self . l . parse , [ '2test' ] )
    def test_indent ( self ) :
        self . l . set_indent_tokens ( 'indent' , 'dedent' )
        self . l . set_token_patterns ( [ { 'id' : [ r'[a-z0-9]+' ] } ] )
        self . assertEqual ( self . l . parse (
            [ 'test1'
            , '  test2'
            , '      test3'
            , '      test4'
            , 'test5' ] ) , 
            [ { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'indent' }
            , { 'type' : 'id' , 'value' : 'test2' }
            , { 'type' : 'indent' }
            , { 'type' : 'id' , 'value' : 'test3' }
            , { 'type' : 'id' , 'value' : 'test4' }
            , { 'type' : 'dedent' }
            , { 'type' : 'dedent' }
            , { 'type' : 'id' , 'value' : 'test5' } ] )
        self . assertRaises ( lexer . indent_exception , self . l . parse ,
            [ '  test1'
            , 'test2' ] )

if __name__ == '__main__' :
    unittest . main ( )
