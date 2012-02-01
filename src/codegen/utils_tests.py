import unittest
import utils

class merge_test_case ( unittest . TestCase ) :
    def test_raises ( self ) :
        ar = self . assertRaises
        m = utils . merge
        ue = utils . exception
        ar ( ue , m , { } , [ ] )
        ar ( ue , m , 1 , 2 )
        ar ( ue , m , 'test1' , 'test2' )
    def test_empty ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { } ) , { } )
        ae ( m ( { } , { } ) , { } )
        ae ( m ( { } , { } , { } ) , { } )
        ae ( m ( [ ] , [ ] , [ ] ) , [ ] )
    def test_value ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( None ) , None )
        ae ( m ( 1 ) , 1 )
        ae ( m ( 'test' ) , 'test' )
    def test_lists ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( [ 1 ] , [ 2 , 3 ] ) , [ 1 , 2 , 3 ] )
    def test_dicts ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { 1 : 2 } , { 3 : 4 } ) , { 1 : 2 , 3 : 4 } )
    def test_dict_of_lists ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { 1 : [ 2 ] } , { 1 : [ 3 ] } ) , { 1 : [ 2 , 3 ] } )

if __name__ == '__main__' :
    unittest . main ( )
