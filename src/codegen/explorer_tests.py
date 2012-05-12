import unittest
from explorer import explorer
from normalizer . skeleton import run as rskel
from utils import merge , merge_exception
from fractions import Fraction

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
        gr = lambda x , p : explorer ( x ) . get_readables ( p )
        gp = lambda x , p : explorer ( x ) . get_passables ( p )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
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
        ae ( gr ( s , p ) , r )
        ae ( gp ( s , p ) , r )
        ae ( ir ( s , p , 'const1' ) , True )
        ae ( iw ( s , p , 'const1' ) , False )
        ae ( ip ( s , p , 'const1' ) , True )
    def test_get_global_consts ( self ) :
        g = lambda x : explorer ( x ) . get_global_consts ( )
        gc = lambda x , p : explorer ( x ) . get_consts ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        gr = lambda x , p : explorer ( x ) . get_readables ( p )
        gp = lambda x , p : explorer ( x ) . get_passables ( p )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
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
        ae ( gr ( s , p ) , r )
        ae ( gp ( s , p ) , r )
        ae ( ir ( s , p , 'group1_consts_const1' ) , True )
        ae ( iw ( s , p , 'group1_consts_const1' ) , False )
        ae ( ip ( s , p , 'group1_consts_const1' ) , True )
    def test_get_local_consts ( self ) :
        g = lambda x , p : explorer ( x ) . get_local_consts ( p )
        gc = lambda x , p : explorer ( x ) . get_consts ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        gr = lambda x , p : explorer ( x ) . get_readables ( p )
        gp = lambda x , p : explorer ( x ) . get_passables ( p )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
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
        ae ( gr ( s , p ) , r2 )
        ae ( gp ( s , p ) , r2 )
        ae ( ir ( s , p , 'consts_const1' ) , True )
        ae ( iw ( s , p , 'consts_const1' ) , False )
        ae ( ip ( s , p , 'consts_const1' ) , True )
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
        gr = lambda x , p : explorer ( x ) . get_readables ( p )
        gw = lambda x , p : explorer ( x ) . get_writables ( p )
        gp = lambda x , p : explorer ( x ) . get_passables ( p )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
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
        ae ( gr ( s , p ) , r )
        ae ( gw ( s , p ) , r )
        ae ( gp ( s , p ) , r )
        ae ( ir ( s , p , 'var1' ) , True )
        ae ( iw ( s , p , 'var1' ) , True )
        ae ( ip ( s , p , 'var1' ) , True )
    def test_get_local_values ( self ) :
        gv = lambda x , p : explorer ( x ) . get_values ( p )
        ge = lambda x , p : explorer ( x ) . get_everything ( p )
        gr = lambda x , p : explorer ( x ) . get_readables ( p )
        gw = lambda x , p : explorer ( x ) . get_writables ( p )
        gp = lambda x , p : explorer ( x ) . get_passables ( p )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
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
            ae ( gr ( s , p ) , r )
            ae ( gw ( s , p ) , r )
            ae ( gp ( s , p ) , r )
            ae ( ir ( s , p , 'var1' ) , True )
            ae ( iw ( s , p , 'var1' ) , True )
            ae ( ip ( s , p , 'var1' ) , True )
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
    def test_get_fields ( self ) :
        g = lambda x : explorer ( x ) . get_fields ( )
        p = [ 'somewhere' , 'faraway' ]
        s = mpath ( p ,
            { 'types' :
                { 'place1' : { 'type1' :
                    [ { 'test1' : { } }
                    , { 'test2' : { } } ] }
                , 'place3' : { 'type3' :
                    [ { 'test1' : { } } ] } } } )
        r = { 'test1' : [ 'place1_type_type1' , 'place3_type_type3' ]
            , 'test2' : [ 'place1_type_type1' ] }
        ae = self . assertEqual
        ae ( g ( s ) , r )
    def test_get_message_some_args ( self ) :
        gv = lambda x , p : explorer ( x ) . get_values ( p )
        gr = lambda x , p : explorer ( x ) . get_readables ( p )
        gp = lambda x , p : explorer ( x ) . get_passables ( p )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
        for some in ( 'request' , 'receive' ) :
            g = lambda x : getattr ( explorer ( x ) ,
                'get_message_%s_args' % some ) ( p )
            p = [ 'module' , 'module1' , some , 'msg1' , 'ops' ]
            s = mpath ( p ,
                { 'messages' :
                    { 'module1' : { some : { 'msg1' :
                        [ { 'arg1' : 'test1' }
                        , { 'arg2' : 'test2' } ] } } }
                , 'module' :
                    { 'module1' : { some : { 'msg1' :
                        { 'ops' : [ ] } } } } } )
            r = { 'msg_arg1' : 'test1'
                , 'msg_arg2' : 'test2' }
            ae = self . assertEqual
            ae ( g ( s ) , r )
            ae ( gv ( s , p ) , r )
            ae ( gr ( s , p ) , r )
            ae ( gp ( s , p ) , r )
            ae ( ir ( s , p , 'msg_arg1' ) , True )
            ae ( iw ( s , p , 'msg_arg1' ) , False )
            ae ( ip ( s , p , 'msg_arg1' ) , True )
    def test_get_message_reply_args ( self ) :
        g = lambda x : explorer ( x ) . get_message_reply_args ( p )
        gv = lambda x , p : explorer ( x ) . get_values ( p )
        gw = lambda x , p : explorer ( x ) . get_writables ( p )
        gp = lambda x , p : explorer ( x ) . get_passables ( p )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
        p = [ 'module' , 'module1' , 'request' , 'msg1' , 'ops' ]
        s = mpath ( p ,
            { 'messages' :
                { 'module1' : { 'reply' : { 'msg1' :
                    [ { 'arg1' : 'test1' }
                    , { 'arg2' : 'test2' } ] } } }
            , 'module' :
                { 'module1' : { 'request' : { 'msg1' :
                    { 'ops' : [ ] } } } } } )
        r = { 'reply_arg1' : 'test1'
            , 'reply_arg2' : 'test2' }
        ae = self . assertEqual
        ae ( g ( s ) , r )
        ae ( gv ( s , p ) , r )
        ae ( gw ( s , p ) , r )
        ae ( gp ( s , p ) , r )
        ae ( ir ( s , p , 'reply_arg1' ) , False )
        ae ( iw ( s , p , 'reply_arg1' ) , True )
        ae ( ip ( s , p , 'reply_arg1' ) , True )
    def test_split_value_fields ( self ) :
        sv = lambda x , p , v : explorer ( x ) . split_value_fields ( p , v )
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
        p = [ 'somewhere' , 'group1' ]
        s = mpath ( p ,
            { 'vars' : { 'group1' :
                [ { 'var1' : 'test1' }
                , { 'var1_2' : 'test1_2' }
                , { 'var3' : 'test3' }
                , { 'var3_field3' : 'test3_field3' } ] }
            , 'types' : { 'group1' :
                { 'type1' : [ { 'field1' : { } } ]
                , 'type1_2' : [ { 'field1_2' : { } } ]
                , 'type3' : [ { 'field3' : { } } ]
            } } } )
        ae = self . assertEqual
        ae ( sv ( s , p , 'var1' ) ,
            [ [ 'var1' ] ] )
        ae ( sv ( s , p , 'var1_2' ) ,
            [ [ 'var1_2' ] ] )
        ae ( sv ( s , p , 'var3_field3_field3' ) ,
            [ [ 'var3' , 'field3' , 'field3' ]
            , [ 'var3_field3' , 'field3' ] ] )
        ae ( sv ( s , p , 'var1_field1' ) ,
            [ [ 'var1' , 'field1' ] ] )
        ae ( sv ( s , p , 'var1_2_field1_2' ) ,
            [ [ 'var1_2' , 'field1_2' ] ] )
        ae ( sv ( s , p , 'var1_field1_field1' ) ,
            [ [ 'var1' , 'field1' , 'field1' ] ] )
        ae ( sv ( s , p , 'var1_field1_field1_2' ) ,
            [ [ 'var1' , 'field1' , 'field1_2' ] ] )
        ae ( sv ( s , p , 'var1_2_field1_2_field1_2' ) ,
            [ [ 'var1_2' , 'field1_2' , 'field1_2' ] ] )
        ae ( sv ( s , p , 'unknown' ) ,
            [ ] )
        ae ( sv ( s , p , 'var1_unknown' ) ,
            [ ] )
        ae ( sv ( s , p , 'var1_field1_unknown' ) ,
            [ ] )
        ae ( ir ( s , p , 'var1_field1' ) , True )
        ae ( iw ( s , p , 'var1_field1' ) , True )
        ae ( ip ( s , p , 'var1_field1' ) , True )
    def test_numbers_are_readable ( self ) :
        ir = lambda x , p , v : explorer ( x ) . is_readable ( p , v )
        iw = lambda x , p , v : explorer ( x ) . is_writable ( p , v )
        ip = lambda x , p , v : explorer ( x ) . is_passable ( p , v )
        p = [ 'anywhere' , 'anywhere' ]
        s = mpath ( p , { } )
        ae = self . assertEqual
        ae ( ir ( s , p , 1 ) , True )
        ae ( iw ( s , p , 1 ) , False )
        ae ( ip ( s , p , 1 ) , True )
        ae ( ir ( s , p , Fraction ( 1 , 2 ) ) , True )
        ae ( iw ( s , p , Fraction ( 1 , 2 ) ) , False )
        ae ( ip ( s , p , Fraction ( 1 , 2 ) ) , True )

if __name__ == '__main__' :
    unittest . main ( )
