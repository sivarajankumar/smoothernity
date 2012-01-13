# $ANTLR 3.4 grammar/Frontend.g 2012-01-13 18:20:10

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
DIVIDE=6
EXPRESSION=7
ID=8
INDENT=9
MINUS=10
MODULE=11
NEWLINE=12
NUMBER=13
TREE_EXPRESSION=14
TREE_NUM_FRACT=15
TREE_NUM_WHOLE=16
TYPES=17
WHITESPACE=18


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

            # grammar/Frontend.g:72:8: ( 'consts' )
            # grammar/Frontend.g:72:10: 'consts'
            pass 
            self.match("consts")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONSTS"



    # $ANTLR start "DEDENT"
    def mDEDENT(self, ):
        try:
            _type = DEDENT
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:73:8: ( 'dedent' )
            # grammar/Frontend.g:73:10: 'dedent'
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

            # grammar/Frontend.g:74:8: ( 'indent' )
            # grammar/Frontend.g:74:10: 'indent'
            pass 
            self.match("indent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INDENT"



    # $ANTLR start "MODULE"
    def mMODULE(self, ):
        try:
            _type = MODULE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:75:8: ( 'module' )
            # grammar/Frontend.g:75:10: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULE"



    # $ANTLR start "TYPES"
    def mTYPES(self, ):
        try:
            _type = TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:76:7: ( 'types' )
            # grammar/Frontend.g:76:9: 'types'
            pass 
            self.match("types")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPES"



    # $ANTLR start "TREE_NUM_WHOLE"
    def mTREE_NUM_WHOLE(self, ):
        try:
            _type = TREE_NUM_WHOLE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:78:16: ( 'TREE_NUM_WHOLE' )
            # grammar/Frontend.g:78:18: 'TREE_NUM_WHOLE'
            pass 
            self.match("TREE_NUM_WHOLE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_NUM_WHOLE"



    # $ANTLR start "TREE_NUM_FRACT"
    def mTREE_NUM_FRACT(self, ):
        try:
            _type = TREE_NUM_FRACT
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:79:16: ( 'TREE_NUM_FRACT' )
            # grammar/Frontend.g:79:18: 'TREE_NUM_FRACT'
            pass 
            self.match("TREE_NUM_FRACT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_NUM_FRACT"



    # $ANTLR start "TREE_EXPRESSION"
    def mTREE_EXPRESSION(self, ):
        try:
            _type = TREE_EXPRESSION
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:80:17: ( 'TREE_EXPRESSION' )
            # grammar/Frontend.g:80:19: 'TREE_EXPRESSION'
            pass 
            self.match("TREE_EXPRESSION")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_EXPRESSION"



    # $ANTLR start "DIVIDE"
    def mDIVIDE(self, ):
        try:
            _type = DIVIDE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:82:8: ( '/' )
            # grammar/Frontend.g:82:10: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIVIDE"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):
        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:83:7: ( '-' )
            # grammar/Frontend.g:83:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:84:9: ( '\\n' )
            # grammar/Frontend.g:84:11: '\\n'
            pass 
            self.match(10)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:85:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/Frontend.g:85:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/Frontend.g:85:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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

            # grammar/Frontend.g:86:8: ( ( '0' .. '9' )+ )
            # grammar/Frontend.g:86:10: ( '0' .. '9' )+
            pass 
            # grammar/Frontend.g:86:10: ( '0' .. '9' )+
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

            # grammar/Frontend.g:87:12: ( ( ' ' )+ )
            # grammar/Frontend.g:87:14: ( ' ' )+
            pass 
            # grammar/Frontend.g:87:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/Frontend.g:87:14: ' '
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



    # $ANTLR start "EXPRESSION"
    def mEXPRESSION(self, ):
        try:
            _type = EXPRESSION
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:88:12: ( '[' ( . )* ']' )
            # grammar/Frontend.g:88:14: '[' ( . )* ']'
            pass 
            self.match(91)

            # grammar/Frontend.g:88:18: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 93) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 92) or (94 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/Frontend.g:88:18: .
                    pass 
                    self.matchAny()


                else:
                    break #loop4


            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EXPRESSION"



    def mTokens(self):
        # grammar/Frontend.g:1:8: ( CONSTS | DEDENT | INDENT | MODULE | TYPES | TREE_NUM_WHOLE | TREE_NUM_FRACT | TREE_EXPRESSION | DIVIDE | MINUS | NEWLINE | ID | NUMBER | WHITESPACE | EXPRESSION )
        alt5 = 15
        LA5 = self.input.LA(1)
        if LA5 == 99:
            LA5_1 = self.input.LA(2)

            if (LA5_1 == 111) :
                LA5_14 = self.input.LA(3)

                if (LA5_14 == 110) :
                    LA5_20 = self.input.LA(4)

                    if (LA5_20 == 115) :
                        LA5_26 = self.input.LA(5)

                        if (LA5_26 == 116) :
                            LA5_32 = self.input.LA(6)

                            if (LA5_32 == 115) :
                                LA5_38 = self.input.LA(7)

                                if ((48 <= LA5_38 <= 57) or LA5_38 == 95 or (97 <= LA5_38 <= 122)) :
                                    alt5 = 12
                                else:
                                    alt5 = 1

                            else:
                                alt5 = 12

                        else:
                            alt5 = 12

                    else:
                        alt5 = 12

                else:
                    alt5 = 12

            else:
                alt5 = 12

        elif LA5 == 100:
            LA5_2 = self.input.LA(2)

            if (LA5_2 == 101) :
                LA5_15 = self.input.LA(3)

                if (LA5_15 == 100) :
                    LA5_21 = self.input.LA(4)

                    if (LA5_21 == 101) :
                        LA5_27 = self.input.LA(5)

                        if (LA5_27 == 110) :
                            LA5_33 = self.input.LA(6)

                            if (LA5_33 == 116) :
                                LA5_39 = self.input.LA(7)

                                if ((48 <= LA5_39 <= 57) or LA5_39 == 95 or (97 <= LA5_39 <= 122)) :
                                    alt5 = 12
                                else:
                                    alt5 = 2

                            else:
                                alt5 = 12

                        else:
                            alt5 = 12

                    else:
                        alt5 = 12

                else:
                    alt5 = 12

            else:
                alt5 = 12

        elif LA5 == 105:
            LA5_3 = self.input.LA(2)

            if (LA5_3 == 110) :
                LA5_16 = self.input.LA(3)

                if (LA5_16 == 100) :
                    LA5_22 = self.input.LA(4)

                    if (LA5_22 == 101) :
                        LA5_28 = self.input.LA(5)

                        if (LA5_28 == 110) :
                            LA5_34 = self.input.LA(6)

                            if (LA5_34 == 116) :
                                LA5_40 = self.input.LA(7)

                                if ((48 <= LA5_40 <= 57) or LA5_40 == 95 or (97 <= LA5_40 <= 122)) :
                                    alt5 = 12
                                else:
                                    alt5 = 3

                            else:
                                alt5 = 12

                        else:
                            alt5 = 12

                    else:
                        alt5 = 12

                else:
                    alt5 = 12

            else:
                alt5 = 12

        elif LA5 == 109:
            LA5_4 = self.input.LA(2)

            if (LA5_4 == 111) :
                LA5_17 = self.input.LA(3)

                if (LA5_17 == 100) :
                    LA5_23 = self.input.LA(4)

                    if (LA5_23 == 117) :
                        LA5_29 = self.input.LA(5)

                        if (LA5_29 == 108) :
                            LA5_35 = self.input.LA(6)

                            if (LA5_35 == 101) :
                                LA5_41 = self.input.LA(7)

                                if ((48 <= LA5_41 <= 57) or LA5_41 == 95 or (97 <= LA5_41 <= 122)) :
                                    alt5 = 12
                                else:
                                    alt5 = 4

                            else:
                                alt5 = 12

                        else:
                            alt5 = 12

                    else:
                        alt5 = 12

                else:
                    alt5 = 12

            else:
                alt5 = 12

        elif LA5 == 116:
            LA5_5 = self.input.LA(2)

            if (LA5_5 == 121) :
                LA5_18 = self.input.LA(3)

                if (LA5_18 == 112) :
                    LA5_24 = self.input.LA(4)

                    if (LA5_24 == 101) :
                        LA5_30 = self.input.LA(5)

                        if (LA5_30 == 115) :
                            LA5_36 = self.input.LA(6)

                            if ((48 <= LA5_36 <= 57) or LA5_36 == 95 or (97 <= LA5_36 <= 122)) :
                                alt5 = 12
                            else:
                                alt5 = 5

                        else:
                            alt5 = 12

                    else:
                        alt5 = 12

                else:
                    alt5 = 12

            else:
                alt5 = 12

        elif LA5 == 84:
            LA5_6 = self.input.LA(2)

            if (LA5_6 == 82) :
                LA5_19 = self.input.LA(3)

                if (LA5_19 == 69) :
                    LA5_25 = self.input.LA(4)

                    if (LA5_25 == 69) :
                        LA5_31 = self.input.LA(5)

                        if (LA5_31 == 95) :
                            LA5_37 = self.input.LA(6)

                            if (LA5_37 == 78) :
                                LA5_43 = self.input.LA(7)

                                if (LA5_43 == 85) :
                                    LA5_49 = self.input.LA(8)

                                    if (LA5_49 == 77) :
                                        LA5_50 = self.input.LA(9)

                                        if (LA5_50 == 95) :
                                            LA5_51 = self.input.LA(10)

                                            if (LA5_51 == 87) :
                                                alt5 = 6
                                            elif (LA5_51 == 70) :
                                                alt5 = 7
                                            else:
                                                nvae = NoViableAltException("", 5, 51, self.input)

                                                raise nvae


                                        else:
                                            nvae = NoViableAltException("", 5, 50, self.input)

                                            raise nvae


                                    else:
                                        nvae = NoViableAltException("", 5, 49, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 5, 43, self.input)

                                    raise nvae


                            elif (LA5_37 == 69) :
                                alt5 = 8
                            else:
                                nvae = NoViableAltException("", 5, 37, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 5, 31, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 5, 25, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 5, 19, self.input)

                    raise nvae


            else:
                nvae = NoViableAltException("", 5, 6, self.input)

                raise nvae


        elif LA5 == 47:
            alt5 = 9
        elif LA5 == 45:
            alt5 = 10
        elif LA5 == 10:
            alt5 = 11
        elif LA5 == 97 or LA5 == 98 or LA5 == 101 or LA5 == 102 or LA5 == 103 or LA5 == 104 or LA5 == 106 or LA5 == 107 or LA5 == 108 or LA5 == 110 or LA5 == 111 or LA5 == 112 or LA5 == 113 or LA5 == 114 or LA5 == 115 or LA5 == 117 or LA5 == 118 or LA5 == 119 or LA5 == 120 or LA5 == 121 or LA5 == 122:
            alt5 = 12
        elif LA5 == 48 or LA5 == 49 or LA5 == 50 or LA5 == 51 or LA5 == 52 or LA5 == 53 or LA5 == 54 or LA5 == 55 or LA5 == 56 or LA5 == 57:
            alt5 = 13
        elif LA5 == 32:
            alt5 = 14
        elif LA5 == 91:
            alt5 = 15
        else:
            nvae = NoViableAltException("", 5, 0, self.input)

            raise nvae


        if alt5 == 1:
            # grammar/Frontend.g:1:10: CONSTS
            pass 
            self.mCONSTS()



        elif alt5 == 2:
            # grammar/Frontend.g:1:17: DEDENT
            pass 
            self.mDEDENT()



        elif alt5 == 3:
            # grammar/Frontend.g:1:24: INDENT
            pass 
            self.mINDENT()



        elif alt5 == 4:
            # grammar/Frontend.g:1:31: MODULE
            pass 
            self.mMODULE()



        elif alt5 == 5:
            # grammar/Frontend.g:1:38: TYPES
            pass 
            self.mTYPES()



        elif alt5 == 6:
            # grammar/Frontend.g:1:44: TREE_NUM_WHOLE
            pass 
            self.mTREE_NUM_WHOLE()



        elif alt5 == 7:
            # grammar/Frontend.g:1:59: TREE_NUM_FRACT
            pass 
            self.mTREE_NUM_FRACT()



        elif alt5 == 8:
            # grammar/Frontend.g:1:74: TREE_EXPRESSION
            pass 
            self.mTREE_EXPRESSION()



        elif alt5 == 9:
            # grammar/Frontend.g:1:90: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt5 == 10:
            # grammar/Frontend.g:1:97: MINUS
            pass 
            self.mMINUS()



        elif alt5 == 11:
            # grammar/Frontend.g:1:103: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt5 == 12:
            # grammar/Frontend.g:1:111: ID
            pass 
            self.mID()



        elif alt5 == 13:
            # grammar/Frontend.g:1:114: NUMBER
            pass 
            self.mNUMBER()



        elif alt5 == 14:
            # grammar/Frontend.g:1:121: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt5 == 15:
            # grammar/Frontend.g:1:132: EXPRESSION
            pass 
            self.mEXPRESSION()








 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(FrontendLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
