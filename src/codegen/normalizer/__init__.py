from normalizer . assigns import run as run_assigns
from normalizer . calls import run as run_calls
from normalizer . consts import run as run_consts
from normalizer . names import run as run_names
from normalizer . sends import run as run_sends
from normalizer . skeleton import run as run_skeleton
from normalizer . withs import run as run_withs

def run ( src ) :
    return reduce ( lambda x , y : lambda a : y ( x ( a ) ) ,
        [ run_skeleton
        , run_consts
        , run_sends
        , run_calls
        , run_assigns
        , run_names
        , run_withs
        ] , lambda a : a ) ( src )
