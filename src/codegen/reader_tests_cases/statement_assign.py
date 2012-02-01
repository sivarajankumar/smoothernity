import unittest
from reader_tests_cases . helper import helper

class statement_assign_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_single ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   dst1 <- src1\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'assign' :
                { 'from' : [ 'src1' ] 
                , 'to' : [ 'dst1' ] } } ] } } } } )
    def test_multi ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   dst1 dst2 <- src1 src2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'assign' :
                { 'from' : [ 'src1' , 'src2' ]
                , 'to' : [ 'dst1' , 'dst2' ] } } ] } } } } )
