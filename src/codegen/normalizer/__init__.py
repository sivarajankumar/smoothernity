from normalizer . assigns_check import run as run_assigns_check
from normalizer . assigns_split import run as run_assigns_split
from normalizer . calls_check import run as run_calls_check
from normalizer . calls_split import run as run_calls_split
from normalizer . consts import run as run_consts
from normalizer . names import run as run_names
from normalizer . sends_check import run as run_sends_check
from normalizer . sends_split import run as run_sends_split
from normalizer . skeleton import run as run_skeleton
from normalizer . withs import run as run_withs

def run ( src ) :
    return reduce ( lambda x , y : lambda a : y ( x ( a ) ) ,
        [ run_skeleton
        , run_consts
        , run_names
        , run_withs
        , run_assigns_split
        , run_assigns_check
        , run_calls_split
        , run_calls_check
        , run_sends_split
        , run_sends_check
        ] , lambda a : a ) ( src )
