from normalizer . calls import run
from normalizer . skeleton import run as rskel
from normalizer . exception import exception
import unittest

class calls_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        ar = self . assertRaises
        r = lambda x : run ( rskel ( x ) )
        ne = exception
        ar ( ne , r ,
            { 'platform_procs' : { 'func1' : { 'args' : [ { } , { } ] } }
            , 'stateless' : { 'st1' : { 'proc' :
                { 'proc1' : { 'ops' : [ { 'call' : [ 'func1' ] } ] } } } } } )
        ar ( ne , r ,
            { 'platform_procs' : { 'func1' : { 'args' : [ { } , { } ] } }
            , 'stateless' : { 'st1' : { 'proc' :
                { 'proc1' : { 'ops' : [ { 'call' : [ 'func1' , 'a' ] } ] } } }
            } } )
        ar ( ne , r ,
            { 'platform_procs' : { 'func2' : { } }
            , 'stateless' : { 'st1' : { 'proc' :
                { 'proc1' : { 'ops' : [ { 'call' : [ 'func2' , 'a' ] } ]
                } } } } } )
        ar ( ne , r , { 'stateless' : { 'st1' : { 'proc' :
            { 'proc1' : { 'ops' : [ { 'call' : [ 'unknown' , 'a' ] }
            ] } } } } } )
        ar ( ne , r , { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' :
                { 'args' : [ { } ] } } }
            , 'st2' : { 'proc' : { 'proc2' :
                { 'ops' : [ { 'call' : [ 'st1_stateless_unknown' , 'a2' ] } ]
            } } } } } )
        ar ( ne , r , { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' :
                { 'args' : [ { } ] } } }
            , 'st2' : { 'proc' : { 'proc2' : 
                { 'ops' : [ { 'call' : [ 'unknown_stateless_proc1' , 'a2' ] }
            ] } } } } } )
        ar ( ne , r ,
            { 'trace' : { 'st1' : { 'proc' : { 'proc1' :
                { 'args' : [ { } ] } } } }
            , 'stateless' : { 'st2' : { 'proc' : { 'proc2' :
                { 'ops' : [ { 'call' : [ 'trace_proc1' , 'a2' ]
            } ] } } } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = run
        ne = exception
        try :
            r ( rskel (
                { 'platform_procs' : { 'func1' : { 'args' : [ { } , { } ] } }
                , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                    { 'ops' : [ { 'if' : [ { 'any' : [ { 'call' :
                        [ 'func1' , 'a' ] } ] } ] } ] } } } } } ) )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'stateless' , 'st1' , 'proc' , 'proc1' ,
            'ops' , 0 , 'if' , 0 , 'any' , 0 ] )
    def test_split_args ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( rskel (
            { 'platform_procs' : { 'func1' : { 'args' : [ { } , { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'ops' :
                    [ { 'call' : [ 'func1' , 'a1' , 'a2' , 'a3' , 'a4' ] }
                ] } } } } } ) ) , rskel (
            { 'platform_procs' : { 'func1' : { 'args' : [ { } , { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'ops' :
                        [ { 'call' : [ 'func1' , 'a1' , 'a2' ] }
                        , { 'call' : [ 'func1' , 'a3' , 'a4' ] }
                ] } } } } } ) )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = run
        s = rskel (
            { 'platform_procs' : { 'func1' : { } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'ops' : [ { 'call' : [ 'func1' ] } ] } } } } } )
        ae ( r ( s ) , s )
    def test_bind_func ( self ) :
        ae = self . assertEqual
        r = run
        s = rskel (
            { 'platform_procs' : { 'func1' : { 'args' : [ { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'ops' : [ { 'call' : [ 'func1' , 'a' ] } ] } } } } } )
        ae ( r ( s ) , s )
    def test_proc_local ( self ) :
        ae = self . assertEqual
        r = run
        s = rskel (
            { 'stateless' : { 'st1' : { 'proc' :
                { 'proc1' : { 'args' : [ { } ] }
                , 'proc2' : { 'ops' : [ { 'call' : [ 'proc1' , 'a' ] }
                ] } } } } } )
        ae ( r ( s ) , s )
    def test_proc_stateless ( self ) :
        ae = self . assertEqual
        r = run
        s = rskel (
            { 'stateless' :
                { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } }
                , 'st2' : { 'proc' : { 'proc2' : { 'ops' : [ { 'call' :
                    [ 'st1_stateless_proc1' , 'a' ] } ] } } } } } )
        ae ( r ( s ) , s )
    def test_proc_trace ( self ) :
        ae = self . assertEqual
        r = run
        s = rskel (
            { 'trace' :
                { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } }
                , 'st2' : { 'proc' : { 'proc2' : { 'ops' : [ { 'call' :
                    [ 'st1_trace_proc1' , 'a' ] } ] } } } } } )
        ae ( r ( s ) , s )
    def test_proc_stateless_local ( self ) :
        ae = self . assertEqual
        r = run
        s = rskel (
            { 'stateless' :
                { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } } }
            , 'trace' :
                { 'st1' : { 'proc' : { 'proc2' : { 'ops' : [ { 'call' :
                    [ 'stateless_proc1' , 'a' ] } ] } } } } } )
        ae ( r ( s ) , s )
    def test_proc_trace_local ( self ) :
        ae = self . assertEqual
        r = run
        s = rskel (
            { 'trace' :
                { 'st1' : { 'proc' : { 'proc1' : { 'args' : [ { } ] } } } }
            , 'stateless' :
                { 'st1' : { 'proc' : { 'proc2' : { 'ops' : [ { 'call' :
                        [ 'trace_proc1' , 'a' ] } ] } } } } } )
        ae ( r ( s ) , s )
