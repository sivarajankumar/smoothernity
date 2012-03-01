def _extract_stateless_procs ( storage ) :
    res = { }
    if 'stateless' in storage :
        for k , v in storage [ 'stateless' ] . items ( ) :
            for kk , vv in v [ 'proc' ] . items ( ) :
                res [ '%s_stateless_%s' % ( k , kk ) ] = vv
    return res

def _extract_trace_procs ( storage ) :
    res = { }
    if 'trace' in storage :
        for k , v in storage [ 'trace' ] . items ( ) :
            for kk , vv in v [ 'proc' ] . items ( ) :
                res [ '%s_trace_%s' % ( k , kk ) ] = vv
    return res

def _extract_platform_procs ( storage ) :
    if 'platform_procs' in storage :
        return storage [ 'platform_procs' ]
    else :
        return { }

class explorer :
    def __init__ ( self , storage ) :
        self . _storage = storage
        self . _platform_procs = _extract_platform_procs ( storage )
        self . _stateless_procs = _extract_stateless_procs ( storage )
        self . _trace_procs = _extract_trace_procs ( storage )
    def get_platform_procs ( self ) :
        return self . _platform_procs
    def get_stateless_procs ( self ) :
        return self . _stateless_procs
    def get_trace_procs ( self ) :
        return self . _trace_procs
