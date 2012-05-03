from normalizer . assigns_check import run
from normalizer . exception import exception
from normalizer . skeleton import run as rskel
import unittest

class assigns_check_test_case ( unittest . TestCase ) :
    def test_exception_args ( self ) :
        r = run
        ne = exception
        s = rskel (
            { 'platform_consts' : { 'const1' : 1 }
            , 'path1' : { 'path2' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'var1' ]
                    , 'to' : [ 'const1' ]
                    } } ] } } } )
        try :
            r ( s )
        except ne as e :
            pass
        ae = self . assertEqual
        ae ( e . get_src ( ) , s )
        ae ( e . get_path ( ) , [ 'path1' , 'path2' , 'ops' , 0 ] )
    def test_assign_to_const ( self ) :
        r = run
        ne = exception
        ar = self . assertRaises
        ar ( ne , r , rskel (
            { 'platform_consts' : { 'const1' : 1 }
            , 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'var1' ]
                    , 'to' : [ 'const1' ]
                    } } ] } } } ) )
    def test_assign_from_const ( self ) :
        r = run
        s = rskel (
            { 'platform_consts' : { 'const1' : 1 }
            , 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'const1' ]
                    , 'to' : [ 'var1' ]
                    } } ] } } } )
        ae = self . assertEqual
        ae ( r ( s ) , s )
    def test_assign_from_value_to_value ( self ) :
        r = run
        s = rskel (
            { 'types' : { 'group1' :
                { 'type1' : [ { 'field1' : { } } ] } }
            , 'anywhere' : { 'group1' :
                { 'vars' :
                    [ { 'var1' : { } }
                    , { 'var2' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'var1_field1' ]
                    , 'to' : [ 'var2_field1' ]
                    } } ] } } } )
        ae = self . assertEqual
        ae ( r ( s ) , s )
    def test_assign_from_unknown ( self ) :
        r = run
        ne = exception
        ar = self . assertRaises
        ar ( ne , r , rskel (
            { 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'unknown' ]
                    , 'to' : [ 'var1' ]
                    } } ] } } } ) )
    def test_assign_to_unknown ( self ) :
        r = run
        ne = exception
        ar = self . assertRaises
        ar ( ne , r , rskel (
            { 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'var1' ]
                    , 'to' : [ 'unknown' ]
                    } } ] } } } ) )
