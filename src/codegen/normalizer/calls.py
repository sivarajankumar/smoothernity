from explorer import explorer
from normalizer . split_args import split_args

def run ( src ) :
    e = explorer ( src )
    return split_args ( 'call'
        , lambda n , p : e . get_callables ( p ) [ n ] [ 'args' ]
        , src )
