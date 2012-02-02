# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-02 18:47:21

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
TREE_STATELESS=62
TREE_STATEMENTS=63
TREE_STATEMENT_ASSIGN=64
TREE_STATEMENT_ASSIGN_TO=65
TREE_STATEMENT_CALL=66
TREE_STATEMENT_ELIF=67
TREE_STATEMENT_ELSE=68
TREE_STATEMENT_IF=69
TREE_STATEMENT_WHILE=70
TREE_STATEMENT_WITH=71
TREE_TYPES=72
TREE_TYPES_ITEM=73
TREE_VARS=74
TYPES=75
UNDERSCORE=76
VARS=77
WHILE=78
WHITESPACE=79
WITH=80

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
    "TREE_PROC_ARGS", "TREE_RECEIVE", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", "TREE_STATEMENT_CALL", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WHILE", 
    "TREE_STATEMENT_WITH", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", 
    "TYPES", "UNDERSCORE", "VARS", "WHILE", "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:52:1: module returns [ title , content ] : ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        ID7 = None
        module_queue8 = None

        procs9 = None

        receives10 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:54:5: ( ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? ) )
                # grammar/ShyRecognizerBackend.g:54:9: ^( TREE_MODULE ID ( module_queue )? ( procs )? ( receives )? )
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





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "module"



    # $ANTLR start "module_queue"
    # grammar/ShyRecognizerBackend.g:68:1: module_queue returns [ value ] : ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        value = None


        ID11 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:70:5: ( ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerBackend.g:70:9: ^( TREE_MODULE_QUEUE ID )
                pass 
                self.match(self.input, TREE_MODULE_QUEUE, self.FOLLOW_TREE_MODULE_QUEUE_in_module_queue480)

                self.match(self.input, DOWN, None)
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue482)

                self.match(self.input, UP, None)


                #action start
                value = ID11.text 
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
    # grammar/ShyRecognizerBackend.g:73:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID12 = None
        ID13 = None
        procs14 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:75:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
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
                    # grammar/ShyRecognizerBackend.g:75:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless515)

                    self.match(self.input, DOWN, None)
                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless517)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID12.text , dict ( ) 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyRecognizerBackend.g:77:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless545)

                    self.match(self.input, DOWN, None)
                    ID13 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless547)

                    self._state.following.append(self.FOLLOW_procs_in_stateless549)
                    procs14 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID13.text , procs14 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "receives"
    # grammar/ShyRecognizerBackend.g:81:1: receives returns [ value ] : ( receive )+ ;
    def receives(self, ):
        value = None


        receive15 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:84:5: ( ( receive )+ )
                # grammar/ShyRecognizerBackend.g:84:9: ( receive )+
                pass 
                # grammar/ShyRecognizerBackend.g:84:9: ( receive )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TREE_RECEIVE) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyRecognizerBackend.g:84:11: receive
                        pass 
                        self._state.following.append(self.FOLLOW_receive_in_receives604)
                        receive15 = self.receive()

                        self._state.following.pop()

                        #action start
                        value [ ((receive15 is not None) and [receive15.title] or [None])[0] ] = ((receive15 is not None) and [receive15.content] or [None])[0] 
                        #action end



                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1





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
    # grammar/ShyRecognizerBackend.g:87:1: receive returns [ title , content ] : ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) ;
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        ID16 = None
        local_vars17 = None

        statements18 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:90:5: ( ^( TREE_RECEIVE ID ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:90:9: ^( TREE_RECEIVE ID ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_RECEIVE, self.FOLLOW_TREE_RECEIVE_in_receive649)

                self.match(self.input, DOWN, None)
                ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_receive663)

                #action start
                retval.title = ID16.text 
                #action end


                # grammar/ShyRecognizerBackend.g:93:13: ( local_vars )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == TREE_LOCAL_VARS) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:93:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_receive697)
                    local_vars17 = self.local_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = local_vars17 
                    #action end





                # grammar/ShyRecognizerBackend.g:96:13: ( statements )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == TREE_STATEMENTS) :
                    alt8 = 1
                if alt8 == 1:
                    # grammar/ShyRecognizerBackend.g:96:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_receive747)
                    statements18 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements18 
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
    # grammar/ShyRecognizerBackend.g:102:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc19 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:105:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:105:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:105:9: ( proc )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == TREE_PROC) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerBackend.g:105:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs830)
                        proc19 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc19 is not None) and [proc19.title] or [None])[0] ] = ((proc19 is not None) and [proc19.content] or [None])[0] 
                        #action end



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1





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
    # grammar/ShyRecognizerBackend.g:108:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID20 = None
        proc_args21 = None

        local_vars22 = None

        statements23 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:111:5: ( ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:111:9: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc875)

                self.match(self.input, DOWN, None)
                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_proc889)

                #action start
                retval.title = ID20.text 
                #action end


                # grammar/ShyRecognizerBackend.g:114:13: ( proc_args )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == TREE_PROC_ARGS) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerBackend.g:114:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc923)
                    proc_args21 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args21 
                    #action end





                # grammar/ShyRecognizerBackend.g:117:13: ( local_vars )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_LOCAL_VARS) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:117:15: local_vars
                    pass 
                    self._state.following.append(self.FOLLOW_local_vars_in_proc973)
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
                    self._state.following.append(self.FOLLOW_statements_in_proc1023)
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

    # $ANTLR end "proc"



    # $ANTLR start "proc_args"
    # grammar/ShyRecognizerBackend.g:126:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:128:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:128:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args1096)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args1098)
                attrs_hints24 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints24 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "local_vars"
    # grammar/ShyRecognizerBackend.g:132:1: local_vars returns [ value ] : ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        value = None


        attrs_hints25 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:134:5: ( ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:134:9: ^( TREE_LOCAL_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_LOCAL_VARS, self.FOLLOW_TREE_LOCAL_VARS_in_local_vars1143)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars1145)
                attrs_hints25 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints25 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "local_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:138:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement26 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:141:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:141:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements1200)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:141:28: ( statement )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_STATEMENT_ASSIGN or LA13_0 == TREE_STATEMENT_CALL or (TREE_STATEMENT_IF <= LA13_0 <= TREE_STATEMENT_WITH)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:141:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1204)
                        statement26 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement26 ) 
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
    # grammar/ShyRecognizerBackend.g:146:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with | statement_while );
    def statement(self, ):
        value = None


        statement_call27 = None

        statement_if28 = None

        statement_assign29 = None

        statement_with30 = None

        statement_while31 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:148:5: ( statement_call | statement_if | statement_assign | statement_with | statement_while )
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
                    # grammar/ShyRecognizerBackend.g:148:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement1260)
                    statement_call27 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call27 
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:150:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement1284)
                    statement_if28 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if28 
                    #action end



                elif alt14 == 3:
                    # grammar/ShyRecognizerBackend.g:152:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1308)
                    statement_assign29 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign29 
                    #action end



                elif alt14 == 4:
                    # grammar/ShyRecognizerBackend.g:154:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1332)
                    statement_with30 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with30 
                    #action end



                elif alt14 == 5:
                    # grammar/ShyRecognizerBackend.g:156:9: statement_while
                    pass 
                    self._state.following.append(self.FOLLOW_statement_while_in_statement1356)
                    statement_while31 = self.statement_while()

                    self._state.following.pop()

                    #action start
                    value = statement_while31 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:160:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID32 = None
        statements33 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:162:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:162:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1399)

                self.match(self.input, DOWN, None)
                ID32 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1401)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1403)
                statements33 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID32.text : statements33 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:166:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID35 = None
        arbitrary_value34 = None


        value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:169:5: ( ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:169:9: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1454)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:170:13: ( arbitrary_value )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA15_0 <= ID) or LA15_0 == MINUS or LA15_0 == NUMBER) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:170:15: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1470)
                        arbitrary_value34 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                                        
                        value [ 'assign' ] [ 'from' ] . append (
                            arbitrary_value34 )
                                        
                        #action end



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                self.match(self.input, TREE_STATEMENT_ASSIGN_TO, self.FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1518)

                # grammar/ShyRecognizerBackend.g:177:13: ( ID )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ID) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:177:15: ID
                        pass 
                        ID35 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1534)

                        #action start
                                        
                        value [ 'assign' ] [ 'to' ] . append (
                            ID35.text )
                                        
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
    # grammar/ShyRecognizerBackend.g:186:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) ;
    def statement_if(self, ):
        value = None


        conditional_ops36 = None

        statements37 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:189:5: ( ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) )
                # grammar/ShyRecognizerBackend.g:189:9: ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1617)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:190:13: ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_STATEMENT_ELIF) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:190:15: ^( TREE_STATEMENT_ELIF conditional_ops )
                        pass 
                        self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1635)

                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_conditional_ops_in_statement_if1637)
                        conditional_ops36 = self.conditional_ops()

                        self._state.following.pop()

                        self.match(self.input, UP, None)


                        #action start
                        value [ 'if' ] . append ( conditional_ops36 ) 
                        #action end



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1


                # grammar/ShyRecognizerBackend.g:193:13: ( ^( TREE_STATEMENT_ELSE statements ) )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == TREE_STATEMENT_ELSE) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerBackend.g:193:15: ^( TREE_STATEMENT_ELSE statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1691)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statements_in_statement_if1693)
                    statements37 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ 'else' ] = statements37 
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
    # grammar/ShyRecognizerBackend.g:199:1: statement_while returns [ value ] : ^( TREE_STATEMENT_WHILE conditional_ops ) ;
    def statement_while(self, ):
        value = None


        conditional_ops38 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:201:5: ( ^( TREE_STATEMENT_WHILE conditional_ops ) )
                # grammar/ShyRecognizerBackend.g:201:9: ^( TREE_STATEMENT_WHILE conditional_ops )
                pass 
                self.match(self.input, TREE_STATEMENT_WHILE, self.FOLLOW_TREE_STATEMENT_WHILE_in_statement_while1768)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_conditional_ops_in_statement_while1770)
                conditional_ops38 = self.conditional_ops()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'while' : conditional_ops38 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_while"



    # $ANTLR start "conditional_ops"
    # grammar/ShyRecognizerBackend.g:205:1: conditional_ops returns [ value ] : ( condition_any statements | condition_all statements );
    def conditional_ops(self, ):
        value = None


        condition_any39 = None

        statements40 = None

        condition_all41 = None

        statements42 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:207:5: ( condition_any statements | condition_all statements )
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
                    # grammar/ShyRecognizerBackend.g:207:9: condition_any statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_any_in_conditional_ops1813)
                    condition_any39 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops1815)
                    statements40 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'any' : condition_any39 ,
                       'ops' : statements40 }
                                
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:212:9: condition_all statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_all_in_conditional_ops1839)
                    condition_all41 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops1841)
                    statements42 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'all' : condition_all41 ,
                       'ops' : statements42 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "conditional_ops"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:219:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call43 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:222:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:222:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1894)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:223:13: ( statement_call )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_STATEMENT_CALL) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:223:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1910)
                        statement_call43 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call43 ) 
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
    # grammar/ShyRecognizerBackend.g:228:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call44 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:231:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:231:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1985)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:232:13: ( statement_call )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_STATEMENT_CALL) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:232:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all2001)
                        statement_call44 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call44 ) 
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
    # grammar/ShyRecognizerBackend.g:237:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args45 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:239:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:239:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call2066)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call2068)
                    statement_call_args45 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args45 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:243:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value46 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:246:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:246:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:246:9: ( arbitrary_value )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:246:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2123)
                        arbitrary_value46 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value46 ) 
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
    # grammar/ShyRecognizerBackend.g:251:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID47 = None
        EXPRESSION48 = None
        num_whole49 = None

        num_fract50 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:253:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt23 = 4
                LA23 = self.input.LA(1)
                if LA23 == ID:
                    alt23 = 1
                elif LA23 == EXPRESSION:
                    alt23 = 2
                elif LA23 == MINUS:
                    LA23_3 = self.input.LA(2)

                    if (LA23_3 == NUMBER) :
                        LA23_5 = self.input.LA(3)

                        if (LA23_5 == DIVIDE) :
                            alt23 = 4
                        elif (LA23_5 == 3 or (EXPRESSION <= LA23_5 <= ID) or LA23_5 == MINUS or LA23_5 == NUMBER or LA23_5 == TREE_STATEMENT_ASSIGN_TO) :
                            alt23 = 3
                        else:
                            nvae = NoViableAltException("", 23, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 23, 3, self.input)

                        raise nvae


                elif LA23 == NUMBER:
                    LA23_4 = self.input.LA(2)

                    if (LA23_4 == DIVIDE) :
                        alt23 = 4
                    elif (LA23_4 == 3 or (EXPRESSION <= LA23_4 <= ID) or LA23_4 == MINUS or LA23_4 == NUMBER or LA23_4 == TREE_STATEMENT_ASSIGN_TO) :
                        alt23 = 3
                    else:
                        nvae = NoViableAltException("", 23, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerBackend.g:253:9: ID
                    pass 
                    ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2176)

                    #action start
                    value = ID47.text 
                    #action end



                elif alt23 == 2:
                    # grammar/ShyRecognizerBackend.g:254:9: EXPRESSION
                    pass 
                    EXPRESSION48 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2188)

                    #action start
                    value = EXPRESSION48.text 
                    #action end



                elif alt23 == 3:
                    # grammar/ShyRecognizerBackend.g:255:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2200)
                    num_whole49 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole49 
                    #action end



                elif alt23 == 4:
                    # grammar/ShyRecognizerBackend.g:256:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2212)
                    num_fract50 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract50 
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
    # grammar/ShyRecognizerBackend.g:259:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID51 = None
        consts_items52 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:262:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:262:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts2253)

                self.match(self.input, DOWN, None)
                ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2255)

                self._state.following.append(self.FOLLOW_consts_items_in_consts2257)
                consts_items52 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID51.text , consts_items52 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:266:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item53 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:269:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:269:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:269:9: ( consts_item )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA24_0 <= TREE_NUM_WHOLE)) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerBackend.g:269:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2312)
                        consts_item53 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item53 is not None) and [consts_item53.name] or [None])[0] ] = ((consts_item53 is not None) and [consts_item53.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:274:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID54 = None
        ID56 = None
        ID58 = None
        EXPRESSION59 = None
        num_whole55 = None

        num_fract57 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:276:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerBackend.g:276:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2367)

                    self.match(self.input, DOWN, None)
                    ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2369)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2371)
                    num_whole55 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID54.text , num_whole55 
                    #action end



                elif alt25 == 2:
                    # grammar/ShyRecognizerBackend.g:278:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2399)

                    self.match(self.input, DOWN, None)
                    ID56 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2401)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2403)
                    num_fract57 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID56.text , num_fract57 
                    #action end



                elif alt25 == 3:
                    # grammar/ShyRecognizerBackend.g:280:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2431)

                    self.match(self.input, DOWN, None)
                    ID58 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2433)

                    EXPRESSION59 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2435)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID58.text , EXPRESSION59.text 
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
    # grammar/ShyRecognizerBackend.g:284:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID60 = None
        types_items61 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:287:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:287:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2490)

                self.match(self.input, DOWN, None)
                ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_types2492)

                self._state.following.append(self.FOLLOW_types_items_in_types2494)
                types_items61 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID60.text , types_items61 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:291:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item62 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:294:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:294:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:294:9: ( types_item )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == TREE_TYPES_ITEM) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerBackend.g:294:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2549)
                        types_item62 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item62 is not None) and [types_item62.name] or [None])[0] ] = ((types_item62 is not None) and [types_item62.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:299:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID63 = None
        attrs_hints64 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:301:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:301:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2604)

                self.match(self.input, DOWN, None)
                ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2606)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2608)
                attrs_hints64 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID63.text , attrs_hints64 
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
    # grammar/ShyRecognizerBackend.g:305:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID65 = None
        messages_items66 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:308:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:308:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2663)

                self.match(self.input, DOWN, None)
                ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2665)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2667)
                messages_items66 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID65.text , messages_items66 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:312:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item67 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:315:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:315:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:315:9: ( messages_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == TREE_MESSAGES_ITEM) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerBackend.g:315:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2722)
                        messages_item67 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item67 is not None) and [messages_item67.name] or [None])[0] ] = ((messages_item67 is not None) and [messages_item67.value] or [None])[0] 
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


    class messages_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.messages_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerBackend.g:320:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID68 = None
        attrs_hints69 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:322:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:322:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2777)

                self.match(self.input, DOWN, None)
                ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2779)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2781)
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

    # $ANTLR end "messages_item"


    class vars_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.vars_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "vars"
    # grammar/ShyRecognizerBackend.g:326:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID70 = None
        attrs_hints71 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:328:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:328:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars2826)

                self.match(self.input, DOWN, None)
                ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2828)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2830)
                attrs_hints71 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID70.text , attrs_hints71 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:332:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint72 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:335:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:335:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2883)

                # grammar/ShyRecognizerBackend.g:335:26: ( attr_hint )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == TREE_ATTR_HINT) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerBackend.g:335:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2887)
                        attr_hint72 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint72 ) 
                        #action end



                    else:
                        break #loop28





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:338:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID73 = None
        ID74 = None
        hint75 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:341:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == TREE_ATTR_HINT) :
                    LA31_1 = self.input.LA(2)

                    if (LA31_1 == 2) :
                        LA31_2 = self.input.LA(3)

                        if (LA31_2 == TREE_HINT_NONE) :
                            alt31 = 1
                        elif (LA31_2 == TREE_HINT) :
                            alt31 = 2
                        else:
                            nvae = NoViableAltException("", 31, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 31, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae


                if alt31 == 1:
                    # grammar/ShyRecognizerBackend.g:341:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2932)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint2934)

                    # grammar/ShyRecognizerBackend.g:341:42: ( ^( TREE_ATTR ID ) )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == TREE_ATTR) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerBackend.g:341:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2940)

                            self.match(self.input, DOWN, None)
                            ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2942)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID73.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    self.match(self.input, UP, None)



                elif alt31 == 2:
                    # grammar/ShyRecognizerBackend.g:344:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2984)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2986)
                    hint75 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:344:32: ( ^( TREE_ATTR ID ) )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == TREE_ATTR) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerBackend.g:344:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2992)

                            self.match(self.input, DOWN, None)
                            ID74 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2994)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID74.text ] = hint75 
                            #action end



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:349:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID76 = None
        ID77 = None
        hint_args78 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:352:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == TREE_HINT) :
                    LA32_1 = self.input.LA(2)

                    if (LA32_1 == 2) :
                        LA32_2 = self.input.LA(3)

                        if (LA32_2 == ID) :
                            LA32_3 = self.input.LA(4)

                            if (LA32_3 == 3) :
                                alt32 = 1
                            elif (LA32_3 == ID or LA32_3 == UNDERSCORE) :
                                alt32 = 2
                            else:
                                nvae = NoViableAltException("", 32, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 32, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 32, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # grammar/ShyRecognizerBackend.g:352:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3063)

                    self.match(self.input, DOWN, None)
                    ID76 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3065)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID76.text ] = list ( ) 
                    #action end



                elif alt32 == 2:
                    # grammar/ShyRecognizerBackend.g:354:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint3093)

                    self.match(self.input, DOWN, None)
                    ID77 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3095)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint3097)
                    hint_args78 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID77.text ] = hint_args78 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:358:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg79 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:361:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:361:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:361:9: ( hint_arg )+
                cnt33 = 0
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == ID or LA33_0 == UNDERSCORE) :
                        alt33 = 1


                    if alt33 == 1:
                        # grammar/ShyRecognizerBackend.g:361:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args3152)
                        hint_arg79 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg79 ) 
                        #action end



                    else:
                        if cnt33 >= 1:
                            break #loop33

                        eee = EarlyExitException(33, self.input)
                        raise eee

                    cnt33 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:364:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID80 = None
        UNDERSCORE81 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:366:5: ( ID | UNDERSCORE )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == ID) :
                    alt34 = 1
                elif (LA34_0 == UNDERSCORE) :
                    alt34 = 2
                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae


                if alt34 == 1:
                    # grammar/ShyRecognizerBackend.g:366:9: ID
                    pass 
                    ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg3185)

                    #action start
                    value = ID80.text 
                    #action end



                elif alt34 == 2:
                    # grammar/ShyRecognizerBackend.g:367:9: UNDERSCORE
                    pass 
                    UNDERSCORE81 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg3197)

                    #action start
                    value = UNDERSCORE81.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:370:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS82 = None
        NUMBER83 = None
        NUMBER84 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:372:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == MINUS) :
                    alt35 = 1
                elif (LA35_0 == NUMBER) :
                    alt35 = 2
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae


                if alt35 == 1:
                    # grammar/ShyRecognizerBackend.g:372:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:372:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:372:11: MINUS NUMBER
                    pass 
                    MINUS82 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3228)

                    NUMBER83 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3230)




                    #action start
                    value = int ( MINUS82.text + NUMBER83.text ) 
                    #action end



                elif alt35 == 2:
                    # grammar/ShyRecognizerBackend.g:374:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:374:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:374:11: NUMBER
                    pass 
                    NUMBER84 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3258)




                    #action start
                    value = int ( NUMBER84.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:378:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS85 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:380:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == MINUS) :
                    alt36 = 1
                elif (LA36_0 == NUMBER) :
                    alt36 = 2
                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # grammar/ShyRecognizerBackend.g:380:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:380:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:380:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS85 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3303)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3309)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3311)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3317)




                    #action start
                                
                    value = Fraction ( int ( MINUS85.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt36 == 2:
                    # grammar/ShyRecognizerBackend.g:385:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:385:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:385:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3349)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3351)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3357)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 43, 50, 52, 62, 72, 74])
    FOLLOW_stateless_in_start114 = frozenset([1, 43, 50, 52, 62, 72, 74])
    FOLLOW_consts_in_start141 = frozenset([1, 43, 50, 52, 62, 72, 74])
    FOLLOW_types_in_start167 = frozenset([1, 43, 50, 52, 62, 72, 74])
    FOLLOW_messages_in_start193 = frozenset([1, 43, 50, 52, 62, 72, 74])
    FOLLOW_vars_in_start219 = frozenset([1, 43, 50, 52, 62, 72, 74])
    FOLLOW_TREE_MODULE_in_module274 = frozenset([2])
    FOLLOW_ID_in_module276 = frozenset([3, 53, 59, 61])
    FOLLOW_module_queue_in_module306 = frozenset([3, 59, 61])
    FOLLOW_procs_in_module357 = frozenset([3, 61])
    FOLLOW_receives_in_module407 = frozenset([3])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue480 = frozenset([2])
    FOLLOW_ID_in_module_queue482 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless515 = frozenset([2])
    FOLLOW_ID_in_stateless517 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless545 = frozenset([2])
    FOLLOW_ID_in_stateless547 = frozenset([59])
    FOLLOW_procs_in_stateless549 = frozenset([3])
    FOLLOW_receive_in_receives604 = frozenset([1, 61])
    FOLLOW_TREE_RECEIVE_in_receive649 = frozenset([2])
    FOLLOW_ID_in_receive663 = frozenset([3, 49, 63])
    FOLLOW_local_vars_in_receive697 = frozenset([3, 63])
    FOLLOW_statements_in_receive747 = frozenset([3])
    FOLLOW_proc_in_procs830 = frozenset([1, 59])
    FOLLOW_TREE_PROC_in_proc875 = frozenset([2])
    FOLLOW_ID_in_proc889 = frozenset([3, 49, 60, 63])
    FOLLOW_proc_args_in_proc923 = frozenset([3, 49, 63])
    FOLLOW_local_vars_in_proc973 = frozenset([3, 63])
    FOLLOW_statements_in_proc1023 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args1096 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args1098 = frozenset([3])
    FOLLOW_TREE_LOCAL_VARS_in_local_vars1143 = frozenset([2])
    FOLLOW_attrs_hints_in_local_vars1145 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements1200 = frozenset([2])
    FOLLOW_statement_in_statements1204 = frozenset([3, 64, 66, 69, 70, 71])
    FOLLOW_statement_call_in_statement1260 = frozenset([1])
    FOLLOW_statement_if_in_statement1284 = frozenset([1])
    FOLLOW_statement_assign_in_statement1308 = frozenset([1])
    FOLLOW_statement_with_in_statement1332 = frozenset([1])
    FOLLOW_statement_while_in_statement1356 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1399 = frozenset([2])
    FOLLOW_ID_in_statement_with1401 = frozenset([63])
    FOLLOW_statements_in_statement_with1403 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1454 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1470 = frozenset([18, 19, 23, 27, 65])
    FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1518 = frozenset([19])
    FOLLOW_ID_in_statement_assign1534 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1617 = frozenset([2])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1635 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_if1637 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1691 = frozenset([2])
    FOLLOW_statements_in_statement_if1693 = frozenset([3])
    FOLLOW_TREE_STATEMENT_WHILE_in_statement_while1768 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_while1770 = frozenset([3])
    FOLLOW_condition_any_in_conditional_ops1813 = frozenset([63])
    FOLLOW_statements_in_conditional_ops1815 = frozenset([1])
    FOLLOW_condition_all_in_conditional_ops1839 = frozenset([63])
    FOLLOW_statements_in_conditional_ops1841 = frozenset([1])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1894 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1910 = frozenset([3, 66])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1985 = frozenset([2])
    FOLLOW_statement_call_in_condition_all2001 = frozenset([3, 66])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call2066 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call2068 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args2123 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value2176 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2188 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2200 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2212 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts2253 = frozenset([2])
    FOLLOW_ID_in_consts2255 = frozenset([46, 54, 55])
    FOLLOW_consts_items_in_consts2257 = frozenset([3])
    FOLLOW_consts_item_in_consts_items2312 = frozenset([1, 46, 54, 55])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2367 = frozenset([2])
    FOLLOW_ID_in_consts_item2369 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2371 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2399 = frozenset([2])
    FOLLOW_ID_in_consts_item2401 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2403 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2431 = frozenset([2])
    FOLLOW_ID_in_consts_item2433 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2435 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2490 = frozenset([2])
    FOLLOW_ID_in_types2492 = frozenset([73])
    FOLLOW_types_items_in_types2494 = frozenset([3])
    FOLLOW_types_item_in_types_items2549 = frozenset([1, 73])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2604 = frozenset([2])
    FOLLOW_ID_in_types_item2606 = frozenset([39])
    FOLLOW_attrs_hints_in_types_item2608 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2663 = frozenset([2])
    FOLLOW_ID_in_messages2665 = frozenset([51])
    FOLLOW_messages_items_in_messages2667 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2722 = frozenset([1, 51])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2777 = frozenset([2])
    FOLLOW_ID_in_messages_item2779 = frozenset([39])
    FOLLOW_attrs_hints_in_messages_item2781 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars2826 = frozenset([2])
    FOLLOW_ID_in_vars2828 = frozenset([39])
    FOLLOW_attrs_hints_in_vars2830 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2883 = frozenset([1, 40])
    FOLLOW_attr_hint_in_attrs_hints2887 = frozenset([1, 40])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2932 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint2934 = frozenset([38])
    FOLLOW_TREE_ATTR_in_attr_hint2940 = frozenset([2])
    FOLLOW_ID_in_attr_hint2942 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2984 = frozenset([2])
    FOLLOW_hint_in_attr_hint2986 = frozenset([38])
    FOLLOW_TREE_ATTR_in_attr_hint2992 = frozenset([2])
    FOLLOW_ID_in_attr_hint2994 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3063 = frozenset([2])
    FOLLOW_ID_in_hint3065 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint3093 = frozenset([2])
    FOLLOW_ID_in_hint3095 = frozenset([19, 76])
    FOLLOW_hint_args_in_hint3097 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args3152 = frozenset([1, 19, 76])
    FOLLOW_ID_in_hint_arg3185 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg3197 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3228 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3230 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole3258 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3303 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3309 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3311 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3317 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract3349 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3351 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3357 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
