grammar Frontend ;

options 
{
    language = Python ;
    output = AST ;
    ASTLabelType = object ;
}

@ parser :: header
{
    class FrontendParserException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ lexer :: header
{
    class FrontendLexerException ( Exception ) :
        def __init__ ( self , text ) :
            Exception . __init__ ( self , text )
}

@ parser :: members
{
    def emitErrorMessage ( self , msg ) :
        raise FrontendParserException ( msg )
}

@ lexer :: members
{
    def emitErrorMessage ( self , msg ) :
        raise FrontendLexerException ( msg )
}

start : ( module | consts ) * ;
module : 'module' ID NEWLINE -> ^( 'module' ID ) ;
consts : 'consts' ID NEWLINE -> ^( 'consts' ID )
       | 'consts' ID NEWLINE consts_values -> ^( 'consts' ID consts_values )
       ;
consts_values : consts_value + ;
consts_value : ID NUMBER NEWLINE -> ^( ID NUMBER ) ;

ID : 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' ) * ;
NUMBER : ( '0' .. '9' ) + ;
WHITESPACE : SP { self . skip ( ) } ;
NEWLINE
    : NL SP ? 
        {
            la = self . input . LA ( 1 )
            if la == EOF :
                while len ( self . _indents ) > 1 :
                    print 'dedent'
                    self . _indents . pop ( )
            elif la not in ( ord ( '\r' ) , ord ( '\n' ) ) :
                indent = len ( $SP . text ) if $SP != None else 0
                while indent < self . _indents [ - 1 ] :
                    print 'dedent'
                    self . _indents . pop ( )
                while indent > self . _indents [ - 1 ] :
                    print 'indent'
                    self . _indents . append ( indent )
        }
    ;

fragment NL : '\r' ? '\n' ;
fragment SP : ' ' + ;
