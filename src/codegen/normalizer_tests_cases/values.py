import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class values_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
        bf = self . n . bind_func
        bf ( 'func1' , [ { } ] )
    def test_raises ( self ) :
        ar = self . assertRaises
        ne = normalizer . exception
        r = self . n . run
        ar ( ne , r , { 'anywhere' : { 'anywhere' : [ { 'call' :
            [ 'func1' , 'unknown' ] } ] } } )
        ar ( ne , r , { 'vars' : { 'test1' : [ { 'test2' : { } } ] } ,
                'anywhere' : { 'test3' : [ { 'call' :
                    [ 'func1' , 'test2' ] } ] } } )
    def test_vars_global ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'vars' : { 'test1' : [ { 'test2' : { } } ] }
            , 'anywhere' : { 'test1' : [ { 'call' :
                [ 'func1' , 'test2' ] } ] } } ) ,
            mroot (
                { 'vars' : { 'test1' : [ { 'test2' : { } } ] }
                , 'anywhere' : { 'test1' : [ { 'call' :
                    [ 'func1' , 'test2' ] } ] } } ) )
    def test_vars_local ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'anywhere' : { 'anywhere' : 
                { 'ops' : [ { 'call' : [ 'func1' , 'test2' ] } ]
                , 'vars' : [ { 'test2' : { } } ] } } } ) ,
            mroot (
                { 'anywhere' : { 'anywhere' : 
                    { 'ops' : [ { 'call' : [ 'func1' , 'test2' ] } ]
                    , 'vars' : [ { 'test2' : { } } ] } } } ) )
    def test_consts_global ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'consts' : { 'test1' : { 'test2' : 1 } }
            , 'anywhere' : { 'anywhere' : [ { 'call' :
                [ 'func1' , 'test1_consts_test2' ] } ] } } ) ,
            mroot (
                { 'consts' : { 'test1' : { 'test2' : 1 } }
                , 'anywhere' : { 'anywhere' : [ { 'call' :
                    [ 'func1' , 1 ] } ] } } ) )
    def test_consts_expression_global ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'consts' : { 'test1' : { 'test2' : 1 } }
            , 'anywhere' : { 'anywhere' : [ { 'call' :
                [ 'func1' , '[ test1_consts_test2 ]' ] } ] } } ) ,
            mroot (
                { 'consts' : { 'test1' : { 'test2' : 1 } }
                , 'anywhere' : { 'anywhere' : [ { 'call' :
                    [ 'func1' , 1 ] } ] } } ) )
    def test_consts_local ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'consts' : { 'test1' : { 'test2' : 1 } }
            , 'anywhere' : { 'test1' : [ { 'call' :
                [ 'func1' , 'consts_test2' ] } ] } } ) ,
            mroot (
                { 'consts' : { 'test1' : { 'test2' : 1 } }
                , 'anywhere' : { 'test1' : [ { 'call' :
                    [ 'func1' , 1 ] } ] } } ) )
    def test_consts_expression_local ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'consts' : { 'test1' : { 'test2' : 1 } }
            , 'anywhere' : { 'test1' : [ { 'call' :
                [ 'func1' , '[ consts_test2 ]' ] } ] } } ) ,
            mroot (
                { 'consts' : { 'test1' : { 'test2' : 1 } }
                , 'anywhere' : { 'test1' : [ { 'call' :
                    [ 'func1' , 1 ] } ] } } ) )

