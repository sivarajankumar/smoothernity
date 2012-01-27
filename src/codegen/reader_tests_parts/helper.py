import io
import reader

class helper :
    def __init__ ( self ) :
        self . _r = reader . reader ( )
    def rec ( self , s ) :
        return self . _r . run ( io . StringIO ( s ) ) 
