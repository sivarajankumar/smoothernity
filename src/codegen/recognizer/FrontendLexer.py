# $ANTLR 3.4 grammar/Frontend.g 2012-01-07 12:50:32

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
T__8=8
T__9=9
ID=4
NEWLINE=5
NUMBER=6
WHITESPACE=7


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



    # $ANTLR start "T__8"
    def mT__8(self, ):
        try:
            _type = T__8
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:17:6: ( 'consts' )
            # grammar/Frontend.g:17:8: 'consts'
            pass 
            self.match("consts")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__8"



    # $ANTLR start "T__9"
    def mT__9(self, ):
        try:
            _type = T__9
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:18:6: ( 'module' )
            # grammar/Frontend.g:18:8: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__9"



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



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):
        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:40:8: ( ( '0' .. '9' )+ )
            # grammar/Frontend.g:40:10: ( '0' .. '9' )+
            pass 
            # grammar/Frontend.g:40:10: ( '0' .. '9' )+
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



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:41:9: ( ( '\\r' )? '\\n' )
            # grammar/Frontend.g:41:11: ( '\\r' )? '\\n'
            pass 
            # grammar/Frontend.g:41:11: ( '\\r' )?
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 13) :
                alt3 = 1
            if alt3 == 1:
                # grammar/Frontend.g:41:11: '\\r'
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

            # grammar/Frontend.g:42:12: ( ( ' ' )+ )
            # grammar/Frontend.g:42:14: ( ' ' )+
            pass 
            # grammar/Frontend.g:42:14: ( ' ' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 32) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/Frontend.g:42:14: ' '
                    pass 
                    self.match(32)


                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1


            #action start
            self . skip ( ) 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITESPACE"



    def mTokens(self):
        # grammar/Frontend.g:1:8: ( T__8 | T__9 | ID | NUMBER | NEWLINE | WHITESPACE )
        alt5 = 6
        LA5 = self.input.LA(1)
        if LA5 == 99:
            LA5_1 = self.input.LA(2)

            if (LA5_1 == 111) :
                LA5_7 = self.input.LA(3)

                if (LA5_7 == 110) :
                    LA5_9 = self.input.LA(4)

                    if (LA5_9 == 115) :
                        LA5_11 = self.input.LA(5)

                        if (LA5_11 == 116) :
                            LA5_13 = self.input.LA(6)

                            if (LA5_13 == 115) :
                                LA5_15 = self.input.LA(7)

                                if ((48 <= LA5_15 <= 57) or LA5_15 == 95 or (97 <= LA5_15 <= 122)) :
                                    alt5 = 3
                                else:
                                    alt5 = 1

                            else:
                                alt5 = 3

                        else:
                            alt5 = 3

                    else:
                        alt5 = 3

                else:
                    alt5 = 3

            else:
                alt5 = 3

        elif LA5 == 109:
            LA5_2 = self.input.LA(2)

            if (LA5_2 == 111) :
                LA5_8 = self.input.LA(3)

                if (LA5_8 == 100) :
                    LA5_10 = self.input.LA(4)

                    if (LA5_10 == 117) :
                        LA5_12 = self.input.LA(5)

                        if (LA5_12 == 108) :
                            LA5_14 = self.input.LA(6)

                            if (LA5_14 == 101) :
                                LA5_16 = self.input.LA(7)

                                if ((48 <= LA5_16 <= 57) or LA5_16 == 95 or (97 <= LA5_16 <= 122)) :
                                    alt5 = 3
                                else:
                                    alt5 = 2

                            else:
                                alt5 = 3

                        else:
                            alt5 = 3

                    else:
                        alt5 = 3

                else:
                    alt5 = 3

            else:
                alt5 = 3

        elif LA5 == 97 or LA5 == 98 or LA5 == 100 or LA5 == 101 or LA5 == 102 or LA5 == 103 or LA5 == 104 or LA5 == 105 or LA5 == 106 or LA5 == 107 or LA5 == 108 or LA5 == 110 or LA5 == 111 or LA5 == 112 or LA5 == 113 or LA5 == 114 or LA5 == 115 or LA5 == 116 or LA5 == 117 or LA5 == 118 or LA5 == 119 or LA5 == 120 or LA5 == 121 or LA5 == 122:
            alt5 = 3
        elif LA5 == 48 or LA5 == 49 or LA5 == 50 or LA5 == 51 or LA5 == 52 or LA5 == 53 or LA5 == 54 or LA5 == 55 or LA5 == 56 or LA5 == 57:
            alt5 = 4
        elif LA5 == 10 or LA5 == 13:
            alt5 = 5
        elif LA5 == 32:
            alt5 = 6
        else:
            nvae = NoViableAltException("", 5, 0, self.input)

            raise nvae


        if alt5 == 1:
            # grammar/Frontend.g:1:10: T__8
            pass 
            self.mT__8()



        elif alt5 == 2:
            # grammar/Frontend.g:1:15: T__9
            pass 
            self.mT__9()



        elif alt5 == 3:
            # grammar/Frontend.g:1:20: ID
            pass 
            self.mID()



        elif alt5 == 4:
            # grammar/Frontend.g:1:23: NUMBER
            pass 
            self.mNUMBER()



        elif alt5 == 5:
            # grammar/Frontend.g:1:30: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt5 == 6:
            # grammar/Frontend.g:1:38: WHITESPACE
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
