import reader
import unittest
from reader_tests_cases . helper import helper

class lexer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( '' ) , { } )
        ae ( r ( ' ' ) , { } )
        ae ( r ( '\n' ) , { } )
        ae ( r ( '\r\n' ) , { } )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , '!@#$' )
        ar ( re , r , 'UPPERCASE' )
        ar ( re , r , '_test1' )
        ar ( re , r , '1_test1' )
