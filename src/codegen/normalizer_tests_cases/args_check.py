from normalizer . args_check import run
from normalizer . skeleton import run as rskel
from normalizer . exception import exception
import unittest

class args_check_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        s = rskel (
            { 'path1' : { 'path2' :
                { 'check' : [ 'func1' , 'unknown' ] } } } )
        try :
            run ( 'check' , s )
        except exception as e :
            ae = self . assertEqual
            ae ( e . get_path ( )  , [ 'path1' , 'path2' ] )
            ae ( e . get_src ( )  , s )
        else :
            self . fail ( )
    def test_success ( self ) :
        s = rskel (
            { 'platform_consts' : { 'const1' : 1 }
            , 'path1' : { 'path2' :
                { 'vars' : [ { 'var1' : { } } ]
                , 'ops' :   
                    [ { 'check' : [ 'func1' , 'const1' , 'var1' ] }
                    ] } } } )
        ae = self . assertEqual
        ae ( run ( 'check' , s ) , s )
