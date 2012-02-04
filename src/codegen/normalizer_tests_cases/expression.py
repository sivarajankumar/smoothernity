import normalizer
import unittest

class expression_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . n . run
        ne = normalizer . exception
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 + ]' } } } )
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
            { 'consts' : { 'test1' : { 'test2' : 1 } } } )
    def test_refs_to_expressions ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : '[ test2 + 1 ]' , 'test2' : '[ 1 ]' } } } ) ,
            { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 } } } )
    def test_ref_ref ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : 1
            , 'test3' : '[ test1 + test2 ]' } } } ) ,
            { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 1 , 'test3' : 2 } } } )
    def test_ref_add ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : '[ test1 + 1 ]'
            , 'test3' : '[ 1 + test1 ]' } } } ) ,
            { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 2 , 'test3' : 2 } } } )
    def test_ref_mul ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 * 3 ]'
            , 'test3' : '[ 3 * test1 ]' } } } ) ,
            { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 6 , 'test3' : 6 } } } )
    def test_ref_lshift ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : '[ test1 << 3 ]'
            , 'test3' : '[ 3 << test1 ]' } } } ) ,
            { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 8 , 'test3' : 6 } } } )
    def test_ref_rshift ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 2
            , 'test2' : '[ test1 >> 1 ]'
            , 'test3' : '[ 4 >> test1 ]' } } } ) ,
            { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 , 'test3' : 1 } } } )
    def test_ref_div ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'consts1' :
            { 'test1' : 4
            , 'test2' : '[ test1 / 2 ]'
            , 'test3' : '[ 8 / test1 ]' } } } ) ,
            { 'consts' : { 'consts1' :
            { 'test1' : 4 , 'test2' : 2 , 'test3' : 2 } } } )
