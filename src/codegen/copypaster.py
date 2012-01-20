from antlr3 import ANTLRInputStream , CommonTokenStream , RecognitionException
from antlr3 . tree import CommonTreeNodeStream
from antlr3 . constants import EOF
from autogenerated . ShyCopypasterBackend import ShyCopypasterBackend
from autogenerated . ShyCopypasterFrontend import ShyCopypasterFrontend
from autogenerated . ShyCopypasterFrontend import ShyCopypasterFrontendException
from autogenerated . ShyLexer import ShyLexer , ShyLexerException

class exception ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )

class copypaster :
    def run ( self , input ) :
        return self . _process ( self . _read ( input ) )
    def _process ( self , tokens ) :
        res = [ ]
        for t in tokens :
            if isinstance ( t , unicode ) :
                res . append ( t )
            elif isinstance ( t , dict ) :
                res += self . _copypaste ( t )
        return res
    def _copypaste ( self , info ) :
        res = [ ]
        for replace in info [ 'paste' ] :
            for t in self . _process ( info [ 'copy' ] ) :
                if t in replace :
                    res += replace [ t ]
                else :
                    for what , with_what in replace . items ( ) :
                        t = t . replace ( what , ' ' . join ( with_what ) )
                    res . append ( t )
        return res
    def _read ( self , input ) :
        sl = ShyLexer ( ANTLRInputStream ( input ) )
        ts = CommonTokenStream ( sl )
        scf = ShyCopypasterFrontend ( ts )
        try :
            t = scf . start ( ) . tree
        except ShyLexerException as e :
            raise exception ( str ( e ) )
        except ShyCopypasterFrontendException as e :
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
            scb = ShyCopypasterBackend ( CommonTreeNodeStream ( t ) )
            return scb . start ( )
