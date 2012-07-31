# $ANTLR 3.4 grammar/ShyLexer.g 2012-02-10 19:36:44

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
ALL=4
ANY=5
ARGS=6
ARROW_LEFT=7
ARROW_RIGHT=8
CONSTS=9
COPY=10
CURLY_CLOSE=11
CURLY_OPEN=12
DEDENT=13
DIVIDE=14
DO=15
ELIF=16
ELSE=17
EXPRESSION=18
ID=19
IF=20
INDENT=21
MESSAGES=22
MINUS=23
MODULE=24
MODULE_QUEUE=25
NEWLINE=26
NUMBER=27
OPS=28
PASTE=29
PROC=30
RECEIVE=31
REPLACE=32
REPLY=33
REQUEST=34
SEND=35
STATELESS=36
STRING=37
TRACE=38
TREE_ARBITRARY_TOKEN=39
TREE_ATTR=40
TREE_ATTRS_HINTS=41
TREE_ATTR_HINT=42
TREE_CONDITION_ALL=43
TREE_CONDITION_ANY=44
TREE_CONSTS=45
TREE_COPY=46
TREE_COPY_PASTE=47
TREE_EXPRESSION=48
TREE_HINT=49
TREE_HINT_NONE=50
TREE_LOCAL_VARS=51
TREE_MESSAGES=52
TREE_MESSAGES_ITEM=53
TREE_MESSAGES_ITEM_RECEIVE=54
TREE_MESSAGES_ITEM_REPLY=55
TREE_MESSAGES_ITEM_REQUEST=56
TREE_MODULE=57
TREE_MODULE_QUEUE=58
TREE_NUM_FRACT=59
TREE_NUM_WHOLE=60
TREE_PASTE=61
TREE_PASTE_REPLACE=62
TREE_PASTE_WITH=63
TREE_PROC=64
TREE_PROC_ARGS=65
TREE_RECEIVE=66
TREE_REQUEST=67
TREE_STATELESS=68
TREE_STATEMENTS=69
TREE_STATEMENT_ASSIGN=70
TREE_STATEMENT_ASSIGN_TO=71
TREE_STATEMENT_CALL=72
TREE_STATEMENT_ELIF=73
TREE_STATEMENT_ELSE=74
TREE_STATEMENT_IF=75
TREE_STATEMENT_SEND=76
TREE_STATEMENT_WHILE=77
TREE_STATEMENT_WITH=78
TREE_TRACE=79
TREE_TYPES=80
TREE_TYPES_ITEM=81
TREE_VARS=82
TYPES=83
UNDERSCORE=84
VARS=85
WHILE=86
WHITESPACE=87
WITH=88


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



    # $ANTLR start "ALL"
    def mALL(self, ):
        try:
            _type = ALL
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:21:5: ( 'all' )
            # grammar/ShyLexer.g:21:7: 'all'
            pass 
            self.match("all")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ALL"



    # $ANTLR start "ANY"
    def mANY(self, ):
        try:
            _type = ANY
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:22:5: ( 'any' )
            # grammar/ShyLexer.g:22:7: 'any'
            pass 
            self.match("any")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ANY"



    # $ANTLR start "ARGS"
    def mARGS(self, ):
        try:
            _type = ARGS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:23:6: ( 'args' )
            # grammar/ShyLexer.g:23:8: 'args'
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

            # grammar/ShyLexer.g:24:8: ( 'consts' )
            # grammar/ShyLexer.g:24:10: 'consts'
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

            # grammar/ShyLexer.g:25:6: ( 'copy' )
            # grammar/ShyLexer.g:25:8: 'copy'
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

            # grammar/ShyLexer.g:26:8: ( 'dedent' )
            # grammar/ShyLexer.g:26:10: 'dedent'
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

            # grammar/ShyLexer.g:27:4: ( 'do' )
            # grammar/ShyLexer.g:27:6: 'do'
            pass 
            self.match("do")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DO"



    # $ANTLR start "ELIF"
    def mELIF(self, ):
        try:
            _type = ELIF
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:28:6: ( 'elif' )
            # grammar/ShyLexer.g:28:8: 'elif'
            pass 
            self.match("elif")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELIF"



    # $ANTLR start "ELSE"
    def mELSE(self, ):
        try:
            _type = ELSE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:29:6: ( 'else' )
            # grammar/ShyLexer.g:29:8: 'else'
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

            # grammar/ShyLexer.g:30:4: ( 'if' )
            # grammar/ShyLexer.g:30:6: 'if'
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

            # grammar/ShyLexer.g:31:8: ( 'indent' )
            # grammar/ShyLexer.g:31:10: 'indent'
            pass 
            self.match("indent")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INDENT"



    # $ANTLR start "MESSAGES"
    def mMESSAGES(self, ):
        try:
            _type = MESSAGES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:32:10: ( 'messages' )
            # grammar/ShyLexer.g:32:12: 'messages'
            pass 
            self.match("messages")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MESSAGES"



    # $ANTLR start "MODULE"
    def mMODULE(self, ):
        try:
            _type = MODULE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:33:8: ( 'module' )
            # grammar/ShyLexer.g:33:10: 'module'
            pass 
            self.match("module")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULE"



    # $ANTLR start "MODULE_QUEUE"
    def mMODULE_QUEUE(self, ):
        try:
            _type = MODULE_QUEUE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:34:14: ( 'module_queue' )
            # grammar/ShyLexer.g:34:16: 'module_queue'
            pass 
            self.match("module_queue")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MODULE_QUEUE"



    # $ANTLR start "OPS"
    def mOPS(self, ):
        try:
            _type = OPS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:35:5: ( 'ops' )
            # grammar/ShyLexer.g:35:7: 'ops'
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

            # grammar/ShyLexer.g:36:7: ( 'paste' )
            # grammar/ShyLexer.g:36:9: 'paste'
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

            # grammar/ShyLexer.g:37:6: ( 'proc' )
            # grammar/ShyLexer.g:37:8: 'proc'
            pass 
            self.match("proc")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PROC"



    # $ANTLR start "RECEIVE"
    def mRECEIVE(self, ):
        try:
            _type = RECEIVE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:38:9: ( 'receive' )
            # grammar/ShyLexer.g:38:11: 'receive'
            pass 
            self.match("receive")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RECEIVE"



    # $ANTLR start "REQUEST"
    def mREQUEST(self, ):
        try:
            _type = REQUEST
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:39:9: ( 'request' )
            # grammar/ShyLexer.g:39:11: 'request'
            pass 
            self.match("request")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REQUEST"



    # $ANTLR start "REPLACE"
    def mREPLACE(self, ):
        try:
            _type = REPLACE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:40:9: ( 'replace' )
            # grammar/ShyLexer.g:40:11: 'replace'
            pass 
            self.match("replace")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REPLACE"



    # $ANTLR start "REPLY"
    def mREPLY(self, ):
        try:
            _type = REPLY
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:41:7: ( 'reply' )
            # grammar/ShyLexer.g:41:9: 'reply'
            pass 
            self.match("reply")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REPLY"



    # $ANTLR start "SEND"
    def mSEND(self, ):
        try:
            _type = SEND
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:42:6: ( 'send' )
            # grammar/ShyLexer.g:42:8: 'send'
            pass 
            self.match("send")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEND"



    # $ANTLR start "STATELESS"
    def mSTATELESS(self, ):
        try:
            _type = STATELESS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:43:11: ( 'stateless' )
            # grammar/ShyLexer.g:43:13: 'stateless'
            pass 
            self.match("stateless")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STATELESS"



    # $ANTLR start "TRACE"
    def mTRACE(self, ):
        try:
            _type = TRACE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:44:7: ( 'trace' )
            # grammar/ShyLexer.g:44:9: 'trace'
            pass 
            self.match("trace")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TRACE"



    # $ANTLR start "TYPES"
    def mTYPES(self, ):
        try:
            _type = TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:45:7: ( 'types' )
            # grammar/ShyLexer.g:45:9: 'types'
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

            # grammar/ShyLexer.g:46:6: ( 'vars' )
            # grammar/ShyLexer.g:46:8: 'vars'
            pass 
            self.match("vars")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VARS"



    # $ANTLR start "WHILE"
    def mWHILE(self, ):
        try:
            _type = WHILE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:47:7: ( 'while' )
            # grammar/ShyLexer.g:47:9: 'while'
            pass 
            self.match("while")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHILE"



    # $ANTLR start "WITH"
    def mWITH(self, ):
        try:
            _type = WITH
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:48:6: ( 'with' )
            # grammar/ShyLexer.g:48:8: 'with'
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

            # grammar/ShyLexer.g:50:12: ( '<-' )
            # grammar/ShyLexer.g:50:14: '<-'
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

            # grammar/ShyLexer.g:51:13: ( '->' )
            # grammar/ShyLexer.g:51:15: '->'
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

            # grammar/ShyLexer.g:52:12: ( '{' )
            # grammar/ShyLexer.g:52:14: '{'
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

            # grammar/ShyLexer.g:53:13: ( '}' )
            # grammar/ShyLexer.g:53:15: '}'
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

            # grammar/ShyLexer.g:54:8: ( '/' )
            # grammar/ShyLexer.g:54:10: '/'
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

            # grammar/ShyLexer.g:55:7: ( '-' )
            # grammar/ShyLexer.g:55:9: '-'
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

            # grammar/ShyLexer.g:56:12: ( '_' )
            # grammar/ShyLexer.g:56:14: '_'
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

            # grammar/ShyLexer.g:57:9: ( '\\n' )
            # grammar/ShyLexer.g:57:11: '\\n'
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

            # grammar/ShyLexer.g:58:4: ( 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )* )
            # grammar/ShyLexer.g:58:6: 'a' .. 'z' ( 'a' .. 'z' | '0' .. '9' | '_' )*
            pass 
            self.matchRange(97, 122)

            # grammar/ShyLexer.g:58:17: ( 'a' .. 'z' | '0' .. '9' | '_' )*
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

            # grammar/ShyLexer.g:59:8: ( ( '0' .. '9' )+ )
            # grammar/ShyLexer.g:59:10: ( '0' .. '9' )+
            pass 
            # grammar/ShyLexer.g:59:10: ( '0' .. '9' )+
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

            # grammar/ShyLexer.g:60:12: ( ( ' ' )+ )
            # grammar/ShyLexer.g:60:14: ( ' ' )+
            pass 
            # grammar/ShyLexer.g:60:14: ( ' ' )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 32) :
                    alt3 = 1


                if alt3 == 1:
                    # grammar/ShyLexer.g:60:14: ' '
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

            # grammar/ShyLexer.g:61:12: ( '[' ( . )* ']' )
            # grammar/ShyLexer.g:61:14: '[' ( . )* ']'
            pass 
            self.match(91)

            # grammar/ShyLexer.g:61:18: ( . )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 93) :
                    alt4 = 2
                elif ((0 <= LA4_0 <= 92) or (94 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
                    # grammar/ShyLexer.g:61:18: .
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

            # grammar/ShyLexer.g:62:8: ( '\\'' ( . )* '\\'' )
            # grammar/ShyLexer.g:62:10: '\\'' ( . )* '\\''
            pass 
            self.match(39)

            # grammar/ShyLexer.g:62:15: ( . )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 39) :
                    alt5 = 2
                elif ((0 <= LA5_0 <= 38) or (40 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # grammar/ShyLexer.g:62:15: .
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

            # grammar/ShyLexer.g:64:22: ( 'TREE_ARBITRARY_TOKEN' )
            # grammar/ShyLexer.g:64:24: 'TREE_ARBITRARY_TOKEN'
            pass 
            self.match("TREE_ARBITRARY_TOKEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_ARBITRARY_TOKEN"



    # $ANTLR start "TREE_ATTR"
    def mTREE_ATTR(self, ):
        try:
            _type = TREE_ATTR
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:65:11: ( 'TREE_ATTR' )
            # grammar/ShyLexer.g:65:13: 'TREE_ATTR'
            pass 
            self.match("TREE_ATTR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_ATTR"



    # $ANTLR start "TREE_ATTR_HINT"
    def mTREE_ATTR_HINT(self, ):
        try:
            _type = TREE_ATTR_HINT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:66:16: ( 'TREE_ATTR_HINT' )
            # grammar/ShyLexer.g:66:18: 'TREE_ATTR_HINT'
            pass 
            self.match("TREE_ATTR_HINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_ATTR_HINT"



    # $ANTLR start "TREE_ATTRS_HINTS"
    def mTREE_ATTRS_HINTS(self, ):
        try:
            _type = TREE_ATTRS_HINTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:67:18: ( 'TREE_ATTRS_HINTS' )
            # grammar/ShyLexer.g:67:20: 'TREE_ATTRS_HINTS'
            pass 
            self.match("TREE_ATTRS_HINTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_ATTRS_HINTS"



    # $ANTLR start "TREE_CONDITION_ALL"
    def mTREE_CONDITION_ALL(self, ):
        try:
            _type = TREE_CONDITION_ALL
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:68:20: ( 'TREE_CONDITION_ALL' )
            # grammar/ShyLexer.g:68:22: 'TREE_CONDITION_ALL'
            pass 
            self.match("TREE_CONDITION_ALL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_CONDITION_ALL"



    # $ANTLR start "TREE_CONDITION_ANY"
    def mTREE_CONDITION_ANY(self, ):
        try:
            _type = TREE_CONDITION_ANY
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:69:20: ( 'TREE_CONDITION_ANY' )
            # grammar/ShyLexer.g:69:22: 'TREE_CONDITION_ANY'
            pass 
            self.match("TREE_CONDITION_ANY")




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

            # grammar/ShyLexer.g:70:13: ( 'TREE_CONSTS' )
            # grammar/ShyLexer.g:70:15: 'TREE_CONSTS'
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

            # grammar/ShyLexer.g:71:11: ( 'TREE_COPY' )
            # grammar/ShyLexer.g:71:13: 'TREE_COPY'
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

            # grammar/ShyLexer.g:72:17: ( 'TREE_COPY_PASTE' )
            # grammar/ShyLexer.g:72:19: 'TREE_COPY_PASTE'
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

            # grammar/ShyLexer.g:73:17: ( 'TREE_EXPRESSION' )
            # grammar/ShyLexer.g:73:19: 'TREE_EXPRESSION'
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

            # grammar/ShyLexer.g:74:11: ( 'TREE_HINT' )
            # grammar/ShyLexer.g:74:13: 'TREE_HINT'
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

            # grammar/ShyLexer.g:75:16: ( 'TREE_HINT_NONE' )
            # grammar/ShyLexer.g:75:18: 'TREE_HINT_NONE'
            pass 
            self.match("TREE_HINT_NONE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_HINT_NONE"



    # $ANTLR start "TREE_LOCAL_VARS"
    def mTREE_LOCAL_VARS(self, ):
        try:
            _type = TREE_LOCAL_VARS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:76:17: ( 'TREE_LOCAL_VARS' )
            # grammar/ShyLexer.g:76:19: 'TREE_LOCAL_VARS'
            pass 
            self.match("TREE_LOCAL_VARS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_LOCAL_VARS"



    # $ANTLR start "TREE_MESSAGES"
    def mTREE_MESSAGES(self, ):
        try:
            _type = TREE_MESSAGES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:77:15: ( 'TREE_MESSAGES' )
            # grammar/ShyLexer.g:77:17: 'TREE_MESSAGES'
            pass 
            self.match("TREE_MESSAGES")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MESSAGES"



    # $ANTLR start "TREE_MESSAGES_ITEM"
    def mTREE_MESSAGES_ITEM(self, ):
        try:
            _type = TREE_MESSAGES_ITEM
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:78:20: ( 'TREE_MESSAGES_ITEM' )
            # grammar/ShyLexer.g:78:22: 'TREE_MESSAGES_ITEM'
            pass 
            self.match("TREE_MESSAGES_ITEM")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MESSAGES_ITEM"



    # $ANTLR start "TREE_MESSAGES_ITEM_RECEIVE"
    def mTREE_MESSAGES_ITEM_RECEIVE(self, ):
        try:
            _type = TREE_MESSAGES_ITEM_RECEIVE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:79:28: ( 'TREE_MESSAGES_ITEM_RECEIVE' )
            # grammar/ShyLexer.g:79:30: 'TREE_MESSAGES_ITEM_RECEIVE'
            pass 
            self.match("TREE_MESSAGES_ITEM_RECEIVE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MESSAGES_ITEM_RECEIVE"



    # $ANTLR start "TREE_MESSAGES_ITEM_REPLY"
    def mTREE_MESSAGES_ITEM_REPLY(self, ):
        try:
            _type = TREE_MESSAGES_ITEM_REPLY
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:80:26: ( 'TREE_MESSAGES_ITEM_REPLY' )
            # grammar/ShyLexer.g:80:28: 'TREE_MESSAGES_ITEM_REPLY'
            pass 
            self.match("TREE_MESSAGES_ITEM_REPLY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MESSAGES_ITEM_REPLY"



    # $ANTLR start "TREE_MESSAGES_ITEM_REQUEST"
    def mTREE_MESSAGES_ITEM_REQUEST(self, ):
        try:
            _type = TREE_MESSAGES_ITEM_REQUEST
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:81:28: ( 'TREE_MESSAGES_ITEM_REQUEST' )
            # grammar/ShyLexer.g:81:30: 'TREE_MESSAGES_ITEM_REQUEST'
            pass 
            self.match("TREE_MESSAGES_ITEM_REQUEST")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MESSAGES_ITEM_REQUEST"



    # $ANTLR start "TREE_MODULE"
    def mTREE_MODULE(self, ):
        try:
            _type = TREE_MODULE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:82:13: ( 'TREE_MODULE' )
            # grammar/ShyLexer.g:82:15: 'TREE_MODULE'
            pass 
            self.match("TREE_MODULE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MODULE"



    # $ANTLR start "TREE_MODULE_QUEUE"
    def mTREE_MODULE_QUEUE(self, ):
        try:
            _type = TREE_MODULE_QUEUE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:83:19: ( 'TREE_MODULE_QUEUE' )
            # grammar/ShyLexer.g:83:21: 'TREE_MODULE_QUEUE'
            pass 
            self.match("TREE_MODULE_QUEUE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_MODULE_QUEUE"



    # $ANTLR start "TREE_NUM_FRACT"
    def mTREE_NUM_FRACT(self, ):
        try:
            _type = TREE_NUM_FRACT
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:84:16: ( 'TREE_NUM_FRACT' )
            # grammar/ShyLexer.g:84:18: 'TREE_NUM_FRACT'
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

            # grammar/ShyLexer.g:85:16: ( 'TREE_NUM_WHOLE' )
            # grammar/ShyLexer.g:85:18: 'TREE_NUM_WHOLE'
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

            # grammar/ShyLexer.g:86:12: ( 'TREE_PASTE' )
            # grammar/ShyLexer.g:86:14: 'TREE_PASTE'
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

            # grammar/ShyLexer.g:87:20: ( 'TREE_PASTE_REPLACE' )
            # grammar/ShyLexer.g:87:22: 'TREE_PASTE_REPLACE'
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

            # grammar/ShyLexer.g:88:17: ( 'TREE_PASTE_WITH' )
            # grammar/ShyLexer.g:88:19: 'TREE_PASTE_WITH'
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

            # grammar/ShyLexer.g:89:11: ( 'TREE_PROC' )
            # grammar/ShyLexer.g:89:13: 'TREE_PROC'
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

            # grammar/ShyLexer.g:90:16: ( 'TREE_PROC_ARGS' )
            # grammar/ShyLexer.g:90:18: 'TREE_PROC_ARGS'
            pass 
            self.match("TREE_PROC_ARGS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_PROC_ARGS"



    # $ANTLR start "TREE_RECEIVE"
    def mTREE_RECEIVE(self, ):
        try:
            _type = TREE_RECEIVE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:91:14: ( 'TREE_RECEIVE' )
            # grammar/ShyLexer.g:91:16: 'TREE_RECEIVE'
            pass 
            self.match("TREE_RECEIVE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_RECEIVE"



    # $ANTLR start "TREE_REQUEST"
    def mTREE_REQUEST(self, ):
        try:
            _type = TREE_REQUEST
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:92:14: ( 'TREE_REQUEST' )
            # grammar/ShyLexer.g:92:16: 'TREE_REQUEST'
            pass 
            self.match("TREE_REQUEST")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_REQUEST"



    # $ANTLR start "TREE_STATELESS"
    def mTREE_STATELESS(self, ):
        try:
            _type = TREE_STATELESS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:93:16: ( 'TREE_STATELESS' )
            # grammar/ShyLexer.g:93:18: 'TREE_STATELESS'
            pass 
            self.match("TREE_STATELESS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATELESS"



    # $ANTLR start "TREE_STATEMENT_ASSIGN"
    def mTREE_STATEMENT_ASSIGN(self, ):
        try:
            _type = TREE_STATEMENT_ASSIGN
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:94:23: ( 'TREE_STATEMENT_ASSIGN' )
            # grammar/ShyLexer.g:94:25: 'TREE_STATEMENT_ASSIGN'
            pass 
            self.match("TREE_STATEMENT_ASSIGN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_ASSIGN"



    # $ANTLR start "TREE_STATEMENT_ASSIGN_TO"
    def mTREE_STATEMENT_ASSIGN_TO(self, ):
        try:
            _type = TREE_STATEMENT_ASSIGN_TO
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:95:26: ( 'TREE_STATEMENT_ASSIGN_TO' )
            # grammar/ShyLexer.g:95:28: 'TREE_STATEMENT_ASSIGN_TO'
            pass 
            self.match("TREE_STATEMENT_ASSIGN_TO")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_ASSIGN_TO"



    # $ANTLR start "TREE_STATEMENT_CALL"
    def mTREE_STATEMENT_CALL(self, ):
        try:
            _type = TREE_STATEMENT_CALL
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:96:21: ( 'TREE_STATEMENT_CALL' )
            # grammar/ShyLexer.g:96:23: 'TREE_STATEMENT_CALL'
            pass 
            self.match("TREE_STATEMENT_CALL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_CALL"



    # $ANTLR start "TREE_STATEMENT_ELIF"
    def mTREE_STATEMENT_ELIF(self, ):
        try:
            _type = TREE_STATEMENT_ELIF
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:97:21: ( 'TREE_STATEMENT_ELIF' )
            # grammar/ShyLexer.g:97:23: 'TREE_STATEMENT_ELIF'
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

            # grammar/ShyLexer.g:98:21: ( 'TREE_STATEMENT_ELSE' )
            # grammar/ShyLexer.g:98:23: 'TREE_STATEMENT_ELSE'
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

            # grammar/ShyLexer.g:99:19: ( 'TREE_STATEMENT_IF' )
            # grammar/ShyLexer.g:99:21: 'TREE_STATEMENT_IF'
            pass 
            self.match("TREE_STATEMENT_IF")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_IF"



    # $ANTLR start "TREE_STATEMENT_SEND"
    def mTREE_STATEMENT_SEND(self, ):
        try:
            _type = TREE_STATEMENT_SEND
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:100:21: ( 'TREE_STATEMENT_SEND' )
            # grammar/ShyLexer.g:100:23: 'TREE_STATEMENT_SEND'
            pass 
            self.match("TREE_STATEMENT_SEND")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_SEND"



    # $ANTLR start "TREE_STATEMENT_WITH"
    def mTREE_STATEMENT_WITH(self, ):
        try:
            _type = TREE_STATEMENT_WITH
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:101:21: ( 'TREE_STATEMENT_WITH' )
            # grammar/ShyLexer.g:101:23: 'TREE_STATEMENT_WITH'
            pass 
            self.match("TREE_STATEMENT_WITH")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_WITH"



    # $ANTLR start "TREE_STATEMENT_WHILE"
    def mTREE_STATEMENT_WHILE(self, ):
        try:
            _type = TREE_STATEMENT_WHILE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:102:22: ( 'TREE_STATEMENT_WHILE' )
            # grammar/ShyLexer.g:102:24: 'TREE_STATEMENT_WHILE'
            pass 
            self.match("TREE_STATEMENT_WHILE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENT_WHILE"



    # $ANTLR start "TREE_STATEMENTS"
    def mTREE_STATEMENTS(self, ):
        try:
            _type = TREE_STATEMENTS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:103:17: ( 'TREE_STATEMENTS' )
            # grammar/ShyLexer.g:103:19: 'TREE_STATEMENTS'
            pass 
            self.match("TREE_STATEMENTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_STATEMENTS"



    # $ANTLR start "TREE_TRACE"
    def mTREE_TRACE(self, ):
        try:
            _type = TREE_TRACE
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:104:12: ( 'TREE_TRACE' )
            # grammar/ShyLexer.g:104:14: 'TREE_TRACE'
            pass 
            self.match("TREE_TRACE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TRACE"



    # $ANTLR start "TREE_TYPES"
    def mTREE_TYPES(self, ):
        try:
            _type = TREE_TYPES
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:105:12: ( 'TREE_TYPES' )
            # grammar/ShyLexer.g:105:14: 'TREE_TYPES'
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

            # grammar/ShyLexer.g:106:17: ( 'TREE_TYPES_ITEM' )
            # grammar/ShyLexer.g:106:19: 'TREE_TYPES_ITEM'
            pass 
            self.match("TREE_TYPES_ITEM")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_TYPES_ITEM"



    # $ANTLR start "TREE_VARS"
    def mTREE_VARS(self, ):
        try:
            _type = TREE_VARS
            _channel = DEFAULT_CHANNEL

            # grammar/ShyLexer.g:107:11: ( 'TREE_VARS' )
            # grammar/ShyLexer.g:107:13: 'TREE_VARS'
            pass 
            self.match("TREE_VARS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TREE_VARS"



    def mTokens(self):
        # grammar/ShyLexer.g:1:8: ( ALL | ANY | ARGS | CONSTS | COPY | DEDENT | DO | ELIF | ELSE | IF | INDENT | MESSAGES | MODULE | MODULE_QUEUE | OPS | PASTE | PROC | RECEIVE | REQUEST | REPLACE | REPLY | SEND | STATELESS | TRACE | TYPES | VARS | WHILE | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | WHITESPACE | EXPRESSION | STRING | TREE_ARBITRARY_TOKEN | TREE_ATTR | TREE_ATTR_HINT | TREE_ATTRS_HINTS | TREE_CONDITION_ALL | TREE_CONDITION_ANY | TREE_CONSTS | TREE_COPY | TREE_COPY_PASTE | TREE_EXPRESSION | TREE_HINT | TREE_HINT_NONE | TREE_LOCAL_VARS | TREE_MESSAGES | TREE_MESSAGES_ITEM | TREE_MESSAGES_ITEM_RECEIVE | TREE_MESSAGES_ITEM_REPLY | TREE_MESSAGES_ITEM_REQUEST | TREE_MODULE | TREE_MODULE_QUEUE | TREE_NUM_FRACT | TREE_NUM_WHOLE | TREE_PASTE | TREE_PASTE_REPLACE | TREE_PASTE_WITH | TREE_PROC | TREE_PROC_ARGS | TREE_RECEIVE | TREE_REQUEST | TREE_STATELESS | TREE_STATEMENT_ASSIGN | TREE_STATEMENT_ASSIGN_TO | TREE_STATEMENT_CALL | TREE_STATEMENT_ELIF | TREE_STATEMENT_ELSE | TREE_STATEMENT_IF | TREE_STATEMENT_SEND | TREE_STATEMENT_WITH | TREE_STATEMENT_WHILE | TREE_STATEMENTS | TREE_TRACE | TREE_TYPES | TREE_TYPES_ITEM | TREE_VARS )
        alt6 = 85
        alt6 = self.dfa6.predict(self.input)
        if alt6 == 1:
            # grammar/ShyLexer.g:1:10: ALL
            pass 
            self.mALL()



        elif alt6 == 2:
            # grammar/ShyLexer.g:1:14: ANY
            pass 
            self.mANY()



        elif alt6 == 3:
            # grammar/ShyLexer.g:1:18: ARGS
            pass 
            self.mARGS()



        elif alt6 == 4:
            # grammar/ShyLexer.g:1:23: CONSTS
            pass 
            self.mCONSTS()



        elif alt6 == 5:
            # grammar/ShyLexer.g:1:30: COPY
            pass 
            self.mCOPY()



        elif alt6 == 6:
            # grammar/ShyLexer.g:1:35: DEDENT
            pass 
            self.mDEDENT()



        elif alt6 == 7:
            # grammar/ShyLexer.g:1:42: DO
            pass 
            self.mDO()



        elif alt6 == 8:
            # grammar/ShyLexer.g:1:45: ELIF
            pass 
            self.mELIF()



        elif alt6 == 9:
            # grammar/ShyLexer.g:1:50: ELSE
            pass 
            self.mELSE()



        elif alt6 == 10:
            # grammar/ShyLexer.g:1:55: IF
            pass 
            self.mIF()



        elif alt6 == 11:
            # grammar/ShyLexer.g:1:58: INDENT
            pass 
            self.mINDENT()



        elif alt6 == 12:
            # grammar/ShyLexer.g:1:65: MESSAGES
            pass 
            self.mMESSAGES()



        elif alt6 == 13:
            # grammar/ShyLexer.g:1:74: MODULE
            pass 
            self.mMODULE()



        elif alt6 == 14:
            # grammar/ShyLexer.g:1:81: MODULE_QUEUE
            pass 
            self.mMODULE_QUEUE()



        elif alt6 == 15:
            # grammar/ShyLexer.g:1:94: OPS
            pass 
            self.mOPS()



        elif alt6 == 16:
            # grammar/ShyLexer.g:1:98: PASTE
            pass 
            self.mPASTE()



        elif alt6 == 17:
            # grammar/ShyLexer.g:1:104: PROC
            pass 
            self.mPROC()



        elif alt6 == 18:
            # grammar/ShyLexer.g:1:109: RECEIVE
            pass 
            self.mRECEIVE()



        elif alt6 == 19:
            # grammar/ShyLexer.g:1:117: REQUEST
            pass 
            self.mREQUEST()



        elif alt6 == 20:
            # grammar/ShyLexer.g:1:125: REPLACE
            pass 
            self.mREPLACE()



        elif alt6 == 21:
            # grammar/ShyLexer.g:1:133: REPLY
            pass 
            self.mREPLY()



        elif alt6 == 22:
            # grammar/ShyLexer.g:1:139: SEND
            pass 
            self.mSEND()



        elif alt6 == 23:
            # grammar/ShyLexer.g:1:144: STATELESS
            pass 
            self.mSTATELESS()



        elif alt6 == 24:
            # grammar/ShyLexer.g:1:154: TRACE
            pass 
            self.mTRACE()



        elif alt6 == 25:
            # grammar/ShyLexer.g:1:160: TYPES
            pass 
            self.mTYPES()



        elif alt6 == 26:
            # grammar/ShyLexer.g:1:166: VARS
            pass 
            self.mVARS()



        elif alt6 == 27:
            # grammar/ShyLexer.g:1:171: WHILE
            pass 
            self.mWHILE()



        elif alt6 == 28:
            # grammar/ShyLexer.g:1:177: WITH
            pass 
            self.mWITH()



        elif alt6 == 29:
            # grammar/ShyLexer.g:1:182: ARROW_LEFT
            pass 
            self.mARROW_LEFT()



        elif alt6 == 30:
            # grammar/ShyLexer.g:1:193: ARROW_RIGHT
            pass 
            self.mARROW_RIGHT()



        elif alt6 == 31:
            # grammar/ShyLexer.g:1:205: CURLY_OPEN
            pass 
            self.mCURLY_OPEN()



        elif alt6 == 32:
            # grammar/ShyLexer.g:1:216: CURLY_CLOSE
            pass 
            self.mCURLY_CLOSE()



        elif alt6 == 33:
            # grammar/ShyLexer.g:1:228: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt6 == 34:
            # grammar/ShyLexer.g:1:235: MINUS
            pass 
            self.mMINUS()



        elif alt6 == 35:
            # grammar/ShyLexer.g:1:241: UNDERSCORE
            pass 
            self.mUNDERSCORE()



        elif alt6 == 36:
            # grammar/ShyLexer.g:1:252: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt6 == 37:
            # grammar/ShyLexer.g:1:260: ID
            pass 
            self.mID()



        elif alt6 == 38:
            # grammar/ShyLexer.g:1:263: NUMBER
            pass 
            self.mNUMBER()



        elif alt6 == 39:
            # grammar/ShyLexer.g:1:270: WHITESPACE
            pass 
            self.mWHITESPACE()



        elif alt6 == 40:
            # grammar/ShyLexer.g:1:281: EXPRESSION
            pass 
            self.mEXPRESSION()



        elif alt6 == 41:
            # grammar/ShyLexer.g:1:292: STRING
            pass 
            self.mSTRING()



        elif alt6 == 42:
            # grammar/ShyLexer.g:1:299: TREE_ARBITRARY_TOKEN
            pass 
            self.mTREE_ARBITRARY_TOKEN()



        elif alt6 == 43:
            # grammar/ShyLexer.g:1:320: TREE_ATTR
            pass 
            self.mTREE_ATTR()



        elif alt6 == 44:
            # grammar/ShyLexer.g:1:330: TREE_ATTR_HINT
            pass 
            self.mTREE_ATTR_HINT()



        elif alt6 == 45:
            # grammar/ShyLexer.g:1:345: TREE_ATTRS_HINTS
            pass 
            self.mTREE_ATTRS_HINTS()



        elif alt6 == 46:
            # grammar/ShyLexer.g:1:362: TREE_CONDITION_ALL
            pass 
            self.mTREE_CONDITION_ALL()



        elif alt6 == 47:
            # grammar/ShyLexer.g:1:381: TREE_CONDITION_ANY
            pass 
            self.mTREE_CONDITION_ANY()



        elif alt6 == 48:
            # grammar/ShyLexer.g:1:400: TREE_CONSTS
            pass 
            self.mTREE_CONSTS()



        elif alt6 == 49:
            # grammar/ShyLexer.g:1:412: TREE_COPY
            pass 
            self.mTREE_COPY()



        elif alt6 == 50:
            # grammar/ShyLexer.g:1:422: TREE_COPY_PASTE
            pass 
            self.mTREE_COPY_PASTE()



        elif alt6 == 51:
            # grammar/ShyLexer.g:1:438: TREE_EXPRESSION
            pass 
            self.mTREE_EXPRESSION()



        elif alt6 == 52:
            # grammar/ShyLexer.g:1:454: TREE_HINT
            pass 
            self.mTREE_HINT()



        elif alt6 == 53:
            # grammar/ShyLexer.g:1:464: TREE_HINT_NONE
            pass 
            self.mTREE_HINT_NONE()



        elif alt6 == 54:
            # grammar/ShyLexer.g:1:479: TREE_LOCAL_VARS
            pass 
            self.mTREE_LOCAL_VARS()



        elif alt6 == 55:
            # grammar/ShyLexer.g:1:495: TREE_MESSAGES
            pass 
            self.mTREE_MESSAGES()



        elif alt6 == 56:
            # grammar/ShyLexer.g:1:509: TREE_MESSAGES_ITEM
            pass 
            self.mTREE_MESSAGES_ITEM()



        elif alt6 == 57:
            # grammar/ShyLexer.g:1:528: TREE_MESSAGES_ITEM_RECEIVE
            pass 
            self.mTREE_MESSAGES_ITEM_RECEIVE()



        elif alt6 == 58:
            # grammar/ShyLexer.g:1:555: TREE_MESSAGES_ITEM_REPLY
            pass 
            self.mTREE_MESSAGES_ITEM_REPLY()



        elif alt6 == 59:
            # grammar/ShyLexer.g:1:580: TREE_MESSAGES_ITEM_REQUEST
            pass 
            self.mTREE_MESSAGES_ITEM_REQUEST()



        elif alt6 == 60:
            # grammar/ShyLexer.g:1:607: TREE_MODULE
            pass 
            self.mTREE_MODULE()



        elif alt6 == 61:
            # grammar/ShyLexer.g:1:619: TREE_MODULE_QUEUE
            pass 
            self.mTREE_MODULE_QUEUE()



        elif alt6 == 62:
            # grammar/ShyLexer.g:1:637: TREE_NUM_FRACT
            pass 
            self.mTREE_NUM_FRACT()



        elif alt6 == 63:
            # grammar/ShyLexer.g:1:652: TREE_NUM_WHOLE
            pass 
            self.mTREE_NUM_WHOLE()



        elif alt6 == 64:
            # grammar/ShyLexer.g:1:667: TREE_PASTE
            pass 
            self.mTREE_PASTE()



        elif alt6 == 65:
            # grammar/ShyLexer.g:1:678: TREE_PASTE_REPLACE
            pass 
            self.mTREE_PASTE_REPLACE()



        elif alt6 == 66:
            # grammar/ShyLexer.g:1:697: TREE_PASTE_WITH
            pass 
            self.mTREE_PASTE_WITH()



        elif alt6 == 67:
            # grammar/ShyLexer.g:1:713: TREE_PROC
            pass 
            self.mTREE_PROC()



        elif alt6 == 68:
            # grammar/ShyLexer.g:1:723: TREE_PROC_ARGS
            pass 
            self.mTREE_PROC_ARGS()



        elif alt6 == 69:
            # grammar/ShyLexer.g:1:738: TREE_RECEIVE
            pass 
            self.mTREE_RECEIVE()



        elif alt6 == 70:
            # grammar/ShyLexer.g:1:751: TREE_REQUEST
            pass 
            self.mTREE_REQUEST()



        elif alt6 == 71:
            # grammar/ShyLexer.g:1:764: TREE_STATELESS
            pass 
            self.mTREE_STATELESS()



        elif alt6 == 72:
            # grammar/ShyLexer.g:1:779: TREE_STATEMENT_ASSIGN
            pass 
            self.mTREE_STATEMENT_ASSIGN()



        elif alt6 == 73:
            # grammar/ShyLexer.g:1:801: TREE_STATEMENT_ASSIGN_TO
            pass 
            self.mTREE_STATEMENT_ASSIGN_TO()



        elif alt6 == 74:
            # grammar/ShyLexer.g:1:826: TREE_STATEMENT_CALL
            pass 
            self.mTREE_STATEMENT_CALL()



        elif alt6 == 75:
            # grammar/ShyLexer.g:1:846: TREE_STATEMENT_ELIF
            pass 
            self.mTREE_STATEMENT_ELIF()



        elif alt6 == 76:
            # grammar/ShyLexer.g:1:866: TREE_STATEMENT_ELSE
            pass 
            self.mTREE_STATEMENT_ELSE()



        elif alt6 == 77:
            # grammar/ShyLexer.g:1:886: TREE_STATEMENT_IF
            pass 
            self.mTREE_STATEMENT_IF()



        elif alt6 == 78:
            # grammar/ShyLexer.g:1:904: TREE_STATEMENT_SEND
            pass 
            self.mTREE_STATEMENT_SEND()



        elif alt6 == 79:
            # grammar/ShyLexer.g:1:924: TREE_STATEMENT_WITH
            pass 
            self.mTREE_STATEMENT_WITH()



        elif alt6 == 80:
            # grammar/ShyLexer.g:1:944: TREE_STATEMENT_WHILE
            pass 
            self.mTREE_STATEMENT_WHILE()



        elif alt6 == 81:
            # grammar/ShyLexer.g:1:965: TREE_STATEMENTS
            pass 
            self.mTREE_STATEMENTS()



        elif alt6 == 82:
            # grammar/ShyLexer.g:1:981: TREE_TRACE
            pass 
            self.mTREE_TRACE()



        elif alt6 == 83:
            # grammar/ShyLexer.g:1:992: TREE_TYPES
            pass 
            self.mTREE_TYPES()



        elif alt6 == 84:
            # grammar/ShyLexer.g:1:1003: TREE_TYPES_ITEM
            pass 
            self.mTREE_TYPES_ITEM()



        elif alt6 == 85:
            # grammar/ShyLexer.g:1:1019: TREE_VARS
            pass 
            self.mTREE_VARS()








    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\uffff\15\25\1\uffff\1\62\13\uffff\5\25\1\72\1\25\1\75\16\25"
        u"\3\uffff\1\117\1\120\4\25\1\uffff\2\25\1\uffff\3\25\1\132\14\25"
        u"\3\uffff\1\150\1\25\1\152\1\25\1\154\1\155\3\25\1\uffff\1\25\1"
        u"\162\3\25\1\167\3\25\1\173\1\25\1\175\2\uffff\1\25\1\uffff\1\25"
        u"\2\uffff\3\25\1\u0084\1\uffff\3\25\1\u0088\1\uffff\1\25\1\u008a"
        u"\1\u008b\1\uffff\1\u008c\2\uffff\1\u0099\1\u009a\1\u009b\1\25\1"
        u"\u009e\1\uffff\3\25\1\uffff\1\25\22\uffff\2\25\1\uffff\1\u00b2"
        u"\1\u00b3\1\u00b4\1\25\15\uffff\1\u00c3\1\25\3\uffff\1\25\16\uffff"
        u"\1\25\1\u00d3\1\u00d6\2\uffff\1\u00d9\1\u00db\4\uffff\1\u00e2\2"
        u"\uffff\1\25\15\uffff\1\u00ea\3\uffff\1\u00ee\1\25\2\uffff\1\u00f3"
        u"\6\uffff\1\u00f7\11\uffff\1\u00fd\30\uffff\1\u0117\11\uffff\1\u0121"
        u"\5\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\u0122\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\1\12\1\154\1\157\1\145\1\154\1\146\1\145\1\160\1\141\2\145\1\162"
        u"\1\141\1\150\1\uffff\1\76\12\uffff\1\122\1\154\1\171\1\147\1\156"
        u"\1\144\1\60\1\151\1\60\1\144\1\163\1\144\2\163\1\157\1\143\1\156"
        u"\2\141\1\160\1\162\1\151\1\164\2\uffff\1\105\2\60\2\163\1\171\1"
        u"\145\1\uffff\1\146\1\145\1\uffff\1\145\1\163\1\165\1\60\1\164\1"
        u"\143\1\145\1\165\1\154\1\144\1\164\1\143\1\145\1\163\1\154\1\150"
        u"\1\105\2\uffff\1\60\1\164\1\60\1\156\2\60\1\156\1\141\1\154\1\uffff"
        u"\1\145\1\60\1\151\1\145\1\141\1\60\2\145\1\163\1\60\1\145\1\60"
        u"\1\137\1\uffff\1\163\1\uffff\1\164\2\uffff\1\164\1\147\1\145\1"
        u"\60\1\uffff\1\166\1\163\1\143\1\60\1\uffff\1\154\2\60\1\uffff\1"
        u"\60\1\uffff\1\101\3\60\1\145\1\60\1\uffff\1\145\1\164\1\145\1\uffff"
        u"\1\145\3\uffff\1\122\1\117\1\uffff\1\111\1\uffff\1\105\1\125\1"
        u"\101\1\105\1\124\1\122\4\uffff\1\163\1\161\1\uffff\3\60\1\163\1"
        u"\uffff\1\124\2\116\1\123\1\104\1\115\1\123\1\117\1\103\1\101\1"
        u"\uffff\1\120\1\60\1\165\3\uffff\1\163\1\122\1\104\1\131\1\124\1"
        u"\123\1\125\1\137\1\124\1\103\2\uffff\1\124\1\105\1\uffff\1\145"
        u"\1\60\1\123\1\111\1\uffff\2\137\1\101\1\114\1\106\1\105\1\137\1"
        u"\105\1\123\1\165\4\uffff\1\124\4\uffff\1\107\1\105\2\uffff\1\137"
        u"\2\uffff\1\114\1\137\1\145\1\111\1\105\1\137\1\122\2\uffff\1\105"
        u"\2\uffff\1\60\1\117\1\123\4\uffff\1\116\1\uffff\1\116\1\137\1\124"
        u"\1\137\1\111\1\uffff\1\123\1\101\1\124\1\101\1\uffff\1\114\1\105"
        u"\1\123\1\uffff\1\114\2\uffff\1\110\2\uffff\1\115\1\123\1\111\2"
        u"\uffff\1\137\1\111\2\uffff\1\122\1\uffff\1\107\1\105\1\116\1\103"
        u"\1\137\5\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\1\175\1\162\2\157\1\154\1\156\1\157\1\160\1\162\1\145\1\164\1"
        u"\171\1\141\1\151\1\uffff\1\76\12\uffff\1\122\1\154\1\171\1\147"
        u"\1\160\1\144\1\172\1\163\1\172\1\144\1\163\1\144\2\163\1\157\1"
        u"\161\1\156\2\141\1\160\1\162\1\151\1\164\2\uffff\1\105\2\172\2"
        u"\163\1\171\1\145\1\uffff\1\146\1\145\1\uffff\1\145\1\163\1\165"
        u"\1\172\1\164\1\143\1\145\1\165\1\154\1\144\1\164\1\143\1\145\1"
        u"\163\1\154\1\150\1\105\2\uffff\1\172\1\164\1\172\1\156\2\172\1"
        u"\156\1\141\1\154\1\uffff\1\145\1\172\1\151\1\145\1\171\1\172\2"
        u"\145\1\163\1\172\1\145\1\172\1\137\1\uffff\1\163\1\uffff\1\164"
        u"\2\uffff\1\164\1\147\1\145\1\172\1\uffff\1\166\1\163\1\143\1\172"
        u"\1\uffff\1\154\2\172\1\uffff\1\172\1\uffff\1\126\3\172\1\145\1"
        u"\172\1\uffff\1\145\1\164\1\145\1\uffff\1\145\3\uffff\1\124\1\117"
        u"\1\uffff\1\111\1\uffff\1\117\1\125\1\122\1\105\1\124\1\131\4\uffff"
        u"\1\163\1\161\1\uffff\3\172\1\163\1\uffff\1\124\1\120\1\116\1\123"
        u"\1\104\1\115\1\123\1\117\1\121\1\101\1\uffff\1\120\1\172\1\165"
        u"\3\uffff\1\163\1\122\1\123\1\131\1\124\1\123\1\125\1\137\1\124"
        u"\1\103\2\uffff\1\124\1\105\1\uffff\1\145\1\172\1\137\1\111\1\uffff"
        u"\2\137\1\101\1\114\1\127\1\105\1\137\1\105\1\123\1\165\4\uffff"
        u"\1\124\4\uffff\1\107\1\105\2\uffff\1\137\2\uffff\1\115\1\137\1"
        u"\145\1\111\1\105\1\137\1\127\2\uffff\1\105\2\uffff\1\172\1\117"
        u"\1\123\4\uffff\1\116\1\uffff\1\116\1\137\1\124\1\137\1\111\1\uffff"
        u"\1\137\1\101\1\124\1\127\1\uffff\1\116\1\105\1\123\1\uffff\1\114"
        u"\2\uffff\1\111\2\uffff\1\115\2\123\2\uffff\1\137\1\111\2\uffff"
        u"\1\122\1\uffff\1\107\1\105\1\116\1\121\1\137\5\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\16\uffff\1\35\1\uffff\1\37\1\40\1\41\1\43\1\44\1\45\1\46\1\47"
        u"\1\50\1\51\27\uffff\1\36\1\42\7\uffff\1\7\2\uffff\1\12\21\uffff"
        u"\1\1\1\2\11\uffff\1\17\15\uffff\1\3\1\uffff\1\5\1\uffff\1\10\1"
        u"\11\4\uffff\1\21\4\uffff\1\26\3\uffff\1\32\1\uffff\1\34\6\uffff"
        u"\1\20\3\uffff\1\25\1\uffff\1\30\1\31\1\33\2\uffff\1\63\1\uffff"
        u"\1\66\6\uffff\1\125\1\4\1\6\1\13\2\uffff\1\15\4\uffff\1\52\12\uffff"
        u"\1\122\3\uffff\1\22\1\23\1\24\12\uffff\1\105\1\106\2\uffff\1\14"
        u"\4\uffff\1\60\12\uffff\1\27\1\54\1\55\1\53\1\uffff\1\62\1\61\1"
        u"\65\1\64\2\uffff\1\76\1\77\1\uffff\1\104\1\103\7\uffff\1\100\1"
        u"\107\1\uffff\1\124\1\123\3\uffff\1\75\1\74\1\101\1\102\1\uffff"
        u"\1\16\5\uffff\1\67\4\uffff\1\121\3\uffff\1\112\1\uffff\1\115\1"
        u"\116\1\uffff\1\56\1\57\3\uffff\1\117\1\120\2\uffff\1\113\1\114"
        u"\1\uffff\1\70\5\uffff\1\71\1\72\1\73\1\111\1\110"
        )

    DFA6_special = DFA.unpack(
        u"\u0122\uffff"
        )


    DFA6_transition = [
        DFA.unpack(u"\1\24\25\uffff\1\27\6\uffff\1\31\5\uffff\1\17\1\uffff"
        u"\1\22\12\26\2\uffff\1\16\27\uffff\1\32\6\uffff\1\30\3\uffff\1\23"
        u"\1\uffff\1\1\1\25\1\2\1\3\1\4\3\25\1\5\3\25\1\6\1\25\1\7\1\10\1"
        u"\25\1\11\1\12\1\13\1\25\1\14\1\15\3\25\1\20\1\uffff\1\21"),
        DFA.unpack(u"\1\33\1\uffff\1\34\3\uffff\1\35"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\37\11\uffff\1\40"),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42\7\uffff\1\43"),
        DFA.unpack(u"\1\44\11\uffff\1\45"),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47\20\uffff\1\50"),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52\16\uffff\1\53"),
        DFA.unpack(u"\1\54\6\uffff\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\57\1\60"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61"),
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
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67\1\uffff\1\70"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\73\11\uffff\1\74"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104\14\uffff\1\106\1\105"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\131"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\137"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\156"),
        DFA.unpack(u"\1\157"),
        DFA.unpack(u"\1\160"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\163"),
        DFA.unpack(u"\1\164"),
        DFA.unpack(u"\1\165\27\uffff\1\166"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u008d\1\uffff\1\u008e\1\uffff\1\u008f\2\uffff\1"
        u"\u0090\3\uffff\1\u0091\1\u0092\1\u0093\1\uffff\1\u0094\1\uffff"
        u"\1\u0095\1\u0096\1\u0097\1\uffff\1\u0098"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\12\25\45\uffff\1\u009d\1\uffff\32\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a3\1\uffff\1\u00a4"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a7\11\uffff\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa\20\uffff\1\u00ab"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae\6\uffff\1\u00af"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7\1\uffff\1\u00b8"),
        DFA.unpack(u"\1\u00b9"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\1\u00bb"),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf\15\uffff\1\u00c0"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c5"),
        DFA.unpack(u"\1\u00c6"),
        DFA.unpack(u"\1\u00c7\16\uffff\1\u00c8"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u"\1\u00ca"),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\1\u00ce"),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\u00d5\13\uffff\1\u00d4"),
        DFA.unpack(u"\1\u00d7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00d8"),
        DFA.unpack(u"\1\u00da"),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\1\u00dd"),
        DFA.unpack(u"\1\u00de\20\uffff\1\u00df"),
        DFA.unpack(u"\1\u00e0"),
        DFA.unpack(u"\1\u00e1"),
        DFA.unpack(u"\1\u00e3"),
        DFA.unpack(u"\1\u00e4"),
        DFA.unpack(u"\1\u00e5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e7"),
        DFA.unpack(u"\1\u00e8"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00e9"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00eb\1\u00ec"),
        DFA.unpack(u"\1\u00ed"),
        DFA.unpack(u"\1\u00ef"),
        DFA.unpack(u"\1\u00f0"),
        DFA.unpack(u"\1\u00f1"),
        DFA.unpack(u"\1\u00f2"),
        DFA.unpack(u"\1\u00f4\4\uffff\1\u00f5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\25\45\uffff\1\25\1\uffff\32\25"),
        DFA.unpack(u"\1\u00f8"),
        DFA.unpack(u"\1\u00f9"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fa"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fb"),
        DFA.unpack(u"\1\u00fc"),
        DFA.unpack(u"\1\u00fe"),
        DFA.unpack(u"\1\u00ff"),
        DFA.unpack(u"\1\u0100"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0102\13\uffff\1\u0101"),
        DFA.unpack(u"\1\u0103"),
        DFA.unpack(u"\1\u0104"),
        DFA.unpack(u"\1\u0105\1\uffff\1\u0106\1\uffff\1\u0107\3\uffff\1"
        u"\u0108\11\uffff\1\u0109\3\uffff\1\u010a"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u010b\1\uffff\1\u010c"),
        DFA.unpack(u"\1\u010d"),
        DFA.unpack(u"\1\u010e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u010f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0111\1\u0110"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0112"),
        DFA.unpack(u"\1\u0113"),
        DFA.unpack(u"\1\u0114\11\uffff\1\u0115"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0116"),
        DFA.unpack(u"\1\u0118"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0119"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u011a"),
        DFA.unpack(u"\1\u011b"),
        DFA.unpack(u"\1\u011c"),
        DFA.unpack(u"\1\u011d\14\uffff\1\u011e\1\u011f"),
        DFA.unpack(u"\1\u0120"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
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