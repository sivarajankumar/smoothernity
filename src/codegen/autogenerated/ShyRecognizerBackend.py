# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-02-01 19:43:04

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
TREE_STATEMENT_ASSIGN_TO=63
TREE_STATEMENT_CALL=64
TREE_STATEMENT_ELIF=65
TREE_STATEMENT_ELSE=66
TREE_STATEMENT_IF=67
TREE_STATEMENT_WHILE=68
TREE_STATEMENT_WITH=69
TREE_TYPES=70
TREE_TYPES_ITEM=71
TREE_VARS=72
TYPES=73
UNDERSCORE=74
VARS=75
WHILE=76
WHITESPACE=77
WITH=78

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
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", 
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

                    if (LA9_0 == TREE_STATEMENT_ASSIGN or LA9_0 == TREE_STATEMENT_CALL or (TREE_STATEMENT_IF <= LA9_0 <= TREE_STATEMENT_WITH)) :
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
    # grammar/ShyRecognizerBackend.g:122:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with | statement_while );
    def statement(self, ):
        value = None


        statement_call22 = None

        statement_if23 = None

        statement_assign24 = None

        statement_with25 = None

        statement_while26 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:124:5: ( statement_call | statement_if | statement_assign | statement_with | statement_while )
                alt10 = 5
                LA10 = self.input.LA(1)
                if LA10 == TREE_STATEMENT_CALL:
                    alt10 = 1
                elif LA10 == TREE_STATEMENT_IF:
                    alt10 = 2
                elif LA10 == TREE_STATEMENT_ASSIGN:
                    alt10 = 3
                elif LA10 == TREE_STATEMENT_WITH:
                    alt10 = 4
                elif LA10 == TREE_STATEMENT_WHILE:
                    alt10 = 5
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



                elif alt10 == 5:
                    # grammar/ShyRecognizerBackend.g:132:9: statement_while
                    pass 
                    self._state.following.append(self.FOLLOW_statement_while_in_statement1080)
                    statement_while26 = self.statement_while()

                    self._state.following.pop()

                    #action start
                    value = statement_while26 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:136:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID27 = None
        statements28 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:138:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:138:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1123)

                self.match(self.input, DOWN, None)
                ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1125)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1127)
                statements28 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID27.text : statements28 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:142:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID30 = None
        arbitrary_value29 = None


        value = { 'assign' : { 'from' : list ( ) , 'to' : list ( ) } } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:145:5: ( ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:145:9: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1178)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:146:13: ( arbitrary_value )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA11_0 <= ID) or LA11_0 == MINUS or LA11_0 == NUMBER) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:146:15: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1194)
                        arbitrary_value29 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                                        
                        value [ 'assign' ] [ 'from' ] . append (
                            arbitrary_value29 )
                                        
                        #action end



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1


                self.match(self.input, TREE_STATEMENT_ASSIGN_TO, self.FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1242)

                # grammar/ShyRecognizerBackend.g:153:13: ( ID )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == ID) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerBackend.g:153:15: ID
                        pass 
                        ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1258)

                        #action start
                                        
                        value [ 'assign' ] [ 'to' ] . append (
                            ID30.text )
                                        
                        #action end



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:162:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) ;
    def statement_if(self, ):
        value = None


        conditional_ops31 = None

        statements32 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:165:5: ( ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? ) )
                # grammar/ShyRecognizerBackend.g:165:9: ^( TREE_STATEMENT_IF ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+ ( ^( TREE_STATEMENT_ELSE statements ) )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1341)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:166:13: ( ^( TREE_STATEMENT_ELIF conditional_ops ) )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_STATEMENT_ELIF) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:166:15: ^( TREE_STATEMENT_ELIF conditional_ops )
                        pass 
                        self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1359)

                        self.match(self.input, DOWN, None)
                        self._state.following.append(self.FOLLOW_conditional_ops_in_statement_if1361)
                        conditional_ops31 = self.conditional_ops()

                        self._state.following.pop()

                        self.match(self.input, UP, None)


                        #action start
                        value [ 'if' ] . append ( conditional_ops31 ) 
                        #action end



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                # grammar/ShyRecognizerBackend.g:169:13: ( ^( TREE_STATEMENT_ELSE statements ) )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == TREE_STATEMENT_ELSE) :
                    alt14 = 1
                if alt14 == 1:
                    # grammar/ShyRecognizerBackend.g:169:15: ^( TREE_STATEMENT_ELSE statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1415)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statements_in_statement_if1417)
                    statements32 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ 'else' ] = statements32 
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
    # grammar/ShyRecognizerBackend.g:175:1: statement_while returns [ value ] : ^( TREE_STATEMENT_WHILE conditional_ops ) ;
    def statement_while(self, ):
        value = None


        conditional_ops33 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:177:5: ( ^( TREE_STATEMENT_WHILE conditional_ops ) )
                # grammar/ShyRecognizerBackend.g:177:9: ^( TREE_STATEMENT_WHILE conditional_ops )
                pass 
                self.match(self.input, TREE_STATEMENT_WHILE, self.FOLLOW_TREE_STATEMENT_WHILE_in_statement_while1492)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_conditional_ops_in_statement_while1494)
                conditional_ops33 = self.conditional_ops()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'while' : conditional_ops33 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_while"



    # $ANTLR start "conditional_ops"
    # grammar/ShyRecognizerBackend.g:181:1: conditional_ops returns [ value ] : ( condition_any statements | condition_all statements );
    def conditional_ops(self, ):
        value = None


        condition_any34 = None

        statements35 = None

        condition_all36 = None

        statements37 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:183:5: ( condition_any statements | condition_all statements )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == TREE_CONDITION_ANY) :
                    alt15 = 1
                elif (LA15_0 == TREE_CONDITION_ALL) :
                    alt15 = 2
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:183:9: condition_any statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_any_in_conditional_ops1537)
                    condition_any34 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops1539)
                    statements35 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'any' : condition_any34 ,
                       'ops' : statements35 }
                                
                    #action end



                elif alt15 == 2:
                    # grammar/ShyRecognizerBackend.g:188:9: condition_all statements
                    pass 
                    self._state.following.append(self.FOLLOW_condition_all_in_conditional_ops1563)
                    condition_all36 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_conditional_ops1565)
                    statements37 = self.statements()

                    self._state.following.pop()

                    #action start
                    value = {
                       'all' : condition_all36 ,
                       'ops' : statements37 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "conditional_ops"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:195:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call38 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:198:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:198:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1618)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:199:13: ( statement_call )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == TREE_STATEMENT_CALL) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:199:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1634)
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

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:204:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call39 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:207:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:207:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1709)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:208:13: ( statement_call )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_STATEMENT_CALL) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:208:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all1725)
                        statement_call39 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call39 ) 
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

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:213:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args40 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:215:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:215:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1790)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1792)
                    statement_call_args40 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args40 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:219:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value41 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:222:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:222:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:222:9: ( arbitrary_value )*
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA18_0 <= ID) or LA18_0 == MINUS or LA18_0 == NUMBER) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerBackend.g:222:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1847)
                        arbitrary_value41 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value41 ) 
                        #action end



                    else:
                        break #loop18





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:227:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID42 = None
        EXPRESSION43 = None
        num_whole44 = None

        num_fract45 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:229:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt19 = 4
                LA19 = self.input.LA(1)
                if LA19 == ID:
                    alt19 = 1
                elif LA19 == EXPRESSION:
                    alt19 = 2
                elif LA19 == MINUS:
                    LA19_3 = self.input.LA(2)

                    if (LA19_3 == NUMBER) :
                        LA19_5 = self.input.LA(3)

                        if (LA19_5 == DIVIDE) :
                            alt19 = 4
                        elif (LA19_5 == 3 or (EXPRESSION <= LA19_5 <= ID) or LA19_5 == MINUS or LA19_5 == NUMBER or LA19_5 == TREE_STATEMENT_ASSIGN_TO) :
                            alt19 = 3
                        else:
                            nvae = NoViableAltException("", 19, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 19, 3, self.input)

                        raise nvae


                elif LA19 == NUMBER:
                    LA19_4 = self.input.LA(2)

                    if (LA19_4 == DIVIDE) :
                        alt19 = 4
                    elif (LA19_4 == 3 or (EXPRESSION <= LA19_4 <= ID) or LA19_4 == MINUS or LA19_4 == NUMBER or LA19_4 == TREE_STATEMENT_ASSIGN_TO) :
                        alt19 = 3
                    else:
                        nvae = NoViableAltException("", 19, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:229:9: ID
                    pass 
                    ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1900)

                    #action start
                    value = ID42.text 
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:230:9: EXPRESSION
                    pass 
                    EXPRESSION43 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1912)

                    #action start
                    value = EXPRESSION43.text 
                    #action end



                elif alt19 == 3:
                    # grammar/ShyRecognizerBackend.g:231:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1924)
                    num_whole44 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole44 
                    #action end



                elif alt19 == 4:
                    # grammar/ShyRecognizerBackend.g:232:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1936)
                    num_fract45 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract45 
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
    # grammar/ShyRecognizerBackend.g:235:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID46 = None
        consts_items47 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:238:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:238:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1977)

                self.match(self.input, DOWN, None)
                ID46 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1979)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1981)
                consts_items47 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID46.text , consts_items47 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:242:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item48 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:245:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:245:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:245:9: ( consts_item )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA20_0 <= TREE_NUM_WHOLE)) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:245:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2036)
                        consts_item48 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item48 is not None) and [consts_item48.name] or [None])[0] ] = ((consts_item48 is not None) and [consts_item48.value] or [None])[0] 
                        #action end



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1





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
    # grammar/ShyRecognizerBackend.g:250:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID49 = None
        ID51 = None
        ID53 = None
        EXPRESSION54 = None
        num_whole50 = None

        num_fract52 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:252:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt21 = 3
                LA21 = self.input.LA(1)
                if LA21 == TREE_NUM_WHOLE:
                    alt21 = 1
                elif LA21 == TREE_NUM_FRACT:
                    alt21 = 2
                elif LA21 == TREE_EXPRESSION:
                    alt21 = 3
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae


                if alt21 == 1:
                    # grammar/ShyRecognizerBackend.g:252:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item2091)

                    self.match(self.input, DOWN, None)
                    ID49 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2093)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2095)
                    num_whole50 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID49.text , num_whole50 
                    #action end



                elif alt21 == 2:
                    # grammar/ShyRecognizerBackend.g:254:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item2123)

                    self.match(self.input, DOWN, None)
                    ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2125)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2127)
                    num_fract52 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID51.text , num_fract52 
                    #action end



                elif alt21 == 3:
                    # grammar/ShyRecognizerBackend.g:256:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2155)

                    self.match(self.input, DOWN, None)
                    ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2157)

                    EXPRESSION54 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2159)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID53.text , EXPRESSION54.text 
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
    # grammar/ShyRecognizerBackend.g:260:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID55 = None
        types_items56 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:263:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:263:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2214)

                self.match(self.input, DOWN, None)
                ID55 = self.match(self.input, ID, self.FOLLOW_ID_in_types2216)

                self._state.following.append(self.FOLLOW_types_items_in_types2218)
                types_items56 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID55.text , types_items56 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:267:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item57 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:270:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:270:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:270:9: ( types_item )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == TREE_TYPES_ITEM) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:270:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2273)
                        types_item57 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item57 is not None) and [types_item57.name] or [None])[0] ] = ((types_item57 is not None) and [types_item57.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:275:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID58 = None
        attrs_hints59 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:277:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:277:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2328)

                self.match(self.input, DOWN, None)
                ID58 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2330)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2332)
                attrs_hints59 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID58.text , attrs_hints59 
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
    # grammar/ShyRecognizerBackend.g:281:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID60 = None
        messages_items61 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:284:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:284:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2387)

                self.match(self.input, DOWN, None)
                ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2389)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2391)
                messages_items61 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID60.text , messages_items61 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:288:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item62 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:291:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:291:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:291:9: ( messages_item )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == TREE_MESSAGES_ITEM) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerBackend.g:291:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2446)
                        messages_item62 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item62 is not None) and [messages_item62.name] or [None])[0] ] = ((messages_item62 is not None) and [messages_item62.value] or [None])[0] 
                        #action end



                    else:
                        if cnt23 >= 1:
                            break #loop23

                        eee = EarlyExitException(23, self.input)
                        raise eee

                    cnt23 += 1





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
    # grammar/ShyRecognizerBackend.g:296:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID63 = None
        attrs_hints64 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:298:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:298:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2501)

                self.match(self.input, DOWN, None)
                ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2503)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2505)
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

    # $ANTLR end "messages_item"


    class vars_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.vars_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "vars"
    # grammar/ShyRecognizerBackend.g:302:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID65 = None
        attrs_hints66 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:304:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:304:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars2550)

                self.match(self.input, DOWN, None)
                ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2552)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2554)
                attrs_hints66 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID65.text , attrs_hints66 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:308:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint67 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:311:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:311:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2607)

                # grammar/ShyRecognizerBackend.g:311:26: ( attr_hint )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == TREE_ATTR_HINT) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerBackend.g:311:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2611)
                        attr_hint67 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint67 ) 
                        #action end



                    else:
                        break #loop24





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:314:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID68 = None
        ID69 = None
        hint70 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:317:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == TREE_ATTR_HINT) :
                    LA27_1 = self.input.LA(2)

                    if (LA27_1 == 2) :
                        LA27_2 = self.input.LA(3)

                        if (LA27_2 == TREE_HINT_NONE) :
                            alt27 = 1
                        elif (LA27_2 == TREE_HINT) :
                            alt27 = 2
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
                    # grammar/ShyRecognizerBackend.g:317:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2656)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint2658)

                    # grammar/ShyRecognizerBackend.g:317:42: ( ^( TREE_ATTR ID ) )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == TREE_ATTR) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerBackend.g:317:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2664)

                            self.match(self.input, DOWN, None)
                            ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2666)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID68.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    self.match(self.input, UP, None)



                elif alt27 == 2:
                    # grammar/ShyRecognizerBackend.g:320:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2708)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2710)
                    hint70 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:320:32: ( ^( TREE_ATTR ID ) )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == TREE_ATTR) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerBackend.g:320:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2716)

                            self.match(self.input, DOWN, None)
                            ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2718)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID69.text ] = hint70 
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

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:325:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID71 = None
        ID72 = None
        hint_args73 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:328:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == TREE_HINT) :
                    LA28_1 = self.input.LA(2)

                    if (LA28_1 == 2) :
                        LA28_2 = self.input.LA(3)

                        if (LA28_2 == ID) :
                            LA28_3 = self.input.LA(4)

                            if (LA28_3 == 3) :
                                alt28 = 1
                            elif (LA28_3 == ID or LA28_3 == UNDERSCORE) :
                                alt28 = 2
                            else:
                                nvae = NoViableAltException("", 28, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 28, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 28, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # grammar/ShyRecognizerBackend.g:328:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2787)

                    self.match(self.input, DOWN, None)
                    ID71 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2789)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID71.text ] = list ( ) 
                    #action end



                elif alt28 == 2:
                    # grammar/ShyRecognizerBackend.g:330:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2817)

                    self.match(self.input, DOWN, None)
                    ID72 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2819)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2821)
                    hint_args73 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID72.text ] = hint_args73 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:334:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg74 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:337:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:337:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:337:9: ( hint_arg )+
                cnt29 = 0
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == ID or LA29_0 == UNDERSCORE) :
                        alt29 = 1


                    if alt29 == 1:
                        # grammar/ShyRecognizerBackend.g:337:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2876)
                        hint_arg74 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg74 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:340:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID75 = None
        UNDERSCORE76 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:342:5: ( ID | UNDERSCORE )
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == ID) :
                    alt30 = 1
                elif (LA30_0 == UNDERSCORE) :
                    alt30 = 2
                else:
                    nvae = NoViableAltException("", 30, 0, self.input)

                    raise nvae


                if alt30 == 1:
                    # grammar/ShyRecognizerBackend.g:342:9: ID
                    pass 
                    ID75 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2909)

                    #action start
                    value = ID75.text 
                    #action end



                elif alt30 == 2:
                    # grammar/ShyRecognizerBackend.g:343:9: UNDERSCORE
                    pass 
                    UNDERSCORE76 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2921)

                    #action start
                    value = UNDERSCORE76.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:346:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS77 = None
        NUMBER78 = None
        NUMBER79 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:348:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:348:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:348:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:348:11: MINUS NUMBER
                    pass 
                    MINUS77 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2952)

                    NUMBER78 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2954)




                    #action start
                    value = int ( MINUS77.text + NUMBER78.text ) 
                    #action end



                elif alt31 == 2:
                    # grammar/ShyRecognizerBackend.g:350:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:350:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:350:11: NUMBER
                    pass 
                    NUMBER79 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2982)




                    #action start
                    value = int ( NUMBER79.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:354:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS80 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:356:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == MINUS) :
                    alt32 = 1
                elif (LA32_0 == NUMBER) :
                    alt32 = 2
                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # grammar/ShyRecognizerBackend.g:356:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:356:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:356:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS80 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3027)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3033)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3035)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3041)




                    #action start
                                
                    value = Fraction ( int ( MINUS80.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt32 == 2:
                    # grammar/ShyRecognizerBackend.g:361:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:361:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:361:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3073)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3075)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3081)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 42, 48, 50, 60, 70, 72])
    FOLLOW_stateless_in_start114 = frozenset([1, 42, 48, 50, 60, 70, 72])
    FOLLOW_consts_in_start141 = frozenset([1, 42, 48, 50, 60, 70, 72])
    FOLLOW_types_in_start167 = frozenset([1, 42, 48, 50, 60, 70, 72])
    FOLLOW_messages_in_start193 = frozenset([1, 42, 48, 50, 60, 70, 72])
    FOLLOW_vars_in_start219 = frozenset([1, 42, 48, 50, 60, 70, 72])
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
    FOLLOW_statement_in_statements928 = frozenset([3, 62, 64, 67, 68, 69])
    FOLLOW_statement_call_in_statement984 = frozenset([1])
    FOLLOW_statement_if_in_statement1008 = frozenset([1])
    FOLLOW_statement_assign_in_statement1032 = frozenset([1])
    FOLLOW_statement_with_in_statement1056 = frozenset([1])
    FOLLOW_statement_while_in_statement1080 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1123 = frozenset([2])
    FOLLOW_ID_in_statement_with1125 = frozenset([61])
    FOLLOW_statements_in_statement_with1127 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1178 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1194 = frozenset([18, 19, 23, 27, 63])
    FOLLOW_TREE_STATEMENT_ASSIGN_TO_in_statement_assign1242 = frozenset([19])
    FOLLOW_ID_in_statement_assign1258 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1341 = frozenset([2])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_if1359 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_if1361 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_if1415 = frozenset([2])
    FOLLOW_statements_in_statement_if1417 = frozenset([3])
    FOLLOW_TREE_STATEMENT_WHILE_in_statement_while1492 = frozenset([2])
    FOLLOW_conditional_ops_in_statement_while1494 = frozenset([3])
    FOLLOW_condition_any_in_conditional_ops1537 = frozenset([61])
    FOLLOW_statements_in_conditional_ops1539 = frozenset([1])
    FOLLOW_condition_all_in_conditional_ops1563 = frozenset([61])
    FOLLOW_statements_in_conditional_ops1565 = frozenset([1])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1618 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1634 = frozenset([3, 64])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1709 = frozenset([2])
    FOLLOW_statement_call_in_condition_all1725 = frozenset([3, 64])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1790 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call1792 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args1847 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value1900 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1912 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1924 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1936 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1977 = frozenset([2])
    FOLLOW_ID_in_consts1979 = frozenset([45, 52, 53])
    FOLLOW_consts_items_in_consts1981 = frozenset([3])
    FOLLOW_consts_item_in_consts_items2036 = frozenset([1, 45, 52, 53])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item2091 = frozenset([2])
    FOLLOW_ID_in_consts_item2093 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2095 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item2123 = frozenset([2])
    FOLLOW_ID_in_consts_item2125 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2127 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2155 = frozenset([2])
    FOLLOW_ID_in_consts_item2157 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2159 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2214 = frozenset([2])
    FOLLOW_ID_in_types2216 = frozenset([71])
    FOLLOW_types_items_in_types2218 = frozenset([3])
    FOLLOW_types_item_in_types_items2273 = frozenset([1, 71])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2328 = frozenset([2])
    FOLLOW_ID_in_types_item2330 = frozenset([38])
    FOLLOW_attrs_hints_in_types_item2332 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2387 = frozenset([2])
    FOLLOW_ID_in_messages2389 = frozenset([49])
    FOLLOW_messages_items_in_messages2391 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2446 = frozenset([1, 49])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2501 = frozenset([2])
    FOLLOW_ID_in_messages_item2503 = frozenset([38])
    FOLLOW_attrs_hints_in_messages_item2505 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars2550 = frozenset([2])
    FOLLOW_ID_in_vars2552 = frozenset([38])
    FOLLOW_attrs_hints_in_vars2554 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2607 = frozenset([1, 39])
    FOLLOW_attr_hint_in_attrs_hints2611 = frozenset([1, 39])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2656 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint2658 = frozenset([37])
    FOLLOW_TREE_ATTR_in_attr_hint2664 = frozenset([2])
    FOLLOW_ID_in_attr_hint2666 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2708 = frozenset([2])
    FOLLOW_hint_in_attr_hint2710 = frozenset([37])
    FOLLOW_TREE_ATTR_in_attr_hint2716 = frozenset([2])
    FOLLOW_ID_in_attr_hint2718 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2787 = frozenset([2])
    FOLLOW_ID_in_hint2789 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2817 = frozenset([2])
    FOLLOW_ID_in_hint2819 = frozenset([19, 74])
    FOLLOW_hint_args_in_hint2821 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2876 = frozenset([1, 19, 74])
    FOLLOW_ID_in_hint_arg2909 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2921 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2952 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2954 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2982 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3027 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3033 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3035 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3041 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract3073 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3075 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3081 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
