import unittest
from reader_tests_cases . helper import helper

class vars_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_single ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'vars test1\n var1\n' ) ,
            { 'vars' : { 'test1' : { 'var1' : { } } } } )
