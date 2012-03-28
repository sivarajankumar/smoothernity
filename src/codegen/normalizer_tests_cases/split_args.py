from normalizer . split_args import run
from normalizer . skeleton import run as rskel
from normalizer . exception import exception
from explorer import explorer
import unittest

class split_args_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        ar = self . assertRaises
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        ne = exception
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
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        ne = exception
        try :
            r ( { 'func1' : [ { } , { } ] } ,
                { 'path1' : { 'path2' :
                    { 'split' : [ 'func1' , 'a' ] } } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'path1' , 'path2' ] )
    def test_split_args ( self ) :
        ae = self . assertEqual
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        ae ( r (
            { 'func1' : [ { } , { } ] } ,
            { 'anywhere' : [ { 'split' :
                [ 'func1' , 'a1' , 'a2' , 'a3' , 'a4' ] } ] } ) ,
            { 'anywhere' :
                [ { 'split' : [ 'func1' , 'a1' , 'a2' ] }
                , { 'split' : [ 'func1' , 'a3' , 'a4' ] } ] } )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = lambda x , y : run ( 'split' , lambda n , p : x [ n ] , y )
        s = { 'anywhere' : { 'split' : [ 'func1' ] } }
        ae ( r ( { 'func1' : [ ] } , s ) , s )
