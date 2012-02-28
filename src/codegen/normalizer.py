import operator
from utils import merge
from itertools import combinations

class exception ( Exception ) :
    def __init__ ( self , text , src , path ) :
        Exception . __init__ ( self , text )
        self . _path = path
        self . _src = src
    def get_path ( self ) :
        return self . _path
    def get_src ( self ) :
        return self . _src

def _is_text ( s ) :
    return type ( s ) in ( str , unicode )

class const_value :
    def __init__ ( self , v , env ) :
        self . _v , self . _env = v , env
    def value ( self ) :
        v = self . _v
        if _is_text ( v ) :
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
        self . _bind_consts = { }
        self . _src = None
        self . _path = None
    def bind_func ( self , func , args ) :
        self . _bind_funcs [ func ] = args
    def bind_const ( self , const , value ) :
        self . _bind_consts [ const ] = value
    def run ( self , src ) :
        self . _src = src
        self . _src = self . run_skeleton ( self . _src )
        self . _src = self . run_consts ( self . _src )
        self . _src = self . run_sends ( self . _src )
        self . _src = self . run_calls ( self . _src )
        self . _src = self . run_assigns ( self . _src )
        self . _src = self . run_names ( self . _src )
        self . _src = self . run_withs ( self . _src )
        return self . _src
    def run_skeleton ( self , src ) :
        self . _src = src
        self . _src = self . _norm_skeleton ( self . _src )
        return self . _src
    def run_consts ( self , src ) :
        self . _src = src
        self . _src = self . _norm_consts ( self . _src )
        return self . _src
    def run_sends ( self , src ) :
        self . _src = src
        self . _src = self . _walk ( self . _src , self . _norm_sends )
        return self . _src
    def run_calls ( self , src ) :
        self . _src = src
        self . _src = self . _walk ( self . _src , self . _norm_calls )
        return self . _src
    def run_assigns ( self , src ) :
        self . _src = src
        self . _src = self . _walk ( self . _src , self . _norm_assigns )
        return self . _src
    def run_names ( self , src ) :
        self . _src = src
        self . _src = self . _walk ( self . _src , self . _norm_names )
        return self . _src
    def run_withs ( self , src ) :
        self . _src = src
        self . _src = self . _walk ( self . _src , self . _norm_withs )
        return self . _src
    def _error ( self , text ) :
        raise exception ( text , self . _src , self . _path )
    def _local_proc ( self , name ) :
        what , which = self . _path [ 0 ] , self . _path [ 1 ]
        storage = self . _src [ what ] [ which ]
        if 'proc' in storage and name in storage [ 'proc' ] :
            return storage [ 'proc' ] [ name ]
    def _local_some_proc ( self , what , name ) :
        if name . startswith ( what + '_' ) :
            proc = name . split ( '%s_' % what ) [ 1 ]
            which = self . _path [ 1 ]
            if which in self . _src [ what ] :
                storage = self . _src [ what ] [ which ]
                if proc in storage [ 'proc' ] :
                    return storage [ 'proc' ] [ proc ]
    def _some_proc ( self , what , name ) :
        parts = name . split ( '_%s_' % what )
        if len ( parts ) > 1 :
            which , proc = parts [ : 2 ]
            if which in self . _src [ what ] :
                procs = self . _src [ what ] [ which ] [ 'proc' ]
                if proc in procs :
                    return procs [ proc ]
    def _stateless_proc ( self , name ) :
        return self . _some_proc ( 'stateless' , name )
    def _trace_proc ( self , name ) :
        return self . _some_proc ( 'trace' , name )
    def _local_stateless_proc ( self , name ) :
        return self . _local_some_proc ( 'stateless' , name )
    def _local_trace_proc ( self , name ) :
        return self . _local_some_proc ( 'trace' , name )
    def _get_callable ( self , name ) :
        res = [ ]
        if name in self . _bind_funcs :
            res . append ( self . _bind_funcs [ name ] )
        if self . _local_proc ( name ) :
            res . append ( self . _local_proc ( name ) [ 'args' ] )
        if self . _local_stateless_proc ( name ) :
            res . append ( self . _local_stateless_proc ( name ) [ 'args' ] )
        if self . _local_trace_proc ( name ) :
            res . append ( self . _local_trace_proc ( name ) [ 'args' ] )
        if self . _stateless_proc ( name ) :
            res . append ( self . _stateless_proc ( name ) [ 'args' ] )
        if self . _trace_proc ( name ) :
            res . append ( self . _trace_proc ( name ) [ 'args' ] )
        return res
    def _get_sendable ( self , name ) :
        all = { }
        for k , v in self . _src [ 'messages' ] . items ( ) :
            for kk , vv in v [ 'receive' ] . items ( ) :
                all [ k + '_' + kk ] = vv
        res = [ ]
        if name in all :
            res . append ( all [ name ] )
        return res
    def _get_anything ( self , name ) :
        res = [ ]
        res += self . _get_callable ( name )
        res += self . _get_sendable ( name )
        res += self . _get_valuable ( name )
        #TODO: move this check somewhere else
        if len ( res ) > 1 :
            self . _error ( "Ambiguous identifier '%s'" % name )
        return res
    def _get_valuable ( self , name ) :
        res = [ ]
        if name in self . _all_consts ( ) :
            res . append ( self . _all_consts ( ) [ name ] )
        what = self . _path [ 1 ]
        if what in self . _src [ 'vars' ] :
            vars = self . _src [ 'vars' ] [ what ]
            if name in reduce ( merge , vars , { } ) :
                res . append ( name )
        cur = self . _src
        for p in self . _path :
            if p in cur :
                cur = cur [ p ]
                for a in ( 'vars' , 'args' ) :
                    if a in cur :
                        if name in reduce ( merge , cur [ a ] , { } ) :
                            res . append ( name )
        return res
    def _all_consts ( self ) :
        all = { }
        for k , v in self . _src [ 'consts' ] . items ( ) :
            for kk , vv in v . items ( ) :
                all [ k + '_consts_' + kk ] = vv
                if self . _path [ 1 ] == k :
                    all [ 'consts_' + kk ] = vv
        return merge ( self . _bind_consts , all )
    def _get_value ( self , name ) :
        res = [ ]
        if name in self . _all_consts ( ) :
            res . append ( self . _all_consts ( ) [ name ] )
        what = self . _path [ 1 ]
        if what in self . _src [ 'vars' ] :
            vars = self . _src [ 'vars' ] [ what ]
            if name in reduce ( merge , vars , { } ) :
                res . append ( name )
        cur = self . _src
        for p in self . _path :
            if p in cur :
                cur = cur [ p ]
                for a in ( 'vars' , 'args' ) :
                    if a in cur :
                        if name in reduce ( merge , cur [ a ] , { } ) :
                            res . append ( name )
        if len ( res ) > 1 :
            self . _error ( "Ambiguous value '%s'" % name )
        elif res :
            return res [ 0 ]
    def _with_prefixes ( self ) :
        res = list ( )
        for i in xrange ( len ( self . _path ) - 1 ) :
            if self . _path [ i ] == 'with' :
                res . append ( self . _path [ i + 1 ] )
        return res
    def _candidates ( self , name , func , prefixes ) :
        return filter ( func ,
            [ name ] + [ '_' . join ( c ) + '_' + name
                for i in xrange ( len ( prefixes ) )
                    for c in combinations ( prefixes , i + 1 ) ] )
    def _use_withs ( self , name , func ) :
        prefixes = self . _with_prefixes ( )
        candidates = self . _candidates ( name , func , prefixes )
        if len ( candidates ) > 1 :
            self . _error ( "Ambiguous identifiers: '%s'" %
                ( ', ' . join ( candidates ) ) )
        elif candidates :
            return candidates [ 0 ]
        else :
            return name
    def _walk ( self , src , visit , path = [ ] ) :
        self . _path = path
        src = visit ( src )
        if isinstance ( src , dict ) :
            res = dict ( )
            for k , v in src . items ( ) :
                res [ k ] = self . _walk ( v , visit , path + [ k ] )
        elif isinstance ( src , list ) :
            res = list ( )
            for iv in xrange ( len ( src ) ) :
                v = src [ iv ]
                a = self . _walk ( v , visit , path + [ iv ] )
                if isinstance ( a , list ) :
                    res += a
                else :
                    res . append ( a )
        else :
            res = src
        return res
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
    def _norm_withs ( self , src ) :
        if isinstance ( src , dict ) :
            if 'with' in src :
                res = list ( )
                for k , v in src [ 'with' ] . items ( ) :
                    res += v
                return res
        return src
    def _norm_assigns ( self , src ) :
        if isinstance ( src , dict ) :
            if 'assign' in src :
                res = list ( )
                froms = src [ 'assign' ] [ 'from' ]
                tos = src [ 'assign' ] [ 'to' ]
                lf , lt = len ( froms ) , len ( tos )
                if lt % lf > 0 :
                    self . _error ( 'Need %i more assign targets' %
                        ( lf - ( lt % lf ) ) )
                for i in xrange ( lt ) :
                    res . append ( { 'assign' :
                        { 'from' : [ froms [ i % lf ] ]
                        , 'to' : [ tos [ i ] ] } } )
                return res if len ( res ) > 1 else res [ 0 ]
        return src
    def _norm_arguable ( self , src , what , how ) :
        if isinstance ( src , dict ) :
            if what in src :
                res = list ( )
                name = src [ what ] [ 0 ]
                args = src [ what ] [ 1 : ]
                if not how ( name ) :
                    self . _error ( "Unknown arguable '%s'" % name )
                assert len ( how ( name ) ) == 1 #TODO: raise here
                need_args = how ( name ) [ 0 ]
                la , lna = len ( args ) , len ( need_args )
                if la != lna and ( not la * lna or la % lna ) :
                    self . _error ( "'%s' takes n*%i args, "
                        "but has been given %i" % ( name , lna , la ) )
                while True :
                    res . append ( { what : [ name ] + args [ : lna ] } )
                    args = args [ lna : ]
                    if not args :
                        break
                return res if len ( res ) > 1 else res [ 0 ]
        return src
    def _norm_names ( self , src ) :
        if _is_text ( src ) :
            return self . _use_withs ( src , self . _get_anything )
        else :
            return src
    def _norm_calls ( self , src ) :
        return self . _norm_arguable ( src , 'call' , self . _get_callable )
    def _norm_sends ( self , src ) :
        return self . _norm_arguable ( src , 'send' , self . _get_sendable )
    def _old_norm_calls ( self , src ) :
        return self . _old_norm_arguable ( src , 'call' , self . _old_get_callable )
    def _old_norm_sends ( self , src ) :
        return self . _old_norm_arguable ( src , 'send' , self . _old_get_sendable )
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
