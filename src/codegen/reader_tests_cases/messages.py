import unittest
import reader
from reader_tests_cases . helper import helper

class messages_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'messages test1 test2\n' )
    def test_single ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'messages test1\n'
                    ' msg1 atr1\n'
                    ' msg2 atr2\n' ) ,
            { 'messages' : { 'test1' : 
                { 'msg1' : { 'atr1' : { } }
                , 'msg2' : { 'atr2' : { } } } } } )
