import unittest
from reader_tests_cases . conditions import *
from reader_tests_cases . consts import *
from reader_tests_cases . copy_paste import *
from reader_tests_cases . ids import *
from reader_tests_cases . lexer import *
from reader_tests_cases . modules import *
from reader_tests_cases . proc import *
from reader_tests_cases . stateless import *
from reader_tests_cases . statement_assign import *
from reader_tests_cases . statement_call import *
from reader_tests_cases . statement_if import *
from reader_tests_cases . statement_with import *
from reader_tests_cases . helper import helper

class types_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1\n type2\n' ) ,
            { 'types' : { 'test1' : { 'type1' : { } , 'type2' : { } } } } )
    def test_combine ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 atr1\n'
                 'types test1\n type2 atr2\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr1' : { } }
                , 'type2' : { 'atr2' : { } } } } } )
    def test_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1\n  atr11\n  atr12\n'
                    ' type2\n  atr21\n  atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_indented_multi_atrs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1\n  atr1 atr2\n  atr3 atr4\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { } , 'atr2' : { }
                , 'atr3' : { } , 'atr4' : { } } } } } )
    def test_single_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1 atr11 atr12\n'
                    ' type2 atr21 atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_single_line_and_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1 atr11\n  atr12\n'
                    ' type2 atr21\n  atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_hint_multi_atrs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1 atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { 'hint1' : [ ] } } } } } )
    def test_hint_indented_multi_atrs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 }\n  atr1\n  atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { 'hint1' : [ ] } } } } } )
    def test_multi_hint ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1\n'
            '  { hint2 } atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { 'hint2' : [ ] } } } } } )
    def test_hint_no_hint ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1\n'
            '  { hint1 } atr1\n  atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { } } } } } )

class hints_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } } } } } )
    def test_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 arg1 arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ 'arg1' , 'arg2' ] } } } } } )
    def test_args_wildcard ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 _ arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ '_' , 'arg2' ] } } } } } )

if __name__ == '__main__' :
    unittest . main ( )
