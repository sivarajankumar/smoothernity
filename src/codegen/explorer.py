from utils import merge

class explorer :
    def __init__ ( self , storage ) :
        self . _storage = storage
        self . _messages_receives = _extract_messages_receives ( storage )
        self . _platform_consts = _extract_platform_consts ( storage )
        self . _platform_procs = _extract_platform_procs ( storage )
        self . _stateless_procs = _extract_stateless_procs ( storage )
        self . _trace_procs = _extract_trace_procs ( storage )
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
    def get_callables ( self , path ) :
        return reduce ( merge ,
            [ self . get_local_procs ( path )
            , self . get_local_stateless_procs ( path )
            , self . get_local_trace_procs ( path )
            , self . get_platform_procs ( )
            , self . get_stateless_procs ( )
            , self . get_trace_procs ( )
            ] , { } )
    def get_consts ( self , path ) :
        return reduce ( merge ,
            [ self . get_platform_consts ( )
            ] , { } )
    def get_everything ( self , path ) :
        return reduce ( merge ,
            [ self . get_callables ( path )
            , self . get_consts ( path )
            , self . get_messages_receives ( )
            ] , { } )

def _extract_stateless_procs ( storage ) :
    res = { }
    for k , v in storage [ 'stateless' ] . items ( ) :
        for kk , vv in v [ 'proc' ] . items ( ) :
            res [ '%s_stateless_%s' % ( k , kk ) ] = vv
    return res

def _extract_trace_procs ( storage ) :
    res = { }
    for k , v in storage [ 'trace' ] . items ( ) :
        for kk , vv in v [ 'proc' ] . items ( ) :
            res [ '%s_trace_%s' % ( k , kk ) ] = vv
    return res

def _extract_platform_consts ( storage ) :
    return storage [ 'platform_consts' ]

def _extract_platform_procs ( storage ) :
    return storage [ 'platform_procs' ]

def _extract_messages_receives ( storage ) :
    res = { }
    for k , v in storage [ 'messages' ] . items ( ) :
        for kk , vv in v [ 'receive' ] . items ( ) :
            res [ '%s_%s' % ( k , kk ) ] = vv
    return res

def _extract_local_some_procs ( storage , path , some ) :
    res = { }
    for kk , vv in storage [ some ] [ path [ 1 ] ] [ 'proc' ] . items ( ) :
        res [ '%s_%s' % ( some , kk ) ] = vv
    return res

def _extract_local_procs ( storage , path ) :
    return storage [ path [ 0 ] ] [ path [ 1 ] ] [ 'proc' ]
