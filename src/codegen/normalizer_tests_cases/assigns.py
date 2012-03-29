from normalizer . assigns import run
from normalizer . exception import exception
import unittest

class assigns_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        r = run
        ne = exception
        ar = self . assertRaises
        ar ( ne , r , { 'anywhere' : { 'anywhere' :
            { 'ops' : [ { 'assign' :
                { 'from' : [ 'a1' , 'a2' ]
                , 'to' : [ 'a3' , 'a4' , 'a5' ]
                } } ] } } } )
    def test_exception_args ( self ) :
        r = run
        ne = exception
        s = { 'path1' : { 'path2' :
                { 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' , 'a2' ]
                    , 'to' : [ 'a3' , 'a4' , 'a5' ] } } ] } } }
        try :
            r ( s )
        except ne as e :
            pass
        ae = self . assertEqual
        ae ( e . get_src ( ) , s )
        ae ( e . get_path ( ) , [ 'path1' , 'path2' , 'ops' , 0 ] )
    def test_split ( self ) :
        r = run
        ae = self . assertEqual
        ae ( r (
            { 'anywhere' : { 'anywhere' :
                { 'ops' : [ { 'assign' :
                    { 'from' : [ 'a1' , 'a2' ]
                    , 'to' : [ 'a3' , 'a4' , 'a5' , 'a6' ]
                    } } ] } } } ) ,
            { 'anywhere' : { 'anywhere' :
                { 'ops' : 
                    [ { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a3' ] } }
                    , { 'assign' : { 'from' : [ 'a2' ] , 'to' : [ 'a4' ] } }
                    , { 'assign' : { 'from' : [ 'a1' ] , 'to' : [ 'a5' ] } }
                    , { 'assign' : { 'from' : [ 'a2' ] , 'to' : [ 'a6' ] } }
                    ] } } } )
