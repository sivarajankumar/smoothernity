from utils import is_text , rewrite
from explorer import explorer
from itertools import combinations
from normalizer . exception import exception

def run ( src ) :
    try :
        a = explorer ( src ) . get_everything
        return rewrite ( src ,
            lambda s , p : _use_withs ( s , p , a ( p ) ) if is_text ( s ) else s )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _use_withs ( name , path , names ) :
    prefixes = _with_prefixes ( path )
    candidates = _candidates ( name , names , prefixes )
    if len ( candidates ) > 1 :
        raise exception ( "Ambiguous identifiers: '%s'" %
            ( ', ' . join ( candidates ) ) , None , path )
    elif candidates :
        return candidates [ 0 ]
    else :
        return name

def _with_prefixes ( path ) :
    res = list ( )
    for i in xrange ( len ( path ) - 1 ) :
        if path [ i ] == 'with' :
            res . append ( path [ i + 1 ] )
    return res

def _candidates ( name , names , prefixes ) :
    return filter ( lambda x : x in names ,
        [ name ] + [ '_' . join ( c ) + '_' + name
            for i in xrange ( len ( prefixes ) )
                for c in combinations ( prefixes , i + 1 ) ] )
