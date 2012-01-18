# $ANTLR 3.4 grammar/ShyLexer.g 2012-01-18 18:42:59

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


class ShyLexerException ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CONSTS=4
COPY=5
CURLY_CLOSE=6
CURLY_OPEN=7
DEDENT=8
DIVIDE=9
EXPRESSION=10
ID=11
INDENT=12
MINUS=13
MODULE=14
NEWLINE=15
NUMBER=16
PASTE=17
REPLACE=18
TREE_ARBITRARY_TOKEN=19
TREE_CONSTS=20
TREE_COPY=21
TREE_COPY_PASTE=22
TREE_EXPRESSION=23
TREE_HINT=24
TREE_HINT_NONE=25
TREE_MODULE=26
TREE_NUM_FRACT=27
TREE_NUM_WHOLE=28
TREE_PASTE=29
TREE_PASTE_REPLACE=30
TREE_PASTE_WITH=31
TREE_TYPES=32
TREE_TYPES_ITEM=33
TREE_TYPES_ITEM_ATTR=34
TREE_TYPES_ITEM_HINT=35
TREE_TYPES_ITEM_HINTS=36
TYPES=37
UNDERSCORE=38
WHITESPACE=39
WITH=40


class ShyLexer(Lexer):

    grammarFileName = "grammar/ShyLexer.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(ShyLexer, self).__init__(input, state)

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
        raise ShyLexerException ( msg )



    # $ANTLR start "CONSTS"
    def mCONSTS(self, ):
        try:
            _type = CONSTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:21:8: ( 'consts' )
            # grammar/ShyLexer.g:21:10: 'consts'
            pass 
            self.match("consts")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CONSTS"



    # $ANTLR start "COPY"
    def mCOPY(self, ):
        try:
            _type = COPY
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:22:6: ( 'copy' )
            # grammar/ShyLexer.g:22:8: 'copy'
            pass 
            self.match("copy")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COPY"



    # $ANTLR start "DEDENT"
    def mDEDENT(self, ):
        try:
            _type = DEDENT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:23:8: ( 'dedent' )
            # grammar/ShyLexer.g:23:10: 'dedent'
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

            # grammar/ShyLexer.g:24:8: ( 'indent' )
            # grammar/ShyLexer.g:24:10: 'indent'
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

            # grammar/ShyLexer.g:25:8: ( 'module' )
            # grammar/ShyLexer.g:25:10: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULE"



    # $ANTLR start "PASTE"
    def mPASTE(self, ):
        try:
            _type = PASTE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:26:7: ( 'paste' )
            # grammar/ShyLexer.g:26:9: 'paste'
            pass 
            self.match("paste")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PASTE"



    # $ANTLR start "REPLACE"
    def mREPLACE(self, ):
        try:
            _type = REPLACE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:27:9: ( 'replace' )
            # grammar/ShyLexer.g:27:11: 'replace'
            pass 
            self.match("replace")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REPLACE"



    # $ANTLR start "TYPES"
    def mTYPES(self, ):
        try:
            _type = TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:28:7: ( 'types' )
            # grammar/ShyLexer.g:28:9: 'types'
            pass 
            self.match("types")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPES"



    # $ANTLR start "WITH"
    def mWITH(self, ):
        try:
            _type = WITH
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:29:6: ( 'with' )
            # grammar/ShyLexer.g:29:8: 'with'
            pass 
            self.match("with")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WITH"



    # $ANTLR start "CURLY_OPEN"
    def mCURLY_OPEN(self, ):
        try:
            _type = CURLY_OPEN
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:31:12: ( '{' )
            # grammar/ShyLexer.g:31:14: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CURLY_OPEN"



    # $ANTLR start "CURLY_CLOSE"
    def mCURLY_CLOSE(self, ):
        try:
            _type = CURLY_CLOSE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:32:13: ( '}' )
            # grammar/ShyLexer.g:32:15: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CURLY_CLOSE"



    # $ANTLR start "DIVIDE"
    def mDIVIDE(self, ):
        try:
            _type = DIVIDE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:33:8: ( '/' )
            # grammar/ShyLexer.g:33:10: '/'
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

            # grammar/ShyLexer.g:34:7: ( '-' )
            # grammar/ShyLexer.g:34:9: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "UNDERSCORE"
    def mUNDERSCORE(self, ):
        try:
            _type = UNDERSCORE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:35:12: ( '_' )
            # grammar/ShyLexer.g:35:14: '_'
            pass 
            self.match(95)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "UNDERSCORE"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:36:9: ( '\\n' )
            # grammar/ShyLexer.g:36:11: '\\n'
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

            # grammar/ShyLexer.g:37:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/ShyLexer.g:37:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/ShyLexer.g:37:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((48 <= LA1_0 <= 57) or LA1_0 == 95 or (97 <= LA1_0 <= 122)) :
                    alt1 = 1


                if alt1 == 1:
                    # grammar/ShyLexer.g:
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

            # grammar/ShyLexer.g:38:8: ( ( '0' .. '9' )+ )
            # grammar/ShyLexer.g:38:10: ( '0' .. '9' )+
            pass 
            # grammar/ShyLexer.g:38:10: ( '0' .. '9' )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((48 <= LA2_0 <= 57)) :
                    alt2 = 1


                if alt2 == 1:
                    # grammar/ShyLexer.g:
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

            # grammar/ShyLexer.g:39:12: ( ( ' ' )+ )
            # grammar/ShyLexer.g:39:14: ( ' ' )+
            pass 
            # grammar/ShyLexer.g:39:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/ShyLexer.g:39:14: ' '
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

            # grammar/ShyLexer.g:40:12: ( '[' ( . )* ']' )
            # grammar/ShyLexer.g:40:14: '[' ( . )* ']'
            pass 
            self.match(91)

            # grammar/ShyLexer.g:40:18: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 93) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 92) or (94 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/ShyLexer.g:40:18: .
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



    # $ANTLR start "TREE_ARBITRARY_TOKEN"
    def mTREE_ARBITRARY_TOKEN(self, ):
        try:
            _type = TREE_ARBITRARY_TOKEN
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:42:22: ( 'TREE_ARBITRARY_TOKEN' )
            # grammar/ShyLexer.g:42:24: 'TREE_ARBITRARY_TOKEN'
            pass 
            self.match("TREE_ARBITRARY_TOKEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_ARBITRARY_TOKEN"



    # $ANTLR start "TREE_CONSTS"
    def mTREE_CONSTS(self, ):
        try:
            _type = TREE_CONSTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:43:13: ( 'TREE_CONSTS' )
            # grammar/ShyLexer.g:43:15: 'TREE_CONSTS'
            pass 
            self.match("TREE_CONSTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_CONSTS"



    # $ANTLR start "TREE_COPY"
    def mTREE_COPY(self, ):
        try:
            _type = TREE_COPY
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:44:11: ( 'TREE_COPY' )
            # grammar/ShyLexer.g:44:13: 'TREE_COPY'
            pass 
            self.match("TREE_COPY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_COPY"



    # $ANTLR start "TREE_COPY_PASTE"
    def mTREE_COPY_PASTE(self, ):
        try:
            _type = TREE_COPY_PASTE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:45:17: ( 'TREE_COPY_PASTE' )
            # grammar/ShyLexer.g:45:19: 'TREE_COPY_PASTE'
            pass 
            self.match("TREE_COPY_PASTE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_COPY_PASTE"



    # $ANTLR start "TREE_EXPRESSION"
    def mTREE_EXPRESSION(self, ):
        try:
            _type = TREE_EXPRESSION
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:46:17: ( 'TREE_EXPRESSION' )
            # grammar/ShyLexer.g:46:19: 'TREE_EXPRESSION'
            pass 
            self.match("TREE_EXPRESSION")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_EXPRESSION"



    # $ANTLR start "TREE_HINT"
    def mTREE_HINT(self, ):
        try:
            _type = TREE_HINT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:47:11: ( 'TREE_HINT' )
            # grammar/ShyLexer.g:47:13: 'TREE_HINT'
            pass 
            self.match("TREE_HINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_HINT"



    # $ANTLR start "TREE_HINT_NONE"
    def mTREE_HINT_NONE(self, ):
        try:
            _type = TREE_HINT_NONE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:48:16: ( 'TREE_HINT_NONE' )
            # grammar/ShyLexer.g:48:18: 'TREE_HINT_NONE'
            pass 
            self.match("TREE_HINT_NONE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_HINT_NONE"



    # $ANTLR start "TREE_MODULE"
    def mTREE_MODULE(self, ):
        try:
            _type = TREE_MODULE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:49:13: ( 'TREE_MODULE' )
            # grammar/ShyLexer.g:49:15: 'TREE_MODULE'
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

            # grammar/ShyLexer.g:50:16: ( 'TREE_NUM_FRACT' )
            # grammar/ShyLexer.g:50:18: 'TREE_NUM_FRACT'
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

            # grammar/ShyLexer.g:51:16: ( 'TREE_NUM_WHOLE' )
            # grammar/ShyLexer.g:51:18: 'TREE_NUM_WHOLE'
            pass 
            self.match("TREE_NUM_WHOLE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_NUM_WHOLE"



    # $ANTLR start "TREE_PASTE"
    def mTREE_PASTE(self, ):
        try:
            _type = TREE_PASTE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:52:12: ( 'TREE_PASTE' )
            # grammar/ShyLexer.g:52:14: 'TREE_PASTE'
            pass 
            self.match("TREE_PASTE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PASTE"



    # $ANTLR start "TREE_PASTE_REPLACE"
    def mTREE_PASTE_REPLACE(self, ):
        try:
            _type = TREE_PASTE_REPLACE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:53:20: ( 'TREE_PASTE_REPLACE' )
            # grammar/ShyLexer.g:53:22: 'TREE_PASTE_REPLACE'
            pass 
            self.match("TREE_PASTE_REPLACE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PASTE_REPLACE"



    # $ANTLR start "TREE_PASTE_WITH"
    def mTREE_PASTE_WITH(self, ):
        try:
            _type = TREE_PASTE_WITH
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:54:17: ( 'TREE_PASTE_WITH' )
            # grammar/ShyLexer.g:54:19: 'TREE_PASTE_WITH'
            pass 
            self.match("TREE_PASTE_WITH")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PASTE_WITH"



    # $ANTLR start "TREE_TYPES"
    def mTREE_TYPES(self, ):
        try:
            _type = TREE_TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:55:12: ( 'TREE_TYPES' )
            # grammar/ShyLexer.g:55:14: 'TREE_TYPES'
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

            # grammar/ShyLexer.g:56:17: ( 'TREE_TYPES_ITEM' )
            # grammar/ShyLexer.g:56:19: 'TREE_TYPES_ITEM'
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

            # grammar/ShyLexer.g:57:22: ( 'TREE_TYPES_ITEM_ATTR' )
            # grammar/ShyLexer.g:57:24: 'TREE_TYPES_ITEM_ATTR'
            pass 
            self.match("TREE_TYPES_ITEM_ATTR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM_ATTR"



    # $ANTLR start "TREE_TYPES_ITEM_HINT"
    def mTREE_TYPES_ITEM_HINT(self, ):
        try:
            _type = TREE_TYPES_ITEM_HINT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:58:22: ( 'TREE_TYPES_ITEM_HINT' )
            # grammar/ShyLexer.g:58:24: 'TREE_TYPES_ITEM_HINT'
            pass 
            self.match("TREE_TYPES_ITEM_HINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM_HINT"



    # $ANTLR start "TREE_TYPES_ITEM_HINTS"
    def mTREE_TYPES_ITEM_HINTS(self, ):
        try:
            _type = TREE_TYPES_ITEM_HINTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:59:23: ( 'TREE_TYPES_ITEM_HINTS' )
            # grammar/ShyLexer.g:59:25: 'TREE_TYPES_ITEM_HINTS'
            pass 
            self.match("TREE_TYPES_ITEM_HINTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM_HINTS"



    def mTokens(self):
        # grammar/ShyLexer.g:1:8: ( CONSTS | COPY | DEDENT | INDENT | MODULE | PASTE | REPLACE | TYPES | WITH | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | WHITESPACE | EXPRESSION | TREE_ARBITRARY_TOKEN | TREE_CONSTS | TREE_COPY | TREE_COPY_PASTE | TREE_EXPRESSION | TREE_HINT | TREE_HINT_NONE | TREE_MODULE | TREE_NUM_FRACT | TREE_NUM_WHOLE | TREE_PASTE | TREE_PASTE_REPLACE | TREE_PASTE_WITH | TREE_TYPES | TREE_TYPES_ITEM | TREE_TYPES_ITEM_ATTR | TREE_TYPES_ITEM_HINT | TREE_TYPES_ITEM_HINTS )
        alt5 = 37
        alt5 = self.dfa5.predict(self.input)
        if alt5 == 1:
            # grammar/ShyLexer.g:1:10: CONSTS
            pass 
            self.mCONSTS()



        elif alt5 == 2:
            # grammar/ShyLexer.g:1:17: COPY
            pass 
            self.mCOPY()



        elif alt5 == 3:
            # grammar/ShyLexer.g:1:22: DEDENT
            pass 
            self.mDEDENT()



        elif alt5 == 4:
            # grammar/ShyLexer.g:1:29: INDENT
            pass 
            self.mINDENT()



        elif alt5 == 5:
            # grammar/ShyLexer.g:1:36: MODULE
            pass 
            self.mMODULE()



        elif alt5 == 6:
            # grammar/ShyLexer.g:1:43: PASTE
            pass 
            self.mPASTE()



        elif alt5 == 7:
            # grammar/ShyLexer.g:1:49: REPLACE
            pass 
            self.mREPLACE()



        elif alt5 == 8:
            # grammar/ShyLexer.g:1:57: TYPES
            pass 
            self.mTYPES()



        elif alt5 == 9:
            # grammar/ShyLexer.g:1:63: WITH
            pass 
            self.mWITH()



        elif alt5 == 10:
            # grammar/ShyLexer.g:1:68: CURLY_OPEN
            pass 
            self.mCURLY_OPEN()



        elif alt5 == 11:
            # grammar/ShyLexer.g:1:79: CURLY_CLOSE
            pass 
            self.mCURLY_CLOSE()



        elif alt5 == 12:
            # grammar/ShyLexer.g:1:91: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt5 == 13:
            # grammar/ShyLexer.g:1:98: MINUS
            pass 
            self.mMINUS()



        elif alt5 == 14:
            # grammar/ShyLexer.g:1:104: UNDERSCORE
            pass 
            self.mUNDERSCORE()



        elif alt5 == 15:
            # grammar/ShyLexer.g:1:115: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt5 == 16:
            # grammar/ShyLexer.g:1:123: ID
            pass 
            self.mID()



        elif alt5 == 17:
            # grammar/ShyLexer.g:1:126: NUMBER
            pass 
            self.mNUMBER()



        elif alt5 == 18:
            # grammar/ShyLexer.g:1:133: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt5 == 19:
            # grammar/ShyLexer.g:1:144: EXPRESSION
            pass 
            self.mEXPRESSION()



        elif alt5 == 20:
            # grammar/ShyLexer.g:1:155: TREE_ARBITRARY_TOKEN
            pass 
            self.mTREE_ARBITRARY_TOKEN()



        elif alt5 == 21:
            # grammar/ShyLexer.g:1:176: TREE_CONSTS
            pass 
            self.mTREE_CONSTS()



        elif alt5 == 22:
            # grammar/ShyLexer.g:1:188: TREE_COPY
            pass 
            self.mTREE_COPY()



        elif alt5 == 23:
            # grammar/ShyLexer.g:1:198: TREE_COPY_PASTE
            pass 
            self.mTREE_COPY_PASTE()



        elif alt5 == 24:
            # grammar/ShyLexer.g:1:214: TREE_EXPRESSION
            pass 
            self.mTREE_EXPRESSION()



        elif alt5 == 25:
            # grammar/ShyLexer.g:1:230: TREE_HINT
            pass 
            self.mTREE_HINT()



        elif alt5 == 26:
            # grammar/ShyLexer.g:1:240: TREE_HINT_NONE
            pass 
            self.mTREE_HINT_NONE()



        elif alt5 == 27:
            # grammar/ShyLexer.g:1:255: TREE_MODULE
            pass 
            self.mTREE_MODULE()



        elif alt5 == 28:
            # grammar/ShyLexer.g:1:267: TREE_NUM_FRACT
            pass 
            self.mTREE_NUM_FRACT()



        elif alt5 == 29:
            # grammar/ShyLexer.g:1:282: TREE_NUM_WHOLE
            pass 
            self.mTREE_NUM_WHOLE()



        elif alt5 == 30:
            # grammar/ShyLexer.g:1:297: TREE_PASTE
            pass 
            self.mTREE_PASTE()



        elif alt5 == 31:
            # grammar/ShyLexer.g:1:308: TREE_PASTE_REPLACE
            pass 
            self.mTREE_PASTE_REPLACE()



        elif alt5 == 32:
            # grammar/ShyLexer.g:1:327: TREE_PASTE_WITH
            pass 
            self.mTREE_PASTE_WITH()



        elif alt5 == 33:
            # grammar/ShyLexer.g:1:343: TREE_TYPES
            pass 
            self.mTREE_TYPES()



        elif alt5 == 34:
            # grammar/ShyLexer.g:1:354: TREE_TYPES_ITEM
            pass 
            self.mTREE_TYPES_ITEM()



        elif alt5 == 35:
            # grammar/ShyLexer.g:1:370: TREE_TYPES_ITEM_ATTR
            pass 
            self.mTREE_TYPES_ITEM_ATTR()



        elif alt5 == 36:
            # grammar/ShyLexer.g:1:391: TREE_TYPES_ITEM_HINT
            pass 
            self.mTREE_TYPES_ITEM_HINT()



        elif alt5 == 37:
            # grammar/ShyLexer.g:1:412: TREE_TYPES_ITEM_HINTS
            pass 
            self.mTREE_TYPES_ITEM_HINTS()








    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\1\uffff\10\17\13\uffff\10\17\1\uffff\11\17\1\uffff\1\17\1\62\6"
        u"\17\1\71\1\uffff\1\17\1\uffff\3\17\1\77\1\17\1\101\2\uffff\1\112"
        u"\1\113\1\114\1\115\1\uffff\1\17\15\uffff\1\124\14\uffff\1\141\1"
        u"\143\11\uffff\1\151\1\153\11\uffff\1\163\6\uffff\1\172\2\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\173\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\1\12\1\157\1\145\1\156\1\157\1\141\1\145\1\171\1\151\12\uffff"
        u"\1\122\1\156\3\144\1\163\2\160\1\164\1\105\1\163\1\171\2\145\1"
        u"\165\1\164\1\154\1\145\1\150\1\105\1\164\1\60\2\156\1\154\1\145"
        u"\1\141\1\163\1\60\1\137\1\163\1\uffff\2\164\1\145\1\60\1\143\1"
        u"\60\1\uffff\1\101\4\60\1\uffff\1\145\2\uffff\1\117\1\uffff\1\111"
        u"\1\uffff\1\125\1\101\1\131\4\uffff\1\60\2\116\1\115\1\123\1\120"
        u"\2\uffff\1\131\1\124\1\137\1\124\1\105\2\137\1\106\1\105\1\123"
        u"\6\uffff\2\137\1\122\1\uffff\1\111\3\uffff\1\124\1\105\1\115\1"
        u"\137\1\101\2\uffff\1\111\1\116\1\124\1\123\2\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\1\175\1\157\1\145\1\156\1\157\1\141\1\145\1\171\1\151\12\uffff"
        u"\1\122\1\160\3\144\1\163\2\160\1\164\1\105\1\163\1\171\2\145\1"
        u"\165\1\164\1\154\1\145\1\150\1\105\1\164\1\172\2\156\1\154\1\145"
        u"\1\141\1\163\1\172\1\137\1\163\1\uffff\2\164\1\145\1\172\1\143"
        u"\1\172\1\uffff\1\124\4\172\1\uffff\1\145\2\uffff\1\117\1\uffff"
        u"\1\111\1\uffff\1\125\1\101\1\131\4\uffff\1\172\1\120\1\116\1\115"
        u"\1\123\1\120\2\uffff\1\131\1\124\1\137\1\124\1\105\2\137\1\127"
        u"\1\105\1\123\6\uffff\2\137\1\127\1\uffff\1\111\3\uffff\1\124\1"
        u"\105\1\115\1\137\1\110\2\uffff\1\111\1\116\1\124\1\123\2\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\11\uffff\1\12\1\13\1\14\1\15\1\16\1\17\1\20\1\21\1\22\1\23\37"
        u"\uffff\1\2\6\uffff\1\11\5\uffff\1\6\1\uffff\1\10\1\24\1\uffff\1"
        u"\30\1\uffff\1\33\3\uffff\1\1\1\3\1\4\1\5\6\uffff\1\7\1\25\12\uffff"
        u"\1\27\1\26\1\32\1\31\1\34\1\35\3\uffff\1\36\1\uffff\1\41\1\37\1"
        u"\40\5\uffff\1\42\1\43\4\uffff\1\45\1\44"
        )

    DFA5_special = DFA.unpack(
        u"\173\uffff"
        )


    DFA5_transition = [
        DFA.unpack(u"\1\16\25\uffff\1\21\14\uffff\1\14\1\uffff\1\13\12\20"
        u"\32\uffff\1\23\6\uffff\1\22\3\uffff\1\15\1\uffff\2\17\1\1\1\2\4"
        u"\17\1\3\3\17\1\4\2\17\1\5\1\17\1\6\1\17\1\7\2\17\1\10\3\17\1\11"
        u"\1\uffff\1\12"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35\1\uffff\1\36"),
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
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\102\1\uffff\1\103\1\uffff\1\104\2\uffff\1\105\4"
        u"\uffff\1\106\1\107\1\uffff\1\110\3\uffff\1\111"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\17\45\uffff\1\17\1\uffff\32\17"),
        DFA.unpack(u"\1\125\1\uffff\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\144\20\uffff\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\154\4\uffff\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u"\1\164\6\uffff\1\165"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(ShyLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
