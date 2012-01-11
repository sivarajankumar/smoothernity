import indenter
import unittest

class indenter_tests ( unittest . TestCase ) :
    def setUp ( self ) :
        self . i = indenter . indenter ( )
        self . i . set_indent_token ( 'indent' )
        self . i . set_dedent_token ( 'dedent' )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ ] ) , '' )
        ae ( r ( [ '' ] ) , '' )
        ae ( r ( [ '' , '' ] ) , '' )
        ae ( r ( [ '\n' , '\r' ] ) , '' )
    def test_no_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , 'test2' ] ) , 'test1 test2' )
    def test_trailing_strip ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1  ' , 'test2\r' , 'test3\n' , 'test4\r\n' ] ) ,
            'test1 test2 test3 test4' )
    def test_single_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , ' test2' ] ) ,
            'test1 indent test2 dedent' )
        ae ( r ( [ 'test1 test2' , ' test3 test4' ] ) ,
            'test1 test2 indent test3 test4 dedent' )
        ae ( r ( [ '  test1' , '  test2' ] ) ,
            'indent test1 test2 dedent' )
    def test_same_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , ' test2' , ' test3' ] ) ,
            'test1 indent test2 test3 dedent' )
    def test_multi_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , ' test2' , '  test3' ] ) ,
            'test1 indent test2 indent test3 dedent dedent' )
    def test_different_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , '  test2' , ' test3' ] ) ,
            'test1 indent test2 dedent indent test3 dedent' )

if __name__ == '__main__' :
    unittest . main ( )
