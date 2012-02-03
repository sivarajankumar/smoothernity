import normalizer
import unittest

class run_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { } ) , { } )
