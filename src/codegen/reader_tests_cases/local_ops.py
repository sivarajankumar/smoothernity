import unittest
from reader_tests_cases . helper import helper

class local_ops_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n'
            '  ops\n   call1\n   call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' :
                [ { 'call' : [ 'call1' ] }
                , { 'call' : [ 'call2' ] } ] } } } } )
