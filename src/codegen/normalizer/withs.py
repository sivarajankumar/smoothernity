from utils import rewrite

def _rewriter ( src , path ) :
    if isinstance ( src , dict ) :
        if 'with' in src :
            res = list ( )
            for k , v in src [ 'with' ] . items ( ) :
                res += v
            return res
    return src

def run ( src ) :
    return rewrite ( src , _rewriter )
