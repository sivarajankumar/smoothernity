from normalizer . withs import run
import unittest

class withs_test_case ( unittest . TestCase ) :
    def test_strip ( self ) :
        ae = self . assertEqual
        ae ( run ( 
            { 'anywhere' : { 'anywhere' : { 'with' :
                { 'prefix' : [ 'something' ] } } } } ) ,
            { 'anywhere' : { 'anywhere' : 
                [ 'something' ] } } ) 
    def test_keep ( self ) :
        ae = self . assertEqual
        s = { 'anywhere' : { 'anywhere' : { 'something' :
                { 'prefix' : [ 'something' ] } } } }
        ae ( run ( s ) , s )