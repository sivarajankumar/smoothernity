from normalizer . sends_check import run
from normalizer . skeleton import run as rskel
from normalizer . exception import exception
import unittest

class sends_check_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        s = rskel (
            { 'path1' : { 'path2' :
                { 'send' : [ 'func1' , 'unknown' ] } } } )
        ne = exception
        ar = self . assertRaises
        ar ( ne , run , s )
    def test_success ( self ) :
        s = rskel (
            { 'path1' : { 'path2' :
                { 'send' : [ 'func1' , 1 ] } } } )
        ae = self . assertEqual
        ae ( run ( s ) , s )
