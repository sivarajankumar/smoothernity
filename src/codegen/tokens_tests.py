import unittest
import lexer
import tokens

class tokens_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . l = lexer . lexer ( )
        tokens . setup ( self . l )
    def test_underscore ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '_' ] ) ,
            [ { 'type' : 'underscore' , 'value' : '_' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . whitespace_exception , p , [ '__' ] )
        ar ( lexer . whitespace_exception , p , [ '_test' ] )
    def test_number_whole ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ '123 -45 - 56' ] ) ,
            [ { 'type' : 'number_whole' , 'value' : '123' }
            , { 'type' : 'number_whole' , 'value' : '-45' }
            , { 'type' : 'number_whole' , 'value' : '- 56' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . whitespace_exception , p , [ '123test' ] )
        ar ( lexer . token_exception , p , [ '--123' ] )
        ar ( lexer . token_exception , p , [ '- - 123' ] )
    def test_id ( self ) :
        p = self . l . parse
        self . assertEqual ( p ( [ 'test test1 test_22' ] ) ,
            [ { 'type' : 'id' , 'value' : 'test' }
            , { 'type' : 'id' , 'value' : 'test1' }
            , { 'type' : 'id' , 'value' : 'test_22' }
            , { 'type' : 'eol' }
            , { 'type' : 'eof' } ] )
        ar = self . assertRaises
        ar ( lexer . token_exception , p , [ 'TEST' ] )

if __name__ == '__main__' :
    unittest . main ( )
