from normalizer . assigns import run as run_split_assigns
from normalizer . calls import run as run_split_calls
from normalizer . consts import run as run_consts
from normalizer . names import run as run_names
from normalizer . sends import run as run_split_sends
from normalizer . skeleton import run as run_skeleton
from normalizer . withs import run as run_withs

def run ( src ) :
    return reduce ( lambda x , y : lambda a : y ( x ( a ) ) ,
        [ run_skeleton
        , run_consts
        , run_names
        , run_withs
        , run_split_sends
        , run_split_calls
        , run_split_assigns
        #, run_check_sends
        #, run_check_calls
        #, run_check_assigns
        ] , lambda a : a ) ( src )
