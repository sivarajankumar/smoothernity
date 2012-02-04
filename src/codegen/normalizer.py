from copy import deepcopy

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
    def __add__ ( self , a ) :
        if isinstance ( a , const_value ) :
            return self . value ( ) + a . value ( )
        else :
            return self . value ( ) + a
    def __radd__ ( self , a ) :
        if isinstance ( a , const_value ) :
            return self . value ( ) + a . value ( )
        else :
            return self . value ( ) + a

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
