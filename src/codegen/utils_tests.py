import unittest
import utils

class merge_test_case ( unittest . TestCase ) :
    def test_empty ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { } , { } ) , { } )
        ae ( m ( [ ] , [ ] ) , [ ] )
    def test_value ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { } , [ ] ) , [ ] )
        ae ( m ( 1 , 2 ) , 2 )
        ae ( m ( 'test1' , 'test2' ) , 'test2' )
    def test_deepcopy ( self ) :
        ane = self . assertNotEqual
        m = utils . merge
        a , b = { } , [ ]
        ane ( id ( m ( a , b ) ) , id ( b ) )
        ane ( id ( m ( a , a ) ) , id ( a ) )
        ane ( id ( m ( b , b ) ) , id ( b ) )
    def test_lists ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( [ 1 ] , [ 2 , 3 ] ) , [ 1 , 2 , 3 ] )
    def test_dicts ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { 1 : 2 } , { 3 : 4 } ) , { 1 : 2 , 3 : 4 } )
        ae ( m ( { 1 : 2 } , { 1 : 3 } ) , { 1 : 3 } )
    def test_dict_of_lists ( self ) :
        ae = self . assertEqual
        m = utils . merge
        ae ( m ( { 1 : [ 2 ] } , { 1 : [ 3 ] } ) , { 1 : [ 2 , 3 ] } )

if __name__ == '__main__' :
    unittest . main ( )
