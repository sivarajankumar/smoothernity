import unittest
from normalizer import run
from normalizer . exception import exception
from normalizer . skeleton import run as rskel

class all_test_case ( unittest . TestCase ) :
    def test_calls_after_names ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r (
            { 'platform_procs' : { 'test1_func1' : { 'args' : [ { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } } ]
                , 'ops' :
                    [ { 'with' : { 'test1' :
                        [ { 'call' : [ 'func1' , 'a1' , 'a2' ] } ]
            } } ] } } } } } ) , rskel (
            { 'platform_procs' : { 'test1_func1' : { 'args' : [ { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } } ]
                , 'ops' :
                    [ { 'call' : [ 'test1_func1' , 'a1' ] }
                    , { 'call' : [ 'test1_func1' , 'a2' ] } ]
            } } } } } ) )
    def test_sends_after_names ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r (
            { 'messages' : { 'test1' : 
                { 'receive' : { 'msg1' : [ { } ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } } ]
                , 'ops' :
                    [ { 'with' : { 'test1' :
                        [ { 'send' : [ 'msg1' , 'a1' , 'a2' ] } ]
            } } ] } } } } } ) , rskel (
            { 'messages' : { 'test1' : 
                { 'receive' : { 'msg1' : [ { } ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } } ]
                , 'ops' :
                    [ { 'send' : [ 'test1_msg1' , 'a1' ] }
                    , { 'send' : [ 'test1_msg1' , 'a2' ] } ]
            } } } } } ) )
    def test_assigns ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r ( 
            { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } } , { 'a3' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' ]
                    , 'to' : [ 'a2' , 'a3' ]
            } } ] } } } } } ) , rskel (
            { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'a1' : { } } , { 'a2' : { } } , { 'a3' : { } } ]
                , 'ops' :
                    [ { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a2' ] } }
                    , { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a3' ] } }
            ] } } } } } ) )
    def test_assigns_check ( self ) :
        r = run
        ne = exception
        ar = self . assertRaises
        ar ( ne , r , 
            { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' ]
                    , 'to' : [ 'a2' ]
            } } ] } } } } } )
    def test_calls_check ( self ) :
        r = run
        ne = exception
        ar = self . assertRaises
        ar ( ne , r , 
            { 'platform_procs' : { 'test1_func1' : { 'args' : [ { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'with' : { 'test1' :
                    [ { 'call' : [ 'func1' , 'unknown' ] } ]
            } } ] } } } } } )
    def test_consts ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r (
            { 'consts' : { 'consts1' : { 'test1' : '[ 1 ]' } } } ) , rskel (
            { 'consts' : { 'consts1' : { 'test1' : 1 } } } ) )
