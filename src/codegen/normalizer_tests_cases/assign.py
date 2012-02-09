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
        ar ( ne , r , { 'anywhere' : { 'anywhere' : [ { 'assign' :
            { 'from' : [ 'test1' , 'test2' ]
            , 'to' : [ 'test3' , 'test4' , 'test5' ] } } ] } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ne = normalizer . exception
        try :
            r ( { 'path1' : { 'path2' : [ { 'assign' :
                { 'from' : [ 'test1' , 'test2' ]
                , 'to' : [ 'test3' , 'test4' , 'test5' ] } } ] } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' , 0 ] )
    def test_split ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'anywhere' : { 'anywhere' : [ { 'assign' :
            { 'from' : [ 'test1' , 'test2' ]
            , 'to' : [ 'test3' , 'test4' , 'test5' , 'test6' ] } } ] } } ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                [ { 'assign' : { 'from' : [ 'test1' ] , 'to' : [ 'test3' ] } }
                , { 'assign' : { 'from' : [ 'test2' ] , 'to' : [ 'test4' ] } }
                , { 'assign' : { 'from' : [ 'test1' ] , 'to' : [ 'test5' ] } }
                , { 'assign' : { 'from' : [ 'test2' ] , 'to' : [ 'test6' ] } }
                ] } } ) )
