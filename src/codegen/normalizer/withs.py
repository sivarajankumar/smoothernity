from utils import rewrite

def run ( src ) :
    return rewrite ( src , lambda s , p : s [ 'with' ] . values ( ) \
        if type ( s ) is dict and 'with' in s else s )
