from normalizer . args_check import run
from normalizer . skeleton import run as rskel
from normalizer . exception import exception
import unittest

class args_check_test_case ( unittest . TestCase ) :
    def test_raise ( self ) :
        r = lambda x , y : run ( 'check' , lambda n , p : n in x , y )
        s = { 'path1' : { 'path2' :
                { 'check' : [ 'func1' , 'a' ] } } }
        try :
            r ( set ( ) , s )
        except exception as e :
            ae = self . assertEqual
            ae ( e . get_path ( )  , [ 'path1' , 'path2' ] )
            ae ( e . get_src ( )  , s )
        else :
            self . fail ( )
    def test_success ( self ) :
        r = lambda x , y : run ( 'check' , lambda n , p : n in x , y )
        s = { 'anywhere' : [ { 'check' : [ 'func1' , 'a1' , 'a2' ] } ] }
        ae = self . assertEqual
        ae ( r ( set ( [ 'a1' , 'a2' ] ) , s ) , s )
