import unittest
import explorer
from normalizer_tests_cases . helper import merge_skeleton_root as mroot

class explorer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . e = explorer . explorer
    def test_get_stateless_procs ( self ) :
        g = lambda x : self . e ( x ) . get_stateless_procs ( )
        ae = self . assertEqual
        ae ( g ( mroot ( { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' : 'test1' } }
            , 'st2' : { 'proc' : { 'proc2' : 'test2' } } } } ) ) ,
            { 'st1_stateless_proc1' : 'test1'
            , 'st2_stateless_proc2' : 'test2' } )
    def test_get_trace_procs ( self ) :
        g = lambda x : self . e ( x ) . get_trace_procs ( )
        ae = self . assertEqual
        ae ( g ( mroot ( { 'trace' :
            { 'st1' : { 'proc' : { 'proc1' : 'test1' } }
            , 'st2' : { 'proc' : { 'proc2' : 'test2' } } } } ) ) ,
            { 'st1_trace_proc1' : 'test1'
            , 'st2_trace_proc2' : 'test2' } )
    def test_get_platform_procs ( self ) :
        g = lambda x : self . e ( x ) . get_platform_procs ( )
        ae = self . assertEqual
        ae ( g ( mroot ( { 'platform_procs' :
            { 'func1' : 'test1'
            , 'func2' : 'test2' } } ) ) ,
            { 'func1' : 'test1'
            , 'func2' : 'test2' } )
    def test_get_messages_receives ( self ) :
        g = lambda x : self . e ( x ) . get_messages_receives ( )
        ae = self . assertEqual
        ae ( g ( mroot ( { 'messages' :
            { 'group1' : { 'receive' : { 'msg1' : 'test1' } }
            , 'group2' : { 'receive' : { 'msg2' : 'test2' } } } } ) ) ,
            { 'group1_msg1' : 'test1'
            , 'group2_msg2' : 'test2' } )

if __name__ == '__main__' :
    unittest . main ( )
