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
    def test_queue ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n module_queue test2\n' ) ,
            { 'module' : { 'test1' : { 'module_queue' : 'test2' } } } )
