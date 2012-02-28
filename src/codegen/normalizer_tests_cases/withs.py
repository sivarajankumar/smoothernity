import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc

class withs_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_strip ( self ) :
        ae = self . assertEqual
        r = self . n . run_withs
        ae ( r ( mroot (
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'prefix' : [ 'something' ] } } } } ) ) , mroot (
            { 'anywhere' : { 'anywhere' : 
                [ 'something' ] } } ) )
