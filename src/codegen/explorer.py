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

def _extract_platform_procs ( storage ) :
    return storage [ 'platform_procs' ]

def _extract_messages_receives ( storage ) :
    res = { }
    for k , v in storage [ 'messages' ] . items ( ) :
        for kk , vv in v [ 'receive' ] . items ( ) :
            res [ '%s_%s' % ( k , kk ) ] = vv
    return res

class explorer :
    def __init__ ( self , storage ) :
        self . _storage = storage
        self . _messages_receives = _extract_messages_receives ( storage )
        self . _platform_procs = _extract_platform_procs ( storage )
        self . _stateless_procs = _extract_stateless_procs ( storage )
        self . _trace_procs = _extract_trace_procs ( storage )
    def get_messages_receives ( self ) :
        return self . _messages_receives
    def get_platform_procs ( self ) :
        return self . _platform_procs
    def get_stateless_procs ( self ) :
        return self . _stateless_procs
    def get_trace_procs ( self ) :
        return self . _trace_procs
    def get_local_procs ( self , path ) :
        return self . _storage [ path [ 0 ] ] [ path [ 1 ] ] [ 'proc' ]
