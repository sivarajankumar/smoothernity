from normalizer . calls import run
from normalizer . skeleton import run as rskel
import unittest

class calls_test_case ( unittest . TestCase ) :
    def test_split_args ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( rskel (
            { 'stateless' : { 'st1' : { 'proc' :
                { 'proc1' : { 'args' : [ { } ] }
                , 'proc2' : { 'ops' :
                    [ { 'call' : [ 'proc1' , 'a1' , 'a2' ] }
                ] } } } } } ) ) , rskel (
            { 'stateless' : { 'st1' : { 'proc' :
                { 'proc1' : { 'args' : [ { } ] }
                , 'proc2' : { 'ops' :
                    [ { 'call' : [ 'proc1' , 'a1' ] }
                    , { 'call' : [ 'proc1' , 'a2' ] }
                ] } } } } } ) )
