# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-02 19:07:01

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
TREE_MODULE=53
TREE_MODULE_QUEUE=54
TREE_NUM_FRACT=55
TREE_NUM_WHOLE=56
TREE_PASTE=57
TREE_PASTE_REPLACE=58
TREE_PASTE_WITH=59
TREE_PROC=60
TREE_PROC_ARGS=61
TREE_RECEIVE=62
TREE_REQUEST=63
TREE_STATELESS=64
TREE_STATEMENTS=65
TREE_STATEMENT_ASSIGN=66
TREE_STATEMENT_ASSIGN_TO=67
TREE_STATEMENT_CALL=68
TREE_STATEMENT_ELIF=69
TREE_STATEMENT_ELSE=70
TREE_STATEMENT_IF=71
TREE_STATEMENT_WHILE=72
TREE_STATEMENT_WITH=73
TREE_TRACE=74
TREE_TYPES=75
TREE_TYPES_ITEM=76
TREE_VARS=77
TYPES=78
UNDERSCORE=79
VARS=80
WHILE=81
WHITESPACE=82
WITH=83

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
    # grammar/ShyRecognizerBackend.g:57:1: module returns [ title , content ] : ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ( requests )? ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        ID8 = None
        module_queue9 = None

        procs10 = None

        receives11 = None

        requests12 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:59:5: ( ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ( requests )? ) )
                # grammar/ShyRecognizerBackend.g:59:9: ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ( requests )? )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module301)

                self.match(self.input, DOWN, None)
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_module303)

                #action start
                retval.title , retval.content = ID8.text , dict ( ) 
                #action end


                # grammar/ShyRecognizerBackend.g:61:13: ( module_queue )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == TREE_MODULE_QUEUE) :
                    alt2 = 1
                if alt2 == 1:
                    # grammar/ShyRecognizerBackend.g:61:15: module_queue
                    pass 
                    self._state.following.append(self.FOLLOW_module_queue_in_module333)
                    module_queue9 = self.module_queue()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'module_queue' ] = module_queue9 
                    #action end





                # grammar/ShyRecognizerBackend.g:64:13: ( procs )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == TREE_PROC) :
                    alt3 = 1
                if alt3 == 1:
                    # grammar/ShyRecognizerBackend.g:64:15: procs
                    pass 
                    self._state.following.append(self.FOLLOW_procs_in_module384)
                    procs10 = self.procs()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'proc' ] = procs10 
                    #action end





                # grammar/ShyRecognizerBackend.g:67:13: ( receives )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_RECEIVE) :
                    alt4 = 1
                if alt4 == 1:
                    # grammar/ShyRecognizerBackend.g:67:15: receives
                    pass 
                    self._state.following.append(self.FOLLOW_receives_in_module434)
                    receives11 = self.receives()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'receive' ] = receives11 
                    #action end





                # grammar/ShyRecognizerBackend.g:70:13: ( requests )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_REQUEST) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:70:15: requests
                    pass 
                    self._state.following.append(self.FOLLOW_requests_in_module484)
                    requests12 = self.requests()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'request' ] = requests12 
                    #action end





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "module"



    # $ANTLR start "module_queue"
    # grammar/ShyRecognizerBackend.g:76:1: module_queue returns [ value ] : ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        value = None


        ID13 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:78:5: ( ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerBackend.g:78:9: ^( TREE_MODULE_QUEUE ID )
                pass 
                self.match(self.input, TREE_MODULE_QUEUE, self.FOLLOW_TREE_MODULE_QUEUE_in_module_queue557)

                self.match(self.input, DOWN, None)
                ID13 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue559)

                self.match(self.input, UP, None)


                #action start
                value = ID13.text 
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
    # grammar/ShyRecognizerBackend.g:81:1: trace returns [ title , content ] : ( ^( TREE_TRACE ID ) | ^( TREE_TRACE ID procs ) );
    def trace(self, ):
        retval = self.trace_return()
        retval.start = self.input.LT(1)


        ID14 = None
        ID15 = None
        procs16 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:83:5: ( ^( TREE_TRACE ID ) | ^( TREE_TRACE ID procs ) )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_TRACE) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == 2) :
                        LA6_2 = self.input.LA(3)

                        if (LA6_2 == ID) :
                            LA6_3 = self.input.LA(4)

                            if (LA6_3 == 3) :
                                alt6 = 1
                            elif (LA6_3 == TREE_PROC) :
                                alt6 = 2
                            else:
                                nvae = NoViableAltException("", 6, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 6, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:83:9: ^( TREE_TRACE ID )
                    pass 
                    self.match(self.input, TREE_TRACE, self.FOLLOW_TREE_TRACE_in_trace592)

                    self.match(self.input, DOWN, None)
                    ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_trace594)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID14.text , dict ( ) 
                    #action end



                elif alt6 == 2:
                    # grammar/ShyRecognizerBackend.g:85:9: ^( TREE_TRACE ID procs )
                    pass 
                    self.match(self.input, TREE_TRACE, self.FOLLOW_TREE_TRACE_in_trace622)

                    self.match(self.input, DOWN, None)
                    ID15 = self.match(self.input, ID, self.FOLLOW_ID_in_trace624)

                    self._state.following.append(self.FOLLOW_procs_in_trace626)
                    procs16 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID15.text , procs16 
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
    # grammar/ShyRecognizerBackend.g:89:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID17 = None
        ID18 = None
        procs19 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:91:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == TREE_STATELESS) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == 2) :
                        LA7_2 = self.input.LA(3)

                        if (LA7_2 == ID) :
                            LA7_3 = self.input.LA(4)

                            if (LA7_3 == 3) :
                                alt7 = 1
                            elif (LA7_3 == TREE_PROC) :
                                alt7 = 2
                            else:
                                nvae = NoViableAltException("", 7, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 7, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:91:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless671)

                    self.match(self.input, DOWN, None)
                    ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless673)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID17.text , dict ( ) 
                    #action end



                elif alt7 == 2:
                    # grammar/ShyRecognizerBackend.g:93:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless701)

                    self.match(self.input, DOWN, None)
                    ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless703)

                    self._state.following.append(self.FOLLOW_procs_in_stateless705)
                    procs19 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID18.text , procs19 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "requests"
    # grammar/ShyRecognizerBackend.g:97:1: requests returns [ value ] : ( request )+ ;
    def requests(self, ):
        value = None


        request20 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:100:5: ( ( request )+ )
                # grammar/ShyRecognizerBackend.g:100:9: ( request )+
                pass 
                # grammar/ShyRecognizerBackend.g:100:9: ( request )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == TREE_REQUEST) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerBackend.g:100:11: request
                        pass 
                        self._state.following.append(self.FOLLOW_request_in_requests760)
                        request20 = self.request()

                        self._state.following.pop()

                        #action start
                        value [ ((request20 is not None) and [request20.title] or [None])[0] ] = ((request20 is not None) and [request20.content] or [None])[0] 
                        #action end



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "requests"


    class request_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.request_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "request"
    # grammar/ShyRecognizerBackend.g:103:1: request returns [ title , content ] : ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) ;
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        ID21 = None
        local_vars22 = None

        statements23 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:106:5: ( ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:106:9: ^( TREE_REQUEST ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_REQUEST, self.FOLLOW_TREE_REQUEST_in_request805)

                self.match(self.input, DOWN, None)
                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_request819)

                #action start
                retval.title = ID21.text 
                #action end


                # grammar/ShyRecognizerBackend.g:109:13: ( local_vars )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == TREE_LOCAL_VARS) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:109:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_request853)
                    local_vars22 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars22 
                    #action end





                # grammar/ShyRecognizerBackend.g:112:13: ( statements )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == TREE_STATEMENTS) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerBackend.g:112:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_request903)
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



    # $ANTLR start "receives"
    # grammar/ShyRecognizerBackend.g:118:1: receives returns [ value ] : ( receive )+ ;
    def receives(self, ):
        value = None


        receive24 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:121:5: ( ( receive )+ )
                # grammar/ShyRecognizerBackend.g:121:9: ( receive )+
                pass 
                # grammar/ShyRecognizerBackend.g:121:9: ( receive )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == TREE_RECEIVE) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:121:11: receive
                        pass 
                        self._state.following.append(self.FOLLOW_receive_in_receives986)
                        receive24 = self.receive()

                        self._state.following.pop()

                        #action start
                        value [ ((receive24 is not None) and [receive24.title] or [None])[0] ] = ((receive24 is not None) and [receive24.content] or [None])[0] 
                        #action end



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "receives"


    class receive_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.receive_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "receive"
    # grammar/ShyRecognizerBackend.g:124:1: receive returns [ title , content ] : ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) ;
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        ID25 = None
        local_vars26 = None

        statements27 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:127:5: ( ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:127:9: ^( TREE_RECEIVE ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_RECEIVE, self.FOLLOW_TREE_RECEIVE_in_receive1031)

                self.match(self.input, DOWN, None)
                ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_receive1045)

                #action start
                retval.title = ID25.text 
                #action end


                # grammar/ShyRecognizerBackend.g:130:13: ( local_vars )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == TREE_LOCAL_VARS) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:130:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_receive1079)
                    local_vars26 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars26 
                    #action end





                # grammar/ShyRecognizerBackend.g:133:13: ( statements )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == TREE_STATEMENTS) :
                    alt13 = 1
                if alt13 == 1:
                    # grammar/ShyRecognizerBackend.g:133:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_receive1129)
                    statements27 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements27 
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
    # grammar/ShyRecognizerBackend.g:139:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc28 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:142:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:142:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:142:9: ( proc )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TREE_PROC) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:142:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs1212)
                        proc28 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc28 is not None) and [proc28.title] or [None])[0] ] = ((proc28 is not None) and [proc28.content] or [None])[0] 
                        #action end



                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1





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
    # grammar/ShyRecognizerBackend.g:145:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID29 = None
        proc_args30 = None

        local_vars31 = None

        statements32 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:148:5: ( ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:148:9: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc1257)

                self.match(self.input, DOWN, None)
                ID29 = self.match(self.input, ID, self.FOLLOW_ID_in_proc1271)

                #action start
                retval.title = ID29.text 
                #action end


                # grammar/ShyRecognizerBackend.g:151:13: ( proc_args )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == TREE_PROC_ARGS) :
                    alt15 = 1
                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:151:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc1305)
                    proc_args30 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args30 
                    #action end





                # grammar/ShyRecognizerBackend.g:154:13: ( local_vars )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == TREE_LOCAL_VARS) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/ShyRecognizerBackend.g:154:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_proc1355)
                    local_vars31 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars31 
                    #action end





                # grammar/ShyRecognizerBackend.g:157:13: ( statements )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == TREE_STATEMENTS) :
                    alt17 = 1
                if alt17 == 1:
                    # grammar/ShyRecognizerBackend.g:157:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc1405)
                    statements32 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements32 
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
    # grammar/ShyRecognizerBackend.g:163:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints33 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:165:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:165:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args1478)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args1480)
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

    # $ANTLR end "proc_args"



    # $ANTLR start "local_vars"
    # grammar/ShyRecognizerBackend.g:169:1: local_vars returns [ value ] : ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        value = None


        attrs_hints34 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:171:5: ( ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:171:9: ^( TREE_LOCAL_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_LOCAL_VARS, self.FOLLOW_TREE_LOCAL_VARS_in_local_vars1525)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars1527)
                attrs_hints34 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints34 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "local_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:175:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement35 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:178:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:178:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements1582)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:178:28: ( statement )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == TREE_STATEMENT_ASSIGN or LA18_0 == TREE_STATEMENT_CALL or (TREE_STATEMENT_IF <= LA18_0 <= TREE_STATEMENT_WITH)) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerBackend.g:178:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1586)
                        statement35 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement35 ) 
                        #action end



                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statements"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:183:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with | statement_while );
    def statement(self, ):
        value = None


        statement_call36 = None

        statement_if37 = None

        statement_assign38 = None

        statement_with39 = None

        statement_while40 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:185:5: ( statement_call | statement_if | statement_assign | statement_with | statement_while )
                alt19 = 5
                LA19 = self.input.LA(1)
                if LA19 == TREE_STATEMENT_CALL:
                    alt19 = 1
                elif LA19 == TREE_STATEMENT_IF:
                    alt19 = 2
                elif LA19 == TREE_STATEMENT_ASSIGN:
                    alt19 = 3
                elif LA19 == TREE_STATEMENT_WITH:
                    alt19 = 4
                elif LA19 == TREE_STATEMENT_WHILE:
                    alt19 = 5
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:185:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement1642)
                    statement_call36 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call36 
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:187:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement1666)
                    statement_if37 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if37 
                    #action end



                elif alt19 == 3:
                    # grammar/ShyRecognizerBackend.g:189:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1690)
                    statement_assign38 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign38 
                    #action end



                elif alt19 == 4:
                    # grammar/ShyRecognizerBackend.g:191:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1714)
                    statement_with39 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with39 
                    #action end



                elif alt19 == 5:
                    # grammar/ShyRecognizerBackend.g:193:9: statement_while
                    pass 
                    self._state.following.append(self.FOLLOW_statement_while_in_statement1738)
                    statement_while40 = self.statement_while()

                    self._state.following.pop()

                    #action start
                    value = statement_while40 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:197:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID41 = None
        statements42 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:199:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:199:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1781)

                self.match(self.input, DOWN, None)
                ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1783)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1785)
                statements42 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID41.text : statements42 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:203:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID44 = None
        arbitrary_value43 = None


        value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:206:5: ( ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:206:9: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1836)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:207:13: ( arbitrary_value )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER or LA20_0 == STRING) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:207:15: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1852)
                        arbitrary_value43 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                                        
                        value [ 'assign' ] [ 'from' ] . append (
                            arbitrary_value43 )
                                        
                        #action end



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1


                self.match(self.input, TREE_STATEMENT_ASSIGN_TO, self.FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1900)

                # grammar/ShyRecognizerBackend.g:214:13: ( ID )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == ID) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:214:15: ID
                        pass 
                        ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1916)

                        #action start
                                        
                        value [ 'assign' ] [ 'to' ] . append (
                            ID44.text )
                                        
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

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:223:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) ;
    def statement_if(self, ):
        value = None


        conditional_ops45 = None

        statements46 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:226:5: ( ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) )
                # grammar/ShyRecognizerBackend.g:226:9: ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1999)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:227:13: ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == TREE_STATEMENT_ELIF) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:227:15: ^( TREE_STATEMENT_ELIF conditional_ops )
                        pass 
                        self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_if2017)

                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_conditional_ops_in_statement_if2019)
                        conditional_ops45 = self.conditional_ops()

                        self._state.following.pop()

                        self.match(self.input, UP, None)


                        #action start
                        value [ 'if' ] . append ( conditional_ops45 ) 
                        #action end



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1


                # grammar/ShyRecognizerBackend.g:230:13: ( ^( TREE_STATEMENT_ELSE statements ) )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == TREE_STATEMENT_ELSE) :
                    alt23 = 1
                if alt23 == 1:
                    # grammar/ShyRecognizerBackend.g:230:15: ^( TREE_STATEMENT_ELSE statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_if2073)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statements_in_statement_if2075)
                    statements46 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ 'else' ] = statements46 
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
    # grammar/ShyRecognizerBackend.g:236:1: statement_while returns [ value ] : ^( TREE_STATEMENT_WHILE conditional_ops ) ;
    def statement_while(self, ):
        value = None


        conditional_ops47 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:238:5: ( ^( TREE_STATEMENT_WHILE conditional_ops ) )
                # grammar/ShyRecognizerBackend.g:238:9: ^( TREE_STATEMENT_WHILE conditional_ops )
                pass 
                self.match(self.input, TREE_STATEMENT_WHILE, self.FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2150)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_conditional_ops_in_statement_while2152)
                conditional_ops47 = self.conditional_ops()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'while' : conditional_ops47 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_while"



    # $ANTLR start "conditional_ops"
    # grammar/ShyRecognizerBackend.g:242:1: conditional_ops returns [ value ] : ( condition_any statements | condition_all statements );
    def conditional_ops(self, ):
        value = None


        condition_any48 = None

        statements49 = None

        condition_all50 = None

        statements51 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:244:5: ( condition_any statements | condition_all statements )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == TREE_CONDITION_ANY) :
                    alt24 = 1
                elif (LA24_0 == TREE_CONDITION_ALL) :
                    alt24 = 2
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerBackend.g:244:9: condition_any statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_any_in_conditional_ops2195)
                    condition_any48 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2197)
                    statements49 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'any' : condition_any48 ,
                       'ops' : statements49 }
                                
                    #action end



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:249:9: condition_all statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_all_in_conditional_ops2221)
                    condition_all50 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2223)
                    statements51 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'all' : condition_all50 ,
                       'ops' : statements51 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "conditional_ops"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:256:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call52 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:259:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:259:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any2276)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:260:13: ( statement_call )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == TREE_STATEMENT_CALL) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerBackend.g:260:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any2292)
                        statement_call52 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call52 ) 
                        #action end



                    else:
                        if cnt25 >= 1:
                            break #loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:265:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call53 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:268:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:268:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all2367)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:269:13: ( statement_call )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == TREE_STATEMENT_CALL) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerBackend.g:269:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all2383)
                        statement_call53 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call53 ) 
                        #action end



                    else:
                        if cnt26 >= 1:
                            break #loop26

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:274:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args54 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:276:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:276:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call2448)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call2450)
                    statement_call_args54 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args54 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:280:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value55 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:283:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:283:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:283:9: ( arbitrary_value )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA27_0 <= ID) or LA27_0 == MINUS or LA27_0 == NUMBER or LA27_0 == STRING) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerBackend.g:283:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2505)
                        arbitrary_value55 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value55 ) 
                        #action end



                    else:
                        break #loop27





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:288:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID56 = None
        EXPRESSION57 = None
        STRING58 = None
        num_whole59 = None

        num_fract60 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:290:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
                alt28 = 5
                LA28 = self.input.LA(1)
                if LA28 == ID:
                    alt28 = 1
                elif LA28 == EXPRESSION:
                    alt28 = 2
                elif LA28 == STRING:
                    alt28 = 3
                elif LA28 == MINUS:
                    LA28_4 = self.input.LA(2)

                    if (LA28_4 == NUMBER) :
                        LA28_6 = self.input.LA(3)

                        if (LA28_6 == DIVIDE) :
                            alt28 = 5
                        elif (LA28_6 == 3 or (EXPRESSION <= LA28_6 <= ID) or LA28_6 == MINUS or LA28_6 == NUMBER or LA28_6 == STRING or LA28_6 == TREE_STATEMENT_ASSIGN_TO) :
                            alt28 = 4
                        else:
                            nvae = NoViableAltException("", 28, 6, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 28, 4, self.input)

                        raise nvae


                elif LA28 == NUMBER:
                    LA28_5 = self.input.LA(2)

                    if (LA28_5 == DIVIDE) :
                        alt28 = 5
                    elif (LA28_5 == 3 or (EXPRESSION <= LA28_5 <= ID) or LA28_5 == MINUS or LA28_5 == NUMBER or LA28_5 == STRING or LA28_5 == TREE_STATEMENT_ASSIGN_TO) :
                        alt28 = 4
                    else:
                        nvae = NoViableAltException("", 28, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # grammar/ShyRecognizerBackend.g:290:9: ID
                    pass 
                    ID56 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2558)

                    #action start
                    value = ID56.text 
                    #action end



                elif alt28 == 2:
                    # grammar/ShyRecognizerBackend.g:291:9: EXPRESSION
                    pass 
                    EXPRESSION57 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2570)

                    #action start
                    value = EXPRESSION57.text 
                    #action end



                elif alt28 == 3:
                    # grammar/ShyRecognizerBackend.g:292:9: STRING
                    pass 
                    STRING58 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2582)

                    #action start
                    value = STRING58.text 
                    #action end



                elif alt28 == 4:
                    # grammar/ShyRecognizerBackend.g:293:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2594)
                    num_whole59 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole59 
                    #action end



                elif alt28 == 5:
                    # grammar/ShyRecognizerBackend.g:294:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2606)
                    num_fract60 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract60 
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
    # grammar/ShyRecognizerBackend.g:297:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID61 = None
        consts_items62 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:300:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:300:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts2647)

                self.match(self.input, DOWN, None)
                ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2649)

                self._state.following.append(self.FOLLOW_consts_items_in_consts2651)
                consts_items62 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID61.text , consts_items62 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:304:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item63 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:307:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:307:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:307:9: ( consts_item )+
                cnt29 = 0
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA29_0 <= TREE_NUM_WHOLE)) :
                        alt29 = 1


                    if alt29 == 1:
                        # grammar/ShyRecognizerBackend.g:307:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2706)
                        consts_item63 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item63 is not None) and [consts_item63.name] or [None])[0] ] = ((consts_item63 is not None) and [consts_item63.value] or [None])[0] 
                        #action end



                    else:
                        if cnt29 >= 1:
                            break #loop29

                        eee = EarlyExitException(29, self.input)
                        raise eee

                    cnt29 += 1





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
    # grammar/ShyRecognizerBackend.g:312:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID64 = None
        ID66 = None
        ID68 = None
        EXPRESSION69 = None
        num_whole65 = None

        num_fract67 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:314:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt30 = 3
                LA30 = self.input.LA(1)
                if LA30 == TREE_NUM_WHOLE:
                    alt30 = 1
                elif LA30 == TREE_NUM_FRACT:
                    alt30 = 2
                elif LA30 == TREE_EXPRESSION:
                    alt30 = 3
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae


                if alt30 == 1:
                    # grammar/ShyRecognizerBackend.g:314:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2761)

                    self.match(self.input, DOWN, None)
                    ID64 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2763)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2765)
                    num_whole65 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID64.text , num_whole65 
                    #action end



                elif alt30 == 2:
                    # grammar/ShyRecognizerBackend.g:316:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2793)

                    self.match(self.input, DOWN, None)
                    ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2795)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2797)
                    num_fract67 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID66.text , num_fract67 
                    #action end



                elif alt30 == 3:
                    # grammar/ShyRecognizerBackend.g:318:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2825)

                    self.match(self.input, DOWN, None)
                    ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2827)

                    EXPRESSION69 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2829)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID68.text , EXPRESSION69.text 
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
    # grammar/ShyRecognizerBackend.g:322:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID70 = None
        types_items71 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:325:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:325:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2884)

                self.match(self.input, DOWN, None)
                ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_types2886)

                self._state.following.append(self.FOLLOW_types_items_in_types2888)
                types_items71 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID70.text , types_items71 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:329:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item72 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:332:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:332:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:332:9: ( types_item )+
                cnt31 = 0
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == TREE_TYPES_ITEM) :
                        alt31 = 1


                    if alt31 == 1:
                        # grammar/ShyRecognizerBackend.g:332:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2943)
                        types_item72 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item72 is not None) and [types_item72.name] or [None])[0] ] = ((types_item72 is not None) and [types_item72.value] or [None])[0] 
                        #action end



                    else:
                        if cnt31 >= 1:
                            break #loop31

                        eee = EarlyExitException(31, self.input)
                        raise eee

                    cnt31 += 1





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
    # grammar/ShyRecognizerBackend.g:337:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID73 = None
        attrs_hints74 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:339:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:339:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2998)

                self.match(self.input, DOWN, None)
                ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item3000)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item3002)
                attrs_hints74 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID73.text , attrs_hints74 
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
    # grammar/ShyRecognizerBackend.g:343:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID75 = None
        messages_items76 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:346:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:346:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages3057)

                self.match(self.input, DOWN, None)
                ID75 = self.match(self.input, ID, self.FOLLOW_ID_in_messages3059)

                self._state.following.append(self.FOLLOW_messages_items_in_messages3061)
                messages_items76 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID75.text , messages_items76 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:350:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item77 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:353:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:353:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:353:9: ( messages_item )+
                cnt32 = 0
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == TREE_MESSAGES_ITEM) :
                        alt32 = 1


                    if alt32 == 1:
                        # grammar/ShyRecognizerBackend.g:353:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items3116)
                        messages_item77 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item77 is not None) and [messages_item77.name] or [None])[0] ] = ((messages_item77 is not None) and [messages_item77.value] or [None])[0] 
                        #action end



                    else:
                        if cnt32 >= 1:
                            break #loop32

                        eee = EarlyExitException(32, self.input)
                        raise eee

                    cnt32 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "messages_items"


    class messages_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.messages_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerBackend.g:358:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID78 = None
        attrs_hints79 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:360:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:360:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3171)

                self.match(self.input, DOWN, None)
                ID78 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3173)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3175)
                attrs_hints79 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID78.text , attrs_hints79 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages_item"


    class vars_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.vars_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "vars"
    # grammar/ShyRecognizerBackend.g:364:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID80 = None
        attrs_hints81 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:366:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:366:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars3220)

                self.match(self.input, DOWN, None)
                ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3222)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3224)
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
    # grammar/ShyRecognizerBackend.g:370:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint82 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:373:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:373:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3277)

                # grammar/ShyRecognizerBackend.g:373:26: ( attr_hint )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == TREE_ATTR_HINT) :
                        alt33 = 1


                    if alt33 == 1:
                        # grammar/ShyRecognizerBackend.g:373:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3281)
                        attr_hint82 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint82 ) 
                        #action end



                    else:
                        break #loop33





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:376:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID83 = None
        ID84 = None
        hint85 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:379:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == TREE_ATTR_HINT) :
                    LA36_1 = self.input.LA(2)

                    if (LA36_1 == 2) :
                        LA36_2 = self.input.LA(3)

                        if (LA36_2 == TREE_HINT_NONE) :
                            alt36 = 1
                        elif (LA36_2 == TREE_HINT) :
                            alt36 = 2
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
                    # grammar/ShyRecognizerBackend.g:379:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3326)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint3328)

                    # grammar/ShyRecognizerBackend.g:379:42: ( ^( TREE_ATTR ID ) )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == TREE_ATTR) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerBackend.g:379:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3334)

                            self.match(self.input, DOWN, None)
                            ID83 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3336)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID83.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


                    self.match(self.input, UP, None)



                elif alt36 == 2:
                    # grammar/ShyRecognizerBackend.g:382:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3378)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3380)
                    hint85 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:382:32: ( ^( TREE_ATTR ID ) )+
                    cnt35 = 0
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == TREE_ATTR) :
                            alt35 = 1


                        if alt35 == 1:
                            # grammar/ShyRecognizerBackend.g:382:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3386)

                            self.match(self.input, DOWN, None)
                            ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3388)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID84.text ] = hint85 
                            #action end



                        else:
                            if cnt35 >= 1:
                                break #loop35

                            eee = EarlyExitException(35, self.input)
                            raise eee

                        cnt35 += 1


                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:387:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID86 = None
        ID87 = None
        hint_args88 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:390:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == TREE_HINT) :
                    LA37_1 = self.input.LA(2)

                    if (LA37_1 == 2) :
                        LA37_2 = self.input.LA(3)

                        if (LA37_2 == ID) :
                            LA37_3 = self.input.LA(4)

                            if (LA37_3 == 3) :
                                alt37 = 1
                            elif (LA37_3 == ID or LA37_3 == UNDERSCORE) :
                                alt37 = 2
                            else:
                                nvae = NoViableAltException("", 37, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 37, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 37, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # grammar/ShyRecognizerBackend.g:390:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3457)

                    self.match(self.input, DOWN, None)
                    ID86 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3459)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID86.text ] = list ( ) 
                    #action end



                elif alt37 == 2:
                    # grammar/ShyRecognizerBackend.g:392:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3487)

                    self.match(self.input, DOWN, None)
                    ID87 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3489)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint3491)
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
    # grammar/ShyRecognizerBackend.g:396:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg89 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:399:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:399:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:399:9: ( hint_arg )+
                cnt38 = 0
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == ID or LA38_0 == UNDERSCORE) :
                        alt38 = 1


                    if alt38 == 1:
                        # grammar/ShyRecognizerBackend.g:399:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args3546)
                        hint_arg89 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg89 ) 
                        #action end



                    else:
                        if cnt38 >= 1:
                            break #loop38

                        eee = EarlyExitException(38, self.input)
                        raise eee

                    cnt38 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:402:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID90 = None
        UNDERSCORE91 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:404:5: ( ID | UNDERSCORE )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == ID) :
                    alt39 = 1
                elif (LA39_0 == UNDERSCORE) :
                    alt39 = 2
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae


                if alt39 == 1:
                    # grammar/ShyRecognizerBackend.g:404:9: ID
                    pass 
                    ID90 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg3579)

                    #action start
                    value = ID90.text 
                    #action end



                elif alt39 == 2:
                    # grammar/ShyRecognizerBackend.g:405:9: UNDERSCORE
                    pass 
                    UNDERSCORE91 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg3591)

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
    # grammar/ShyRecognizerBackend.g:408:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS92 = None
        NUMBER93 = None
        NUMBER94 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:410:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:410:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:410:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:410:11: MINUS NUMBER
                    pass 
                    MINUS92 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3622)

                    NUMBER93 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3624)




                    #action start
                    value = int ( MINUS92.text + NUMBER93.text ) 
                    #action end



                elif alt40 == 2:
                    # grammar/ShyRecognizerBackend.g:412:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:412:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:412:11: NUMBER
                    pass 
                    NUMBER94 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3652)




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
    # grammar/ShyRecognizerBackend.g:416:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS95 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:418:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == MINUS) :
                    alt41 = 1
                elif (LA41_0 == NUMBER) :
                    alt41 = 2
                else:
                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae


                if alt41 == 1:
                    # grammar/ShyRecognizerBackend.g:418:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:418:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:418:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS95 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3697)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3703)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3705)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3711)




                    #action start
                                
                    value = Fraction ( int ( MINUS95.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt41 == 2:
                    # grammar/ShyRecognizerBackend.g:423:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:423:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:423:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3743)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3745)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3751)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 44, 51, 53, 64, 74, 75, 77])
    FOLLOW_stateless_in_start114 = frozenset([1, 44, 51, 53, 64, 74, 75, 77])
    FOLLOW_trace_in_start141 = frozenset([1, 44, 51, 53, 64, 74, 75, 77])
    FOLLOW_consts_in_start168 = frozenset([1, 44, 51, 53, 64, 74, 75, 77])
    FOLLOW_types_in_start194 = frozenset([1, 44, 51, 53, 64, 74, 75, 77])
    FOLLOW_messages_in_start220 = frozenset([1, 44, 51, 53, 64, 74, 75, 77])
    FOLLOW_vars_in_start246 = frozenset([1, 44, 51, 53, 64, 74, 75, 77])
    FOLLOW_TREE_MODULE_in_module301 = frozenset([2])
    FOLLOW_ID_in_module303 = frozenset([3, 54, 60, 62, 63])
    FOLLOW_module_queue_in_module333 = frozenset([3, 60, 62, 63])
    FOLLOW_procs_in_module384 = frozenset([3, 62, 63])
    FOLLOW_receives_in_module434 = frozenset([3, 63])
    FOLLOW_requests_in_module484 = frozenset([3])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue557 = frozenset([2])
    FOLLOW_ID_in_module_queue559 = frozenset([3])
    FOLLOW_TREE_TRACE_in_trace592 = frozenset([2])
    FOLLOW_ID_in_trace594 = frozenset([3])
    FOLLOW_TREE_TRACE_in_trace622 = frozenset([2])
    FOLLOW_ID_in_trace624 = frozenset([60])
    FOLLOW_procs_in_trace626 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless671 = frozenset([2])
    FOLLOW_ID_in_stateless673 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless701 = frozenset([2])
    FOLLOW_ID_in_stateless703 = frozenset([60])
    FOLLOW_procs_in_stateless705 = frozenset([3])
    FOLLOW_request_in_requests760 = frozenset([1, 63])
    FOLLOW_TREE_REQUEST_in_request805 = frozenset([2])
    FOLLOW_ID_in_request819 = frozenset([3, 50, 65])
    FOLLOW_local_vars_in_request853 = frozenset([3, 65])
    FOLLOW_statements_in_request903 = frozenset([3])
    FOLLOW_receive_in_receives986 = frozenset([1, 62])
    FOLLOW_TREE_RECEIVE_in_receive1031 = frozenset([2])
    FOLLOW_ID_in_receive1045 = frozenset([3, 50, 65])
    FOLLOW_local_vars_in_receive1079 = frozenset([3, 65])
    FOLLOW_statements_in_receive1129 = frozenset([3])
    FOLLOW_proc_in_procs1212 = frozenset([1, 60])
    FOLLOW_TREE_PROC_in_proc1257 = frozenset([2])
    FOLLOW_ID_in_proc1271 = frozenset([3, 50, 61, 65])
    FOLLOW_proc_args_in_proc1305 = frozenset([3, 50, 65])
    FOLLOW_local_vars_in_proc1355 = frozenset([3, 65])
    FOLLOW_statements_in_proc1405 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args1478 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args1480 = frozenset([3])
    FOLLOW_TREE_LOCAL_VARS_in_local_vars1525 = frozenset([2])
    FOLLOW_attrs_hints_in_local_vars1527 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements1582 = frozenset([2])
    FOLLOW_statement_in_statements1586 = frozenset([3, 66, 68, 71, 72, 73])
    FOLLOW_statement_call_in_statement1642 = frozenset([1])
    FOLLOW_statement_if_in_statement1666 = frozenset([1])
    FOLLOW_statement_assign_in_statement1690 = frozenset([1])
    FOLLOW_statement_with_in_statement1714 = frozenset([1])
    FOLLOW_statement_while_in_statement1738 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1781 = frozenset([2])
    FOLLOW_ID_in_statement_with1783 = frozenset([65])
    FOLLOW_statements_in_statement_with1785 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1836 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1852 = frozenset([18, 19, 23, 27, 36, 67])
    FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1900 = frozenset([19])
    FOLLOW_ID_in_statement_assign1916 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1999 = frozenset([2])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_if2017 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_if2019 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_if2073 = frozenset([2])
    FOLLOW_statements_in_statement_if2075 = frozenset([3])
    FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2150 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_while2152 = frozenset([3])
    FOLLOW_condition_any_in_conditional_ops2195 = frozenset([65])
    FOLLOW_statements_in_conditional_ops2197 = frozenset([1])
    FOLLOW_condition_all_in_conditional_ops2221 = frozenset([65])
    FOLLOW_statements_in_conditional_ops2223 = frozenset([1])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any2276 = frozenset([2])
    FOLLOW_statement_call_in_condition_any2292 = frozenset([3, 68])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all2367 = frozenset([2])
    FOLLOW_statement_call_in_condition_all2383 = frozenset([3, 68])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call2448 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call2450 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args2505 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_ID_in_arbitrary_value2558 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2570 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2582 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2594 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2606 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts2647 = frozenset([2])
    FOLLOW_ID_in_consts2649 = frozenset([47, 55, 56])
    FOLLOW_consts_items_in_consts2651 = frozenset([3])
    FOLLOW_consts_item_in_consts_items2706 = frozenset([1, 47, 55, 56])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2761 = frozenset([2])
    FOLLOW_ID_in_consts_item2763 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2765 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2793 = frozenset([2])
    FOLLOW_ID_in_consts_item2795 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2797 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2825 = frozenset([2])
    FOLLOW_ID_in_consts_item2827 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2829 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2884 = frozenset([2])
    FOLLOW_ID_in_types2886 = frozenset([76])
    FOLLOW_types_items_in_types2888 = frozenset([3])
    FOLLOW_types_item_in_types_items2943 = frozenset([1, 76])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2998 = frozenset([2])
    FOLLOW_ID_in_types_item3000 = frozenset([40])
    FOLLOW_attrs_hints_in_types_item3002 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages3057 = frozenset([2])
    FOLLOW_ID_in_messages3059 = frozenset([52])
    FOLLOW_messages_items_in_messages3061 = frozenset([3])
    FOLLOW_messages_item_in_messages_items3116 = frozenset([1, 52])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3171 = frozenset([2])
    FOLLOW_ID_in_messages_item3173 = frozenset([40])
    FOLLOW_attrs_hints_in_messages_item3175 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars3220 = frozenset([2])
    FOLLOW_ID_in_vars3222 = frozenset([40])
    FOLLOW_attrs_hints_in_vars3224 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3277 = frozenset([1, 41])
    FOLLOW_attr_hint_in_attrs_hints3281 = frozenset([1, 41])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3326 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint3328 = frozenset([39])
    FOLLOW_TREE_ATTR_in_attr_hint3334 = frozenset([2])
    FOLLOW_ID_in_attr_hint3336 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3378 = frozenset([2])
    FOLLOW_hint_in_attr_hint3380 = frozenset([39])
    FOLLOW_TREE_ATTR_in_attr_hint3386 = frozenset([2])
    FOLLOW_ID_in_attr_hint3388 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3457 = frozenset([2])
    FOLLOW_ID_in_hint3459 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3487 = frozenset([2])
    FOLLOW_ID_in_hint3489 = frozenset([19, 79])
    FOLLOW_hint_args_in_hint3491 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args3546 = frozenset([1, 19, 79])
    FOLLOW_ID_in_hint_arg3579 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg3591 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3622 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3624 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole3652 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3697 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3703 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3705 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3711 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract3743 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3745 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3751 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
