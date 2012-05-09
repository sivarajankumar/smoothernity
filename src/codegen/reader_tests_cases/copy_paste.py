import fractions
import reader
import unittest
from reader_tests_cases . helper import helper

class copy_paste_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'copy\n' )
        ar ( re , r , 'paste\n' )
        ar ( re , r , 'copy\n copy\n  test1\n'
            ' paste replace test1 with test2\n'
            'paste replace test2 with test3\n' )
    def test_multi_paste ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  const1 11\n'
            'paste replace const1 with const2\n'
            'paste replace const1 with const3\n' ) ,
            { 'consts' : { 'test1' : { 'const2' : 11 , 'const3' : 11 } } } )
    def test_substring ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'copy\n consts test1\n  myvalue 2\npaste\n'
            ' replace my with their\n'
            ' replace value with test 1 /\n' ) ,
            { 'consts' : { 'test1' : { 'theirtest' : f ( 1 , 2 ) } } } )
    def test_multi_replace ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  const1 11\npaste\n'
            ' replace test1 with test2\n'
            ' replace const1 with const2\n' ) ,
            { 'consts' : { 'test2' : { 'const2' : 11 } } } )
    def test_same_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n copy const1 11\n'
            ' paste replace const1 with const2\n' ) ,
            { 'consts' : { 'test1' : { 'const2' : 11 } } } )
    def test_multi_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  test2\n'
            'paste replace test2 with\n const1 11\n const2 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : 22 } } } )

