# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-02 18:53:52

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
TREE_ARBITRARY_TOKEN=37
TREE_ATTR=38
TREE_ATTRS_HINTS=39
TREE_ATTR_HINT=40
TREE_CONDITION_ALL=41
TREE_CONDITION_ANY=42
TREE_CONSTS=43
TREE_COPY=44
TREE_COPY_PASTE=45
TREE_EXPRESSION=46
TREE_HINT=47
TREE_HINT_NONE=48
TREE_LOCAL_VARS=49
TREE_MESSAGES=50
TREE_MESSAGES_ITEM=51
TREE_MODULE=52
TREE_MODULE_QUEUE=53
TREE_NUM_FRACT=54
TREE_NUM_WHOLE=55
TREE_PASTE=56
TREE_PASTE_REPLACE=57
TREE_PASTE_WITH=58
TREE_PROC=59
TREE_PROC_ARGS=60
TREE_RECEIVE=61
TREE_REQUEST=62
TREE_STATELESS=63
TREE_STATEMENTS=64
TREE_STATEMENT_ASSIGN=65
TREE_STATEMENT_ASSIGN_TO=66
TREE_STATEMENT_CALL=67
TREE_STATEMENT_ELIF=68
TREE_STATEMENT_ELSE=69
TREE_STATEMENT_IF=70
TREE_STATEMENT_WHILE=71
TREE_STATEMENT_WITH=72
TREE_TYPES=73
TREE_TYPES_ITEM=74
TREE_VARS=75
TYPES=76
UNDERSCORE=77
VARS=78
WHILE=79
WHITESPACE=80
WITH=81

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "RECEIVE", "REPLACE", "REPLY", 
    "REQUEST", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", 
    "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_LOCAL_VARS", "TREE_MESSAGES", "TREE_MESSAGES_ITEM", 
    "TREE_MODULE", "TREE_MODULE_QUEUE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_RECEIVE", "TREE_REQUEST", "TREE_STATELESS", 
    "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", 
    "TREE_STATEMENT_IF", "TREE_STATEMENT_WHILE", "TREE_STATEMENT_WITH", 
    "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", "UNDERSCORE", 
    "VARS", "WHILE", "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:16:1: start returns [ value ] : ( module | stateless | consts | types | messages | vars )* ;
    def start(self, ):
        value = None


        module1 = None

        stateless2 = None

        consts3 = None

        types4 = None

        messages5 = None

        vars6 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:19:5: ( ( module | stateless | consts | types | messages | vars )* )
                # grammar/ShyRecognizerBackend.g:19:9: ( module | stateless | consts | types | messages | vars )*
                pass 
                # grammar/ShyRecognizerBackend.g:19:9: ( module | stateless | consts | types | messages | vars )*
                while True: #loop1
                    alt1 = 7
                    LA1 = self.input.LA(1)
                    if LA1 == TREE_MODULE:
                        alt1 = 1
                    elif LA1 == TREE_STATELESS:
                        alt1 = 2
                    elif LA1 == TREE_CONSTS:
                        alt1 = 3
                    elif LA1 == TREE_TYPES:
                        alt1 = 4
                    elif LA1 == TREE_MESSAGES:
                        alt1 = 5
                    elif LA1 == TREE_VARS:
                        alt1 = 6

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
                        # grammar/ShyRecognizerBackend.g:29:11: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start141)
                        consts3 = self.consts()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'consts' :
                            { ((consts3 is not None) and [consts3.title] or [None])[0] : ((consts3 is not None) and [consts3.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 4:
                        # grammar/ShyRecognizerBackend.g:34:11: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start167)
                        types4 = self.types()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'types' :
                            { ((types4 is not None) and [types4.title] or [None])[0] : ((types4 is not None) and [types4.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 5:
                        # grammar/ShyRecognizerBackend.g:39:11: messages
                        pass 
                        self._state.following.append(self.FOLLOW_messages_in_start193)
                        messages5 = self.messages()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'messages' :
                            { ((messages5 is not None) and [messages5.title] or [None])[0] : ((messages5 is not None) and [messages5.content] or [None])[0] } } )
                                    
                        #action end



                    elif alt1 == 6:
                        # grammar/ShyRecognizerBackend.g:44:11: vars
                        pass 
                        self._state.following.append(self.FOLLOW_vars_in_start219)
                        vars6 = self.vars()

                        self._state.following.pop()

                        #action start
                                    
                        value = merge ( value , { 'vars' :
                            { ((vars6 is not None) and [vars6.title] or [None])[0] : ((vars6 is not None) and [vars6.content] or [None])[0] } } )
                                    
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
    # grammar/ShyRecognizerBackend.g:52:1: module returns [ title , content ] : ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ( requests )? ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        ID7 = None
        module_queue8 = None

        procs9 = None

        receives10 = None

        requests11 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:54:5: ( ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ( requests )? ) )
                # grammar/ShyRecognizerBackend.g:54:9: ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ( requests )? )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module274)

                self.match(self.input, DOWN, None)
                ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_module276)

                #action start
                retval.title , retval.content = ID7.text , dict ( ) 
                #action end


                # grammar/ShyRecognizerBackend.g:56:13: ( module_queue )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == TREE_MODULE_QUEUE) :
                    alt2 = 1
                if alt2 == 1:
                    # grammar/ShyRecognizerBackend.g:56:15: module_queue
                    pass 
                    self._state.following.append(self.FOLLOW_module_queue_in_module306)
                    module_queue8 = self.module_queue()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'module_queue' ] = module_queue8 
                    #action end





                # grammar/ShyRecognizerBackend.g:59:13: ( procs )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == TREE_PROC) :
                    alt3 = 1
                if alt3 == 1:
                    # grammar/ShyRecognizerBackend.g:59:15: procs
                    pass 
                    self._state.following.append(self.FOLLOW_procs_in_module357)
                    procs9 = self.procs()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'proc' ] = procs9 
                    #action end





                # grammar/ShyRecognizerBackend.g:62:13: ( receives )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_RECEIVE) :
                    alt4 = 1
                if alt4 == 1:
                    # grammar/ShyRecognizerBackend.g:62:15: receives
                    pass 
                    self._state.following.append(self.FOLLOW_receives_in_module407)
                    receives10 = self.receives()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'receive' ] = receives10 
                    #action end





                # grammar/ShyRecognizerBackend.g:65:13: ( requests )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_REQUEST) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:65:15: requests
                    pass 
                    self._state.following.append(self.FOLLOW_requests_in_module457)
                    requests11 = self.requests()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'request' ] = requests11 
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
    # grammar/ShyRecognizerBackend.g:71:1: module_queue returns [ value ] : ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        value = None


        ID12 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:73:5: ( ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerBackend.g:73:9: ^( TREE_MODULE_QUEUE ID )
                pass 
                self.match(self.input, TREE_MODULE_QUEUE, self.FOLLOW_TREE_MODULE_QUEUE_in_module_queue530)

                self.match(self.input, DOWN, None)
                ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue532)

                self.match(self.input, UP, None)


                #action start
                value = ID12.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module_queue"


    class stateless_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.stateless_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "stateless"
    # grammar/ShyRecognizerBackend.g:76:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID13 = None
        ID14 = None
        procs15 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:78:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_STATELESS) :
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
                    # grammar/ShyRecognizerBackend.g:78:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless565)

                    self.match(self.input, DOWN, None)
                    ID13 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless567)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID13.text , dict ( ) 
                    #action end



                elif alt6 == 2:
                    # grammar/ShyRecognizerBackend.g:80:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless595)

                    self.match(self.input, DOWN, None)
                    ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless597)

                    self._state.following.append(self.FOLLOW_procs_in_stateless599)
                    procs15 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID14.text , procs15 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "requests"
    # grammar/ShyRecognizerBackend.g:84:1: requests returns [ value ] : ( request )+ ;
    def requests(self, ):
        value = None


        request16 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:87:5: ( ( request )+ )
                # grammar/ShyRecognizerBackend.g:87:9: ( request )+
                pass 
                # grammar/ShyRecognizerBackend.g:87:9: ( request )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == TREE_REQUEST) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerBackend.g:87:11: request
                        pass 
                        self._state.following.append(self.FOLLOW_request_in_requests654)
                        request16 = self.request()

                        self._state.following.pop()

                        #action start
                        value [ ((request16 is not None) and [request16.title] or [None])[0] ] = ((request16 is not None) and [request16.content] or [None])[0] 
                        #action end



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1





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
    # grammar/ShyRecognizerBackend.g:90:1: request returns [ title , content ] : ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) ;
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        ID17 = None
        local_vars18 = None

        statements19 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:93:5: ( ^( TREE_REQUEST ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:93:9: ^( TREE_REQUEST ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_REQUEST, self.FOLLOW_TREE_REQUEST_in_request699)

                self.match(self.input, DOWN, None)
                ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_request713)

                #action start
                retval.title = ID17.text 
                #action end


                # grammar/ShyRecognizerBackend.g:96:13: ( local_vars )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == TREE_LOCAL_VARS) :
                    alt8 = 1
                if alt8 == 1:
                    # grammar/ShyRecognizerBackend.g:96:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_request747)
                    local_vars18 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars18 
                    #action end





                # grammar/ShyRecognizerBackend.g:99:13: ( statements )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == TREE_STATEMENTS) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:99:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_request797)
                    statements19 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements19 
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
    # grammar/ShyRecognizerBackend.g:105:1: receives returns [ value ] : ( receive )+ ;
    def receives(self, ):
        value = None


        receive20 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:108:5: ( ( receive )+ )
                # grammar/ShyRecognizerBackend.g:108:9: ( receive )+
                pass 
                # grammar/ShyRecognizerBackend.g:108:9: ( receive )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_RECEIVE) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:108:11: receive
                        pass 
                        self._state.following.append(self.FOLLOW_receive_in_receives880)
                        receive20 = self.receive()

                        self._state.following.pop()

                        #action start
                        value [ ((receive20 is not None) and [receive20.title] or [None])[0] ] = ((receive20 is not None) and [receive20.content] or [None])[0] 
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

    # $ANTLR end "receives"


    class receive_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.receive_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "receive"
    # grammar/ShyRecognizerBackend.g:111:1: receive returns [ title , content ] : ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) ;
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        ID21 = None
        local_vars22 = None

        statements23 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:114:5: ( ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:114:9: ^( TREE_RECEIVE ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_RECEIVE, self.FOLLOW_TREE_RECEIVE_in_receive925)

                self.match(self.input, DOWN, None)
                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_receive939)

                #action start
                retval.title = ID21.text 
                #action end


                # grammar/ShyRecognizerBackend.g:117:13: ( local_vars )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_LOCAL_VARS) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:117:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_receive973)
                    local_vars22 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars22 
                    #action end





                # grammar/ShyRecognizerBackend.g:120:13: ( statements )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == TREE_STATEMENTS) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:120:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_receive1023)
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

    # $ANTLR end "receive"



    # $ANTLR start "procs"
    # grammar/ShyRecognizerBackend.g:126:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc24 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:129:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:129:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:129:9: ( proc )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_PROC) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:129:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs1106)
                        proc24 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc24 is not None) and [proc24.title] or [None])[0] ] = ((proc24 is not None) and [proc24.content] or [None])[0] 
                        #action end



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1





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
    # grammar/ShyRecognizerBackend.g:132:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID25 = None
        proc_args26 = None

        local_vars27 = None

        statements28 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:135:5: ( ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:135:9: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc1151)

                self.match(self.input, DOWN, None)
                ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_proc1165)

                #action start
                retval.title = ID25.text 
                #action end


                # grammar/ShyRecognizerBackend.g:138:13: ( proc_args )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == TREE_PROC_ARGS) :
                    alt14 = 1
                if alt14 == 1:
                    # grammar/ShyRecognizerBackend.g:138:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc1199)
                    proc_args26 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args26 
                    #action end





                # grammar/ShyRecognizerBackend.g:141:13: ( local_vars )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == TREE_LOCAL_VARS) :
                    alt15 = 1
                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:141:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_proc1249)
                    local_vars27 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars27 
                    #action end





                # grammar/ShyRecognizerBackend.g:144:13: ( statements )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == TREE_STATEMENTS) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/ShyRecognizerBackend.g:144:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc1299)
                    statements28 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements28 
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
    # grammar/ShyRecognizerBackend.g:150:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints29 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:152:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:152:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args1372)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args1374)
                attrs_hints29 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints29 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "local_vars"
    # grammar/ShyRecognizerBackend.g:156:1: local_vars returns [ value ] : ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        value = None


        attrs_hints30 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:158:5: ( ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:158:9: ^( TREE_LOCAL_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_LOCAL_VARS, self.FOLLOW_TREE_LOCAL_VARS_in_local_vars1419)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars1421)
                attrs_hints30 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints30 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "local_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:162:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement31 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:165:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:165:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements1476)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:165:28: ( statement )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_STATEMENT_ASSIGN or LA17_0 == TREE_STATEMENT_CALL or (TREE_STATEMENT_IF <= LA17_0 <= TREE_STATEMENT_WITH)) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:165:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1480)
                        statement31 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement31 ) 
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

    # $ANTLR end "statements"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:170:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with | statement_while );
    def statement(self, ):
        value = None


        statement_call32 = None

        statement_if33 = None

        statement_assign34 = None

        statement_with35 = None

        statement_while36 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:172:5: ( statement_call | statement_if | statement_assign | statement_with | statement_while )
                alt18 = 5
                LA18 = self.input.LA(1)
                if LA18 == TREE_STATEMENT_CALL:
                    alt18 = 1
                elif LA18 == TREE_STATEMENT_IF:
                    alt18 = 2
                elif LA18 == TREE_STATEMENT_ASSIGN:
                    alt18 = 3
                elif LA18 == TREE_STATEMENT_WITH:
                    alt18 = 4
                elif LA18 == TREE_STATEMENT_WHILE:
                    alt18 = 5
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerBackend.g:172:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement1536)
                    statement_call32 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call32 
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:174:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement1560)
                    statement_if33 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if33 
                    #action end



                elif alt18 == 3:
                    # grammar/ShyRecognizerBackend.g:176:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1584)
                    statement_assign34 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign34 
                    #action end



                elif alt18 == 4:
                    # grammar/ShyRecognizerBackend.g:178:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1608)
                    statement_with35 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with35 
                    #action end



                elif alt18 == 5:
                    # grammar/ShyRecognizerBackend.g:180:9: statement_while
                    pass 
                    self._state.following.append(self.FOLLOW_statement_while_in_statement1632)
                    statement_while36 = self.statement_while()

                    self._state.following.pop()

                    #action start
                    value = statement_while36 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:184:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID37 = None
        statements38 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:186:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:186:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1675)

                self.match(self.input, DOWN, None)
                ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1677)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1679)
                statements38 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID37.text : statements38 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:190:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID40 = None
        arbitrary_value39 = None


        value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:193:5: ( ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:193:9: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1730)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:194:13: ( arbitrary_value )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerBackend.g:194:15: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1746)
                        arbitrary_value39 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                                        
                        value [ 'assign' ] [ 'from' ] . append (
                            arbitrary_value39 )
                                        
                        #action end



                    else:
                        if cnt19 >= 1:
                            break #loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1


                self.match(self.input, TREE_STATEMENT_ASSIGN_TO, self.FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1794)

                # grammar/ShyRecognizerBackend.g:201:13: ( ID )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == ID) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:201:15: ID
                        pass 
                        ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1810)

                        #action start
                                        
                        value [ 'assign' ] [ 'to' ] . append (
                            ID40.text )
                                        
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

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:210:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) ;
    def statement_if(self, ):
        value = None


        conditional_ops41 = None

        statements42 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:213:5: ( ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) )
                # grammar/ShyRecognizerBackend.g:213:9: ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1893)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:214:13: ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_STATEMENT_ELIF) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:214:15: ^( TREE_STATEMENT_ELIF conditional_ops )
                        pass 
                        self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1911)

                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_conditional_ops_in_statement_if1913)
                        conditional_ops41 = self.conditional_ops()

                        self._state.following.pop()

                        self.match(self.input, UP, None)


                        #action start
                        value [ 'if' ] . append ( conditional_ops41 ) 
                        #action end



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1


                # grammar/ShyRecognizerBackend.g:217:13: ( ^( TREE_STATEMENT_ELSE statements ) )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == TREE_STATEMENT_ELSE) :
                    alt22 = 1
                if alt22 == 1:
                    # grammar/ShyRecognizerBackend.g:217:15: ^( TREE_STATEMENT_ELSE statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1967)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statements_in_statement_if1969)
                    statements42 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ 'else' ] = statements42 
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
    # grammar/ShyRecognizerBackend.g:223:1: statement_while returns [ value ] : ^( TREE_STATEMENT_WHILE conditional_ops ) ;
    def statement_while(self, ):
        value = None


        conditional_ops43 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:225:5: ( ^( TREE_STATEMENT_WHILE conditional_ops ) )
                # grammar/ShyRecognizerBackend.g:225:9: ^( TREE_STATEMENT_WHILE conditional_ops )
                pass 
                self.match(self.input, TREE_STATEMENT_WHILE, self.FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2044)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_conditional_ops_in_statement_while2046)
                conditional_ops43 = self.conditional_ops()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'while' : conditional_ops43 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_while"



    # $ANTLR start "conditional_ops"
    # grammar/ShyRecognizerBackend.g:229:1: conditional_ops returns [ value ] : ( condition_any statements | condition_all statements );
    def conditional_ops(self, ):
        value = None


        condition_any44 = None

        statements45 = None

        condition_all46 = None

        statements47 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:231:5: ( condition_any statements | condition_all statements )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == TREE_CONDITION_ANY) :
                    alt23 = 1
                elif (LA23_0 == TREE_CONDITION_ALL) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerBackend.g:231:9: condition_any statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_any_in_conditional_ops2089)
                    condition_any44 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2091)
                    statements45 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'any' : condition_any44 ,
                       'ops' : statements45 }
                                
                    #action end



                elif alt23 == 2:
                    # grammar/ShyRecognizerBackend.g:236:9: condition_all statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_all_in_conditional_ops2115)
                    condition_all46 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops2117)
                    statements47 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'all' : condition_all46 ,
                       'ops' : statements47 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "conditional_ops"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:243:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call48 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:246:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:246:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any2170)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:247:13: ( statement_call )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == TREE_STATEMENT_CALL) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerBackend.g:247:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any2186)
                        statement_call48 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call48 ) 
                        #action end



                    else:
                        if cnt24 >= 1:
                            break #loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:252:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call49 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:255:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:255:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all2261)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:256:13: ( statement_call )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == TREE_STATEMENT_CALL) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerBackend.g:256:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all2277)
                        statement_call49 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call49 ) 
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

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:261:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args50 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:263:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:263:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call2342)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call2344)
                    statement_call_args50 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args50 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:267:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value51 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:270:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:270:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:270:9: ( arbitrary_value )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA26_0 <= ID) or LA26_0 == MINUS or LA26_0 == NUMBER) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerBackend.g:270:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2399)
                        arbitrary_value51 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value51 ) 
                        #action end



                    else:
                        break #loop26





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:275:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID52 = None
        EXPRESSION53 = None
        num_whole54 = None

        num_fract55 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:277:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt27 = 4
                LA27 = self.input.LA(1)
                if LA27 == ID:
                    alt27 = 1
                elif LA27 == EXPRESSION:
                    alt27 = 2
                elif LA27 == MINUS:
                    LA27_3 = self.input.LA(2)

                    if (LA27_3 == NUMBER) :
                        LA27_5 = self.input.LA(3)

                        if (LA27_5 == DIVIDE) :
                            alt27 = 4
                        elif (LA27_5 == 3 or (EXPRESSION <= LA27_5 <= ID) or LA27_5 == MINUS or LA27_5 == NUMBER or LA27_5 == TREE_STATEMENT_ASSIGN_TO) :
                            alt27 = 3
                        else:
                            nvae = NoViableAltException("", 27, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 27, 3, self.input)

                        raise nvae


                elif LA27 == NUMBER:
                    LA27_4 = self.input.LA(2)

                    if (LA27_4 == DIVIDE) :
                        alt27 = 4
                    elif (LA27_4 == 3 or (EXPRESSION <= LA27_4 <= ID) or LA27_4 == MINUS or LA27_4 == NUMBER or LA27_4 == TREE_STATEMENT_ASSIGN_TO) :
                        alt27 = 3
                    else:
                        nvae = NoViableAltException("", 27, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammar/ShyRecognizerBackend.g:277:9: ID
                    pass 
                    ID52 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2452)

                    #action start
                    value = ID52.text 
                    #action end



                elif alt27 == 2:
                    # grammar/ShyRecognizerBackend.g:278:9: EXPRESSION
                    pass 
                    EXPRESSION53 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2464)

                    #action start
                    value = EXPRESSION53.text 
                    #action end



                elif alt27 == 3:
                    # grammar/ShyRecognizerBackend.g:279:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2476)
                    num_whole54 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole54 
                    #action end



                elif alt27 == 4:
                    # grammar/ShyRecognizerBackend.g:280:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2488)
                    num_fract55 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract55 
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
    # grammar/ShyRecognizerBackend.g:283:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID56 = None
        consts_items57 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:286:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:286:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts2529)

                self.match(self.input, DOWN, None)
                ID56 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2531)

                self._state.following.append(self.FOLLOW_consts_items_in_consts2533)
                consts_items57 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID56.text , consts_items57 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:290:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item58 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:293:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:293:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:293:9: ( consts_item )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA28_0 <= TREE_NUM_WHOLE)) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerBackend.g:293:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2588)
                        consts_item58 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item58 is not None) and [consts_item58.name] or [None])[0] ] = ((consts_item58 is not None) and [consts_item58.value] or [None])[0] 
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

    # $ANTLR end "consts_items"


    class consts_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerBackend.g:298:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID59 = None
        ID61 = None
        ID63 = None
        EXPRESSION64 = None
        num_whole60 = None

        num_fract62 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:300:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt29 = 3
                LA29 = self.input.LA(1)
                if LA29 == TREE_NUM_WHOLE:
                    alt29 = 1
                elif LA29 == TREE_NUM_FRACT:
                    alt29 = 2
                elif LA29 == TREE_EXPRESSION:
                    alt29 = 3
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # grammar/ShyRecognizerBackend.g:300:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2643)

                    self.match(self.input, DOWN, None)
                    ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2645)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2647)
                    num_whole60 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID59.text , num_whole60 
                    #action end



                elif alt29 == 2:
                    # grammar/ShyRecognizerBackend.g:302:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2675)

                    self.match(self.input, DOWN, None)
                    ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2677)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2679)
                    num_fract62 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID61.text , num_fract62 
                    #action end



                elif alt29 == 3:
                    # grammar/ShyRecognizerBackend.g:304:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2707)

                    self.match(self.input, DOWN, None)
                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2709)

                    EXPRESSION64 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2711)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID63.text , EXPRESSION64.text 
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
    # grammar/ShyRecognizerBackend.g:308:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID65 = None
        types_items66 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:311:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:311:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2766)

                self.match(self.input, DOWN, None)
                ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_types2768)

                self._state.following.append(self.FOLLOW_types_items_in_types2770)
                types_items66 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID65.text , types_items66 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:315:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item67 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:318:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:318:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:318:9: ( types_item )+
                cnt30 = 0
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == TREE_TYPES_ITEM) :
                        alt30 = 1


                    if alt30 == 1:
                        # grammar/ShyRecognizerBackend.g:318:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2825)
                        types_item67 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item67 is not None) and [types_item67.name] or [None])[0] ] = ((types_item67 is not None) and [types_item67.value] or [None])[0] 
                        #action end



                    else:
                        if cnt30 >= 1:
                            break #loop30

                        eee = EarlyExitException(30, self.input)
                        raise eee

                    cnt30 += 1





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
    # grammar/ShyRecognizerBackend.g:323:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID68 = None
        attrs_hints69 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:325:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:325:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2880)

                self.match(self.input, DOWN, None)
                ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2882)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2884)
                attrs_hints69 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID68.text , attrs_hints69 
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
    # grammar/ShyRecognizerBackend.g:329:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID70 = None
        messages_items71 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:332:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:332:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2939)

                self.match(self.input, DOWN, None)
                ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2941)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2943)
                messages_items71 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID70.text , messages_items71 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:336:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item72 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:339:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:339:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:339:9: ( messages_item )+
                cnt31 = 0
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == TREE_MESSAGES_ITEM) :
                        alt31 = 1


                    if alt31 == 1:
                        # grammar/ShyRecognizerBackend.g:339:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2998)
                        messages_item72 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item72 is not None) and [messages_item72.name] or [None])[0] ] = ((messages_item72 is not None) and [messages_item72.value] or [None])[0] 
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

    # $ANTLR end "messages_items"


    class messages_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.messages_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerBackend.g:344:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID73 = None
        attrs_hints74 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:346:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:346:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3053)

                self.match(self.input, DOWN, None)
                ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3055)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3057)
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

    # $ANTLR end "messages_item"


    class vars_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.vars_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "vars"
    # grammar/ShyRecognizerBackend.g:350:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID75 = None
        attrs_hints76 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:352:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:352:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars3102)

                self.match(self.input, DOWN, None)
                ID75 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3104)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3106)
                attrs_hints76 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID75.text , attrs_hints76 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:356:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint77 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:359:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:359:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3159)

                # grammar/ShyRecognizerBackend.g:359:26: ( attr_hint )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == TREE_ATTR_HINT) :
                        alt32 = 1


                    if alt32 == 1:
                        # grammar/ShyRecognizerBackend.g:359:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3163)
                        attr_hint77 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint77 ) 
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
    # grammar/ShyRecognizerBackend.g:362:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID78 = None
        ID79 = None
        hint80 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:365:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
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
                    # grammar/ShyRecognizerBackend.g:365:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3208)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint3210)

                    # grammar/ShyRecognizerBackend.g:365:42: ( ^( TREE_ATTR ID ) )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == TREE_ATTR) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerBackend.g:365:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3216)

                            self.match(self.input, DOWN, None)
                            ID78 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3218)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID78.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


                    self.match(self.input, UP, None)



                elif alt35 == 2:
                    # grammar/ShyRecognizerBackend.g:368:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint3260)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3262)
                    hint80 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:368:32: ( ^( TREE_ATTR ID ) )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == TREE_ATTR) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerBackend.g:368:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint3268)

                            self.match(self.input, DOWN, None)
                            ID79 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3270)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID79.text ] = hint80 
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
    # grammar/ShyRecognizerBackend.g:373:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID81 = None
        ID82 = None
        hint_args83 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:376:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
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
                    # grammar/ShyRecognizerBackend.g:376:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3339)

                    self.match(self.input, DOWN, None)
                    ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3341)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID81.text ] = list ( ) 
                    #action end



                elif alt36 == 2:
                    # grammar/ShyRecognizerBackend.g:378:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3369)

                    self.match(self.input, DOWN, None)
                    ID82 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3371)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint3373)
                    hint_args83 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID82.text ] = hint_args83 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:382:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg84 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:385:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:385:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:385:9: ( hint_arg )+
                cnt37 = 0
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == ID or LA37_0 == UNDERSCORE) :
                        alt37 = 1


                    if alt37 == 1:
                        # grammar/ShyRecognizerBackend.g:385:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args3428)
                        hint_arg84 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg84 ) 
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
    # grammar/ShyRecognizerBackend.g:388:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID85 = None
        UNDERSCORE86 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:390:5: ( ID | UNDERSCORE )
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
                    # grammar/ShyRecognizerBackend.g:390:9: ID
                    pass 
                    ID85 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg3461)

                    #action start
                    value = ID85.text 
                    #action end



                elif alt38 == 2:
                    # grammar/ShyRecognizerBackend.g:391:9: UNDERSCORE
                    pass 
                    UNDERSCORE86 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg3473)

                    #action start
                    value = UNDERSCORE86.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:394:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS87 = None
        NUMBER88 = None
        NUMBER89 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:396:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:396:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:396:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:396:11: MINUS NUMBER
                    pass 
                    MINUS87 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3504)

                    NUMBER88 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3506)




                    #action start
                    value = int ( MINUS87.text + NUMBER88.text ) 
                    #action end



                elif alt39 == 2:
                    # grammar/ShyRecognizerBackend.g:398:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:398:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:398:11: NUMBER
                    pass 
                    NUMBER89 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3534)




                    #action start
                    value = int ( NUMBER89.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:402:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS90 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:404:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:404:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:404:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:404:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS90 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3579)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3585)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3587)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3593)




                    #action start
                                
                    value = Fraction ( int ( MINUS90.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt40 == 2:
                    # grammar/ShyRecognizerBackend.g:409:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:409:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:409:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3625)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3627)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3633)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 43, 50, 52, 63, 73, 75])
    FOLLOW_stateless_in_start114 = frozenset([1, 43, 50, 52, 63, 73, 75])
    FOLLOW_consts_in_start141 = frozenset([1, 43, 50, 52, 63, 73, 75])
    FOLLOW_types_in_start167 = frozenset([1, 43, 50, 52, 63, 73, 75])
    FOLLOW_messages_in_start193 = frozenset([1, 43, 50, 52, 63, 73, 75])
    FOLLOW_vars_in_start219 = frozenset([1, 43, 50, 52, 63, 73, 75])
    FOLLOW_TREE_MODULE_in_module274 = frozenset([2])
    FOLLOW_ID_in_module276 = frozenset([3, 53, 59, 61, 62])
    FOLLOW_module_queue_in_module306 = frozenset([3, 59, 61, 62])
    FOLLOW_procs_in_module357 = frozenset([3, 61, 62])
    FOLLOW_receives_in_module407 = frozenset([3, 62])
    FOLLOW_requests_in_module457 = frozenset([3])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue530 = frozenset([2])
    FOLLOW_ID_in_module_queue532 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless565 = frozenset([2])
    FOLLOW_ID_in_stateless567 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless595 = frozenset([2])
    FOLLOW_ID_in_stateless597 = frozenset([59])
    FOLLOW_procs_in_stateless599 = frozenset([3])
    FOLLOW_request_in_requests654 = frozenset([1, 62])
    FOLLOW_TREE_REQUEST_in_request699 = frozenset([2])
    FOLLOW_ID_in_request713 = frozenset([3, 49, 64])
    FOLLOW_local_vars_in_request747 = frozenset([3, 64])
    FOLLOW_statements_in_request797 = frozenset([3])
    FOLLOW_receive_in_receives880 = frozenset([1, 61])
    FOLLOW_TREE_RECEIVE_in_receive925 = frozenset([2])
    FOLLOW_ID_in_receive939 = frozenset([3, 49, 64])
    FOLLOW_local_vars_in_receive973 = frozenset([3, 64])
    FOLLOW_statements_in_receive1023 = frozenset([3])
    FOLLOW_proc_in_procs1106 = frozenset([1, 59])
    FOLLOW_TREE_PROC_in_proc1151 = frozenset([2])
    FOLLOW_ID_in_proc1165 = frozenset([3, 49, 60, 64])
    FOLLOW_proc_args_in_proc1199 = frozenset([3, 49, 64])
    FOLLOW_local_vars_in_proc1249 = frozenset([3, 64])
    FOLLOW_statements_in_proc1299 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args1372 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args1374 = frozenset([3])
    FOLLOW_TREE_LOCAL_VARS_in_local_vars1419 = frozenset([2])
    FOLLOW_attrs_hints_in_local_vars1421 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements1476 = frozenset([2])
    FOLLOW_statement_in_statements1480 = frozenset([3, 65, 67, 70, 71, 72])
    FOLLOW_statement_call_in_statement1536 = frozenset([1])
    FOLLOW_statement_if_in_statement1560 = frozenset([1])
    FOLLOW_statement_assign_in_statement1584 = frozenset([1])
    FOLLOW_statement_with_in_statement1608 = frozenset([1])
    FOLLOW_statement_while_in_statement1632 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1675 = frozenset([2])
    FOLLOW_ID_in_statement_with1677 = frozenset([64])
    FOLLOW_statements_in_statement_with1679 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1730 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1746 = frozenset([18, 19, 23, 27, 66])
    FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1794 = frozenset([19])
    FOLLOW_ID_in_statement_assign1810 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1893 = frozenset([2])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1911 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_if1913 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1967 = frozenset([2])
    FOLLOW_statements_in_statement_if1969 = frozenset([3])
    FOLLOW_TREE_STATEMENT_WHILE_in_statement_while2044 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_while2046 = frozenset([3])
    FOLLOW_condition_any_in_conditional_ops2089 = frozenset([64])
    FOLLOW_statements_in_conditional_ops2091 = frozenset([1])
    FOLLOW_condition_all_in_conditional_ops2115 = frozenset([64])
    FOLLOW_statements_in_conditional_ops2117 = frozenset([1])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any2170 = frozenset([2])
    FOLLOW_statement_call_in_condition_any2186 = frozenset([3, 67])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all2261 = frozenset([2])
    FOLLOW_statement_call_in_condition_all2277 = frozenset([3, 67])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call2342 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call2344 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args2399 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value2452 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2464 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2476 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2488 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts2529 = frozenset([2])
    FOLLOW_ID_in_consts2531 = frozenset([46, 54, 55])
    FOLLOW_consts_items_in_consts2533 = frozenset([3])
    FOLLOW_consts_item_in_consts_items2588 = frozenset([1, 46, 54, 55])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2643 = frozenset([2])
    FOLLOW_ID_in_consts_item2645 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2647 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2675 = frozenset([2])
    FOLLOW_ID_in_consts_item2677 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2679 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2707 = frozenset([2])
    FOLLOW_ID_in_consts_item2709 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2711 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2766 = frozenset([2])
    FOLLOW_ID_in_types2768 = frozenset([74])
    FOLLOW_types_items_in_types2770 = frozenset([3])
    FOLLOW_types_item_in_types_items2825 = frozenset([1, 74])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2880 = frozenset([2])
    FOLLOW_ID_in_types_item2882 = frozenset([39])
    FOLLOW_attrs_hints_in_types_item2884 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2939 = frozenset([2])
    FOLLOW_ID_in_messages2941 = frozenset([51])
    FOLLOW_messages_items_in_messages2943 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2998 = frozenset([1, 51])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item3053 = frozenset([2])
    FOLLOW_ID_in_messages_item3055 = frozenset([39])
    FOLLOW_attrs_hints_in_messages_item3057 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars3102 = frozenset([2])
    FOLLOW_ID_in_vars3104 = frozenset([39])
    FOLLOW_attrs_hints_in_vars3106 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints3159 = frozenset([1, 40])
    FOLLOW_attr_hint_in_attrs_hints3163 = frozenset([1, 40])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3208 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint3210 = frozenset([38])
    FOLLOW_TREE_ATTR_in_attr_hint3216 = frozenset([2])
    FOLLOW_ID_in_attr_hint3218 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint3260 = frozenset([2])
    FOLLOW_hint_in_attr_hint3262 = frozenset([38])
    FOLLOW_TREE_ATTR_in_attr_hint3268 = frozenset([2])
    FOLLOW_ID_in_attr_hint3270 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3339 = frozenset([2])
    FOLLOW_ID_in_hint3341 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3369 = frozenset([2])
    FOLLOW_ID_in_hint3371 = frozenset([19, 77])
    FOLLOW_hint_args_in_hint3373 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args3428 = frozenset([1, 19, 77])
    FOLLOW_ID_in_hint_arg3461 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg3473 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3504 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3506 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole3534 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3579 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3585 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3587 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3593 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract3625 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3627 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3633 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
