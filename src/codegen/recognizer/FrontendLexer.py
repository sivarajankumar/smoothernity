# $ANTLR 3.4 grammar/Frontend.g 2012-01-06 13:08:35

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
T__7=7
T__8=8
ID=4
NEWLINE=5
WHITESPACE=6


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



    # $ANTLR start "T__7"
    def mT__7(self, ):
        try:
            _type = T__7
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:17:6: ( 'consts' )
            # grammar/Frontend.g:17:8: 'consts'
            pass 
            self.match("consts")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__7"



    # $ANTLR start "T__8"
    def mT__8(self, ):
        try:
            _type = T__8
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:18:6: ( 'module' )
            # grammar/Frontend.g:18:8: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__8"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:39:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/Frontend.g:39:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/Frontend.g:39:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:40:9: ( ( '\\r' )? '\\n' )
            # grammar/Frontend.g:40:11: ( '\\r' )? '\\n'
            pass 
            # grammar/Frontend.g:40:11: ( '\\r' )?
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 13) :
                alt2 = 1
            if alt2 == 1:
                # grammar/Frontend.g:40:11: '\\r'
                pass 
                self.match(13)




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

            # grammar/Frontend.g:41:12: ( ( ' ' )+ )
            # grammar/Frontend.g:41:14: ( ' ' )+
            pass 
            # grammar/Frontend.g:41:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/Frontend.g:41:14: ' '
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
        # grammar/Frontend.g:1:8: ( T__7 | T__8 | ID | NEWLINE | WHITESPACE )
        alt4 = 5
        LA4 = self.input.LA(1)
        if LA4 == 99:
            LA4_1 = self.input.LA(2)

            if (LA4_1 == 111) :
                LA4_6 = self.input.LA(3)

                if (LA4_6 == 110) :
                    LA4_8 = self.input.LA(4)

                    if (LA4_8 == 115) :
                        LA4_10 = self.input.LA(5)

                        if (LA4_10 == 116) :
                            LA4_12 = self.input.LA(6)

                            if (LA4_12 == 115) :
                                LA4_14 = self.input.LA(7)

                                if ((48 <= LA4_14 <= 57) or LA4_14 == 95 or (97 <= LA4_14 <= 122)) :
                                    alt4 = 3
                                else:
                                    alt4 = 1

                            else:
                                alt4 = 3

                        else:
                            alt4 = 3

                    else:
                        alt4 = 3

                else:
                    alt4 = 3

            else:
                alt4 = 3

        elif LA4 == 109:
            LA4_2 = self.input.LA(2)

            if (LA4_2 == 111) :
                LA4_7 = self.input.LA(3)

                if (LA4_7 == 100) :
                    LA4_9 = self.input.LA(4)

                    if (LA4_9 == 117) :
                        LA4_11 = self.input.LA(5)

                        if (LA4_11 == 108) :
                            LA4_13 = self.input.LA(6)

                            if (LA4_13 == 101) :
                                LA4_15 = self.input.LA(7)

                                if ((48 <= LA4_15 <= 57) or LA4_15 == 95 or (97 <= LA4_15 <= 122)) :
                                    alt4 = 3
                                else:
                                    alt4 = 2

                            else:
                                alt4 = 3

                        else:
                            alt4 = 3

                    else:
                        alt4 = 3

                else:
                    alt4 = 3

            else:
                alt4 = 3

        elif LA4 == 97 or LA4 == 98 or LA4 == 100 or LA4 == 101 or LA4 == 102 or LA4 == 103 or LA4 == 104 or LA4 == 105 or LA4 == 106 or LA4 == 107 or LA4 == 108 or LA4 == 110 or LA4 == 111 or LA4 == 112 or LA4 == 113 or LA4 == 114 or LA4 == 115 or LA4 == 116 or LA4 == 117 or LA4 == 118 or LA4 == 119 or LA4 == 120 or LA4 == 121 or LA4 == 122:
            alt4 = 3
        elif LA4 == 10 or LA4 == 13:
            alt4 = 4
        elif LA4 == 32:
            alt4 = 5
        else:
            nvae = NoViableAltException("", 4, 0, self.input)

            raise nvae


        if alt4 == 1:
            # grammar/Frontend.g:1:10: T__7
            pass 
            self.mT__7()



        elif alt4 == 2:
            # grammar/Frontend.g:1:15: T__8
            pass 
            self.mT__8()



        elif alt4 == 3:
            # grammar/Frontend.g:1:20: ID
            pass 
            self.mID()



        elif alt4 == 4:
            # grammar/Frontend.g:1:23: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt4 == 5:
            # grammar/Frontend.g:1:31: WHITESPACE
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
