import unittest
import explorer
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from utils import merge

class explorer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . e = explorer . explorer
    def test_get_some_procs ( self ) :
        gc = lambda x , p : self . e ( x ) . get_callables ( p )
        for some in ( 'stateless' , 'trace' ) :
            g = lambda x : getattr ( self . e ( x ) ,
                                'get_%s_procs' % some ) ( )
            s = mroot (
                { some :
                    { 'st1' : { 'proc' : { 'proc1' : 'test1' } }
                    , 'st2' : { 'proc' : { 'proc2' : 'test2' } } }
                , 'somewhere' :
                    { 'faraway' : { 'proc' : { } } }
                } )
            r = { 'st1_%s_proc1' % some : 'test1'
                , 'st2_%s_proc2' % some : 'test2' }
            ae = self . assertEqual
            ae ( g ( s ) , r )
            ae ( gc ( s , [ 'somewhere' , 'faraway' ] ) , r )
    def test_get_platform_procs ( self ) :
        g = lambda x : self . e ( x ) . get_platform_procs ( )
        gc = lambda x , p : self . e ( x ) . get_callables ( p )
        s = mroot (
            { 'platform_procs' :
                { 'func1' : 'test1'
                , 'func2' : 'test2' }
            , 'somewhere' :
                { 'faraway' : { 'proc' : { } } }
            } )
        r = { 'func1' : 'test1'
            , 'func2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s ) , r )
        ae ( gc ( s , [ 'somewhere' , 'faraway' ] ) , r )
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
        gc = lambda p , x : self . e ( x ) . get_callables ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mroot (
            { 'somewhere' : { 'faraway' : { 'proc' :
            { 'proc1' : 'test1'
            , 'proc2' : 'test2' } } } } )
        r = { 'proc1' : 'test1'
            , 'proc2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( p , s ) , r )
        ae ( gc ( p , s ) , r )
    def test_get_local_some_procs ( self ) :
        gc = lambda p , x : self . e ( x ) . get_callables ( p )
        for some in ( 'stateless' , 'trace' ) :
            g = lambda p , x : getattr ( self . e ( x ) ,
                                    'get_local_%s_procs' % some ) ( p )
            p = [ 'foo' , 'group1' ]
            s = mroot (
                { some :
                    { 'group1' : { 'proc' : { 'proc1' : 'test1' } }
                    , 'group2' : { 'proc' : { 'proc2' : 'test2' } } } } )
            r = { '%s_proc1' % some : 'test1' }
            ae = self . assertEqual
            ae ( g ( p , s ) , r )
            ae ( gc ( p , s ) , r )

if __name__ == '__main__' :
    unittest . main ( )
