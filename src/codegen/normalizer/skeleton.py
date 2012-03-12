from utils import merge

def run ( src ) :
    res = src
    res = run_outmost ( res )
    res = run_stateless ( res )
    res = run_trace ( res )
    res = run_module ( res )
    res = run_module_receive ( res )
    res = run_module_request ( res )
    res = run_messages ( res )
    for k , v in res . items ( ) :
        for kk , vv in v . items ( ) :
            if 'proc' in vv :
                for kkk , vvv in vv [ 'proc' ] . items ( ) :
                    res [ k ] [ kk ] [ 'proc' ] [ kkk ] = merge (
                        { 'args' : [ ] , 'vars' : [ ] , 'ops' : [ ] }
                        , vvv )
    for k , v in res [ 'module' ] . items ( ) :
        for kk in [ 'request' , 'receive' ] :
            for kkk , vvv in v [ kk ] . items ( ) :
                res [ 'module' ] [ k ] [ kk ] [ kkk ] = merge (
                    { 'vars' : [ ] , 'ops' : [ ] } , vvv )
    return res

def run_outmost ( src ) :
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

def run_some_storage ( src , what , skel ) :
    return merge ( { what : dict (
        [ ( k , skel ) for k in src [ what ] . keys ( ) ] ) } , src )
