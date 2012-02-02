import unittest
from reader_tests_cases . helper import helper

class request_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n request req1\n' ) ,
            { 'module' : { 'test1' : { 'request' :
                { 'req1' : { } } } } } )
    def test_vars ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n request req1\n  vars var1\n' ) ,
            { 'module' : { 'test1' : { 'request' :
                { 'req1' : { 'vars' : { 'var1' : { } } } } } } } )
    def test_ops ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n request req1\n  ops\n   call1\n' ) ,
            { 'module' : { 'test1' : { 'request' :
                { 'req1' : { 'ops' : [ { 'call' : [ 'call1' ] } ] } } } } } )
    def test_silent_ops ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n request req1\n  call1\n' ) ,
            { 'module' : { 'test1' : { 'request' :
                { 'req1' : { 'ops' : [ { 'call' : [ 'call1' ] } ] } } } } } )
