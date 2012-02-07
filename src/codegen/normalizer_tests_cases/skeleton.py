import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton as mskel

class skeleton_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { } ) , mskel ( { } ) )
    def test_stateless ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'stateless' : { 'test1' : { } } } ) ,
            mskel ( { 'stateless' : { 'test1' : { 'proc' : { } } } } ) )
    def test_trace ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'trace' : { 'test1' : { } } } ) ,
            mskel ( { 'trace' : { 'test1' : { 'proc' : { } } } } ) )
    def test_module ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'module' : { 'test1' : { } } } ) ,
            mskel ( { 'module' : { 'test1' : { 'module_queue' : '' ,
                'proc' : { } , 'receive' : { } , 'request' : { } } } } ) )
    def test_proc ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : { } } } } } ) ,
            mskel ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] }
            } } } } ) )
