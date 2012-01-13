# $ANTLR 3.4 grammar/Frontend.g 2012-01-13 18:49:23

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
TREE_CONSTS=14
TREE_EXPRESSION=15
TREE_MODULE=16
TREE_NUM_FRACT=17
TREE_NUM_WHOLE=18
TREE_TYPES=19
TREE_TYPES_ITEM=20
TREE_TYPES_ITEM_ATTR=21
TREE_TYPES_ITEM_ATTRS=22
TYPES=23
WHITESPACE=24


class FrontendLexer(Lexer):

    grammarFileName = "grammar/Frontend.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(FrontendLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )




             
    def emitErrorMessage ( self , msg ) :
        raise FrontendLexerException ( msg )



    # $ANTLR start "CONSTS"
    def mCONSTS(self, ):
        try:
            _type = CONSTS
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:80:8: ( 'consts' )
            # grammar/Frontend.g:80:10: 'consts'
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

            # grammar/Frontend.g:81:8: ( 'dedent' )
            # grammar/Frontend.g:81:10: 'dedent'
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

            # grammar/Frontend.g:82:8: ( 'indent' )
            # grammar/Frontend.g:82:10: 'indent'
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

            # grammar/Frontend.g:83:8: ( 'module' )
            # grammar/Frontend.g:83:10: 'module'
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

            # grammar/Frontend.g:84:7: ( 'types' )
            # grammar/Frontend.g:84:9: 'types'
            pass 
            self.match("types")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPES"



    # $ANTLR start "TREE_CONSTS"
    def mTREE_CONSTS(self, ):
        try:
            _type = TREE_CONSTS
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:86:13: ( 'TREE_CONSTS' )
            # grammar/Frontend.g:86:15: 'TREE_CONSTS'
            pass 
            self.match("TREE_CONSTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_CONSTS"



    # $ANTLR start "TREE_EXPRESSION"
    def mTREE_EXPRESSION(self, ):
        try:
            _type = TREE_EXPRESSION
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:87:17: ( 'TREE_EXPRESSION' )
            # grammar/Frontend.g:87:19: 'TREE_EXPRESSION'
            pass 
            self.match("TREE_EXPRESSION")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_EXPRESSION"



    # $ANTLR start "TREE_MODULE"
    def mTREE_MODULE(self, ):
        try:
            _type = TREE_MODULE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:88:13: ( 'TREE_MODULE' )
            # grammar/Frontend.g:88:15: 'TREE_MODULE'
            pass 
            self.match("TREE_MODULE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MODULE"



    # $ANTLR start "TREE_NUM_FRACT"
    def mTREE_NUM_FRACT(self, ):
        try:
            _type = TREE_NUM_FRACT
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:89:16: ( 'TREE_NUM_FRACT' )
            # grammar/Frontend.g:89:18: 'TREE_NUM_FRACT'
            pass 
            self.match("TREE_NUM_FRACT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_NUM_FRACT"



    # $ANTLR start "TREE_NUM_WHOLE"
    def mTREE_NUM_WHOLE(self, ):
        try:
            _type = TREE_NUM_WHOLE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:90:16: ( 'TREE_NUM_WHOLE' )
            # grammar/Frontend.g:90:18: 'TREE_NUM_WHOLE'
            pass 
            self.match("TREE_NUM_WHOLE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_NUM_WHOLE"



    # $ANTLR start "TREE_TYPES"
    def mTREE_TYPES(self, ):
        try:
            _type = TREE_TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:91:12: ( 'TREE_TYPES' )
            # grammar/Frontend.g:91:14: 'TREE_TYPES'
            pass 
            self.match("TREE_TYPES")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES"



    # $ANTLR start "TREE_TYPES_ITEM"
    def mTREE_TYPES_ITEM(self, ):
        try:
            _type = TREE_TYPES_ITEM
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:92:17: ( 'TREE_TYPES_ITEM' )
            # grammar/Frontend.g:92:19: 'TREE_TYPES_ITEM'
            pass 
            self.match("TREE_TYPES_ITEM")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM"



    # $ANTLR start "TREE_TYPES_ITEM_ATTR"
    def mTREE_TYPES_ITEM_ATTR(self, ):
        try:
            _type = TREE_TYPES_ITEM_ATTR
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:93:22: ( 'TREE_TYPES_ITEM_ATTR' )
            # grammar/Frontend.g:93:24: 'TREE_TYPES_ITEM_ATTR'
            pass 
            self.match("TREE_TYPES_ITEM_ATTR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM_ATTR"



    # $ANTLR start "TREE_TYPES_ITEM_ATTRS"
    def mTREE_TYPES_ITEM_ATTRS(self, ):
        try:
            _type = TREE_TYPES_ITEM_ATTRS
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:94:23: ( 'TREE_TYPES_ITEM_ATTRS' )
            # grammar/Frontend.g:94:25: 'TREE_TYPES_ITEM_ATTRS'
            pass 
            self.match("TREE_TYPES_ITEM_ATTRS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM_ATTRS"



    # $ANTLR start "DIVIDE"
    def mDIVIDE(self, ):
        try:
            _type = DIVIDE
            _channel = DEFAULT_CHANNEL

            # grammar/Frontend.g:96:8: ( '/' )
            # grammar/Frontend.g:96:10: '/'
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

            # grammar/Frontend.g:97:7: ( '-' )
            # grammar/Frontend.g:97:9: '-'
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

            # grammar/Frontend.g:98:9: ( '\\n' )
            # grammar/Frontend.g:98:11: '\\n'
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

            # grammar/Frontend.g:99:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/Frontend.g:99:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/Frontend.g:99:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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

            # grammar/Frontend.g:100:8: ( ( '0' .. '9' )+ )
            # grammar/Frontend.g:100:10: ( '0' .. '9' )+
            pass 
            # grammar/Frontend.g:100:10: ( '0' .. '9' )+
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

            # grammar/Frontend.g:101:12: ( ( ' ' )+ )
            # grammar/Frontend.g:101:14: ( ' ' )+
            pass 
            # grammar/Frontend.g:101:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/Frontend.g:101:14: ' '
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

            # grammar/Frontend.g:102:12: ( '[' ( . )* ']' )
            # grammar/Frontend.g:102:14: '[' ( . )* ']'
            pass 
            self.match(91)

            # grammar/Frontend.g:102:18: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 93) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 92) or (94 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/Frontend.g:102:18: .
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
        # grammar/Frontend.g:1:8: ( CONSTS | DEDENT | INDENT | MODULE | TYPES | TREE_CONSTS | TREE_EXPRESSION | TREE_MODULE | TREE_NUM_FRACT | TREE_NUM_WHOLE | TREE_TYPES | TREE_TYPES_ITEM | TREE_TYPES_ITEM_ATTR | TREE_TYPES_ITEM_ATTRS | DIVIDE | MINUS | NEWLINE | ID | NUMBER | WHITESPACE | EXPRESSION )
        alt5 = 21
        alt5 = self.dfa5.predict(self.input)
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
            # grammar/Frontend.g:1:44: TREE_CONSTS
            pass 
            self.mTREE_CONSTS()



        elif alt5 == 7:
            # grammar/Frontend.g:1:56: TREE_EXPRESSION
            pass 
            self.mTREE_EXPRESSION()



        elif alt5 == 8:
            # grammar/Frontend.g:1:72: TREE_MODULE
            pass 
            self.mTREE_MODULE()



        elif alt5 == 9:
            # grammar/Frontend.g:1:84: TREE_NUM_FRACT
            pass 
            self.mTREE_NUM_FRACT()



        elif alt5 == 10:
            # grammar/Frontend.g:1:99: TREE_NUM_WHOLE
            pass 
            self.mTREE_NUM_WHOLE()



        elif alt5 == 11:
            # grammar/Frontend.g:1:114: TREE_TYPES
            pass 
            self.mTREE_TYPES()



        elif alt5 == 12:
            # grammar/Frontend.g:1:125: TREE_TYPES_ITEM
            pass 
            self.mTREE_TYPES_ITEM()



        elif alt5 == 13:
            # grammar/Frontend.g:1:141: TREE_TYPES_ITEM_ATTR
            pass 
            self.mTREE_TYPES_ITEM_ATTR()



        elif alt5 == 14:
            # grammar/Frontend.g:1:162: TREE_TYPES_ITEM_ATTRS
            pass 
            self.mTREE_TYPES_ITEM_ATTRS()



        elif alt5 == 15:
            # grammar/Frontend.g:1:184: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt5 == 16:
            # grammar/Frontend.g:1:191: MINUS
            pass 
            self.mMINUS()



        elif alt5 == 17:
            # grammar/Frontend.g:1:197: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt5 == 18:
            # grammar/Frontend.g:1:205: ID
            pass 
            self.mID()



        elif alt5 == 19:
            # grammar/Frontend.g:1:208: NUMBER
            pass 
            self.mNUMBER()



        elif alt5 == 20:
            # grammar/Frontend.g:1:215: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt5 == 21:
            # grammar/Frontend.g:1:226: EXPRESSION
            pass 
            self.mEXPRESSION()








    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\1\uffff\5\12\10\uffff\5\12\1\uffff\5\12\1\uffff\5\12\1\uffff\4"
        u"\12\1\52\1\uffff\1\60\1\61\1\62\1\63\22\uffff\1\76\5\uffff\1\104"
        u"\5\uffff\1\112\2\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\113\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\12\1\157\1\145\1\156\1\157\1\171\1\122\7\uffff\1\156\3\144\1"
        u"\160\1\105\1\163\2\145\1\165\1\145\1\105\1\164\2\156\1\154\1\163"
        u"\1\137\1\163\2\164\1\145\1\60\1\103\4\60\4\uffff\1\125\1\131\4"
        u"\uffff\1\115\1\120\1\137\1\105\1\106\1\123\2\uffff\1\137\1\111"
        u"\1\uffff\1\124\1\105\1\115\1\137\1\101\1\uffff\2\124\1\122\1\123"
        u"\2\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\172\1\157\1\145\1\156\1\157\1\171\1\122\7\uffff\1\156\3\144"
        u"\1\160\1\105\1\163\2\145\1\165\1\145\1\105\1\164\2\156\1\154\1"
        u"\163\1\137\1\163\2\164\1\145\1\172\1\124\4\172\4\uffff\1\125\1"
        u"\131\4\uffff\1\115\1\120\1\137\1\105\1\127\1\123\2\uffff\1\137"
        u"\1\111\1\uffff\1\124\1\105\1\115\1\137\1\101\1\uffff\2\124\1\122"
        u"\1\123\2\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\7\uffff\1\17\1\20\1\21\1\22\1\23\1\24\1\25\34\uffff\1\5\1\6\1"
        u"\7\1\10\2\uffff\1\1\1\2\1\3\1\4\6\uffff\1\11\1\12\2\uffff\1\13"
        u"\5\uffff\1\14\4\uffff\1\16\1\15"
        )

    DFA5_special = DFA.unpack(
        u"\113\uffff"
        )


    DFA5_transition = [
        DFA.unpack(u"\1\11\25\uffff\1\14\14\uffff\1\10\1\uffff\1\7\12\13"
        u"\32\uffff\1\6\6\uffff\1\15\5\uffff\2\12\1\1\1\2\4\12\1\3\3\12\1"
        u"\4\6\12\1\5\6\12"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\22"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\12\12\45\uffff\1\12\1\uffff\32\12"),
        DFA.unpack(u"\1\53\1\uffff\1\54\7\uffff\1\55\1\56\5\uffff\1\57"),
        DFA.unpack(u"\12\12\45\uffff\1\12\1\uffff\32\12"),
        DFA.unpack(u"\12\12\45\uffff\1\12\1\uffff\32\12"),
        DFA.unpack(u"\12\12\45\uffff\1\12\1\uffff\32\12"),
        DFA.unpack(u"\12\12\45\uffff\1\12\1\uffff\32\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72\20\uffff\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(FrontendLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
