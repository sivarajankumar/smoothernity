import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc
from normalizer_tests_cases . helper import merge_skeleton_messages as mmsg

class sends_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raise ( self ) :
        ar = self . assertRaises
        r = self . n . run_sends
        ne = normalizer . exception
        ar ( ne , r , mroot (
            { 'messages' : { 'test1' : mmsg ( { 'receive' :
                { 'msg1' : [ { } , { } ] } } ) }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : mproc (
                { 'ops' : [ { 'send' : [ 'test1_msg1' , 'a' ] } ]
            } ) } } } } ) )
        ar ( ne , r , mroot (
            { 'messages' : { 'test1' : mmsg ( { 'receive' :
                { 'msg1' : [ { } , { } ] } } ) }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : mproc (
                { 'ops' : [ { 'send' : [ 'unknown' , 'a' ] } ]
            } ) } } } } ) )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run_sends
        ne = normalizer . exception
        try :
            r ( mroot (
                { 'messages' : { 'test1' : mmsg ( { 'receive' :
                    { 'msg1' : [ { } , { } ] } } ) }
                , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : mproc (
                    { 'ops' : [ { 'if' : [ { 'any' : [ { 'send' :
                        [ 'test1_msg1' , 'a' ] } ] } ] } ] } ) } } } } ) )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'stateless' , 'st1' , 'proc' , 'proc1' ,
            'ops' , 0 , 'if' , 0 , 'any' , 0 ] )
    def test_split_args ( self ) :
        ae = self . assertEqual
        r = self . n . run_sends
        ae ( r ( mroot (
            { 'messages' : { 'test1' : mmsg (
                { 'receive' : { 'msg1' : [ { } , { } ] } } ) }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : mproc (
                { 'ops' : [ { 'send' :
                    [ 'test1_msg1' , 'a1' , 'a2' , 'a3' , 'a4' ] } ]
            } ) } } } } ) ) , mroot (
            { 'messages' : { 'test1' : mmsg (
                { 'receive' : { 'msg1' : [ { } , { } ] } } ) }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : mproc (
                { 'ops' :
                    [ { 'send' : [ 'test1_msg1' , 'a1' , 'a2' ] }
                    , { 'send' : [ 'test1_msg1' , 'a3' , 'a4' ] }
            ] } ) } } } } ) )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = self . n . run_sends
        s = mroot (
            { 'messages' : { 'test1' : mmsg (
                { 'receive' : { 'msg1' : [ ] } } ) }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : mproc (
                { 'ops' :
                    [ { 'send' : [ 'test1_msg1' ] } ]
            } ) } } } } )
        ae ( r ( s ) , s )
