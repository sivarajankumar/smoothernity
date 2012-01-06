from antlr3 import ANTLRInputStream , CommonTokenStream , RecognitionException
from antlr3 . tree import CommonTreeNodeStream
from FrontendParser import FrontendParser
from FrontendLexer import FrontendLexer
from Backend import Backend

class exception ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )

class recognizer :
    def recognize ( self , input ) :
        fel = FrontendLexer ( ANTLRInputStream ( input ) )
        fep = FrontendParser ( CommonTokenStream ( fel ) )
        try :
            t = fep . start ( ) . tree
        except Exception as e :
            raise exception ( str ( e ) )
        if t == None :
            return { }
        else :
            be = Backend ( CommonTreeNodeStream ( t ) )
            return be . start ( )
