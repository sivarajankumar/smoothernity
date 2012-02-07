import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton as mskel

class expression_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . n . run
        ne = normalizer . exception
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 + ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 / 0 ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ test3 ]' } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        try :
            r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 + ]' } } } )
        except Exception as e :
            pass
        ae ( e . get_path ( ) , [ 'consts' , 'test1' , 'test2' ] )
    def test_unicode ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : u'[ 1 ]' } } } ) ,
            mskel ( { 'consts' : { 'test1' : { 'test2' : 1 } } } ) )
    def test_ref_to_expressions ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : '[ test2 + 1 ]' , 'test2' : '[ 1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 } } } ) )
    def test_ref_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : 1
            , 'test3' : '[ test1 + test2 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 1 , 'test3' : 2 } } } ) )
    def test_pure_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : '[ test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 1 } } } ) )
    def test_global_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' :
            { 'consts1' : { 'test1' : 1 }
            , 'consts2' : { 'test2' : '[ consts1_consts_test1 ]' } } } ) ,
            mskel ( { 'consts' :
            { 'consts1' : { 'test1' : 1 }
            , 'consts2' : { 'test2' : 1 } } } ) )

class expression_math_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_add ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : '[ test1 + 1 ]'
            , 'test3' : '[ 1 + test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 2 , 'test3' : 2 } } } ) )
    def test_sub ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 - 1 ]'
            , 'test3' : '[ 3 - test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 , 'test3' : 1 } } } ) )
    def test_mul ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 * 3 ]'
            , 'test3' : '[ 3 * test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 6 , 'test3' : 6 } } } ) )
    def test_lshift ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : '[ test1 << 3 ]'
            , 'test3' : '[ 3 << test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 8 , 'test3' : 6 } } } ) )
    def test_rshift ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 >> 1 ]'
            , 'test3' : '[ 4 >> test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 , 'test3' : 1 } } } ) )
    def test_div ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 4
            , 'test2' : '[ test1 / 2 ]'
            , 'test3' : '[ 8 / test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 4 , 'test2' : 2 , 'test3' : 2 } } } ) )
    def test_mod ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 3
            , 'test2' : '[ test1 % 2 ]'
            , 'test3' : '[ 7 % test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 3 , 'test2' : 1 , 'test3' : 1 } } } ) )
    def test_pow ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 ** 3 ]'
            , 'test3' : '[ 3 ** test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 8 , 'test3' : 9 } } } ) )
    def test_and ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 0xFF00
            , 'test2' : '[ test1 & 0x1111 ]'
            , 'test3' : '[ 0x1111 & test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 0xFF00 , 'test2' : 0x1100 , 'test3' : 0x1100 } } } ) )
    def test_or ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233
            , 'test2' : '[ test1 | 0x1111 ]'
            , 'test3' : '[ 0x1111 | test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233 , 'test2' : 0x3333 , 'test3' : 0x3333 } } } ) )
    def test_xor ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233
            , 'test2' : '[ test1 ^ 0x1111 ]'
            , 'test3' : '[ 0x1111 ^ test1 ]' } } } ) ,
            mskel ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233 , 'test2' : 0x3322 , 'test3' : 0x3322 } } } ) )
