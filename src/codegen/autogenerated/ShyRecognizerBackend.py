# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-31 19:47:32

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset


from fractions import Fraction

def update_start_dict ( res , part , name , value ) :
    if part not in res :
        res [ part ] = dict ( )
    if name not in res [ part ] :
        res [ part ] [ name ] = dict ( )
    res [ part ] [ name ] . update ( value )



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
    # grammar/ShyRecognizerBackend.g:22:1: start returns [ value ] : ( module | stateless | consts | types | messages | vars )* ;
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
                # grammar/ShyRecognizerBackend.g:25:5: ( ( module | stateless | consts | types | messages | vars )* )
                # grammar/ShyRecognizerBackend.g:25:9: ( module | stateless | consts | types | messages | vars )*
                pass 
                # grammar/ShyRecognizerBackend.g:25:9: ( module | stateless | consts | types | messages | vars )*
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
                        # grammar/ShyRecognizerBackend.g:25:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start87)
                        module1 = self.module()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'module' ,
                            ((module1 is not None) and [module1.title] or [None])[0] , ((module1 is not None) and [module1.content] or [None])[0] )
                                    
                        #action end



                    elif alt1 == 2:
                        # grammar/ShyRecognizerBackend.g:30:11: stateless
                        pass 
                        self._state.following.append(self.FOLLOW_stateless_in_start114)
                        stateless2 = self.stateless()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'stateless' ,
                            ((stateless2 is not None) and [stateless2.title] or [None])[0] , ((stateless2 is not None) and [stateless2.content] or [None])[0] )
                                    
                        #action end



                    elif alt1 == 3:
                        # grammar/ShyRecognizerBackend.g:35:11: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start141)
                        consts3 = self.consts()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'consts' ,
                            ((consts3 is not None) and [consts3.title] or [None])[0] , ((consts3 is not None) and [consts3.content] or [None])[0] )
                                    
                        #action end



                    elif alt1 == 4:
                        # grammar/ShyRecognizerBackend.g:40:11: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start167)
                        types4 = self.types()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'types' ,
                            ((types4 is not None) and [types4.title] or [None])[0] , ((types4 is not None) and [types4.content] or [None])[0] )
                                    
                        #action end



                    elif alt1 == 5:
                        # grammar/ShyRecognizerBackend.g:45:11: messages
                        pass 
                        self._state.following.append(self.FOLLOW_messages_in_start193)
                        messages5 = self.messages()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'messages' ,
                            ((messages5 is not None) and [messages5.title] or [None])[0] , ((messages5 is not None) and [messages5.content] or [None])[0] )
                                    
                        #action end



                    elif alt1 == 6:
                        # grammar/ShyRecognizerBackend.g:50:11: vars
                        pass 
                        self._state.following.append(self.FOLLOW_vars_in_start219)
                        vars6 = self.vars()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'vars' ,
                            ((vars6 is not None) and [vars6.title] or [None])[0] , ((vars6 is not None) and [vars6.content] or [None])[0] )
                                    
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
    # grammar/ShyRecognizerBackend.g:58:1: module returns [ title , content ] : ^( TREE_MODULE ID ( module_queue )? ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        ID7 = None
        module_queue8 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:60:5: ( ^( TREE_MODULE ID ( module_queue )? ) )
                # grammar/ShyRecognizerBackend.g:60:9: ^( TREE_MODULE ID ( module_queue )? )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module274)

                self.match(self.input, DOWN, None)
                ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_module276)

                #action start
                retval.title , retval.content = ID7.text , dict ( ) 
                #action end


                # grammar/ShyRecognizerBackend.g:62:13: ( module_queue )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == TREE_MODULE_QUEUE) :
                    alt2 = 1
                if alt2 == 1:
                    # grammar/ShyRecognizerBackend.g:62:15: module_queue
                    pass 
                    self._state.following.append(self.FOLLOW_module_queue_in_module306)
                    module_queue8 = self.module_queue()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'module_queue' ] = module_queue8 
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


        ID9 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:70:5: ( ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerBackend.g:70:9: ^( TREE_MODULE_QUEUE ID )
                pass 
                self.match(self.input, TREE_MODULE_QUEUE, self.FOLLOW_TREE_MODULE_QUEUE_in_module_queue380)

                self.match(self.input, DOWN, None)
                ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue382)

                self.match(self.input, UP, None)


                #action start
                value = ID9.text 
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


        ID10 = None
        ID11 = None
        procs12 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:75:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == TREE_STATELESS) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 2) :
                        LA3_2 = self.input.LA(3)

                        if (LA3_2 == ID) :
                            LA3_3 = self.input.LA(4)

                            if (LA3_3 == 3) :
                                alt3 = 1
                            elif (LA3_3 == TREE_PROC) :
                                alt3 = 2
                            else:
                                nvae = NoViableAltException("", 3, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 3, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyRecognizerBackend.g:75:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless415)

                    self.match(self.input, DOWN, None)
                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless417)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID10.text , dict ( ) 
                    #action end



                elif alt3 == 2:
                    # grammar/ShyRecognizerBackend.g:77:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless445)

                    self.match(self.input, DOWN, None)
                    ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless447)

                    self._state.following.append(self.FOLLOW_procs_in_stateless449)
                    procs12 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID11.text , procs12 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "procs"
    # grammar/ShyRecognizerBackend.g:81:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc13 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:84:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:84:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:84:9: ( proc )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == TREE_PROC) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerBackend.g:84:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs504)
                        proc13 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc13 is not None) and [proc13.title] or [None])[0] ] = ((proc13 is not None) and [proc13.content] or [None])[0] 
                        #action end



                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1





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
    # grammar/ShyRecognizerBackend.g:87:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID14 = None
        proc_args15 = None

        proc_vars16 = None

        statements17 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:90:5: ( ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:90:9: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc549)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_proc563)

                #action start
                retval.title = ID14.text 
                #action end


                # grammar/ShyRecognizerBackend.g:93:13: ( proc_args )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_PROC_ARGS) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:93:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc597)
                    proc_args15 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args15 
                    #action end





                # grammar/ShyRecognizerBackend.g:96:13: ( proc_vars )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_PROC_VARS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:96:15: proc_vars
                    pass 
                    self._state.following.append(self.FOLLOW_proc_vars_in_proc647)
                    proc_vars16 = self.proc_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = proc_vars16 
                    #action end





                # grammar/ShyRecognizerBackend.g:99:13: ( statements )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == TREE_STATEMENTS) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:99:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc697)
                    statements17 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements17 
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
    # grammar/ShyRecognizerBackend.g:105:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints18 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:107:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:107:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args770)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args772)
                attrs_hints18 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints18 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "proc_vars"
    # grammar/ShyRecognizerBackend.g:111:1: proc_vars returns [ value ] : ^( TREE_PROC_VARS attrs_hints ) ;
    def proc_vars(self, ):
        value = None


        attrs_hints19 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:113:5: ( ^( TREE_PROC_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:113:9: ^( TREE_PROC_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_VARS, self.FOLLOW_TREE_PROC_VARS_in_proc_vars817)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_vars819)
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

    # $ANTLR end "proc_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:117:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement20 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:120:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:120:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements874)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:120:28: ( statement )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((TREE_STATEMENT_ASSIGN <= LA8_0 <= TREE_STATEMENT_CALL) or (TREE_STATEMENT_IF <= LA8_0 <= TREE_STATEMENT_WITH)) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerBackend.g:120:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements878)
                        statement20 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement20 ) 
                        #action end



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statements"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:125:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with );
    def statement(self, ):
        value = None


        statement_call21 = None

        statement_if22 = None

        statement_assign23 = None

        statement_with24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:127:5: ( statement_call | statement_if | statement_assign | statement_with )
                alt9 = 4
                LA9 = self.input.LA(1)
                if LA9 == TREE_STATEMENT_CALL:
                    alt9 = 1
                elif LA9 == TREE_STATEMENT_IF:
                    alt9 = 2
                elif LA9 == TREE_STATEMENT_ASSIGN:
                    alt9 = 3
                elif LA9 == TREE_STATEMENT_WITH:
                    alt9 = 4
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:127:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement934)
                    statement_call21 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call21 
                    #action end



                elif alt9 == 2:
                    # grammar/ShyRecognizerBackend.g:129:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement958)
                    statement_if22 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if22 
                    #action end



                elif alt9 == 3:
                    # grammar/ShyRecognizerBackend.g:131:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement982)
                    statement_assign23 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign23 
                    #action end



                elif alt9 == 4:
                    # grammar/ShyRecognizerBackend.g:133:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement1006)
                    statement_with24 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with24 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:137:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID25 = None
        statements26 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:139:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:139:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with1049)

                self.match(self.input, DOWN, None)
                ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1051)

                self._state.following.append(self.FOLLOW_statements_in_statement_with1053)
                statements26 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID25.text : statements26 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:143:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID28 = None
        arbitrary_value27 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:145:5: ( ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:145:9: ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1094)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1096)
                arbitrary_value27 = self.arbitrary_value()

                self._state.following.pop()

                #action start
                value = { 'assign' : [ arbitrary_value27 , list ( ) ] } 
                #action end


                # grammar/ShyRecognizerBackend.g:147:13: ( ID )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ID) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:147:15: ID
                        pass 
                        ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1126)

                        #action start
                        value [ 'assign' ] [ - 1 ] . append ( ID28.text ) 
                        #action end



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:153:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) ;
    def statement_if(self, ):
        value = None


        statement_elif29 = None

        statement_else30 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:156:5: ( ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) )
                # grammar/ShyRecognizerBackend.g:156:9: ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1209)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:157:13: ( statement_elif )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == TREE_STATEMENT_ELIF) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:157:15: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1225)
                        statement_elif29 = self.statement_elif()

                        self._state.following.pop()

                        #action start
                        value [ 'if' ] . append ( statement_elif29 ) 
                        #action end



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1


                # grammar/ShyRecognizerBackend.g:160:13: ( statement_else )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == TREE_STATEMENT_ELSE) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:160:15: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1275)
                    statement_else30 = self.statement_else()

                    self._state.following.pop()

                    #action start
                    value [ 'else' ] = statement_else30 
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
    # grammar/ShyRecognizerBackend.g:166:1: statement_elif returns [ value ] : ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) );
    def statement_elif(self, ):
        value = None


        condition_any31 = None

        statements32 = None

        condition_all33 = None

        statements34 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:168:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == TREE_STATEMENT_ELIF) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == 2) :
                        LA13_2 = self.input.LA(3)

                        if (LA13_2 == TREE_CONDITION_ANY) :
                            alt13 = 1
                        elif (LA13_2 == TREE_CONDITION_ALL) :
                            alt13 = 2
                        else:
                            nvae = NoViableAltException("", 13, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 13, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # grammar/ShyRecognizerBackend.g:168:9: ^( TREE_STATEMENT_ELIF condition_any statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1348)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_any_in_statement_elif1350)
                    condition_any31 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1352)
                    statements32 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'any' : condition_any31 ,
                       'ops' : statements32 }
                                
                    #action end



                elif alt13 == 2:
                    # grammar/ShyRecognizerBackend.g:173:9: ^( TREE_STATEMENT_ELIF condition_all statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1380)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_all_in_statement_elif1382)
                    condition_all33 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1384)
                    statements34 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'all' : condition_all33 ,
                       'ops' : statements34 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerBackend.g:180:1: statement_else returns [ value ] : ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        value = None


        statements35 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:182:5: ( ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerBackend.g:182:9: ^( TREE_STATEMENT_ELSE statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1429)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statements_in_statement_else1431)
                statements35 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = statements35 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_else"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:186:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call36 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:189:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:189:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1486)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:190:13: ( statement_call )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TREE_STATEMENT_CALL) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:190:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1502)
                        statement_call36 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call36 ) 
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

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:195:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call37 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:198:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:198:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1577)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:199:13: ( statement_call )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == TREE_STATEMENT_CALL) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:199:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all1593)
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

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:204:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args38 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:206:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:206:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1658)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1660)
                    statement_call_args38 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args38 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:210:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value39 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:213:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:213:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:213:9: ( arbitrary_value )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA16_0 <= ID) or LA16_0 == MINUS or LA16_0 == NUMBER) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:213:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1715)
                        arbitrary_value39 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value39 ) 
                        #action end



                    else:
                        break #loop16





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:218:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID40 = None
        EXPRESSION41 = None
        num_whole42 = None

        num_fract43 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:220:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt17 = 4
                LA17 = self.input.LA(1)
                if LA17 == ID:
                    alt17 = 1
                elif LA17 == EXPRESSION:
                    alt17 = 2
                elif LA17 == MINUS:
                    LA17_3 = self.input.LA(2)

                    if (LA17_3 == NUMBER) :
                        LA17_5 = self.input.LA(3)

                        if (LA17_5 == DIVIDE) :
                            alt17 = 4
                        elif (LA17_5 == 3 or (EXPRESSION <= LA17_5 <= ID) or LA17_5 == MINUS or LA17_5 == NUMBER) :
                            alt17 = 3
                        else:
                            nvae = NoViableAltException("", 17, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 17, 3, self.input)

                        raise nvae


                elif LA17 == NUMBER:
                    LA17_4 = self.input.LA(2)

                    if (LA17_4 == DIVIDE) :
                        alt17 = 4
                    elif (LA17_4 == 3 or (EXPRESSION <= LA17_4 <= ID) or LA17_4 == MINUS or LA17_4 == NUMBER) :
                        alt17 = 3
                    else:
                        nvae = NoViableAltException("", 17, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerBackend.g:220:9: ID
                    pass 
                    ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1768)

                    #action start
                    value = ID40.text 
                    #action end



                elif alt17 == 2:
                    # grammar/ShyRecognizerBackend.g:221:9: EXPRESSION
                    pass 
                    EXPRESSION41 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1780)

                    #action start
                    value = EXPRESSION41.text 
                    #action end



                elif alt17 == 3:
                    # grammar/ShyRecognizerBackend.g:222:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1792)
                    num_whole42 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole42 
                    #action end



                elif alt17 == 4:
                    # grammar/ShyRecognizerBackend.g:223:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1804)
                    num_fract43 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract43 
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
    # grammar/ShyRecognizerBackend.g:226:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID44 = None
        consts_items45 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:229:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:229:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1845)

                self.match(self.input, DOWN, None)
                ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1847)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1849)
                consts_items45 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID44.text , consts_items45 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:233:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item46 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:236:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:236:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:236:9: ( consts_item )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA18_0 <= TREE_NUM_WHOLE)) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerBackend.g:236:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1904)
                        consts_item46 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item46 is not None) and [consts_item46.name] or [None])[0] ] = ((consts_item46 is not None) and [consts_item46.value] or [None])[0] 
                        #action end



                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1





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
    # grammar/ShyRecognizerBackend.g:241:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID47 = None
        ID49 = None
        ID51 = None
        EXPRESSION52 = None
        num_whole48 = None

        num_fract50 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:243:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt19 = 3
                LA19 = self.input.LA(1)
                if LA19 == TREE_NUM_WHOLE:
                    alt19 = 1
                elif LA19 == TREE_NUM_FRACT:
                    alt19 = 2
                elif LA19 == TREE_EXPRESSION:
                    alt19 = 3
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:243:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1959)

                    self.match(self.input, DOWN, None)
                    ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1961)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1963)
                    num_whole48 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID47.text , num_whole48 
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:245:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1991)

                    self.match(self.input, DOWN, None)
                    ID49 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1993)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1995)
                    num_fract50 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID49.text , num_fract50 
                    #action end



                elif alt19 == 3:
                    # grammar/ShyRecognizerBackend.g:247:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item2023)

                    self.match(self.input, DOWN, None)
                    ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2025)

                    EXPRESSION52 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2027)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID51.text , EXPRESSION52.text 
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
    # grammar/ShyRecognizerBackend.g:251:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID53 = None
        types_items54 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:254:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:254:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types2082)

                self.match(self.input, DOWN, None)
                ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_types2084)

                self._state.following.append(self.FOLLOW_types_items_in_types2086)
                types_items54 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID53.text , types_items54 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:258:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item55 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:261:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:261:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:261:9: ( types_item )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_TYPES_ITEM) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:261:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2141)
                        types_item55 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item55 is not None) and [types_item55.name] or [None])[0] ] = ((types_item55 is not None) and [types_item55.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:266:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID56 = None
        attrs_hints57 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:268:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:268:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2196)

                self.match(self.input, DOWN, None)
                ID56 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2198)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2200)
                attrs_hints57 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID56.text , attrs_hints57 
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
    # grammar/ShyRecognizerBackend.g:272:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID58 = None
        messages_items59 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:275:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:275:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2255)

                self.match(self.input, DOWN, None)
                ID58 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2257)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2259)
                messages_items59 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID58.text , messages_items59 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:279:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item60 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:282:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:282:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:282:9: ( messages_item )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_MESSAGES_ITEM) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:282:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2314)
                        messages_item60 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item60 is not None) and [messages_item60.name] or [None])[0] ] = ((messages_item60 is not None) and [messages_item60.value] or [None])[0] 
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

    # $ANTLR end "messages_items"


    class messages_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.messages_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerBackend.g:287:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID61 = None
        attrs_hints62 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:289:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:289:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2369)

                self.match(self.input, DOWN, None)
                ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2371)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2373)
                attrs_hints62 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID61.text , attrs_hints62 
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
    # grammar/ShyRecognizerBackend.g:293:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID63 = None
        attrs_hints64 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:295:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:295:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars2418)

                self.match(self.input, DOWN, None)
                ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2420)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2422)
                attrs_hints64 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID63.text , attrs_hints64 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:299:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint65 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:302:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:302:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2475)

                # grammar/ShyRecognizerBackend.g:302:26: ( attr_hint )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == TREE_ATTR_HINT) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:302:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2479)
                        attr_hint65 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint65 ) 
                        #action end



                    else:
                        break #loop22





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:305:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID66 = None
        ID67 = None
        hint68 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:308:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == TREE_ATTR_HINT) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == 2) :
                        LA25_2 = self.input.LA(3)

                        if (LA25_2 == TREE_HINT_NONE) :
                            alt25 = 1
                        elif (LA25_2 == TREE_HINT) :
                            alt25 = 2
                        else:
                            nvae = NoViableAltException("", 25, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # grammar/ShyRecognizerBackend.g:308:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2524)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint2526)

                    # grammar/ShyRecognizerBackend.g:308:42: ( ^( TREE_ATTR ID ) )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == TREE_ATTR) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerBackend.g:308:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2532)

                            self.match(self.input, DOWN, None)
                            ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2534)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID66.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    self.match(self.input, UP, None)



                elif alt25 == 2:
                    # grammar/ShyRecognizerBackend.g:311:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2576)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2578)
                    hint68 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:311:32: ( ^( TREE_ATTR ID ) )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == TREE_ATTR) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerBackend.g:311:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2584)

                            self.match(self.input, DOWN, None)
                            ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2586)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID67.text ] = hint68 
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

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:316:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID69 = None
        ID70 = None
        hint_args71 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:319:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == TREE_HINT) :
                    LA26_1 = self.input.LA(2)

                    if (LA26_1 == 2) :
                        LA26_2 = self.input.LA(3)

                        if (LA26_2 == ID) :
                            LA26_3 = self.input.LA(4)

                            if (LA26_3 == 3) :
                                alt26 = 1
                            elif (LA26_3 == ID or LA26_3 == UNDERSCORE) :
                                alt26 = 2
                            else:
                                nvae = NoViableAltException("", 26, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerBackend.g:319:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2655)

                    self.match(self.input, DOWN, None)
                    ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2657)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID69.text ] = list ( ) 
                    #action end



                elif alt26 == 2:
                    # grammar/ShyRecognizerBackend.g:321:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2685)

                    self.match(self.input, DOWN, None)
                    ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2687)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2689)
                    hint_args71 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID70.text ] = hint_args71 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:325:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg72 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:328:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:328:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:328:9: ( hint_arg )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == ID or LA27_0 == UNDERSCORE) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerBackend.g:328:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2744)
                        hint_arg72 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg72 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:331:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID73 = None
        UNDERSCORE74 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:333:5: ( ID | UNDERSCORE )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == ID) :
                    alt28 = 1
                elif (LA28_0 == UNDERSCORE) :
                    alt28 = 2
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # grammar/ShyRecognizerBackend.g:333:9: ID
                    pass 
                    ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2777)

                    #action start
                    value = ID73.text 
                    #action end



                elif alt28 == 2:
                    # grammar/ShyRecognizerBackend.g:334:9: UNDERSCORE
                    pass 
                    UNDERSCORE74 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2789)

                    #action start
                    value = UNDERSCORE74.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:337:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS75 = None
        NUMBER76 = None
        NUMBER77 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:339:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == MINUS) :
                    alt29 = 1
                elif (LA29_0 == NUMBER) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # grammar/ShyRecognizerBackend.g:339:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:339:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:339:11: MINUS NUMBER
                    pass 
                    MINUS75 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2820)

                    NUMBER76 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2822)




                    #action start
                    value = int ( MINUS75.text + NUMBER76.text ) 
                    #action end



                elif alt29 == 2:
                    # grammar/ShyRecognizerBackend.g:341:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:341:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:341:11: NUMBER
                    pass 
                    NUMBER77 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2850)




                    #action start
                    value = int ( NUMBER77.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:345:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS78 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:347:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:347:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:347:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:347:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS78 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2895)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2901)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2903)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2909)




                    #action start
                                
                    value = Fraction ( int ( MINUS78.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt30 == 2:
                    # grammar/ShyRecognizerBackend.g:352:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:352:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:352:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2941)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2943)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2949)




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
    FOLLOW_ID_in_module276 = frozenset([3, 51])
    FOLLOW_module_queue_in_module306 = frozenset([3])
    FOLLOW_TREE_MODULE_QUEUE_in_module_queue380 = frozenset([2])
    FOLLOW_ID_in_module_queue382 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless415 = frozenset([2])
    FOLLOW_ID_in_stateless417 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless445 = frozenset([2])
    FOLLOW_ID_in_stateless447 = frozenset([57])
    FOLLOW_procs_in_stateless449 = frozenset([3])
    FOLLOW_proc_in_procs504 = frozenset([1, 57])
    FOLLOW_TREE_PROC_in_proc549 = frozenset([2])
    FOLLOW_ID_in_proc563 = frozenset([3, 58, 59, 61])
    FOLLOW_proc_args_in_proc597 = frozenset([3, 59, 61])
    FOLLOW_proc_vars_in_proc647 = frozenset([3, 61])
    FOLLOW_statements_in_proc697 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args770 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args772 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars817 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_vars819 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements874 = frozenset([2])
    FOLLOW_statement_in_statements878 = frozenset([3, 62, 63, 66, 67])
    FOLLOW_statement_call_in_statement934 = frozenset([1])
    FOLLOW_statement_if_in_statement958 = frozenset([1])
    FOLLOW_statement_assign_in_statement982 = frozenset([1])
    FOLLOW_statement_with_in_statement1006 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with1049 = frozenset([2])
    FOLLOW_ID_in_statement_with1051 = frozenset([61])
    FOLLOW_statements_in_statement_with1053 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign1094 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign1096 = frozenset([19])
    FOLLOW_ID_in_statement_assign1126 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1209 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if1225 = frozenset([3, 64, 65])
    FOLLOW_statement_else_in_statement_if1275 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1348 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif1350 = frozenset([61])
    FOLLOW_statements_in_statement_elif1352 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1380 = frozenset([2])
    FOLLOW_condition_all_in_statement_elif1382 = frozenset([61])
    FOLLOW_statements_in_statement_elif1384 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1429 = frozenset([2])
    FOLLOW_statements_in_statement_else1431 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1486 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1502 = frozenset([3, 63])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1577 = frozenset([2])
    FOLLOW_statement_call_in_condition_all1593 = frozenset([3, 63])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1658 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call1660 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args1715 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value1768 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1780 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1792 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1804 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1845 = frozenset([2])
    FOLLOW_ID_in_consts1847 = frozenset([45, 52, 53])
    FOLLOW_consts_items_in_consts1849 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1904 = frozenset([1, 45, 52, 53])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1959 = frozenset([2])
    FOLLOW_ID_in_consts_item1961 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item1963 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1991 = frozenset([2])
    FOLLOW_ID_in_consts_item1993 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item1995 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item2023 = frozenset([2])
    FOLLOW_ID_in_consts_item2025 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2027 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types2082 = frozenset([2])
    FOLLOW_ID_in_types2084 = frozenset([69])
    FOLLOW_types_items_in_types2086 = frozenset([3])
    FOLLOW_types_item_in_types_items2141 = frozenset([1, 69])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2196 = frozenset([2])
    FOLLOW_ID_in_types_item2198 = frozenset([38])
    FOLLOW_attrs_hints_in_types_item2200 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2255 = frozenset([2])
    FOLLOW_ID_in_messages2257 = frozenset([49])
    FOLLOW_messages_items_in_messages2259 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2314 = frozenset([1, 49])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2369 = frozenset([2])
    FOLLOW_ID_in_messages_item2371 = frozenset([38])
    FOLLOW_attrs_hints_in_messages_item2373 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars2418 = frozenset([2])
    FOLLOW_ID_in_vars2420 = frozenset([38])
    FOLLOW_attrs_hints_in_vars2422 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2475 = frozenset([1, 39])
    FOLLOW_attr_hint_in_attrs_hints2479 = frozenset([1, 39])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2524 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint2526 = frozenset([37])
    FOLLOW_TREE_ATTR_in_attr_hint2532 = frozenset([2])
    FOLLOW_ID_in_attr_hint2534 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2576 = frozenset([2])
    FOLLOW_hint_in_attr_hint2578 = frozenset([37])
    FOLLOW_TREE_ATTR_in_attr_hint2584 = frozenset([2])
    FOLLOW_ID_in_attr_hint2586 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2655 = frozenset([2])
    FOLLOW_ID_in_hint2657 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2685 = frozenset([2])
    FOLLOW_ID_in_hint2687 = frozenset([19, 72])
    FOLLOW_hint_args_in_hint2689 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2744 = frozenset([1, 19, 72])
    FOLLOW_ID_in_hint_arg2777 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2789 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2820 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2822 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2850 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2895 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2901 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2903 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2909 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2941 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2943 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2949 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
