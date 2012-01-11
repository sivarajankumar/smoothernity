import indenter
import unittest

class indenter_tests ( unittest . TestCase ) :
    def setUp ( self ) :
        self . i = indenter . indenter ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ '' ] ) , [ '' ] )

if __name__ == '__main__' :
    unittest . main ( )
