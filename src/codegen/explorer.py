from utils import merge

class explorer :
    def __init__ ( self , storage ) :
        self . _storage = storage
        self . _global_consts = _extract_global_consts ( storage )
        self . _messages_receives = _extract_messages_receives ( storage )
        self . _platform_consts = _extract_platform_consts ( storage )
        self . _platform_procs = _extract_platform_procs ( storage )
        self . _stateless_procs = _extract_stateless_procs ( storage )
        self . _trace_procs = _extract_trace_procs ( storage )
    def get_global_consts ( self ) :
        return self . _global_consts
    def get_global_vars ( self , path ) :
        return _extract_global_vars ( self . _storage , path )
    def get_local_consts ( self , path ) :
        return _extract_local_consts ( self . _storage , path )
    def get_messages_receives ( self ) :
        return self . _messages_receives
    def get_platform_consts ( self ) :
        return self . _platform_consts
    def get_platform_procs ( self ) :
        return self . _platform_procs
    def get_stateless_procs ( self ) :
        return self . _stateless_procs
    def get_trace_procs ( self ) :
        return self . _trace_procs
    def get_local_procs ( self , path ) :
        return _extract_local_procs ( self . _storage , path )
    def get_local_stateless_procs ( self , path ) :
        return _extract_local_some_procs \
            ( self . _storage , path , 'stateless' )
    def get_local_trace_procs ( self , path ) :
        return _extract_local_some_procs \
            ( self . _storage , path , 'trace' )
    def get_local_args ( self , path ) :
        return _extract_local_values ( self . _storage , path , 'args' )
    def get_local_vars ( self , path ) :
        return _extract_local_values ( self . _storage , path , 'vars' )
    def get_callables ( self , path ) :
        return _glue (
            [ self . get_local_procs ( path )
            , self . get_local_stateless_procs ( path )
            , self . get_local_trace_procs ( path )
            , self . get_platform_procs ( )
            , self . get_stateless_procs ( )
            , self . get_trace_procs ( )
            ] , { } )
    def get_consts ( self , path ) :
        return _glue (
            [ self . get_global_consts ( )
            , self . get_local_consts ( path )
            , self . get_platform_consts ( )
            ] , { } )
    def get_values ( self , path ) :
        return _glue (
            [ self . get_global_vars ( path )
            , self . get_local_vars ( path )
            , self . get_local_args ( path )
            ] , { } )
    def get_everything ( self , path ) :
        return _glue (
            [ self . get_callables ( path )
            , self . get_consts ( path )
            , self . get_messages_receives ( )
            , self . get_values ( path )
            ] , { } )

def _glue ( items , first ) :
    return reduce ( merge , items , first )

def _extract_stateless_procs ( storage ) :
    res = [ ]
    for k , v in storage [ 'stateless' ] . items ( ) :
        for kk , vv in v [ 'proc' ] . items ( ) :
            res . append ( { '%s_stateless_%s' % ( k , kk ) : vv } )
    return _glue ( res , { } )

def _extract_trace_procs ( storage ) :
    res = [ ]
    for k , v in storage [ 'trace' ] . items ( ) :
        for kk , vv in v [ 'proc' ] . items ( ) :
            res . append ( { '%s_trace_%s' % ( k , kk ) : vv } )
    return _glue ( res , { } )

def _extract_platform_consts ( storage ) :
    return storage [ 'platform_consts' ]

def _extract_platform_procs ( storage ) :
    return storage [ 'platform_procs' ]

def _extract_messages_receives ( storage ) :
    res = [ ]
    for k , v in storage [ 'messages' ] . items ( ) :
        for kk , vv in v [ 'receive' ] . items ( ) :
            res . append ( { '%s_%s' % ( k , kk ) : vv } )
    return _glue ( res , { } )

def _extract_local_some_procs ( storage , path , some ) :
    res = [ ]
    for kk , vv in storage [ some ] [ path [ 1 ] ] [ 'proc' ] . items ( ) :
        res . append ( { '%s_%s' % ( some , kk ) : vv } )
    return _glue ( res , { } )

def _extract_local_procs ( storage , path ) :
    return storage [ path [ 0 ] ] [ path [ 1 ] ] [ 'proc' ]

def _extract_global_consts ( storage ) :
    res = [ ]
    for k , v in storage [ 'consts' ] . items ( ) :
        for kk , vv in v . items ( ) :
            res . append ( { '%s_consts_%s' % ( k , kk ) : vv } )
    return _glue ( res , { } )

def _extract_local_consts ( storage , path ) :
    res = [ ]
    for k , v in storage [ 'consts' ] [ path [ 1 ] ] . items ( ) :
        if path [ 0 ] == 'consts' :
            res . append ( { '%s' % k : v } )
        else :
            res . append ( { 'consts_%s' % k : v } )
    return _glue ( res , { } )

def _extract_global_vars ( storage , path ) :
    return _glue ( storage [ 'vars' ] [ path [ 1 ] ] , { } )

def _extract_local_values ( storage , path , some ) :
    res = { }
    cur = storage
    for p in path :
        cur = cur [ p ]
        if some in cur :
            res = _glue ( cur [ some ] , res )
    return res
