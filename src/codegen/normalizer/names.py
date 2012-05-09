from utils import is_text , rewrite
from explorer import explorer
from itertools import combinations
from normalizer . exception import exception

def run ( src ) :
    where = explorer ( src ) . get_everything
    try :
        return rewrite ( src , lambda s , p : _rewriter ( where , s , p ) )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( where , src , path ) :
    if is_text ( src ) :
        prefixes = [ path [ i + 1 ]
            for i in xrange ( len ( path ) - 1 ) if path [ i ] == 'with' ]
        valids = filter ( lambda x : x in where ( path ) ,
            [ src ] + [ '_' . join ( c ) + '_' + src
                for i in xrange ( len ( prefixes ) )
                    for c in combinations ( prefixes , i + 1 ) ] )
        if len ( valids ) > 1 :
            raise exception ( "Ambiguous identifiers: '%s'" %
                ( ', ' . join ( valids ) ) , None , path )
        else :
            return ( valids + [ src ] ) [ 0 ]
    else :
        return src
