import normalizer
import unittest

class call_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raise ( self ) :
        ar = self . assertRaises
        r = self . n . run
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ { } , { } ] )
        ar ( ne , r , { 'stateless' : { 'st1' : { 'proc1' : { 'ops' :
            [ { 'call' : [ 'func1' , 'a1' ] } ] } } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        bf = self . n . bind_func
        ne = normalizer . exception
        bf ( 'func1' , [ { } , { } ] )
        try :
            r ( { 'stateless' : { 'st1' : { 'proc1' : { 'ops' :
                [ { 'call' : [ 'func1' , 'a1' ] } ] } } } } )
        except ne as e :
            pass
        gp = e . get_path ( )
        ae ( gp , [ 'stateless' , 'st1' , 'proc1' , 'ops' , 0 ] )
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
