import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton as mskel

class consts_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_number ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : 1 } } } ) ,
            mskel ( { 'consts' : { 'test1' : { 'test2' : 1 } } } ) )
    def test_expression ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 ]' } } } ) ,
            mskel ( { 'consts' : { 'test1' : { 'test2' : 1 } } } ) )
