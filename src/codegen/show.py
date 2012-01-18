class line_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self , 'Line number %s is out of range' % line )

class line_col_exception ( Exception ) :
    def __init__ ( self , line , col ) :
        Exception . __init__ ( self ,
            'Col number %s is out of range in line %s' % ( col , line ) )

class show :
    def __init__ ( self ) :
        self . _context = None
        self . _source = None
    def set_context ( self , context ) :
        self . _context = context
    def set_source ( self , source ) :
        self . _source = source
    def context_line ( self , line ) :
        return self . _context_line_col ( line , None )
    def context_line_col ( self , line , col ) :
        return self . _context_line_col ( line , col )
    def _context_line_col ( self , line , col ) :
        if line < 0 or line >= len ( self . _source ) :
            raise line_exception ( line )
        marked = self . _source [ : line + 1 ]
        if col == None :
            marked += [ '^' * len ( str ( self . _source [ line ] ) ) ]
        else :
            if col < 0 or col >= len ( str ( self . _source [ line ] ) ) :
                raise line_col_exception ( line , col )
            marked += [ str ( ' ' * col ) + '^' ]
        marked += self . _source [ line + 1 : ]
        start = max ( 0 , line - self . _context + 1 )
        end = start + self . _context + 1
        return [ str ( s ) for s in marked [ start : end ] ]
