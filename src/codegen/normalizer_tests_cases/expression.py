import normalizer
import unittest

class expression_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_number ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 ]' } } } ) ,
            { 'consts' : { 'test1' : { 'test2' : 1 } } } )
    def test_math ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 + 1 ]' } } } ) ,
            { 'consts' : { 'test1' : { 'test2' : 2 } } } )
