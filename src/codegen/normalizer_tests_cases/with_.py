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
            { 'test1' : [ { 'call' : [ 'func1' ] } ] } } ] } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ ] )
        bf ( 'test1func1' , [ ] )
        try :
            r ( { 'path1' : { 'path2' : [ { 'with' :
                { 'test1' : [ { 'call' : [ 'func1' ] } ] } } ] } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' , 0 , 'with' , 'test1' , 0 ] )
    def test_same_func ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'func1' , [ ] )
        ae ( r ( { 'anywhere' : { 'anywhere' : [ { 'with' :
            { 'test1' : [ { 'call' : [ 'func1' ] } ] } } ] } } ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                [ { 'call' : [ 'func1' ] } ] } } ) )
    def test_nested_with ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'test1test2test3func1' , [ ] )
        bf ( 'test2test3func2' , [ ] )
        bf ( 'test1func3' , [ ] )
        bf ( 'test2func4' , [ ] )
        ae ( r ( { 'anywhere' : { 'anywhere' : [ { 'with' :
            { 'test1' : [ { 'anywhere' : [ { 'with' :
                { 'test2' : [ { 'anywhere' : [ { 'with' :
                    { 'test3' :
                        [ { 'call' : [ 'func1' ] }
                        , { 'call' : [ 'func2' ] }
                        , { 'call' : [ 'func3' ] }
                        , { 'call' : [ 'func4' ] }
                        ] } } ] } ] } } ] } ] } } ] } } ) ,
            mroot ( { 'anywhere' : { 'anywhere' :
                [ { 'anywhere' : [ { 'anywhere' :
                [ { 'call' : [ 'test1test2func1' ] }
                , { 'call' : [ 'test2test3func2' ] }
                , { 'call' : [ 'test1func3' ] }
                , { 'call' : [ 'test2func4' ] }
                ] } ] } ] } } ) )
