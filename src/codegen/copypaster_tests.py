import unittest
import copypaster
import io
import indenter
import formatter

class copypaster_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . c = copypaster . copypaster ( )
        self . i = indenter . indenter ( )
        self . f = formatter . formatter ( )
        for o in ( self . i , self . f ) :
            o . set_indent_token ( 'indent' )
            o . set_dedent_token ( 'dedent' )
            o . set_newline_token ( '\n' )
    def cp ( self , s ) :
        indented = self . i . run ( io . StringIO ( s ) . readlines ( ) )
        copypasted = self . c . run ( io . StringIO ( indented ) )
        return self . f . run ( copypasted )
    def test_empty ( self ) :
        ae = self . assertEqual
        c = self . cp
        ae ( c ( '' ) , '' )
        ae ( c ( ' ' ) , '' )
        ae ( c ( '\n' ) , '' )
        ae ( c ( '\r\n' ) , '' )
    def test_no_copy ( self ) :
        ae = self . assertEqual
        c = self . cp
        ae ( c ( 'test1 test2\n test3\ntest4\n' ) ,
            'test1 test2\n test3\ntest4\n' )

if __name__ == '__main__' :
    unittest . main ( )
