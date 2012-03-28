from normalizer . sends import run
from normalizer . skeleton import run as rskel
import unittest

class sends_test_case ( unittest . TestCase ) :
    def test_split_args ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( rskel (
            { 'messages' : { 'test1' : 
                { 'receive' : { 'msg1' : [ { } , { } ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : 
                { 'ops' : [ { 'send' :
                    [ 'test1_msg1' , 'a1' , 'a2' , 'a3' , 'a4' ] } ]
            } } } } } ) ) , rskel (
            { 'messages' : { 'test1' : 
                { 'receive' : { 'msg1' : [ { } , { } ] } } }
            , 'stateless' : { 'st1' : { 'proc' : { 'proc1' : 
                { 'ops' :
                    [ { 'send' : [ 'test1_msg1' , 'a1' , 'a2' ] }
                    , { 'send' : [ 'test1_msg1' , 'a3' , 'a4' ] }
            ] } } } } } ) )
