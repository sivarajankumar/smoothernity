# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-06 20:15:08

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
STATELESS=35
STRING=36
TRACE=37
TREE_ARBITRARY_TOKEN=38
TREE_ATTR=39
TREE_ATTRS_HINTS=40
TREE_ATTR_HINT=41
TREE_CONDITION_ALL=42
TREE_CONDITION_ANY=43
TREE_CONSTS=44
TREE_COPY=45
TREE_COPY_PASTE=46
TREE_EXPRESSION=47
TREE_HINT=48
TREE_HINT_NONE=49
TREE_LOCAL_VARS=50
TREE_MESSAGES=51
TREE_MESSAGES_ITEM=52
TREE_MESSAGES_ITEM_RECEIVE=53
TREE_MESSAGES_ITEM_REPLY=54
TREE_MESSAGES_ITEM_REQUEST=55
TREE_MODULE=56
TREE_MODULE_QUEUE=57
TREE_NUM_FRACT=58
TREE_NUM_WHOLE=59
TREE_PASTE=60
TREE_PASTE_REPLACE=61
TREE_PASTE_WITH=62
TREE_PROC=63
TREE_PROC_ARGS=64
TREE_RECEIVE=65
TREE_REQUEST=66
TREE_STATELESS=67
TREE_STATEMENTS=68
TREE_STATEMENT_ASSIGN=69
TREE_STATEMENT_ASSIGN_TO=70
TREE_STATEMENT_CALL=71
TREE_STATEMENT_ELIF=72
TREE_STATEMENT_ELSE=73
TREE_STATEMENT_IF=74
TREE_STATEMENT_WHILE=75
TREE_STATEMENT_WITH=76
TREE_TRACE=77
TREE_TYPES=78
TREE_TYPES_ITEM=79
TREE_VARS=80
TYPES=81
UNDERSCORE=82
VARS=83
WHILE=84
WHITESPACE=85
WITH=86

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "RECEIVE", "REPLACE", "REPLY", 
    "REQUEST", "STATELESS", "STRING", "TRACE", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", 
    "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_LOCAL_VARS", "TREE_MESSAGES", "TREE_MESSAGES_ITEM", 
    "TREE_MESSAGES_ITEM_RECEIVE", "TREE_MESSAGES_ITEM_REPLY", "TREE_MESSAGES_ITEM_REQUEST", 
    "TREE_MODULE", "TREE_MODULE_QUEUE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_RECEIVE", "TREE_REQUEST", "TREE_STATELESS", 
    "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", 
    "TREE_STATEMENT_IF", "TREE_STATEMENT_WHILE", "TREE_STATEMENT_WITH", 
    "TREE_TRACE", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", 
    "UNDERSCORE", "VARS", "WHILE", "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:184:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with | statement_while );
    def statement(self, ):
        value = None


        statement_call34 = None

        statement_if35 = None

        statement_assign36 = None

        statement_with37 = None

        statement_while38 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:186:5: ( statement_call | statement_if | statement_assign | statement_with | statement_while )
                alt14 = 5
                LA14 = self.input.LA(1)
                if LA14 == TREE_STATEMENT_CALL:
                    alt14 = 1
                elif LA14 == TREE_STATEMENT_IF:
                    alt14 = 2
                elif LA14 == TREE_STATEMENT_ASSIGN:
                    alt14 = 3
                elif LA14 == TREE_STATEMENT_WITH:
                    alt14 = 4
                elif LA14 == TREE_STATEMENT_WHILE:
                    alt14 = 5
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
                    # grammar/ShyRecognizerBackend.g:188:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement1628)
                    statement_if35 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if35 
                    #action end



                elif alt14 == 3:
                    # grammar/ShyRecognizerBackend.g:190:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1652)
                    statement_assign36 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign36 
                    #action end



                elif alt14 == 4:
                    # grammar/ShyRecognizerBackend.g:192:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1676)
                    statement_with37 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with37 
                    #action end



                elif alt14 == 5:
                    # grammar/ShyRecognizerBackend.g:194:9: statement_while
                    pass 
                    self._state.following.append(self.FOLLOW_statement_while_in_statement1700)
                    statement_while38 = self.statement_while()

                    self._state.following.pop()

                    #action start
                    value = statement_while38 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:198:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID39 = None
        statements40 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:200:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:200:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1743)

                self.match(self.input, DOWN, None)
                ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1745)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1747)
                statements40 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID39.text : statements40 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:204:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID42 = None
        arbitrary_value41 = None


        value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:207:5: ( ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:207:9: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1798)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:208:13: ( arbitrary_value )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA15_0 <= ID) or LA15_0 == MINUS or LA15_0 == NUMBER or LA15_0 == STRING) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:208:15: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1814)
                        arbitrary_value41 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                                        
                        value [ 'assign' ] [ 'from' ] . append (
                            arbitrary_value41 )
                                        
                        #action end



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                self.match(self.input, TREE_STATEMENT_ASSIGN_TO, self.FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1862)

                # grammar/ShyRecognizerBackend.g:215:13: ( ID )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ID) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:215:15: ID
                        pass 
                        ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1878)

                        #action start
                                        
                        value [ 'assign' ] [ 'to' ] . append (
                            ID42.text )
                                        
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
    # grammar/ShyRecognizerBackend.g:224:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) ;
    def statement_if(self, ):
        value = None


        conditional_ops43 = None

        statements44 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:227:5: ( ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) )
                # grammar/ShyRecognizerBackend.g:227:9: ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1961)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:228:13: ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_STATEMENT_ELIF) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:228:15: ^( TREE_STATEMENT_ELIF conditional_ops )
                        pass 
                        self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1979)

                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_conditional_ops_in_statement_if1981)
                        conditional_ops43 = self.conditional_ops()

                        self._state.following.pop()

                        self.match(self.input, UP, None)


                        #action start
                        value [ 'if' ] . append ( conditional_ops43 ) 
                        #action end



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1


                # grammar/ShyRecognizerBackend.g:231:13: ( ^( TREE_STATEMENT_ELSE statements ) )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == TREE_STATEMENT_ELSE) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerBackend.g:231:15: ^( TREE_STATEMENT_ELSE statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_if2035)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statements_in_statement_if2037)
                    statements44 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ 'else' ] = statements44 
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
    # grammar/ShyRecognizerBackend.g:237:1: statement_while returns [ value ] : ^( TREE_STATEMENT_WHILE conditional_ops ) ;
    def statement_while(self, ):
        value = None


        conditional_ops45 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:239:5: ( ^( TREE_STATEMENT_WHILE conditional_ops ) )
                # grammar/ShyRecognizerBackend.g:239:9: ^( TREE_STATEMENT_WHILE conditional_ops )
                pass 
                self.match(self.input, TREE_STATEMENT_WHILE, self.FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2112)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_conditional_ops_in_statement_while2114)
                conditional_ops45 = self.conditional_ops()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'while' : conditional_ops45 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_while"



    # $ANTLR start "conditional_ops"
    # grammar/ShyRecognizerBackend.g:243:1: conditional_ops returns [ value ] : ( condition_any statements | condition_all statements );
    def conditional_ops(self, ):
        value = None


        condition_any46 = None

        statements47 = None

        condition_all48 = None

        statements49 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:245:5: ( condition_any statements | condition_all statements )
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
                    # grammar/ShyRecognizerBackend.g:245:9: condition_any statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_any_in_conditional_ops2157)
                    condition_any46 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2159)
                    statements47 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'any' : condition_any46 ,
                       'ops' : statements47 }
                                
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:250:9: condition_all statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_all_in_conditional_ops2183)
                    condition_all48 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2185)
                    statements49 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'all' : condition_all48 ,
                       'ops' : statements49 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "conditional_ops"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:257:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call50 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:260:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:260:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any2238)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:261:13: ( statement_call )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_STATEMENT_CALL) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:261:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any2254)
                        statement_call50 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call50 ) 
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
    # grammar/ShyRecognizerBackend.g:266:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call51 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:269:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:269:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all2329)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:270:13: ( statement_call )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_STATEMENT_CALL) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:270:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all2345)
                        statement_call51 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call51 ) 
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
    # grammar/ShyRecognizerBackend.g:275:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args52 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:277:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:277:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call2410)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call2412)
                    statement_call_args52 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args52 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:281:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value53 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:284:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:284:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:284:9: ( arbitrary_value )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER or LA22_0 == STRING) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:284:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2467)
                        arbitrary_value53 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value53 ) 
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



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:289:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID54 = None
        EXPRESSION55 = None
        STRING56 = None
        num_whole57 = None

        num_fract58 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:291:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
                alt23 = 5
                LA23 = self.input.LA(1)
                if LA23 == ID:
                    alt23 = 1
                elif LA23 == EXPRESSION:
                    alt23 = 2
                elif LA23 == STRING:
                    alt23 = 3
                elif LA23 == MINUS:
                    LA23_4 = self.input.LA(2)

                    if (LA23_4 == NUMBER) :
                        LA23_6 = self.input.LA(3)

                        if (LA23_6 == DIVIDE) :
                            alt23 = 5
                        elif (LA23_6 == 3 or (EXPRESSION <= LA23_6 <= ID) or LA23_6 == MINUS or LA23_6 == NUMBER or LA23_6 == STRING or LA23_6 == TREE_STATEMENT_ASSIGN_TO) :
                            alt23 = 4
                        else:
                            nvae = NoViableAltException("", 23, 6, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 23, 4, self.input)

                        raise nvae


                elif LA23 == NUMBER:
                    LA23_5 = self.input.LA(2)

                    if (LA23_5 == DIVIDE) :
                        alt23 = 5
                    elif (LA23_5 == 3 or (EXPRESSION <= LA23_5 <= ID) or LA23_5 == MINUS or LA23_5 == NUMBER or LA23_5 == STRING or LA23_5 == TREE_STATEMENT_ASSIGN_TO) :
                        alt23 = 4
                    else:
                        nvae = NoViableAltException("", 23, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerBackend.g:291:9: ID
                    pass 
                    ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2520)

                    #action start
                    value = ID54.text 
                    #action end



                elif alt23 == 2:
                    # grammar/ShyRecognizerBackend.g:292:9: EXPRESSION
                    pass 
                    EXPRESSION55 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2532)

                    #action start
                    value = EXPRESSION55.text 
                    #action end



                elif alt23 == 3:
                    # grammar/ShyRecognizerBackend.g:293:9: STRING
                    pass 
                    STRING56 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2544)

                    #action start
                    value = STRING56.text 
                    #action end



                elif alt23 == 4:
                    # grammar/ShyRecognizerBackend.g:294:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2556)
                    num_whole57 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole57 
                    #action end



                elif alt23 == 5:
                    # grammar/ShyRecognizerBackend.g:295:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2568)
                    num_fract58 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract58 
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
    # grammar/ShyRecognizerBackend.g:298:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID59 = None
        consts_items60 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:301:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:301:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts2609)

                self.match(self.input, DOWN, None)
                ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2611)

                self._state.following.append(self.FOLLOW_consts_items_in_consts2613)
                consts_items60 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID59.text , consts_items60 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:305:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item61 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:308:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:308:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:308:9: ( consts_item )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA24_0 <= TREE_NUM_WHOLE)) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerBackend.g:308:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2668)
                        consts_item61 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item61 is not None) and [consts_item61.name] or [None])[0] ] = ((consts_item61 is not None) and [consts_item61.value] or [None])[0] 
                        #action end



                    else:
                        if cnt24 >= 1:
                            break #loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1





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
    # grammar/ShyRecognizerBackend.g:313:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID62 = None
        ID64 = None
        ID66 = None
        EXPRESSION67 = None
        num_whole63 = None

        num_fract65 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:315:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt25 = 3
                LA25 = self.input.LA(1)
                if LA25 == TREE_NUM_WHOLE:
                    alt25 = 1
                elif LA25 == TREE_NUM_FRACT:
                    alt25 = 2
                elif LA25 == TREE_EXPRESSION:
                    alt25 = 3
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # grammar/ShyRecognizerBackend.g:315:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2723)

                    self.match(self.input, DOWN, None)
                    ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2725)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2727)
                    num_whole63 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID62.text , num_whole63 
                    #action end



                elif alt25 == 2:
                    # grammar/ShyRecognizerBackend.g:317:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2755)

                    self.match(self.input, DOWN, None)
                    ID64 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2757)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2759)
                    num_fract65 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID64.text , num_fract65 
                    #action end



                elif alt25 == 3:
                    # grammar/ShyRecognizerBackend.g:319:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2787)

                    self.match(self.input, DOWN, None)
                    ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2789)

                    EXPRESSION67 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2791)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID66.text , EXPRESSION67.text 
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
    # grammar/ShyRecognizerBackend.g:323:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID68 = None
        types_items69 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:326:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:326:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2846)

                self.match(self.input, DOWN, None)
                ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_types2848)

                self._state.following.append(self.FOLLOW_types_items_in_types2850)
                types_items69 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID68.text , types_items69 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:330:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item70 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:333:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:333:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:333:9: ( types_item )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == TREE_TYPES_ITEM) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerBackend.g:333:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2905)
                        types_item70 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item70 is not None) and [types_item70.name] or [None])[0] ] = ((types_item70 is not None) and [types_item70.value] or [None])[0] 
                        #action end



                    else:
                        if cnt26 >= 1:
                            break #loop26

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1





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
    # grammar/ShyRecognizerBackend.g:338:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID71 = None
        attrs_hints72 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:340:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:340:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2960)

                self.match(self.input, DOWN, None)
                ID71 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2962)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2964)
                attrs_hints72 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID71.text , attrs_hints72 
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
    # grammar/ShyRecognizerBackend.g:344:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID73 = None
        messages_items74 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:347:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:347:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages3019)

                self.match(self.input, DOWN, None)
                ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_messages3021)

                self._state.following.append(self.FOLLOW_messages_items_in_messages3023)
                messages_items74 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID73.text , messages_items74 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:351:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item75 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:354:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:354:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:354:9: ( messages_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == TREE_MESSAGES_ITEM) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerBackend.g:354:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items3078)
                        messages_item75 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value = merge ( value, messages_item75 ) 
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

    # $ANTLR end "messages_items"



    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerBackend.g:359:1: messages_item returns [ value ] : ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? ) ;
    def messages_item(self, ):
        value = None


        ID76 = None
        a = None

        c = None

        b = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:362:5: ( ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? ) )
                # grammar/ShyRecognizerBackend.g:362:9: ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3143)

                self.match(self.input, DOWN, None)
                ID76 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3145)

                # grammar/ShyRecognizerBackend.g:363:13: ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == TREE_MESSAGES_ITEM_RECEIVE) :
                    alt28 = 1
                if alt28 == 1:
                    # grammar/ShyRecognizerBackend.g:363:15: TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_RECEIVE, self.FOLLOW_TREE_MESSAGES_ITEM_RECEIVE_in_messages_item3161)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3167)
                    a = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'receive' : { ID76.text : a } } )
                                    
                    #action end





                # grammar/ShyRecognizerBackend.g:369:13: ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == TREE_MESSAGES_ITEM_REQUEST) :
                    alt29 = 1
                if alt29 == 1:
                    # grammar/ShyRecognizerBackend.g:369:15: TREE_MESSAGES_ITEM_REQUEST c= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_REQUEST, self.FOLLOW_TREE_MESSAGES_ITEM_REQUEST_in_messages_item3217)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3223)
                    c = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'request' : { ID76.text : c } } )
                                    
                    #action end





                # grammar/ShyRecognizerBackend.g:375:13: ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == TREE_MESSAGES_ITEM_REPLY) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerBackend.g:375:15: TREE_MESSAGES_ITEM_REPLY b= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_REPLY, self.FOLLOW_TREE_MESSAGES_ITEM_REPLY_in_messages_item3273)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3279)
                    b = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'reply' : { ID76.text : b } } )
                                    
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
    # grammar/ShyRecognizerBackend.g:384:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID77 = None
        attrs_hints78 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:386:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:386:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars3352)

                self.match(self.input, DOWN, None)
                ID77 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3354)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3356)
                attrs_hints78 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID77.text , attrs_hints78 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:390:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint79 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:393:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:393:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3409)

                # grammar/ShyRecognizerBackend.g:393:26: ( attr_hint )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == TREE_ATTR_HINT) :
                        alt31 = 1


                    if alt31 == 1:
                        # grammar/ShyRecognizerBackend.g:393:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3413)
                        attr_hint79 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value += attr_hint79 
                        #action end



                    else:
                        break #loop31





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:396:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID80 = None
        ID81 = None
        hint82 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:399:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == TREE_ATTR_HINT) :
                    LA34_1 = self.input.LA(2)

                    if (LA34_1 == 2) :
                        LA34_2 = self.input.LA(3)

                        if (LA34_2 == TREE_HINT_NONE) :
                            alt34 = 1
                        elif (LA34_2 == TREE_HINT) :
                            alt34 = 2
                        else:
                            nvae = NoViableAltException("", 34, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 34, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae


                if alt34 == 1:
                    # grammar/ShyRecognizerBackend.g:399:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3458)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint3460)

                    # grammar/ShyRecognizerBackend.g:399:42: ( ^( TREE_ATTR ID ) )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == TREE_ATTR) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerBackend.g:399:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3466)

                            self.match(self.input, DOWN, None)
                            ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3468)

                            self.match(self.input, UP, None)


                            #action start
                            value . append ( { ID80.text : dict ( ) } ) 
                            #action end



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


                    self.match(self.input, UP, None)



                elif alt34 == 2:
                    # grammar/ShyRecognizerBackend.g:402:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3510)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3512)
                    hint82 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:402:32: ( ^( TREE_ATTR ID ) )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == TREE_ATTR) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerBackend.g:402:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3518)

                            self.match(self.input, DOWN, None)
                            ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3520)

                            self.match(self.input, UP, None)


                            #action start
                            value . append ( { ID81.text : hint82 } ) 
                            #action end



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:407:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID83 = None
        ID84 = None
        hint_args85 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:410:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == TREE_HINT) :
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == 2) :
                        LA35_2 = self.input.LA(3)

                        if (LA35_2 == ID) :
                            LA35_3 = self.input.LA(4)

                            if (LA35_3 == 3) :
                                alt35 = 1
                            elif (LA35_3 == ID or LA35_3 == UNDERSCORE) :
                                alt35 = 2
                            else:
                                nvae = NoViableAltException("", 35, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerBackend.g:410:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3589)

                    self.match(self.input, DOWN, None)
                    ID83 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3591)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID83.text ] = list ( ) 
                    #action end



                elif alt35 == 2:
                    # grammar/ShyRecognizerBackend.g:412:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3619)

                    self.match(self.input, DOWN, None)
                    ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3621)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint3623)
                    hint_args85 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID84.text ] = hint_args85 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:416:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg86 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:419:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:419:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:419:9: ( hint_arg )+
                cnt36 = 0
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == ID or LA36_0 == UNDERSCORE) :
                        alt36 = 1


                    if alt36 == 1:
                        # grammar/ShyRecognizerBackend.g:419:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args3678)
                        hint_arg86 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg86 ) 
                        #action end



                    else:
                        if cnt36 >= 1:
                            break #loop36

                        eee = EarlyExitException(36, self.input)
                        raise eee

                    cnt36 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:422:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID87 = None
        UNDERSCORE88 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:424:5: ( ID | UNDERSCORE )
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == ID) :
                    alt37 = 1
                elif (LA37_0 == UNDERSCORE) :
                    alt37 = 2
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # grammar/ShyRecognizerBackend.g:424:9: ID
                    pass 
                    ID87 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg3711)

                    #action start
                    value = ID87.text 
                    #action end



                elif alt37 == 2:
                    # grammar/ShyRecognizerBackend.g:425:9: UNDERSCORE
                    pass 
                    UNDERSCORE88 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg3723)

                    #action start
                    value = UNDERSCORE88.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:428:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS89 = None
        NUMBER90 = None
        NUMBER91 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:430:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == MINUS) :
                    alt38 = 1
                elif (LA38_0 == NUMBER) :
                    alt38 = 2
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # grammar/ShyRecognizerBackend.g:430:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:430:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:430:11: MINUS NUMBER
                    pass 
                    MINUS89 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3754)

                    NUMBER90 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3756)




                    #action start
                    value = int ( MINUS89.text + NUMBER90.text ) 
                    #action end



                elif alt38 == 2:
                    # grammar/ShyRecognizerBackend.g:432:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:432:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:432:11: NUMBER
                    pass 
                    NUMBER91 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3784)




                    #action start
                    value = int ( NUMBER91.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:436:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS92 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:438:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:438:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:438:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:438:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS92 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3829)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3835)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3837)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3843)




                    #action start
                                
                    value = Fraction ( int ( MINUS92.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt39 == 2:
                    # grammar/ShyRecognizerBackend.g:443:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:443:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:443:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3875)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3877)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3883)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 44, 51, 56, 67, 77, 78, 80])
    FOLLOW_stateless_in_start114 = frozenset([1, 44, 51, 56, 67, 77, 78, 80])
    FOLLOW_trace_in_start141 = frozenset([1, 44, 51, 56, 67, 77, 78, 80])
    FOLLOW_consts_in_start168 = frozenset([1, 44, 51, 56, 67, 77, 78, 80])
    FOLLOW_types_in_start194 = frozenset([1, 44, 51, 56, 67, 77, 78, 80])
    FOLLOW_messages_in_start220 = frozenset([1, 44, 51, 56, 67, 77, 78, 80])
    FOLLOW_vars_in_start246 = frozenset([1, 44, 51, 56, 67, 77, 78, 80])
    FOLLOW_TREE_TRACE_in_trace301 = frozenset([2])
    FOLLOW_ID_in_trace303 = frozenset([3, 63])
    FOLLOW_trace_item_in_trace333 = frozenset([3, 63])
    FOLLOW_proc_in_trace_item404 = frozenset([1])
    FOLLOW_TREE_STATELESS_in_stateless447 = frozenset([2])
    FOLLOW_ID_in_stateless449 = frozenset([3, 63])
    FOLLOW_stateless_item_in_stateless479 = frozenset([3, 63])
    FOLLOW_proc_in_stateless_item550 = frozenset([1])
    FOLLOW_TREE_MODULE_in_module593 = frozenset([2])
    FOLLOW_ID_in_module595 = frozenset([3, 57, 63, 65, 66])
    FOLLOW_module_item_in_module625 = frozenset([3, 57, 63, 65, 66])
    FOLLOW_module_queue_in_module_item696 = frozenset([1])
    FOLLOW_proc_in_module_item721 = frozenset([1])
    FOLLOW_receive_in_module_item745 = frozenset([1])
    FOLLOW_request_in_module_item769 = frozenset([1])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue812 = frozenset([2])
    FOLLOW_ID_in_module_queue814 = frozenset([3])
    FOLLOW_TREE_REQUEST_in_request857 = frozenset([2])
    FOLLOW_ID_in_request871 = frozenset([3, 50, 68])
    FOLLOW_local_vars_in_request905 = frozenset([3, 68])
    FOLLOW_statements_in_request955 = frozenset([3])
    FOLLOW_TREE_RECEIVE_in_receive1038 = frozenset([2])
    FOLLOW_ID_in_receive1052 = frozenset([3, 50, 68])
    FOLLOW_local_vars_in_receive1086 = frozenset([3, 68])
    FOLLOW_statements_in_receive1136 = frozenset([3])
    FOLLOW_TREE_PROC_in_proc1219 = frozenset([2])
    FOLLOW_ID_in_proc1233 = frozenset([3, 50, 64, 68])
    FOLLOW_proc_args_in_proc1267 = frozenset([3, 50, 68])
    FOLLOW_local_vars_in_proc1317 = frozenset([3, 68])
    FOLLOW_statements_in_proc1367 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args1440 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args1442 = frozenset([3])
    FOLLOW_TREE_LOCAL_VARS_in_local_vars1487 = frozenset([2])
    FOLLOW_attrs_hints_in_local_vars1489 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements1544 = frozenset([2])
    FOLLOW_statement_in_statements1548 = frozenset([3, 69, 71, 74, 75, 76])
    FOLLOW_statement_call_in_statement1604 = frozenset([1])
    FOLLOW_statement_if_in_statement1628 = frozenset([1])
    FOLLOW_statement_assign_in_statement1652 = frozenset([1])
    FOLLOW_statement_with_in_statement1676 = frozenset([1])
    FOLLOW_statement_while_in_statement1700 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1743 = frozenset([2])
    FOLLOW_ID_in_statement_with1745 = frozenset([68])
    FOLLOW_statements_in_statement_with1747 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1798 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1814 = frozenset([18, 19, 23, 27, 36, 70])
    FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1862 = frozenset([19])
    FOLLOW_ID_in_statement_assign1878 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1961 = frozenset([2])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1979 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_if1981 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_if2035 = frozenset([2])
    FOLLOW_statements_in_statement_if2037 = frozenset([3])
    FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2112 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_while2114 = frozenset([3])
    FOLLOW_condition_any_in_conditional_ops2157 = frozenset([68])
    FOLLOW_statements_in_conditional_ops2159 = frozenset([1])
    FOLLOW_condition_all_in_conditional_ops2183 = frozenset([68])
    FOLLOW_statements_in_conditional_ops2185 = frozenset([1])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any2238 = frozenset([2])
    FOLLOW_statement_call_in_condition_any2254 = frozenset([3, 71])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all2329 = frozenset([2])
    FOLLOW_statement_call_in_condition_all2345 = frozenset([3, 71])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call2410 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call2412 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args2467 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_ID_in_arbitrary_value2520 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2532 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2544 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2556 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2568 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts2609 = frozenset([2])
    FOLLOW_ID_in_consts2611 = frozenset([47, 58, 59])
    FOLLOW_consts_items_in_consts2613 = frozenset([3])
    FOLLOW_consts_item_in_consts_items2668 = frozenset([1, 47, 58, 59])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2723 = frozenset([2])
    FOLLOW_ID_in_consts_item2725 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2727 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2755 = frozenset([2])
    FOLLOW_ID_in_consts_item2757 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2759 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2787 = frozenset([2])
    FOLLOW_ID_in_consts_item2789 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2791 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2846 = frozenset([2])
    FOLLOW_ID_in_types2848 = frozenset([79])
    FOLLOW_types_items_in_types2850 = frozenset([3])
    FOLLOW_types_item_in_types_items2905 = frozenset([1, 79])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2960 = frozenset([2])
    FOLLOW_ID_in_types_item2962 = frozenset([40])
    FOLLOW_attrs_hints_in_types_item2964 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages3019 = frozenset([2])
    FOLLOW_ID_in_messages3021 = frozenset([52])
    FOLLOW_messages_items_in_messages3023 = frozenset([3])
    FOLLOW_messages_item_in_messages_items3078 = frozenset([1, 52])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3143 = frozenset([2])
    FOLLOW_ID_in_messages_item3145 = frozenset([3, 53, 54, 55])
    FOLLOW_TREE_MESSAGES_ITEM_RECEIVE_in_messages_item3161 = frozenset([40])
    FOLLOW_attrs_hints_in_messages_item3167 = frozenset([3, 54, 55])
    FOLLOW_TREE_MESSAGES_ITEM_REQUEST_in_messages_item3217 = frozenset([40])
    FOLLOW_attrs_hints_in_messages_item3223 = frozenset([3, 54])
    FOLLOW_TREE_MESSAGES_ITEM_REPLY_in_messages_item3273 = frozenset([40])
    FOLLOW_attrs_hints_in_messages_item3279 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars3352 = frozenset([2])
    FOLLOW_ID_in_vars3354 = frozenset([40])
    FOLLOW_attrs_hints_in_vars3356 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3409 = frozenset([1, 41])
    FOLLOW_attr_hint_in_attrs_hints3413 = frozenset([1, 41])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3458 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint3460 = frozenset([39])
    FOLLOW_TREE_ATTR_in_attr_hint3466 = frozenset([2])
    FOLLOW_ID_in_attr_hint3468 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3510 = frozenset([2])
    FOLLOW_hint_in_attr_hint3512 = frozenset([39])
    FOLLOW_TREE_ATTR_in_attr_hint3518 = frozenset([2])
    FOLLOW_ID_in_attr_hint3520 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3589 = frozenset([2])
    FOLLOW_ID_in_hint3591 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3619 = frozenset([2])
    FOLLOW_ID_in_hint3621 = frozenset([19, 82])
    FOLLOW_hint_args_in_hint3623 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args3678 = frozenset([1, 19, 82])
    FOLLOW_ID_in_hint_arg3711 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg3723 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3754 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3756 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole3784 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3829 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3835 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3837 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3843 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract3875 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3877 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3883 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
