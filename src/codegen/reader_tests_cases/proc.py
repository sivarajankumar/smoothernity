import unittest
from reader_tests_cases . helper import helper

class proc_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { } } } } )
    def test_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  args arg1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { 'args' : { 'arg1' : { } } } } } } )
    def test_vars ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  vars arg1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { 'vars' : { 'arg1' : { } } } } } } )
    def test_ops ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n   call1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { 'ops' : [ { 'call' : [ 'call1' ] } ] } } } } )
