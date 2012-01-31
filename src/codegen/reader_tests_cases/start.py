import unittest
from reader_tests_cases . helper import helper

class start_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_combine_dict ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 atr1\n'
                 'types test1\n type2 atr2\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr1' : { } }
                , 'type2' : { 'atr2' : { } } } } } )
    def test_combine_list ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\n proc proc1\n'
                 'module test1\n proc proc2\n' ) ,
            { 'modules' : { 'module1' : 
                { 'procs' : { 'proc1' : { } , 'proc2' : { } } } } } )
