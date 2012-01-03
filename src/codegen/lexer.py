import re

class lexer_exception ( Exception ) :
    def __init__ ( self , line ) :
        Exception . __init__ ( self , 'Lexical error: "%s"' + line )

class lexer :
    def __init__ ( self ) :
        self . _token_patterns = [ ]
    def set_token_patterns ( self , pats ) :
        self . _token_patterns = pats
    def parse ( self , lines ) :
        res = [ ]
        for line in lines :
            while line :
                was_match = False
                for pats in self . _token_patterns :
                    for token , match in pats . items ( ) :
                        rem = re . match ( match , line )
                        if rem :
                            value = line [ rem . start ( ) : rem . end ( ) ]
                            line = line [ rem . end ( ) : ]
                            res . append ( { 'type' : token
                                           , 'value' : value } )
                            was_match = True
                if not was_match :
                    raise lexer_exception ( line )
        return res
