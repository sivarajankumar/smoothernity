# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-10 19:37:32

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset


from utils import merge
from fractions import Fraction



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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "RECEIVE", "REPLACE", "REPLY", 
    "REQUEST", "SEND", "STATELESS", "STRING", "TRACE", "TREE_ARBITRARY_TOKEN", 
    "TREE_ATTR", "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", "TREE_CONDITION_ALL", 
    "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_LOCAL_VARS", 
    "TREE_MESSAGES", "TREE_MESSAGES_ITEM", "TREE_MESSAGES_ITEM_RECEIVE", 
    "TREE_MESSAGES_ITEM_REPLY", "TREE_MESSAGES_ITEM_REQUEST", "TREE_MODULE", 
    "TREE_MODULE_QUEUE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_PASTE", 
    "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", "TREE_PROC_ARGS", 
    "TREE_RECEIVE", "TREE_REQUEST", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", "TREE_STATEMENT_CALL", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_SEND", 
    "TREE_STATEMENT_WHILE", "TREE_STATEMENT_WITH", "TREE_TRACE", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", "UNDERSCORE", "VARS", "WHILE", 
    "WHITESPACE", "WITH"
]




class ShyRecognizerBackend(TreeParser):
    grammarFileName = "grammar/ShyRecognizerBackend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerBackend, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # grammar/ShyRecognizerBackend.g:16:1: start returns [ value ] : ( module | stateless | trace | consts | types | messages | vars )* ;
    def start(self, ):
        value = None


        module1 = None

        stateless2 = None

        trace3 = None

        consts4 = None

        types5 = None

        messages6 = None

        vars7 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:19:5: ( ( module | stateless | trace | consts | types | messages | vars )* )
                # grammar/ShyRecognizerBackend.g:19:9: ( module | stateless | trace | consts | types | messages | vars )*
                pass 
                # grammar/ShyRecognizerBackend.g:19:9: ( module | stateless | trace | consts | types | messages | vars )*
                while True: #loop1
                    alt1 = 8
                    LA1 = self.input.LA(1)
                    if LA1 == TREE_MODULE:
                        alt1 = 1
                    elif LA1 == TREE_STATELESS:
                        alt1 = 2
                    elif LA1 == TREE_TRACE:
                        alt1 = 3
                    elif LA1 == TREE_CONSTS:
                        alt1 = 4
                    elif LA1 == TREE_TYPES:
                        alt1 = 5
                    elif LA1 == TREE_MESSAGES:
                        alt1 = 6
                    elif LA1 == TREE_VARS:
                        alt1 = 7

                    if alt1 == 1:
                        # grammar/ShyRecognizerBackend.g:19:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start87)
                        module1 = self.module()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'module' :
                            { ((module1 is not None) and [module1.title] or [None])[0] : ((module1 is not None) and [module1.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 2:
                        # grammar/ShyRecognizerBackend.g:24:11: stateless
                        pass 
                        self._state.following.append(self.FOLLOW_stateless_in_start114)
                        stateless2 = self.stateless()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'stateless' :
                            { ((stateless2 is not None) and [stateless2.title] or [None])[0] : ((stateless2 is not None) and [stateless2.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 3:
                        # grammar/ShyRecognizerBackend.g:29:11: trace
                        pass 
                        self._state.following.append(self.FOLLOW_trace_in_start141)
                        trace3 = self.trace()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'trace' :
                            { ((trace3 is not None) and [trace3.title] or [None])[0] : ((trace3 is not None) and [trace3.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 4:
                        # grammar/ShyRecognizerBackend.g:34:11: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start168)
                        consts4 = self.consts()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'consts' :
                            { ((consts4 is not None) and [consts4.title] or [None])[0] : ((consts4 is not None) and [consts4.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 5:
                        # grammar/ShyRecognizerBackend.g:39:11: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start194)
                        types5 = self.types()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'types' :
                            { ((types5 is not None) and [types5.title] or [None])[0] : ((types5 is not None) and [types5.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 6:
                        # grammar/ShyRecognizerBackend.g:44:11: messages
                        pass 
                        self._state.following.append(self.FOLLOW_messages_in_start220)
                        messages6 = self.messages()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'messages' :
                            { ((messages6 is not None) and [messages6.title] or [None])[0] : ((messages6 is not None) and [messages6.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 7:
                        # grammar/ShyRecognizerBackend.g:49:11: vars
                        pass 
                        self._state.following.append(self.FOLLOW_vars_in_start246)
                        vars7 = self.vars()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'vars' :
                            { ((vars7 is not None) and [vars7.title] or [None])[0] : ((vars7 is not None) and [vars7.content] or [None])[0] } } )
                                    
                        #action end



                    else:
                        break #loop1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "start"


    class trace_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.trace_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "trace"
    # grammar/ShyRecognizerBackend.g:57:1: trace returns [ title , content ] : ^( TREE_TRACE ID ( trace_item )* ) ;
    def trace(self, ):
        retval = self.trace_return()
        retval.start = self.input.LT(1)


        ID8 = None
        trace_item9 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:59:5: ( ^( TREE_TRACE ID ( trace_item )* ) )
                # grammar/ShyRecognizerBackend.g:59:9: ^( TREE_TRACE ID ( trace_item )* )
                pass 
                self.match(self.input, TREE_TRACE, self.FOLLOW_TREE_TRACE_in_trace301)

                self.match(self.input, DOWN, None)
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_trace303)

                #action start
                retval.title , retval.content = ID8.text , dict ( ) 
                #action end


                # grammar/ShyRecognizerBackend.g:61:13: ( trace_item )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == TREE_PROC) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyRecognizerBackend.g:61:15: trace_item
                        pass 
                        self._state.following.append(self.FOLLOW_trace_item_in_trace333)
                        trace_item9 = self.trace_item()

                        self._state.following.pop()

                        #action start
                        retval.content = merge ( retval.content , trace_item9 ) 
                        #action end



                    else:
                        break #loop2


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "trace"



    # $ANTLR start "trace_item"
    # grammar/ShyRecognizerBackend.g:67:1: trace_item returns [ value ] : proc ;
    def trace_item(self, ):
        value = None


        proc10 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:69:5: ( proc )
                # grammar/ShyRecognizerBackend.g:69:9: proc
                pass 
                self._state.following.append(self.FOLLOW_proc_in_trace_item404)
                proc10 = self.proc()

                self._state.following.pop()

                #action start
                value = { 'proc' : { ((proc10 is not None) and [proc10.title] or [None])[0] : ((proc10 is not None) and [proc10.content] or [None])[0] } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "trace_item"


    class stateless_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.stateless_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "stateless"
    # grammar/ShyRecognizerBackend.g:73:1: stateless returns [ title , content ] : ^( TREE_STATELESS ID ( stateless_item )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID11 = None
        stateless_item12 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:75:5: ( ^( TREE_STATELESS ID ( stateless_item )* ) )
                # grammar/ShyRecognizerBackend.g:75:9: ^( TREE_STATELESS ID ( stateless_item )* )
                pass 
                self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless447)

                self.match(self.input, DOWN, None)
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless449)

                #action start
                retval.title , retval.content = ID11.text , dict ( ) 
                #action end


                # grammar/ShyRecognizerBackend.g:77:13: ( stateless_item )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == TREE_PROC) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyRecognizerBackend.g:77:15: stateless_item
                        pass 
                        self._state.following.append(self.FOLLOW_stateless_item_in_stateless479)
                        stateless_item12 = self.stateless_item()

                        self._state.following.pop()

                        #action start
                        retval.content = merge ( retval.content , stateless_item12 ) 
                        #action end



                    else:
                        break #loop3


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "stateless_item"
    # grammar/ShyRecognizerBackend.g:83:1: stateless_item returns [ value ] : proc ;
    def stateless_item(self, ):
        value = None


        proc13 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:85:5: ( proc )
                # grammar/ShyRecognizerBackend.g:85:9: proc
                pass 
                self._state.following.append(self.FOLLOW_proc_in_stateless_item550)
                proc13 = self.proc()

                self._state.following.pop()

                #action start
                value = { 'proc' : { ((proc13 is not None) and [proc13.title] or [None])[0] : ((proc13 is not None) and [proc13.content] or [None])[0] } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "stateless_item"


    class module_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.module_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "module"
    # grammar/ShyRecognizerBackend.g:89:1: module returns [ title , content ] : ^( TREE_MODULE ID ( module_item )* ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        ID14 = None
        module_item15 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:91:5: ( ^( TREE_MODULE ID ( module_item )* ) )
                # grammar/ShyRecognizerBackend.g:91:9: ^( TREE_MODULE ID ( module_item )* )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module593)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_module595)

                #action start
                retval.title , retval.content = ID14.text , dict ( ) 
                #action end


                # grammar/ShyRecognizerBackend.g:93:13: ( module_item )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == TREE_MODULE_QUEUE or LA4_0 == TREE_PROC or (TREE_RECEIVE <= LA4_0 <= TREE_REQUEST)) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerBackend.g:93:15: module_item
                        pass 
                        self._state.following.append(self.FOLLOW_module_item_in_module625)
                        module_item15 = self.module_item()

                        self._state.following.pop()

                        #action start
                        retval.content = merge ( retval.content , module_item15 ) 
                        #action end



                    else:
                        break #loop4


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "module"



    # $ANTLR start "module_item"
    # grammar/ShyRecognizerBackend.g:99:1: module_item returns [ value ] : ( module_queue | proc | receive | request );
    def module_item(self, ):
        value = None


        module_queue16 = None

        proc17 = None

        receive18 = None

        request19 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:101:5: ( module_queue | proc | receive | request )
                alt5 = 4
                LA5 = self.input.LA(1)
                if LA5 == TREE_MODULE_QUEUE:
                    alt5 = 1
                elif LA5 == TREE_PROC:
                    alt5 = 2
                elif LA5 == TREE_RECEIVE:
                    alt5 = 3
                elif LA5 == TREE_REQUEST:
                    alt5 = 4
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:101:9: module_queue
                    pass 
                    self._state.following.append(self.FOLLOW_module_queue_in_module_item696)
                    module_queue16 = self.module_queue()

                    self._state.following.pop()

                    #action start
                    value = { 'module_queue' : module_queue16 } 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyRecognizerBackend.g:103:9: proc
                    pass 
                    self._state.following.append(self.FOLLOW_proc_in_module_item721)
                    proc17 = self.proc()

                    self._state.following.pop()

                    #action start
                    value = { 'proc' : { ((proc17 is not None) and [proc17.title] or [None])[0] : ((proc17 is not None) and [proc17.content] or [None])[0] } } 
                    #action end



                elif alt5 == 3:
                    # grammar/ShyRecognizerBackend.g:105:9: receive
                    pass 
                    self._state.following.append(self.FOLLOW_receive_in_module_item745)
                    receive18 = self.receive()

                    self._state.following.pop()

                    #action start
                    value = { 'receive' : { ((receive18 is not None) and [receive18.title] or [None])[0] : ((receive18 is not None) and [receive18.content] or [None])[0] } } 
                    #action end



                elif alt5 == 4:
                    # grammar/ShyRecognizerBackend.g:107:9: request
                    pass 
                    self._state.following.append(self.FOLLOW_request_in_module_item769)
                    request19 = self.request()

                    self._state.following.pop()

                    #action start
                    value = { 'request' : { ((request19 is not None) and [request19.title] or [None])[0] : ((request19 is not None) and [request19.content] or [None])[0] } } 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module_item"



    # $ANTLR start "module_queue"
    # grammar/ShyRecognizerBackend.g:111:1: module_queue returns [ value ] : ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        value = None


        ID20 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:113:5: ( ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerBackend.g:113:9: ^( TREE_MODULE_QUEUE ID )
                pass 
                self.match(self.input, TREE_MODULE_QUEUE, self.FOLLOW_TREE_MODULE_QUEUE_in_module_queue812)

                self.match(self.input, DOWN, None)
                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue814)

                self.match(self.input, UP, None)


                #action start
                value = ID20.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module_queue"


    class request_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.request_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "request"
    # grammar/ShyRecognizerBackend.g:116:1: request returns [ title , content ] : ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) ;
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        ID21 = None
        local_vars22 = None

        statements23 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:119:5: ( ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:119:9: ^( TREE_REQUEST ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_REQUEST, self.FOLLOW_TREE_REQUEST_in_request857)

                self.match(self.input, DOWN, None)
                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_request871)

                #action start
                retval.title = ID21.text 
                #action end


                # grammar/ShyRecognizerBackend.g:122:13: ( local_vars )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_LOCAL_VARS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:122:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_request905)
                    local_vars22 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars22 
                    #action end





                # grammar/ShyRecognizerBackend.g:125:13: ( statements )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == TREE_STATEMENTS) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:125:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_request955)
                    statements23 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements23 
                    #action end





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "request"


    class receive_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.receive_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "receive"
    # grammar/ShyRecognizerBackend.g:131:1: receive returns [ title , content ] : ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) ;
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        ID24 = None
        local_vars25 = None

        statements26 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:134:5: ( ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:134:9: ^( TREE_RECEIVE ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_RECEIVE, self.FOLLOW_TREE_RECEIVE_in_receive1038)

                self.match(self.input, DOWN, None)
                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_receive1052)

                #action start
                retval.title = ID24.text 
                #action end


                # grammar/ShyRecognizerBackend.g:137:13: ( local_vars )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == TREE_LOCAL_VARS) :
                    alt8 = 1
                if alt8 == 1:
                    # grammar/ShyRecognizerBackend.g:137:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_receive1086)
                    local_vars25 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars25 
                    #action end





                # grammar/ShyRecognizerBackend.g:140:13: ( statements )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == TREE_STATEMENTS) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:140:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_receive1136)
                    statements26 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements26 
                    #action end





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "receive"


    class proc_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.proc_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "proc"
    # grammar/ShyRecognizerBackend.g:146:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID27 = None
        proc_args28 = None

        local_vars29 = None

        statements30 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:149:5: ( ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:149:9: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc1219)

                self.match(self.input, DOWN, None)
                ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_proc1233)

                #action start
                retval.title = ID27.text 
                #action end


                # grammar/ShyRecognizerBackend.g:152:13: ( proc_args )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == TREE_PROC_ARGS) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerBackend.g:152:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc1267)
                    proc_args28 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args28 
                    #action end





                # grammar/ShyRecognizerBackend.g:155:13: ( local_vars )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_LOCAL_VARS) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:155:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_proc1317)
                    local_vars29 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars29 
                    #action end





                # grammar/ShyRecognizerBackend.g:158:13: ( statements )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == TREE_STATEMENTS) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:158:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc1367)
                    statements30 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements30 
                    #action end





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "proc"



    # $ANTLR start "proc_args"
    # grammar/ShyRecognizerBackend.g:164:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints31 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:166:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:166:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args1440)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args1442)
                attrs_hints31 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints31 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "local_vars"
    # grammar/ShyRecognizerBackend.g:170:1: local_vars returns [ value ] : ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        value = None


        attrs_hints32 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:172:5: ( ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:172:9: ^( TREE_LOCAL_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_LOCAL_VARS, self.FOLLOW_TREE_LOCAL_VARS_in_local_vars1487)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars1489)
                attrs_hints32 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints32 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "local_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:176:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement33 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:179:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:179:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements1544)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:179:28: ( statement )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_STATEMENT_ASSIGN or LA13_0 == TREE_STATEMENT_CALL or (TREE_STATEMENT_IF <= LA13_0 <= TREE_STATEMENT_WITH)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:179:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1548)
                        statement33 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement33 ) 
                        #action end



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statements"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:184:1: statement returns [ value ] : ( statement_call | statement_send | statement_if | statement_assign | statement_with | statement_while );
    def statement(self, ):
        value = None


        statement_call34 = None

        statement_send35 = None

        statement_if36 = None

        statement_assign37 = None

        statement_with38 = None

        statement_while39 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:186:5: ( statement_call | statement_send | statement_if | statement_assign | statement_with | statement_while )
                alt14 = 6
                LA14 = self.input.LA(1)
                if LA14 == TREE_STATEMENT_CALL:
                    alt14 = 1
                elif LA14 == TREE_STATEMENT_SEND:
                    alt14 = 2
                elif LA14 == TREE_STATEMENT_IF:
                    alt14 = 3
                elif LA14 == TREE_STATEMENT_ASSIGN:
                    alt14 = 4
                elif LA14 == TREE_STATEMENT_WITH:
                    alt14 = 5
                elif LA14 == TREE_STATEMENT_WHILE:
                    alt14 = 6
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyRecognizerBackend.g:186:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement1604)
                    statement_call34 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call34 
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:188:9: statement_send
                    pass 
                    self._state.following.append(self.FOLLOW_statement_send_in_statement1628)
                    statement_send35 = self.statement_send()

                    self._state.following.pop()

                    #action start
                    value = statement_send35 
                    #action end



                elif alt14 == 3:
                    # grammar/ShyRecognizerBackend.g:190:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement1652)
                    statement_if36 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if36 
                    #action end



                elif alt14 == 4:
                    # grammar/ShyRecognizerBackend.g:192:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1676)
                    statement_assign37 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign37 
                    #action end



                elif alt14 == 5:
                    # grammar/ShyRecognizerBackend.g:194:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1700)
                    statement_with38 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with38 
                    #action end



                elif alt14 == 6:
                    # grammar/ShyRecognizerBackend.g:196:9: statement_while
                    pass 
                    self._state.following.append(self.FOLLOW_statement_while_in_statement1724)
                    statement_while39 = self.statement_while()

                    self._state.following.pop()

                    #action start
                    value = statement_while39 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:200:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID40 = None
        statements41 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:202:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:202:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1767)

                self.match(self.input, DOWN, None)
                ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1769)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1771)
                statements41 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID40.text : statements41 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:206:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID43 = None
        arbitrary_value42 = None


        value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:209:5: ( ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:209:9: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1822)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:210:13: ( arbitrary_value )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA15_0 <= ID) or LA15_0 == MINUS or LA15_0 == NUMBER or LA15_0 == STRING) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:210:15: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1838)
                        arbitrary_value42 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                                        
                        value [ 'assign' ] [ 'from' ] . append (
                            arbitrary_value42 )
                                        
                        #action end



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                self.match(self.input, TREE_STATEMENT_ASSIGN_TO, self.FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1886)

                # grammar/ShyRecognizerBackend.g:217:13: ( ID )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ID) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:217:15: ID
                        pass 
                        ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1902)

                        #action start
                                        
                        value [ 'assign' ] [ 'to' ] . append (
                            ID43.text )
                                        
                        #action end



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:226:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) ;
    def statement_if(self, ):
        value = None


        conditional_ops44 = None

        statements45 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:229:5: ( ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) )
                # grammar/ShyRecognizerBackend.g:229:9: ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1985)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:230:13: ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_STATEMENT_ELIF) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:230:15: ^( TREE_STATEMENT_ELIF conditional_ops )
                        pass 
                        self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_if2003)

                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_conditional_ops_in_statement_if2005)
                        conditional_ops44 = self.conditional_ops()

                        self._state.following.pop()

                        self.match(self.input, UP, None)


                        #action start
                        value [ 'if' ] . append ( conditional_ops44 ) 
                        #action end



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1


                # grammar/ShyRecognizerBackend.g:233:13: ( ^( TREE_STATEMENT_ELSE statements ) )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == TREE_STATEMENT_ELSE) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerBackend.g:233:15: ^( TREE_STATEMENT_ELSE statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_if2059)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statements_in_statement_if2061)
                    statements45 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ 'else' ] = statements45 
                    #action end





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_if"



    # $ANTLR start "statement_while"
    # grammar/ShyRecognizerBackend.g:239:1: statement_while returns [ value ] : ^( TREE_STATEMENT_WHILE conditional_ops ) ;
    def statement_while(self, ):
        value = None


        conditional_ops46 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:241:5: ( ^( TREE_STATEMENT_WHILE conditional_ops ) )
                # grammar/ShyRecognizerBackend.g:241:9: ^( TREE_STATEMENT_WHILE conditional_ops )
                pass 
                self.match(self.input, TREE_STATEMENT_WHILE, self.FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2136)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_conditional_ops_in_statement_while2138)
                conditional_ops46 = self.conditional_ops()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'while' : conditional_ops46 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_while"



    # $ANTLR start "conditional_ops"
    # grammar/ShyRecognizerBackend.g:245:1: conditional_ops returns [ value ] : ( condition_any statements | condition_all statements );
    def conditional_ops(self, ):
        value = None


        condition_any47 = None

        statements48 = None

        condition_all49 = None

        statements50 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:247:5: ( condition_any statements | condition_all statements )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == TREE_CONDITION_ANY) :
                    alt19 = 1
                elif (LA19_0 == TREE_CONDITION_ALL) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:247:9: condition_any statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_any_in_conditional_ops2181)
                    condition_any47 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2183)
                    statements48 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'any' : condition_any47 ,
                       'ops' : statements48 }
                                
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:252:9: condition_all statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_all_in_conditional_ops2207)
                    condition_all49 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2209)
                    statements50 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'all' : condition_all49 ,
                       'ops' : statements50 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "conditional_ops"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:259:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call51 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:262:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:262:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any2262)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:263:13: ( statement_call )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_STATEMENT_CALL) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:263:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any2278)
                        statement_call51 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call51 ) 
                        #action end



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:268:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call52 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:271:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:271:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all2353)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:272:13: ( statement_call )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_STATEMENT_CALL) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:272:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all2369)
                        statement_call52 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call52 ) 
                        #action end



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:277:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args53 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:279:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:279:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call2434)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call2436)
                    statement_call_args53 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args53 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:283:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value54 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:286:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:286:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:286:9: ( arbitrary_value )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER or LA22_0 == STRING) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:286:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2491)
                        arbitrary_value54 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value54 ) 
                        #action end



                    else:
                        break #loop22





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "statement_send"
    # grammar/ShyRecognizerBackend.g:291:1: statement_send returns [ value ] : ^( TREE_STATEMENT_SEND statement_send_args ) ;
    def statement_send(self, ):
        value = None


        statement_send_args55 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:293:5: ( ^( TREE_STATEMENT_SEND statement_send_args ) )
                # grammar/ShyRecognizerBackend.g:293:9: ^( TREE_STATEMENT_SEND statement_send_args )
                pass 
                self.match(self.input, TREE_STATEMENT_SEND, self.FOLLOW_TREE_STATEMENT_SEND_in_statement_send2546)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_send_args_in_statement_send2548)
                    statement_send_args55 = self.statement_send_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'send' : statement_send_args55 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_send"



    # $ANTLR start "statement_send_args"
    # grammar/ShyRecognizerBackend.g:297:1: statement_send_args returns [ value ] : ( arbitrary_value )* ;
    def statement_send_args(self, ):
        value = None


        arbitrary_value56 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:300:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:300:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:300:9: ( arbitrary_value )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER or LA23_0 == STRING) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerBackend.g:300:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_send_args2603)
                        arbitrary_value56 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value56 ) 
                        #action end



                    else:
                        break #loop23





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_send_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:305:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID57 = None
        EXPRESSION58 = None
        STRING59 = None
        num_whole60 = None

        num_fract61 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:307:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
                alt24 = 5
                LA24 = self.input.LA(1)
                if LA24 == ID:
                    alt24 = 1
                elif LA24 == EXPRESSION:
                    alt24 = 2
                elif LA24 == STRING:
                    alt24 = 3
                elif LA24 == MINUS:
                    LA24_4 = self.input.LA(2)

                    if (LA24_4 == NUMBER) :
                        LA24_6 = self.input.LA(3)

                        if (LA24_6 == DIVIDE) :
                            alt24 = 5
                        elif (LA24_6 == 3 or (EXPRESSION <= LA24_6 <= ID) or LA24_6 == MINUS or LA24_6 == NUMBER or LA24_6 == STRING or LA24_6 == TREE_STATEMENT_ASSIGN_TO) :
                            alt24 = 4
                        else:
                            nvae = NoViableAltException("", 24, 6, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 24, 4, self.input)

                        raise nvae


                elif LA24 == NUMBER:
                    LA24_5 = self.input.LA(2)

                    if (LA24_5 == DIVIDE) :
                        alt24 = 5
                    elif (LA24_5 == 3 or (EXPRESSION <= LA24_5 <= ID) or LA24_5 == MINUS or LA24_5 == NUMBER or LA24_5 == STRING or LA24_5 == TREE_STATEMENT_ASSIGN_TO) :
                        alt24 = 4
                    else:
                        nvae = NoViableAltException("", 24, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerBackend.g:307:9: ID
                    pass 
                    ID57 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2656)

                    #action start
                    value = ID57.text 
                    #action end



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:308:9: EXPRESSION
                    pass 
                    EXPRESSION58 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2668)

                    #action start
                    value = EXPRESSION58.text 
                    #action end



                elif alt24 == 3:
                    # grammar/ShyRecognizerBackend.g:309:9: STRING
                    pass 
                    STRING59 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2680)

                    #action start
                    value = STRING59.text 
                    #action end



                elif alt24 == 4:
                    # grammar/ShyRecognizerBackend.g:310:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2692)
                    num_whole60 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole60 
                    #action end



                elif alt24 == 5:
                    # grammar/ShyRecognizerBackend.g:311:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2704)
                    num_fract61 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract61 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_value"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:314:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID62 = None
        consts_items63 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:317:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:317:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts2745)

                self.match(self.input, DOWN, None)
                ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2747)

                self._state.following.append(self.FOLLOW_consts_items_in_consts2749)
                consts_items63 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID62.text , consts_items63 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:321:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item64 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:324:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:324:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:324:9: ( consts_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA25_0 <= TREE_NUM_WHOLE)) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerBackend.g:324:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2804)
                        consts_item64 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item64 is not None) and [consts_item64.name] or [None])[0] ] = ((consts_item64 is not None) and [consts_item64.value] or [None])[0] 
                        #action end



                    else:
                        if cnt25 >= 1:
                            break #loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "consts_items"


    class consts_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerBackend.g:329:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID65 = None
        ID67 = None
        ID69 = None
        EXPRESSION70 = None
        num_whole66 = None

        num_fract68 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:331:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt26 = 3
                LA26 = self.input.LA(1)
                if LA26 == TREE_NUM_WHOLE:
                    alt26 = 1
                elif LA26 == TREE_NUM_FRACT:
                    alt26 = 2
                elif LA26 == TREE_EXPRESSION:
                    alt26 = 3
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # grammar/ShyRecognizerBackend.g:331:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2859)

                    self.match(self.input, DOWN, None)
                    ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2861)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2863)
                    num_whole66 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID65.text , num_whole66 
                    #action end



                elif alt26 == 2:
                    # grammar/ShyRecognizerBackend.g:333:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2891)

                    self.match(self.input, DOWN, None)
                    ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2893)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2895)
                    num_fract68 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID67.text , num_fract68 
                    #action end



                elif alt26 == 3:
                    # grammar/ShyRecognizerBackend.g:335:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2923)

                    self.match(self.input, DOWN, None)
                    ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2925)

                    EXPRESSION70 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2927)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID69.text , EXPRESSION70.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts_item"


    class types_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "types"
    # grammar/ShyRecognizerBackend.g:339:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID71 = None
        types_items72 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:342:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:342:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2982)

                self.match(self.input, DOWN, None)
                ID71 = self.match(self.input, ID, self.FOLLOW_ID_in_types2984)

                self._state.following.append(self.FOLLOW_types_items_in_types2986)
                types_items72 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID71.text , types_items72 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:346:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item73 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:349:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:349:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:349:9: ( types_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == TREE_TYPES_ITEM) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerBackend.g:349:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items3041)
                        types_item73 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item73 is not None) and [types_item73.name] or [None])[0] ] = ((types_item73 is not None) and [types_item73.value] or [None])[0] 
                        #action end



                    else:
                        if cnt27 >= 1:
                            break #loop27

                        eee = EarlyExitException(27, self.input)
                        raise eee

                    cnt27 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:354:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID74 = None
        attrs_hints75 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:356:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:356:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item3096)

                self.match(self.input, DOWN, None)
                ID74 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item3098)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item3100)
                attrs_hints75 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID74.text , attrs_hints75 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"


    class messages_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.messages_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "messages"
    # grammar/ShyRecognizerBackend.g:360:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID76 = None
        messages_items77 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:363:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:363:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages3155)

                self.match(self.input, DOWN, None)
                ID76 = self.match(self.input, ID, self.FOLLOW_ID_in_messages3157)

                self._state.following.append(self.FOLLOW_messages_items_in_messages3159)
                messages_items77 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID76.text , messages_items77 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:367:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item78 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:370:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:370:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:370:9: ( messages_item )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == TREE_MESSAGES_ITEM) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerBackend.g:370:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items3214)
                        messages_item78 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value = merge ( value, messages_item78 ) 
                        #action end



                    else:
                        if cnt28 >= 1:
                            break #loop28

                        eee = EarlyExitException(28, self.input)
                        raise eee

                    cnt28 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "messages_items"



    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerBackend.g:375:1: messages_item returns [ value ] : ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? ) ;
    def messages_item(self, ):
        value = None


        ID79 = None
        a = None

        c = None

        b = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:378:5: ( ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? ) )
                # grammar/ShyRecognizerBackend.g:378:9: ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3279)

                self.match(self.input, DOWN, None)
                ID79 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3281)

                # grammar/ShyRecognizerBackend.g:379:13: ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == TREE_MESSAGES_ITEM_RECEIVE) :
                    alt29 = 1
                if alt29 == 1:
                    # grammar/ShyRecognizerBackend.g:379:15: TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_RECEIVE, self.FOLLOW_TREE_MESSAGES_ITEM_RECEIVE_in_messages_item3297)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3303)
                    a = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'receive' : { ID79.text : a } } )
                                    
                    #action end





                # grammar/ShyRecognizerBackend.g:385:13: ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == TREE_MESSAGES_ITEM_REQUEST) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerBackend.g:385:15: TREE_MESSAGES_ITEM_REQUEST c= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_REQUEST, self.FOLLOW_TREE_MESSAGES_ITEM_REQUEST_in_messages_item3353)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3359)
                    c = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'request' : { ID79.text : c } } )
                                    
                    #action end





                # grammar/ShyRecognizerBackend.g:391:13: ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == TREE_MESSAGES_ITEM_REPLY) :
                    alt31 = 1
                if alt31 == 1:
                    # grammar/ShyRecognizerBackend.g:391:15: TREE_MESSAGES_ITEM_REPLY b= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_REPLY, self.FOLLOW_TREE_MESSAGES_ITEM_REPLY_in_messages_item3409)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3415)
                    b = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'reply' : { ID79.text : b } } )
                                    
                    #action end





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "messages_item"


    class vars_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.vars_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "vars"
    # grammar/ShyRecognizerBackend.g:400:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID80 = None
        attrs_hints81 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:402:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:402:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars3488)

                self.match(self.input, DOWN, None)
                ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3490)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3492)
                attrs_hints81 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID80.text , attrs_hints81 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:406:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint82 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:409:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:409:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3545)

                # grammar/ShyRecognizerBackend.g:409:26: ( attr_hint )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == TREE_ATTR_HINT) :
                        alt32 = 1


                    if alt32 == 1:
                        # grammar/ShyRecognizerBackend.g:409:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3549)
                        attr_hint82 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value += attr_hint82 
                        #action end



                    else:
                        break #loop32





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:412:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID83 = None
        ID84 = None
        hint85 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:415:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == TREE_ATTR_HINT) :
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == 2) :
                        LA35_2 = self.input.LA(3)

                        if (LA35_2 == TREE_HINT_NONE) :
                            alt35 = 1
                        elif (LA35_2 == TREE_HINT) :
                            alt35 = 2
                        else:
                            nvae = NoViableAltException("", 35, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae


                if alt35 == 1:
                    # grammar/ShyRecognizerBackend.g:415:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3594)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint3596)

                    # grammar/ShyRecognizerBackend.g:415:42: ( ^( TREE_ATTR ID ) )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == TREE_ATTR) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerBackend.g:415:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3602)

                            self.match(self.input, DOWN, None)
                            ID83 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3604)

                            self.match(self.input, UP, None)


                            #action start
                            value . append ( { ID83.text : dict ( ) } ) 
                            #action end



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


                    self.match(self.input, UP, None)



                elif alt35 == 2:
                    # grammar/ShyRecognizerBackend.g:418:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3646)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3648)
                    hint85 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:418:32: ( ^( TREE_ATTR ID ) )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == TREE_ATTR) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerBackend.g:418:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3654)

                            self.match(self.input, DOWN, None)
                            ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3656)

                            self.match(self.input, UP, None)


                            #action start
                            value . append ( { ID84.text : hint85 } ) 
                            #action end



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:423:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID86 = None
        ID87 = None
        hint_args88 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:426:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == TREE_HINT) :
                    LA36_1 = self.input.LA(2)

                    if (LA36_1 == 2) :
                        LA36_2 = self.input.LA(3)

                        if (LA36_2 == ID) :
                            LA36_3 = self.input.LA(4)

                            if (LA36_3 == 3) :
                                alt36 = 1
                            elif (LA36_3 == ID or LA36_3 == UNDERSCORE) :
                                alt36 = 2
                            else:
                                nvae = NoViableAltException("", 36, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 36, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 36, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # grammar/ShyRecognizerBackend.g:426:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3725)

                    self.match(self.input, DOWN, None)
                    ID86 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3727)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID86.text ] = list ( ) 
                    #action end



                elif alt36 == 2:
                    # grammar/ShyRecognizerBackend.g:428:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3755)

                    self.match(self.input, DOWN, None)
                    ID87 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3757)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint3759)
                    hint_args88 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID87.text ] = hint_args88 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:432:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg89 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:435:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:435:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:435:9: ( hint_arg )+
                cnt37 = 0
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == ID or LA37_0 == UNDERSCORE) :
                        alt37 = 1


                    if alt37 == 1:
                        # grammar/ShyRecognizerBackend.g:435:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args3814)
                        hint_arg89 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg89 ) 
                        #action end



                    else:
                        if cnt37 >= 1:
                            break #loop37

                        eee = EarlyExitException(37, self.input)
                        raise eee

                    cnt37 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:438:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID90 = None
        UNDERSCORE91 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:440:5: ( ID | UNDERSCORE )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == ID) :
                    alt38 = 1
                elif (LA38_0 == UNDERSCORE) :
                    alt38 = 2
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # grammar/ShyRecognizerBackend.g:440:9: ID
                    pass 
                    ID90 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg3847)

                    #action start
                    value = ID90.text 
                    #action end



                elif alt38 == 2:
                    # grammar/ShyRecognizerBackend.g:441:9: UNDERSCORE
                    pass 
                    UNDERSCORE91 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg3859)

                    #action start
                    value = UNDERSCORE91.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:444:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS92 = None
        NUMBER93 = None
        NUMBER94 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:446:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == MINUS) :
                    alt39 = 1
                elif (LA39_0 == NUMBER) :
                    alt39 = 2
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae


                if alt39 == 1:
                    # grammar/ShyRecognizerBackend.g:446:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:446:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:446:11: MINUS NUMBER
                    pass 
                    MINUS92 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3890)

                    NUMBER93 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3892)




                    #action start
                    value = int ( MINUS92.text + NUMBER93.text ) 
                    #action end



                elif alt39 == 2:
                    # grammar/ShyRecognizerBackend.g:448:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:448:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:448:11: NUMBER
                    pass 
                    NUMBER94 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3920)




                    #action start
                    value = int ( NUMBER94.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:452:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS95 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:454:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == MINUS) :
                    alt40 = 1
                elif (LA40_0 == NUMBER) :
                    alt40 = 2
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae


                if alt40 == 1:
                    # grammar/ShyRecognizerBackend.g:454:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:454:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:454:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS95 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3965)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3971)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3973)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3979)




                    #action start
                                
                    value = Fraction ( int ( MINUS95.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt40 == 2:
                    # grammar/ShyRecognizerBackend.g:459:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:459:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:459:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract4011)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract4013)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract4019)




                    #action start
                    value = Fraction ( int ( n.text ) , int ( d.text ) ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_fract"



 

    FOLLOW_module_in_start87 = frozenset([1, 45, 52, 57, 68, 79, 80, 82])
    FOLLOW_stateless_in_start114 = frozenset([1, 45, 52, 57, 68, 79, 80, 82])
    FOLLOW_trace_in_start141 = frozenset([1, 45, 52, 57, 68, 79, 80, 82])
    FOLLOW_consts_in_start168 = frozenset([1, 45, 52, 57, 68, 79, 80, 82])
    FOLLOW_types_in_start194 = frozenset([1, 45, 52, 57, 68, 79, 80, 82])
    FOLLOW_messages_in_start220 = frozenset([1, 45, 52, 57, 68, 79, 80, 82])
    FOLLOW_vars_in_start246 = frozenset([1, 45, 52, 57, 68, 79, 80, 82])
    FOLLOW_TREE_TRACE_in_trace301 = frozenset([2])
    FOLLOW_ID_in_trace303 = frozenset([3, 64])
    FOLLOW_trace_item_in_trace333 = frozenset([3, 64])
    FOLLOW_proc_in_trace_item404 = frozenset([1])
    FOLLOW_TREE_STATELESS_in_stateless447 = frozenset([2])
    FOLLOW_ID_in_stateless449 = frozenset([3, 64])
    FOLLOW_stateless_item_in_stateless479 = frozenset([3, 64])
    FOLLOW_proc_in_stateless_item550 = frozenset([1])
    FOLLOW_TREE_MODULE_in_module593 = frozenset([2])
    FOLLOW_ID_in_module595 = frozenset([3, 58, 64, 66, 67])
    FOLLOW_module_item_in_module625 = frozenset([3, 58, 64, 66, 67])
    FOLLOW_module_queue_in_module_item696 = frozenset([1])
    FOLLOW_proc_in_module_item721 = frozenset([1])
    FOLLOW_receive_in_module_item745 = frozenset([1])
    FOLLOW_request_in_module_item769 = frozenset([1])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue812 = frozenset([2])
    FOLLOW_ID_in_module_queue814 = frozenset([3])
    FOLLOW_TREE_REQUEST_in_request857 = frozenset([2])
    FOLLOW_ID_in_request871 = frozenset([3, 51, 69])
    FOLLOW_local_vars_in_request905 = frozenset([3, 69])
    FOLLOW_statements_in_request955 = frozenset([3])
    FOLLOW_TREE_RECEIVE_in_receive1038 = frozenset([2])
    FOLLOW_ID_in_receive1052 = frozenset([3, 51, 69])
    FOLLOW_local_vars_in_receive1086 = frozenset([3, 69])
    FOLLOW_statements_in_receive1136 = frozenset([3])
    FOLLOW_TREE_PROC_in_proc1219 = frozenset([2])
    FOLLOW_ID_in_proc1233 = frozenset([3, 51, 65, 69])
    FOLLOW_proc_args_in_proc1267 = frozenset([3, 51, 69])
    FOLLOW_local_vars_in_proc1317 = frozenset([3, 69])
    FOLLOW_statements_in_proc1367 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args1440 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args1442 = frozenset([3])
    FOLLOW_TREE_LOCAL_VARS_in_local_vars1487 = frozenset([2])
    FOLLOW_attrs_hints_in_local_vars1489 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements1544 = frozenset([2])
    FOLLOW_statement_in_statements1548 = frozenset([3, 70, 72, 75, 76, 77, 78])
    FOLLOW_statement_call_in_statement1604 = frozenset([1])
    FOLLOW_statement_send_in_statement1628 = frozenset([1])
    FOLLOW_statement_if_in_statement1652 = frozenset([1])
    FOLLOW_statement_assign_in_statement1676 = frozenset([1])
    FOLLOW_statement_with_in_statement1700 = frozenset([1])
    FOLLOW_statement_while_in_statement1724 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1767 = frozenset([2])
    FOLLOW_ID_in_statement_with1769 = frozenset([69])
    FOLLOW_statements_in_statement_with1771 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1822 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1838 = frozenset([18, 19, 23, 27, 37, 71])
    FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1886 = frozenset([19])
    FOLLOW_ID_in_statement_assign1902 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1985 = frozenset([2])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_if2003 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_if2005 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_if2059 = frozenset([2])
    FOLLOW_statements_in_statement_if2061 = frozenset([3])
    FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2136 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_while2138 = frozenset([3])
    FOLLOW_condition_any_in_conditional_ops2181 = frozenset([69])
    FOLLOW_statements_in_conditional_ops2183 = frozenset([1])
    FOLLOW_condition_all_in_conditional_ops2207 = frozenset([69])
    FOLLOW_statements_in_conditional_ops2209 = frozenset([1])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any2262 = frozenset([2])
    FOLLOW_statement_call_in_condition_any2278 = frozenset([3, 72])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all2353 = frozenset([2])
    FOLLOW_statement_call_in_condition_all2369 = frozenset([3, 72])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call2434 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call2436 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args2491 = frozenset([1, 18, 19, 23, 27, 37])
    FOLLOW_TREE_STATEMENT_SEND_in_statement_send2546 = frozenset([2])
    FOLLOW_statement_send_args_in_statement_send2548 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_send_args2603 = frozenset([1, 18, 19, 23, 27, 37])
    FOLLOW_ID_in_arbitrary_value2656 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2668 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2680 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2692 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2704 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts2745 = frozenset([2])
    FOLLOW_ID_in_consts2747 = frozenset([48, 59, 60])
    FOLLOW_consts_items_in_consts2749 = frozenset([3])
    FOLLOW_consts_item_in_consts_items2804 = frozenset([1, 48, 59, 60])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2859 = frozenset([2])
    FOLLOW_ID_in_consts_item2861 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2863 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2891 = frozenset([2])
    FOLLOW_ID_in_consts_item2893 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2895 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2923 = frozenset([2])
    FOLLOW_ID_in_consts_item2925 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2927 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2982 = frozenset([2])
    FOLLOW_ID_in_types2984 = frozenset([81])
    FOLLOW_types_items_in_types2986 = frozenset([3])
    FOLLOW_types_item_in_types_items3041 = frozenset([1, 81])
    FOLLOW_TREE_TYPES_ITEM_in_types_item3096 = frozenset([2])
    FOLLOW_ID_in_types_item3098 = frozenset([41])
    FOLLOW_attrs_hints_in_types_item3100 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages3155 = frozenset([2])
    FOLLOW_ID_in_messages3157 = frozenset([53])
    FOLLOW_messages_items_in_messages3159 = frozenset([3])
    FOLLOW_messages_item_in_messages_items3214 = frozenset([1, 53])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3279 = frozenset([2])
    FOLLOW_ID_in_messages_item3281 = frozenset([3, 54, 55, 56])
    FOLLOW_TREE_MESSAGES_ITEM_RECEIVE_in_messages_item3297 = frozenset([41])
    FOLLOW_attrs_hints_in_messages_item3303 = frozenset([3, 55, 56])
    FOLLOW_TREE_MESSAGES_ITEM_REQUEST_in_messages_item3353 = frozenset([41])
    FOLLOW_attrs_hints_in_messages_item3359 = frozenset([3, 55])
    FOLLOW_TREE_MESSAGES_ITEM_REPLY_in_messages_item3409 = frozenset([41])
    FOLLOW_attrs_hints_in_messages_item3415 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars3488 = frozenset([2])
    FOLLOW_ID_in_vars3490 = frozenset([41])
    FOLLOW_attrs_hints_in_vars3492 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3545 = frozenset([1, 42])
    FOLLOW_attr_hint_in_attrs_hints3549 = frozenset([1, 42])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3594 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint3596 = frozenset([40])
    FOLLOW_TREE_ATTR_in_attr_hint3602 = frozenset([2])
    FOLLOW_ID_in_attr_hint3604 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3646 = frozenset([2])
    FOLLOW_hint_in_attr_hint3648 = frozenset([40])
    FOLLOW_TREE_ATTR_in_attr_hint3654 = frozenset([2])
    FOLLOW_ID_in_attr_hint3656 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3725 = frozenset([2])
    FOLLOW_ID_in_hint3727 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3755 = frozenset([2])
    FOLLOW_ID_in_hint3757 = frozenset([19, 84])
    FOLLOW_hint_args_in_hint3759 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args3814 = frozenset([1, 19, 84])
    FOLLOW_ID_in_hint_arg3847 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg3859 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3890 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3892 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole3920 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3965 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3971 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3973 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3979 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract4011 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract4013 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract4019 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
