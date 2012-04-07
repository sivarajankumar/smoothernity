from utils import rewrite
from normalizer . exception import exception

def run ( src ) :
    try :
        return rewrite ( src , _rewriter )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

def _rewriter ( src , path ) :
    if type ( src ) is dict and 'assign' in src :
        res = list ( )
        froms = src [ 'assign' ] [ 'from' ]
        tos = src [ 'assign' ] [ 'to' ]
        lf , lt = len ( froms ) , len ( tos )
        if lt % lf > 0 :
            raise exception ( 'Need %i more assign targets' %
                ( lf - ( lt % lf ) ) , None , path )
        for i in xrange ( lt ) :
            res . append ( { 'assign' :
                { 'from' : [ froms [ i % lf ] ]
                , 'to' : [ tos [ i ] ] } } )
        return res if len ( res ) > 1 else res [ 0 ]
    return src
