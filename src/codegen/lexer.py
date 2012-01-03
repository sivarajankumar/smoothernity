import re

class parse_token_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self , 'Unknown token: "%s"' % line )

class parse_whitespace_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self ,
            'Missing whitespace before next token: "%s"' % line )

class parse_indent_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self ,
            'Dedent exceeds first indent: "%s"' % line )

class generate_indent_exception ( Exception ) :
    def __init__ ( self , delta ) :
        Exception . __init__ ( self ,
            'Invalid indent delta: %s' % delta )

class generate_dedent_exception ( Exception ) :
    def __init__ ( self , delta ) :
        Exception . __init__ ( self ,
            'Invalid dedent delta: %s' % delta )

class lexer :
    def __init__ ( self ) :
        self . _token_patterns = [ ]
        self . _indent_token = None
        self . _dedent_token = None
        self . _eof_token = None
        self . _eol_token = None
        self . _indents = [ ]
        self . _tokens = [ ]
    def set_token_patterns ( self , pats ) :
        self . _token_patterns = pats
    def set_indent_tokens ( self , indent , dedent ) :
        self . _indent_token = indent
        self . _dedent_token = dedent
    def set_eol_token ( self , eol ) :
        self . _eol_token = eol
    def set_eof_token ( self , eof ) :
        self . _eof_token = eof
    def generate ( self , tokens ) :
        lines = [ ]
        line = indent = ''
        has_token = False
        for token in tokens :
            if token [ 'type' ] == 'eol' :
                lines . append ( indent + line )
                line = ''
                has_token = False
            elif token [ 'type' ] == 'eof' :
                break
            elif token [ 'type' ] == 'indent' :
                if token [ 'delta' ] <= 0 :
                    raise generate_indent_exception ( token [ 'delta' ] )
                indent += ' ' * token [ 'delta' ]
            elif token [ 'type' ] == 'dedent' :
                if - token [ 'delta' ] > len ( indent ) :
                    raise generate_dedent_exception ( token [ 'delta' ] )
                indent = indent [ - token [ 'delta' ] : ]
            else :
                if has_token :
                    line += ' '
                line += token [ 'value' ]
                has_token = True
        return lines
    def parse ( self , lines ) :
        self . _tokens = [ ]
        self . _indents = [ ]
        for line in lines :
            if self . _meaning_line ( line ) :
                line = self . _parse_tokens ( self . _parse_indent ( line ) )
                self . _append_eol ( )
                assert not line
        self . _append_dedents ( )
        self . _append_eof ( )
        return self . _tokens
    def _meaning_line ( self , line ) :
        return len ( line . strip ( ' ' ) ) > 0
    def _append_eol ( self ) :
        self . _tokens . append ( { 'type' : self . _eol_token } )
    def _append_eof ( self ) :
        self . _tokens . append ( { 'type' : self . _eof_token } )
    def _append_dedents ( self ) :
        while len ( self . _indents ) > 1 :
            delta = self . _indents [ - 2 ] - self . _indents [ - 1 ]
            self . _indents . pop ( )
            self . _tokens . append ( 
                { 'type' : self . _dedent_token , 'delta' : delta } )
    def _parse_indent ( self , line ) :
        spaces , line = self . _resplit ( r' *' , line )
        indent = len ( spaces )
        while self . _indents :
            if self . _indents [ - 1 ] < indent :
                delta = indent - self . _indents [ - 1 ]
                self . _tokens . append (
                    { 'type' : self . _indent_token , 'delta' : delta } )
                self . _indents . append ( indent )
            elif self . _indents [ - 1 ] > indent :
                if len ( self . _indents ) == 1 :
                    raise parse_indent_exception ( line )
                delta = self . _indents [ - 2 ] - self . _indents [ - 1 ]
                self . _tokens . append (
                    { 'type' : self . _dedent_token , 'delta' : delta } )
                self . _indents . pop ( )
            else :
                break
        else :
            self . _indents . append ( indent )
        return line
    def _parse_tokens ( self , line ) :
        while line :
            was_match = False
            for token , match in self . _token_patterns :
                while True :
                    value , line = self . _resplit ( match , line )
                    if value :
                        if line and line [ 0 ] != ' ' :
                            raise parse_whitespace_exception ( line )
                        line = line . strip ( ' ' )
                        self . _tokens . append (
                            { 'type' : token , 'value' : value } )
                        was_match = True
                    else :
                        break
            if not was_match :
                raise parse_token_exception ( line )
        return line
    def _resplit ( self , match , line ) :
        rem = re . match ( match , line )
        if rem :
            value = line [ rem . start ( ) : rem . end ( ) ]
            return value , line [ rem . end ( ) : ]
        return '' , line
