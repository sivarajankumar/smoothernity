import unittest
from normalizer . consts import run
from normalizer . exception import exception
from normalizer . skeleton import run as rskel

class consts_test_case ( unittest . TestCase ) :
    def test_raises ( self ) :
        ar = self . assertRaises
        r = lambda x : run ( rskel ( x ) )
        ne = exception
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 + ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 / 0 ]' } } } )
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ t3 ]' } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = run
        try :
            r ( rskel ( { 'consts' : { 't1' : { 't2' : '[ 1 + ]' } } } ) )
        except exception as e :
            pass
        ae ( e . get_path ( ) , [ 'consts' , 't1' , 't2' ] )
    def test_ref_to_expressions ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( rskel ( { 'consts' : { 'consts1' :
            { 'test1' : '[ test2 + 1 ]' , 'test2' : '[ 1 ]' } } } ) ) ,
            rskel ( { 'consts' : { 'consts1' :
            { 'test1' : 2 , 'test2' : 1 } } } ) )
    def test_ref_ref ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( rskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1
            , 'test2' : 1
            , 'test3' : '[ test1 + test2 ]' } } } ) ) ,
            rskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 1 , 'test3' : 2 } } } ) )
    def test_pure_ref ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( rskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : '[ test1 ]' } } } ) ) ,
            rskel ( { 'consts' : { 'consts1' :
            { 'test1' : 1 , 'test2' : 1 } } } ) )
    def test_global_ref ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( rskel ( { 'consts' :
            { 'consts1' : { 'test1' : 1 }
            , 'consts2' : { 'test2' : '[ consts1_consts_test1 ]' } } } ) ) ,
            rskel ( { 'consts' :
            { 'consts1' : { 'test1' : 1 }
            , 'consts2' : { 'test2' : 1 } } } ) )
    def test_same_name ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r ( rskel ( { 'consts' :
            { 'group1' : { 'test1' : 1 , 'test2' : '[ test1 ]' }
            , 'group2' : { 'test1' : 2 , 'test2' : '[ test1 ]' } } } ) ) ,
            rskel ( { 'consts' :
            { 'group1' : { 'test1' : 1 , 'test2' : 1 }
            , 'group2' : { 'test1' : 2 , 'test2' : 2 } } } ) )
    def test_outside ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r ( rskel (
            { 'consts' : { 'consts1' : { 'test1' : '[ 1 ]' } }
            , 'somewhere' : { 'out' : { 'there' :
                '[ consts1_consts_test1 ]' } }
            } ) ) , rskel (
            { 'consts' : { 'consts1' : { 'test1' : 1 } }
            , 'somewhere' : { 'out' : { 'there' : 1 } }
            } ) )
