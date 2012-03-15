from copy import deepcopy

def is_text ( s ) :
    return type ( s ) in ( str , unicode )

class merge_exception ( Exception ) :
    def __init__ ( self , txt , key ) :
        Exception . __init__ ( self , txt )
        self . _key = key
    def get_key ( self ) :
        return self . _key

def merge ( dst_ , src_ , overwrite = True ) :
    dst = deepcopy ( dst_ )
    src = deepcopy ( src_ )
    types = ( type ( dst ) , type ( src ) )
    if types == ( dict , dict ) :
        for k , v in src . items ( ) :
            if not overwrite and k in dst :
                raise merge_exception ( 'Key overwrite' , k )
            dst [ k ] = merge ( dst [ k ] , v ) if k in dst else v
        return dst
    elif types == ( list , list ) :
        dst += src
        return dst
    else :
        return src

def rewrite ( src , rewriter , path = [ ] ) :
    return src
