import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc
from normalizer_tests_cases . helper import merge_skeleton_messages as mmsg

class send_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raise ( self ) :
        ar = self . assertRaises
        r = self . n . run
        ne = normalizer . exception
        ar ( ne , r ,
            { 'messages' : { 'test1' : { 'receive' :
                { 'msg1' : [ { } , { } ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'test1_msg1' , 'a1' ] } ] } } } } } )
        ar ( ne , r ,
            { 'messages' : { 'test1' : { 'receive' :
                { 'msg1' : [ { } , { } ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'unknown' , 'a1' ] } ] } } } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ne = normalizer . exception
        try :
            r ( { 'messages' : { 'test1' : { 'receive' :
                    { 'msg1' : [ { } , { } ] } } }
                , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                    [ { 'if' : [ { 'any' : [ { 'send' :
                        [ 'test1_msg1' , 'a1' ] } ] } ] } ] } } } } } )
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
        ae ( r (
            { 'messages' : { 'test1' : { 'receive' :
                { 'msg1' : [ { } , { } ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'test1_msg1' , 'a1' , 'a2' , 'a3' , 'a4' ] } ]
            } } } } } ) ,
            mroot (
                { 'messages' : { 'test1' : mmsg (
                    { 'receive' : { 'msg1' : [ { } , { } ] } } ) }
                , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                    mproc ( { 'ops' :
                        [ { 'send' : [ 'test1_msg1' , 'a1' , 'a2' ] }
                        , { 'send' : [ 'test1_msg1' , 'a3' , 'a4' ] }
                ] } ) } } } } ) )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r (
            { 'messages' : { 'test1' : { 'receive' : { 'msg1' : [ ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'test1_msg1' ] } ]
            } } } } } ) ,
            mroot (
                { 'messages' : { 'test1' : mmsg (
                    { 'receive' : { 'msg1' : [ { } , { } ] } } ) }
                , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                    mproc ( { 'ops' :
                        [ { 'send' : [ 'test1_msg1' ] }
                ] } ) } } } } ) )
