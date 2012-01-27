import unittest
import fractions
import reader
from reader_tests_cases . conditions import *
from reader_tests_cases . copy_paste import *
from reader_tests_cases . ids import *
from reader_tests_cases . lexer import *
from reader_tests_cases . modules import *
from reader_tests_cases . proc import *
from reader_tests_cases . stateless import *
from reader_tests_cases . statement_assign import *
from reader_tests_cases . statement_call import *
from reader_tests_cases . statement_with import *
from reader_tests_cases . helper import helper

class statement_if_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'stateless test1\n proc proc1\n  ops\n'
            '   elif call1\n   do\n    call2\n' )
        ar ( re , r , 'stateless test1\n proc proc1\n  ops\n'
            '   else call1\n   do\n    call2\n' )
        ar ( re , r , 'stateless test1\n proc proc1\n  ops\n'
            '   if call1\n   do\n    call2\n'
            '   else call3\n   do\n    call4\n'
            '   else call5\n   do\n    call6\n' )
    def test_one_cond ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if call1\n   do\n    call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' : [
                    { 'any' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } ] } ] } } } } )
    def test_do_on_same_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if call1 do\n    call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' : [
                    { 'any' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } ] } ] } } } } )
    def test_else ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if call1 do\n    call2\n'
            '   else\n    call3\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' : [
                    { 'any' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } ]
                , 'else' : [ { 'call' : [ 'call3' ] } ]
                } ] } } } } )
    def test_elif ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if call1 do\n    call2\n'
            '   elif call3 do\n    call4\n'
            '   elif call5 do\n    call6\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' :
                    [   { 'any' : [ { 'call' : [ 'call1' ] } ]
                        , 'ops' : [ { 'call' : [ 'call2' ] } ] }
                    ,   { 'any' : [ { 'call' : [ 'call3' ] } ]
                        , 'ops' : [ { 'call' : [ 'call4' ] } ] }
                    ,   { 'any' : [ { 'call' : [ 'call5' ] } ]
                        , 'ops' : [ { 'call' : [ 'call6' ] } ] }
                    ] } ] } } } } )

class consts_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'consts test1\nconsts test2\n' )
        ar ( re , r , 'consts test1\nconst1 11\n' )
        ar ( re , r , 'consts test1\n const1 11\nconst2 11\n' )
        ar ( re , r , 'consts test1\n const1 11\n  const2 11\n' )
    def test_num_whole ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 11\n const2 - 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : - 22 } } } )
    def test_num_fract ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'consts test1\n const1 11 / 22\n const2 - 22 / 33\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : f ( 11 , 22 ) 
                , 'const2' : f ( - 22 , 33 ) } } } )
    def test_expression ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 [ 2 + 2 ]\n const2 []\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : '[ 2 + 2 ]' , 'const2' : '[]' } } } )
    def test_combine ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 11\nconsts test1\n  const2 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : 22 } } } )

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
