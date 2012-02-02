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
        ar ( re , r , 'module test1\n'
            ' module_queue test2\n module_queue test3\n' )
        ar ( re , r , 'module test1\n'
            ' proc test1\n module_queue test2\n proc test3\n' )
        ar ( re , r , 'module test1\n'
            ' receive test1\n module_queue test2\n receive test3\n' )
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
                { 'proc1' : { }
                , 'proc2' : { } } } } } )
    def test_receives ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n receive rcv1\n receive rcv2' ) ,
            { 'module' : { 'test1' : { 'receive' : 
                { 'rcv1' : { }
                , 'rcv2' : { } } } } } )
