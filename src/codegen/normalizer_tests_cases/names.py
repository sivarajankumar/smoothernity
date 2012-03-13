import normalizer
import unittest
from normalizer . skeleton import run as rskel

class names_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . n . run_names
        ne = normalizer . exception
        bf = self . n . bind_func
        bf ( 'msg1' , [ ] )
        bf ( 'func1' , [ ] )
        bf ( 'test1_func1' , [ ] )
        ar ( ne , r , rskel ( { 'anywhere' : { 'anywhere' : [ { 'with' :
            { 'test1' : [ 'func1' ] } } ] } } ) )
        ar ( ne , r , rskel ( { 'anywhere' : { 'anywhere' : 
            { 'ops' : [ 'test1' ]
            , 'args' : [ { 'test1' : { } } ]
            , 'vars' : [ { 'test1' : { } } ] } } } ) )
        ar ( ne , r , rskel (
            { 'messages' : { 'test1' : 
                { 'receive' : { 'msg1' : [ ] } } }
            , 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'msg1' ] } } } } ) )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ ] )
        bf ( 'test1_func1' , [ ] )
        try :
            r ( rskel ( { 'path1' : { 'path2' : [ { 'with' :
                { 'test1' : [ 'func1' ] } } ] } } ) )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' , 0 , 'with' , 'test1' , 0 ] )
    def test_callable ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        bf = self . n . bind_func
        bf ( 'test1_func1' , [ ] )
        ae ( r ( rskel (
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'func1' ] } } } } ) ) , rskel (
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'test1_func1' ] } } } } ) )
    def test_sendable ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        ae ( r ( rskel (
            { 'messages' : { 'test1' : 
                { 'receive' : { 'msg1' : [ ] } } }
            , 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'msg1' ] } } } } ) ) , rskel (
            { 'messages' : { 'test1' : 
                { 'receive' : { 'msg1' : [ ] } } }
            , 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'test1_msg1' ] } } } } ) )
    def test_consts_global ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        ae ( r ( rskel (
            { 'consts' : { 'test1' : { 'const1' : 1 } }
            , 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1_consts' : [ 'const1' ] } } } } ) ) , rskel (
            { 'consts' : { 'test1' : { 'const1' : 1 } }
            , 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1_consts' : [ 'test1_consts_const1' ] } } } } ) )
    def test_consts_local ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        ae ( r ( rskel (
            { 'consts' : { 'space1' : { 'test1_const1' : 1 } }
            , 'anywhere' : { 'space1' : { 'with' :
                { 'consts_test1' : [ 'const1' ] } } } } ) ) , rskel (
            { 'consts' : { 'space1' : { 'test1_const1' : 1 } }
            , 'anywhere' : { 'space1' : { 'with' :
                { 'consts_test1' : [ 'consts_test1_const1' ] } } } } ) )
    def test_consts_bound ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        bc = self . n . bind_const
        bc ( 'test1_const1' , 1 )
        ae ( r ( rskel (
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'const1' ] } } } } ) ) , rskel (
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'test1' : [ 'test1_const1' ] } } } } ) )
    def test_vars_global ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        ae ( r ( rskel (
            { 'vars' : { 'space1' : [ { 'test1_var1' : { } } ] }
            , 'anywhere' : { 'space1' : { 'with' :
                { 'test1' : [ 'var1' ] } } } } ) ) , rskel (
            { 'vars' : { 'space1' : [ { 'test1_var1' : { } } ] }
            , 'anywhere' : { 'space1' : { 'with' :
                { 'test1' : [ 'test1_var1' ] } } } } ) )
    def test_vars_local ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        ae ( r ( rskel (
            { 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'test1_var1' : { } } ]
                , 'ops' : { 'with' :
                    { 'test1' : [ 'var1' ] } } } } } ) ) , rskel (
            { 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'test1_var1' : { } } ]
                , 'ops' : { 'with' :
                    { 'test1' : [ 'test1_var1' ] } } } } } ) )
    def test_args_local ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        ae ( r ( rskel (
            { 'anywhere' : { 'anywhere' :
                { 'args' : [ { 'test1_arg1' : { } } ]
                , 'ops' : { 'with' :
                    { 'test1' : [ 'arg1' ] } } } } } ) ) , rskel (
            { 'anywhere' : { 'anywhere' :
                { 'args' : [ { 'test1_arg1' : { } } ]
                , 'ops' : { 'with' :
                    { 'test1' : [ 'test1_arg1' ] } } } } } ) )
    def test_unknown_name ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        s = rskel ( { 'anywhere' : { 'anywhere' : { 'with' :
            { 'test1' : [ 'unknown' ] } } } } )
        ae ( r ( s ) , s )
    def test_double_prefix ( self ) :
        ae = self . assertEqual
        r = self . n . run_names
        s = rskel (
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
        ae ( r ( rskel (
            { 'anywhere' : { 'anywhere' : [ { 'with' :
                { 'test1' : [ { 'anywhere' : [ { 'with' :
                    { 'test2' : [ { 'anywhere' : [ { 'with' :
                        { 'test3' :
                            [ 'func1' 
                            , 'func2'
                            , 'func3'
                            , 'func4'
                            ] } } ] } ] } } ] } ] } } ] } } ) ) , rskel (
            { 'anywhere' : { 'anywhere' : [ { 'with' :
                { 'test1' : [ { 'anywhere' : [ { 'with' :
                    { 'test2' : [ { 'anywhere' : [ { 'with' :
                        { 'test3' :
                            [ 'test1_test2_test3_func1'
                            , 'test1_test3_func2'
                            , 'test1_func3'
                            , 'test2_func4'
                            ] } } ] } ] } } ] } ] } } ] } } ) )
