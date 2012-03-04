import unittest
import explorer
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from utils import merge

def mpath ( path , src ) :
    return mroot ( merge ( src ,
        { 'stateless' : { path [ 1 ] : { 'proc' : { } } }
        , 'trace'     : { path [ 1 ] : { 'proc' : { } } }
        , 'consts'    : { path [ 1 ] : { } }
        , path [ 0 ]  : { path [ 1 ] : { 'proc' : { } } } } ) )

class explorer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . e = explorer . explorer
    def test_get_some_procs ( self ) :
        gc = lambda x , p : self . e ( x ) . get_callables ( p )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        for some in ( 'stateless' , 'trace' ) :
            g = lambda x : getattr ( self . e ( x ) ,
                                'get_%s_procs' % some ) ( )
            p = [ 'somewhere' , 'faraway' ]
            s = mpath ( p , 
                { some :
                    { 'st1' : { 'proc' : { 'proc1' : 'test1' } }
                    , 'st2' : { 'proc' : { 'proc2' : 'test2' } } } } )
            r = { 'st1_%s_proc1' % some : 'test1'
                , 'st2_%s_proc2' % some : 'test2' }
            ae = self . assertEqual
            ae ( g ( s ) , r )
            ae ( gc ( s , p ) , r )
            ae ( ge ( s , p ) , r )
    def test_get_platform_procs ( self ) :
        g = lambda x : self . e ( x ) . get_platform_procs ( )
        gc = lambda x , p : self . e ( x ) . get_callables ( p )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'platform_procs' :
                { 'proc1' : 'test1'
                , 'proc2' : 'test2' } } )
        r = { 'proc1' : 'test1'
            , 'proc2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s ) , r )
        ae ( gc ( s , p ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_messages_receives ( self ) :
        g = lambda x : self . e ( x ) . get_messages_receives ( )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'messages' :
                { 'group1' : { 'receive' : { 'msg1' : 'test1' } }
                , 'group2' : { 'receive' : { 'msg2' : 'test2' } } } } )
        r = { 'group1_msg1' : 'test1'
            , 'group2_msg2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_local_procs ( self ) :
        g = lambda x , p : self . e ( x ) . get_local_procs ( p )
        gc = lambda x , p : self . e ( x ) . get_callables ( p )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'somewhere' : { 'faraway' : { 'proc' :
                { 'proc1' : 'test1'
                , 'proc2' : 'test2' } } } } )
        r = { 'proc1' : 'test1'
            , 'proc2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s , p ) , r )
        ae ( gc ( s , p ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_local_some_procs ( self ) :
        gc = lambda x , p : self . e ( x ) . get_callables ( p )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        for some in ( 'stateless' , 'trace' ) :
            g = lambda x , p : getattr ( self . e ( x ) ,
                                    'get_local_%s_procs' % some ) ( p )
            p = [ 'somewhere' , 'group1' ]
            s1 = mroot (
                { some :
                    { 'group1' : { 'proc' : { 'proc1' : 'test1' } }
                    , 'group2' : { 'proc' : { 'proc2' : 'test2' } } } } )
            r1 = { '%s_proc1' % some : 'test1' }
            s2 = mpath ( p , s1 )
            r2 = merge ( r1 ,
                { 'group1_%s_proc1' % some : 'test1'
                , 'group2_%s_proc2' % some : 'test2' } )
            ae = self . assertEqual
            ae ( g ( s1 , p ) , r1 )
            ae ( gc ( s2 , p ) , r2 )
            ae ( ge ( s2 , p ) , r2 )
    def test_get_platform_consts ( self ) :
        g = lambda x : self . e ( x ) . get_platform_consts ( )
        gc = lambda x , p : self . e ( x ) . get_consts ( p )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'platform_consts' :
                { 'const1' : 'test1'
                , 'const2' : 'test2' } } )
        r = { 'const1' : 'test1'
            , 'const2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s ) , r )
        ae ( gc ( s , p ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_global_consts ( self ) :
        g = lambda x : self . e ( x ) . get_global_consts ( )
        gc = lambda x , p : self . e ( x ) . get_consts ( p )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'consts' :
                { 'group1' : { 'const1' : 'test1' }
                , 'group2' : { 'const2' : 'test2' } } } )
        r = { 'group1_consts_const1' : 'test1'
            , 'group2_consts_const2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s ) , r )
        ae ( gc ( s , p ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_local_consts ( self ) :
        g = lambda x , p : self . e ( x ) . get_local_consts ( p )
        gc = lambda x , p : self . e ( x ) . get_consts ( p )
        ge = lambda x , p : self . e ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'group1' ]
        s = mpath ( p ,
            { 'consts' : { 'group1' :
                { 'const1' : 'test1'
                , 'const2' : 'test2' } } } )
        r1 = \
            { 'consts_const1' : 'test1'
            , 'consts_const2' : 'test2' }
        r2 = merge ( r1 ,
            { 'group1_consts_const1' : 'test1'
            , 'group1_consts_const2' : 'test2' } )
        ae = self . assertEqual
        ae ( g ( s , p ) , r1 )
        ae ( gc ( s , p ) , r2 )
        ae ( ge ( s , p ) , r2 )

if __name__ == '__main__' :
    unittest . main ( )
