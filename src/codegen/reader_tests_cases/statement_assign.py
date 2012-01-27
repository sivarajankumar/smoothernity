import unittest
from reader_tests_cases . helper import helper

class statement_assign_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_single ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   var1 <- var2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'assign' : [ 'var2' , [ 'var1' ] ] } ] } } } } )
