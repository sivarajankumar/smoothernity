from utils import is_text , rewrite
from explorer import explorer
from itertools import combinations
from normalizer . exception import exception

def run ( src ) :
    x = explorer ( src )
    try :
        return rewrite ( src , lambda s , p : _rewriter ( s , p , x ) )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( src , path , expl ) :
    if is_text ( src ) :
        prefixes = [ path [ i + 1 ]
            for i in xrange ( len ( path ) - 1 ) if path [ i ] == 'with' ]
        valids = filter ( lambda x :
                            x in expl . get_everything ( path )
                            or expl . split_value_fields ( path , x ) ,
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
