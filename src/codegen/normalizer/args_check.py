from utils import rewrite
from normalizer . exception import exception

def run ( what , where , src ) :
    try :
        return rewrite ( src ,
            lambda s , p : _rewriter ( what , where , s , p ) )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( what , where , src , path ) :
    if type ( src ) is dict and what in src :
        for arg in src [ what ] [ 1 : ] :
            if not where ( arg , path ) :
                raise exception ( "Unknown %sable argument '%s'"
                    % ( what , arg ) , None , path )
    return src
