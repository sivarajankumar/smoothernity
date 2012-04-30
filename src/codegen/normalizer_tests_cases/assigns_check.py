from normalizer . assigns_check import run
from normalizer . exception import exception
import unittest

class assigns_check_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        r = run
        ne = exception
        ar = self . assertRaises
        ar ( ne , r ,
            { 'platform_consts' : { 'const1' : 1 }
            , 'anywhere' : { 'anywhere' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' : [ { 'assign' :
                    { 'from' : [ 'var1' ]
                    , 'to' : [ 'const1' ]
                    } } ] } } } )
    def test_exception_args ( self ) :
        pass
    def test_correct ( self ) :
        pass
