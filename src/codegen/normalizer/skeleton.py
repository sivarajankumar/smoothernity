from utils import merge

def run ( src ) :
    res = src
    res = run_outermost ( res )
    res = run_stateless ( res )
    res = run_trace ( res )
    res = run_module ( res )
    res = run_module_receive ( res )
    res = run_module_request ( res )
    res = run_messages ( res )
    res = run_procs ( res )
    res = run_message_handlers ( res )
    return res

def run_outermost ( src ) :
    return merge (
        { 'consts' : { } , 'messages' : { } , 'types' : { }
        , 'vars' : { } , 'module' : { } , 'stateless' : { }
        , 'trace' : { } , 'platform_consts' : { }
        , 'platform_procs' : { } } , src )

def run_stateless ( src ) :
    return run_some_storage ( src , 'stateless' , { 'proc' : { } } )

def run_trace ( src ) :
    return run_some_storage ( src , 'trace' , { 'proc' : { } } )

def run_module ( src ) :
    return run_some_storage ( src , 'module' , 
        { 'proc' : { } , 'receive' : { }
        , 'request' : { } , 'module_queue' : '' } )

def run_module_request ( src ) :
    return reduce ( merge ,
        [ { 'messages' : { k :
            { 'request' : { kk : [ ] }
            , 'reply'   : { kk : [ ] } } } }
        for k , v in src [ 'module' ] . items ( )
            for kk in v [ 'request' ] . keys ( ) ] ,
        src )

def run_module_receive ( src ) :
    return reduce ( merge ,
        [ { 'messages' : { k : { 'receive' : { kk : [ ] } } } }
        for k , v in src [ 'module' ] . items ( )
            for kk in v [ 'receive' ] . keys ( ) ] ,
        src )

def run_messages ( src ) :
    return run_some_storage ( src , 'messages' , 
        { 'receive' : { } , 'reply' : { } , 'request' : { } } )

def run_procs ( src ) :
    return reduce ( merge ,
        [ { k : { kk : { 'proc' : { kkk :
            { 'args' : [ ]
            , 'vars' : [ ]
            , 'ops'  : [ ] } } } } }
        for k , v in src . items ( )
            for kk , vv in v . items ( )
                if 'proc' in vv
                    for kkk in vv [ 'proc' ] . keys ( ) ] ,
        src )

def run_message_handlers ( src ) :
    return reduce ( merge ,
        [ { 'module' : { k : { kk : { kkk :
            { 'vars' : [ ]
            , 'ops'  : [ ] } } } } }
        for k , v in src [ 'module' ] . items ( )
            for kk in [ 'request' , 'receive' ]
                for kkk in v [ kk ] . keys ( ) ] ,
        src )

def run_some_storage ( src , what , skel ) :
    return reduce ( merge ,
        [ { what : { k : skel } }
            for k in src [ what ] . keys ( ) ] ,
        src )
