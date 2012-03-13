import normalizer
import unittest

class withs_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_strip ( self ) :
        ae = self . assertEqual
        r = self . n . run_withs
        ae ( r ( 
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'prefix' : [ 'something' ] } } } } ) ,
            { 'anywhere' : { 'anywhere' : 
                [ 'something' ] } } ) 
