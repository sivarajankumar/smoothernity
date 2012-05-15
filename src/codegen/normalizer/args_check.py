from utils import rewrite
from normalizer . exception import exception
from explorer import explorer

def run ( what , src ) :
    x = explorer ( src )
    try :
        return rewrite ( src ,
            lambda s , p : _rewriter ( s , p , what , x ) )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( src , path , what , expl ) :
    if type ( src ) is dict and what in src :
        for arg in src [ what ] [ 1 : ] :
            if not expl . is_passable ( path , arg ) :
                raise exception ( "Unknown %sable argument '%s'"
                    % ( what , arg ) , None , path )
    return src
