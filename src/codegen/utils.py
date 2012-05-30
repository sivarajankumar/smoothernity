def is_text ( s ) :
    return type ( s ) in ( str , unicode )

def is_string ( s ) :
    return is_text ( s ) and ( s [ : 1 ] , s [ - 1 : ] ) == ( "'" , "'" ) 

class merge_exception ( Exception ) :
    def __init__ ( self , txt , keys ) :
        Exception . __init__ ( self , txt )
        self . _keys = keys
    def get_keys ( self ) :
        return self . _keys

def merge ( dst , src , overwrite = True ) :
    types = ( type ( dst ) , type ( src ) )
    if types == ( dict , dict ) :
        overlap = set ( src . keys ( ) ) . intersection ( dst . keys ( ) )
        if overlap and not overwrite :
            raise merge_exception ( 'Keys overwrite' ,
                list ( sorted ( overlap ) ) )
        return dict ( dst . items ( ) + [
            ( k , merge ( dst [ k ] , v ) if k in dst else v )
            for k , v in src . items ( ) ] )
    elif types == ( list , list ) :
        return dst + src
    else :
        return src

def rewrite ( src , rewriter , path = [ ] ) :
    res = rewriter ( src , path )
    if type ( res ) is dict :
        return dict ( [
            ( k , rewrite ( v , rewriter , path + [ k ] ) )
            for k , v in res . items ( ) ] )
    elif type ( res ) is list :
        return reduce (
            lambda x , y : x + y if type ( y ) is list else x + [ y ] ,
            [ rewrite ( res [ i ] , rewriter , path + [ i ] )
                for i in xrange ( len ( res ) )
            ] , [ ] )
    else :
        return res
