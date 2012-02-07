import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton as mskel

class skeleton_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { } ) , mskel ( { } ) )
    def test_stateless ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'stateless' : { 'test1' : { } } } ) ,
            mskel ( { 'stateless' : { 'test1' : { 'proc' : { } } } } ) )
