import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class expression_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_add ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : '[ test1 + 1 ]'
            , 'test3' : '[ 1 + test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 2 , 'test3' : 2 } } } ) )
    def test_sub ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 - 1 ]'
            , 'test3' : '[ 3 - test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 , 'test3' : 1 } } } ) )
    def test_mul ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 * 3 ]'
            , 'test3' : '[ 3 * test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 6 , 'test3' : 6 } } } ) )
    def test_lshift ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : '[ test1 << 3 ]'
            , 'test3' : '[ 3 << test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 8 , 'test3' : 6 } } } ) )
    def test_rshift ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 >> 1 ]'
            , 'test3' : '[ 4 >> test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 , 'test3' : 1 } } } ) )
    def test_div ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 4
            , 'test2' : '[ test1 / 2 ]'
            , 'test3' : '[ 8 / test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 4 , 'test2' : 2 , 'test3' : 2 } } } ) )
    def test_mod ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 3
            , 'test2' : '[ test1 % 2 ]'
            , 'test3' : '[ 7 % test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 3 , 'test2' : 1 , 'test3' : 1 } } } ) )
    def test_pow ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 ** 3 ]'
            , 'test3' : '[ 3 ** test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 8 , 'test3' : 9 } } } ) )
    def test_and ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 0xFF00
            , 'test2' : '[ test1 & 0x1111 ]'
            , 'test3' : '[ 0x1111 & test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 0xFF00 , 'test2' : 0x1100 , 'test3' : 0x1100 } } } ) )
    def test_or ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233
            , 'test2' : '[ test1 | 0x1111 ]'
            , 'test3' : '[ 0x1111 | test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233 , 'test2' : 0x3333 , 'test3' : 0x3333 } } } ) )
    def test_xor ( self ) :
        ae = self . assertEqual
        r = self . n . run_consts
        ae ( r ( mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233
            , 'test2' : '[ test1 ^ 0x1111 ]'
            , 'test3' : '[ 0x1111 ^ test1 ]' } } } ) ) ,
            mroot ( { 'consts' : { 'consts1' :
            { 'test1' : 0x2233 , 'test2' : 0x3322 , 'test3' : 0x3322 } } } ) )
