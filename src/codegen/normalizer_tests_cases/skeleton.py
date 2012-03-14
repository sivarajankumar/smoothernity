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
                , 'receive' : { 'rcv1' : { } } } }
            , 'messages' : { 'test2' : { } } } ) ,
            { 'stateless' :
                { 'test1' : { 'proc' : { } }
                , 'test2' : { 'proc' : { } } }
            , 'trace' :
                { 'test1' : { 'proc' : { } }
                , 'test2' : { 'proc' : { } } }
            , 'vars' :
                { 'test1' : [ ]
                , 'test2' : [ ] }
            , 'consts' :
                { 'test1' : { }
                , 'test2' : { } }
            , 'types' :
                { 'test1' : { }
                , 'test2' : { } }
            , 'platform_procs' : { }
            , 'platform_consts' : { }
            , 'messages' :
                { 'test1' :
                    { 'request' : { 'req1' : [ ] }
                    , 'reply' : { 'req1' : [ ] }
                    , 'receive' : { 'rcv1' : [ ] } }
                , 'test2' :
                    { 'request' : { } 
                    , 'reply' : { }
                    , 'receive' : { } } }
            , 'module' :
                { 'test1' :
                    { 'module_queue' : ''
                    , 'proc' : { 'proc1' :
                        { 'vars' : [ ] , 'args' : [ ] , 'ops' : [ ] } }
                    , 'request' : { 'req1' : 
                        { 'vars' : [ ] , 'ops' : [ ] } }
                    , 'receive' : { 'rcv1' :
                        { 'vars' : [ ] , 'ops' : [ ] } } }
                , 'test2' :
                    { 'module_queue' : ''
                    , 'proc' : { }
                    , 'request' : { }
                    , 'receive' : { } } } } )
    def test_populate ( self ) :
        ae = self . assertEqual
        r = skeleton . run_populate
        ae ( r (
            { 'somewhere' : { 'test1' : { } }
            , 'platform_procs' : { 'test2' : [ ] }
            , 'platform_consts' : { 'test3' : 1 }
            } ) ,
            { 'consts'    : { 'test1' : { } }
            , 'messages'  : { 'test1' : { } }
            , 'module'    : { 'test1' : { } }
            , 'stateless' : { 'test1' : { } }
            , 'trace'     : { 'test1' : { } }
            , 'types'     : { 'test1' : { } }
            , 'vars'      : { 'test1' : [ ] }
            , 'somewhere' : { 'test1' : { } }
            , 'platform_procs' : { 'test2' : [ ] }
            , 'platform_consts' : { 'test3' : 1 }
            } )
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
                'test2' : { } } } }
            , 'platform_procs' : { 'test3' : [ ] } 
            , 'platform_consts' : { 'test4' : 1 } } ) ,
            { 'anywhere' : { 'test1' : { 'proc' : {
                'test2' : { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] } } } }
            , 'platform_procs' : { 'test3' : [ ] } 
            , 'platform_consts' : { 'test4' : 1 } } )
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
