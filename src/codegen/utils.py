from copy import deepcopy

def is_text ( s ) :
    return type ( s ) in ( str , unicode )

class merge_exception ( Exception ) :
    def __init__ ( self , txt , keys ) :
        Exception . __init__ ( self , txt )
        self . _keys = keys
    def get_keys ( self ) :
        return self . _keys

def merge ( dst_ , src_ , overwrite = True ) :
    dst = deepcopy ( dst_ )
    src = deepcopy ( src_ )
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
            [ rewrite ( res [ iv ] , rewriter , path + [ iv ] )
                for iv in xrange ( len ( res ) )
            ] , [ ] )
    else :
        return res
