# $ANTLR 3.4 grammar/Frontend.g 2012-01-11 20:50:10

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
CONSTS=4
DEDENT=5
ID=6
INDENT=7
MODULE=8
NUMBER=9
WHITESPACE=10


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



    # $ANTLR start "CONSTS"
    def mCONSTS(self, ):
        try:
            _type = CONSTS
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:43:8: ( 'consts' )
            # grammar/Frontend.g:43:10: 'consts'
            pass 
            self.match("consts")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONSTS"



    # $ANTLR start "MODULE"
    def mMODULE(self, ):
        try:
            _type = MODULE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:44:8: ( 'module' )
            # grammar/Frontend.g:44:10: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULE"



    # $ANTLR start "INDENT"
    def mINDENT(self, ):
        try:
            _type = INDENT
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:45:8: ( 'indent' )
            # grammar/Frontend.g:45:10: 'indent'
            pass 
            self.match("indent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INDENT"



    # $ANTLR start "DEDENT"
    def mDEDENT(self, ):
        try:
            _type = DEDENT
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:46:8: ( 'dedent' )
            # grammar/Frontend.g:46:10: 'dedent'
            pass 
            self.match("dedent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEDENT"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:47:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/Frontend.g:47:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/Frontend.g:47:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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

            # grammar/Frontend.g:48:8: ( ( '0' .. '9' )+ )
            # grammar/Frontend.g:48:10: ( '0' .. '9' )+
            pass 
            # grammar/Frontend.g:48:10: ( '0' .. '9' )+
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

            # grammar/Frontend.g:49:12: ( ( ' ' )+ )
            # grammar/Frontend.g:49:14: ( ' ' )+
            pass 
            # grammar/Frontend.g:49:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/Frontend.g:49:14: ' '
                    pass 
                    self.match(32)


                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1


            #action start
            self . skip ( ) 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # grammar/Frontend.g:1:8: ( CONSTS | MODULE | INDENT | DEDENT | ID | NUMBER | WHITESPACE )
        alt4 = 7
        LA4 = self.input.LA(1)
        if LA4 == 99:
            LA4_1 = self.input.LA(2)

            if (LA4_1 == 111) :
                LA4_8 = self.input.LA(3)

                if (LA4_8 == 110) :
                    LA4_12 = self.input.LA(4)

                    if (LA4_12 == 115) :
                        LA4_16 = self.input.LA(5)

                        if (LA4_16 == 116) :
                            LA4_20 = self.input.LA(6)

                            if (LA4_20 == 115) :
                                LA4_24 = self.input.LA(7)

                                if ((48 <= LA4_24 <= 57) or LA4_24 == 95 or (97 <= LA4_24 <= 122)) :
                                    alt4 = 5
                                else:
                                    alt4 = 1

                            else:
                                alt4 = 5

                        else:
                            alt4 = 5

                    else:
                        alt4 = 5

                else:
                    alt4 = 5

            else:
                alt4 = 5

        elif LA4 == 109:
            LA4_2 = self.input.LA(2)

            if (LA4_2 == 111) :
                LA4_9 = self.input.LA(3)

                if (LA4_9 == 100) :
                    LA4_13 = self.input.LA(4)

                    if (LA4_13 == 117) :
                        LA4_17 = self.input.LA(5)

                        if (LA4_17 == 108) :
                            LA4_21 = self.input.LA(6)

                            if (LA4_21 == 101) :
                                LA4_25 = self.input.LA(7)

                                if ((48 <= LA4_25 <= 57) or LA4_25 == 95 or (97 <= LA4_25 <= 122)) :
                                    alt4 = 5
                                else:
                                    alt4 = 2

                            else:
                                alt4 = 5

                        else:
                            alt4 = 5

                    else:
                        alt4 = 5

                else:
                    alt4 = 5

            else:
                alt4 = 5

        elif LA4 == 105:
            LA4_3 = self.input.LA(2)

            if (LA4_3 == 110) :
                LA4_10 = self.input.LA(3)

                if (LA4_10 == 100) :
                    LA4_14 = self.input.LA(4)

                    if (LA4_14 == 101) :
                        LA4_18 = self.input.LA(5)

                        if (LA4_18 == 110) :
                            LA4_22 = self.input.LA(6)

                            if (LA4_22 == 116) :
                                LA4_26 = self.input.LA(7)

                                if ((48 <= LA4_26 <= 57) or LA4_26 == 95 or (97 <= LA4_26 <= 122)) :
                                    alt4 = 5
                                else:
                                    alt4 = 3

                            else:
                                alt4 = 5

                        else:
                            alt4 = 5

                    else:
                        alt4 = 5

                else:
                    alt4 = 5

            else:
                alt4 = 5

        elif LA4 == 100:
            LA4_4 = self.input.LA(2)

            if (LA4_4 == 101) :
                LA4_11 = self.input.LA(3)

                if (LA4_11 == 100) :
                    LA4_15 = self.input.LA(4)

                    if (LA4_15 == 101) :
                        LA4_19 = self.input.LA(5)

                        if (LA4_19 == 110) :
                            LA4_23 = self.input.LA(6)

                            if (LA4_23 == 116) :
                                LA4_27 = self.input.LA(7)

                                if ((48 <= LA4_27 <= 57) or LA4_27 == 95 or (97 <= LA4_27 <= 122)) :
                                    alt4 = 5
                                else:
                                    alt4 = 4

                            else:
                                alt4 = 5

                        else:
                            alt4 = 5

                    else:
                        alt4 = 5

                else:
                    alt4 = 5

            else:
                alt4 = 5

        elif LA4 == 97 or LA4 == 98 or LA4 == 101 or LA4 == 102 or LA4 == 103 or LA4 == 104 or LA4 == 106 or LA4 == 107 or LA4 == 108 or LA4 == 110 or LA4 == 111 or LA4 == 112 or LA4 == 113 or LA4 == 114 or LA4 == 115 or LA4 == 116 or LA4 == 117 or LA4 == 118 or LA4 == 119 or LA4 == 120 or LA4 == 121 or LA4 == 122:
            alt4 = 5
        elif LA4 == 48 or LA4 == 49 or LA4 == 50 or LA4 == 51 or LA4 == 52 or LA4 == 53 or LA4 == 54 or LA4 == 55 or LA4 == 56 or LA4 == 57:
            alt4 = 6
        elif LA4 == 32:
            alt4 = 7
        else:
            nvae = NoViableAltException("", 4, 0, self.input)

            raise nvae


        if alt4 == 1:
            # grammar/Frontend.g:1:10: CONSTS
            pass 
            self.mCONSTS()



        elif alt4 == 2:
            # grammar/Frontend.g:1:17: MODULE
            pass 
            self.mMODULE()



        elif alt4 == 3:
            # grammar/Frontend.g:1:24: INDENT
            pass 
            self.mINDENT()



        elif alt4 == 4:
            # grammar/Frontend.g:1:31: DEDENT
            pass 
            self.mDEDENT()



        elif alt4 == 5:
            # grammar/Frontend.g:1:38: ID
            pass 
            self.mID()



        elif alt4 == 6:
            # grammar/Frontend.g:1:41: NUMBER
            pass 
            self.mNUMBER()



        elif alt4 == 7:
            # grammar/Frontend.g:1:48: WHITESPACE
            pass 
            self.mWHITESPACE()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(FrontendLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
