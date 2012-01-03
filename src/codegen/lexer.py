import re

class lexer_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self , 'Lexical error: "%s"' % line )

class lexer :
    def __init__ ( self ) :
        self . _token_patterns = [ ]
    def set_token_patterns ( self , pats ) :
        self . _token_patterns = pats
    def parse ( self , lines ) :
        res = [ ]
        for line in lines :
            line = line . strip ( ' ' )
            while line :
                was_match = False
                for pats in self . _token_patterns :
                    for token , matches in pats . items ( ) :
                        for match in matches :
                            rem = re . match ( match , line )
                            if rem :
                                value = line [ rem . start ( )
                                             : rem . end ( ) ]
                                line = line [ rem . end ( ) : ]
                                if line and line [ 0 ] != ' ' :
                                    raise lexer_exception ( line )
                                line = line . strip ( ' ' )
                                res . append ( { 'type' : token
                                               , 'value' : value } )
                                was_match = True
                if not was_match :
                    raise lexer_exception ( line )
        return res
