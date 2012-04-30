from explorer import explorer
from utils import rewrite
from normalizer . exception import exception

def run ( src ) :
    x = explorer ( src )
    try :
        return rewrite ( src , lambda s , p : _rewriter ( s , p , x ) )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( src , path , expl ) :
    if type ( src ) is dict and 'assign' in src :
        froms = src [ 'assign' ] [ 'from' ]
        tos = src [ 'assign' ] [ 'to' ]
        for x in tos :
            if x in expl . get_consts ( path ) :
                raise exception ( "Assign to constant '%s'" % x
                                , None , path )
    return src
