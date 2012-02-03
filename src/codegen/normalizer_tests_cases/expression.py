import normalizer
import unittest

class expression_test_case ( unittest . TestCase ) :
    def setUp ( self ) :
        self . n = normalizer . normalizer ( )
    def test_raises ( self ) :
        ar = self . assertRaises
        r = self . n . run
        ne = normalizer . exception
        ar ( ne , r , { 'consts' : { 'test1' : { 'test2' : '[ 1 + ]' } } } )
    def test_exception_path ( self ) :
        ae = self . assertEqual
        r = self . n . run
        try :
            r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 + ]' } } } )
        except Exception as e :
            pass
        ae ( e . get_path ( ) , [ 'consts' , 'test1' , 'test2' ] )
    def test_unicode ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : u'[ 1 ]' } } } ) ,
            { 'consts' : { 'test1' : { 'test2' : 1 } } } )
    def test_number ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 ]' } } } ) ,
            { 'consts' : { 'test1' : { 'test2' : 1 } } } )
    def test_math ( self ) :
        ae = self . assertEqual
        r = self . n . run
        ae ( r ( { 'consts' : { 'test1' : { 'test2' : '[ 1 + 1 ]' } } } ) ,
            { 'consts' : { 'test1' : { 'test2' : 2 } } } )
