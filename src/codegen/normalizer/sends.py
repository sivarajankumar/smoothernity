from explorer import explorer
from normalizer . split_args import split_args

def run ( src ) :
    e = explorer ( src )
    return split_args ( 'send'
        , lambda n , p : e . get_messages_receives ( ) [ n ]
        , src )
