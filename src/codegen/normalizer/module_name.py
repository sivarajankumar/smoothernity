from utils import rewrite

def run ( src ) :
    return rewrite ( src ,
        lambda s , p : ( "'%s'" % p [ 1 ] ) if s == 'module_name' else s )
