import normalizer
import unittest

class normalizer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { } ) , { } )

if __name__ == '__main__' :
    unittest . main ( )
