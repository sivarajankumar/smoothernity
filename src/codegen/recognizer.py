from antlr3 import ANTLRInputStream , CommonTokenStream , RecognitionException
from antlr3 . tree import CommonTreeNodeStream
from antlr3 . constants import EOF
from autogenerated . ShyRecognizerBackend import ShyRecognizerBackend
from autogenerated . ShyRecognizerFrontend import ShyRecognizerFrontend
from autogenerated . ShyRecognizerFrontend import ShyRecognizerFrontendException
from autogenerated . ShyLexer import ShyLexer , ShyLexerException

class exception ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )

class recognizer :
    def run ( self , input ) :
        sl = ShyLexer ( ANTLRInputStream ( input ) )
        ts = CommonTokenStream ( sl )
        srf = ShyRecognizerFrontend ( ts )
        try :
            t = srf . start ( ) . tree
        except ShyLexerException as e :
            raise exception ( str ( e ) )
        except ShyRecognizerFrontendException as e :
            raise exception ( str ( e ) )
        last = ts . LT ( 1 )
        if last . getType ( ) != EOF :
            raise exception ( 'Unparsed token "%s" at line %s col %s' %
                ( last . getText ( )
                , last . getLine ( )
                , last . getCharPositionInLine ( ) ) )
        if t == None :
            return { }
        else :
            srb = ShyRecognizerBackend ( CommonTreeNodeStream ( t ) )
            return srb . start ( )