import unittest
from reader_tests_cases . helper import helper

class receive_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n receive rcv1\n' ) ,
            { 'module' : { 'test1' : { 'receive' :
                { 'rcv1' : { } } } } } )
    def test_vars ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n receive rcv1\n  vars var1\n' ) ,
            { 'module' : { 'test1' : { 'receive' :
                { 'rcv1' : { 'vars' : { 'var1' : { } } } } } } } )
    def test_ops ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n receive rcv1\n  ops\n   call1\n' ) ,
            { 'module' : { 'test1' : { 'receive' :
                { 'rcv1' : { 'ops' : [ { 'call' : [ 'call1' ] } ] } } } } } )
