import unittest
from normalizer . skeleton import run
from utils import merge

def mroot ( x ) :
    return merge (
        { 'consts' : { }
        , 'messages' : { }
        , 'module' : { }
        , 'platform_consts' : { }
        , 'platform_procs' : { }
        , 'stateless' : { }
        , 'trace' : { }
        , 'types' : { }
        , 'vars' : { }
        } , x )

def mmod ( x ) :
    return merge (
        { 'module_queue' : ''
        , 'proc' : { }
        , 'receive' : { }
        , 'request' : { }
        } , x )

def mproc ( x ) :
    return merge (
        { 'vars' : [ ]
        , 'args' : [ ]
        , 'ops' : [ ]
        } , x )

def mmsg ( x ) :
    return merge (
        { 'receive' : { }
        , 'reply' : { }
        , 'request' : { }
        } , x )

class skeleton_test_case ( unittest . TestCase ) :
    def test_empty ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { } ) , mroot ( { } ) )
    def test_stateless ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { 'stateless' : { 'test1' : { } } } ) ,
            mroot ( { 'stateless' : { 'test1' : { 'proc' : { } } } } ) )
    def test_trace ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { 'trace' : { 'test1' : { } } } ) ,
            mroot ( { 'trace' : { 'test1' : { 'proc' : { } } } } ) )
    def test_module ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { 'module' : { 'test1' : { } } } ) ,
            mroot ( { 'module' : { 'test1' : mmod ( { } ) } } ) )
    def test_messages ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { 'messages' : { 'test1' : { } } } ) ,
            mroot ( { 'messages' : { 'test1' : mmsg ( { } ) } } ) )
    def test_proc ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : { } } } } } ) ,
            mroot ( { 'anywhere' : { 'test1' : { 'proc' : {
            'test2' : mproc ( { } )
            } } } } ) )
    def test_request ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { 'module' : { 'test1' : { 'request' : {
            'test2' : { } } } } } ) ,
            mroot (
                { 'messages' : { 'test1' : mmsg (
                    { 'request' : { 'test2' : [ ] }
                    , 'reply' : { 'test2' : [ ] } } ) } 
                , 'module' : { 'test1' : mmod (
                    { 'request' : { 'test2' :
                        { 'vars' : [ ] , 'ops' : [ ] }
                } } ) } } ) )
    def test_receive ( self ) :
        ae = self . assertEqual
        r = run
        ae ( r ( { 'module' : { 'test1' : { 'receive' : {
            'test2' : { } } } } } ) ,
            mroot (
                { 'messages' : { 'test1' : mmsg (
                    { 'receive' : { 'test2' : [ ] } } ) }
                , 'module' : { 'test1' : mmod (
                    { 'receive' : { 'test2' :
                        { 'vars' : [ ] , 'ops' : [ ] }
                } } ) } } ) )
