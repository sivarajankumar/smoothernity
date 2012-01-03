class line_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self , 'Line number %s is out of range' % line )

class show :
    def __init__ ( self ) :
        self . _context = None
        self . _source = None
    def set_context ( self , context ) :
        self . _context = context
    def set_source ( self , source ) :
        self . _source = source
    def context_line ( self , line ) :
        if line < 0 or line >= len ( self . _source ) :
            raise line_exception ( line )
        marked = self . _source [ : line + 1 ]
        marked += [ '^' * len ( str ( self . _source [ line ] ) ) ]
        marked += self . _source [ line + 1 : ]
        start = max ( 0 , line - self . _context + 1 )
        end = start + self . _context + 1
        return [ str ( s ) for s in marked [ start : end ] ]
