import reader
import unittest
from reader_tests_cases . helper import helper

class trace_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'trace test1\ntrace test2\n' ) ,
            { 'trace' : { 'test1' : { } , 'test2' : { } } } )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'trace' )
        ar ( re , r , 'trace\n' )
        ar ( re , r , 'trace trace\n' )
    def test_procs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'trace test1\n proc proc1\n proc proc2\n' ) ,
            { 'trace' : { 'test1' :
                { 'proc1' : { } , 'proc2' : { } } } } )

