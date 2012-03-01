import unittest
import explorer

class explorer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . e = explorer . explorer
    def test_get_stateless_procs ( self ) :
        g = lambda x : self . e ( x ) . get_stateless_procs ( )
        ae = self . assertEqual
        ae ( g ( { 'stateless' :
            { 'st1' : { 'proc' : { 'proc1' : 'test1' } }
            , 'st2' : { 'proc' : { 'proc2' : 'test2' } } } } ) ,
            { 'st1_stateless_proc1' : 'test1'
            , 'st2_stateless_proc2' : 'test2' } )

if __name__ == '__main__' :
    unittest . main ( )
