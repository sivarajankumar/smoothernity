from utils import rewrite
from normalizer import exception

def run ( what , where , src ) :
    try :
        return rewrite ( src ,
            lambda s , p : _rewriter ( what , where , s , p ) )
    except exception as e :
        raise exception ( str ( e ) , src , e . get_path ( ) )

class _rewriter_exception ( Exception ) :
    pass

def _rewriter ( what , where , src , path ) :
    try :
        if type ( src ) is dict and what in src :
            res = list ( )
            name , args = src [ what ] [ 0 ] , src [ what ] [ 1 : ]
            try :
                need_args = where ( name , path )
            except KeyError as e :
                raise _rewriter_exception ( "Unknown %sable '%s'"
                    % ( what , name ) )
            la , lna = len ( args ) , len ( need_args )
            if la != lna and ( not la * lna or la % lna ) :
                raise _rewriter_exception ( "'%s' takes n*%i args, "
                    "but has been given %i" % ( name , lna , la ) )
            while True :
                res . append ( { what : [ name ] + args [ : lna ] } )
                args = args [ lna : ]
                if not args :
                    break
            return res if len ( res ) > 1 else res [ 0 ]
        return src
    except _rewriter_exception as e :
        raise exception ( str ( e ) , None , path )

