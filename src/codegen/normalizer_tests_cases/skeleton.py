import unittest
from normalizer import skeleton

class skeleton_test_case ( unittest . TestCase ) :
    def test_all ( self ) :
        ae = self . assertEqual
        r = skeleton . run
        ae ( r (
            { 'module' : { 'test1' :
                { 'proc' : { 'proc1' : { } }
                , 'request' : { 'req1' : { } }
                , 'receive' : { 'rcv1' : { } } } } } ) ,
            { 'stateless' : { }
            , 'trace' : { }
            , 'vars' : { }
            , 'consts' : { }
            , 'types' : { }
            , 'platform_procs' : { }
            , 'platform_consts' : { }
            , 'messages' : { 'test1' :
                { 'request' : { 'req1' : [ ] }
                , 'reply' : { 'req1' : [ ] }
                , 'receive' : { 'rcv1' : [ ] } } }
            , 'module' : { 'test1' :
                { 'module_queue' : ''
                , 'proc' : { 'proc1' :
                    { 'vars' : [ ]
                    , 'args' : [ ]
                    , 'ops' : [ ] } }
                , 'request' : { 'req1' : 
                    { 'vars' : [ ]
                    , 'ops' : [ ] } }
                , 'receive' : { 'rcv1' :
                    { 'vars' : [ ]
                    , 'ops' : [ ] } } } } } )
    def test_outermost ( self ) :
        ae = self . assertEqual
        r = skeleton . run_outermost
        ae ( r ( { } ) ,
            { 'consts' : { }
            , 'messages' : { }
            , 'module' : { }
            , 'platform_consts' : { }
            , 'platform_procs' : { }
            , 'stateless' : { }
            , 'trace' : { }
            , 'types' : { }
            , 'vars' : { }
            } )
    def test_stateless ( self ) :
        ae = self . assertEqual
        r = skeleton . run_stateless
        ae ( r ( { 'stateless' : { 'test1' : { } } } ) ,
            { 'stateless' : { 'test1' : { 'proc' : { } } } } )
    def test_trace ( self ) :
        ae = self . assertEqual
        r = skeleton . run_trace
        ae ( r ( { 'trace' : { 'test1' : { } } } ) ,
            { 'trace' : { 'test1' : { 'proc' : { } } } } )
    def test_module ( self ) :
        ae = self . assertEqual
        r = skeleton . run_module
        ae ( r ( { 'module' : { 'test1' : { } } } ) ,
            { 'module' : { 'test1' :
                { 'module_queue' : ''
                , 'proc' : { }
                , 'receive' : { }
                , 'request' : { } } } } )
    def test_messages ( self ) :
        ae = self . assertEqual
        r = skeleton . run_messages
        ae ( r ( { 'messages' : { 'test1' : { } } } ) ,
            { 'messages' : { 'test1' : 
                { 'receive' : { }
                , 'request' : { }
                , 'reply' : { } } } } )
    def test_procs ( self ) :
        ae = self . assertEqual
        r = skeleton . run_procs
        ae ( r (
            { 'anywhere' : { 'test1' : { 'proc' : {
                'test2' : { } } } } } ) ,
            { 'anywhere' : { 'test1' : { 'proc' : {
                'test2' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] }
            } } } } )
    def test_module_request ( self ) :
        ae = self . assertEqual
        r = skeleton . run_module_request
        ae ( r (
            { 'module' : { 'test1' : { 'request' : {
                'test2' : { } } } } } ) ,
            { 'messages' : { 'test1' : 
                { 'request' : { 'test2' : [ ] }
                , 'reply' : { 'test2' : [ ] } } } 
            , 'module' : { 'test1' : { 'request' : {
                'test2' : { } } } } } )
    def test_module_receive ( self ) :
        ae = self . assertEqual
        r = skeleton . run_module_receive
        ae ( r (
            { 'module' : { 'test1' : { 'receive' : {
                'test2' : { } } } } } ) ,
            { 'messages' : { 'test1' :
                { 'receive' : { 'test2' : [ ] } } }
            , 'module' : { 'test1' : { 'receive' : {
                'test2' : { } } } } } )
