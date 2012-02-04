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
    def __init__ ( self , v ) :
        self . _v = v
    def value ( self , env ) :
        v = self . _v
        if type ( v ) in ( str , unicode ) :
            assert ( v [ 0 ] , v [ - 1 ] ) == ( '[' , ']' )
            return eval ( v [ 1 : - 1 ] , env )
        else :
            return v

class normalizer :
    def run ( self , src ) :
        res = dict ( )
        if 'consts' in src :
            res [ 'consts' ] = dict ( )
            for module , consts in src [ 'consts' ] . items ( ) :
                env = dict ( [ ( k , const_value ( v ) )
                    for k , v in consts . items ( ) ] )
                res [ 'consts' ] [ module ] = dict ( )
                for k in sorted ( consts . keys ( ) ) :
                    try :
                        res [ 'consts' ] [ module ] [ k ] = \
                            env [ k ] . value ( env )
                    except Exception as e :
                        raise exception ( str ( e ) , src ,
                            [ 'consts' , module , k ] )
        return res
