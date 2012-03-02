import unittest
import explorer
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class explorer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . e = explorer . explorer
    def test_get_some_procs ( self ) :
        for some in ( 'stateless' , 'trace' ) :
            g = lambda x : getattr ( self . e ( x ) ,
                                'get_%s_procs' % some ) ( )
            ae = self . assertEqual
            ae ( g ( mroot ( { some :
                { 'st1' : { 'proc' : { 'proc1' : 'test1' } }
                , 'st2' : { 'proc' : { 'proc2' : 'test2' } } } } ) ) ,
                { 'st1_%s_proc1' % some : 'test1'
                , 'st2_%s_proc2' % some : 'test2' } )
    def test_get_platform_procs ( self ) :
        g = lambda x : self . e ( x ) . get_platform_procs ( )
        ae = self . assertEqual
        ae ( g ( mroot ( { 'platform_procs' :
            { 'func1' : 'test1'
            , 'func2' : 'test2' } } ) ) ,
            { 'func1' : 'test1'
            , 'func2' : 'test2' } )
    def test_get_messages_receives ( self ) :
        g = lambda x : self . e ( x ) . get_messages_receives ( )
        ae = self . assertEqual
        ae ( g ( mroot ( { 'messages' :
            { 'group1' : { 'receive' : { 'msg1' : 'test1' } }
            , 'group2' : { 'receive' : { 'msg2' : 'test2' } } } } ) ) ,
            { 'group1_msg1' : 'test1'
            , 'group2_msg2' : 'test2' } )
    def test_get_local_procs ( self ) :
        g = lambda p , x : self . e ( x ) . get_local_procs ( p )
        ae = self . assertEqual
        ae ( g (
            [ 'somewhere' , 'faraway' ] , mroot (
            { 'somewhere' : { 'faraway' : { 'proc' :
            { 'proc1' : 'test1'
            , 'proc2' : 'test2' } } } } ) ) ,
            { 'proc1' : 'test1'
            , 'proc2' : 'test2' } )
    def test_get_local_some_procs ( self ) :
        for some in ( 'stateless' , 'trace' ) :
            g = lambda p , x : getattr ( self . e ( x ) ,
                                    'get_local_%s_procs' % some ) ( p )
            ae = self . assertEqual
            ae ( g (
                [ 'foo' , 'st1' ] , mroot (
                { some :
                    { 'st1' : { 'proc' : { 'proc1' : 'test1' } }
                    , 'st2' : { 'proc' : { 'proc2' : 'test2' } } } } ) ) ,
                { '%s_proc1' % some : 'test1' } )

if __name__ == '__main__' :
    unittest . main ( )
