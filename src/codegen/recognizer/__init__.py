from antlr3 import ANTLRInputStream , CommonTokenStream
from antlr3 . tree import CommonTreeNodeStream
from FrontendParser import FrontendParser
from FrontendLexer import FrontendLexer
from Backend import Backend

class recognizer :
    def recognize ( self , input ) :
        fel = FrontendLexer ( ANTLRInputStream ( input ) )
        fep = FrontendParser ( CommonTokenStream ( fel ) )
        t = fep . start ( ) . tree
        if t == None :
            return { }
        else :
            be = Backend ( CommonTreeNodeStream ( t ) )
            return be . start ( )
