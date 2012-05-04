from explorer import explorer
from normalizer . args_split import run as run_args_split

def run ( src ) :
    e = explorer ( src )
    return run_args_split ( 'call'
        , lambda n , p : e . get_callables ( p ) [ n ] [ 'args' ]
        , src )
