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
        self . _types = _extract_types ( storage )
        self . _fields = _extract_fields ( storage )
    def get_fields ( self ) :
        return self . _fields
    def get_types ( self ) :
        return self . _types
    def get_global_consts ( self ) :
        return self . _global_consts
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
    def get_global_vars ( self , path ) :
        return _extract_global_vars ( self . _storage , path )
    def get_local_consts ( self , path ) :
        return _extract_local_consts ( self . _storage , path )
    def get_message_receive_args ( self , path ) :
        return _extract_message_receive_args ( self . _storage , path )
    def get_message_request_args ( self , path ) :
        return _extract_message_request_args ( self . _storage , path )
    def get_message_reply_args ( self , path ) :
        return _extract_message_reply_args ( self . _storage , path )
    def get_local_procs ( self , path ) :
        return _extract_local_procs ( self . _storage , path )
    def get_local_stateless_procs ( self , path ) :
        return _extract_local_stateless_procs ( self . _storage , path )
    def get_local_trace_procs ( self , path ) :
        return _extract_local_trace_procs ( self . _storage , path )
    def get_local_args ( self , path ) :
        return _extract_local_args ( self . _storage , path )
    def get_local_vars ( self , path ) :
        return _extract_local_vars ( self . _storage , path )
    def get_callables ( self , path ) :
        return _glue (
            [ self . get_local_procs ( path )
            , self . get_local_stateless_procs ( path )
            , self . get_local_trace_procs ( path )
            , self . get_platform_procs ( )
            , self . get_stateless_procs ( )
            , self . get_trace_procs ( )
            ] , { } )
    def get_readables ( self , path ) :
        return _glue (
            [ self . get_global_vars ( path )
            , self . get_local_vars ( path )
            , self . get_local_args ( path )
            , self . get_message_receive_args ( path )
            , self . get_message_request_args ( path )
            ] , { } )
    def get_writables ( self , path ) :
        return _glue (
            [ self . get_global_vars ( path )
            , self . get_local_vars ( path )
            , self . get_local_args ( path )
            , self . get_message_reply_args ( path )
            ] , { } )
    def get_consts ( self , path ) :
        return _glue (
            [ self . get_global_consts ( )
            , self . get_local_consts ( path )
            , self . get_platform_consts ( )
            ] , { } )
    def get_values ( self , path ) :
        # should be gone
        return _glue (
            [ self . get_global_vars ( path )
            , self . get_local_vars ( path )
            , self . get_local_args ( path )
            , self . get_message_receive_args ( path )
            , self . get_message_request_args ( path )
            , self . get_message_reply_args ( path )
            ] , { } )
    def get_everything ( self , path ) :
        return _glue (
            [ self . get_callables ( path )
            , self . get_consts ( path )
            , self . get_messages_receives ( )
            , self . get_values ( path )
            ] , { } )
    def split_value_fields ( self , path , value ) :
        def _walk ( fs , acc ) :
            return [ x
                for i in xrange ( len ( fs ) )
                    for x in _walk ( fs [ i + 1 : ]
                                   , acc + [ '_' . join ( fs [ : i + 1 ] ) ] )
                        if '_' . join ( fs [ : i + 1 ] )
                            in self . get_fields ( ) ] \
                if fs else [ acc ]
        ps = value . split ( '_' )
        return [ x
            for i in xrange ( len ( ps ) )
                for x in _walk ( ps [ i + 1 : ]
                               , [ '_' . join ( ps [ : i + 1 ] ) ] )
                    if '_' . join ( ps [ : i + 1 ] ) \
                        in self . get_values ( path ) ]

def _glue ( items , first ) :
    return reduce ( lambda x , y : merge ( x , y , overwrite = False ) ,
        items , first )

def _combine ( items , first ) :
    return reduce ( lambda x , y : merge ( x , y , overwrite = True ) ,
        items , first )

def _traverse ( storage , path , some ) :
    def _walk ( s , p , x ) :
        return _glue ( s [ x ] , { } ) \
            if x in s else _walk ( s [ p [ 0 ] ] , p [ 1 : ] , x ) \
                if p else { }
    return _walk ( storage [ path [ 0 ] ] , path [ 1 : ] , some )

