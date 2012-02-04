import normalizer
import unittest

class call_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_split ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        bf ( 'func1' , [ { } , { } ] )
        ae ( r ( { 'stateless' : { 'st1' : { 'proc1' : { 'ops' :
            [ { 'call' : [ 'func1' , 'a1' , 'a2' , 'a3' , 'a4' ] }
            ] } } } } ) ,
            { 'stateless' : { 'st1' : { 'proc1' : { 'ops' :
            [ { 'call' : [ 'func1' , 'a1' , 'a2' ] }
            , { 'call' : [ 'func1' , 'a3' , 'a4' ] }
            ] } } } } )
            
