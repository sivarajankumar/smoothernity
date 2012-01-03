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
            { 'word' : r'[a-z]+'
            , 'number' : r'[0-9]+'
            , 'whitespace' : r' +'
            } ] )
        self . assertEqual ( self . l . parse (
            [ 'test1 test2' ] ) ,
            [ { 'type' : 'word' , 'value' : 'test' }
            , { 'type' : 'number' , 'value' : '1' }
            , { 'type' : 'whitespace' , 'value' : ' ' }
            , { 'type' : 'word' , 'value' : 'test' }
            , { 'type' : 'number' , 'value' : '2' }
            ] )

if __name__ == '__main__' :
    unittest . main ( )
