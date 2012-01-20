# $ANTLR 3.4 grammar/ShyLexer.g 2012-01-20 17:40:59

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
ARROW_LEFT=4
ARROW_RIGHT=5
CONSTS=6
COPY=7
CURLY_CLOSE=8
CURLY_OPEN=9
DEDENT=10
DIVIDE=11
EXPRESSION=12
ID=13
INDENT=14
MINUS=15
MODULE=16
NEWLINE=17
NUMBER=18
PASTE=19
REPLACE=20
STATELESS=21
STRING=22
TREE_ARBITRARY_TOKEN=23
TREE_CONSTS=24
TREE_COPY=25
TREE_COPY_PASTE=26
TREE_EXPRESSION=27
TREE_HINT=28
TREE_HINT_NONE=29
TREE_MODULE=30
TREE_NUM_FRACT=31
TREE_NUM_WHOLE=32
TREE_PASTE=33
TREE_PASTE_REPLACE=34
TREE_PASTE_WITH=35
TREE_STATELESS=36
TREE_TYPES=37
TREE_TYPES_ITEM=38
TREE_TYPES_ITEM_ATTR=39
TREE_TYPES_ITEM_HINT=40
TREE_TYPES_ITEM_HINTS=41
TYPES=42
UNDERSCORE=43
WHITESPACE=44
WITH=45


