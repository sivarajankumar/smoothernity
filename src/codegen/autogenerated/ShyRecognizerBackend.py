# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-01 18:56:21

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
REPLACE=31
REPLY=32
REQUEST=33
STATELESS=34
STRING=35
TREE_ARBITRARY_TOKEN=36
TREE_ATTR=37
TREE_ATTRS_HINTS=38
TREE_ATTR_HINT=39
TREE_CONDITION_ALL=40
TREE_CONDITION_ANY=41
TREE_CONSTS=42
TREE_COPY=43
TREE_COPY_PASTE=44
TREE_EXPRESSION=45
TREE_HINT=46
TREE_HINT_NONE=47
TREE_MESSAGES=48
TREE_MESSAGES_ITEM=49
TREE_MODULE=50
TREE_MODULE_QUEUE=51
TREE_NUM_FRACT=52
TREE_NUM_WHOLE=53
TREE_PASTE=54
TREE_PASTE_REPLACE=55
TREE_PASTE_WITH=56
TREE_PROC=57
TREE_PROC_ARGS=58
TREE_PROC_VARS=59
TREE_STATELESS=60
TREE_STATEMENTS=61
TREE_STATEMENT_ASSIGN=62
TREE_STATEMENT_CALL=63
TREE_STATEMENT_ELIF=64
TREE_STATEMENT_ELSE=65
TREE_STATEMENT_IF=66
TREE_STATEMENT_WITH=67
TREE_TYPES=68
TREE_TYPES_ITEM=69
TREE_VARS=70
TYPES=71
UNDERSCORE=72
VARS=73
WHITESPACE=74
WITH=75

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "REPLY", "REQUEST", 
    "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", "TREE_ATTRS_HINTS", 
    "TREE_ATTR_HINT", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", "TREE_CONSTS", 
    "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", 
    "TREE_MESSAGES", "TREE_MESSAGES_ITEM", "TREE_MODULE", "TREE_MODULE_QUEUE", 
    "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", 
    "TREE_PASTE_WITH", "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", 
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_CALL", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WITH", 
    "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", "UNDERSCORE", 
    "VARS", "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:52:1: module returns [ title , content ] : ^( TREE_MODULE ID ( module_queue )? ( procs )? ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        ID7 = None
        module_queue8 = None

        procs9 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:54:5: ( ^( TREE_MODULE ID ( module_queue )? ( procs )? ) )
                # grammar/ShyRecognizerBackend.g:54:9: ^( TREE_MODULE ID ( module_queue )? ( procs )? )
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
                    retval.content [ 'procs' ] = procs9 
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
    # grammar/ShyRecognizerBackend.g:65:1: module_queue returns [ value ] : ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        value = None


        ID10 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:67:5: ( ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerBackend.g:67:9: ^( TREE_MODULE_QUEUE ID )
                pass 
                self.match(self.input, TREE_MODULE_QUEUE, self.FOLLOW_TREE_MODULE_QUEUE_in_module_queue430)

                self.match(self.input, DOWN, None)
                ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue432)

                self.match(self.input, UP, None)


                #action start
                value = ID10.text 
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
    # grammar/ShyRecognizerBackend.g:70:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID11 = None
        ID12 = None
        procs13 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:72:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_STATELESS) :
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
                    # grammar/ShyRecognizerBackend.g:72:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless465)

                    self.match(self.input, DOWN, None)
                    ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless467)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID11.text , dict ( ) 
                    #action end



                elif alt4 == 2:
                    # grammar/ShyRecognizerBackend.g:74:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless495)

                    self.match(self.input, DOWN, None)
                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless497)

                    self._state.following.append(self.FOLLOW_procs_in_stateless499)
                    procs13 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID12.text , procs13 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "procs"
    # grammar/ShyRecognizerBackend.g:78:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc14 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:81:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:81:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:81:9: ( proc )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == TREE_PROC) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/ShyRecognizerBackend.g:81:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs554)
                        proc14 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc14 is not None) and [proc14.title] or [None])[0] ] = ((proc14 is not None) and [proc14.content] or [None])[0] 
                        #action end



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1





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
    # grammar/ShyRecognizerBackend.g:84:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID15 = None
        proc_args16 = None

        proc_vars17 = None

        statements18 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:87:5: ( ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:87:9: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc599)

                self.match(self.input, DOWN, None)
                ID15 = self.match(self.input, ID, self.FOLLOW_ID_in_proc613)

                #action start
                retval.title = ID15.text 
                #action end


                # grammar/ShyRecognizerBackend.g:90:13: ( proc_args )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_PROC_ARGS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:90:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc647)
                    proc_args16 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args16 
                    #action end





                # grammar/ShyRecognizerBackend.g:93:13: ( proc_vars )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == TREE_PROC_VARS) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:93:15: proc_vars
                    pass 
                    self._state.following.append(self.FOLLOW_proc_vars_in_proc697)
                    proc_vars17 = self.proc_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = proc_vars17 
                    #action end





                # grammar/ShyRecognizerBackend.g:96:13: ( statements )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == TREE_STATEMENTS) :
                    alt8 = 1
                if alt8 == 1:
                    # grammar/ShyRecognizerBackend.g:96:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc747)
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

    # $ANTLR end "proc"



    # $ANTLR start "proc_args"
    # grammar/ShyRecognizerBackend.g:102:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints19 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:104:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:104:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args820)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args822)
                attrs_hints19 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints19 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "proc_vars"
    # grammar/ShyRecognizerBackend.g:108:1: proc_vars returns [ value ] : ^( TREE_PROC_VARS attrs_hints ) ;
    def proc_vars(self, ):
        value = None


        attrs_hints20 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:110:5: ( ^( TREE_PROC_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:110:9: ^( TREE_PROC_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_VARS, self.FOLLOW_TREE_PROC_VARS_in_proc_vars867)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_vars869)
                attrs_hints20 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints20 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:114:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement21 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:117:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:117:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements924)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:117:28: ( statement )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((TREE_STATEMENT_ASSIGN <= LA9_0 <= TREE_STATEMENT_CALL) or (TREE_STATEMENT_IF <= LA9_0 <= TREE_STATEMENT_WITH)) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerBackend.g:117:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements928)
                        statement21 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement21 ) 
                        #action end



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statements"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:122:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with );
    def statement(self, ):
        value = None


        statement_call22 = None

        statement_if23 = None

        statement_assign24 = None

        statement_with25 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:124:5: ( statement_call | statement_if | statement_assign | statement_with )
                alt10 = 4
                LA10 = self.input.LA(1)
                if LA10 == TREE_STATEMENT_CALL:
                    alt10 = 1
                elif LA10 == TREE_STATEMENT_IF:
                    alt10 = 2
                elif LA10 == TREE_STATEMENT_ASSIGN:
                    alt10 = 3
                elif LA10 == TREE_STATEMENT_WITH:
                    alt10 = 4
                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # grammar/ShyRecognizerBackend.g:124:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement984)
                    statement_call22 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call22 
                    #action end



                elif alt10 == 2:
                    # grammar/ShyRecognizerBackend.g:126:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement1008)
                    statement_if23 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if23 
                    #action end



                elif alt10 == 3:
                    # grammar/ShyRecognizerBackend.g:128:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1032)
                    statement_assign24 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign24 
                    #action end



                elif alt10 == 4:
                    # grammar/ShyRecognizerBackend.g:130:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1056)
                    statement_with25 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with25 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:134:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID26 = None
        statements27 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:136:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:136:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1099)

                self.match(self.input, DOWN, None)
                ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1101)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1103)
                statements27 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID26.text : statements27 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:140:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID29 = None
        arbitrary_value28 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:142:5: ( ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:142:9: ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1144)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1146)
                arbitrary_value28 = self.arbitrary_value()

                self._state.following.pop()

                #action start
                value = { 'assign' : [ arbitrary_value28 , list ( ) ] } 
                #action end


                # grammar/ShyRecognizerBackend.g:144:13: ( ID )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ID) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:144:15: ID
                        pass 
                        ID29 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1176)

                        #action start
                        value [ 'assign' ] [ - 1 ] . append ( ID29.text ) 
                        #action end



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:150:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) ;
    def statement_if(self, ):
        value = None


        statement_elif30 = None

        statement_else31 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:153:5: ( ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) )
                # grammar/ShyRecognizerBackend.g:153:9: ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1259)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:154:13: ( statement_elif )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == TREE_STATEMENT_ELIF) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerBackend.g:154:15: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1275)
                        statement_elif30 = self.statement_elif()

                        self._state.following.pop()

                        #action start
                        value [ 'if' ] . append ( statement_elif30 ) 
                        #action end



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1


                # grammar/ShyRecognizerBackend.g:157:13: ( statement_else )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == TREE_STATEMENT_ELSE) :
                    alt13 = 1
                if alt13 == 1:
                    # grammar/ShyRecognizerBackend.g:157:15: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1325)
                    statement_else31 = self.statement_else()

                    self._state.following.pop()

                    #action start
                    value [ 'else' ] = statement_else31 
                    #action end





                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_if"



    # $ANTLR start "statement_elif"
    # grammar/ShyRecognizerBackend.g:163:1: statement_elif returns [ value ] : ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) );
    def statement_elif(self, ):
        value = None


        condition_any32 = None

        statements33 = None

        condition_all34 = None

        statements35 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:165:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == TREE_STATEMENT_ELIF) :
                    LA14_1 = self.input.LA(2)

                    if (LA14_1 == 2) :
                        LA14_2 = self.input.LA(3)

                        if (LA14_2 == TREE_CONDITION_ANY) :
                            alt14 = 1
                        elif (LA14_2 == TREE_CONDITION_ALL) :
                            alt14 = 2
                        else:
                            nvae = NoViableAltException("", 14, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyRecognizerBackend.g:165:9: ^( TREE_STATEMENT_ELIF condition_any statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1398)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_any_in_statement_elif1400)
                    condition_any32 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1402)
                    statements33 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'any' : condition_any32 ,
                       'ops' : statements33 }
                                
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:170:9: ^( TREE_STATEMENT_ELIF condition_all statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1430)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_all_in_statement_elif1432)
                    condition_all34 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1434)
                    statements35 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'all' : condition_all34 ,
                       'ops' : statements35 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerBackend.g:177:1: statement_else returns [ value ] : ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        value = None


        statements36 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:179:5: ( ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerBackend.g:179:9: ^( TREE_STATEMENT_ELSE statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1479)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statements_in_statement_else1481)
                statements36 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = statements36 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_else"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:183:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call37 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:186:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:186:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1536)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:187:13: ( statement_call )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == TREE_STATEMENT_CALL) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:187:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1552)
                        statement_call37 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call37 ) 
                        #action end



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:192:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call38 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:195:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:195:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1627)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:196:13: ( statement_call )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == TREE_STATEMENT_CALL) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:196:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all1643)
                        statement_call38 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call38 ) 
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

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:201:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args39 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:203:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:203:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1708)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1710)
                    statement_call_args39 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args39 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:207:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value40 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:210:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:210:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:210:9: ( arbitrary_value )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA17_0 <= ID) or LA17_0 == MINUS or LA17_0 == NUMBER) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:210:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1765)
                        arbitrary_value40 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value40 ) 
                        #action end



                    else:
                        break #loop17





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:215:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID41 = None
        EXPRESSION42 = None
        num_whole43 = None

        num_fract44 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:217:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt18 = 4
                LA18 = self.input.LA(1)
                if LA18 == ID:
                    alt18 = 1
                elif LA18 == EXPRESSION:
                    alt18 = 2
                elif LA18 == MINUS:
                    LA18_3 = self.input.LA(2)

                    if (LA18_3 == NUMBER) :
                        LA18_5 = self.input.LA(3)

                        if (LA18_5 == DIVIDE) :
                            alt18 = 4
                        elif (LA18_5 == 3 or (EXPRESSION <= LA18_5 <= ID) or LA18_5 == MINUS or LA18_5 == NUMBER) :
                            alt18 = 3
                        else:
                            nvae = NoViableAltException("", 18, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 18, 3, self.input)

                        raise nvae


                elif LA18 == NUMBER:
                    LA18_4 = self.input.LA(2)

                    if (LA18_4 == DIVIDE) :
                        alt18 = 4
                    elif (LA18_4 == 3 or (EXPRESSION <= LA18_4 <= ID) or LA18_4 == MINUS or LA18_4 == NUMBER) :
                        alt18 = 3
                    else:
                        nvae = NoViableAltException("", 18, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerBackend.g:217:9: ID
                    pass 
                    ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1818)

                    #action start
                    value = ID41.text 
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:218:9: EXPRESSION
                    pass 
                    EXPRESSION42 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1830)

                    #action start
                    value = EXPRESSION42.text 
                    #action end



                elif alt18 == 3:
                    # grammar/ShyRecognizerBackend.g:219:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1842)
                    num_whole43 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole43 
                    #action end



                elif alt18 == 4:
                    # grammar/ShyRecognizerBackend.g:220:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1854)
                    num_fract44 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract44 
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
    # grammar/ShyRecognizerBackend.g:223:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID45 = None
        consts_items46 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:226:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:226:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1895)

                self.match(self.input, DOWN, None)
                ID45 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1897)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1899)
                consts_items46 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID45.text , consts_items46 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:230:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item47 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:233:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:233:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:233:9: ( consts_item )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA19_0 <= TREE_NUM_WHOLE)) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerBackend.g:233:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1954)
                        consts_item47 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item47 is not None) and [consts_item47.name] or [None])[0] ] = ((consts_item47 is not None) and [consts_item47.value] or [None])[0] 
                        #action end



                    else:
                        if cnt19 >= 1:
                            break #loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1





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
    # grammar/ShyRecognizerBackend.g:238:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID48 = None
        ID50 = None
        ID52 = None
        EXPRESSION53 = None
        num_whole49 = None

        num_fract51 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:240:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt20 = 3
                LA20 = self.input.LA(1)
                if LA20 == TREE_NUM_WHOLE:
                    alt20 = 1
                elif LA20 == TREE_NUM_FRACT:
                    alt20 = 2
                elif LA20 == TREE_EXPRESSION:
                    alt20 = 3
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammar/ShyRecognizerBackend.g:240:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2009)

                    self.match(self.input, DOWN, None)
                    ID48 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2011)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2013)
                    num_whole49 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID48.text , num_whole49 
                    #action end



                elif alt20 == 2:
                    # grammar/ShyRecognizerBackend.g:242:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2041)

                    self.match(self.input, DOWN, None)
                    ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2043)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2045)
                    num_fract51 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID50.text , num_fract51 
                    #action end



                elif alt20 == 3:
                    # grammar/ShyRecognizerBackend.g:244:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2073)

                    self.match(self.input, DOWN, None)
                    ID52 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2075)

                    EXPRESSION53 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2077)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID52.text , EXPRESSION53.text 
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
    # grammar/ShyRecognizerBackend.g:248:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID54 = None
        types_items55 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:251:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:251:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2132)

                self.match(self.input, DOWN, None)
                ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_types2134)

                self._state.following.append(self.FOLLOW_types_items_in_types2136)
                types_items55 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID54.text , types_items55 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:255:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item56 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:258:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:258:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:258:9: ( types_item )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_TYPES_ITEM) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:258:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2191)
                        types_item56 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item56 is not None) and [types_item56.name] or [None])[0] ] = ((types_item56 is not None) and [types_item56.value] or [None])[0] 
                        #action end



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1





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
    # grammar/ShyRecognizerBackend.g:263:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID57 = None
        attrs_hints58 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:265:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:265:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2246)

                self.match(self.input, DOWN, None)
                ID57 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2248)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2250)
                attrs_hints58 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID57.text , attrs_hints58 
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
    # grammar/ShyRecognizerBackend.g:269:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID59 = None
        messages_items60 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:272:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:272:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2305)

                self.match(self.input, DOWN, None)
                ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2307)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2309)
                messages_items60 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID59.text , messages_items60 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:276:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item61 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:279:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:279:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:279:9: ( messages_item )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == TREE_MESSAGES_ITEM) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:279:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2364)
                        messages_item61 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item61 is not None) and [messages_item61.name] or [None])[0] ] = ((messages_item61 is not None) and [messages_item61.value] or [None])[0] 
                        #action end



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1





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
    # grammar/ShyRecognizerBackend.g:284:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID62 = None
        attrs_hints63 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:286:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:286:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2419)

                self.match(self.input, DOWN, None)
                ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2421)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2423)
                attrs_hints63 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID62.text , attrs_hints63 
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
    # grammar/ShyRecognizerBackend.g:290:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID64 = None
        attrs_hints65 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:292:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:292:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars2468)

                self.match(self.input, DOWN, None)
                ID64 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2470)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2472)
                attrs_hints65 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID64.text , attrs_hints65 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:296:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint66 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:299:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:299:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2525)

                # grammar/ShyRecognizerBackend.g:299:26: ( attr_hint )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == TREE_ATTR_HINT) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerBackend.g:299:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2529)
                        attr_hint66 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint66 ) 
                        #action end



                    else:
                        break #loop23





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:302:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID67 = None
        ID68 = None
        hint69 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:305:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == TREE_ATTR_HINT) :
                    LA26_1 = self.input.LA(2)

                    if (LA26_1 == 2) :
                        LA26_2 = self.input.LA(3)

                        if (LA26_2 == TREE_HINT_NONE) :
                            alt26 = 1
                        elif (LA26_2 == TREE_HINT) :
                            alt26 = 2
                        else:
                            nvae = NoViableAltException("", 26, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 26, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # grammar/ShyRecognizerBackend.g:305:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2574)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint2576)

                    # grammar/ShyRecognizerBackend.g:305:42: ( ^( TREE_ATTR ID ) )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == TREE_ATTR) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerBackend.g:305:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2582)

                            self.match(self.input, DOWN, None)
                            ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2584)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID67.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    self.match(self.input, UP, None)



                elif alt26 == 2:
                    # grammar/ShyRecognizerBackend.g:308:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2626)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2628)
                    hint69 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:308:32: ( ^( TREE_ATTR ID ) )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == TREE_ATTR) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerBackend.g:308:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2634)

                            self.match(self.input, DOWN, None)
                            ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2636)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID68.text ] = hint69 
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

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:313:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID70 = None
        ID71 = None
        hint_args72 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:316:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == TREE_HINT) :
                    LA27_1 = self.input.LA(2)

                    if (LA27_1 == 2) :
                        LA27_2 = self.input.LA(3)

                        if (LA27_2 == ID) :
                            LA27_3 = self.input.LA(4)

                            if (LA27_3 == 3) :
                                alt27 = 1
                            elif (LA27_3 == ID or LA27_3 == UNDERSCORE) :
                                alt27 = 2
                            else:
                                nvae = NoViableAltException("", 27, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 27, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 27, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammar/ShyRecognizerBackend.g:316:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2705)

                    self.match(self.input, DOWN, None)
                    ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2707)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID70.text ] = list ( ) 
                    #action end



                elif alt27 == 2:
                    # grammar/ShyRecognizerBackend.g:318:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2735)

                    self.match(self.input, DOWN, None)
                    ID71 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2737)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2739)
                    hint_args72 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID71.text ] = hint_args72 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:322:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg73 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:325:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:325:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:325:9: ( hint_arg )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == ID or LA28_0 == UNDERSCORE) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerBackend.g:325:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2794)
                        hint_arg73 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg73 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:328:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID74 = None
        UNDERSCORE75 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:330:5: ( ID | UNDERSCORE )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == ID) :
                    alt29 = 1
                elif (LA29_0 == UNDERSCORE) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # grammar/ShyRecognizerBackend.g:330:9: ID
                    pass 
                    ID74 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2827)

                    #action start
                    value = ID74.text 
                    #action end



                elif alt29 == 2:
                    # grammar/ShyRecognizerBackend.g:331:9: UNDERSCORE
                    pass 
                    UNDERSCORE75 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2839)

                    #action start
                    value = UNDERSCORE75.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:334:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS76 = None
        NUMBER77 = None
        NUMBER78 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:336:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == MINUS) :
                    alt30 = 1
                elif (LA30_0 == NUMBER) :
                    alt30 = 2
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae


                if alt30 == 1:
                    # grammar/ShyRecognizerBackend.g:336:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:336:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:336:11: MINUS NUMBER
                    pass 
                    MINUS76 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2870)

                    NUMBER77 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2872)




                    #action start
                    value = int ( MINUS76.text + NUMBER77.text ) 
                    #action end



                elif alt30 == 2:
                    # grammar/ShyRecognizerBackend.g:338:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:338:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:338:11: NUMBER
                    pass 
                    NUMBER78 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2900)




                    #action start
                    value = int ( NUMBER78.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:342:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS79 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:344:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == MINUS) :
                    alt31 = 1
                elif (LA31_0 == NUMBER) :
                    alt31 = 2
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae


                if alt31 == 1:
                    # grammar/ShyRecognizerBackend.g:344:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:344:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:344:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS79 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2945)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2951)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2953)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2959)




                    #action start
                                
                    value = Fraction ( int ( MINUS79.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt31 == 2:
                    # grammar/ShyRecognizerBackend.g:349:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:349:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:349:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2991)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2993)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2999)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 42, 48, 50, 60, 68, 70])
    FOLLOW_stateless_in_start114 = frozenset([1, 42, 48, 50, 60, 68, 70])
    FOLLOW_consts_in_start141 = frozenset([1, 42, 48, 50, 60, 68, 70])
    FOLLOW_types_in_start167 = frozenset([1, 42, 48, 50, 60, 68, 70])
    FOLLOW_messages_in_start193 = frozenset([1, 42, 48, 50, 60, 68, 70])
    FOLLOW_vars_in_start219 = frozenset([1, 42, 48, 50, 60, 68, 70])
    FOLLOW_TREE_MODULE_in_module274 = frozenset([2])
    FOLLOW_ID_in_module276 = frozenset([3, 51, 57])
    FOLLOW_module_queue_in_module306 = frozenset([3, 57])
    FOLLOW_procs_in_module357 = frozenset([3])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue430 = frozenset([2])
    FOLLOW_ID_in_module_queue432 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless465 = frozenset([2])
    FOLLOW_ID_in_stateless467 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless495 = frozenset([2])
    FOLLOW_ID_in_stateless497 = frozenset([57])
    FOLLOW_procs_in_stateless499 = frozenset([3])
    FOLLOW_proc_in_procs554 = frozenset([1, 57])
    FOLLOW_TREE_PROC_in_proc599 = frozenset([2])
    FOLLOW_ID_in_proc613 = frozenset([3, 58, 59, 61])
    FOLLOW_proc_args_in_proc647 = frozenset([3, 59, 61])
    FOLLOW_proc_vars_in_proc697 = frozenset([3, 61])
    FOLLOW_statements_in_proc747 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args820 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args822 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars867 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_vars869 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements924 = frozenset([2])
    FOLLOW_statement_in_statements928 = frozenset([3, 62, 63, 66, 67])
    FOLLOW_statement_call_in_statement984 = frozenset([1])
    FOLLOW_statement_if_in_statement1008 = frozenset([1])
    FOLLOW_statement_assign_in_statement1032 = frozenset([1])
    FOLLOW_statement_with_in_statement1056 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1099 = frozenset([2])
    FOLLOW_ID_in_statement_with1101 = frozenset([61])
    FOLLOW_statements_in_statement_with1103 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1144 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1146 = frozenset([19])
    FOLLOW_ID_in_statement_assign1176 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1259 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if1275 = frozenset([3, 64, 65])
    FOLLOW_statement_else_in_statement_if1325 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1398 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif1400 = frozenset([61])
    FOLLOW_statements_in_statement_elif1402 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1430 = frozenset([2])
    FOLLOW_condition_all_in_statement_elif1432 = frozenset([61])
    FOLLOW_statements_in_statement_elif1434 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1479 = frozenset([2])
    FOLLOW_statements_in_statement_else1481 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1536 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1552 = frozenset([3, 63])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1627 = frozenset([2])
    FOLLOW_statement_call_in_condition_all1643 = frozenset([3, 63])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1708 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call1710 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args1765 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value1818 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1830 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1842 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1854 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1895 = frozenset([2])
    FOLLOW_ID_in_consts1897 = frozenset([45, 52, 53])
    FOLLOW_consts_items_in_consts1899 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1954 = frozenset([1, 45, 52, 53])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2009 = frozenset([2])
    FOLLOW_ID_in_consts_item2011 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2013 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2041 = frozenset([2])
    FOLLOW_ID_in_consts_item2043 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2045 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2073 = frozenset([2])
    FOLLOW_ID_in_consts_item2075 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2077 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2132 = frozenset([2])
    FOLLOW_ID_in_types2134 = frozenset([69])
    FOLLOW_types_items_in_types2136 = frozenset([3])
    FOLLOW_types_item_in_types_items2191 = frozenset([1, 69])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2246 = frozenset([2])
    FOLLOW_ID_in_types_item2248 = frozenset([38])
    FOLLOW_attrs_hints_in_types_item2250 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2305 = frozenset([2])
    FOLLOW_ID_in_messages2307 = frozenset([49])
    FOLLOW_messages_items_in_messages2309 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2364 = frozenset([1, 49])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2419 = frozenset([2])
    FOLLOW_ID_in_messages_item2421 = frozenset([38])
    FOLLOW_attrs_hints_in_messages_item2423 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars2468 = frozenset([2])
    FOLLOW_ID_in_vars2470 = frozenset([38])
    FOLLOW_attrs_hints_in_vars2472 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2525 = frozenset([1, 39])
    FOLLOW_attr_hint_in_attrs_hints2529 = frozenset([1, 39])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2574 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint2576 = frozenset([37])
    FOLLOW_TREE_ATTR_in_attr_hint2582 = frozenset([2])
    FOLLOW_ID_in_attr_hint2584 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2626 = frozenset([2])
    FOLLOW_hint_in_attr_hint2628 = frozenset([37])
    FOLLOW_TREE_ATTR_in_attr_hint2634 = frozenset([2])
    FOLLOW_ID_in_attr_hint2636 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2705 = frozenset([2])
    FOLLOW_ID_in_hint2707 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2735 = frozenset([2])
    FOLLOW_ID_in_hint2737 = frozenset([19, 72])
    FOLLOW_hint_args_in_hint2739 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2794 = frozenset([1, 19, 72])
    FOLLOW_ID_in_hint_arg2827 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2839 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2870 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2872 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2900 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2945 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2951 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2953 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2959 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2991 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2993 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2999 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
