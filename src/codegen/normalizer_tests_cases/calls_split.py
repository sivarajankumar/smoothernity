import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc

class calls_split_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raise ( self ) :
        ar = self . assertRaises
        r = self . n . run_calls_split
        ne = normalizer . exception
        bf = self . n . bind_func
        bf ( 'func1' , [ { } , { } ] )
        bf ( 'func2' , [ ] )
        ar ( ne , r , mroot ( { 'stateless' : { 'st1' : { 'proc' :
            mproc ( { 'proc1' : { 'ops' : [ { 'call' : [ 'func1' ] } ] } } )
            } } } ) )
        ar ( ne , r , mroot ( { 'stateless' : { 'st1' : { 'proc' :
            mproc ( { 'proc1' : { 'ops' : [ { 'call' : [ 'func1' , 'a' ] } ]
            } } ) } } } ) )
        ar ( ne , r , mroot ( { 'stateless' : { 'st1' : { 'proc' :
            mproc ( { 'proc1' : { 'ops' : [ { 'call' : [ 'func2' , 'a' ] } ]
            } } ) } } } ) )
        ar ( ne , r , mroot ( { 'stateless' : { 'st1' : { 'proc' :
            mproc ( { 'proc1' : { 'ops' : [ { 'call' : [ 'unknown' , 'a' ] }
            ] } } ) } } } ) )
        ar ( ne , r , mroot ( { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' : mproc (
                { 'args' : [ { } ] } ) } }
            , 'st2' : { 'proc' : { 'proc2' : mproc (
                { 'ops' : [ { 'call' : [ 'st1_stateless_unknown' , 'a2' ] } ]
            } ) } } } } ) )
        ar ( ne , r , mroot ( { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' : mproc (
                { 'args' : [ { } ] } ) } }
            , 'st2' : { 'proc' : { 'proc2' : mproc (
                { 'ops' : [ { 'call' : [ 'unknown_stateless_proc1' , 'a2' ] }
            ] } ) } } } } ) )
        ar ( ne , r , mroot (
            { 'trace' : { 'st1' : { 'proc' : { 'proc1' : mproc ( 
                { 'args' : [ { } ] } ) } } }
            , 'stateless' : { 'st2' : { 'proc' : { 'proc2' : mproc (
                { 'ops' : [ { 'call' : [ 'trace_proc1' , 'a2' ]
            } ] } ) } } } } ) )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ { } , { } ] )
        try :
            r ( mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                    mproc ( { 'ops' : [ { 'if' : [ { 'any' : [ { 'call' :
                        [ 'func1' , 'a' ] } ] } ] } ] } ) } } } } ) )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'stateless' , 'st1' , 'proc' , 'proc1' ,
            'ops' , 0 , 'if' , 0 , 'any' , 0 ] )
    def test_split_args ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        bf = self . n . bind_func
        bf ( 'func1' , [ { } , { } ] )
        ae ( r (
            mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                mproc ( { 'ops' :
                        [ { 'call' : [ 'func1' , 'a1' , 'a2' , 'a3' , 'a4' ] }
                ] } ) } } } } ) ) ,
            mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                mproc ( { 'ops' :
                        [ { 'call' : [ 'func1' , 'a1' , 'a2' ] }
                        , { 'call' : [ 'func1' , 'a3' , 'a4' ] }
                ] } ) } } } } ) )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        bf = self . n . bind_func
        bf ( 'func1' , [ ] )
        s = mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                mproc ( { 'ops' : [ { 'call' : [ 'func1' ] } ] } )
            } } } } )
        ae ( r ( s ) , s )
    def test_bind_func ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        bf = self . n . bind_func
        bf ( 'func1' , [ { } ] )
        s = mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                mproc ( { 'ops' : [ { 'call' : [ 'func1' , 'a' ] } ] } )
            } } } } )
        ae ( r ( s ) , s )
    def test_proc_local ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        s = mroot ( { 'stateless' : { 'st1' : { 'proc' :
            { 'proc1' : mproc ( { 'args' : [ { } ] } )
            , 'proc2' : mproc ( { 'ops' : [ { 'call' : [ 'proc1' , 'a' ] }
            ] } ) } } } } )
        ae ( r ( s ) , s )
    def test_proc_stateless ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        s = mroot ( { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' :
                mproc ( { 'args' : [ { } ] } ) } }
            , 'st2' : { 'proc' : { 'proc2' :
                mproc ( { 'ops' : [ { 'call' :
                    [ 'st1_stateless_proc1' , 'a' ] } ] } ) } } } } )
        ae ( r ( s ) , s )
    def test_proc_trace ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        s = mroot ( { 'trace' :
            { 'st1' : { 'proc' : { 'proc1' :
                mproc ( { 'args' : [ { } ] } ) } } }
            , 'st2' : { 'proc' : { 'proc2' :
                mproc ( { 'ops' : [ { 'call' :
                    [ 'st1_trace_proc1' , 'a' ] } ] } ) } } } )
        ae ( r ( s ) , s )
    def test_proc_stateless_local ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        s = mroot (
            { 'stateless' :
                { 'st1' : { 'proc' : { 'proc1' :
                    mproc ( { 'args' : [ { } ] } ) } } }
            , 'trace' :
                { 'st1' : { 'proc' : { 'proc2' :
                    mproc ( { 'ops' : [ { 'call' :
                        [ 'stateless_proc1' , 'a' ] } ] } ) } } } } )
        ae ( r ( s ) , s )
    def test_proc_trace_local ( self ) :
        ae = self . assertEqual
        r = self . n . run_calls_split
        s = mroot (
            { 'trace' :
                { 'st1' : { 'proc' : { 'proc1' :
                    mproc ( { 'args' : [ { } ] } ) } } }
            , 'stateless' :
                { 'st1' : { 'proc' : { 'proc2' :
                    mproc ( { 'ops' : [ { 'call' :
                        [ 'trace_proc1' , 'a' ] } ] } ) } } } } )
        ae ( r ( s ) , s )
