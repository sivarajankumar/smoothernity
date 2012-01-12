from antlr3 import ANTLRInputStream , CommonTokenStream , RecognitionException
from antlr3 . tree import CommonTreeNodeStream
from antlr3 . constants import EOF
from FrontendParser import FrontendParser , FrontendParserException
from FrontendLexer import FrontendLexer , FrontendLexerException
from Backend import Backend
from indenter import indenter
from io import StringIO

class exception ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )

class recognizer :
    def __init__ ( self ) :
        self . _indenter = indenter ( )
        self . _indenter . set_indent_token ( 'indent' )
        self . _indenter . set_dedent_token ( 'dedent' )
        self . _indenter . set_newline_token ( '\n' )
    def recognize ( self , input ) :
        indented = self . _indenter . run ( input . readlines ( ) )
        fel = FrontendLexer ( ANTLRInputStream ( StringIO ( indented ) ) )
        ts = CommonTokenStream ( fel )
        fep = FrontendParser ( ts )
        try :
            t = fep . start ( ) . tree
        except FrontendLexerException as e :
            raise exception ( str ( e ) )
        except FrontendParserException as e :
            raise exception ( str ( e ) )
        if ts . LA ( 1 ) != EOF :
            raise exception ( 'unparsed tokens left' )
        if t == None :
            return { }
        else :
            be = Backend ( CommonTreeNodeStream ( t ) )
            return be . start ( )
