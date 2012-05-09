from explorer import explorer
from normalizer . args_split import run as run_args_split

def run ( src ) :
    e = explorer ( src )
    return run_args_split ( 'send'
        , lambda n , p : e . get_messages_receives ( ) [ n ]
        , src )
