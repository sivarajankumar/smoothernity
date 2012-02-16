import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc

class call_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raise ( self ) :
        ar = self . assertRaises
        r = self . n . run
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ { } , { } ] )
        bf ( 'func2' , [ ] )
        ar ( ne , r , { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
            { 'ops' : [ { 'call' : [ 'func1' ] } ] } } } } } )
        ar ( ne , r , { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
            { 'vars' : [ { 'a1' : { } } ]
            , 'ops' : [ { 'call' : [ 'func1' , 'a1' ] } ] } } } } } )
        ar ( ne , r , { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
            { 'vars' : [ { 'a1' : { } } ]
            , 'ops' : [ { 'call' : [ 'func2' , 'a1' ] } ] } } } } } )
        ar ( ne , r , { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
            { 'vars' : [ { 'a1' : { } } ]
            , 'ops' : [ { 'call' : [ 'unknown' , 'a1' ] } ] } } } } } )
        ar ( ne , r , { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } }
            , 'st2' : { 'proc' : { 'proc2' :
                { 'vars' : [ { 'a2' : { } } ]
                , 'ops' : [ { 'call' : [ 'st1_stateless_unknown' , 'a2' ]
            } ] } } } } } )
        ar ( ne , r , { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } }
            , 'st2' : { 'proc' : { 'proc2' :
                { 'vars' : [ { 'a2' : { } } ]
                , 'ops' : [ { 'call' : [ 'unknown_stateless_proc1' , 'a2' ]
            } ] } } } } } )
        ar ( ne , r ,
            { 'trace' :
                { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } } }
            , 'stateless' :
                { 'st2' : { 'proc' : { 'proc2' :
                    { 'vars' : [ { 'a2' : { } } ]
                    , 'ops' : [ { 'call' : [ 'trace_proc1' , 'a2' ]
            } ] } } } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ { } , { } ] )
        try :
            r ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'a1' : { } } ]
                , 'ops' :
                [ { 'if' : [ { 'any' : [ { 'call' : [ 'func1' , 'a1' ] } ] } ]
                } ] } } } } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'stateless' , 'st1' , 'proc' , 'proc1' ,
            'ops' , 0 , 'if' , 0 , 'any' , 0 ] )
    def test_split_args ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'func1' , [ { } , { } ] )
        ae ( r ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
            { 'vars' : [ { 'a1' : { } } , { 'a2' : { } }
                       , { 'a3' : { } } , { 'a4' : { } } ]
            , 'ops' :
                [ { 'call' : [ 'func1' , 'a1' , 'a2' , 'a3' , 'a4' ] }
                ] } } } } } ) ,
            mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                mproc (
                    { 'vars' : [ { 'a1' : { } } , { 'a2' : { } }
                               , { 'a3' : { } } , { 'a4' : { } } ]
                    , 'ops' :
                        [ { 'call' : [ 'func1' , 'a1' , 'a2' ] }
                        , { 'call' : [ 'func1' , 'a3' , 'a4' ] }
                        ] } ) } } } } ) )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'func1' , [ ] )
        ae ( r ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
            [ { 'call' : [ 'func1' ] } ] } } } } } ) ,
            mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                mproc ( { 'ops' : [ { 'call' : [ 'func1' ] } ] } )
            } } } } ) )
    def test_bind_func ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'func1' , [ { } ] )
        ae ( r ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
            { 'vars' : [ { 'a1' : { } } ]
            , 'ops' : [ { 'call' : [ 'func1' , 'a1' ] }
            ] } } } } } ) ,
            mroot ( { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                mproc (
                    { 'vars' : [ { 'a1' : { } } ]
                    , 'ops' : [ { 'call' : [ 'func1' , 'a1' ] }
                    ] } ) } } } } ) )
    def test_proc_local ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'stateless' : { 'st1' : { 'proc' :
            { 'proc1' : { 'args' : [ { } ] }
            , 'proc2' :
                { 'vars' : [ { 'a1' : { } } ]
                , 'ops' : [ { 'call' : [ 'proc1' , 'a1' ] }
                ] } } } } } ) ,
            mroot ( { 'stateless' : { 'st1' : { 'proc' :
            { 'proc1' : mproc ( { 'args' : [ { } ] } )
            , 'proc2' : mproc (
                { 'vars' : [ { 'a1' : { } } ]
                , 'ops' : [ { 'call' : [ 'proc1' , 'a1' ] }
                ] } ) } } } } ) )
    def test_proc_stateless ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } }
            , 'st2' : { 'proc' : { 'proc2' :
                { 'vars' : [ { 'a1' : { } } ]
                , 'ops' : [ { 'call' : [ 'st1_stateless_proc1' , 'a1' ] }
                ] } } } } } ) ,
            mroot ( { 'stateless' :
                { 'st1' : { 'proc' : { 'proc1' :
                    mproc ( { 'args' : [ { } ] } ) } }
                , 'st2' : { 'proc' : { 'proc2' :
                    mproc (
                        { 'vars' : [ { 'a1' : { } } ]
                        , 'ops' :
                            [ { 'call' : [ 'st1_stateless_proc1' , 'a1' ] }
                            ] } ) } } } } ) )
    def test_proc_trace ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'trace' :
            { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } }
            , 'st2' : { 'proc' : { 'proc2' :
                { 'vars' : [ { 'a1' : { } } ]
                , 'ops' : [ { 'call' : [ 'st1_trace_proc1' , 'a1' ] }
                ] } } } } } ) ,
            mroot ( { 'trace' :
                { 'st1' : { 'proc' : { 'proc1' :
                    mproc ( { 'args' : [ { } ] } ) } }
                , 'st2' : { 'proc' : { 'proc2' :
                    mproc (
                        { 'vars' : [ { 'a1' : { } } ]
                        , 'ops' :
                            [ { 'call' : [ 'st1_trace_proc1' , 'a1' ] }
                            ] } ) } } } } ) )
    def test_proc_stateless_local ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'stateless' :
                { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } } }
            , 'trace' :
                { 'st1' : { 'proc' : { 'proc2' :
                    { 'vars' : [ { 'a1' : { } } ]
                    , 'ops' : [ { 'call' : [ 'stateless_proc1' , 'a1' ] }
                    ] } } } } } ) ,
            mroot (
                { 'stateless' :
                    { 'st1' : { 'proc' : { 'proc1' :
                        mproc ( { 'args' : [ { } ] } ) } } }
                , 'trace' :
                    { 'st1' : { 'proc' : { 'proc2' :
                        mproc (
                            { 'vars' : [ { 'a1' : { } } ]
                            , 'ops' :
                                [ { 'call' : [ 'stateless_proc1' , 'a1' ] }
                                ] } ) } } } } ) )
    def test_proc_trace_local ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'trace' :
                { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } } }
            , 'stateless' :
                { 'st1' : { 'proc' : { 'proc2' :
                    { 'vars' : [ { 'a1' : { } } ]
                    , 'ops' : [ { 'call' : [ 'trace_proc1' , 'a1' ] }
                    ] } } } } } ) ,
            mroot (
                { 'trace' :
                    { 'st1' : { 'proc' : { 'proc1' :
                        mproc ( { 'args' : [ { } ] } ) } } }
                , 'stateless' :
                    { 'st1' : { 'proc' : { 'proc2' :
                        mproc (
                            { 'vars' : [ { 'a1' : { } } ]
                            , 'ops' :
                                [ { 'call' : [ 'trace_proc1' , 'a1' ] }
                                ] } ) } } } } ) )
