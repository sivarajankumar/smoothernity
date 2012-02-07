import normalizer
import unittest
from normalizer_tests_cases . helper import skeleton

class skeleton_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { } ) , skeleton )
