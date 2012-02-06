import reader
import unittest
from reader_tests_cases . helper import helper

class modules_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'module' )
        ar ( re , r , 'module\n' )
        ar ( re , r , 'module module\n' )
        ar ( re , r , 'module test1\n' )
    def test_queue ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n module_queue test2\n' ) ,
            { 'module' : { 'test1' : { 'module_queue' : 'test2' } } } )
    def test_procs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n proc proc1\n proc proc2' ) ,
            { 'module' : { 'test1' : { 'proc' : 
                { 'proc1' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] }
                , 'proc2' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] }
                } } } } )
    def test_receives ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n receive rcv1\n receive rcv2' ) ,
            { 'module' : { 'test1' : { 'receive' : 
                { 'rcv1' : { }
                , 'rcv2' : { } } } } } )
    def test_requests ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n request req1\n request req2' ) ,
            { 'module' : { 'test1' : { 'request' : 
                { 'req1' : { }
                , 'req2' : { } } } } } )
    def test_random_order ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n'
            ' proc proc1\n request req1\n proc proc2\n' ) ,
            { 'module' : { 'test1' :
                { 'proc' :
                    { 'proc1' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] }
                    , 'proc2' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] } }
                , 'request' : { 'req1' : { } } } } } )
