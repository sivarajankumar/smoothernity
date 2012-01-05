import unittest
import recognizer
import io

class recognizer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . r = recognizer . recognizer ( )
    def rec ( self , s ) :
        return self . r . recognize ( io . StringIO ( s ) )
    def test_simple ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( '' ) , { } )

if __name__ == '__main__' :
    unittest . main ( )
