import unittest
import formatter

class formatter_tests ( unittest . TestCase ) :
    def setUp ( self ) :
        self . f = formatter . formatter ( )
        self . f . set_indent_token ( 'indent' )
        self . f . set_dedent_token ( 'dedent' )
        self . f . set_newline_token ( '\n' )
    def test_empty ( self ) :
        ae = self . assertEqual
        u = self . f . run
        ae ( u ( [ ] ) , '' )
    def test_one_line ( self ) :
        ae = self . assertEqual
        u = self . f . run
        ae ( u ( [ 'test1' , 'test2' ] ) , 'test1 test2' )
    def test_newline ( self ) :
        ae = self . assertEqual
        u = self . f . run
        ae ( u ( [ 'test1' , '\n' , 'test2' ] ) , 'test1\ntest2' )
        ae ( u ( [ 'test1' , '\n' , '\n' , 'test2' , '\n' , '\n' ] ) , 'test1\ntest2\n' )

if __name__ == '__main__' :
    unittest . main ( )
