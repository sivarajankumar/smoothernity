import normalizer
import unittest

class consts_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_number ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : 1 } } } ) ,
            { 'messages' : { } , 'types' : { } , 'stateless' : { }
            , 'vars' : { } , 'module' : { } , 'trace' : { } 
            , 'consts' : { 'test1' : { 'test2' : 1 } } } )
    def test_expression ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 ]' } } } ) ,
            { 'messages' : { } , 'types' : { } , 'stateless' : { }
            , 'vars' : { } , 'module' : { } , 'trace' : { } 
            , 'consts' : { 'test1' : { 'test2' : 1 } } } )
