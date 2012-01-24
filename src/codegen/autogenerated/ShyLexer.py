# $ANTLR 3.4 grammar/ShyLexer.g 2012-01-24 20:19:18

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
ELSE=14
EXPRESSION=15
ID=16
IF=17
INDENT=18
MINUS=19
MODULE=20
NEWLINE=21
NUMBER=22
OPS=23
PASTE=24
PROC=25
REPLACE=26
STATELESS=27
STRING=28
TREE_ARBITRARY_TOKEN=29
TREE_CONDITION_ANY=30
TREE_CONSTS=31
TREE_COPY=32
TREE_COPY_PASTE=33
TREE_EXPRESSION=34
TREE_HINT=35
TREE_HINT_NONE=36
TREE_MODULE=37
TREE_NUM_FRACT=38
TREE_NUM_WHOLE=39
TREE_PASTE=40
TREE_PASTE_REPLACE=41
TREE_PASTE_WITH=42
TREE_PROC=43
TREE_PROC_ARGS=44
TREE_PROC_VARS=45
TREE_STATELESS=46
TREE_STATEMENTS=47
TREE_STATEMENT_CALL=48
TREE_STATEMENT_CALL_ARGS=49
TREE_STATEMENT_ELIF=50
TREE_STATEMENT_ELSE=51
TREE_STATEMENT_IF=52
TREE_TYPES=53
TREE_TYPES_ITEM=54
TREE_VAR=55
TREE_VARS_HINT=56
TREE_VAR_HINT=57
TYPES=58
UNDERSCORE=59
VARS=60
WHITESPACE=61
WITH=62


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



    # $ANTLR start "ELSE"
    def mELSE(self, ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:26:6: ( 'else' )
            # grammar/ShyLexer.g:26:8: 'else'
            pass 
            self.match("else")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELSE"



    # $ANTLR start "IF"
    def mIF(self, ):
        try:
            _type = IF
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:27:4: ( 'if' )
            # grammar/ShyLexer.g:27:6: 'if'
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

            # grammar/ShyLexer.g:28:8: ( 'indent' )
            # grammar/ShyLexer.g:28:10: 'indent'
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

            # grammar/ShyLexer.g:29:8: ( 'module' )
            # grammar/ShyLexer.g:29:10: 'module'
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

            # grammar/ShyLexer.g:30:5: ( 'ops' )
            # grammar/ShyLexer.g:30:7: 'ops'
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

            # grammar/ShyLexer.g:31:7: ( 'paste' )
            # grammar/ShyLexer.g:31:9: 'paste'
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

            # grammar/ShyLexer.g:32:6: ( 'proc' )
            # grammar/ShyLexer.g:32:8: 'proc'
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

            # grammar/ShyLexer.g:33:9: ( 'replace' )
            # grammar/ShyLexer.g:33:11: 'replace'
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

            # grammar/ShyLexer.g:34:11: ( 'stateless' )
            # grammar/ShyLexer.g:34:13: 'stateless'
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

            # grammar/ShyLexer.g:35:7: ( 'types' )
            # grammar/ShyLexer.g:35:9: 'types'
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

            # grammar/ShyLexer.g:36:6: ( 'vars' )
            # grammar/ShyLexer.g:36:8: 'vars'
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

            # grammar/ShyLexer.g:37:6: ( 'with' )
            # grammar/ShyLexer.g:37:8: 'with'
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

            # grammar/ShyLexer.g:39:12: ( '<-' )
            # grammar/ShyLexer.g:39:14: '<-'
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

            # grammar/ShyLexer.g:40:13: ( '->' )
            # grammar/ShyLexer.g:40:15: '->'
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

            # grammar/ShyLexer.g:41:12: ( '{' )
            # grammar/ShyLexer.g:41:14: '{'
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

            # grammar/ShyLexer.g:42:13: ( '}' )
            # grammar/ShyLexer.g:42:15: '}'
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

            # grammar/ShyLexer.g:43:8: ( '/' )
            # grammar/ShyLexer.g:43:10: '/'
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

            # grammar/ShyLexer.g:44:7: ( '-' )
            # grammar/ShyLexer.g:44:9: '-'
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

            # grammar/ShyLexer.g:45:12: ( '_' )
            # grammar/ShyLexer.g:45:14: '_'
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

            # grammar/ShyLexer.g:46:9: ( '\\n' )
            # grammar/ShyLexer.g:46:11: '\\n'
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

            # grammar/ShyLexer.g:47:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/ShyLexer.g:47:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/ShyLexer.g:47:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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

            # grammar/ShyLexer.g:48:8: ( ( '0' .. '9' )+ )
            # grammar/ShyLexer.g:48:10: ( '0' .. '9' )+
            pass 
            # grammar/ShyLexer.g:48:10: ( '0' .. '9' )+
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

            # grammar/ShyLexer.g:49:12: ( ( ' ' )+ )
            # grammar/ShyLexer.g:49:14: ( ' ' )+
            pass 
            # grammar/ShyLexer.g:49:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/ShyLexer.g:49:14: ' '
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

            # grammar/ShyLexer.g:50:12: ( '[' ( . )* ']' )
            # grammar/ShyLexer.g:50:14: '[' ( . )* ']'
            pass 
            self.match(91)

            # grammar/ShyLexer.g:50:18: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 93) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 92) or (94 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/ShyLexer.g:50:18: .
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

            # grammar/ShyLexer.g:51:8: ( '\\'' ( . )* '\\'' )
            # grammar/ShyLexer.g:51:10: '\\'' ( . )* '\\''
            pass 
            self.match(39)

            # grammar/ShyLexer.g:51:15: ( . )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 39) :
                    alt5 = 2
                elif ((0 <= LA5_0 <= 38) or (40 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # grammar/ShyLexer.g:51:15: .
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

            # grammar/ShyLexer.g:53:22: ( 'TREE_ARBITRARY_TOKEN' )
            # grammar/ShyLexer.g:53:24: 'TREE_ARBITRARY_TOKEN'
            pass 
            self.match("TREE_ARBITRARY_TOKEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_ARBITRARY_TOKEN"



    # $ANTLR start "TREE_CONDITION_ANY"
    def mTREE_CONDITION_ANY(self, ):
        try:
            _type = TREE_CONDITION_ANY
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:54:20: ( 'TREE_COND_ANY' )
            # grammar/ShyLexer.g:54:22: 'TREE_COND_ANY'
            pass 
            self.match("TREE_COND_ANY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_CONDITION_ANY"



    # $ANTLR start "TREE_CONSTS"
    def mTREE_CONSTS(self, ):
        try:
            _type = TREE_CONSTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:55:13: ( 'TREE_CONSTS' )
            # grammar/ShyLexer.g:55:15: 'TREE_CONSTS'
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

            # grammar/ShyLexer.g:56:11: ( 'TREE_COPY' )
            # grammar/ShyLexer.g:56:13: 'TREE_COPY'
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

            # grammar/ShyLexer.g:57:17: ( 'TREE_COPY_PASTE' )
            # grammar/ShyLexer.g:57:19: 'TREE_COPY_PASTE'
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

            # grammar/ShyLexer.g:58:17: ( 'TREE_EXPRESSION' )
            # grammar/ShyLexer.g:58:19: 'TREE_EXPRESSION'
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

            # grammar/ShyLexer.g:59:11: ( 'TREE_HINT' )
            # grammar/ShyLexer.g:59:13: 'TREE_HINT'
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

            # grammar/ShyLexer.g:60:16: ( 'TREE_HINT_NONE' )
            # grammar/ShyLexer.g:60:18: 'TREE_HINT_NONE'
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

            # grammar/ShyLexer.g:61:13: ( 'TREE_MODULE' )
            # grammar/ShyLexer.g:61:15: 'TREE_MODULE'
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

            # grammar/ShyLexer.g:62:16: ( 'TREE_NUM_FRACT' )
            # grammar/ShyLexer.g:62:18: 'TREE_NUM_FRACT'
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

            # grammar/ShyLexer.g:63:16: ( 'TREE_NUM_WHOLE' )
            # grammar/ShyLexer.g:63:18: 'TREE_NUM_WHOLE'
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

            # grammar/ShyLexer.g:64:12: ( 'TREE_PASTE' )
            # grammar/ShyLexer.g:64:14: 'TREE_PASTE'
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

            # grammar/ShyLexer.g:65:20: ( 'TREE_PASTE_REPLACE' )
            # grammar/ShyLexer.g:65:22: 'TREE_PASTE_REPLACE'
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

            # grammar/ShyLexer.g:66:17: ( 'TREE_PASTE_WITH' )
            # grammar/ShyLexer.g:66:19: 'TREE_PASTE_WITH'
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

            # grammar/ShyLexer.g:67:11: ( 'TREE_PROC' )
            # grammar/ShyLexer.g:67:13: 'TREE_PROC'
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

            # grammar/ShyLexer.g:68:16: ( 'TREE_PROC_ARGS' )
            # grammar/ShyLexer.g:68:18: 'TREE_PROC_ARGS'
            pass 
            self.match("TREE_PROC_ARGS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PROC_ARGS"



    # $ANTLR start "TREE_PROC_VARS"
    def mTREE_PROC_VARS(self, ):
        try:
            _type = TREE_PROC_VARS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:69:16: ( 'TREE_PROC_VARS' )
            # grammar/ShyLexer.g:69:18: 'TREE_PROC_VARS'
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

            # grammar/ShyLexer.g:70:16: ( 'TREE_STATELESS' )
            # grammar/ShyLexer.g:70:18: 'TREE_STATELESS'
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

            # grammar/ShyLexer.g:71:21: ( 'TREE_STATEMENT_CALL' )
            # grammar/ShyLexer.g:71:23: 'TREE_STATEMENT_CALL'
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

            # grammar/ShyLexer.g:72:26: ( 'TREE_STATEMENT_CALL_ARGS' )
            # grammar/ShyLexer.g:72:28: 'TREE_STATEMENT_CALL_ARGS'
            pass 
            self.match("TREE_STATEMENT_CALL_ARGS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_CALL_ARGS"



    # $ANTLR start "TREE_STATEMENT_ELIF"
    def mTREE_STATEMENT_ELIF(self, ):
        try:
            _type = TREE_STATEMENT_ELIF
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:73:21: ( 'TREE_STATEMENT_ELIF' )
            # grammar/ShyLexer.g:73:23: 'TREE_STATEMENT_ELIF'
            pass 
            self.match("TREE_STATEMENT_ELIF")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_ELIF"



    # $ANTLR start "TREE_STATEMENT_ELSE"
    def mTREE_STATEMENT_ELSE(self, ):
        try:
            _type = TREE_STATEMENT_ELSE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:74:21: ( 'TREE_STATEMENT_ELSE' )
            # grammar/ShyLexer.g:74:23: 'TREE_STATEMENT_ELSE'
            pass 
            self.match("TREE_STATEMENT_ELSE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_ELSE"



    # $ANTLR start "TREE_STATEMENT_IF"
    def mTREE_STATEMENT_IF(self, ):
        try:
            _type = TREE_STATEMENT_IF
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:75:19: ( 'TREE_STATEMENT_IF' )
            # grammar/ShyLexer.g:75:21: 'TREE_STATEMENT_IF'
            pass 
            self.match("TREE_STATEMENT_IF")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_IF"



    # $ANTLR start "TREE_STATEMENTS"
    def mTREE_STATEMENTS(self, ):
        try:
            _type = TREE_STATEMENTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:76:17: ( 'TREE_STATEMENTS' )
            # grammar/ShyLexer.g:76:19: 'TREE_STATEMENTS'
            pass 
            self.match("TREE_STATEMENTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENTS"



    # $ANTLR start "TREE_TYPES"
    def mTREE_TYPES(self, ):
        try:
            _type = TREE_TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:77:12: ( 'TREE_TYPES' )
            # grammar/ShyLexer.g:77:14: 'TREE_TYPES'
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

            # grammar/ShyLexer.g:78:17: ( 'TREE_TYPES_ITEM' )
            # grammar/ShyLexer.g:78:19: 'TREE_TYPES_ITEM'
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

            # grammar/ShyLexer.g:79:10: ( 'TREE_VAR' )
            # grammar/ShyLexer.g:79:12: 'TREE_VAR'
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

            # grammar/ShyLexer.g:80:15: ( 'TREE_VAR_HINT' )
            # grammar/ShyLexer.g:80:17: 'TREE_VAR_HINT'
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

            # grammar/ShyLexer.g:81:16: ( 'TREE_VARS_HINT' )
            # grammar/ShyLexer.g:81:18: 'TREE_VARS_HINT'
            pass 
            self.match("TREE_VARS_HINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_VARS_HINT"



    def mTokens(self):
        # grammar/ShyLexer.g:1:8: ( ARGS | CONSTS | COPY | DEDENT | DO | ELSE | IF | INDENT | MODULE | OPS | PASTE | PROC | REPLACE | STATELESS | TYPES | VARS | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | WHITESPACE | EXPRESSION | STRING | TREE_ARBITRARY_TOKEN | TREE_CONDITION_ANY | TREE_CONSTS | TREE_COPY | TREE_COPY_PASTE | TREE_EXPRESSION | TREE_HINT | TREE_HINT_NONE | TREE_MODULE | TREE_NUM_FRACT | TREE_NUM_WHOLE | TREE_PASTE | TREE_PASTE_REPLACE | TREE_PASTE_WITH | TREE_PROC | TREE_PROC_ARGS | TREE_PROC_VARS | TREE_STATELESS | TREE_STATEMENT_CALL | TREE_STATEMENT_CALL_ARGS | TREE_STATEMENT_ELIF | TREE_STATEMENT_ELSE | TREE_STATEMENT_IF | TREE_STATEMENTS | TREE_TYPES | TREE_TYPES_ITEM | TREE_VAR | TREE_VAR_HINT | TREE_VARS_HINT )
        alt6 = 59
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
            # grammar/ShyLexer.g:1:37: ELSE
            pass 
            self.mELSE()



        elif alt6 == 7:
            # grammar/ShyLexer.g:1:42: IF
            pass 
            self.mIF()



        elif alt6 == 8:
            # grammar/ShyLexer.g:1:45: INDENT
            pass 
            self.mINDENT()



        elif alt6 == 9:
            # grammar/ShyLexer.g:1:52: MODULE
            pass 
            self.mMODULE()



        elif alt6 == 10:
            # grammar/ShyLexer.g:1:59: OPS
            pass 
            self.mOPS()



        elif alt6 == 11:
            # grammar/ShyLexer.g:1:63: PASTE
            pass 
            self.mPASTE()



        elif alt6 == 12:
            # grammar/ShyLexer.g:1:69: PROC
            pass 
            self.mPROC()



        elif alt6 == 13:
            # grammar/ShyLexer.g:1:74: REPLACE
            pass 
            self.mREPLACE()



        elif alt6 == 14:
            # grammar/ShyLexer.g:1:82: STATELESS
            pass 
            self.mSTATELESS()



        elif alt6 == 15:
            # grammar/ShyLexer.g:1:92: TYPES
            pass 
            self.mTYPES()



        elif alt6 == 16:
            # grammar/ShyLexer.g:1:98: VARS
            pass 
            self.mVARS()



        elif alt6 == 17:
            # grammar/ShyLexer.g:1:103: WITH
            pass 
            self.mWITH()



        elif alt6 == 18:
            # grammar/ShyLexer.g:1:108: ARROW_LEFT
            pass 
            self.mARROW_LEFT()



        elif alt6 == 19:
            # grammar/ShyLexer.g:1:119: ARROW_RIGHT
            pass 
            self.mARROW_RIGHT()



        elif alt6 == 20:
            # grammar/ShyLexer.g:1:131: CURLY_OPEN
            pass 
            self.mCURLY_OPEN()



        elif alt6 == 21:
            # grammar/ShyLexer.g:1:142: CURLY_CLOSE
            pass 
            self.mCURLY_CLOSE()



        elif alt6 == 22:
            # grammar/ShyLexer.g:1:154: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt6 == 23:
            # grammar/ShyLexer.g:1:161: MINUS
            pass 
            self.mMINUS()



        elif alt6 == 24:
            # grammar/ShyLexer.g:1:167: UNDERSCORE
            pass 
            self.mUNDERSCORE()



        elif alt6 == 25:
            # grammar/ShyLexer.g:1:178: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt6 == 26:
            # grammar/ShyLexer.g:1:186: ID
            pass 
            self.mID()



        elif alt6 == 27:
            # grammar/ShyLexer.g:1:189: NUMBER
            pass 
            self.mNUMBER()



        elif alt6 == 28:
            # grammar/ShyLexer.g:1:196: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt6 == 29:
            # grammar/ShyLexer.g:1:207: EXPRESSION
            pass 
            self.mEXPRESSION()



        elif alt6 == 30:
            # grammar/ShyLexer.g:1:218: STRING
            pass 
            self.mSTRING()



        elif alt6 == 31:
            # grammar/ShyLexer.g:1:225: TREE_ARBITRARY_TOKEN
            pass 
            self.mTREE_ARBITRARY_TOKEN()



        elif alt6 == 32:
            # grammar/ShyLexer.g:1:246: TREE_CONDITION_ANY
            pass 
            self.mTREE_CONDITION_ANY()



        elif alt6 == 33:
            # grammar/ShyLexer.g:1:265: TREE_CONSTS
            pass 
            self.mTREE_CONSTS()



        elif alt6 == 34:
            # grammar/ShyLexer.g:1:277: TREE_COPY
            pass 
            self.mTREE_COPY()



        elif alt6 == 35:
            # grammar/ShyLexer.g:1:287: TREE_COPY_PASTE
            pass 
            self.mTREE_COPY_PASTE()



        elif alt6 == 36:
            # grammar/ShyLexer.g:1:303: TREE_EXPRESSION
            pass 
            self.mTREE_EXPRESSION()



        elif alt6 == 37:
            # grammar/ShyLexer.g:1:319: TREE_HINT
            pass 
            self.mTREE_HINT()



        elif alt6 == 38:
            # grammar/ShyLexer.g:1:329: TREE_HINT_NONE
            pass 
            self.mTREE_HINT_NONE()



        elif alt6 == 39:
            # grammar/ShyLexer.g:1:344: TREE_MODULE
            pass 
            self.mTREE_MODULE()



        elif alt6 == 40:
            # grammar/ShyLexer.g:1:356: TREE_NUM_FRACT
            pass 
            self.mTREE_NUM_FRACT()



        elif alt6 == 41:
            # grammar/ShyLexer.g:1:371: TREE_NUM_WHOLE
            pass 
            self.mTREE_NUM_WHOLE()



        elif alt6 == 42:
            # grammar/ShyLexer.g:1:386: TREE_PASTE
            pass 
            self.mTREE_PASTE()



        elif alt6 == 43:
            # grammar/ShyLexer.g:1:397: TREE_PASTE_REPLACE
            pass 
            self.mTREE_PASTE_REPLACE()



        elif alt6 == 44:
            # grammar/ShyLexer.g:1:416: TREE_PASTE_WITH
            pass 
            self.mTREE_PASTE_WITH()



        elif alt6 == 45:
            # grammar/ShyLexer.g:1:432: TREE_PROC
            pass 
            self.mTREE_PROC()



        elif alt6 == 46:
            # grammar/ShyLexer.g:1:442: TREE_PROC_ARGS
            pass 
            self.mTREE_PROC_ARGS()



        elif alt6 == 47:
            # grammar/ShyLexer.g:1:457: TREE_PROC_VARS
            pass 
            self.mTREE_PROC_VARS()



        elif alt6 == 48:
            # grammar/ShyLexer.g:1:472: TREE_STATELESS
            pass 
            self.mTREE_STATELESS()



        elif alt6 == 49:
            # grammar/ShyLexer.g:1:487: TREE_STATEMENT_CALL
            pass 
            self.mTREE_STATEMENT_CALL()



        elif alt6 == 50:
            # grammar/ShyLexer.g:1:507: TREE_STATEMENT_CALL_ARGS
            pass 
            self.mTREE_STATEMENT_CALL_ARGS()



        elif alt6 == 51:
            # grammar/ShyLexer.g:1:532: TREE_STATEMENT_ELIF
            pass 
            self.mTREE_STATEMENT_ELIF()



        elif alt6 == 52:
            # grammar/ShyLexer.g:1:552: TREE_STATEMENT_ELSE
            pass 
            self.mTREE_STATEMENT_ELSE()



        elif alt6 == 53:
            # grammar/ShyLexer.g:1:572: TREE_STATEMENT_IF
            pass 
            self.mTREE_STATEMENT_IF()



        elif alt6 == 54:
            # grammar/ShyLexer.g:1:590: TREE_STATEMENTS
            pass 
            self.mTREE_STATEMENTS()



        elif alt6 == 55:
            # grammar/ShyLexer.g:1:606: TREE_TYPES
            pass 
            self.mTREE_TYPES()



        elif alt6 == 56:
            # grammar/ShyLexer.g:1:617: TREE_TYPES_ITEM
            pass 
            self.mTREE_TYPES_ITEM()



        elif alt6 == 57:
            # grammar/ShyLexer.g:1:633: TREE_VAR
            pass 
            self.mTREE_VAR()



        elif alt6 == 58:
            # grammar/ShyLexer.g:1:642: TREE_VAR_HINT
            pass 
            self.mTREE_VAR_HINT()



        elif alt6 == 59:
            # grammar/ShyLexer.g:1:656: TREE_VARS_HINT
            pass 
            self.mTREE_VARS_HINT()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\uffff\15\25\1\uffff\1\54\13\uffff\3\25\1\62\1\25\1\64\12\25"
        u"\3\uffff\4\25\1\uffff\1\25\1\uffff\2\25\1\107\7\25\1\uffff\1\120"
        u"\1\25\1\122\1\25\1\124\2\25\1\uffff\1\25\1\130\3\25\1\134\1\135"
        u"\2\uffff\1\25\1\uffff\1\25\1\uffff\2\25\1\143\1\uffff\2\25\1\146"
        u"\3\uffff\1\161\1\162\1\163\1\164\1\uffff\2\25\17\uffff\1\177\1"
        u"\25\11\uffff\1\25\10\uffff\1\u0096\1\u0097\2\uffff\1\u0099\1\u009b"
        u"\2\uffff\1\u00a0\14\uffff\1\u00a4\3\uffff\1\u00aa\27\uffff\1\u00bc"
        u"\2\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\u00bd\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\12\1\162\1\157\1\145\1\154\1\146\1\157\1\160\1\141\1\145\1\164"
        u"\1\171\1\141\1\151\1\uffff\1\76\12\uffff\1\122\1\147\1\156\1\144"
        u"\1\60\1\163\1\60\2\144\2\163\1\157\1\160\1\141\1\160\1\162\1\164"
        u"\2\uffff\1\105\2\163\1\171\1\145\1\uffff\1\145\1\uffff\1\145\1"
        u"\165\1\60\1\164\1\143\1\154\1\164\1\145\1\163\1\150\1\105\1\60"
        u"\1\164\1\60\1\156\1\60\1\156\1\154\1\uffff\1\145\1\60\1\141\1\145"
        u"\1\163\2\60\1\137\1\uffff\1\163\1\uffff\1\164\1\uffff\1\164\1\145"
        u"\1\60\1\uffff\1\143\1\154\1\60\2\uffff\1\101\4\60\1\uffff\2\145"
        u"\2\uffff\1\117\1\uffff\1\111\1\uffff\1\125\1\101\1\124\1\131\1"
        u"\101\4\uffff\1\60\1\163\2\116\1\115\1\123\1\117\1\101\1\120\1\122"
        u"\1\uffff\1\163\1\104\1\131\1\124\1\137\1\124\1\103\1\124\1\105"
        u"\1\123\1\60\2\uffff\2\137\1\106\1\105\1\137\1\105\1\123\12\uffff"
        u"\1\137\1\101\1\uffff\1\114\1\137\1\122\4\uffff\1\105\4\uffff\1"
        u"\116\1\124\1\123\1\103\1\uffff\1\101\1\114\1\uffff\1\114\1\111"
        u"\1\114\2\uffff\1\137\2\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\175\1\162\2\157\1\154\1\156\1\157\1\160\1\162\1\145\1\164\1"
        u"\171\1\141\1\151\1\uffff\1\76\12\uffff\1\122\1\147\1\160\1\144"
        u"\1\172\1\163\1\172\2\144\2\163\1\157\1\160\1\141\1\160\1\162\1"
        u"\164\2\uffff\1\105\2\163\1\171\1\145\1\uffff\1\145\1\uffff\1\145"
        u"\1\165\1\172\1\164\1\143\1\154\1\164\1\145\1\163\1\150\1\105\1"
        u"\172\1\164\1\172\1\156\1\172\1\156\1\154\1\uffff\1\145\1\172\1"
        u"\141\1\145\1\163\2\172\1\137\1\uffff\1\163\1\uffff\1\164\1\uffff"
        u"\1\164\1\145\1\172\1\uffff\1\143\1\154\1\172\2\uffff\1\126\4\172"
        u"\1\uffff\2\145\2\uffff\1\117\1\uffff\1\111\1\uffff\1\125\1\122"
        u"\1\124\1\131\1\101\4\uffff\1\172\1\163\1\120\1\116\1\115\1\123"
        u"\1\117\1\101\1\120\1\122\1\uffff\1\163\1\123\1\131\1\124\1\137"
        u"\1\124\1\103\1\124\1\105\1\137\1\172\2\uffff\2\137\1\127\1\105"
        u"\1\137\1\105\1\123\12\uffff\1\137\1\126\1\uffff\1\115\1\137\1\127"
        u"\4\uffff\1\105\4\uffff\1\116\1\124\1\137\1\111\1\uffff\1\101\1"
        u"\114\1\uffff\1\114\1\123\1\114\2\uffff\1\137\2\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\16\uffff\1\22\1\uffff\1\24\1\25\1\26\1\30\1\31\1\32\1\33\1\34"
        u"\1\35\1\36\21\uffff\1\23\1\27\5\uffff\1\5\1\uffff\1\7\22\uffff"
        u"\1\12\10\uffff\1\1\1\uffff\1\3\1\uffff\1\6\3\uffff\1\14\3\uffff"
        u"\1\20\1\21\5\uffff\1\13\2\uffff\1\17\1\37\1\uffff\1\44\1\uffff"
        u"\1\47\5\uffff\1\2\1\4\1\10\1\11\12\uffff\1\15\13\uffff\1\40\1\41"
        u"\7\uffff\1\72\1\73\1\71\1\16\1\43\1\42\1\46\1\45\1\50\1\51\2\uffff"
        u"\1\55\3\uffff\1\52\1\56\1\57\1\60\1\uffff\1\70\1\67\1\53\1\54\4"
        u"\uffff\1\66\2\uffff\1\65\3\uffff\1\63\1\64\1\uffff\1\62\1\61"
        )

    DFA6_special = DFA.unpack(
        u"\u00bd\uffff"
        )


    DFA6_transition = [
        DFA.unpack(u"\1\24\25\uffff\1\27\6\uffff\1\31\5\uffff\1\17\1\uffff"
        u"\1\22\12\26\2\uffff\1\16\27\uffff\1\32\6\uffff\1\30\3\uffff\1\23"
        u"\1\uffff\1\1\1\25\1\2\1\3\1\4\3\25\1\5\3\25\1\6\1\25\1\7\1\10\1"
        u"\25\1\11\1\12\1\13\1\25\1\14\1\15\3\25\1\20\1\uffff\1\21"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u"\1\34"),
        DFA.unpack(u"\1\35\11\uffff\1\36"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\40\7\uffff\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44\20\uffff\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\53"),
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
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57\1\uffff\1\60"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\147\1\uffff\1\150\1\uffff\1\151\2\uffff\1\152\4"
        u"\uffff\1\153\1\154\1\uffff\1\155\2\uffff\1\156\1\157\1\uffff\1"
        u"\160"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\166"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\167"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172\20\uffff\1\173"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081\1\uffff\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\1\u0084"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008a"),
        DFA.unpack(u"\1\u008b\16\uffff\1\u008c"),
        DFA.unpack(u"\1\u008d"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\1\u0095\13\uffff\1\u0094"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0098"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009c\20\uffff\1\u009d"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
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
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a5\24\uffff\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a7\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00ab\4\uffff\1\u00ac"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b1\13\uffff\1\u00b0"),
        DFA.unpack(u"\1\u00b2\1\uffff\1\u00b3\3\uffff\1\u00b4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\1\u00b8\11\uffff\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00bb"),
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
