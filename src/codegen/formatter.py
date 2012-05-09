class formatter :
    def __init__ ( self ) :
        self . _indent_token = None
        self . _dedent_token = None
        self . _newline_token = None
    def set_indent_token ( self , token ) :
        self . _indent_token = token
    def set_dedent_token ( self , token ) :
        self . _dedent_token = token
    def set_newline_token ( self , token ) :
        self . _newline_token = token
    def run ( self , tokens ) :
        res = str ( )
        line = str ( )
        indent = 0
        for t in tokens :
            if t == self . _newline_token :
                if line :
                    line += self . _newline_token
                    res += ' ' * indent + line
                line = str ( )
            elif t == self . _indent_token :
                indent += 1
            elif t == self . _dedent_token :
                indent -= 1
            else :
                if line :
                    line += ' '
                line += t
        if line :
            res += ' ' * indent + line
        return res
