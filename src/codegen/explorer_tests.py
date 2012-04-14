import unittest
from explorer import explorer
from normalizer . skeleton import run as rskel
from utils import merge , merge_exception

def mpath ( path , src ) :
    return rskel ( merge ( src ,
        { 'stateless' : { path [ 1 ] : { 'proc' : { } } }
        , 'trace'     : { path [ 1 ] : { 'proc' : { } } }
        , 'consts'    : { path [ 1 ] : { } }
        , 'vars'      : { path [ 1 ] : [ ] }
        , path [ 0 ]  : { path [ 1 ] : { 'proc' : { } } } } ) )

class explorer_test_case ( unittest . TestCase ) :
    def test_ambiguity ( self ) :
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'platform_consts' : { 'group1_consts_const1' : 'test1' }
            , 'consts' : { 'group1' : { 'const1' : 'test2' } } } )
        me = merge_exception
        ar = self . assertRaises
        ar ( me , ge , s , p )
    def test_get_some_procs ( self ) :
        gc = lambda x , p : explorer ( x ) . get_callables ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        for some in ( 'stateless' , 'trace' ) :
            g = lambda x : getattr ( explorer ( x ) ,
                                'get_%s_procs' % some ) ( )
            p = [ 'somewhere' , 'faraway' ]
            s = mpath ( p , 
                { some :
                    { 'st1' : { 'proc' :
                        { 'proc1' : { 'ops' : [ 'test1' ] } } }
                    , 'st2' : { 'proc' :
                        { 'proc2' : { 'ops' : [ 'test2' ] } } } } } )
            st1p1 = s [ some ] [ 'st1' ] [ 'proc' ] [ 'proc1' ]
            st2p2 = s [ some ] [ 'st2' ] [ 'proc' ] [ 'proc2' ]
            r = { 'st1_%s_proc1' % some : st1p1
                , 'st2_%s_proc2' % some : st2p2 }
            ae = self . assertEqual
            ae ( g ( s ) , r )
            ae ( gc ( s , p ) , r )
            ae ( ge ( s , p ) , r )
    def test_get_platform_procs ( self ) :
        g = lambda x : explorer ( x ) . get_platform_procs ( )
        gc = lambda x , p : explorer ( x ) . get_callables ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'platform_procs' :
                { 'proc1' : { 'args' : [ 'test1' ] }
                , 'proc2' : { 'args' : [ 'test2' ] } } } )
        r = { 'proc1' : { 'args' : [ 'test1' ] }
            , 'proc2' : { 'args' : [ 'test2' ] } }
        ae = self . assertEqual
        ae ( g ( s ) , r )
        ae ( gc ( s , p ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_messages_receives ( self ) :
        g = lambda x : explorer ( x ) . get_messages_receives ( )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
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
        g = lambda x , p : explorer ( x ) . get_local_procs ( p )
        gc = lambda x , p : explorer ( x ) . get_callables ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'somewhere' : { 'faraway' : { 'proc' :
                { 'proc1' : { 'ops' : [ 'test1' ] }
                , 'proc2' : { 'ops' : [ 'test2' ] } } } } } )
        p1 = s [ 'somewhere' ] [ 'faraway' ] [ 'proc' ] [ 'proc1' ]
        p2 = s [ 'somewhere' ] [ 'faraway' ] [ 'proc' ] [ 'proc2' ]
        r = { 'proc1' : p1
            , 'proc2' : p2 }
        ae = self . assertEqual
        ae ( g ( s , p ) , r )
        ae ( gc ( s , p ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_local_some_procs ( self ) :
        gc = lambda x , p : explorer ( x ) . get_callables ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        for some in ( 'stateless' , 'trace' ) :
            g = lambda x , p : getattr ( explorer ( x ) ,
                                    'get_local_%s_procs' % some ) ( p )
            p = [ 'somewhere' , 'group1' ]
            s1 = rskel (
                { some :
                    { 'group1' : { 'proc' :
                        { 'proc1' : { 'ops' : [ 'test1' ] } } }
                    , 'group2' : { 'proc' :
                        { 'proc2' : { 'ops' : [ 'test2' ] } } } } } )
            p1 = s1 [ some ] [ 'group1' ] [ 'proc' ] [ 'proc1' ]
            r1 = { '%s_proc1' % some : p1 }
            s2 = mpath ( p , s1 )
            g1p1 = s2 [ some ] [ 'group1' ] [ 'proc' ] [ 'proc1' ]
            g2p2 = s2 [ some ] [ 'group2' ] [ 'proc' ] [ 'proc2' ]
            r2 = merge ( r1 ,
                { 'group1_%s_proc1' % some : g1p1
                , 'group2_%s_proc2' % some : g2p2 } )
            ae = self . assertEqual
            ae ( g ( s1 , p ) , r1 )
            ae ( gc ( s2 , p ) , r2 )
            ae ( ge ( s2 , p ) , r2 )
    def test_get_platform_consts ( self ) :
        g = lambda x : explorer ( x ) . get_platform_consts ( )
        gc = lambda x , p : explorer ( x ) . get_consts ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
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
        g = lambda x : explorer ( x ) . get_global_consts ( )
        gc = lambda x , p : explorer ( x ) . get_consts ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
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
        g = lambda x , p : explorer ( x ) . get_local_consts ( p )
        gc = lambda x , p : explorer ( x ) . get_consts ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
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
    def test_get_local_consts_in_consts ( self ) :
        g = lambda x , p : explorer ( x ) . get_local_consts ( p )
        p = [ 'consts' , 'group1' ]
        s = rskel (
            { 'consts' : { 'group1' :
                { 'const1' : 'test1'
                , 'const2' : 'test2' } } } )
        r = { 'const1' : 'test1'
            , 'const2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s , p ) , r )
    def test_get_global_vars ( self ) :
        g = lambda x , p : explorer ( x ) . get_global_vars ( p )
        gv = lambda x , p : explorer ( x ) . get_values ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        p = [ 'somewhere' , 'group1' ]
        s = mpath ( p ,
            { 'vars' : { 'group1' :
                [ { 'var1' : 'test1' }
                , { 'var2' : 'test2' } ] } } )
        r = { 'var1' : 'test1'
            , 'var2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s , p ) , r )
        ae ( gv ( s , p ) , r )
        ae ( ge ( s , p ) , r )
    def test_get_local_values ( self ) :
        gv = lambda x , p : explorer ( x ) . get_values ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        for some in ( 'vars' , 'args' ) :
            g = lambda x , p : getattr ( explorer ( x ) ,
                                'get_local_%s' % some ) ( p )
            p = [ 'path1' , 'path2' , 'path3' , 'path4' ]
            s = mpath ( p ,
                { 'path1' : { 'path2' : { 'path3' :
                    { 'path4' : { }
                    , some :
                        [ { 'var1' : 'test1' }
                        , { 'var2' : 'test2' } ] } } } } )
            r = { 'var1' : 'test1'
                , 'var2' : 'test2' }
            ae = self . assertEqual
            ae ( g ( s , p ) , r )
            ae ( gv ( s , p ) , r )
            ae ( ge ( s , p ) , r )
    def test_get_types ( self ) :
        g = lambda x : explorer ( x ) . get_types ( )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'types' :
                { 'place1' : { 'type1' :
                    [ { 'test1' : { } }
                    , { 'test2' : { } } ] }
                , 'place3' : { 'type3' :
                    [ { 'test3' : { } } ] } } } )
        r = { 'place1_type_type1' :
                { 'test1' : { }
                , 'test2' : { } }
            , 'place3_type_type3' :
                { 'test3' : { } } }
        ae = self . assertEqual
        ae ( g ( s ) , r )

if __name__ == '__main__' :
    unittest . main ( )
