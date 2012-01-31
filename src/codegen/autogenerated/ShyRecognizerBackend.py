# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-31 19:08:12

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
NEWLINE=25
NUMBER=26
OPS=27
PASTE=28
PROC=29
REPLACE=30
REPLY=31
REQUEST=32
STATELESS=33
STRING=34
TREE_ARBITRARY_TOKEN=35
TREE_ATTR=36
TREE_ATTRS_HINTS=37
TREE_ATTR_HINT=38
TREE_CONDITION_ALL=39
TREE_CONDITION_ANY=40
TREE_CONSTS=41
TREE_COPY=42
TREE_COPY_PASTE=43
TREE_EXPRESSION=44
TREE_HINT=45
TREE_HINT_NONE=46
TREE_MESSAGES=47
TREE_MESSAGES_ITEM=48
TREE_MODULE=49
TREE_NUM_FRACT=50
TREE_NUM_WHOLE=51
TREE_PASTE=52
TREE_PASTE_REPLACE=53
TREE_PASTE_WITH=54
TREE_PROC=55
TREE_PROC_ARGS=56
TREE_PROC_VARS=57
TREE_STATELESS=58
TREE_STATEMENTS=59
TREE_STATEMENT_ASSIGN=60
TREE_STATEMENT_CALL=61
TREE_STATEMENT_ELIF=62
TREE_STATEMENT_ELSE=63
TREE_STATEMENT_IF=64
TREE_STATEMENT_WITH=65
TREE_TYPES=66
TREE_TYPES_ITEM=67
TREE_VARS=68
TYPES=69
UNDERSCORE=70
VARS=71
WHITESPACE=72
WITH=73

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "NEWLINE", 
    "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "REPLY", "REQUEST", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", 
    "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", 
    "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", 
    "TREE_MESSAGES", "TREE_MESSAGES_ITEM", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WITH", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", "UNDERSCORE", "VARS", "WHITESPACE", 
    "WITH"
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
                            module1 , dict ( ) )
                                    
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



    # $ANTLR start "module"
    # grammar/ShyRecognizerBackend.g:58:1: module returns [ value ] : ^( TREE_MODULE ID ) ;
    def module(self, ):
        value = None


        ID7 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:60:5: ( ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerBackend.g:60:9: ^( TREE_MODULE ID )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module274)

                self.match(self.input, DOWN, None)
                ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_module276)

                self.match(self.input, UP, None)


                #action start
                value = ID7.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module"


    class stateless_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.stateless_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "stateless"
    # grammar/ShyRecognizerBackend.g:63:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID8 = None
        ID9 = None
        procs10 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:65:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == TREE_STATELESS) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 2) :
                        LA2_2 = self.input.LA(3)

                        if (LA2_2 == ID) :
                            LA2_3 = self.input.LA(4)

                            if (LA2_3 == 3) :
                                alt2 = 1
                            elif (LA2_3 == TREE_PROC) :
                                alt2 = 2
                            else:
                                nvae = NoViableAltException("", 2, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 2, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 2, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # grammar/ShyRecognizerBackend.g:65:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless309)

                    self.match(self.input, DOWN, None)
                    ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless311)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID8.text , dict ( ) 
                    #action end



                elif alt2 == 2:
                    # grammar/ShyRecognizerBackend.g:67:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless339)

                    self.match(self.input, DOWN, None)
                    ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless341)

                    self._state.following.append(self.FOLLOW_procs_in_stateless343)
                    procs10 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID9.text , procs10 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "procs"
    # grammar/ShyRecognizerBackend.g:71:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc11 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:74:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:74:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:74:9: ( proc )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == TREE_PROC) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyRecognizerBackend.g:74:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs398)
                        proc11 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc11 is not None) and [proc11.title] or [None])[0] ] = ((proc11 is not None) and [proc11.content] or [None])[0] 
                        #action end



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1





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
    # grammar/ShyRecognizerBackend.g:77:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID12 = None
        proc_args13 = None

        proc_vars14 = None

        statements15 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:80:5: ( ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:80:9: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc443)

                self.match(self.input, DOWN, None)
                ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_proc457)

                #action start
                retval.title = ID12.text 
                #action end


                # grammar/ShyRecognizerBackend.g:83:13: ( proc_args )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_PROC_ARGS) :
                    alt4 = 1
                if alt4 == 1:
                    # grammar/ShyRecognizerBackend.g:83:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc491)
                    proc_args13 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args13 
                    #action end





                # grammar/ShyRecognizerBackend.g:86:13: ( proc_vars )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_PROC_VARS) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:86:15: proc_vars
                    pass 
                    self._state.following.append(self.FOLLOW_proc_vars_in_proc541)
                    proc_vars14 = self.proc_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = proc_vars14 
                    #action end





                # grammar/ShyRecognizerBackend.g:89:13: ( statements )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_STATEMENTS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:89:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc591)
                    statements15 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements15 
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
    # grammar/ShyRecognizerBackend.g:95:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints16 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:97:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:97:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args664)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args666)
                attrs_hints16 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints16 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "proc_vars"
    # grammar/ShyRecognizerBackend.g:101:1: proc_vars returns [ value ] : ^( TREE_PROC_VARS attrs_hints ) ;
    def proc_vars(self, ):
        value = None


        attrs_hints17 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:103:5: ( ^( TREE_PROC_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:103:9: ^( TREE_PROC_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_VARS, self.FOLLOW_TREE_PROC_VARS_in_proc_vars711)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_vars713)
                attrs_hints17 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints17 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:107:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement18 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:110:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:110:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements768)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:110:28: ( statement )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((TREE_STATEMENT_ASSIGN <= LA7_0 <= TREE_STATEMENT_CALL) or (TREE_STATEMENT_IF <= LA7_0 <= TREE_STATEMENT_WITH)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerBackend.g:110:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements772)
                        statement18 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement18 ) 
                        #action end



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statements"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:115:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with );
    def statement(self, ):
        value = None


        statement_call19 = None

        statement_if20 = None

        statement_assign21 = None

        statement_with22 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:117:5: ( statement_call | statement_if | statement_assign | statement_with )
                alt8 = 4
                LA8 = self.input.LA(1)
                if LA8 == TREE_STATEMENT_CALL:
                    alt8 = 1
                elif LA8 == TREE_STATEMENT_IF:
                    alt8 = 2
                elif LA8 == TREE_STATEMENT_ASSIGN:
                    alt8 = 3
                elif LA8 == TREE_STATEMENT_WITH:
                    alt8 = 4
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # grammar/ShyRecognizerBackend.g:117:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement828)
                    statement_call19 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call19 
                    #action end



                elif alt8 == 2:
                    # grammar/ShyRecognizerBackend.g:119:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement852)
                    statement_if20 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if20 
                    #action end



                elif alt8 == 3:
                    # grammar/ShyRecognizerBackend.g:121:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement876)
                    statement_assign21 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign21 
                    #action end



                elif alt8 == 4:
                    # grammar/ShyRecognizerBackend.g:123:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement900)
                    statement_with22 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with22 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:127:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID23 = None
        statements24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:129:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:129:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with943)

                self.match(self.input, DOWN, None)
                ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with945)

                self._state.following.append(self.FOLLOW_statements_in_statement_with947)
                statements24 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID23.text : statements24 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:133:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID26 = None
        arbitrary_value25 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:135:5: ( ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:135:9: ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign988)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign990)
                arbitrary_value25 = self.arbitrary_value()

                self._state.following.pop()

                #action start
                value = { 'assign' : [ arbitrary_value25 , list ( ) ] } 
                #action end


                # grammar/ShyRecognizerBackend.g:137:13: ( ID )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == ID) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerBackend.g:137:15: ID
                        pass 
                        ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1020)

                        #action start
                        value [ 'assign' ] [ - 1 ] . append ( ID26.text ) 
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

    # $ANTLR end "statement_assign"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:143:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) ;
    def statement_if(self, ):
        value = None


        statement_elif27 = None

        statement_else28 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:146:5: ( ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) )
                # grammar/ShyRecognizerBackend.g:146:9: ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1103)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:147:13: ( statement_elif )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_STATEMENT_ELIF) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:147:15: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1119)
                        statement_elif27 = self.statement_elif()

                        self._state.following.pop()

                        #action start
                        value [ 'if' ] . append ( statement_elif27 ) 
                        #action end



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1


                # grammar/ShyRecognizerBackend.g:150:13: ( statement_else )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_STATEMENT_ELSE) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:150:15: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1169)
                    statement_else28 = self.statement_else()

                    self._state.following.pop()

                    #action start
                    value [ 'else' ] = statement_else28 
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
    # grammar/ShyRecognizerBackend.g:156:1: statement_elif returns [ value ] : ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) );
    def statement_elif(self, ):
        value = None


        condition_any29 = None

        statements30 = None

        condition_all31 = None

        statements32 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:158:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == TREE_STATEMENT_ELIF) :
                    LA12_1 = self.input.LA(2)

                    if (LA12_1 == 2) :
                        LA12_2 = self.input.LA(3)

                        if (LA12_2 == TREE_CONDITION_ANY) :
                            alt12 = 1
                        elif (LA12_2 == TREE_CONDITION_ALL) :
                            alt12 = 2
                        else:
                            nvae = NoViableAltException("", 12, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 12, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:158:9: ^( TREE_STATEMENT_ELIF condition_any statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1242)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_any_in_statement_elif1244)
                    condition_any29 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1246)
                    statements30 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'any' : condition_any29 ,
                       'ops' : statements30 }
                                
                    #action end



                elif alt12 == 2:
                    # grammar/ShyRecognizerBackend.g:163:9: ^( TREE_STATEMENT_ELIF condition_all statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1274)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_all_in_statement_elif1276)
                    condition_all31 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1278)
                    statements32 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'all' : condition_all31 ,
                       'ops' : statements32 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerBackend.g:170:1: statement_else returns [ value ] : ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        value = None


        statements33 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:172:5: ( ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerBackend.g:172:9: ^( TREE_STATEMENT_ELSE statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1323)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statements_in_statement_else1325)
                statements33 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = statements33 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_else"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:176:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call34 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:179:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:179:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1380)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:180:13: ( statement_call )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_STATEMENT_CALL) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:180:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1396)
                        statement_call34 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call34 ) 
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

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:185:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call35 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:188:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:188:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1471)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:189:13: ( statement_call )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TREE_STATEMENT_CALL) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:189:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all1487)
                        statement_call35 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call35 ) 
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

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:194:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args36 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:196:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:196:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1552)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1554)
                    statement_call_args36 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args36 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:200:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value37 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:203:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:203:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:203:9: ( arbitrary_value )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA15_0 <= ID) or LA15_0 == MINUS or LA15_0 == NUMBER) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:203:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1609)
                        arbitrary_value37 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value37 ) 
                        #action end



                    else:
                        break #loop15





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerBackend.g:208:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID38 = None
        EXPRESSION39 = None
        num_whole40 = None

        num_fract41 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:210:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt16 = 4
                LA16 = self.input.LA(1)
                if LA16 == ID:
                    alt16 = 1
                elif LA16 == EXPRESSION:
                    alt16 = 2
                elif LA16 == MINUS:
                    LA16_3 = self.input.LA(2)

                    if (LA16_3 == NUMBER) :
                        LA16_5 = self.input.LA(3)

                        if (LA16_5 == DIVIDE) :
                            alt16 = 4
                        elif (LA16_5 == 3 or (EXPRESSION <= LA16_5 <= ID) or LA16_5 == MINUS or LA16_5 == NUMBER) :
                            alt16 = 3
                        else:
                            nvae = NoViableAltException("", 16, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 16, 3, self.input)

                        raise nvae


                elif LA16 == NUMBER:
                    LA16_4 = self.input.LA(2)

                    if (LA16_4 == DIVIDE) :
                        alt16 = 4
                    elif (LA16_4 == 3 or (EXPRESSION <= LA16_4 <= ID) or LA16_4 == MINUS or LA16_4 == NUMBER) :
                        alt16 = 3
                    else:
                        nvae = NoViableAltException("", 16, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammar/ShyRecognizerBackend.g:210:9: ID
                    pass 
                    ID38 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1662)

                    #action start
                    value = ID38.text 
                    #action end



                elif alt16 == 2:
                    # grammar/ShyRecognizerBackend.g:211:9: EXPRESSION
                    pass 
                    EXPRESSION39 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1674)

                    #action start
                    value = EXPRESSION39.text 
                    #action end



                elif alt16 == 3:
                    # grammar/ShyRecognizerBackend.g:212:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1686)
                    num_whole40 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole40 
                    #action end



                elif alt16 == 4:
                    # grammar/ShyRecognizerBackend.g:213:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1698)
                    num_fract41 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract41 
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
    # grammar/ShyRecognizerBackend.g:216:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID42 = None
        consts_items43 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:219:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:219:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1739)

                self.match(self.input, DOWN, None)
                ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1741)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1743)
                consts_items43 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID42.text , consts_items43 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:223:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item44 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:226:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:226:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:226:9: ( consts_item )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA17_0 <= TREE_NUM_WHOLE)) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:226:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1798)
                        consts_item44 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item44 is not None) and [consts_item44.name] or [None])[0] ] = ((consts_item44 is not None) and [consts_item44.value] or [None])[0] 
                        #action end



                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1





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
    # grammar/ShyRecognizerBackend.g:231:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID45 = None
        ID47 = None
        ID49 = None
        EXPRESSION50 = None
        num_whole46 = None

        num_fract48 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:233:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt18 = 3
                LA18 = self.input.LA(1)
                if LA18 == TREE_NUM_WHOLE:
                    alt18 = 1
                elif LA18 == TREE_NUM_FRACT:
                    alt18 = 2
                elif LA18 == TREE_EXPRESSION:
                    alt18 = 3
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerBackend.g:233:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1853)

                    self.match(self.input, DOWN, None)
                    ID45 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1855)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1857)
                    num_whole46 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID45.text , num_whole46 
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:235:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1885)

                    self.match(self.input, DOWN, None)
                    ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1887)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1889)
                    num_fract48 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID47.text , num_fract48 
                    #action end



                elif alt18 == 3:
                    # grammar/ShyRecognizerBackend.g:237:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1917)

                    self.match(self.input, DOWN, None)
                    ID49 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1919)

                    EXPRESSION50 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1921)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID49.text , EXPRESSION50.text 
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
    # grammar/ShyRecognizerBackend.g:241:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID51 = None
        types_items52 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:244:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:244:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1976)

                self.match(self.input, DOWN, None)
                ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_types1978)

                self._state.following.append(self.FOLLOW_types_items_in_types1980)
                types_items52 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID51.text , types_items52 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:248:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item53 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:251:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:251:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:251:9: ( types_item )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == TREE_TYPES_ITEM) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerBackend.g:251:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2035)
                        types_item53 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item53 is not None) and [types_item53.name] or [None])[0] ] = ((types_item53 is not None) and [types_item53.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:256:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID54 = None
        attrs_hints55 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:258:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:258:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2090)

                self.match(self.input, DOWN, None)
                ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2092)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2094)
                attrs_hints55 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID54.text , attrs_hints55 
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
    # grammar/ShyRecognizerBackend.g:262:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID56 = None
        messages_items57 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:265:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:265:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2149)

                self.match(self.input, DOWN, None)
                ID56 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2151)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2153)
                messages_items57 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID56.text , messages_items57 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:269:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item58 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:272:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:272:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:272:9: ( messages_item )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_MESSAGES_ITEM) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:272:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2208)
                        messages_item58 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item58 is not None) and [messages_item58.name] or [None])[0] ] = ((messages_item58 is not None) and [messages_item58.value] or [None])[0] 
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

    # $ANTLR end "messages_items"


    class messages_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.messages_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerBackend.g:277:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID59 = None
        attrs_hints60 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:279:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:279:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2263)

                self.match(self.input, DOWN, None)
                ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2265)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2267)
                attrs_hints60 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID59.text , attrs_hints60 
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
    # grammar/ShyRecognizerBackend.g:283:1: vars returns [ title , content ] : ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        ID61 = None
        attrs_hints62 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:285:5: ( ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:285:9: ^( TREE_VARS ID attrs_hints )
                pass 
                self.match(self.input, TREE_VARS, self.FOLLOW_TREE_VARS_in_vars2312)

                self.match(self.input, DOWN, None)
                ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2314)

                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2316)
                attrs_hints62 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID61.text , attrs_hints62 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "vars"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:289:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint63 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:292:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:292:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2369)

                # grammar/ShyRecognizerBackend.g:292:26: ( attr_hint )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_ATTR_HINT) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:292:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2373)
                        attr_hint63 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint63 ) 
                        #action end



                    else:
                        break #loop21





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attrs_hints"



    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerBackend.g:295:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID64 = None
        ID65 = None
        hint66 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:298:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == TREE_ATTR_HINT) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == 2) :
                        LA24_2 = self.input.LA(3)

                        if (LA24_2 == TREE_HINT_NONE) :
                            alt24 = 1
                        elif (LA24_2 == TREE_HINT) :
                            alt24 = 2
                        else:
                            nvae = NoViableAltException("", 24, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerBackend.g:298:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2418)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint2420)

                    # grammar/ShyRecognizerBackend.g:298:42: ( ^( TREE_ATTR ID ) )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == TREE_ATTR) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerBackend.g:298:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2426)

                            self.match(self.input, DOWN, None)
                            ID64 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2428)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID64.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    self.match(self.input, UP, None)



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:301:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2470)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2472)
                    hint66 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:301:32: ( ^( TREE_ATTR ID ) )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == TREE_ATTR) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerBackend.g:301:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2478)

                            self.match(self.input, DOWN, None)
                            ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2480)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID65.text ] = hint66 
                            #action end



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "attr_hint"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:306:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID67 = None
        ID68 = None
        hint_args69 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:309:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == TREE_HINT) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == 2) :
                        LA25_2 = self.input.LA(3)

                        if (LA25_2 == ID) :
                            LA25_3 = self.input.LA(4)

                            if (LA25_3 == 3) :
                                alt25 = 1
                            elif (LA25_3 == ID or LA25_3 == UNDERSCORE) :
                                alt25 = 2
                            else:
                                nvae = NoViableAltException("", 25, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerBackend.g:309:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2549)

                    self.match(self.input, DOWN, None)
                    ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2551)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID67.text ] = list ( ) 
                    #action end



                elif alt25 == 2:
                    # grammar/ShyRecognizerBackend.g:311:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2579)

                    self.match(self.input, DOWN, None)
                    ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2581)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2583)
                    hint_args69 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID68.text ] = hint_args69 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:315:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg70 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:318:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:318:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:318:9: ( hint_arg )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ID or LA26_0 == UNDERSCORE) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerBackend.g:318:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2638)
                        hint_arg70 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg70 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:321:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID71 = None
        UNDERSCORE72 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:323:5: ( ID | UNDERSCORE )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == ID) :
                    alt27 = 1
                elif (LA27_0 == UNDERSCORE) :
                    alt27 = 2
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammar/ShyRecognizerBackend.g:323:9: ID
                    pass 
                    ID71 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2671)

                    #action start
                    value = ID71.text 
                    #action end



                elif alt27 == 2:
                    # grammar/ShyRecognizerBackend.g:324:9: UNDERSCORE
                    pass 
                    UNDERSCORE72 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2683)

                    #action start
                    value = UNDERSCORE72.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:327:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS73 = None
        NUMBER74 = None
        NUMBER75 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:329:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == MINUS) :
                    alt28 = 1
                elif (LA28_0 == NUMBER) :
                    alt28 = 2
                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # grammar/ShyRecognizerBackend.g:329:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:329:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:329:11: MINUS NUMBER
                    pass 
                    MINUS73 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2714)

                    NUMBER74 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2716)




                    #action start
                    value = int ( MINUS73.text + NUMBER74.text ) 
                    #action end



                elif alt28 == 2:
                    # grammar/ShyRecognizerBackend.g:331:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:331:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:331:11: NUMBER
                    pass 
                    NUMBER75 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2744)




                    #action start
                    value = int ( NUMBER75.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:335:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS76 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:337:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:337:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:337:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:337:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS76 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2789)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2795)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2797)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2803)




                    #action start
                                
                    value = Fraction ( int ( MINUS76.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt29 == 2:
                    # grammar/ShyRecognizerBackend.g:342:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:342:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:342:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2835)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2837)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2843)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 41, 47, 49, 58, 66, 68])
    FOLLOW_stateless_in_start114 = frozenset([1, 41, 47, 49, 58, 66, 68])
    FOLLOW_consts_in_start141 = frozenset([1, 41, 47, 49, 58, 66, 68])
    FOLLOW_types_in_start167 = frozenset([1, 41, 47, 49, 58, 66, 68])
    FOLLOW_messages_in_start193 = frozenset([1, 41, 47, 49, 58, 66, 68])
    FOLLOW_vars_in_start219 = frozenset([1, 41, 47, 49, 58, 66, 68])
    FOLLOW_TREE_MODULE_in_module274 = frozenset([2])
    FOLLOW_ID_in_module276 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless309 = frozenset([2])
    FOLLOW_ID_in_stateless311 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless339 = frozenset([2])
    FOLLOW_ID_in_stateless341 = frozenset([55])
    FOLLOW_procs_in_stateless343 = frozenset([3])
    FOLLOW_proc_in_procs398 = frozenset([1, 55])
    FOLLOW_TREE_PROC_in_proc443 = frozenset([2])
    FOLLOW_ID_in_proc457 = frozenset([3, 56, 57, 59])
    FOLLOW_proc_args_in_proc491 = frozenset([3, 57, 59])
    FOLLOW_proc_vars_in_proc541 = frozenset([3, 59])
    FOLLOW_statements_in_proc591 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args664 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args666 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars711 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_vars713 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements768 = frozenset([2])
    FOLLOW_statement_in_statements772 = frozenset([3, 60, 61, 64, 65])
    FOLLOW_statement_call_in_statement828 = frozenset([1])
    FOLLOW_statement_if_in_statement852 = frozenset([1])
    FOLLOW_statement_assign_in_statement876 = frozenset([1])
    FOLLOW_statement_with_in_statement900 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with943 = frozenset([2])
    FOLLOW_ID_in_statement_with945 = frozenset([59])
    FOLLOW_statements_in_statement_with947 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign988 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign990 = frozenset([19])
    FOLLOW_ID_in_statement_assign1020 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1103 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if1119 = frozenset([3, 62, 63])
    FOLLOW_statement_else_in_statement_if1169 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1242 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif1244 = frozenset([59])
    FOLLOW_statements_in_statement_elif1246 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1274 = frozenset([2])
    FOLLOW_condition_all_in_statement_elif1276 = frozenset([59])
    FOLLOW_statements_in_statement_elif1278 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1323 = frozenset([2])
    FOLLOW_statements_in_statement_else1325 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1380 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1396 = frozenset([3, 61])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1471 = frozenset([2])
    FOLLOW_statement_call_in_condition_all1487 = frozenset([3, 61])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1552 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call1554 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args1609 = frozenset([1, 18, 19, 23, 26])
    FOLLOW_ID_in_arbitrary_value1662 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1674 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1686 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1698 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1739 = frozenset([2])
    FOLLOW_ID_in_consts1741 = frozenset([44, 50, 51])
    FOLLOW_consts_items_in_consts1743 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1798 = frozenset([1, 44, 50, 51])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1853 = frozenset([2])
    FOLLOW_ID_in_consts_item1855 = frozenset([23, 26])
    FOLLOW_num_whole_in_consts_item1857 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1885 = frozenset([2])
    FOLLOW_ID_in_consts_item1887 = frozenset([23, 26])
    FOLLOW_num_fract_in_consts_item1889 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1917 = frozenset([2])
    FOLLOW_ID_in_consts_item1919 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1921 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1976 = frozenset([2])
    FOLLOW_ID_in_types1978 = frozenset([67])
    FOLLOW_types_items_in_types1980 = frozenset([3])
    FOLLOW_types_item_in_types_items2035 = frozenset([1, 67])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2090 = frozenset([2])
    FOLLOW_ID_in_types_item2092 = frozenset([37])
    FOLLOW_attrs_hints_in_types_item2094 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2149 = frozenset([2])
    FOLLOW_ID_in_messages2151 = frozenset([48])
    FOLLOW_messages_items_in_messages2153 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2208 = frozenset([1, 48])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2263 = frozenset([2])
    FOLLOW_ID_in_messages_item2265 = frozenset([37])
    FOLLOW_attrs_hints_in_messages_item2267 = frozenset([3])
    FOLLOW_TREE_VARS_in_vars2312 = frozenset([2])
    FOLLOW_ID_in_vars2314 = frozenset([37])
    FOLLOW_attrs_hints_in_vars2316 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2369 = frozenset([1, 38])
    FOLLOW_attr_hint_in_attrs_hints2373 = frozenset([1, 38])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2418 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint2420 = frozenset([36])
    FOLLOW_TREE_ATTR_in_attr_hint2426 = frozenset([2])
    FOLLOW_ID_in_attr_hint2428 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2470 = frozenset([2])
    FOLLOW_hint_in_attr_hint2472 = frozenset([36])
    FOLLOW_TREE_ATTR_in_attr_hint2478 = frozenset([2])
    FOLLOW_ID_in_attr_hint2480 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2549 = frozenset([2])
    FOLLOW_ID_in_hint2551 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2579 = frozenset([2])
    FOLLOW_ID_in_hint2581 = frozenset([19, 70])
    FOLLOW_hint_args_in_hint2583 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2638 = frozenset([1, 19, 70])
    FOLLOW_ID_in_hint_arg2671 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2683 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2714 = frozenset([26])
    FOLLOW_NUMBER_in_num_whole2716 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2744 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2789 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2795 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2797 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2803 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2835 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2837 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2843 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
