import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class assign_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raise ( self ) :
        ar = self . assertRaises
        r = self . n . run
        ne = normalizer . exception
        ar ( ne , r , { 'anywhere' : { 'anywhere' :
            { 'vars' : [ { 'a1' : { } } , { 'a2' : { } }
                       , { 'a3' : { } } , { 'a4' : { } }
                       , { 'a5' : { } } ]
            , 'ops' : [ { 'assign' :
                { 'from' : [ 'a1' , 'a2' ]
                , 'to' : [ 'a3' , 'a4' , 'a5' ]
                } } ] } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ne = normalizer . exception
        try :
            r ( { 'path1' : { 'path2' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } }
                           , { 'a3' : { } } , { 'a4' : { } }
                           , { 'a5' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' , 'a2' ]
                    , 'to' : [ 'a3' , 'a4' , 'a5' ] } } ] } } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' , 'ops' , 0 ] )
    def test_split ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'anywhere' : { 'anywhere' :
            { 'vars' : [ { 'a1' : { } } , { 'a2' : { } }
                       , { 'a3' : { } } , { 'a4' : { } }
                       , { 'a5' : { } } , { 'a6' : { } } ]
            , 'ops' : [ { 'assign' :
                { 'from' : [ 'a1' , 'a2' ]
                , 'to' : [ 'a3' , 'a4' , 'a5' , 'a6' ]
                } } ] } } } ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } }
                           , { 'a3' : { } } , { 'a4' : { } }
                           , { 'a5' : { } } , { 'a6' : { } } ]
                , 'ops' : 
                    [ { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a3' ] } }
                    , { 'assign' : { 'from' : [ 'a2' ] , 'to' : [ 'a4' ] } }
                    , { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a5' ] } }
                    , { 'assign' : { 'from' : [ 'a2' ] , 'to' : [ 'a6' ] } }
                    ] } } } ) )
