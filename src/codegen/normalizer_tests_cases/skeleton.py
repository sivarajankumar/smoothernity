import normalizer
import unittest
from normalizer_tests_cases . helper import merge_skeleton_root as mroot
from normalizer_tests_cases . helper import merge_skeleton_module as mmod
from normalizer_tests_cases . helper import merge_skeleton_proc as mproc
from normalizer_tests_cases . helper import merge_skeleton_messages as mmsg

class skeleton_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { } ) , mroot ( { } ) )
    def test_stateless ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { 'stateless' : { 'test1' : { } } } ) ,
            mroot ( { 'stateless' : { 'test1' : { 'proc' : { } } } } ) )
    def test_trace ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { 'trace' : { 'test1' : { } } } ) ,
            mroot ( { 'trace' : { 'test1' : { 'proc' : { } } } } ) )
    def test_module ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { 'module' : { 'test1' : { } } } ) ,
            mroot ( { 'module' : { 'test1' : mmod ( { } ) } } ) )
    def test_messages ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { 'messages' : { 'test1' : { } } } ) ,
            mroot ( { 'messages' : { 'test1' : mmsg ( { } ) } } ) )
    def test_proc ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : { } } } } } ) ,
            mroot ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : mproc ( { } )
            } } } } ) )
    def test_request ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { 'module' : { 'test1' : { 'request' : {
            'test2' : { } } } } } ) ,
            mroot (
                { 'messages' : { 'test1' : mmsg (
                    { 'request' : { 'test2' : [ ] }
                    , 'reply' : { 'test2' : [ ] } } ) } 
                , 'module' : { 'test1' : mmod (
                    { 'request' : { 'test2' :
                        { 'vars' : [ ] , 'ops' : [ ] }
                } } ) } } ) )
    def test_receive ( self ) :
        ae = self . assertEqual
        r = self . n . run_skeleton
        ae ( r ( { 'module' : { 'test1' : { 'receive' : {
            'test2' : { } } } } } ) ,
            mroot (
                { 'messages' : { 'test1' : mmsg (
                    { 'receive' : { 'test2' : [ ] } } ) }
                , 'module' : { 'test1' : mmod (
                    { 'receive' : { 'test2' :
                        { 'vars' : [ ] , 'ops' : [ ] }
                } } ) } } ) )
