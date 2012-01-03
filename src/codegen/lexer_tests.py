import unittest
from lexer import lexer

class lexer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        pass
    def tearDown ( self ) :
        pass
    def test_empty ( self ) :
        self . assertEqual ( lexer ( ) . parse ( [ ] ) , [ ] )

if __name__ == '__main__' :
    unittest . main ( )
