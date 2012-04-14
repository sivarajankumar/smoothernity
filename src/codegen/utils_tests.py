import unittest
import utils

class merge_test_case ( unittest . TestCase ) :
    def test_no_overwrite ( self ) :
        ae = self . assertEqual
        me = utils . merge_exception
        m = lambda x , y : utils . merge ( x , y , overwrite = False )
        try :
            m ( { 'test1' : 1
                , 'test2' : 1
                , 'first' : 1 } ,
                { 'test1' : 1
                , 'test2' : 1
                , 'second' : 1 } )
            self . fail ( )
        except me as e :
            ae ( e . get_keys ( ) , [ 'test1' , 'test2' ] )
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

class rewrite_test_case ( unittest . TestCase ) :
    def test_value ( self ) :
        ae = self . assertEqual
        r = lambda x : utils . rewrite ( x , lambda a , b : a )
        ae ( r ( 'test1' ) , 'test1' )
        ae ( r ( 123 ) , 123 )
    def test_list_flatten ( self ) :
        ae = self . assertEqual
        r = lambda x : utils . rewrite ( x , lambda a , b : a )
        ae ( r ( [ 1 , [ 2 , [ 3 ] ] ] ) , [ 1 , 2 , 3 ] )
    def test_dict ( self ) :
        ae = self . assertEqual
        r = lambda x : utils . rewrite ( x ,
            lambda a , b : ( 'path' , b ) if type ( a ) is str else a )
        ae ( r (
            { 'test1' : 'test2'
            , 'test3' : { 'test4' : 'test5' } } ) ,
            { 'test1' : ( 'path' , [ 'test1' ] )
            , 'test3' : { 'test4' : ( 'path' , [ 'test3' , 'test4' ] ) } } )
    def test_list ( self ) :
        ae = self . assertEqual
        r = lambda x : utils . rewrite ( x ,
            lambda a , b : ( 'path' , b ) if type ( a ) is str else a )
        ae ( r (
            [ { 'test1' :
                [ 'test2'
                , 'test3' ] }
            , 'test4' ] ) ,
            [ { 'test1' :
                [ ( 'path' , [ 0 , 'test1' , 0 ] ) 
                , ( 'path' , [ 0 , 'test1' , 1 ] ) ] }
            , ( 'path' , [ 1 ] ) ] )

class utils_test_case ( unittest . TestCase ) :
    def test_is_text ( self ) :
        at = self . assertTrue
        af = self . assertFalse
        t = utils . is_text
        at ( t ( 'test' ) )
        at ( t ( u'test' ) )
        af ( t ( 123 ) )

if __name__ == '__main__' :
    unittest . main ( )
