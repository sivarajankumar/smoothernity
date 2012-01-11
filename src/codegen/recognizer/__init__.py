from antlr3 import ANTLRInputStream , CommonTokenStream , RecognitionException
from antlr3 . tree import CommonTreeNodeStream
from FrontendParser import FrontendParser , FrontendParserException
from FrontendLexer import FrontendLexer , FrontendLexerException
from Backend import Backend
from indenter import indenter
from io import StringIO

class exception ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )

class lexer ( FrontendLexer ) :
    def __init__ ( self , * args , ** kw_args ) :
        FrontendLexer . __init__ ( self , * args , ** kw_args )
        self . _indents = [ 0 ]

class recognizer :
    def __init__ ( self ) :
        self . _indenter = indenter ( )
        self . _indenter . set_indent_token ( 'indent' )
        self . _indenter . set_dedent_token ( 'dedent' )
    def recognize ( self , input ) :
        indented = self . _indenter . run ( input . readlines ( ) )
        fel = lexer ( ANTLRInputStream ( StringIO ( indented ) ) )
        fep = FrontendParser ( CommonTokenStream ( fel ) )
        try :
            t = fep . start ( ) . tree
        except FrontendLexerException as e :
            raise exception ( str ( e ) )
        except FrontendParserException as e :
            raise exception ( str ( e ) )
        if t == None :
            return { }
        else :
            be = Backend ( CommonTreeNodeStream ( t ) )
            return be . start ( )
