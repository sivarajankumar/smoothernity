import unittest
import fractions
import reader
from reader_tests_cases . helper import helper

class lexer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( '' ) , { } )
        ae ( r ( ' ' ) , { } )
        ae ( r ( '\n' ) , { } )
        ae ( r ( '\r\n' ) , { } )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , '!@#$' )
        ar ( re , r , 'UPPERCASE' )
        ar ( re , r , '_test1' )
        ar ( re , r , '1_test1' )

class copy_paste_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'copy\n' )
        ar ( re , r , 'paste\n' )
        ar ( re , r , 'copy\n copy\n  test1\n'
            ' paste replace test1 with test2\n'
            'paste replace test2 with test3\n' )
    def test_multi_paste ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  const1 11\n'
            'paste replace const1 with const2\n'
            'paste replace const1 with const3\n' ) ,
            { 'consts' : { 'test1' : { 'const2' : 11 , 'const3' : 11 } } } )
    def test_substring ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'copy\n consts test1\n  myvalue 2\npaste\n'
            ' replace my with their\n'
            ' replace value with test 1 /\n' ) ,
            { 'consts' : { 'test1' : { 'theirtest' : f ( 1 , 2 ) } } } )
    def test_multi_replace ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  const1 11\npaste\n'
            ' replace test1 with test2\n'
            ' replace const1 with const2\n' ) ,
            { 'consts' : { 'test2' : { 'const2' : 11 } } } )
    def test_same_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n copy const1 11\n'
            ' paste replace const1 with const2\n' ) ,
            { 'consts' : { 'test1' : { 'const2' : 11 } } } )
    def test_multi_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  test2\n'
            'paste replace test2 with\n const1 11\n const2 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : 22 } } } )

class ids_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module t\n' ) , { 'module' : { 't' : { } } } )
        ae ( r ( 'module test\n' ) , { 'module' : { 'test' : { } } } )
        ae ( r ( 'module test1\n' ) , { 'module' : { 'test1' : { } } } )
        ae ( r ( 'module test_1\n' ) , { 'module' : { 'test_1' : { } } } )

class modules_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module test1\nmodule test2\n' ) ,
            { 'module' : { 'test1' : { } , 'test2' : { } } } )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'module' )
        ar ( re , r , 'module\n' )
        ar ( re , r , 'module module\n' )

class stateless_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\nstateless test2\n' ) ,
            { 'stateless' : { 'test1' : { } , 'test2' : { } } } )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = reader . exception
        ar ( re , r , 'stateless' )
        ar ( re , r , 'stateless\n' )
        ar ( re , r , 'stateless stateless\n' )
    def test_procs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n proc proc2\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { } , 'proc2' : { } } } } )

class proc_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { } } } } )
    def test_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  args arg1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { 'args' : { 'arg1' : { } } } } } } )
    def test_vars ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  vars arg1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { 'vars' : { 'arg1' : { } } } } } } )
    def test_ops ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n   call1\n' ) ,
            { 'stateless' : { 'test1' :
                { 'proc1' : { 'ops' : [ { 'call' : [ 'call1' ] } ] } } } } )

class statement_with_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_simple ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   with call1\n    call2\n    call3\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'with' :
                { 'call1' :
                    [ { 'call' : [ 'call2' ] }
                    , { 'call' : [ 'call3' ] } ] } } ] } } } } )

class statement_assign_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_single ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   var1 <- var2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'assign' : [ 'var2' , [ 'var1' ] ] } ] } } } } )

class statement_call_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_no_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' :
                [ { 'call' : [ 'call1' ] } ] } } } } )
    def test_multi_calls ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1\n   call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' :
                [ { 'call' : [ 'call1' ] }
                , { 'call' : [ 'call2' ] } ] } } } } )
    def test_args_one_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 arg1 arg2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , 'arg1' , 'arg2' ] } ] } } } } )
    def test_args_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1\n    arg1 arg2\n    arg3' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , 'arg1' , 'arg2' , 'arg3' ] } ] } } } } )
    def test_args_num_whole ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 1\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , 1 ] } ] } } } } )
    def test_args_num_fract ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 1 / 2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , f ( 1 , 2 ) ] } ] } } } } )
    def test_args_expression ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   call1 [ expr1 ]\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [ { 'call' :
                [ 'call1' , '[ expr1 ]' ] } ] } } } } )

class conditions_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_no_grouping ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if call1 do\n    call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' : [
                    { 'any' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } ] } ] } } } } )
    def test_any_grouping ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if any call1 do\n    call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' : [
                    { 'any' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } ] } ] } } } } )
    def test_all_grouping ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if all call1 do\n    call2\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' : [
                    { 'all' : [ { 'call' : [ 'call1' ] } ]
                    , 'ops' : [ { 'call' : [ 'call2' ] } ]
                    } ] } ] } } } } )
    def test_multi_call ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'stateless test1\n proc proc1\n  ops\n'
            '   if any\n    call1\n    call2\n   do\n    call3\n' ) ,
            { 'stateless' : { 'test1' : { 'proc1' : { 'ops' : [
                { 'if' : [
                    { 'any' : [ { 'call' : [ 'call1' ] }
                              , { 'call' : [ 'call2' ] } ]
                    , 'ops' : [ { 'call' : [ 'call3' ] } ]
                    } ] } ] } } } } )

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
