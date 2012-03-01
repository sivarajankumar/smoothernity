def _extract_stateless_procs ( storage ) :
    res = { }
    if 'stateless' in storage :
        for k , v in storage [ 'stateless' ] . items ( ) :
            for kk , vv in v [ 'proc' ] . items ( ) :
                res [ '%s_stateless_%s' % ( k , kk ) ] = vv
    return res

class explorer :
    def __init__ ( self , storage ) :
        self . _storage = storage
        self . _stateless_procs = _extract_stateless_procs ( storage )
    def get_stateless_procs ( self ) :
        return self . _stateless_procs
