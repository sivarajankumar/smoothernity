# $ANTLR 3.4 copypaster/Frontend.g 2012-01-16 18:05:35

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CHARS=4
DEDENT=5
INDENT=6
NEWLINE=7
WHITESPACE=8


class FrontendLexer(Lexer):

    grammarFileName = "copypaster/Frontend.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(FrontendLexer, self).__init__(input, state)

        self.delegates = []






    # $ANTLR start "DEDENT"
    def mDEDENT(self, ):
        try:
            _type = DEDENT
            _channel = DEFAULT_CHANNEL

            # copypaster/Frontend.g:12:8: ( 'dedent' )
            # copypaster/Frontend.g:12:10: 'dedent'
            pass 
            self.match("dedent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEDENT"



    # $ANTLR start "INDENT"
    def mINDENT(self, ):
        try:
            _type = INDENT
            _channel = DEFAULT_CHANNEL

            # copypaster/Frontend.g:13:8: ( 'indent' )
            # copypaster/Frontend.g:13:10: 'indent'
            pass 
            self.match("indent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INDENT"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # copypaster/Frontend.g:14:9: ( '\\n' )
            # copypaster/Frontend.g:14:11: '\\n'
            pass 
            self.match(10)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):
        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # copypaster/Frontend.g:15:12: ( ( ' ' )+ )
            # copypaster/Frontend.g:15:14: ( ' ' )+
            pass 
            # copypaster/Frontend.g:15:14: ( ' ' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 32) :
                    alt1 = 1


                if alt1 == 1:
                    # copypaster/Frontend.g:15:14: ' '
                    pass 
                    self.match(32)


                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1


            #action start
            self . skip ( ) 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "CHARS"
    def mCHARS(self, ):
        try:
            _type = CHARS
            _channel = DEFAULT_CHANNEL

            # copypaster/Frontend.g:16:7: ( ( 'a' .. 'z' | '0' .. '9' )* )
            # copypaster/Frontend.g:16:9: ( 'a' .. 'z' | '0' .. '9' )*
            pass 
            # copypaster/Frontend.g:16:9: ( 'a' .. 'z' | '0' .. '9' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57) or (97 <= LA2_0 <= 122)) :
                    alt2 = 1


                if alt2 == 1:
                    # copypaster/Frontend.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHARS"



    def mTokens(self):
        # copypaster/Frontend.g:1:8: ( DEDENT | INDENT | NEWLINE | WHITESPACE | CHARS )
        alt3 = 5
        LA3 = self.input.LA(1)
        if LA3 == 100:
            LA3_1 = self.input.LA(2)

            if (LA3_1 == 101) :
                LA3_6 = self.input.LA(3)

                if (LA3_6 == 100) :
                    LA3_8 = self.input.LA(4)

                    if (LA3_8 == 101) :
                        LA3_10 = self.input.LA(5)

                        if (LA3_10 == 110) :
                            LA3_12 = self.input.LA(6)

                            if (LA3_12 == 116) :
                                LA3_14 = self.input.LA(7)

                                if ((48 <= LA3_14 <= 57) or (97 <= LA3_14 <= 122)) :
                                    alt3 = 5
                                else:
                                    alt3 = 1

                            else:
                                alt3 = 5

                        else:
                            alt3 = 5

                    else:
                        alt3 = 5

                else:
                    alt3 = 5

            else:
                alt3 = 5

        elif LA3 == 105:
            LA3_2 = self.input.LA(2)

            if (LA3_2 == 110) :
                LA3_7 = self.input.LA(3)

                if (LA3_7 == 100) :
                    LA3_9 = self.input.LA(4)

                    if (LA3_9 == 101) :
                        LA3_11 = self.input.LA(5)

                        if (LA3_11 == 110) :
                            LA3_13 = self.input.LA(6)

                            if (LA3_13 == 116) :
                                LA3_15 = self.input.LA(7)

                                if ((48 <= LA3_15 <= 57) or (97 <= LA3_15 <= 122)) :
                                    alt3 = 5
                                else:
                                    alt3 = 2

                            else:
                                alt3 = 5

                        else:
                            alt3 = 5

                    else:
                        alt3 = 5

                else:
                    alt3 = 5

            else:
                alt3 = 5

        elif LA3 == 10:
            alt3 = 3
        elif LA3 == 32:
            alt3 = 4
        else:
            alt3 = 5

        if alt3 == 1:
            # copypaster/Frontend.g:1:10: DEDENT
            pass 
            self.mDEDENT()



        elif alt3 == 2:
            # copypaster/Frontend.g:1:17: INDENT
            pass 
            self.mINDENT()



        elif alt3 == 3:
            # copypaster/Frontend.g:1:24: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt3 == 4:
            # copypaster/Frontend.g:1:32: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt3 == 5:
            # copypaster/Frontend.g:1:43: CHARS
            pass 
            self.mCHARS()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(FrontendLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
