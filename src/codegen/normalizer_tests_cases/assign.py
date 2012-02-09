import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc

class assign_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_augment ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'anywhere' : { 'anywhere' : [ { 'assign' :
            { 'from' : [ 'test1' ]
            , 'to' : [ 'test2' , 'test3' ] } } ] } } ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                [ { 'assign' : { 'from' : [ 'test1' ] , 'to' : [ 'test2' ] } }
                , { 'assign' : { 'from' : [ 'test1' ] , 'to' : [ 'test3' ] } }
                ] } } ) )
