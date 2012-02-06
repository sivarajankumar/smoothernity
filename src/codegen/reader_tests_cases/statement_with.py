import unittest
from reader_tests_cases . helper import helper

class statement_with_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_simple ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   with call1\n    call2\n    call3\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'with' : { 'call1' :
                    [ { 'call' : [ 'call2' ] }
                    , { 'call' : [ 'call3' ] } ] } } ] } } } } } )
