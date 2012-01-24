# $ANTLR 3.4 grammar/ShyLexer.g 2012-01-24 14:40:57

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
ARGS=4
ARROW_LEFT=5
ARROW_RIGHT=6
CONSTS=7
COPY=8
CURLY_CLOSE=9
CURLY_OPEN=10
DEDENT=11
DIVIDE=12
DO=13
EXPRESSION=14
ID=15
IF=16
INDENT=17
MINUS=18
MODULE=19
NEWLINE=20
NUMBER=21
OPS=22
PASTE=23
PROC=24
REPLACE=25
STATELESS=26
STRING=27
TREE_ARBITRARY_TOKEN=28
TREE_CONSTS=29
TREE_COPY=30
TREE_COPY_PASTE=31
TREE_EXPRESSION=32
TREE_HINT=33
TREE_HINT_NONE=34
TREE_MODULE=35
TREE_NUM_FRACT=36
TREE_NUM_WHOLE=37
TREE_PASTE=38
TREE_PASTE_REPLACE=39
TREE_PASTE_WITH=40
TREE_PROC=41
TREE_PROC_ARGS=42
TREE_PROC_OPS=43
TREE_PROC_VARS=44
TREE_STATELESS=45
TREE_STATEMENT_CALL=46
TREE_STATEMENT_CALL_ARGS=47
TREE_TYPES=48
TREE_TYPES_ITEM=49
TREE_VAR=50
TREE_VARS_HINT=51
TREE_VAR_HINT=52
TYPES=53
UNDERSCORE=54
VARS=55
WHITESPACE=56
WITH=57


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



    # $ANTLR start "ARGS"
    def mARGS(self, ):
        try:
            _type = ARGS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:21:6: ( 'args' )
            # grammar/ShyLexer.g:21:8: 'args'
            pass 
            self.match("args")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARGS"



    # $ANTLR start "CONSTS"
    def mCONSTS(self, ):
        try:
            _type = CONSTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:22:8: ( 'consts' )
            # grammar/ShyLexer.g:22:10: 'consts'
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

            # grammar/ShyLexer.g:23:6: ( 'copy' )
            # grammar/ShyLexer.g:23:8: 'copy'
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

            # grammar/ShyLexer.g:24:8: ( 'dedent' )
            # grammar/ShyLexer.g:24:10: 'dedent'
            pass 
            self.match("dedent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEDENT"



    # $ANTLR start "DO"
    def mDO(self, ):
        try:
            _type = DO
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:25:4: ( 'do' )
            # grammar/ShyLexer.g:25:6: 'do'
            pass 
            self.match("do")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DO"



    # $ANTLR start "IF"
    def mIF(self, ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:26:4: ( 'if' )
            # grammar/ShyLexer.g:26:6: 'if'
            pass 
            self.match("if")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IF"



    # $ANTLR start "INDENT"
    def mINDENT(self, ):
        try:
            _type = INDENT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:27:8: ( 'indent' )
            # grammar/ShyLexer.g:27:10: 'indent'
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

            # grammar/ShyLexer.g:28:8: ( 'module' )
            # grammar/ShyLexer.g:28:10: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULE"



    # $ANTLR start "OPS"
    def mOPS(self, ):
        try:
            _type = OPS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:29:5: ( 'ops' )
            # grammar/ShyLexer.g:29:7: 'ops'
            pass 
            self.match("ops")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OPS"



    # $ANTLR start "PASTE"
    def mPASTE(self, ):
        try:
            _type = PASTE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:30:7: ( 'paste' )
            # grammar/ShyLexer.g:30:9: 'paste'
            pass 
            self.match("paste")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PASTE"



    # $ANTLR start "PROC"
    def mPROC(self, ):
        try:
            _type = PROC
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:31:6: ( 'proc' )
            # grammar/ShyLexer.g:31:8: 'proc'
            pass 
            self.match("proc")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROC"



    # $ANTLR start "REPLACE"
    def mREPLACE(self, ):
        try:
            _type = REPLACE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:32:9: ( 'replace' )
            # grammar/ShyLexer.g:32:11: 'replace'
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

            # grammar/ShyLexer.g:33:11: ( 'stateless' )
            # grammar/ShyLexer.g:33:13: 'stateless'
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

            # grammar/ShyLexer.g:34:7: ( 'types' )
            # grammar/ShyLexer.g:34:9: 'types'
            pass 
            self.match("types")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPES"



    # $ANTLR start "VARS"
    def mVARS(self, ):
        try:
            _type = VARS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:35:6: ( 'vars' )
            # grammar/ShyLexer.g:35:8: 'vars'
            pass 
            self.match("vars")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VARS"



    # $ANTLR start "WITH"
    def mWITH(self, ):
        try:
            _type = WITH
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:36:6: ( 'with' )
            # grammar/ShyLexer.g:36:8: 'with'
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

            # grammar/ShyLexer.g:38:12: ( '<-' )
            # grammar/ShyLexer.g:38:14: '<-'
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

            # grammar/ShyLexer.g:39:13: ( '->' )
            # grammar/ShyLexer.g:39:15: '->'
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

            # grammar/ShyLexer.g:40:12: ( '{' )
            # grammar/ShyLexer.g:40:14: '{'
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

            # grammar/ShyLexer.g:41:13: ( '}' )
            # grammar/ShyLexer.g:41:15: '}'
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

            # grammar/ShyLexer.g:42:8: ( '/' )
            # grammar/ShyLexer.g:42:10: '/'
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

            # grammar/ShyLexer.g:43:7: ( '-' )
            # grammar/ShyLexer.g:43:9: '-'
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

            # grammar/ShyLexer.g:44:12: ( '_' )
            # grammar/ShyLexer.g:44:14: '_'
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

            # grammar/ShyLexer.g:45:9: ( '\\n' )
            # grammar/ShyLexer.g:45:11: '\\n'
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

            # grammar/ShyLexer.g:46:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/ShyLexer.g:46:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/ShyLexer.g:46:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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

            # grammar/ShyLexer.g:47:8: ( ( '0' .. '9' )+ )
            # grammar/ShyLexer.g:47:10: ( '0' .. '9' )+
            pass 
            # grammar/ShyLexer.g:47:10: ( '0' .. '9' )+
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

            # grammar/ShyLexer.g:48:12: ( ( ' ' )+ )
            # grammar/ShyLexer.g:48:14: ( ' ' )+
            pass 
            # grammar/ShyLexer.g:48:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/ShyLexer.g:48:14: ' '
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

            # grammar/ShyLexer.g:49:12: ( '[' ( . )* ']' )
            # grammar/ShyLexer.g:49:14: '[' ( . )* ']'
            pass 
            self.match(91)

            # grammar/ShyLexer.g:49:18: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 93) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 92) or (94 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/ShyLexer.g:49:18: .
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

            # grammar/ShyLexer.g:50:8: ( '\\'' ( . )* '\\'' )
            # grammar/ShyLexer.g:50:10: '\\'' ( . )* '\\''
            pass 
            self.match(39)

            # grammar/ShyLexer.g:50:15: ( . )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 39) :
                    alt5 = 2
                elif ((0 <= LA5_0 <= 38) or (40 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # grammar/ShyLexer.g:50:15: .
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

            # grammar/ShyLexer.g:52:22: ( 'TREE_ARBITRARY_TOKEN' )
            # grammar/ShyLexer.g:52:24: 'TREE_ARBITRARY_TOKEN'
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

            # grammar/ShyLexer.g:53:13: ( 'TREE_CONSTS' )
            # grammar/ShyLexer.g:53:15: 'TREE_CONSTS'
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

            # grammar/ShyLexer.g:54:11: ( 'TREE_COPY' )
            # grammar/ShyLexer.g:54:13: 'TREE_COPY'
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

            # grammar/ShyLexer.g:55:17: ( 'TREE_COPY_PASTE' )
            # grammar/ShyLexer.g:55:19: 'TREE_COPY_PASTE'
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

            # grammar/ShyLexer.g:56:17: ( 'TREE_EXPRESSION' )
            # grammar/ShyLexer.g:56:19: 'TREE_EXPRESSION'
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

            # grammar/ShyLexer.g:57:11: ( 'TREE_HINT' )
            # grammar/ShyLexer.g:57:13: 'TREE_HINT'
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

            # grammar/ShyLexer.g:58:16: ( 'TREE_HINT_NONE' )
            # grammar/ShyLexer.g:58:18: 'TREE_HINT_NONE'
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

            # grammar/ShyLexer.g:59:13: ( 'TREE_MODULE' )
            # grammar/ShyLexer.g:59:15: 'TREE_MODULE'
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

            # grammar/ShyLexer.g:60:16: ( 'TREE_NUM_FRACT' )
            # grammar/ShyLexer.g:60:18: 'TREE_NUM_FRACT'
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

            # grammar/ShyLexer.g:61:16: ( 'TREE_NUM_WHOLE' )
            # grammar/ShyLexer.g:61:18: 'TREE_NUM_WHOLE'
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

            # grammar/ShyLexer.g:62:12: ( 'TREE_PASTE' )
            # grammar/ShyLexer.g:62:14: 'TREE_PASTE'
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

            # grammar/ShyLexer.g:63:20: ( 'TREE_PASTE_REPLACE' )
            # grammar/ShyLexer.g:63:22: 'TREE_PASTE_REPLACE'
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

            # grammar/ShyLexer.g:64:17: ( 'TREE_PASTE_WITH' )
            # grammar/ShyLexer.g:64:19: 'TREE_PASTE_WITH'
            pass 
            self.match("TREE_PASTE_WITH")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PASTE_WITH"



    # $ANTLR start "TREE_PROC"
    def mTREE_PROC(self, ):
        try:
            _type = TREE_PROC
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:65:11: ( 'TREE_PROC' )
            # grammar/ShyLexer.g:65:13: 'TREE_PROC'
            pass 
            self.match("TREE_PROC")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PROC"



    # $ANTLR start "TREE_PROC_ARGS"
    def mTREE_PROC_ARGS(self, ):
        try:
            _type = TREE_PROC_ARGS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:66:16: ( 'TREE_PROC_ARGS' )
            # grammar/ShyLexer.g:66:18: 'TREE_PROC_ARGS'
            pass 
            self.match("TREE_PROC_ARGS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PROC_ARGS"



    # $ANTLR start "TREE_PROC_OPS"
    def mTREE_PROC_OPS(self, ):
        try:
            _type = TREE_PROC_OPS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:67:15: ( 'TREE_PROC_OPS' )
            # grammar/ShyLexer.g:67:17: 'TREE_PROC_OPS'
            pass 
            self.match("TREE_PROC_OPS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PROC_OPS"



    # $ANTLR start "TREE_PROC_VARS"
    def mTREE_PROC_VARS(self, ):
        try:
            _type = TREE_PROC_VARS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:68:16: ( 'TREE_PROC_VARS' )
            # grammar/ShyLexer.g:68:18: 'TREE_PROC_VARS'
            pass 
            self.match("TREE_PROC_VARS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PROC_VARS"



    # $ANTLR start "TREE_STATELESS"
    def mTREE_STATELESS(self, ):
        try:
            _type = TREE_STATELESS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:69:16: ( 'TREE_STATELESS' )
            # grammar/ShyLexer.g:69:18: 'TREE_STATELESS'
            pass 
            self.match("TREE_STATELESS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATELESS"



    # $ANTLR start "TREE_STATEMENT_CALL"
    def mTREE_STATEMENT_CALL(self, ):
        try:
            _type = TREE_STATEMENT_CALL
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:70:21: ( 'TREE_STATEMENT_CALL' )
            # grammar/ShyLexer.g:70:23: 'TREE_STATEMENT_CALL'
            pass 
            self.match("TREE_STATEMENT_CALL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_CALL"



    # $ANTLR start "TREE_STATEMENT_CALL_ARGS"
    def mTREE_STATEMENT_CALL_ARGS(self, ):
        try:
            _type = TREE_STATEMENT_CALL_ARGS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:71:26: ( 'TREE_STATEMENT_CALL_ARGS' )
            # grammar/ShyLexer.g:71:28: 'TREE_STATEMENT_CALL_ARGS'
            pass 
            self.match("TREE_STATEMENT_CALL_ARGS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_CALL_ARGS"



    # $ANTLR start "TREE_TYPES"
    def mTREE_TYPES(self, ):
        try:
            _type = TREE_TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:72:12: ( 'TREE_TYPES' )
            # grammar/ShyLexer.g:72:14: 'TREE_TYPES'
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

            # grammar/ShyLexer.g:73:17: ( 'TREE_TYPES_ITEM' )
            # grammar/ShyLexer.g:73:19: 'TREE_TYPES_ITEM'
            pass 
            self.match("TREE_TYPES_ITEM")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM"



    # $ANTLR start "TREE_VAR"
    def mTREE_VAR(self, ):
        try:
            _type = TREE_VAR
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:74:10: ( 'TREE_VAR' )
            # grammar/ShyLexer.g:74:12: 'TREE_VAR'
            pass 
            self.match("TREE_VAR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_VAR"



    # $ANTLR start "TREE_VAR_HINT"
    def mTREE_VAR_HINT(self, ):
        try:
            _type = TREE_VAR_HINT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:75:15: ( 'TREE_VAR_HINT' )
            # grammar/ShyLexer.g:75:17: 'TREE_VAR_HINT'
            pass 
            self.match("TREE_VAR_HINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_VAR_HINT"



    # $ANTLR start "TREE_VARS_HINT"
    def mTREE_VARS_HINT(self, ):
        try:
            _type = TREE_VARS_HINT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:76:16: ( 'TREE_VARS_HINT' )
            # grammar/ShyLexer.g:76:18: 'TREE_VARS_HINT'
            pass 
            self.match("TREE_VARS_HINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_VARS_HINT"



    def mTokens(self):
        # grammar/ShyLexer.g:1:8: ( ARGS | CONSTS | COPY | DEDENT | DO | IF | INDENT | MODULE | OPS | PASTE | PROC | REPLACE | STATELESS | TYPES | VARS | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | WHITESPACE | EXPRESSION | STRING | TREE_ARBITRARY_TOKEN | TREE_CONSTS | TREE_COPY | TREE_COPY_PASTE | TREE_EXPRESSION | TREE_HINT | TREE_HINT_NONE | TREE_MODULE | TREE_NUM_FRACT | TREE_NUM_WHOLE | TREE_PASTE | TREE_PASTE_REPLACE | TREE_PASTE_WITH | TREE_PROC | TREE_PROC_ARGS | TREE_PROC_OPS | TREE_PROC_VARS | TREE_STATELESS | TREE_STATEMENT_CALL | TREE_STATEMENT_CALL_ARGS | TREE_TYPES | TREE_TYPES_ITEM | TREE_VAR | TREE_VAR_HINT | TREE_VARS_HINT )
        alt6 = 54
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # grammar/ShyLexer.g:1:10: ARGS
            pass 
            self.mARGS()



        elif alt6 == 2:
            # grammar/ShyLexer.g:1:15: CONSTS
            pass 
            self.mCONSTS()



        elif alt6 == 3:
            # grammar/ShyLexer.g:1:22: COPY
            pass 
            self.mCOPY()



        elif alt6 == 4:
            # grammar/ShyLexer.g:1:27: DEDENT
            pass 
            self.mDEDENT()



        elif alt6 == 5:
            # grammar/ShyLexer.g:1:34: DO
            pass 
            self.mDO()



        elif alt6 == 6:
            # grammar/ShyLexer.g:1:37: IF
            pass 
            self.mIF()



        elif alt6 == 7:
            # grammar/ShyLexer.g:1:40: INDENT
            pass 
            self.mINDENT()



        elif alt6 == 8:
            # grammar/ShyLexer.g:1:47: MODULE
            pass 
            self.mMODULE()



        elif alt6 == 9:
            # grammar/ShyLexer.g:1:54: OPS
            pass 
            self.mOPS()



        elif alt6 == 10:
            # grammar/ShyLexer.g:1:58: PASTE
            pass 
            self.mPASTE()



        elif alt6 == 11:
            # grammar/ShyLexer.g:1:64: PROC
            pass 
            self.mPROC()



        elif alt6 == 12:
            # grammar/ShyLexer.g:1:69: REPLACE
            pass 
            self.mREPLACE()



        elif alt6 == 13:
            # grammar/ShyLexer.g:1:77: STATELESS
            pass 
            self.mSTATELESS()



        elif alt6 == 14:
            # grammar/ShyLexer.g:1:87: TYPES
            pass 
            self.mTYPES()



        elif alt6 == 15:
            # grammar/ShyLexer.g:1:93: VARS
            pass 
            self.mVARS()



        elif alt6 == 16:
            # grammar/ShyLexer.g:1:98: WITH
            pass 
            self.mWITH()



        elif alt6 == 17:
            # grammar/ShyLexer.g:1:103: ARROW_LEFT
            pass 
            self.mARROW_LEFT()



        elif alt6 == 18:
            # grammar/ShyLexer.g:1:114: ARROW_RIGHT
            pass 
            self.mARROW_RIGHT()



        elif alt6 == 19:
            # grammar/ShyLexer.g:1:126: CURLY_OPEN
            pass 
            self.mCURLY_OPEN()



        elif alt6 == 20:
            # grammar/ShyLexer.g:1:137: CURLY_CLOSE
            pass 
            self.mCURLY_CLOSE()



        elif alt6 == 21:
            # grammar/ShyLexer.g:1:149: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt6 == 22:
            # grammar/ShyLexer.g:1:156: MINUS
            pass 
            self.mMINUS()



        elif alt6 == 23:
            # grammar/ShyLexer.g:1:162: UNDERSCORE
            pass 
            self.mUNDERSCORE()



        elif alt6 == 24:
            # grammar/ShyLexer.g:1:173: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt6 == 25:
            # grammar/ShyLexer.g:1:181: ID
            pass 
            self.mID()



        elif alt6 == 26:
            # grammar/ShyLexer.g:1:184: NUMBER
            pass 
            self.mNUMBER()



        elif alt6 == 27:
            # grammar/ShyLexer.g:1:191: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt6 == 28:
            # grammar/ShyLexer.g:1:202: EXPRESSION
            pass 
            self.mEXPRESSION()



        elif alt6 == 29:
            # grammar/ShyLexer.g:1:213: STRING
            pass 
            self.mSTRING()



        elif alt6 == 30:
            # grammar/ShyLexer.g:1:220: TREE_ARBITRARY_TOKEN
            pass 
            self.mTREE_ARBITRARY_TOKEN()



        elif alt6 == 31:
            # grammar/ShyLexer.g:1:241: TREE_CONSTS
            pass 
            self.mTREE_CONSTS()



        elif alt6 == 32:
            # grammar/ShyLexer.g:1:253: TREE_COPY
            pass 
            self.mTREE_COPY()



        elif alt6 == 33:
            # grammar/ShyLexer.g:1:263: TREE_COPY_PASTE
            pass 
            self.mTREE_COPY_PASTE()



        elif alt6 == 34:
            # grammar/ShyLexer.g:1:279: TREE_EXPRESSION
            pass 
            self.mTREE_EXPRESSION()



        elif alt6 == 35:
            # grammar/ShyLexer.g:1:295: TREE_HINT
            pass 
            self.mTREE_HINT()



        elif alt6 == 36:
            # grammar/ShyLexer.g:1:305: TREE_HINT_NONE
            pass 
            self.mTREE_HINT_NONE()



        elif alt6 == 37:
            # grammar/ShyLexer.g:1:320: TREE_MODULE
            pass 
            self.mTREE_MODULE()



        elif alt6 == 38:
            # grammar/ShyLexer.g:1:332: TREE_NUM_FRACT
            pass 
            self.mTREE_NUM_FRACT()



        elif alt6 == 39:
            # grammar/ShyLexer.g:1:347: TREE_NUM_WHOLE
            pass 
            self.mTREE_NUM_WHOLE()



        elif alt6 == 40:
            # grammar/ShyLexer.g:1:362: TREE_PASTE
            pass 
            self.mTREE_PASTE()



        elif alt6 == 41:
            # grammar/ShyLexer.g:1:373: TREE_PASTE_REPLACE
            pass 
            self.mTREE_PASTE_REPLACE()



        elif alt6 == 42:
            # grammar/ShyLexer.g:1:392: TREE_PASTE_WITH
            pass 
            self.mTREE_PASTE_WITH()



        elif alt6 == 43:
            # grammar/ShyLexer.g:1:408: TREE_PROC
            pass 
            self.mTREE_PROC()



        elif alt6 == 44:
            # grammar/ShyLexer.g:1:418: TREE_PROC_ARGS
            pass 
            self.mTREE_PROC_ARGS()



        elif alt6 == 45:
            # grammar/ShyLexer.g:1:433: TREE_PROC_OPS
            pass 
            self.mTREE_PROC_OPS()



        elif alt6 == 46:
            # grammar/ShyLexer.g:1:447: TREE_PROC_VARS
            pass 
            self.mTREE_PROC_VARS()



        elif alt6 == 47:
            # grammar/ShyLexer.g:1:462: TREE_STATELESS
            pass 
            self.mTREE_STATELESS()



        elif alt6 == 48:
            # grammar/ShyLexer.g:1:477: TREE_STATEMENT_CALL
            pass 
            self.mTREE_STATEMENT_CALL()



        elif alt6 == 49:
            # grammar/ShyLexer.g:1:497: TREE_STATEMENT_CALL_ARGS
            pass 
            self.mTREE_STATEMENT_CALL_ARGS()



        elif alt6 == 50:
            # grammar/ShyLexer.g:1:522: TREE_TYPES
            pass 
            self.mTREE_TYPES()



        elif alt6 == 51:
            # grammar/ShyLexer.g:1:533: TREE_TYPES_ITEM
            pass 
            self.mTREE_TYPES_ITEM()



        elif alt6 == 52:
            # grammar/ShyLexer.g:1:549: TREE_VAR
            pass 
            self.mTREE_VAR()



        elif alt6 == 53:
            # grammar/ShyLexer.g:1:558: TREE_VAR_HINT
            pass 
            self.mTREE_VAR_HINT()



        elif alt6 == 54:
            # grammar/ShyLexer.g:1:572: TREE_VARS_HINT
            pass 
            self.mTREE_VARS_HINT()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\uffff\14\24\1\uffff\1\52\13\uffff\3\24\1\60\1\61\12\24\3\uffff"
        u"\4\24\2\uffff\2\24\1\103\7\24\1\uffff\1\114\1\24\1\116\3\24\1\uffff"
        u"\1\24\1\123\3\24\1\127\1\130\2\uffff\1\24\1\uffff\3\24\1\136\1"
        u"\uffff\2\24\1\141\3\uffff\1\154\1\155\1\156\1\157\1\uffff\2\24"
        u"\17\uffff\1\172\1\24\11\uffff\1\24\10\uffff\1\u008f\1\u0090\1\u0092"
        u"\1\u0094\2\uffff\1\u0099\14\uffff\1\u009d\3\uffff\1\u00a4\22\uffff"
        u"\1\u00b0\2\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\u00b1\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\12\1\162\1\157\1\145\1\146\1\157\1\160\1\141\1\145\1\164\1\171"
        u"\1\141\1\151\1\uffff\1\76\12\uffff\1\122\1\147\1\156\1\144\2\60"
        u"\2\144\2\163\1\157\1\160\1\141\1\160\1\162\1\164\2\uffff\1\105"
        u"\2\163\1\171\1\145\2\uffff\1\145\1\165\1\60\1\164\1\143\1\154\1"
        u"\164\1\145\1\163\1\150\1\105\1\60\1\164\1\60\2\156\1\154\1\uffff"
        u"\1\145\1\60\1\141\1\145\1\163\2\60\1\137\1\uffff\1\163\1\uffff"
        u"\2\164\1\145\1\60\1\uffff\1\143\1\154\1\60\2\uffff\1\101\4\60\1"
        u"\uffff\2\145\2\uffff\1\117\1\uffff\1\111\1\uffff\1\125\1\101\1"
        u"\124\1\131\1\101\4\uffff\1\60\1\163\2\116\1\115\1\123\1\117\1\101"
        u"\1\120\1\122\1\uffff\1\163\1\uffff\1\131\1\124\1\137\1\124\1\103"
        u"\1\124\1\105\1\123\1\60\2\137\1\106\1\105\1\137\1\105\1\123\12"
        u"\uffff\1\137\1\101\1\uffff\1\114\1\137\1\122\5\uffff\1\105\4\uffff"
        u"\1\116\1\124\1\137\1\103\1\101\2\114\1\137\2\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\175\1\162\2\157\1\156\1\157\1\160\1\162\1\145\1\164\1\171\1"
        u"\141\1\151\1\uffff\1\76\12\uffff\1\122\1\147\1\160\1\144\2\172"
        u"\2\144\2\163\1\157\1\160\1\141\1\160\1\162\1\164\2\uffff\1\105"
        u"\2\163\1\171\1\145\2\uffff\1\145\1\165\1\172\1\164\1\143\1\154"
        u"\1\164\1\145\1\163\1\150\1\105\1\172\1\164\1\172\2\156\1\154\1"
        u"\uffff\1\145\1\172\1\141\1\145\1\163\2\172\1\137\1\uffff\1\163"
        u"\1\uffff\2\164\1\145\1\172\1\uffff\1\143\1\154\1\172\2\uffff\1"
        u"\126\4\172\1\uffff\2\145\2\uffff\1\117\1\uffff\1\111\1\uffff\1"
        u"\125\1\122\1\124\1\131\1\101\4\uffff\1\172\1\163\1\120\1\116\1"
        u"\115\1\123\1\117\1\101\1\120\1\122\1\uffff\1\163\1\uffff\1\131"
        u"\1\124\1\137\1\124\1\103\1\124\1\105\1\137\1\172\2\137\1\127\1"
        u"\105\1\137\1\105\1\123\12\uffff\1\137\1\126\1\uffff\1\115\1\137"
        u"\1\127\5\uffff\1\105\4\uffff\1\116\1\124\1\137\1\103\1\101\2\114"
        u"\1\137\2\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\15\uffff\1\21\1\uffff\1\23\1\24\1\25\1\27\1\30\1\31\1\32\1\33"
        u"\1\34\1\35\20\uffff\1\22\1\26\5\uffff\1\5\1\6\21\uffff\1\11\10"
        u"\uffff\1\1\1\uffff\1\3\4\uffff\1\13\3\uffff\1\17\1\20\5\uffff\1"
        u"\12\2\uffff\1\16\1\36\1\uffff\1\42\1\uffff\1\45\5\uffff\1\2\1\4"
        u"\1\7\1\10\12\uffff\1\14\1\uffff\1\37\20\uffff\1\65\1\66\1\64\1"
        u"\15\1\41\1\40\1\44\1\43\1\46\1\47\2\uffff\1\53\3\uffff\1\50\1\54"
        u"\1\55\1\56\1\57\1\uffff\1\63\1\62\1\51\1\52\10\uffff\1\61\1\60"
        )

    DFA6_special = DFA.unpack(
        u"\u00b1\uffff"
        )


    DFA6_transition = [
        DFA.unpack(u"\1\23\25\uffff\1\26\6\uffff\1\30\5\uffff\1\16\1\uffff"
        u"\1\21\12\25\2\uffff\1\15\27\uffff\1\31\6\uffff\1\27\3\uffff\1\22"
        u"\1\uffff\1\1\1\24\1\2\1\3\4\24\1\4\3\24\1\5\1\24\1\6\1\7\1\24\1"
        u"\10\1\11\1\12\1\24\1\13\1\14\3\24\1\17\1\uffff\1\20"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34\11\uffff\1\35"),
        DFA.unpack(u"\1\36\7\uffff\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42\20\uffff\1\43"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\51"),
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
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55\1\uffff\1\56"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\142\1\uffff\1\143\1\uffff\1\144\2\uffff\1\145\4"
        u"\uffff\1\146\1\147\1\uffff\1\150\2\uffff\1\151\1\152\1\uffff\1"
        u"\153"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\162"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165\20\uffff\1\166"),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\174\1\uffff\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\1\u008e\13\uffff\1\u008d"),
        DFA.unpack(u"\12\24\45\uffff\1\24\1\uffff\32\24"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\1\u0095\20\uffff\1\u0096"),
        DFA.unpack(u"\1\u0097"),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
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
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\1\u009e\15\uffff\1\u009f\6\uffff\1\u00a0"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a1\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a5\4\uffff\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
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
