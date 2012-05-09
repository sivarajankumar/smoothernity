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
            if not is_text ( x ) or not reduce ( or_ ,
                [ y [ 0 ] in expl . get_writables ( path )
                    for y in expl . split_value_fields ( path , x ) + [ [ x ] ]
                ] , False ) :
                raise exception ( "Assign to unknown writable '%s'" % x
                                , None , path )
        for x in src [ 'assign' ] [ 'from' ] :
            if is_text ( x ) and not reduce ( or_ ,
                [ y [ 0 ] in expl . get_readables ( path )
                    for y in expl . split_value_fields ( path , x ) + [ [ x ] ]
                ] , False ) :
                raise exception ( "Assign from unknown readable '%s'" % x
                                , None , path )
    return src
