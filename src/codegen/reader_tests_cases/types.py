import unittest
import reader
from reader_tests_cases . helper import helper

class types_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'types test1 test2\n' )
    def test_single ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1 atr1\n'
                    ' type2 atr2\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : [ { 'atr1' : { } } ]
                , 'type2' : [ { 'atr2' : { } } ] } } } )
