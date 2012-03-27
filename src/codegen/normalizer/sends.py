from utils import rewrite
from explorer import explorer

def split_args ( what , where , src , path ) :
    if type ( src ) is dict and what in src :
        res = list ( )
        name , args = src [ what ] [ 0 ] , src [ what ] [ 1 : ]
        need_args = where [ name ]
        la , lna = len ( args ) , len ( need_args )
        while True :
            res . append ( { what : [ name ] + args [ : lna ] } )
            args = args [ lna : ]
            if not args :
                break
        return res if len ( res ) > 1 else res [ 0 ]
    return src

def run ( src ) :
    e = explorer ( src ) . get_messages_receives ( )
    return rewrite ( src , lambda s , p : split_args ( 'send' , e , s , p ) )
