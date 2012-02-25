import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class assigns_split_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raise ( self ) :
        ar = self . assertRaises
        r = self . n . run_assigns_split
        ne = normalizer . exception
        ar ( ne , r , mroot ( { 'anywhere' : { 'anywhere' :
            { 'ops' : [ { 'assign' :
                { 'from' : [ 'a1' , 'a2' ]
                , 'to' : [ 'a3' , 'a4' , 'a5' ]
                } } ] } } } ) )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run_assigns_split
        ne = normalizer . exception
        try :
            r ( mroot ( { 'path1' : { 'path2' :
                { 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' , 'a2' ]
                    , 'to' : [ 'a3' , 'a4' , 'a5' ] } } ] } } } ) )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' , 'ops' , 0 ] )
    def test_split ( self ) :
        ae = self . assertEqual
        r = self . n . run_assigns_split
        ae ( r (
            mroot ( { 'anywhere' : { 'anywhere' :
                { 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' , 'a2' ]
                    , 'to' : [ 'a3' , 'a4' , 'a5' , 'a6' ]
                    } } ] } } } ) ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                { 'ops' : 
                    [ { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a3' ] } }
                    , { 'assign' : { 'from' : [ 'a2' ] , 'to' : [ 'a4' ] } }
                    , { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a5' ] } }
                    , { 'assign' : { 'from' : [ 'a2' ] , 'to' : [ 'a6' ] } }
                    ] } } } ) )
