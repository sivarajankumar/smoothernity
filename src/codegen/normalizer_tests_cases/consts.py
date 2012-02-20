import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class consts_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        ne = normalizer . exception
        r = self . n . run_consts
        ar ( ne , r , mroot ( { 'consts' : { 'test1' :
            { 'test2' : '[ unknown ]' } } } ) )
    def test_local_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'test1' :
                { 'test2' : 1
                , 'test3' : '[ test2 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'test1' :
                { 'test2' : 1
                , 'test3' : 1 } } } ) )
    def test_global_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' :
                { 'test1' : { 'const1' : 1 }
                , 'test2' : { 'const2' : '[ test1_consts_const1 ]' } } } ) ) ,
            mroot ( { 'consts' :
                { 'test1' : { 'const1' : 1 }
                , 'test2' : { 'const2' : 1 } } } ) )
    def test_inter_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'test1' :
                { 'test2' : 1
                , 'test3' : '[ test4 ]'
                , 'test4' : '[ test2 ]'
                } } } ) ) ,
            mroot ( { 'consts' : { 'test1' :
                { 'test2' : 1
                , 'test3' : 1
                , 'test4' : 1 } } } ) )
