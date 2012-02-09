import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc

class with_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . n . run
        ne = normalizer . exception
        bf = self . n . bind_func
        bf ( 'func1' , [ ] )
        bf ( 'test1func1' , [ ] )
        ar ( ne , r , { 'anywhere' : { 'anywhere' : [ { 'with' :
            { 'test1' : { 'anywhere' : [ 'func1' ] } } } ] } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ ] )
        bf ( 'test1func1' , [ ] )
        try :
            r ( { 'path1' : { 'path2' : [ { 'with' :
                { 'test1' : { 'path3' : [ 'func1' ] } } } ] } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' , 0 , 'with' , 'test1' , 'path3' , 0 ] )
    def test_same_func ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'func1' , [ ] )
        ae ( r ( { 'anywhere' : { 'anywhere' : [ { 'with' :
            { 'test1' : { 'anywhere' : [ 'func1' ] } } } ] } } ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                { 'anywhere' : [ 'func1' ] } } } ) )
    def test_bound_func ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'test1func1' , [ ] )
        ae ( r ( { 'anywhere' : { 'anywhere' : [ { 'with' :
            { 'test1' : { 'anywhere' : [ 'func1' ] } } } ] } } ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                { 'anywhere' : [ 'test1func1' ] } } } ) )
