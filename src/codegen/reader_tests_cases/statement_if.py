import reader
import unittest
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
