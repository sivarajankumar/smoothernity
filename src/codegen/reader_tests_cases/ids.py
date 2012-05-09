import unittest
from reader_tests_cases . helper import helper

class ids_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts t\n a 1' ) ,
            { 'consts' : { 't' : { 'a' : 1 } } } )
        ae ( r ( 'consts test\n a 1' ) ,
            { 'consts' : { 'test' : { 'a' : 1 } } } )
        ae ( r ( 'consts test1\n a 1' ) ,
            { 'consts' : { 'test1' : { 'a' : 1 } } } )
        ae ( r ( 'consts test_1\n a 1' ) ,
            { 'consts' : { 'test_1' : { 'a' : 1 } } } )
