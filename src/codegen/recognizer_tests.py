import unittest
import recognizer
import io
import fractions
import indenter
import formatter
import copypaster

class helper :
    def __init__ ( self ) :
        self . c = copypaster . copypaster ( )
        self . r = recognizer . recognizer ( )
        self . i = indenter . indenter ( )
        self . f = formatter . formatter ( )
        for o in ( self . i , self . f ) :
            o . set_indent_token ( 'indent' )
            o . set_dedent_token ( 'dedent' )
            o . set_newline_token ( '\n' )
    def rec ( self , s ) :
        indented1 = self . i . run ( io . StringIO ( s ) . readlines ( ) )
        copypasted = self . c . run ( io . StringIO ( indented1 ) )
        formatted = self . f . run ( copypasted )
        indented2 = self . i . run ( io . StringIO ( formatted ) . readlines ( ) )
        return self . r . run ( io . StringIO ( indented2 ) )

class recognizer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . h = helper ( )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( '' ) , { } )
        ae ( r ( ' ' ) , { } )
        ae ( r ( '\n' ) , { } )
        ae ( r ( '\r\n' ) , { } )
    def test_lexer_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        ce = copypaster . exception
        ar ( ce , r , '!@#$' )
        ar ( ce , r , 'UPPERCASE' )
    def test_copy_paste ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  const1 11\n'
            'paste replace const1 with const2\n'
            'paste replace const1 with const3\n' ) ,
            { 'consts' : { 'test1' : { 'const2' : 11 , 'const3' : 11 } } } )
    def test_copy_paste_substring ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'copy\n consts test1\n  myvalue 2\npaste\n'
            ' replace my with their\n'
            ' replace value with test 1 /\n' ) ,
            { 'consts' : { 'test1' : { 'theirtest' : f ( 1 , 2 ) } } } )
    def test_copy_paste_multi_replace ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  const1 11\npaste\n'
            ' replace test1 with test2\n'
            ' replace const1 with const2\n' ) ,
            { 'consts' : { 'test2' : { 'const2' : 11 } } } )
    def test_copy_paste_same_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n copy const1 11\n'
            ' paste replace const1 with const2\n' ) ,
            { 'consts' : { 'test1' : { 'const2' : 11 } } } )
    def test_copy_paste_multi_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'copy\n consts test1\n  test2\n'
            'paste replace test2 with\n const1 11\n const2 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : 22 } } } )
    def test_copy_paste_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        ce = copypaster . exception
        ar ( ce , r , 'copy\n' )
        ar ( ce , r , 'paste\n' )
        ar ( ce , r , 'copy\n copy\n  test1\n'
            ' paste replace test1 with test2\n'
            'paste replace test2 with test3\n' )
    def test_modules ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'module a\n' ) , { 'module' : { 'a' : { } } } )
        ae ( r ( 'module test_1\n' ) , { 'module' : { 'test_1' : { } } } )
        ae ( r ( 'module test1\nmodule test2\n' ) ,
            { 'module' : { 'test1' : { } , 'test2' : { } } } )
    def test_modules_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = recognizer . exception
        ar ( re , r , 'module _test1\n' )
        ar ( re , r , 'module 1_test1\n' )
        ar ( re , r , 'module' )
        ar ( re , r , 'module\n' )
        ar ( re , r , 'module module\n' )
    def test_consts_raises ( self ) :
        ar = self . assertRaises
        r = self . h . rec
        re = recognizer . exception
        ar ( re , r , 'consts test1\nconsts test2\n' )
        ar ( re , r , 'consts test1\nconst1 11\n' )
        ar ( re , r , 'consts test1\n const1 11\nconst2 11\n' )
        ar ( re , r , 'consts test1\n const1 11\n  const2 11\n' )
    def test_consts_num_whole ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 11\n const2 - 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : - 22 } } } )
    def test_consts_num_fract ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        f = fractions . Fraction
        ae ( r ( 'consts test1\n const1 11 / 22\n const2 - 22 / 33\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : f ( 11 , 22 ) 
                , 'const2' : f ( - 22 , 33 ) } } } )
    def test_consts_expression ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 [ 2 + 2 ]\n const2 []\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : '[ 2 + 2 ]' , 'const2' : '[]' } } } )
    def test_consts_combine ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'consts test1\n const1 11\nconsts test1\n  const2 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : 22 } } } )
    def test_types_empty ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1\n type2\n' ) ,
            { 'types' : { 'test1' : { 'type1' : { } , 'type2' : { } } } } )
    def test_types_combine ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 atr1\n'
                 'types test1\n type2 atr2\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr1' : { } }
                , 'type2' : { 'atr2' : { } } } } } )
    def test_types_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1\n  atr11\n  atr12\n'
                    ' type2\n  atr21\n  atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_types_indented_multi_atrs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1\n  atr1 atr2\n  atr3 atr4\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { } , 'atr2' : { }
                , 'atr3' : { } , 'atr4' : { } } } } } )
    def test_types_single_line ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1 atr11 atr12\n'
                    ' type2 atr21 atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_types_single_line_and_indented ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n'
                    ' type1 atr11\n  atr12\n'
                    ' type2 atr21\n  atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_types_hint ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } } } } } )
    def test_types_hint_args ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 arg1 arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ 'arg1' , 'arg2' ] } } } } } )
    def test_types_hint_args_wildcard ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 _ arg2 } atr1\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ '_' , 'arg2' ] } } } } } )
    def _test_types_hint_multi_atrs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1 atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { 'hint1' : [ ] } } } } } )
    def test_types_hint_indented_multi_atrs ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 }\n  atr1\n  atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { 'hint1' : [ ] } } } } } )
    def test_types_multi_hint ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1 { hint1 } atr1\n'
            '  { hint2 } atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { 'hint2' : [ ] } } } } } )
    def test_types_hint_no_hint ( self ) :
        ae = self . assertEqual
        r = self . h . rec
        ae ( r ( 'types test1\n type1\n'
            '  { hint1 } atr1\n  atr2\n' ) ,
            { 'types' : { 'test1' : { 'type1' :
                { 'atr1' : { 'hint1' : [ ] } 
                , 'atr2' : { } } } } } )

if __name__ == '__main__' :
    unittest . main ( )
