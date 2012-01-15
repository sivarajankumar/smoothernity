import unittest
import copypaster
import io
import indenter

class copypaster_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . c = copypaster . copypaster ( )
        self . i = indenter . indenter ( )
        self . i . set_indent_token ( 'indent' )
        self . i . set_dedent_token ( 'dedent' )
        self . i . set_newline_token ( '\n' )
    def cp ( self , s ) :
        indented = self . i . run ( io . StringIO ( s ) . readlines ( ) )
        return self . c . copypaste ( io . StringIO ( indented ) )
    def test_empty ( self ) :
        ae = self . assertEqual
        c = self . cp
        ae ( c ( '' ) , [ ] )
        ae ( c ( ' ' ) , [ ] )
        ae ( c ( '\n' ) , [ ] )
        ae ( c ( '\r\n' ) , [ ] )

if __name__ == '__main__' :
    unittest . main ( )
