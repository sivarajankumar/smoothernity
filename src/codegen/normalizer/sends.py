from explorer import explorer
from normalizer . split_args import split_args

def run ( src ) :
    e = explorer ( src ) . get_messages_receives ( )
    return split_args ( 'send' , e , src )
