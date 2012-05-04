from normalizer . args_split import run
from normalizer . skeleton import run as rskel
from normalizer . exception import exception
from explorer import explorer
import unittest

class args_split_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        ne = exception
        ar = self . assertRaises
        ar ( ne , r ,
            { 'func1' : [ { } , { } ] } ,
            { 'anywhere' : { 'split' : [ 'func1' ] } } )
        ar ( ne , r ,
            { 'func1' : [ { } , { } ] } ,
            { 'anywhere' : { 'split' : [ 'func1' , 'a' ] } } )
        ar ( ne , r ,
            { 'func1' : [ ] } ,
            { 'anywhere' : { 'split' : [ 'func1' , 'a' ] } } )
        ar ( ne , r , { } ,
            { 'anywhere' : { 'split' : [ 'unknown' , 'a' ] } } )
    def test_exception_args ( self ) :
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        s = { 'path1' : { 'path2' :
                { 'split' : [ 'func1' , 'a' ] } } }
        try :
            r ( { 'func1' : [ { } , { } ] } , s )
        except exception as e :
            pass
        ae = self . assertEqual
        ae ( e . get_path ( )  , [ 'path1' , 'path2' ] )
        ae ( e . get_src ( )  , s )
    def test_args_split ( self ) :
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        ae = self . assertEqual
        ae ( r (
            { 'func1' : [ { } , { } ] } ,
            { 'anywhere' : [ { 'split' :
                [ 'func1' , 'a1' , 'a2' , 'a3' , 'a4' ] } ] } ) ,
            { 'anywhere' :
                [ { 'split' : [ 'func1' , 'a1' , 'a2' ] }
                , { 'split' : [ 'func1' , 'a3' , 'a4' ] } ] } )
    def test_no_args ( self ) :
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        s = { 'anywhere' : { 'split' : [ 'func1' ] } }
        ae = self . assertEqual
        ae ( r ( { 'func1' : [ ] } , s ) , s )
    def test_path ( self ) :
        r = lambda x , y : run ( 'split' ,
                lambda n , p : x [ '-' . join ( p ) ] [ n ] , y )
        s = { 'path1' : { 'path2' : { 'split' : [ 'func1' ] } } }
        ae = self . assertEqual
        ae ( r ( { 'path1-path2' : { 'func1' : [ ] } } , s ) , s )
