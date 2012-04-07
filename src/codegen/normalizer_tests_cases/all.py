import unittest
from normalizer import run
from normalizer . skeleton import run as rskel

class all_test_case ( unittest . TestCase ) :
    def test_calls_after_names ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r (
            { 'platform_procs' : { 'test1_func1' : { 'args' : [ { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'with' : { 'test1' :
                    [ { 'call' : [ 'func1' , 'a1' , 'a2' ] } ]
            } } ] } } } } } ) , rskel (
            { 'platform_procs' : { 'test1_func1' : { 'args' : [ { } ] } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'call' : [ 'test1_func1' , 'a1' ] }
                , { 'call' : [ 'test1_func1' , 'a2' ] } ]
            } } } } } ) )
    def test_sends_after_names ( self ) :
        pass
    def test_assigns ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r ( 
            { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' ]
                    , 'to' : [ 'a2' , 'a3' ]
            } } ] } } } } } ) , rskel (
            { 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'ops' :
                    [ { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a2' ] } }
                    , { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a3' ] } }
            ] } } } } } ) )
    def test_consts ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r (
            { 'consts' : { 'consts1' : { 'test1' : '[ 1 ]' } } } ) , rskel (
            { 'consts' : { 'consts1' : { 'test1' : 1 } } } ) )
