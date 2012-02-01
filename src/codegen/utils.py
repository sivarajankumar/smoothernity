def merge ( dst , src ) :
    types = ( type ( dst ) , type ( src ) )
    if types == ( dict , dict ) :
        for k , v in src . items ( ) :
            dst [ k ] = merge ( dst [ k ] , v ) if k in dst else v
        return dst
    elif types == ( list , list ) :
        dst += src
        return dst
    else :
        return src
