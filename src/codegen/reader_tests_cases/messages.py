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
        ar ( re , r , 'messages test1\n msg1\n  reply a\n  request b\n' )
        ar ( re , r , 'messages test1\n msg1\n  reply a\n  reply b\n' )
        ar ( re , r , 'messages test1\n msg1\n  request a\n  request b\n' )
    def test_single ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'messages test1\n'
                    ' msg1 atr1\n'
                    ' msg2 atr2\n' ) ,
            { 'messages' : { 'test1' : { 'receive' :
                { 'msg1' : { 'atr1' : { } }
                , 'msg2' : { 'atr2' : { } } } } } } )
    def test_reply_same_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'messages test1\n msg1 reply atr1\n' ) ,
            { 'messages' : { 'test1' : { 'reply' : { 'msg1' :
                { 'atr1' : { } } } } } } )
    def test_reply_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'messages test1\n msg1\n  reply atr1\n' ) ,
            { 'messages' : { 'test1' : { 'reply' : { 'msg1' :
                { 'atr1' : { } } } } } } )
    def test_request_same_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'messages test1\n msg1 request atr1\n' ) ,
            { 'messages' : { 'test1' : { 'request' : { 'msg1' :
                { 'atr1' : { } } } } } } )
    def test_request_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'messages test1\n msg1\n  request atr1\n' ) ,
            { 'messages' : { 'test1' : { 'request' : { 'msg1' :
                { 'atr1' : { } } } } } } )
    def test_request_reply ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'messages test1\n msg1\n  request atr1\n  reply atr2\n' ) ,
            { 'messages' : { 'test1' :
                { 'request' : { 'msg1' : { 'atr1' : { } } }
                , 'reply' : { 'msg1' : { 'atr2' : { } } } } } } )

