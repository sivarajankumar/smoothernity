from explorer import explorer
from normalizer . split_args import run as run_split_args

def run ( src ) :
    e = explorer ( src )
    return run_split_args ( 'call'
        , lambda n , p : e . get_callables ( p ) [ n ] [ 'args' ]
        , src )
