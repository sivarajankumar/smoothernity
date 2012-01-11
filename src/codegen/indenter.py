class indenter :
    def __init__ ( self ) :
        self . _res = None
        self . _indent_token = None
        self . _dedent_token = None
    def set_indent_token ( self , token ) :
        self . _indent_token = token
    def set_dedent_token ( self , token ) :
        self . _dedent_token = token
    def run ( self , lines ) :
        self . _res = ''
        indents = [ 0 ]
        for line in lines :
            line = line . rstrip ( )
            indent = len ( line ) - len ( line . lstrip ( ) )
            line = line . lstrip ( )
            if line :
                while indent < indents [ - 1 ] :
                    self . _append ( self . _dedent_token )
                    indents . pop ( )
                while indent > indents [ - 1 ] :
                    self . _append ( self . _indent_token )
                    indents . append ( indent )
                self . _append ( line )
        while len ( indents ) > 1 :
            self . _append ( self . _dedent_token )
            indents . pop ( )
        return self . _res
    def _append ( self , s ) :
        if self . _res :
            self . _res += ' '
        self . _res += s
