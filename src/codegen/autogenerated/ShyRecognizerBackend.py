# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-03 22:28:19

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


    class module_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.module_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "module"
    # grammar/ShyRecognizerBackend.g:57:1: module returns [ title , content ] : ^( TREE_MODULE ID ( module_item )* ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        ID8 = None
        module_item9 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:59:5: ( ^( TREE_MODULE ID ( module_item )* ) )
                # grammar/ShyRecognizerBackend.g:59:9: ^( TREE_MODULE ID ( module_item )* )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module301)

                self.match(self.input, DOWN, None)
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_module303)

                #action start
                retval.title , retval.content = ID8.text , dict ( ) 
                #action end


                # grammar/ShyRecognizerBackend.g:61:13: ( module_item )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == TREE_MODULE_QUEUE or LA2_0 == TREE_PROC or (TREE_RECEIVE <= LA2_0 <= TREE_REQUEST)) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyRecognizerBackend.g:61:15: module_item
                        pass 
                        self._state.following.append(self.FOLLOW_module_item_in_module333)
                        module_item9 = self.module_item()

                        self._state.following.pop()

                        #action start
                        retval.content = merge ( retval.content , module_item9 ) 
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

    # $ANTLR end "module"



    # $ANTLR start "module_item"
    # grammar/ShyRecognizerBackend.g:67:1: module_item returns [ value ] : ( module_queue | proc | receive | request );
    def module_item(self, ):
        value = None


        module_queue10 = None

        proc11 = None

        receive12 = None

        request13 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:69:5: ( module_queue | proc | receive | request )
                alt3 = 4
                LA3 = self.input.LA(1)
                if LA3 == TREE_MODULE_QUEUE:
                    alt3 = 1
                elif LA3 == TREE_PROC:
                    alt3 = 2
                elif LA3 == TREE_RECEIVE:
                    alt3 = 3
                elif LA3 == TREE_REQUEST:
                    alt3 = 4
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyRecognizerBackend.g:69:9: module_queue
                    pass 
                    self._state.following.append(self.FOLLOW_module_queue_in_module_item404)
                    module_queue10 = self.module_queue()

                    self._state.following.pop()

                    #action start
                    value = { 'module_queue' : module_queue10 } 
                    #action end



                elif alt3 == 2:
                    # grammar/ShyRecognizerBackend.g:71:9: proc
                    pass 
                    self._state.following.append(self.FOLLOW_proc_in_module_item429)
                    proc11 = self.proc()

                    self._state.following.pop()

                    #action start
                    value = { 'proc' : { ((proc11 is not None) and [proc11.title] or [None])[0] : ((proc11 is not None) and [proc11.content] or [None])[0] } } 
                    #action end



                elif alt3 == 3:
                    # grammar/ShyRecognizerBackend.g:73:9: receive
                    pass 
                    self._state.following.append(self.FOLLOW_receive_in_module_item453)
                    receive12 = self.receive()

                    self._state.following.pop()

                    #action start
                    value = { 'receive' : { ((receive12 is not None) and [receive12.title] or [None])[0] : ((receive12 is not None) and [receive12.content] or [None])[0] } } 
                    #action end



                elif alt3 == 4:
                    # grammar/ShyRecognizerBackend.g:75:9: request
                    pass 
                    self._state.following.append(self.FOLLOW_request_in_module_item477)
                    request13 = self.request()

                    self._state.following.pop()

                    #action start
                    value = { 'request' : { ((request13 is not None) and [request13.title] or [None])[0] : ((request13 is not None) and [request13.content] or [None])[0] } } 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module_item"



    # $ANTLR start "module_queue"
    # grammar/ShyRecognizerBackend.g:79:1: module_queue returns [ value ] : ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        value = None


        ID14 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:81:5: ( ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerBackend.g:81:9: ^( TREE_MODULE_QUEUE ID )
                pass 
                self.match(self.input, TREE_MODULE_QUEUE, self.FOLLOW_TREE_MODULE_QUEUE_in_module_queue520)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue522)

                self.match(self.input, UP, None)


                #action start
                value = ID14.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module_queue"


    class trace_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.trace_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "trace"
    # grammar/ShyRecognizerBackend.g:84:1: trace returns [ title , content ] : ( ^( TREE_TRACE ID ) | ^( TREE_TRACE ID procs ) );
    def trace(self, ):
        retval = self.trace_return()
        retval.start = self.input.LT(1)


        ID15 = None
        ID16 = None
        procs17 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:86:5: ( ^( TREE_TRACE ID ) | ^( TREE_TRACE ID procs ) )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_TRACE) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 2) :
                        LA4_2 = self.input.LA(3)

                        if (LA4_2 == ID) :
                            LA4_3 = self.input.LA(4)

                            if (LA4_3 == 3) :
                                alt4 = 1
                            elif (LA4_3 == TREE_PROC) :
                                alt4 = 2
                            else:
                                nvae = NoViableAltException("", 4, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 4, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # grammar/ShyRecognizerBackend.g:86:9: ^( TREE_TRACE ID )
                    pass 
                    self.match(self.input, TREE_TRACE, self.FOLLOW_TREE_TRACE_in_trace555)

                    self.match(self.input, DOWN, None)
                    ID15 = self.match(self.input, ID, self.FOLLOW_ID_in_trace557)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID15.text , dict ( ) 
                    #action end



                elif alt4 == 2:
                    # grammar/ShyRecognizerBackend.g:88:9: ^( TREE_TRACE ID procs )
                    pass 
                    self.match(self.input, TREE_TRACE, self.FOLLOW_TREE_TRACE_in_trace585)

                    self.match(self.input, DOWN, None)
                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_trace587)

                    self._state.following.append(self.FOLLOW_procs_in_trace589)
                    procs17 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID16.text , procs17 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "trace"


    class stateless_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.stateless_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "stateless"
    # grammar/ShyRecognizerBackend.g:92:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID18 = None
        ID19 = None
        procs20 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:94:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_STATELESS) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == 2) :
                        LA5_2 = self.input.LA(3)

                        if (LA5_2 == ID) :
                            LA5_3 = self.input.LA(4)

                            if (LA5_3 == 3) :
                                alt5 = 1
                            elif (LA5_3 == TREE_PROC) :
                                alt5 = 2
                            else:
                                nvae = NoViableAltException("", 5, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 5, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 5, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:94:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless634)

                    self.match(self.input, DOWN, None)
                    ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless636)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID18.text , dict ( ) 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyRecognizerBackend.g:96:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless664)

                    self.match(self.input, DOWN, None)
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless666)

                    self._state.following.append(self.FOLLOW_procs_in_stateless668)
                    procs20 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID19.text , procs20 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"


    class request_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.request_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "request"
    # grammar/ShyRecognizerBackend.g:100:1: request returns [ title , content ] : ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) ;
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        ID21 = None
        local_vars22 = None

        statements23 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:103:5: ( ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:103:9: ^( TREE_REQUEST ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_REQUEST, self.FOLLOW_TREE_REQUEST_in_request723)

                self.match(self.input, DOWN, None)
                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_request737)

                #action start
                retval.title = ID21.text 
                #action end


                # grammar/ShyRecognizerBackend.g:106:13: ( local_vars )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_LOCAL_VARS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:106:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_request771)
                    local_vars22 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars22 
                    #action end





                # grammar/ShyRecognizerBackend.g:109:13: ( statements )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == TREE_STATEMENTS) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:109:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_request821)
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
    # grammar/ShyRecognizerBackend.g:115:1: receive returns [ title , content ] : ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) ;
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        ID24 = None
        local_vars25 = None

        statements26 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:118:5: ( ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:118:9: ^( TREE_RECEIVE ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_RECEIVE, self.FOLLOW_TREE_RECEIVE_in_receive904)

                self.match(self.input, DOWN, None)
                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_receive918)

                #action start
                retval.title = ID24.text 
                #action end


                # grammar/ShyRecognizerBackend.g:121:13: ( local_vars )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == TREE_LOCAL_VARS) :
                    alt8 = 1
                if alt8 == 1:
                    # grammar/ShyRecognizerBackend.g:121:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_receive952)
                    local_vars25 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars25 
                    #action end





                # grammar/ShyRecognizerBackend.g:124:13: ( statements )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == TREE_STATEMENTS) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:124:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_receive1002)
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



    # $ANTLR start "procs"
    # grammar/ShyRecognizerBackend.g:130:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc27 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:133:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:133:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:133:9: ( proc )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_PROC) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:133:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs1085)
                        proc27 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc27 is not None) and [proc27.title] or [None])[0] ] = ((proc27 is not None) and [proc27.content] or [None])[0] 
                        #action end



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "procs"


    class proc_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.proc_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "proc"
    # grammar/ShyRecognizerBackend.g:136:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID28 = None
        proc_args29 = None

        local_vars30 = None

        statements31 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:139:5: ( ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:139:9: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc1130)

                self.match(self.input, DOWN, None)
                ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_proc1144)

                #action start
                retval.title = ID28.text 
                #action end


                # grammar/ShyRecognizerBackend.g:142:13: ( proc_args )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_PROC_ARGS) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:142:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc1178)
                    proc_args29 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args29 
                    #action end





                # grammar/ShyRecognizerBackend.g:145:13: ( local_vars )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == TREE_LOCAL_VARS) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:145:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_proc1228)
                    local_vars30 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars30 
                    #action end





                # grammar/ShyRecognizerBackend.g:148:13: ( statements )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == TREE_STATEMENTS) :
                    alt13 = 1
                if alt13 == 1:
                    # grammar/ShyRecognizerBackend.g:148:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc1278)
                    statements31 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements31 
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
    # grammar/ShyRecognizerBackend.g:154:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints32 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:156:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:156:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args1351)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args1353)
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

    # $ANTLR end "proc_args"



    # $ANTLR start "local_vars"
    # grammar/ShyRecognizerBackend.g:160:1: local_vars returns [ value ] : ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        value = None


        attrs_hints33 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:162:5: ( ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:162:9: ^( TREE_LOCAL_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_LOCAL_VARS, self.FOLLOW_TREE_LOCAL_VARS_in_local_vars1398)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars1400)
                attrs_hints33 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints33 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "local_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:166:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement34 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:169:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:169:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements1455)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:169:28: ( statement )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TREE_STATEMENT_ASSIGN or LA14_0 == TREE_STATEMENT_CALL or (TREE_STATEMENT_IF <= LA14_0 <= TREE_STATEMENT_WITH)) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:169:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1459)
                        statement34 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement34 ) 
                        #action end



                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statements"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:174:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with | statement_while );
    def statement(self, ):
        value = None


        statement_call35 = None

        statement_if36 = None

        statement_assign37 = None

        statement_with38 = None

        statement_while39 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:176:5: ( statement_call | statement_if | statement_assign | statement_with | statement_while )
                alt15 = 5
                LA15 = self.input.LA(1)
                if LA15 == TREE_STATEMENT_CALL:
                    alt15 = 1
                elif LA15 == TREE_STATEMENT_IF:
                    alt15 = 2
                elif LA15 == TREE_STATEMENT_ASSIGN:
                    alt15 = 3
                elif LA15 == TREE_STATEMENT_WITH:
                    alt15 = 4
                elif LA15 == TREE_STATEMENT_WHILE:
                    alt15 = 5
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:176:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement1515)
                    statement_call35 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call35 
                    #action end



                elif alt15 == 2:
                    # grammar/ShyRecognizerBackend.g:178:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement1539)
                    statement_if36 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if36 
                    #action end



                elif alt15 == 3:
                    # grammar/ShyRecognizerBackend.g:180:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1563)
                    statement_assign37 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign37 
                    #action end



                elif alt15 == 4:
                    # grammar/ShyRecognizerBackend.g:182:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1587)
                    statement_with38 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with38 
                    #action end



                elif alt15 == 5:
                    # grammar/ShyRecognizerBackend.g:184:9: statement_while
                    pass 
                    self._state.following.append(self.FOLLOW_statement_while_in_statement1611)
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
    # grammar/ShyRecognizerBackend.g:188:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID40 = None
        statements41 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:190:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:190:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1654)

                self.match(self.input, DOWN, None)
                ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1656)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1658)
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
    # grammar/ShyRecognizerBackend.g:194:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID43 = None
        arbitrary_value42 = None


        value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:197:5: ( ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:197:9: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1709)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:198:13: ( arbitrary_value )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA16_0 <= ID) or LA16_0 == MINUS or LA16_0 == NUMBER or LA16_0 == STRING) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:198:15: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1725)
                        arbitrary_value42 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                                        
                        value [ 'assign' ] [ 'from' ] . append (
                            arbitrary_value42 )
                                        
                        #action end



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1


                self.match(self.input, TREE_STATEMENT_ASSIGN_TO, self.FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1773)

                # grammar/ShyRecognizerBackend.g:205:13: ( ID )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == ID) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:205:15: ID
                        pass 
                        ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1789)

                        #action start
                                        
                        value [ 'assign' ] [ 'to' ] . append (
                            ID43.text )
                                        
                        #action end



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:214:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) ;
    def statement_if(self, ):
        value = None


        conditional_ops44 = None

        statements45 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:217:5: ( ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) )
                # grammar/ShyRecognizerBackend.g:217:9: ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1872)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:218:13: ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == TREE_STATEMENT_ELIF) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerBackend.g:218:15: ^( TREE_STATEMENT_ELIF conditional_ops )
                        pass 
                        self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1890)

                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_conditional_ops_in_statement_if1892)
                        conditional_ops44 = self.conditional_ops()

                        self._state.following.pop()

                        self.match(self.input, UP, None)


                        #action start
                        value [ 'if' ] . append ( conditional_ops44 ) 
                        #action end



                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1


                # grammar/ShyRecognizerBackend.g:221:13: ( ^( TREE_STATEMENT_ELSE statements ) )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == TREE_STATEMENT_ELSE) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:221:15: ^( TREE_STATEMENT_ELSE statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1946)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statements_in_statement_if1948)
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
    # grammar/ShyRecognizerBackend.g:227:1: statement_while returns [ value ] : ^( TREE_STATEMENT_WHILE conditional_ops ) ;
    def statement_while(self, ):
        value = None


        conditional_ops46 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:229:5: ( ^( TREE_STATEMENT_WHILE conditional_ops ) )
                # grammar/ShyRecognizerBackend.g:229:9: ^( TREE_STATEMENT_WHILE conditional_ops )
                pass 
                self.match(self.input, TREE_STATEMENT_WHILE, self.FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2023)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_conditional_ops_in_statement_while2025)
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
    # grammar/ShyRecognizerBackend.g:233:1: conditional_ops returns [ value ] : ( condition_any statements | condition_all statements );
    def conditional_ops(self, ):
        value = None


        condition_any47 = None

        statements48 = None

        condition_all49 = None

        statements50 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:235:5: ( condition_any statements | condition_all statements )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == TREE_CONDITION_ANY) :
                    alt20 = 1
                elif (LA20_0 == TREE_CONDITION_ALL) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammar/ShyRecognizerBackend.g:235:9: condition_any statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_any_in_conditional_ops2068)
                    condition_any47 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2070)
                    statements48 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'any' : condition_any47 ,
                       'ops' : statements48 }
                                
                    #action end



                elif alt20 == 2:
                    # grammar/ShyRecognizerBackend.g:240:9: condition_all statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_all_in_conditional_ops2094)
                    condition_all49 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2096)
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
    # grammar/ShyRecognizerBackend.g:247:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call51 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:250:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:250:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any2149)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:251:13: ( statement_call )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_STATEMENT_CALL) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:251:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any2165)
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

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:256:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call52 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:259:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:259:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all2240)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:260:13: ( statement_call )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == TREE_STATEMENT_CALL) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:260:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all2256)
                        statement_call52 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call52 ) 
                        #action end



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:265:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args53 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:267:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:267:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call2321)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call2323)
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
    # grammar/ShyRecognizerBackend.g:271:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value54 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:274:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:274:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:274:9: ( arbitrary_value )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER or LA23_0 == STRING) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerBackend.g:274:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2378)
                        arbitrary_value54 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value54 ) 
                        #action end



                    else:
                        break #loop23





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:279:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID55 = None
        EXPRESSION56 = None
        STRING57 = None
        num_whole58 = None

        num_fract59 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:281:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
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
                    # grammar/ShyRecognizerBackend.g:281:9: ID
                    pass 
                    ID55 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2431)

                    #action start
                    value = ID55.text 
                    #action end



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:282:9: EXPRESSION
                    pass 
                    EXPRESSION56 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2443)

                    #action start
                    value = EXPRESSION56.text 
                    #action end



                elif alt24 == 3:
                    # grammar/ShyRecognizerBackend.g:283:9: STRING
                    pass 
                    STRING57 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2455)

                    #action start
                    value = STRING57.text 
                    #action end



                elif alt24 == 4:
                    # grammar/ShyRecognizerBackend.g:284:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2467)
                    num_whole58 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole58 
                    #action end



                elif alt24 == 5:
                    # grammar/ShyRecognizerBackend.g:285:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2479)
                    num_fract59 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract59 
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
    # grammar/ShyRecognizerBackend.g:288:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID60 = None
        consts_items61 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:291:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:291:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts2520)

                self.match(self.input, DOWN, None)
                ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2522)

                self._state.following.append(self.FOLLOW_consts_items_in_consts2524)
                consts_items61 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID60.text , consts_items61 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:295:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item62 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:298:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:298:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:298:9: ( consts_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA25_0 <= TREE_NUM_WHOLE)) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerBackend.g:298:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2579)
                        consts_item62 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item62 is not None) and [consts_item62.name] or [None])[0] ] = ((consts_item62 is not None) and [consts_item62.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:303:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID63 = None
        ID65 = None
        ID67 = None
        EXPRESSION68 = None
        num_whole64 = None

        num_fract66 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:305:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerBackend.g:305:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2634)

                    self.match(self.input, DOWN, None)
                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2636)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2638)
                    num_whole64 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID63.text , num_whole64 
                    #action end



                elif alt26 == 2:
                    # grammar/ShyRecognizerBackend.g:307:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2666)

                    self.match(self.input, DOWN, None)
                    ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2668)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2670)
                    num_fract66 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID65.text , num_fract66 
                    #action end



                elif alt26 == 3:
                    # grammar/ShyRecognizerBackend.g:309:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2698)

                    self.match(self.input, DOWN, None)
                    ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2700)

                    EXPRESSION68 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2702)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID67.text , EXPRESSION68.text 
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
    # grammar/ShyRecognizerBackend.g:313:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID69 = None
        types_items70 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:316:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:316:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2757)

                self.match(self.input, DOWN, None)
                ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_types2759)

                self._state.following.append(self.FOLLOW_types_items_in_types2761)
                types_items70 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID69.text , types_items70 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:320:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item71 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:323:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:323:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:323:9: ( types_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == TREE_TYPES_ITEM) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerBackend.g:323:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2816)
                        types_item71 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item71 is not None) and [types_item71.name] or [None])[0] ] = ((types_item71 is not None) and [types_item71.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:328:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID72 = None
        attrs_hints73 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:330:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:330:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2871)

                self.match(self.input, DOWN, None)
                ID72 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2873)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2875)
                attrs_hints73 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID72.text , attrs_hints73 
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
    # grammar/ShyRecognizerBackend.g:334:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID74 = None
        messages_items75 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:337:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:337:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2930)

                self.match(self.input, DOWN, None)
                ID74 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2932)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2934)
                messages_items75 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID74.text , messages_items75 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:341:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item76 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:344:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:344:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:344:9: ( messages_item )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == TREE_MESSAGES_ITEM) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerBackend.g:344:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2989)
                        messages_item76 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value = merge ( value, messages_item76 ) 
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
    # grammar/ShyRecognizerBackend.g:349:1: messages_item returns [ value ] : ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? ) ;
    def messages_item(self, ):
        value = None


        ID77 = None
        a = None

        c = None

        b = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:352:5: ( ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? ) )
                # grammar/ShyRecognizerBackend.g:352:9: ^( TREE_MESSAGES_ITEM ID ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )? ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )? ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )? )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3054)

                self.match(self.input, DOWN, None)
                ID77 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3056)

                # grammar/ShyRecognizerBackend.g:353:13: ( TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == TREE_MESSAGES_ITEM_RECEIVE) :
                    alt29 = 1
                if alt29 == 1:
                    # grammar/ShyRecognizerBackend.g:353:15: TREE_MESSAGES_ITEM_RECEIVE a= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_RECEIVE, self.FOLLOW_TREE_MESSAGES_ITEM_RECEIVE_in_messages_item3072)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3078)
                    a = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'receive' : { ID77.text : a } } )
                                    
                    #action end





                # grammar/ShyRecognizerBackend.g:359:13: ( TREE_MESSAGES_ITEM_REQUEST c= attrs_hints )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == TREE_MESSAGES_ITEM_REQUEST) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerBackend.g:359:15: TREE_MESSAGES_ITEM_REQUEST c= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_REQUEST, self.FOLLOW_TREE_MESSAGES_ITEM_REQUEST_in_messages_item3128)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3134)
                    c = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'request' : { ID77.text : c } } )
                                    
                    #action end





                # grammar/ShyRecognizerBackend.g:365:13: ( TREE_MESSAGES_ITEM_REPLY b= attrs_hints )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == TREE_MESSAGES_ITEM_REPLY) :
                    alt31 = 1
                if alt31 == 1:
                    # grammar/ShyRecognizerBackend.g:365:15: TREE_MESSAGES_ITEM_REPLY b= attrs_hints
                    pass 
                    self.match(self.input, TREE_MESSAGES_ITEM_REPLY, self.FOLLOW_TREE_MESSAGES_ITEM_REPLY_in_messages_item3184)

                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3190)
                    b = self.attrs_hints()

                    self._state.following.pop()

                    #action start
                                    
                    value = merge ( value ,
                        { 'reply' : { ID77.text : b } } )
                                    
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
    # grammar/ShyRecognizerBackend.g:374:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID78 = None
        attrs_hints79 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:376:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:376:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars3263)

                self.match(self.input, DOWN, None)
                ID78 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3265)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3267)
                attrs_hints79 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID78.text , attrs_hints79 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:380:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint80 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:383:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:383:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3320)

                # grammar/ShyRecognizerBackend.g:383:26: ( attr_hint )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == TREE_ATTR_HINT) :
                        alt32 = 1


                    if alt32 == 1:
                        # grammar/ShyRecognizerBackend.g:383:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3324)
                        attr_hint80 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint80 ) 
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
    # grammar/ShyRecognizerBackend.g:386:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID81 = None
        ID82 = None
        hint83 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:389:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
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
                    # grammar/ShyRecognizerBackend.g:389:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3369)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint3371)

                    # grammar/ShyRecognizerBackend.g:389:42: ( ^( TREE_ATTR ID ) )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == TREE_ATTR) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerBackend.g:389:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3377)

                            self.match(self.input, DOWN, None)
                            ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3379)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID81.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


                    self.match(self.input, UP, None)



                elif alt35 == 2:
                    # grammar/ShyRecognizerBackend.g:392:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3421)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3423)
                    hint83 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:392:32: ( ^( TREE_ATTR ID ) )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == TREE_ATTR) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerBackend.g:392:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3429)

                            self.match(self.input, DOWN, None)
                            ID82 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3431)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID82.text ] = hint83 
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
    # grammar/ShyRecognizerBackend.g:397:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID84 = None
        ID85 = None
        hint_args86 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:400:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
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
                    # grammar/ShyRecognizerBackend.g:400:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3500)

                    self.match(self.input, DOWN, None)
                    ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3502)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID84.text ] = list ( ) 
                    #action end



                elif alt36 == 2:
                    # grammar/ShyRecognizerBackend.g:402:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3530)

                    self.match(self.input, DOWN, None)
                    ID85 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3532)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint3534)
                    hint_args86 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID85.text ] = hint_args86 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:406:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg87 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:409:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:409:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:409:9: ( hint_arg )+
                cnt37 = 0
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == ID or LA37_0 == UNDERSCORE) :
                        alt37 = 1


                    if alt37 == 1:
                        # grammar/ShyRecognizerBackend.g:409:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args3589)
                        hint_arg87 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg87 ) 
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
    # grammar/ShyRecognizerBackend.g:412:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID88 = None
        UNDERSCORE89 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:414:5: ( ID | UNDERSCORE )
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
                    # grammar/ShyRecognizerBackend.g:414:9: ID
                    pass 
                    ID88 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg3622)

                    #action start
                    value = ID88.text 
                    #action end



                elif alt38 == 2:
                    # grammar/ShyRecognizerBackend.g:415:9: UNDERSCORE
                    pass 
                    UNDERSCORE89 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg3634)

                    #action start
                    value = UNDERSCORE89.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:418:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS90 = None
        NUMBER91 = None
        NUMBER92 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:420:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:420:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:420:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:420:11: MINUS NUMBER
                    pass 
                    MINUS90 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3665)

                    NUMBER91 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3667)




                    #action start
                    value = int ( MINUS90.text + NUMBER91.text ) 
                    #action end



                elif alt39 == 2:
                    # grammar/ShyRecognizerBackend.g:422:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:422:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:422:11: NUMBER
                    pass 
                    NUMBER92 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3695)




                    #action start
                    value = int ( NUMBER92.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:426:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS93 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:428:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:428:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:428:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:428:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS93 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3740)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3746)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3748)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3754)




                    #action start
                                
                    value = Fraction ( int ( MINUS93.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt40 == 2:
                    # grammar/ShyRecognizerBackend.g:433:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:433:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:433:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3786)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3788)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3794)




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
    FOLLOW_TREE_MODULE_in_module301 = frozenset([2])
    FOLLOW_ID_in_module303 = frozenset([3, 57, 63, 65, 66])
    FOLLOW_module_item_in_module333 = frozenset([3, 57, 63, 65, 66])
    FOLLOW_module_queue_in_module_item404 = frozenset([1])
    FOLLOW_proc_in_module_item429 = frozenset([1])
    FOLLOW_receive_in_module_item453 = frozenset([1])
    FOLLOW_request_in_module_item477 = frozenset([1])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue520 = frozenset([2])
    FOLLOW_ID_in_module_queue522 = frozenset([3])
    FOLLOW_TREE_TRACE_in_trace555 = frozenset([2])
    FOLLOW_ID_in_trace557 = frozenset([3])
    FOLLOW_TREE_TRACE_in_trace585 = frozenset([2])
    FOLLOW_ID_in_trace587 = frozenset([63])
    FOLLOW_procs_in_trace589 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless634 = frozenset([2])
    FOLLOW_ID_in_stateless636 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless664 = frozenset([2])
    FOLLOW_ID_in_stateless666 = frozenset([63])
    FOLLOW_procs_in_stateless668 = frozenset([3])
    FOLLOW_TREE_REQUEST_in_request723 = frozenset([2])
    FOLLOW_ID_in_request737 = frozenset([3, 50, 68])
    FOLLOW_local_vars_in_request771 = frozenset([3, 68])
    FOLLOW_statements_in_request821 = frozenset([3])
    FOLLOW_TREE_RECEIVE_in_receive904 = frozenset([2])
    FOLLOW_ID_in_receive918 = frozenset([3, 50, 68])
    FOLLOW_local_vars_in_receive952 = frozenset([3, 68])
    FOLLOW_statements_in_receive1002 = frozenset([3])
    FOLLOW_proc_in_procs1085 = frozenset([1, 63])
    FOLLOW_TREE_PROC_in_proc1130 = frozenset([2])
    FOLLOW_ID_in_proc1144 = frozenset([3, 50, 64, 68])
    FOLLOW_proc_args_in_proc1178 = frozenset([3, 50, 68])
    FOLLOW_local_vars_in_proc1228 = frozenset([3, 68])
    FOLLOW_statements_in_proc1278 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args1351 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args1353 = frozenset([3])
    FOLLOW_TREE_LOCAL_VARS_in_local_vars1398 = frozenset([2])
    FOLLOW_attrs_hints_in_local_vars1400 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements1455 = frozenset([2])
    FOLLOW_statement_in_statements1459 = frozenset([3, 69, 71, 74, 75, 76])
    FOLLOW_statement_call_in_statement1515 = frozenset([1])
    FOLLOW_statement_if_in_statement1539 = frozenset([1])
    FOLLOW_statement_assign_in_statement1563 = frozenset([1])
    FOLLOW_statement_with_in_statement1587 = frozenset([1])
    FOLLOW_statement_while_in_statement1611 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1654 = frozenset([2])
    FOLLOW_ID_in_statement_with1656 = frozenset([68])
    FOLLOW_statements_in_statement_with1658 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1709 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1725 = frozenset([18, 19, 23, 27, 36, 70])
    FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1773 = frozenset([19])
    FOLLOW_ID_in_statement_assign1789 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1872 = frozenset([2])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1890 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_if1892 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1946 = frozenset([2])
    FOLLOW_statements_in_statement_if1948 = frozenset([3])
    FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2023 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_while2025 = frozenset([3])
    FOLLOW_condition_any_in_conditional_ops2068 = frozenset([68])
    FOLLOW_statements_in_conditional_ops2070 = frozenset([1])
    FOLLOW_condition_all_in_conditional_ops2094 = frozenset([68])
    FOLLOW_statements_in_conditional_ops2096 = frozenset([1])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any2149 = frozenset([2])
    FOLLOW_statement_call_in_condition_any2165 = frozenset([3, 71])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all2240 = frozenset([2])
    FOLLOW_statement_call_in_condition_all2256 = frozenset([3, 71])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call2321 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call2323 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args2378 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_ID_in_arbitrary_value2431 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2443 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2455 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2467 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2479 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts2520 = frozenset([2])
    FOLLOW_ID_in_consts2522 = frozenset([47, 58, 59])
    FOLLOW_consts_items_in_consts2524 = frozenset([3])
    FOLLOW_consts_item_in_consts_items2579 = frozenset([1, 47, 58, 59])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2634 = frozenset([2])
    FOLLOW_ID_in_consts_item2636 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2638 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2666 = frozenset([2])
    FOLLOW_ID_in_consts_item2668 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2670 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2698 = frozenset([2])
    FOLLOW_ID_in_consts_item2700 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2702 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2757 = frozenset([2])
    FOLLOW_ID_in_types2759 = frozenset([79])
    FOLLOW_types_items_in_types2761 = frozenset([3])
    FOLLOW_types_item_in_types_items2816 = frozenset([1, 79])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2871 = frozenset([2])
    FOLLOW_ID_in_types_item2873 = frozenset([40])
    FOLLOW_attrs_hints_in_types_item2875 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2930 = frozenset([2])
    FOLLOW_ID_in_messages2932 = frozenset([52])
    FOLLOW_messages_items_in_messages2934 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2989 = frozenset([1, 52])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3054 = frozenset([2])
    FOLLOW_ID_in_messages_item3056 = frozenset([3, 53, 54, 55])
    FOLLOW_TREE_MESSAGES_ITEM_RECEIVE_in_messages_item3072 = frozenset([40])
    FOLLOW_attrs_hints_in_messages_item3078 = frozenset([3, 54, 55])
    FOLLOW_TREE_MESSAGES_ITEM_REQUEST_in_messages_item3128 = frozenset([40])
    FOLLOW_attrs_hints_in_messages_item3134 = frozenset([3, 54])
    FOLLOW_TREE_MESSAGES_ITEM_REPLY_in_messages_item3184 = frozenset([40])
    FOLLOW_attrs_hints_in_messages_item3190 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars3263 = frozenset([2])
    FOLLOW_ID_in_vars3265 = frozenset([40])
    FOLLOW_attrs_hints_in_vars3267 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3320 = frozenset([1, 41])
    FOLLOW_attr_hint_in_attrs_hints3324 = frozenset([1, 41])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3369 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint3371 = frozenset([39])
    FOLLOW_TREE_ATTR_in_attr_hint3377 = frozenset([2])
    FOLLOW_ID_in_attr_hint3379 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3421 = frozenset([2])
    FOLLOW_hint_in_attr_hint3423 = frozenset([39])
    FOLLOW_TREE_ATTR_in_attr_hint3429 = frozenset([2])
    FOLLOW_ID_in_attr_hint3431 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3500 = frozenset([2])
    FOLLOW_ID_in_hint3502 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3530 = frozenset([2])
    FOLLOW_ID_in_hint3532 = frozenset([19, 82])
    FOLLOW_hint_args_in_hint3534 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args3589 = frozenset([1, 19, 82])
    FOLLOW_ID_in_hint_arg3622 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg3634 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3665 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3667 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole3695 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3740 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3746 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3748 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3754 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract3786 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3788 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3794 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
