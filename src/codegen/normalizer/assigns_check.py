from explorer import explorer
from utils import rewrite , is_text
from normalizer . exception import exception
from operator import or_

def run ( src ) :
    x = explorer ( src )
    try :
        return rewrite ( src , lambda s , p : _rewriter ( s , p , x ) )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( src , path , expl ) :
    if type ( src ) is dict and 'assign' in src :
        for x in src [ 'assign' ] [ 'to' ] :
            if not expl . is_writable ( path , x ) :
                raise exception ( "Assign to unknown writable '%s'" % x
                                , None , path )
        for x in src [ 'assign' ] [ 'from' ] :
            if not expl . is_readable ( path , x ) :
                raise exception ( "Assign from unknown readable '%s'" % x
                                , None , path )
    return src
