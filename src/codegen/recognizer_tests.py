import unittest
import recognizer
import io

class recognizer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . r = recognizer . recognizer ( )
    def rec ( self , s ) :
        return self . r . recognize ( io . StringIO ( s ) )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( '' ) , { } )
        ae ( r ( ' ' ) , { } )
        ae ( r ( '\n' ) , { } )
        ae ( r ( '\r\n' ) , { } )
    def test_lexer_raises ( self ) :
        ar = self . assertRaises
        r = self . rec
        ar ( recognizer . exception , r , '!@#$' )
    def test_modules ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'module test1\n' ) , { 'module' : { 'test1' : { } } } )
        ae ( r ( 'module test1\nmodule test2\n' ) ,
            { 'module' : { 'test1' : { } , 'test2' : { } } } )
    def test_modules_raises ( self ) :
        ar = self . assertRaises
        r = self . rec
        ar ( recognizer . exception , r , 'module test1' )
        ar ( recognizer . exception , r , 'module' )
        ar ( recognizer . exception , r , 'module\n' )
        ar ( recognizer . exception , r , 'module module\n' )

if __name__ == '__main__' :
    unittest . main ( )
