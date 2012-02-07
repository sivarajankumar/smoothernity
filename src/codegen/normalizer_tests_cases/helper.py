from utils import merge

def merge_skeleton_root ( x ) :
    return merge (
        { 'consts' : { }
        , 'messages' : { }
        , 'module' : { }
        , 'stateless' : { }
        , 'trace' : { }
        , 'types' : { }
        , 'vars' : { }
        } , x )

def merge_skeleton_module ( x ) :
    return merge (
        { 'module_queue' : ''
        , 'proc' : { }
        , 'receive' : { }
        , 'request' : { }
        } , x )
