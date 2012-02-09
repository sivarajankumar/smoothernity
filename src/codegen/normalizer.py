import operator
from utils import merge

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
        self . _path = None
    def bind_func ( self , func , args ) :
        self . _bind_funcs [ func ] = args
    def run ( self , src ) :
        self . _src = src
        self . _src = self . _norm_skeleton ( self . _src )
        self . _src = self . _norm_consts ( self . _src )
        self . _src = self . _norm_withs ( self . _src )
        self . _src = self . _norm_calls ( self . _src )
        self . _src = self . _norm_assigns ( self . _src )
        return self . _src
    def _error ( self , text ) :
        raise exception ( text , self . _src , self . _path )
    def _local_proc ( self , name ) :
        what , which = self . _path [ 0 ] , self . _path [ 1 ]
        storage = self . _src [ what ] [ which ]
        if 'proc' in storage and name in storage [ 'proc' ] :
            return storage [ 'proc' ] [ name ]
        else :
            return None
    def _some_proc ( self , what , name ) :
        parts = name . split ( '_%s_' % what )
        if len ( parts ) > 1 :
            which , proc = parts
            if which in self . _src [ what ] :
                procs = self . _src [ what ] [ which ] [ 'proc' ]
                if proc in procs :
                    return procs [ proc ]
                else :
                    self . _error ( "Unknown proc '%s' in %s '%s'" %
                        ( proc , what , which ) )
            else :
                self . _error ( "Unknown %s '%s'" % ( what , which ) )
        else :
            return None
    def _stateless_proc ( self , name ) :
        return self . _some_proc ( 'stateless' , name )
    def _trace_proc ( self , name ) :
        return self . _some_proc ( 'trace' , name )
    def _get_call_args ( self , name ) :
        if name in self . _bind_funcs :
            return self . _bind_funcs [ name ]
        elif self . _local_proc ( name ) :
            return self . _local_proc ( name ) [ 'args' ]
        elif self . _stateless_proc ( name ) :
            return self . _stateless_proc ( name ) [ 'args' ]
        elif self . _trace_proc ( name ) :
            return self . _trace_proc ( name ) [ 'args' ]
        else :
            self . _error ( "Unknown callable entity '%s'" % name )
    def _norm_skeleton ( self , src ) :
        res = merge (
            { 'consts' : { } , 'messages' : { } , 'types' : { }
            , 'vars' : { } , 'module' : { } , 'stateless' : { }
            , 'trace' : { } } , src )
        for k , v in res [ 'stateless' ] . items ( ) :
            res [ 'stateless' ] [ k ] = merge ( { 'proc' : { } } , v )
        for k , v in res [ 'trace' ] . items ( ) :
            res [ 'trace' ] [ k ] = merge ( { 'proc' : { } } , v )
        for k , v in res [ 'module' ] . items ( ) :
            res [ 'module' ] [ k ] = merge (
                { 'proc' : { } , 'receive' : { }
                , 'request' : { } , 'module_queue' : '' } , v )
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
    def _is_callable ( self , name ) :
        return name in self . _bind_funcs
    def _norm_withs ( self , src , path = [ ] , prefixes = [ ] ) :
        if isinstance ( src , dict ) :
            if 'call' in src :
                self . _path = path
                func = src [ 'call' ] [ 0 ]
                args = src [ 'call' ] [ 1 : ]
                candidates = filter ( self . _is_callable ,
                    [ p + func for p in set (
                        [ '' , '' . join ( prefixes ) ] + prefixes ) ] )
                if len ( candidates ) > 1 :
                    self . _error ( 'Ambiguous callables: %s' %
                        ( ', ' . join ( candidates ) ) )
                if candidates :
                    res = { 'call' : candidates + args }
                else :
                    res = src
            elif 'with' in src :
                res = list ( )
                for k , v in src [ 'with' ] . items ( ) :
                    for iv in xrange ( len ( v ) ) :
                        res . append ( self . _norm_withs \
                            ( v [ iv ]
                            , path + [ 'with' , k , iv ]
                            , prefixes + [ k ] ) )
            else :
                res = dict ( )
                for k , v in src . items ( ) :
                    res [ k ] = self . _norm_withs (
                        v , path + [ k ] , prefixes )
        elif isinstance ( src , list ) :
            res = list ( )
            for iv in xrange ( len ( src ) ) :
                v = src [ iv ]
                a = self . _norm_withs (
                    v , path + [ iv ] , prefixes )
                if isinstance ( a , list ) :
                    res += a
                else :
                    res . append ( a )
        else :
            res = src
        return res
    def _norm_assigns ( self , src , path = [ ] ) :
        if isinstance ( src , dict ) :
            res = dict ( )
            for k , v in src . items ( ) :
                res [ k ] = self . _norm_assigns ( v , path + [ k ] )
        elif isinstance ( src , list ) :
            res = list ( )
            for iv in xrange ( len ( src ) ) :
                self . _path = path + [ iv ]
                v = src [ iv ]
                if isinstance ( v , dict ) and 'assign' in v :
                    froms = v [ 'assign' ] [ 'from' ]
                    tos = v [ 'assign' ] [ 'to' ]
                    if len ( tos ) % len ( froms ) > 0 :
                        self . _error ( 'Need %i more assign targets' %
                            ( len ( tos ) % len ( froms ) ) )
                    for i in xrange ( len ( tos ) ) :
                        res . append ( { 'assign' :
                            { 'from' : [ froms [ i % len ( froms ) ] ]
                            , 'to' : [ tos [ i ] ] } } )
                else :
                    res . append ( self . _norm_assigns ( v , self . _path ) )
        else :
            res = src
        return res
    def _norm_calls ( self , src , path = [ ] ) :
        if isinstance ( src , dict ) :
            res = dict ( )
            for k , v in src . items ( ) :
                res [ k ] = self . _norm_calls ( v , path + [ k ] )
        elif isinstance ( src , list ) :
            res = list ( )
            for iv in xrange ( len ( src ) ) :
                self . _path = path + [ iv ]
                v = src [ iv ]
                if isinstance ( v , dict ) and 'call' in v \
                                and len ( v [ 'call' ] ) > 1 :
                    func = v [ 'call' ] [ 0 ]
                    args = v [ 'call' ] [ 1 : ]
                    need_args = self . _get_call_args ( func )
                    if len ( args ) % len ( need_args ) > 0 :
                        self . _error ( 'Need %i more args' % \
                            ( len ( args ) % len ( need_args ) ) )
                    while args :
                        split_args = [ ]
                        for i in xrange ( len ( need_args ) ) :
                            split_args . append ( args [ 0 ] )
                            args = args [ 1 : ]
                        res . append ( { 'call' : [ func ] + split_args } )
                else :
                    res . append ( self . _norm_calls ( v , self . _path ) )
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
                        self . _path = [ 'consts' , module , k ]
                        try :
                            res [ 'consts' ] [ module ] [ k ] = \
                                env [ k ] . value ( )
                        except Exception as e :
                            self . _error ( str ( e ) )
            else :
                res [ root_k ] = root_v
        return res
