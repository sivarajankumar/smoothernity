from utils import rewrite
from normalizer . exception import exception

def run ( src ) :
    try :
        return rewrite ( src , _rewriter )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( src , path ) :
    if type ( src ) is dict and 'assign' in src :
        froms = src [ 'assign' ] [ 'from' ]
        tos = src [ 'assign' ] [ 'to' ]
    return src
