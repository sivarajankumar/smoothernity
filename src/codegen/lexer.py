import re

class token_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self , 'Unknown token: "%s"' % line )

class whitespace_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self ,
            'Missing whitespace before next token: "%s"' % line )

class indent_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self ,
            'Dedent exceeds first indent: "%s"' % line )

class lexer :
    def __init__ ( self ) :
        self . _token_patterns = [ ]
        self . _indent_token = None
        self . _dedent_token = None
        self . _indents = [ ]
        self . _tokens = [ ]
    def set_token_patterns ( self , pats ) :
        self . _token_patterns = pats
    def set_indent_tokens ( self , indent , dedent ) :
        self . _indent_token = indent
        self . _dedent_token = dedent
    def parse ( self , lines ) :
        self . _tokens = [ ]
        self . _indents = [ ]
        for line in lines :
            spaces , line = self . _resplit ( r' *' , line )
            indent = len ( spaces )
            while self . _indents :
                if self . _indents [ - 1 ] < indent :
                    self . _tokens . append (
                        { 'type' : self . _indent_token } )
                    self . _indents . append ( indent )
                elif self . _indents [ - 1 ] > indent :
                    if len ( self . _indents ) == 1 :
                        raise indent_exception ( line )
                    self . _tokens . append (
                        { 'type' : self . _dedent_token } )
                    self . _indents . pop ( )
                else :
                    break
            else :
                self . _indents . append ( indent )
            while line :
                was_match = False
                for pats in self . _token_patterns :
                    for token , matches in pats . items ( ) :
                        for match in matches :
                            value , line = self . _resplit ( match , line )
                            if value :
                                if line and line [ 0 ] != ' ' :
                                    raise whitespace_exception ( line )
                                line = line . strip ( ' ' )
                                self . _tokens . append (
                                    { 'type' : token , 'value' : value } )
                                was_match = True
                if not was_match :
                    raise token_exception ( line )
        return self . _tokens
    def _resplit ( self , match , line ) :
        rem = re . match ( match , line )
        if rem :
            value = line [ rem . start ( ) : rem . end ( ) ]
            return value , line [ rem . end ( ) : ]
        return '' , line
