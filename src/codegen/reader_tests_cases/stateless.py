import reader
import unittest
from reader_tests_cases . helper import helper

class stateless_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\nstateless test2\n' ) ,
            { 'stateless' : { 'test1' : { } , 'test2' : { } } } )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'stateless' )
        ar ( re , r , 'stateless\n' )
        ar ( re , r , 'stateless stateless\n' )
    def test_procs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n proc proc2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' :
                { 'proc1' : { } , 'proc2' : { } } } } } )
