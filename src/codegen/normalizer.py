import operator

class exception ( Exception ) :
    def __init__ ( self , text , src , path ) :
        Exception . __init__ ( self , text )
        self . _path = path
        self . _src = src
    def get_path ( self ) :
        return self . _path
    def get_src ( self ) :
        return self . _src

class const_value :
    def __init__ ( self , v , env ) :
        self . _v , self . _env = v , env
    def value ( self ) :
        v = self . _v
        if type ( v ) in ( str , unicode ) :
            assert ( v [ 0 ] , v [ - 1 ] ) == ( '[' , ']' )
            ev = eval ( v [ 1 : - 1 ] , self . _env )
            return ev . value ( ) if isinstance ( ev , const_value ) else ev
        else :
            return v
    def _calc ( self , a , b , op ) :
        return op \
            ( a . value ( ) if isinstance ( a , const_value ) else a
            , b . value ( ) if isinstance ( b , const_value ) else b )
    def __add__ ( self , a ) :
        return self . _calc ( self , a , operator . add )
    def __radd__ ( self , a ) :
        return self . _calc ( a , self , operator . add )
    def __sub__ ( self , a ) :
        return self . _calc ( self , a , operator . sub )
    def __rsub__ ( self , a ) :
        return self . _calc ( a , self , operator . sub )
    def __mul__ ( self , a ) :
        return self . _calc ( self , a , operator . mul )
    def __rmul__ ( self , a ) :
        return self . _calc ( a , self , operator . mul )
    def __lshift__ ( self , a ) :
        return self . _calc ( self , a , operator . lshift )
    def __rlshift__ ( self , a ) :
        return self . _calc ( a , self , operator . lshift )
    def __rshift__ ( self , a ) :
        return self . _calc ( self , a , operator . rshift )
    def __rrshift__ ( self , a ) :
        return self . _calc ( a , self , operator . rshift )
    def __div__ ( self , a ) :
        return self . _calc ( self , a , operator . div )
    def __rdiv__ ( self , a ) :
        return self . _calc ( a , self , operator . div )
    def __mod__ ( self , a ) :
        return self . _calc ( self , a , operator . mod )
    def __rmod__ ( self , a ) :
        return self . _calc ( a , self , operator . mod )
    def __pow__ ( self , a ) :
        return self . _calc ( self , a , operator . pow )
    def __rpow__ ( self , a ) :
        return self . _calc ( a , self , operator . pow )
    def __and__ ( self , a ) :
        return self . _calc ( self , a , operator . and_ )
    def __rand__ ( self , a ) :
        return self . _calc ( a , self , operator . and_ )
    def __or__ ( self , a ) :
        return self . _calc ( self , a , operator . or_ )
    def __ror__ ( self , a ) :
        return self . _calc ( a , self , operator . or_ )
    def __xor__ ( self , a ) :
        return self . _calc ( self , a , operator . xor )
    def __rxor__ ( self , a ) :
        return self . _calc ( a , self , operator . xor )

class normalizer :
    def __init__ ( self ) :
        self . _bind_funcs = { }
        self . _src = None
    def bind_func ( self , func , args ) :
        self . _bind_funcs [ func ] = args
    def run ( self , src ) :
        self . _src = src
        self . _src = self . _norm_consts ( self . _src )
        self . _src = self . _norm_calls ( self . _src )
        return self . _src
    def _norm_calls ( self , src , path = [ ] ) :
        if isinstance ( src , dict ) :
            res = dict ( )
            for k , v in src . items ( ) :
                res [ k ] = self . _norm_calls ( v , path + [ k ] )
        elif isinstance ( src , list ) :
            res = list ( )
            for iv in xrange ( len ( src ) ) :
                v = src [ iv ]
                if isinstance ( v , dict ) and 'call' in v :
                    func = v [ 'call' ] [ 0 ]
                    args = v [ 'call' ] [ 1 : ]
                    bind_args = self . _bind_funcs [ func ]
                    while args :
                        split_args = [ ]
                        for i in xrange ( len ( bind_args ) ) :
                            if not args :
                                raise exception ( 'Need %i more args' %
                                    ( len ( bind_args ) - i - 1 ) ,
                                    self . _src , path + [ iv ] )
                            split_args . append ( args [ 0 ] )
                            args = args [ 1 : ]
                        res . append ( { 'call' : [ func ] + split_args } )
                else :
                    res . append ( self . _norm_calls ( v ) )
        else :
            res = src
        return res
    def _norm_consts ( self , src ) :
        res = dict ( )
        for root_k , root_v in src . items ( ) :
            if root_k == 'consts' :
                res [ 'consts' ] = dict ( )
                env = dict ( )
                for module , consts in src [ 'consts' ] . items ( ) :
                    for k , v in consts . items ( ) :
                        env [ module + '_consts_' + k ] = const_value ( v , env )
                for module , consts in src [ 'consts' ] . items ( ) :
                    for k , v in consts . items ( ) :
                        env [ k ] = const_value ( v , env )
                    res [ 'consts' ] [ module ] = dict ( )
                    for k in sorted ( consts . keys ( ) ) :
                        try :
                            res [ 'consts' ] [ module ] [ k ] = \
                                env [ k ] . value ( )
                        except Exception as e :
                            raise exception ( str ( e ) , src ,
                                [ 'consts' , module , k ] )
            else :
                res [ root_k ] = root_v
        return res
