import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc

class names_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . n . run_names
        ne = normalizer . exception
        bf = self . n . bind_func
        bf ( 'func1' , [ ] )
        bf ( 'test1_func1' , [ ] )
        ar ( ne , r , mroot ( { 'anywhere' : { 'anywhere' : [ { 'with' :
            { 'test1' : [ 'func1' ] } } ] } } ) )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ ] )
        bf ( 'test1_func1' , [ ] )
        try :
            r ( { 'path1' : { 'path2' : [ { 'with' :
                { 'test1' : [ 'func1' ] } } ] } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' , 0 , 'with' , 'test1' , 0 ] )
    def test_callable ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        bf = self . n . bind_func
        bf ( 'test1_func1' , [ ] )
        ae ( r ( mroot (
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'func1' ] } } } } ) ) , mroot (
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'test1_func1' ] } } } } ) )
    def test_unknown_func ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        s = mroot ( { 'anywhere' : { 'anywhere' : { 'with' :
            { 'test1' : [ 'unknown' ] } } } } )
        ae ( r ( s ) , s )
    def test_double_prefix ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        s = mroot (
            { 'stateless' : { 'test1' : { 'proc' :
                { 'func1' : { } } } }
            , 'anywhere' : { 'anywhere' : [ { 'with' : { 'test1_stateless' :
                [ 'test1_stateless_func1' ]
            } } ] } } )
        ae ( r ( s ) , s )
    def test_nested_with ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        bf = self . n . bind_func
        bf ( 'test1_test2_test3_func1' , [ ] )
        bf ( 'test1_test3_func2' , [ ] )
        bf ( 'test1_func3' , [ ] )
        bf ( 'test2_func4' , [ ] )
        ae ( r ( mroot (
            { 'anywhere' : { 'anywhere' : [ { 'with' :
                { 'test1' : [ { 'anywhere' : [ { 'with' :
                    { 'test2' : [ { 'anywhere' : [ { 'with' :
                        { 'test3' :
                            [ 'func1' 
                            , 'func2'
                            , 'func3'
                            , 'func4'
                            ] } } ] } ] } } ] } ] } } ] } } ) ) , mroot (
            { 'anywhere' : { 'anywhere' : [ { 'with' :
                { 'test1' : [ { 'anywhere' : [ { 'with' :
                    { 'test2' : [ { 'anywhere' : [ { 'with' :
                        { 'test3' :
                            [ 'test1_test2_test3_func1'
                            , 'test1_test3_func2'
                            , 'test1_func3'
                            , 'test2_func4'
                            ] } } ] } ] } } ] } ] } } ] } } ) )
