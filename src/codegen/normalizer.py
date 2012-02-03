class exception ( Exception ) :
    def __init__ ( self , s , p ) :
        Exception . __init__ ( self , s + str ( p ) )
        self . path = p

class normalizer :
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
                        try :
                            exec ( '_expr = ' + v [ 1 : - 1 ] ) in env
                        except Exception as e :
                            raise exception ( str ( e ) ,
                                [ 'consts' , module , k ] )
                        v = env [ '_expr' ]
                    res [ 'consts' ] [ module ] [ k ] = v
        return res
