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
        ae ( r ( '\r' ) , { } )
    def test_modules ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'module test1' ) , { 'module' : { 'test1' : { } } } )
        ae ( r ( 'module test1\nmodule test2' ) ,
            { 'module' : { 'test1' : { } , 'test2' : { } } } )

if __name__ == '__main__' :
    unittest . main ( )
