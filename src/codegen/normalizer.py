import operator

class exception ( Exception ) :
    def __init__ ( self , text , src , path ) :
        Exception . __init__ ( self , text )
        self . _path = path
        self . _src = src
    def get_path ( self ) :
        return self . _path
    def get_src ( self ) :
        return self . _src

class const_value :
    def __init__ ( self , v , env ) :
        self . _v = v
        self . _env = env
    def value ( self ) :
        v = self . _v
        if type ( v ) in ( str , unicode ) :
            assert ( v [ 0 ] , v [ - 1 ] ) == ( '[' , ']' )
            return eval ( v [ 1 : - 1 ] , self . _env )
        else :
            return v
    def _calc ( self , a , b , op ) :
        if isinstance ( a , const_value ) :
            a = a . value ( )
        if isinstance ( b , const_value ) :
            b = b . value ( )
        return op ( a , b )
    def __add__ ( self , a ) :
        return self . _calc ( self , a , operator . add )
    def __radd__ ( self , a ) :
        return self . _calc ( a , self , operator . add )
    def __mul__ ( self , a ) :
        return self . _calc ( self , a , operator . mul )
    def __rmul__ ( self , a ) :
        return self . _calc ( self , a , operator . mul )

class normalizer :
    def run ( self , src ) :
        res = dict ( )
        if 'consts' in src :
            res [ 'consts' ] = dict ( )
            for module , consts in src [ 'consts' ] . items ( ) :
                env = dict ( )
                for k , v in consts . items ( ) :
                    env [ k ] = const_value ( v , env )
                res [ 'consts' ] [ module ] = dict ( )
                for k in sorted ( consts . keys ( ) ) :
                    try :
                        res [ 'consts' ] [ module ] [ k ] = \
                            env [ k ] . value ( )
                    except Exception as e :
                        raise exception ( str ( e ) , src ,
                            [ 'consts' , module , k ] )
        return res
