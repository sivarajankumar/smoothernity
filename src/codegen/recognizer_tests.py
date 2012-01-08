import unittest
import recognizer
import io

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
        ar ( recognizer . exception , r , '!@#$' )
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
        ar ( recognizer . exception , r , 'module _test1\n' )
        ar ( recognizer . exception , r , 'module 1_test1\n' )
        ar ( recognizer . exception , r , 'module test1' )
        ar ( recognizer . exception , r , 'module' )
        ar ( recognizer . exception , r , 'module\n' )
        ar ( recognizer . exception , r , 'module module\n' )
    def test_consts ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'consts test1\nconsts test2\n' ) ,
            { 'consts' : { 'test1' : { } , 'test2' : { } } } )
    def test_consts_num_whole ( self ) :
        ae = self . assertEqual
        r = self . rec
        ae ( r ( 'consts test1\n const1 11\n' ) ,
            { 'consts' : { 'test1' : { 'const1' : 11 } } } )
    def test_consts_indent_raises ( self ) :
        ar = self . assertRaises
        r = self . rec
        ar ( recognizer . exception , r , 'consts test1\nconst1 11\n' )
        ar ( recognizer . exception , r , 'consts test1\n const1 11\nconst2 11\n' )

if __name__ == '__main__' :
    unittest . main ( )
