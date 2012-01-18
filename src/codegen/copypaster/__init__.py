from antlr3 import ANTLRInputStream , CommonTokenStream , RecognitionException
from antlr3 . tree import CommonTreeNodeStream
from antlr3 . constants import EOF
from FrontendParser import FrontendParser
from FrontendLexer import FrontendLexer
from Backend import Backend

class copypaster :
    def run ( self , input ) :
        fel = FrontendLexer ( ANTLRInputStream ( input ) )
        ts = CommonTokenStream ( fel )
        fep = FrontendParser ( ts )
        t = fep . start ( ) . tree
        if t == None :
            return { }
        else :
            be = Backend ( CommonTreeNodeStream ( t ) )
            return be . start ( )
