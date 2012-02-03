class normalizer :
    def __init__ ( self ) :
        pass
    def run ( self , src ) :
        res = dict ( )
        if 'consts' in src :
            res [ 'consts' ] = dict ( )
            for module , consts in src [ 'consts' ] . items ( ) :
                res [ 'consts' ] [ module ] = dict ( )
                for k , v in consts . items ( ) :
                    if type ( v ) is str :
                        assert ( v [ 0 ] , v [ - 1 ] ) == ( '[' , ']' )
                        env = { }
                        exec ( '_expr = ' + v [ 1 : - 1 ] ) in env
                        v = env [ '_expr' ]
                    res [ 'consts' ] [ module ] [ k ] = v
        return res
