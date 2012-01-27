import unittest
from reader_tests_cases . helper import helper

class ids_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module t\n' ) , { 'module' : { 't' : { } } } )
        ae ( r ( 'module test\n' ) , { 'module' : { 'test' : { } } } )
        ae ( r ( 'module test1\n' ) , { 'module' : { 'test1' : { } } } )
        ae ( r ( 'module test_1\n' ) , { 'module' : { 'test_1' : { } } } )