def _extract_local_args ( storage , path ) :
    return _traverse ( storage , path , 'args' )

def _extract_local_vars ( storage , path ) :
    return _traverse ( storage , path , 'vars' )

def _extract_stateless_procs ( storage ) :
    return _extract_some_procs ( storage , 'stateless' )

def _extract_trace_procs ( storage ) :
    return _extract_some_procs ( storage , 'trace' )

def _extract_some_procs ( storage , some ) :
    return _glue ( [
        { '%s_%s_%s' % ( k , some , kk ) : vv }
        for k , v in storage [ some ] . items ( )
            for kk , vv in v [ 'proc' ] . items ( )
        ] , { } )

def _extract_platform_consts ( storage ) :
    return storage [ 'platform_consts' ]

def _extract_platform_procs ( storage ) :
    return storage [ 'platform_procs' ]

def _extract_messages_receives ( storage ) :
    return _glue ( [
        { '%s_%s' % ( k , kk ) : vv }
        for k , v in storage [ 'messages' ] . items ( )
            for kk , vv in v [ 'receive' ] . items ( )
        ] , { } )

def _extract_local_stateless_procs ( storage , path ) :
    return _extract_local_some_procs ( storage , path , 'stateless' )

def _extract_local_trace_procs ( storage , path ) :
    return _extract_local_some_procs ( storage , path , 'trace' )

def _extract_local_some_procs ( storage , path , some ) :
    return _glue ( [
        { '%s_%s' % ( some , k ) : v }
        for k , v in storage [ some ] [ path [ 1 ] ] [ 'proc' ] . items ( )
        ] , { } )

def _extract_local_procs ( storage , path ) :
    return storage [ path [ 0 ] ] [ path [ 1 ] ] [ 'proc' ] \
        if path [ 0 ] not in ( 'vars' , 'types' ) else { }

def _extract_global_consts ( storage ) :
    return _glue ( [
        { '%s_consts_%s' % ( k , kk ) : vv }
        for k , v in storage [ 'consts' ] . items ( )
            for kk , vv in v . items ( )
        ] , { } )

def _extract_local_consts ( storage , path ) :
    return _glue ( [
        { '%s' % k : v }
            if path [ 0 ] == 'consts' else
        { 'consts_%s' % k : v }
            for k , v in storage [ 'consts' ] [ path [ 1 ] ] . items ( )
        ] , { } )

def _extract_global_vars ( storage , path ) :
    return _glue ( storage [ 'vars' ] [ path [ 1 ] ] , { } )

def _extract_types ( storage ) :
    return _glue ( [
        { '%s_type_%s' % ( k , kk ) : _glue ( vv , { } ) }
        for k , v in storage [ 'types' ] . items ( )
            for kk , vv in v . items ( )
        ] , { } )

def _extract_fields ( storage ) :
    return _combine ( [
        { kkkk : [ '%s_type_%s' % ( k , kk ) ] }
        for k , v in storage [ 'types' ] . items ( )
            for kk , vv in v . items ( )
                for vvv in vv
                    for kkkk in vvv . keys ( )
        ] , { } )

def _extract_message_some_args ( s , p , x , y , prefix ) :
    return dict ( [ ( '%s_%s' % ( prefix , k ) , v )
        for k , v in _traverse ( s ,
            [ 'messages' , p [ 1 ] , x ] , p [ 3 ] ) . items ( )
    ] ) if len ( p ) >= 4 and p [ 2 ] == y else { }

def _extract_message_receive_args ( storage , path ) :
    return _extract_message_some_args \
        ( storage , path , 'receive' , 'receive' , 'msg' )

def _extract_message_request_args ( storage , path ) :
    return _extract_message_some_args \
        ( storage , path , 'request' , 'request' , 'msg' )

def _extract_message_reply_args ( storage , path ) :
    return _extract_message_some_args \
        ( storage , path , 'reply' , 'request' , 'reply' )
