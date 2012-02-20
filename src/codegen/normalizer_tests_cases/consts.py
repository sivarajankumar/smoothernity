import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class consts_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = lambda x : self . n . run_consts ( mroot ( x ) )
        ne = normalizer . exception
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 + ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 / 0 ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ t3 ]' } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        try :
            r ( mroot ( { 'consts' : { 't1' : { 't2' : '[ 1 + ]' } } } ) )
        except Exception as e :
            pass
        ae ( e . get_path ( ) , [ 'consts' , 't1' , 't2' ] )
    def test_unicode ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 't1' : { 't2' : u'[ 1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 't1' : { 't2' : 1 } } } ) )
    def test_ref_to_expressions ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : '[ test2 + 1 ]' , 'test2' : '[ 1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 } } } ) )
    def test_ref_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : 1
            , 'test3' : '[ test1 + test2 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 1 , 'test3' : 2 } } } ) )
    def test_pure_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : '[ test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 1 } } } ) )
    def test_global_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' :
            { 'consts1' : { 'test1' : 1 }
            , 'consts2' : { 'test2' : '[ consts1_consts_test1 ]' } } } ) ) ,
            mroot ( { 'consts' :
            { 'consts1' : { 'test1' : 1 }
            , 'consts2' : { 'test2' : 1 } } } ) )