class ShyLexer(Lexer):

    grammarFileName = "grammar/ShyLexer.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(ShyLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
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



    # $ANTLR start "STATELESS"
    def mSTATELESS(self, ):
        try:
            _type = STATELESS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:28:11: ( 'stateless' )
            # grammar/ShyLexer.g:28:13: 'stateless'
            pass 
            self.match("stateless")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STATELESS"



    # $ANTLR start "TYPES"
    def mTYPES(self, ):
        try:
            _type = TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:29:7: ( 'types' )
            # grammar/ShyLexer.g:29:9: 'types'
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

            # grammar/ShyLexer.g:30:6: ( 'with' )
            # grammar/ShyLexer.g:30:8: 'with'
            pass 
            self.match("with")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WITH"



    # $ANTLR start "ARROW_LEFT"
    def mARROW_LEFT(self, ):
        try:
            _type = ARROW_LEFT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:32:12: ( '<-' )
            # grammar/ShyLexer.g:32:14: '<-'
            pass 
            self.match("<-")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARROW_LEFT"



    # $ANTLR start "ARROW_RIGHT"
    def mARROW_RIGHT(self, ):
        try:
            _type = ARROW_RIGHT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:33:13: ( '->' )
            # grammar/ShyLexer.g:33:15: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARROW_RIGHT"



    # $ANTLR start "CURLY_OPEN"
    def mCURLY_OPEN(self, ):
        try:
            _type = CURLY_OPEN
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:34:12: ( '{' )
            # grammar/ShyLexer.g:34:14: '{'
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

            # grammar/ShyLexer.g:35:13: ( '}' )
            # grammar/ShyLexer.g:35:15: '}'
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

            # grammar/ShyLexer.g:36:8: ( '/' )
            # grammar/ShyLexer.g:36:10: '/'
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

            # grammar/ShyLexer.g:37:7: ( '-' )
            # grammar/ShyLexer.g:37:9: '-'
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

            # grammar/ShyLexer.g:38:12: ( '_' )
            # grammar/ShyLexer.g:38:14: '_'
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

            # grammar/ShyLexer.g:39:9: ( '\\n' )
            # grammar/ShyLexer.g:39:11: '\\n'
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

            # grammar/ShyLexer.g:40:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/ShyLexer.g:40:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/ShyLexer.g:40:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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

            # grammar/ShyLexer.g:41:8: ( ( '0' .. '9' )+ )
            # grammar/ShyLexer.g:41:10: ( '0' .. '9' )+
            pass 
            # grammar/ShyLexer.g:41:10: ( '0' .. '9' )+
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

            # grammar/ShyLexer.g:42:12: ( ( ' ' )+ )
            # grammar/ShyLexer.g:42:14: ( ' ' )+
            pass 
            # grammar/ShyLexer.g:42:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/ShyLexer.g:42:14: ' '
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

            # grammar/ShyLexer.g:43:12: ( '[' ( . )* ']' )
            # grammar/ShyLexer.g:43:14: '[' ( . )* ']'
            pass 
            self.match(91)

            # grammar/ShyLexer.g:43:18: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 93) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 92) or (94 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/ShyLexer.g:43:18: .
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



    # $ANTLR start "STRING"
    def mSTRING(self, ):
        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:44:8: ( '\\'' ( . )* '\\'' )
            # grammar/ShyLexer.g:44:10: '\\'' ( . )* '\\''
            pass 
            self.match(39)

            # grammar/ShyLexer.g:44:15: ( . )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 39) :
                    alt5 = 2
                elif ((0 <= LA5_0 <= 38) or (40 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # grammar/ShyLexer.g:44:15: .
                    pass 
                    self.matchAny()


                else:
                    break #loop5


            self.match(39)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STRING"



    # $ANTLR start "TREE_ARBITRARY_TOKEN"
    def mTREE_ARBITRARY_TOKEN(self, ):
        try:
            _type = TREE_ARBITRARY_TOKEN
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:46:22: ( 'TREE_ARBITRARY_TOKEN' )
            # grammar/ShyLexer.g:46:24: 'TREE_ARBITRARY_TOKEN'
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

            # grammar/ShyLexer.g:47:13: ( 'TREE_CONSTS' )
            # grammar/ShyLexer.g:47:15: 'TREE_CONSTS'
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

            # grammar/ShyLexer.g:48:11: ( 'TREE_COPY' )
            # grammar/ShyLexer.g:48:13: 'TREE_COPY'
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

            # grammar/ShyLexer.g:49:17: ( 'TREE_COPY_PASTE' )
            # grammar/ShyLexer.g:49:19: 'TREE_COPY_PASTE'
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

            # grammar/ShyLexer.g:50:17: ( 'TREE_EXPRESSION' )
            # grammar/ShyLexer.g:50:19: 'TREE_EXPRESSION'
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

            # grammar/ShyLexer.g:51:11: ( 'TREE_HINT' )
            # grammar/ShyLexer.g:51:13: 'TREE_HINT'
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

            # grammar/ShyLexer.g:52:16: ( 'TREE_HINT_NONE' )
            # grammar/ShyLexer.g:52:18: 'TREE_HINT_NONE'
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

            # grammar/ShyLexer.g:53:13: ( 'TREE_MODULE' )
            # grammar/ShyLexer.g:53:15: 'TREE_MODULE'
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

            # grammar/ShyLexer.g:54:16: ( 'TREE_NUM_FRACT' )
            # grammar/ShyLexer.g:54:18: 'TREE_NUM_FRACT'
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

            # grammar/ShyLexer.g:55:16: ( 'TREE_NUM_WHOLE' )
            # grammar/ShyLexer.g:55:18: 'TREE_NUM_WHOLE'
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

            # grammar/ShyLexer.g:56:12: ( 'TREE_PASTE' )
            # grammar/ShyLexer.g:56:14: 'TREE_PASTE'
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

            # grammar/ShyLexer.g:57:20: ( 'TREE_PASTE_REPLACE' )
            # grammar/ShyLexer.g:57:22: 'TREE_PASTE_REPLACE'
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

            # grammar/ShyLexer.g:58:17: ( 'TREE_PASTE_WITH' )
            # grammar/ShyLexer.g:58:19: 'TREE_PASTE_WITH'
            pass 
            self.match("TREE_PASTE_WITH")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PASTE_WITH"



    # $ANTLR start "TREE_STATELESS"
    def mTREE_STATELESS(self, ):
        try:
            _type = TREE_STATELESS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:59:16: ( 'TREE_STATELESS' )
            # grammar/ShyLexer.g:59:18: 'TREE_STATELESS'
            pass 
            self.match("TREE_STATELESS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATELESS"



    # $ANTLR start "TREE_TYPES"
    def mTREE_TYPES(self, ):
        try:
            _type = TREE_TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:60:12: ( 'TREE_TYPES' )
            # grammar/ShyLexer.g:60:14: 'TREE_TYPES'
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

            # grammar/ShyLexer.g:61:17: ( 'TREE_TYPES_ITEM' )
            # grammar/ShyLexer.g:61:19: 'TREE_TYPES_ITEM'
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

            # grammar/ShyLexer.g:62:22: ( 'TREE_TYPES_ITEM_ATTR' )
            # grammar/ShyLexer.g:62:24: 'TREE_TYPES_ITEM_ATTR'
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

            # grammar/ShyLexer.g:63:22: ( 'TREE_TYPES_ITEM_HINT' )
            # grammar/ShyLexer.g:63:24: 'TREE_TYPES_ITEM_HINT'
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

            # grammar/ShyLexer.g:64:23: ( 'TREE_TYPES_ITEM_HINTS' )
            # grammar/ShyLexer.g:64:25: 'TREE_TYPES_ITEM_HINTS'
            pass 
            self.match("TREE_TYPES_ITEM_HINTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM_HINTS"



    def mTokens(self):
        # grammar/ShyLexer.g:1:8: ( CONSTS | COPY | DEDENT | INDENT | MODULE | PASTE | REPLACE | STATELESS | TYPES | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | WHITESPACE | EXPRESSION | STRING | TREE_ARBITRARY_TOKEN | TREE_CONSTS | TREE_COPY | TREE_COPY_PASTE | TREE_EXPRESSION | TREE_HINT | TREE_HINT_NONE | TREE_MODULE | TREE_NUM_FRACT | TREE_NUM_WHOLE | TREE_PASTE | TREE_PASTE_REPLACE | TREE_PASTE_WITH | TREE_STATELESS | TREE_TYPES | TREE_TYPES_ITEM | TREE_TYPES_ITEM_ATTR | TREE_TYPES_ITEM_HINT | TREE_TYPES_ITEM_HINTS )
        alt6 = 42
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # grammar/ShyLexer.g:1:10: CONSTS
            pass 
            self.mCONSTS()



        elif alt6 == 2:
            # grammar/ShyLexer.g:1:17: COPY
            pass 
            self.mCOPY()



        elif alt6 == 3:
            # grammar/ShyLexer.g:1:22: DEDENT
            pass 
            self.mDEDENT()



        elif alt6 == 4:
            # grammar/ShyLexer.g:1:29: INDENT
            pass 
            self.mINDENT()



        elif alt6 == 5:
            # grammar/ShyLexer.g:1:36: MODULE
            pass 
            self.mMODULE()



        elif alt6 == 6:
            # grammar/ShyLexer.g:1:43: PASTE
            pass 
            self.mPASTE()



        elif alt6 == 7:
            # grammar/ShyLexer.g:1:49: REPLACE
            pass 
            self.mREPLACE()



        elif alt6 == 8:
            # grammar/ShyLexer.g:1:57: STATELESS
            pass 
            self.mSTATELESS()



        elif alt6 == 9:
            # grammar/ShyLexer.g:1:67: TYPES
            pass 
            self.mTYPES()



        elif alt6 == 10:
            # grammar/ShyLexer.g:1:73: WITH
            pass 
            self.mWITH()



        elif alt6 == 11:
            # grammar/ShyLexer.g:1:78: ARROW_LEFT
            pass 
            self.mARROW_LEFT()



        elif alt6 == 12:
            # grammar/ShyLexer.g:1:89: ARROW_RIGHT
            pass 
            self.mARROW_RIGHT()



        elif alt6 == 13:
            # grammar/ShyLexer.g:1:101: CURLY_OPEN
            pass 
            self.mCURLY_OPEN()



        elif alt6 == 14:
            # grammar/ShyLexer.g:1:112: CURLY_CLOSE
            pass 
            self.mCURLY_CLOSE()



        elif alt6 == 15:
            # grammar/ShyLexer.g:1:124: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt6 == 16:
            # grammar/ShyLexer.g:1:131: MINUS
            pass 
            self.mMINUS()



        elif alt6 == 17:
            # grammar/ShyLexer.g:1:137: UNDERSCORE
            pass 
            self.mUNDERSCORE()



        elif alt6 == 18:
            # grammar/ShyLexer.g:1:148: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt6 == 19:
            # grammar/ShyLexer.g:1:156: ID
            pass 
            self.mID()



        elif alt6 == 20:
            # grammar/ShyLexer.g:1:159: NUMBER
            pass 
            self.mNUMBER()



        elif alt6 == 21:
            # grammar/ShyLexer.g:1:166: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt6 == 22:
            # grammar/ShyLexer.g:1:177: EXPRESSION
            pass 
            self.mEXPRESSION()



        elif alt6 == 23:
            # grammar/ShyLexer.g:1:188: STRING
            pass 
            self.mSTRING()



        elif alt6 == 24:
            # grammar/ShyLexer.g:1:195: TREE_ARBITRARY_TOKEN
            pass 
            self.mTREE_ARBITRARY_TOKEN()



        elif alt6 == 25:
            # grammar/ShyLexer.g:1:216: TREE_CONSTS
            pass 
            self.mTREE_CONSTS()



        elif alt6 == 26:
            # grammar/ShyLexer.g:1:228: TREE_COPY
            pass 
            self.mTREE_COPY()



        elif alt6 == 27:
            # grammar/ShyLexer.g:1:238: TREE_COPY_PASTE
            pass 
            self.mTREE_COPY_PASTE()



        elif alt6 == 28:
            # grammar/ShyLexer.g:1:254: TREE_EXPRESSION
            pass 
            self.mTREE_EXPRESSION()



        elif alt6 == 29:
            # grammar/ShyLexer.g:1:270: TREE_HINT
            pass 
            self.mTREE_HINT()



        elif alt6 == 30:
            # grammar/ShyLexer.g:1:280: TREE_HINT_NONE
            pass 
            self.mTREE_HINT_NONE()



        elif alt6 == 31:
            # grammar/ShyLexer.g:1:295: TREE_MODULE
            pass 
            self.mTREE_MODULE()



        elif alt6 == 32:
            # grammar/ShyLexer.g:1:307: TREE_NUM_FRACT
            pass 
            self.mTREE_NUM_FRACT()



        elif alt6 == 33:
            # grammar/ShyLexer.g:1:322: TREE_NUM_WHOLE
            pass 
            self.mTREE_NUM_WHOLE()



        elif alt6 == 34:
            # grammar/ShyLexer.g:1:337: TREE_PASTE
            pass 
            self.mTREE_PASTE()



        elif alt6 == 35:
            # grammar/ShyLexer.g:1:348: TREE_PASTE_REPLACE
            pass 
            self.mTREE_PASTE_REPLACE()



        elif alt6 == 36:
            # grammar/ShyLexer.g:1:367: TREE_PASTE_WITH
            pass 
            self.mTREE_PASTE_WITH()



        elif alt6 == 37:
            # grammar/ShyLexer.g:1:383: TREE_STATELESS
            pass 
            self.mTREE_STATELESS()



        elif alt6 == 38:
            # grammar/ShyLexer.g:1:398: TREE_TYPES
            pass 
            self.mTREE_TYPES()



        elif alt6 == 39:
            # grammar/ShyLexer.g:1:409: TREE_TYPES_ITEM
            pass 
            self.mTREE_TYPES_ITEM()



        elif alt6 == 40:
            # grammar/ShyLexer.g:1:425: TREE_TYPES_ITEM_ATTR
            pass 
            self.mTREE_TYPES_ITEM_ATTR()



        elif alt6 == 41:
            # grammar/ShyLexer.g:1:446: TREE_TYPES_ITEM_HINT
            pass 
            self.mTREE_TYPES_ITEM_HINT()



        elif alt6 == 42:
            # grammar/ShyLexer.g:1:467: TREE_TYPES_ITEM_HINTS
            pass 
            self.mTREE_TYPES_ITEM_HINTS()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\uffff\11\21\1\uffff\1\41\13\uffff\11\21\3\uffff\12\21\1\uffff"
        u"\1\21\1\72\7\21\1\102\1\uffff\1\21\1\uffff\3\21\1\110\2\21\1\113"
        u"\2\uffff\1\125\1\126\1\127\1\130\1\uffff\2\21\16\uffff\1\140\1"
        u"\21\6\uffff\1\21\6\uffff\1\156\1\160\1\162\12\uffff\1\170\1\172"
        u"\11\uffff\1\u0082\6\uffff\1\u0089\2\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\u008a\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\12\1\157\1\145\1\156\1\157\1\141\1\145\1\164\1\171\1\151\1\uffff"
        u"\1\76\12\uffff\1\122\1\156\3\144\1\163\1\160\1\141\1\160\1\164"
        u"\2\uffff\1\105\1\163\1\171\2\145\1\165\1\164\1\154\1\164\1\145"
        u"\1\150\1\105\1\164\1\60\2\156\1\154\1\145\1\141\1\145\1\163\1\60"
        u"\1\137\1\163\1\uffff\2\164\1\145\1\60\1\143\1\154\1\60\1\uffff"
        u"\1\101\4\60\1\uffff\2\145\2\uffff\1\117\1\uffff\1\111\1\uffff\1"
        u"\125\1\101\1\uffff\1\131\4\uffff\1\60\1\163\2\116\1\115\1\123\1"
        u"\120\1\uffff\1\163\1\uffff\1\131\1\124\1\137\1\124\1\105\1\60\2"
        u"\137\1\106\1\105\1\123\7\uffff\2\137\1\122\1\uffff\1\111\3\uffff"
        u"\1\124\1\105\1\115\1\137\1\101\2\uffff\1\111\1\116\1\124\1\123"
        u"\2\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\175\1\157\1\145\1\156\1\157\1\141\1\145\1\164\1\171\1\151\1"
        u"\uffff\1\76\12\uffff\1\122\1\160\3\144\1\163\1\160\1\141\1\160"
        u"\1\164\2\uffff\1\105\1\163\1\171\2\145\1\165\1\164\1\154\1\164"
        u"\1\145\1\150\1\105\1\164\1\172\2\156\1\154\1\145\1\141\1\145\1"
        u"\163\1\172\1\137\1\163\1\uffff\2\164\1\145\1\172\1\143\1\154\1"
        u"\172\1\uffff\1\124\4\172\1\uffff\2\145\2\uffff\1\117\1\uffff\1"
        u"\111\1\uffff\1\125\1\101\1\uffff\1\131\4\uffff\1\172\1\163\1\120"
        u"\1\116\1\115\1\123\1\120\1\uffff\1\163\1\uffff\1\131\1\124\1\137"
        u"\1\124\1\105\1\172\2\137\1\127\1\105\1\123\7\uffff\2\137\1\127"
        u"\1\uffff\1\111\3\uffff\1\124\1\105\1\115\1\137\1\110\2\uffff\1"
        u"\111\1\116\1\124\1\123\2\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\12\uffff\1\13\1\uffff\1\15\1\16\1\17\1\21\1\22\1\23\1\24\1\25"
        u"\1\26\1\27\12\uffff\1\14\1\20\30\uffff\1\2\7\uffff\1\12\5\uffff"
        u"\1\6\2\uffff\1\11\1\30\1\uffff\1\34\1\uffff\1\37\2\uffff\1\45\1"
        u"\uffff\1\1\1\3\1\4\1\5\7\uffff\1\7\1\uffff\1\31\13\uffff\1\10\1"
        u"\33\1\32\1\36\1\35\1\40\1\41\3\uffff\1\42\1\uffff\1\46\1\43\1\44"
        u"\5\uffff\1\47\1\50\4\uffff\1\52\1\51"
        )

    DFA6_special = DFA.unpack(
        u"\u008a\uffff"
        )


    DFA6_transition = [
        DFA.unpack(u"\1\20\25\uffff\1\23\6\uffff\1\25\5\uffff\1\13\1\uffff"
        u"\1\16\12\22\2\uffff\1\12\27\uffff\1\26\6\uffff\1\24\3\uffff\1\17"
        u"\1\uffff\2\21\1\1\1\2\4\21\1\3\3\21\1\4\2\21\1\5\1\21\1\6\1\7\1"
        u"\10\2\21\1\11\3\21\1\14\1\uffff\1\15"),
        DFA.unpack(u"\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\40"),
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
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43\1\uffff\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\114\1\uffff\1\115\1\uffff\1\116\2\uffff\1\117\4"
        u"\uffff\1\120\1\121\1\uffff\1\122\2\uffff\1\123\1\124"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142\1\uffff\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\152"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\1\154"),
        DFA.unpack(u"\1\155"),
        DFA.unpack(u"\12\21\45\uffff\1\21\1\uffff\32\21"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\163\20\uffff\1\164"),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\173\4\uffff\1\174"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0083\6\uffff\1\u0084"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
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
