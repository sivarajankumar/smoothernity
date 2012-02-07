import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_module as mmod

class skeleton_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { } ) , mroot ( { } ) )
    def test_stateless ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'stateless' : { 'test1' : { } } } ) ,
            mroot ( { 'stateless' : { 'test1' : { 'proc' : { } } } } ) )
    def test_trace ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'trace' : { 'test1' : { } } } ) ,
            mroot ( { 'trace' : { 'test1' : { 'proc' : { } } } } ) )
    def test_module ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'module' : { 'test1' : { } } } ) ,
            mroot ( { 'module' : { 'test1' : mmod ( { } ) } } ) )
    def test_proc ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : { } } } } } ) ,
            mroot ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] }
            } } } } ) )
    def test_request ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'module' : { 'test1' : { 'request' : {
            'test2' : { } } } } } ) ,
            mroot ( { 'module' : { 'test1' : mmod ( { 'request' : {
            'test2' : { 'vars' : [ ] , 'ops' : [ ] } } } ) } } ) )
    def test_receive ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'module' : { 'test1' : { 'receive' : {
            'test2' : { } } } } } ) ,
            mroot ( { 'module' : { 'test1' : mmod ( { 'receive' : {
            'test2' : { 'vars' : [ ] , 'ops' : [ ] } } } ) } } ) )
