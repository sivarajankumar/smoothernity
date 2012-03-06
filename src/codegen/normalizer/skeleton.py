from utils import merge

def run ( src ) :
    res = merge (
        { 'consts' : { } , 'messages' : { } , 'types' : { }
        , 'vars' : { } , 'module' : { } , 'stateless' : { }
        , 'trace' : { } , 'platform_consts' : { }
        , 'platform_procs' : { } } , src )
    for k , v in res [ 'stateless' ] . items ( ) :
        res [ 'stateless' ] [ k ] = merge ( { 'proc' : { } } , v )
    for k , v in res [ 'trace' ] . items ( ) :
        res [ 'trace' ] [ k ] = merge ( { 'proc' : { } } , v )
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
