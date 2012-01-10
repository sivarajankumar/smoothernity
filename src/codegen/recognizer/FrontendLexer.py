# $ANTLR 3.4 grammar/Frontend.g 2012-01-10 21:15:13

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

        
class FrontendLexerException ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__10=10
T__11=11
ID=4
NEWLINE=5
NL=6
NUMBER=7
SP=8
WHITESPACE=9


class FrontendLexer(Lexer):

    grammarFileName = "grammar/Frontend.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(FrontendLexer, self).__init__(input, state)

        self.delegates = []




             
    def emitErrorMessage ( self , msg ) :
        raise FrontendLexerException ( msg )



    # $ANTLR start "T__10"
    def mT__10(self, ):
        try:
            _type = T__10
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:17:7: ( 'consts' )
            # grammar/Frontend.g:17:9: 'consts'
            pass 
            self.match("consts")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__10"



    # $ANTLR start "T__11"
    def mT__11(self, ):
        try:
            _type = T__11
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:18:7: ( 'module' )
            # grammar/Frontend.g:18:9: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__11"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:44:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/Frontend.g:44:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/Frontend.g:44:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # grammar/Frontend.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):
        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:45:8: ( ( '0' .. '9' )+ )
            # grammar/Frontend.g:45:10: ( '0' .. '9' )+
            pass 
            # grammar/Frontend.g:45:10: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # grammar/Frontend.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):
        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:46:12: ( SP )
            # grammar/Frontend.g:46:14: SP
            pass 
            self.mSP()


            #action start
            self . skip ( ) 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            SP1 = None

            # grammar/Frontend.g:48:5: ( NL ( SP )? )
            # grammar/Frontend.g:48:7: NL ( SP )?
            pass 
            self.mNL()


            # grammar/Frontend.g:48:10: ( SP )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 32) :
                alt3 = 1
            if alt3 == 1:
                # grammar/Frontend.g:48:10: SP
                pass 
                SP1Start123 = self.getCharIndex()
                self.mSP()
                SP1StartLine123 = self.getLine()
                SP1StartCharPos123 = self.getCharPositionInLine()
                SP1 = CommonToken(
                    input=self.input,
                    type=INVALID_TOKEN_TYPE,
                    channel=DEFAULT_CHANNEL,
                    start=SP1Start123,
                    stop=self.getCharIndex()-1)
                SP1.setLine(SP1StartLine123)
                SP1.setCharPositionInLine(SP1StartCharPos123)





            #action start
                    
            la = self . input . LA ( 1 )
            if la == EOF :
                while len ( self . _indents ) > 1 :
                    print 'dedent'
                    self . _indents . pop ( )
            elif la not in ( ord ( '\r' ) , ord ( '\n' ) ) :
                indent = len ( SP1 . text ) if SP1 != None else 0
                while indent < self . _indents [ - 1 ] :
                    print 'dedent'
                    self . _indents . pop ( )
                while indent > self . _indents [ - 1 ] :
                    print 'indent'
                    self . _indents . append ( indent )
                    
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "NL"
    def mNL(self, ):
        try:
            # grammar/Frontend.g:66:13: ( ( '\\r' )? '\\n' )
            # grammar/Frontend.g:66:15: ( '\\r' )? '\\n'
            pass 
            # grammar/Frontend.g:66:15: ( '\\r' )?
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if (LA4_0 == 13) :
                alt4 = 1
            if alt4 == 1:
                # grammar/Frontend.g:66:15: '\\r'
                pass 
                self.match(13)




            self.match(10)




        finally:
            pass

    # $ANTLR end "NL"



    # $ANTLR start "SP"
    def mSP(self, ):
        try:
            # grammar/Frontend.g:67:13: ( ( ' ' )+ )
            # grammar/Frontend.g:67:15: ( ' ' )+
            pass 
            # grammar/Frontend.g:67:15: ( ' ' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 32) :
                    alt5 = 1


                if alt5 == 1:
                    # grammar/Frontend.g:67:15: ' '
                    pass 
                    self.match(32)


                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1





        finally:
            pass

    # $ANTLR end "SP"



    def mTokens(self):
        # grammar/Frontend.g:1:8: ( T__10 | T__11 | ID | NUMBER | WHITESPACE | NEWLINE )
        alt6 = 6
        LA6 = self.input.LA(1)
        if LA6 == 99:
            LA6_1 = self.input.LA(2)

            if (LA6_1 == 111) :
                LA6_7 = self.input.LA(3)

                if (LA6_7 == 110) :
                    LA6_9 = self.input.LA(4)

                    if (LA6_9 == 115) :
                        LA6_11 = self.input.LA(5)

                        if (LA6_11 == 116) :
                            LA6_13 = self.input.LA(6)

                            if (LA6_13 == 115) :
                                LA6_15 = self.input.LA(7)

                                if ((48 <= LA6_15 <= 57) or LA6_15 == 95 or (97 <= LA6_15 <= 122)) :
                                    alt6 = 3
                                else:
                                    alt6 = 1

                            else:
                                alt6 = 3

                        else:
                            alt6 = 3

                    else:
                        alt6 = 3

                else:
                    alt6 = 3

            else:
                alt6 = 3

        elif LA6 == 109:
            LA6_2 = self.input.LA(2)

            if (LA6_2 == 111) :
                LA6_8 = self.input.LA(3)

                if (LA6_8 == 100) :
                    LA6_10 = self.input.LA(4)

                    if (LA6_10 == 117) :
                        LA6_12 = self.input.LA(5)

                        if (LA6_12 == 108) :
                            LA6_14 = self.input.LA(6)

                            if (LA6_14 == 101) :
                                LA6_16 = self.input.LA(7)

                                if ((48 <= LA6_16 <= 57) or LA6_16 == 95 or (97 <= LA6_16 <= 122)) :
                                    alt6 = 3
                                else:
                                    alt6 = 2

                            else:
                                alt6 = 3

                        else:
                            alt6 = 3

                    else:
                        alt6 = 3

                else:
                    alt6 = 3

            else:
                alt6 = 3

        elif LA6 == 97 or LA6 == 98 or LA6 == 100 or LA6 == 101 or LA6 == 102 or LA6 == 103 or LA6 == 104 or LA6 == 105 or LA6 == 106 or LA6 == 107 or LA6 == 108 or LA6 == 110 or LA6 == 111 or LA6 == 112 or LA6 == 113 or LA6 == 114 or LA6 == 115 or LA6 == 116 or LA6 == 117 or LA6 == 118 or LA6 == 119 or LA6 == 120 or LA6 == 121 or LA6 == 122:
            alt6 = 3
        elif LA6 == 48 or LA6 == 49 or LA6 == 50 or LA6 == 51 or LA6 == 52 or LA6 == 53 or LA6 == 54 or LA6 == 55 or LA6 == 56 or LA6 == 57:
            alt6 = 4
        elif LA6 == 32:
            alt6 = 5
        elif LA6 == 10 or LA6 == 13:
            alt6 = 6
        else:
            nvae = NoViableAltException("", 6, 0, self.input)

            raise nvae


        if alt6 == 1:
            # grammar/Frontend.g:1:10: T__10
            pass 
            self.mT__10()



        elif alt6 == 2:
            # grammar/Frontend.g:1:16: T__11
            pass 
            self.mT__11()



        elif alt6 == 3:
            # grammar/Frontend.g:1:22: ID
            pass 
            self.mID()



        elif alt6 == 4:
            # grammar/Frontend.g:1:25: NUMBER
            pass 
            self.mNUMBER()



        elif alt6 == 5:
            # grammar/Frontend.g:1:32: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt6 == 6:
            # grammar/Frontend.g:1:43: NEWLINE
            pass 
            self.mNEWLINE()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(FrontendLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
