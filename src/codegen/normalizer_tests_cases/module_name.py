from normalizer . module_name import run
import unittest

class module_name_test_case ( unittest . TestCase ) :
    def test_module_name ( self ) :
        ae = self . assertEqual
        ae ( run ( 
            { 'p1' : { 'p2' : { 'p3' : [ 'module_name' ] } } } ) ,
            { 'p1' : { 'p2' : { 'p3' : [ 'p2' ] } } } )
