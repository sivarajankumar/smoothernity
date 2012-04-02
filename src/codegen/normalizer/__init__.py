from utils import merge , is_text
from itertools import combinations
from normalizer . exception import exception
from normalizer . assigns import run as run_assigns
from normalizer . calls import run as run_calls
from normalizer . consts import run as run_consts
from normalizer . sends import run as run_sends
from normalizer . skeleton import run as run_skeleton
from normalizer . withs import run as run_withs

class normalizer :
    def __init__ ( self ) :
        self . _src = None
        self . _path = None
    def run ( self , src ) :
        self . _src = src
        self . _src = run_skeleton ( self . _src )
        self . _src = run_consts ( self . _src )
        self . _src = run_sends ( self . _src )
        self . _src = run_calls ( self . _src )
        self . _src = run_assigns ( self . _src )
        self . _src = self . run_names ( self . _src )
        self . _src = run_withs ( self . _src )
        return self . _src
    def run_names ( self , src ) :
        self . _src = src
        self . _src = self . _walk ( self . _src , self . _norm_names )
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
        m = merge ( self . _src , { 'platform_procs' : { } } )
        if name in m [ 'platform_procs' ] :
            res . append ( m [ 'platform_procs' ] [ name ] )
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
        return merge ( self . _src [ 'platform_consts' ] , all )
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
    def _norm_names ( self , src ) :
        if is_text ( src ) :
            return self . _use_withs ( src , self . _get_anything )
        else :
            return src
