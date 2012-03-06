import operator
from explorer import explorer
from normalizer . exception import exception
from utils import is_text

def run ( src ) :
    exp = explorer ( src )
    res = dict ( )
    for root_k , root_v in src . items ( ) :
        if root_k == 'consts' :
            res [ 'consts' ] = dict ( )
            env = dict ( )
            for module in src [ 'consts' ] . keys ( ) :
                for k , v in exp . get_consts (
                                    [ 'consts' , module ] ) . items ( ) :
                    env [ k ] = _const_value ( v , env )
            for module , consts in src [ 'consts' ] . items ( ) :
                res [ 'consts' ] [ module ] = dict ( )
                for k in sorted ( consts . keys ( ) ) :
                    try :
                        res [ 'consts' ] [ module ] [ k ] = \
                            env [ k ] . value ( )
                    except Exception as e :
                        raise exception ( str ( e ) , src ,
                                [ 'consts' , module , k ] )
        else :
            res [ root_k ] = root_v
    return res

class _const_value :
    def __init__ ( self , v , env ) :
        self . _v , self . _env = v , env
    def value ( self ) :
        v = self . _v
        if is_text ( v ) :
            assert ( v [ 0 ] , v [ - 1 ] ) == ( '[' , ']' )
            ev = eval ( v [ 1 : - 1 ] , self . _env )
            return ev . value ( ) if isinstance ( ev , _const_value ) else ev
        else :
            return v
    def _calc ( self , a , b , op ) :
        return op \
            ( a . value ( ) if isinstance ( a , _const_value ) else a
            , b . value ( ) if isinstance ( b , _const_value ) else b )
    def _ops ( op ) :
        def fwd ( self , a ) :
            return self . _calc ( self , a , op )
        def back ( self , a ) :
            return self . _calc ( a , self , op )
        return fwd , back
    __or__ , __ror__ = _ops ( operator . or_ )
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
