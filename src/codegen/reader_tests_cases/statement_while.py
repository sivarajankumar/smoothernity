import reader
import unittest
from reader_tests_cases . helper import helper

class statement_while_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_one_cond ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   while call1\n   do\n    call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' : [
                { 'while' :
                    { 'any' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } } ] } } } } } )
    def test_do_on_same_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   while call1 do\n    call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' : [
                { 'while' :
                    { 'any' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } } ] } } } } } )
