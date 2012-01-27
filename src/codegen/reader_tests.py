import unittest
from reader_tests_cases . conditions import *
from reader_tests_cases . consts import *
from reader_tests_cases . copy_paste import *
from reader_tests_cases . ids import *
from reader_tests_cases . lexer import *
from reader_tests_cases . modules import *
from reader_tests_cases . proc import *
from reader_tests_cases . stateless import *
from reader_tests_cases . statement_assign import *
from reader_tests_cases . statement_call import *
from reader_tests_cases . statement_if import *
from reader_tests_cases . statement_with import *
from reader_tests_cases . types import *
from reader_tests_cases . helper import helper

class hints_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } } } } } )
    def test_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 arg1 arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ 'arg1' , 'arg2' ] } } } } } )
    def test_args_wildcard ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 _ arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ '_' , 'arg2' ] } } } } } )

if __name__ == '__main__' :
    unittest . main ( )
