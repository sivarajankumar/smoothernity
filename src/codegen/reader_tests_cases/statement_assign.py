import unittest
from reader_tests_cases . helper import helper

class statement_assign_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_left_one_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   dst1 dst2 <- src1 src2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'assign' :
                { 'from' : [ 'src1' , 'src2' ]
                , 'to' : [ 'dst1' , 'dst2' ] } } ] } } } } )
    def test_left_multi_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   dst1 dst2 dst3 <-\n    src1 src2\n    src3\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'assign' :
                { 'from' : [ 'src1' , 'src2' , 'src3' ]
                , 'to' : [ 'dst1' , 'dst2' , 'dst3' ] } } ] } } } } )
    def test_right_one_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   src1 src2 -> dst1 dst2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'assign' :
                { 'from' : [ 'src1' , 'src2' ]
                , 'to' : [ 'dst1' , 'dst2' ] } } ] } } } } )
    def test_right_multi_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   src1 src2 src3 ->\n    dst1 dst2\n    dst3\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'assign' :
                { 'from' : [ 'src1' , 'src2' , 'src3' ]
                , 'to' : [ 'dst1' , 'dst2' , 'dst3' ] } } ] } } } } )
