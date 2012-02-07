from utils import merge

skeleton = \
    { 'consts' : { }
    , 'messages' : { }
    , 'module' : { }
    , 'stateless' : { }
    , 'trace' : { }
    , 'types' : { }
    , 'vars' : { }
    }

def merge_skeleton ( x ) :
    return merge ( skeleton , x )
