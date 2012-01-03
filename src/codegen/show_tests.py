import unittest
import show

class show_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . s = show . show ( )
        self . s . set_context ( 3 )
        self . s . set_source ( [ 1 , 22 , 333 , 4444 , 55555 ] )
    def test_context_line ( self ) :
        cl = self . s . context_line
        self . assertEqual ( cl ( 0 ) ,
            [ '1'
            , '^'
            , '22'
            , '333' ] )
        self . assertEqual ( cl ( 3 ) ,
            [ '22'
            , '333'
            , '4444'
            , '^^^^' ] )
        self . assertEqual ( cl ( 4 ) ,
            [ '333'
            , '4444'
            , '55555'
            , '^^^^^' ] )
        ar = self . assertRaises
        ar ( show . line_exception , cl , - 1 )
        ar ( show . line_exception , cl , 5 )
        ar ( show . line_exception , cl , 10 )

if __name__ == '__main__' :
    unittest . main ( )
