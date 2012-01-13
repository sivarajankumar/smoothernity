import unittest
import recognizer
import io
import fractions

class recognizer_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . r = recognizer . recognizer ( )
    def rec ( self , s ) :
        return self . r . recognize ( io . StringIO ( s ) )
    def test_empty ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( '' ) , { } )
        ae ( r ( ' ' ) , { } )
        ae ( r ( '\n' ) , { } )
        ae ( r ( '\r\n' ) , { } )
    def test_lexer_raises ( self ) :
        ar = self . assertRaises
        r = self . rec
        re = recognizer . exception
        ar ( re , r , '!@#$' )
        ar ( re , r , 'UPPERCASE' )
    def test_modules ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'module a\n' ) , { 'module' : { 'a' : { } } } )
        ae ( r ( 'module test_1\n' ) , { 'module' : { 'test_1' : { } } } )
        ae ( r ( 'module test1\nmodule test2\n' ) ,
            { 'module' : { 'test1' : { } , 'test2' : { } } } )
    def test_modules_raises ( self ) :
        ar = self . assertRaises
        r = self . rec
        re = recognizer . exception
        ar ( re , r , 'module _test1\n' )
        ar ( re , r , 'module 1_test1\n' )
        ar ( re , r , 'module' )
        ar ( re , r , 'module\n' )
        ar ( re , r , 'module module\n' )
    def test_consts_raises ( self ) :
        ar = self . assertRaises
        r = self . rec
        re = recognizer . exception
        ar ( re , r , 'consts test1\nconsts test2\n' )
        ar ( re , r , 'consts test1\nconst1 11\n' )
        ar ( re , r , 'consts test1\n const1 11\nconst2 11\n' )
        ar ( re , r , 'consts test1\n const1 11\n  const2 11\n' )
    def test_consts_num_whole ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'consts test1\n const1 11\n const2 - 22\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 , 'const2' : - 22 } } } )
    def test_consts_num_fract ( self ) :
        ae = self . assertEqual
        r = self . rec
        f = fractions . Fraction
        ae ( r ( 'consts test1\n const1 11 / 22\n const2 - 22 / 33\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : f ( 11 , 22 ) 
                , 'const2' : f ( - 22 , 33 ) } } } )
    def test_consts_expression ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'consts test1\n const1 [ 2 + 2 ]\n const2 []\n' ) ,
            { 'consts' : { 'test1' : 
                { 'const1' : '[ 2 + 2 ]' , 'const2' : '[]' } } } )
    def test_types_indented ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'types test1\n'
                    ' type1\n  atr11\n  atr12\n'
                    ' type2\n  atr21\n  atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_types_single_line ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'types test1\n'
                    ' type1 atr11 atr12\n'
                    ' type2 atr21 atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )
    def test_types_single_line_and_indented ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'types test1\n'
                    ' type1 atr11\n  atr12\n'
                    ' type2 atr21\n  atr22\n' ) ,
            { 'types' : { 'test1' : 
                { 'type1' : { 'atr11' : { } , 'atr12' : { } }
                , 'type2' : { 'atr21' : { } , 'atr22' : { } } } } } )

if __name__ == '__main__' :
    unittest . main ( )
