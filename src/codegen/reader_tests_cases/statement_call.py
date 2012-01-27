import fractions
import unittest
from reader_tests_cases . helper import helper

class statement_call_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' :
                [ { 'call' : [ 'call1' ] } ] } } } } )
    def test_multi_calls ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1\n   call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' :
                [ { 'call' : [ 'call1' ] }
                , { 'call' : [ 'call2' ] } ] } } } } )
    def test_args_one_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 arg1 arg2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , 'arg1' , 'arg2' ] } ] } } } } )
    def test_args_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1\n    arg1 arg2\n    arg3' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , 'arg1' , 'arg2' , 'arg3' ] } ] } } } } )
    def test_args_num_whole ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 1\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , 1 ] } ] } } } } )
    def test_args_num_fract ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 1 / 2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , f ( 1 , 2 ) ] } ] } } } } )
    def test_args_expression ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 [ expr1 ]\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , '[ expr1 ]' ] } ] } } } } )
