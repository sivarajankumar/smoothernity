import fractions
import reader
import unittest
from reader_tests_cases . helper import helper

class consts_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'consts test1\nconsts test2\n' )
        ar ( re , r , 'consts test1\nconst1 11\n' )
        ar ( re , r , 'consts test1\n const1 11\nconst2 11\n' )
        ar ( re , r , 'consts test1\n const1 11\n  const2 11\n' )
    def test_num_whole ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 11\n const2 - 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : - 22 } } } )
    def test_num_fract ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'consts test1\n const1 11 / 22\n const2 - 22 / 33\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : f ( 11 , 22 ) 
                , 'const2' : f ( - 22 , 33 ) } } } )
    def test_expression ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 [ 2 + 2 ]\n const2 []\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : '[ 2 + 2 ]' , 'const2' : '[]' } } } )
    def test_combine ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 11\nconsts test1\n  const2 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : 22 } } } )

