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

class normalizer :
    def run ( self , src ) :
        res = dict ( )
        if 'consts' in src :
            res [ 'consts' ] = dict ( )
            for module , consts in src [ 'consts' ] . items ( ) :
                res [ 'consts' ] [ module ] = dict ( )
                for k , v in sorted ( consts . items ( ) ) :
                    if type ( v ) in ( str , unicode ) :
                        assert ( v [ 0 ] , v [ - 1 ] ) == ( '[' , ']' )
                        env = deepcopy ( consts )
                        try :
                            v = eval ( v [ 1 : - 1 ] , env )
                        except Exception as e :
                            raise exception ( str ( e ) , src ,
                                [ 'consts' , module , k ] )
                    res [ 'consts' ] [ module ] [ k ] = v
        return res
