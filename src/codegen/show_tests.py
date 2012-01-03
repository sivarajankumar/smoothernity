import unittest
import show

class show_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . s = show . show ( )
        self . s . set_context ( 3 )
        self . s . set_source ( [ 1 , 22 , 333 , 4444 , 55555 ] )
    def test_context_line_first ( self ) :
        c = self . s . context_line
        ae = self . assertEqual
        ae ( c ( 0 ) , [ '1' , '^' , '22' , '333' ] )
    def test_context_line_middle ( self ) :
        c = self . s . context_line
        ae = self . assertEqual
        ae ( c ( 3 ) , [ '22' , '333' , '4444' , '^^^^' ] )
    def test_context_line_last ( self ) :
        c = self . s . context_line
        ae = self . assertEqual
        ae ( c ( 4 ) , [ '333' , '4444' , '55555' , '^^^^^' ] )
    def test_context_line_raises ( self ) :
        c = self . s . context_line
        ar = self . assertRaises
        ar ( show . line_exception , c , - 1 )
        ar ( show . line_exception , c , 5 )
        ar ( show . line_exception , c , 10 )
    def test_context_line_col ( self ) :
        c = self . s . context_line_col
        ae = self . assertEqual
        ae ( c ( 3 , 2 ) , [ '22' , '333' , '4444' , '  ^' ] )
    def test_context_line_col_raises ( self ) :
        c = self . s . context_line_col
        ar = self . assertRaises
        ar ( show . line_col_exception , c , 3 , - 1 )
        ar ( show . line_col_exception , c , 3 , 4 )
        ar ( show . line_col_exception , c , 3 , 10 )

if __name__ == '__main__' :
    unittest . main ( )
