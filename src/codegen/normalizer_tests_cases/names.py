import unittest
from normalizer . exception import exception
from normalizer . skeleton import run as rskel
from normalizer . names import run

class names_test_case ( unittest . TestCase ) :
    def test_exception_args ( self ) :
        s = rskel (
            { 'platform_procs' : { 'func1' : { } , 'test1_func1' : { } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'with' : { 'test1' : [ 'func1' ] } } ]
            } } } } } )
        r = run
        ne = exception
        try :
            r ( s )
        except ne as e :
            pass
        ae = self . assertEqual
        ae ( e . get_src ( ) , s )
        ae ( e . get_path ( ) , [ 'stateless' , 'st1' , 'proc' ,
            'proc1' , 'ops' , 0 , 'with' , 'test1' , 0 ] )
    def test_unknown_name ( self ) :
        r = run
        s = rskel ( 
            { 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'with' : { 'test1' : [ 'unknown' ] } } ]
            } } } } } )
        ae = self . assertEqual
        ae ( r ( s ) , s )
    def test_nested_with ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r ( rskel (
            { 'platform_procs' :
                { 'test1_test2_test3_func1' : { }
                , 'test1_test3_func2' : { }
                , 'test1_func3' : { }
                , 'test2_func4' : { } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                    [ { 'with' : { 'test1' : [ { 'anywhere' :
                        [ { 'with' : { 'test2' : [ { 'anywhere' :
                            [ { 'with' : { 'test3' :
                                [ 'func1' 
                                , 'func2'
                                , 'func3'
                                , 'func4'
            ] } } ] } ] } } ] } ] } } ] } } } } } ) ) , rskel (
            { 'platform_procs' :
                { 'test1_test2_test3_func1' : { }
                , 'test1_test3_func2' : { }
                , 'test1_func3' : { }
                , 'test2_func4' : { } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : { 'ops' :
                    [ { 'with' : { 'test1' : [ { 'anywhere' :
                        [ { 'with' : { 'test2' : [ { 'anywhere' :
                            [ { 'with' : { 'test3' :
                                [ 'test1_test2_test3_func1'
                                , 'test1_test3_func2'
                                , 'test1_func3'
                                , 'test2_func4'
            ] } } ] } ] } } ] } ] } } ] } } } } } ) )
    def test_fields ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r ( rskel (
            { 'types' :
                { 'type1' : [ { 'field1' : { } } ] }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' :
                    [ { 'with' : { 'var1' :
                        [ 'field1' 
            ] } } ] } } } } } ) ) , rskel (
            { 'types' :
                { 'type1' : [ { 'field1' : { } } ] }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' :
                    [ { 'with' : { 'var1' :
                        [ 'var1_field1' 
            ] } } ] } } } } } ) )
