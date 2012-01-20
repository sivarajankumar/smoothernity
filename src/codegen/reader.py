import io
import indenter
import recognizer
import formatter
import copypaster

class reader :
    def __init__ ( self ) :
        self . _c = copypaster . copypaster ( )
        self . _r = recognizer . recognizer ( )
        self . _i = indenter . indenter ( )
        self . _f = formatter . formatter ( )
        for o in ( self . _i , self . _f ) :
            o . set_indent_token ( 'indent' )
            o . set_dedent_token ( 'dedent' )
            o . set_newline_token ( '\n' )
    def run ( self , stream ) :
        d1 = self . _i . run ( stream . readlines ( ) )
        d2 = self . _c . run ( io . StringIO ( d1 ) )
        d3 = self . _f . run ( d2 )
        d4 = self . _i . run ( io . StringIO ( d3 ) . readlines ( ) )
        return self . _r . run ( io . StringIO ( d4 ) )
