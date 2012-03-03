from utils import merge

def merge_skeleton_root ( x ) :
    return merge (
        { 'consts' : { }
        , 'messages' : { }
        , 'module' : { }
        , 'platform_consts' : { }
        , 'platform_procs' : { }
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

def merge_skeleton_proc ( x ) :
    return merge (
        { 'vars' : [ ]
        , 'args' : [ ]
        , 'ops' : [ ]
        } , x )

def merge_skeleton_messages ( x ) :
    return merge (
        { 'receive' : { }
        , 'reply' : { }
        , 'request' : { }
        } , x )
