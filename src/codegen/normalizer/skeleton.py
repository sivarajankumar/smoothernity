from utils import merge

def run ( src ) :
    res = src
    res = run_outmost ( res )
    res = run_stateless ( res )
    res = run_trace ( res )
    for k , v in res [ 'module' ] . items ( ) :
        res [ 'module' ] [ k ] = merge (
            { 'proc' : { } , 'receive' : { }
            , 'request' : { } , 'module_queue' : '' } , v )
    for k , v in res [ 'module' ] . items ( ) :
        for kk in v [ 'request' ] . keys ( ) :
            res = merge ( { 'messages' : { k :
                { 'request' : { kk : [ ] }
                , 'reply' : { kk : [ ] } } } } , res )
        for kk in v [ 'receive' ] . keys ( ) :
            res = merge ( { 'messages' : { k :
                { 'receive' : { kk : [ ] } } } } , res )
    for k , v in res [ 'messages' ] . items ( ) :
        res [ 'messages' ] [ k ] = merge (
            { 'receive' : { } , 'reply' : { } , 'request' : { } } , v )
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

def run_some_storage ( src , what , skel ) :
    return merge ( { what : dict (
        [ ( k , skel ) for k in src [ what ] . keys ( ) ] ) } , src )
