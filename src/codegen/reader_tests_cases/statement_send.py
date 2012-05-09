import fractions
import unittest
import reader
from reader_tests_cases . helper import helper

class statement_send_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'stateless test1\n proc proc1\n  ops\n   send\n' )
        ar ( re , r , 'stateless test1\n proc proc1\n  ops\n   send 123\n' )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   send msg1\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'msg1' ] } ] } } } } } )
    def test_multi_calls ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   send msg1\n   send msg2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'msg1' ] }
                , { 'send' : [ 'msg2' ] } ] } } } } } )
    def test_args_one_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   send msg1 arg1 arg2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'msg1' , 'arg1' , 'arg2' ] } ] } } } } } )
    def test_args_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   send msg1\n    arg1 arg2\n    arg3' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'msg1' , 'arg1' , 'arg2' , 'arg3' ] }
            ] } } } } } )
    def test_args_num_whole ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   send msg1 1\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'msg1' , 1 ] } ] } } } } } )
    def test_args_num_fract ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   send msg1 1 / 2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'msg1' , f ( 1 , 2 ) ] } ] } } } } } )
    def test_args_expression ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   send msg1 [ expr1 ]\n' ) ,
            { 'stateless' : { 'test1' : { 'proc' : { 'proc1' : { 'ops' :
                [ { 'send' : [ 'msg1' , '[ expr1 ]' ] } ] } } } } } )
