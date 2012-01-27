import unittest
from reader_tests_cases . helper import helper

class hints_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } } } } } )
    def test_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 arg1 arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ 'arg1' , 'arg2' ] } } } } } )
    def test_args_wildcard ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 _ arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ '_' , 'arg2' ] } } } } } )
