from antlr3 import ANTLRInputStream , CommonTokenStream
from antlr3 . tree import CommonTreeNodeStream
from FrontendParser import FrontendParser
from FrontendLexer import FrontendLexer
from Backend import Backend

class recognizer :
    def recognize ( self , input ) :
        fel = FrontendLexer ( ANTLRInputStream ( input ) )
        fep = FrontendParser ( CommonTokenStream ( fel ) )
        be = Backend ( CommonTreeNodeStream ( fep . start ( ) ) )
        return be . start ( )
