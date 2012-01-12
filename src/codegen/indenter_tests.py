import indenter
import unittest

class indenter_tests ( unittest . TestCase ) :
    def setUp ( self ) :
        self . i = indenter . indenter ( )
        self . i . set_indent_token ( 'indent' )
        self . i . set_dedent_token ( 'dedent' )
        self . i . set_newline_token ( '\n' )
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
        ae ( r ( [ 'test1' , 'test2' ] ) , 'test1\ntest2\n' )
    def test_trailing_strip ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1  ' , 'test2\r' , 'test3\n' , 'test4\r\n' ] ) ,
            'test1\ntest2\ntest3\ntest4\n' )
    def test_single_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , ' test2' ] ) ,
            'test1\nindent\ntest2\ndedent\n' )
        ae ( r ( [ 'test1 test2' , ' test3 test4' ] ) ,
            'test1 test2\nindent\ntest3 test4\ndedent\n' )
        ae ( r ( [ '  test1' , '  test2' ] ) ,
            'indent\ntest1\ntest2\ndedent\n' )
    def test_same_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , ' test2' , ' test3' ] ) ,
            'test1\nindent\ntest2\ntest3\ndedent\n' )
    def test_multi_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , ' test2' , '  test3' ] ) ,
            'test1\nindent\ntest2\nindent\ntest3\ndedent\ndedent\n' )
    def test_different_indent ( self ) :
        ae = self . assertEqual
        r = self . i . run
        ae ( r ( [ 'test1' , '  test2' , ' test3' ] ) ,
            'test1\nindent\ntest2\ndedent\nindent\ntest3\ndedent\n' )

if __name__ == '__main__' :
    unittest . main ( )
