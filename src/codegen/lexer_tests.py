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
            , 'number' : [ r'[-]? *[0-9]+' ]
            } ] )
        self . assertEqual ( self . l . parse (
            [ 'test1 test_2 - 22 33' ] ) ,
            [ { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'id' , 'value' : 'test_2' }
            , { 'type' : 'number' , 'value' : '- 22' }
            , { 'type' : 'number' , 'value' : '33' }
            ] )
        self . assertRaises ( lexer . lexer_exception , self . l . parse , [ 'A' ] )
        self . assertRaises ( lexer . lexer_exception , self . l . parse , [ '2test' ] )

if __name__ == '__main__' :
    unittest . main ( )
