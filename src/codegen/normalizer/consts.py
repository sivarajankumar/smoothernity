import operator
from explorer import explorer
from fractions import Fraction
from normalizer . exception import exception
from utils import is_text , rewrite

def run ( src ) :
    r = lambda x : lambda y : rewrite ( y , lambda s , p : x ( s , p , y ) )
    return reduce ( lambda x , y : lambda a : y ( x ( a ) ) ,
        [ r ( _ready )
        , r ( _steady )
        , r ( _go )
        ] ) ( src )

def _is_expr ( x ) :
    return is_text ( x ) and ( x [ : 1 ] , x [ - 1 : ] ) == ( '[' , ']' )

def _ready ( src , path , top ) :
    if _is_expr ( src ) or type ( src ) in ( int , Fraction ) :
        return _const_value ( src , path )
    else :
        return src

def _steady ( src , path , top ) :
    if isinstance ( src , _const_value ) :
        src . set_top ( top )
    return src

def _go ( src , path , top ) :
    if isinstance ( src , _const_value ) :
        try :
            return src . value ( )
        except Exception as e :
            raise exception ( str ( e ) , top , path )
    else :
        return src

class _const_value :
    def __init__ ( self , v , path ) :
        self . _v , self . _path = v , path
    def set_top ( self , top ) :
        self . _top = top
    def value ( self ) :
        v = self . _v
        if is_text ( v ) :
            assert ( v [ 0 ] , v [ - 1 ] ) == ( '[' , ']' )
            env = explorer ( self . _top ) . get_consts ( self . _path )
            ev = eval ( v [ 1 : - 1 ] , env )
            return ev . value ( ) if isinstance ( ev , _const_value ) else ev
        else :
            return v
    def _calc ( self , a , b , op ) :
        return op \
            ( a . value ( ) if isinstance ( a , _const_value ) else a
            , b . value ( ) if isinstance ( b , _const_value ) else b )
    def _ops ( op ) :
        return lambda self , a : self . _calc ( self , a , op ) \
             , lambda self , a : self . _calc ( a , self , op )
    __or__  , __ror__  = _ops ( operator . or_ )
    __add__ , __radd__ = _ops ( operator . add )
    __sub__ , __rsub__ = _ops ( operator . sub )
    __mul__ , __rmul__ = _ops ( operator . mul )
    __div__ , __rdiv__ = _ops ( operator . div )
    __mod__ , __rmod__ = _ops ( operator . mod )
    __pow__ , __rpow__ = _ops ( operator . pow )
    __and__ , __rand__ = _ops ( operator . and_ )
    __xor__ , __rxor__ = _ops ( operator . xor )
    __lshift__ , __rlshift__ = _ops ( operator . lshift )
    __rshift__ , __rrshift__ = _ops ( operator . rshift )
