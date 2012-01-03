import re

class lexer :
    def __init__ ( self ) :
        self . _token_patterns = [ ]
    def set_token_patterns ( self , pats ) :
        self . _token_patterns = pats
    def parse ( self , lines ) :
        res = [ ]
        for line in lines :
            while line :
                for pats in self . _token_patterns :
                    for token , match in pats . items ( ) :
                        rem = re . match ( match , line )
                        if rem :
                            value = line [ rem . start ( ) : rem . end ( ) ]
                            line = line [ rem . end ( ) : ]
                            res . append ( { 'type' : token , 'value' : value } )
        return res
