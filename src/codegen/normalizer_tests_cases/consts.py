import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class consts_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_expression ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'test1' :
                { 'test2' : 1 , 'test3' : '[ test2 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'test1' :
                { 'test2' : 1 , 'test3' : 1 } } } ) )
