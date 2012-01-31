# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-31 18:11:05

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
TREE_CONDITION_ALL=36
TREE_CONDITION_ANY=37
TREE_CONSTS=38
TREE_COPY=39
TREE_COPY_PASTE=40
TREE_EXPRESSION=41
TREE_HINT=42
TREE_HINT_NONE=43
TREE_MODULE=44
TREE_NUM_FRACT=45
TREE_NUM_WHOLE=46
TREE_PASTE=47
TREE_PASTE_REPLACE=48
TREE_PASTE_WITH=49
TREE_PROC=50
TREE_PROC_ARGS=51
TREE_PROC_VARS=52
TREE_STATELESS=53
TREE_STATEMENTS=54
TREE_STATEMENT_ASSIGN=55
TREE_STATEMENT_CALL=56
TREE_STATEMENT_ELIF=57
TREE_STATEMENT_ELSE=58
TREE_STATEMENT_IF=59
TREE_STATEMENT_WITH=60
TREE_TYPES=61
TREE_TYPES_ITEM=62
TREE_VAR=63
TREE_VARS_HINT=64
TREE_VAR_HINT=65
TYPES=66
UNDERSCORE=67
VARS=68
WHITESPACE=69
WITH=70

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "NEWLINE", 
    "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "REPLY", "REQUEST", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WITH", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_VAR", "TREE_VARS_HINT", "TREE_VAR_HINT", "TYPES", 
    "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:22:1: start returns [ value ] : ( module | stateless | consts | types )* ;
    def start(self, ):
        value = None


        module1 = None

        stateless2 = None

        consts3 = None

        types4 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:25:5: ( ( module | stateless | consts | types )* )
                # grammar/ShyRecognizerBackend.g:25:9: ( module | stateless | consts | types )*
                pass 
                # grammar/ShyRecognizerBackend.g:25:9: ( module | stateless | consts | types )*
                while True: #loop1
                    alt1 = 5
                    LA1 = self.input.LA(1)
                    if LA1 == TREE_MODULE:
                        alt1 = 1
                    elif LA1 == TREE_STATELESS:
                        alt1 = 2
                    elif LA1 == TREE_CONSTS:
                        alt1 = 3
                    elif LA1 == TREE_TYPES:
                        alt1 = 4

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
    # grammar/ShyRecognizerBackend.g:48:1: module returns [ value ] : ^( TREE_MODULE ID ) ;
    def module(self, ):
        value = None


        ID5 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:50:5: ( ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerBackend.g:50:9: ^( TREE_MODULE ID )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module222)

                self.match(self.input, DOWN, None)
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_module224)

                self.match(self.input, UP, None)


                #action start
                value = ID5.text 
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
    # grammar/ShyRecognizerBackend.g:53:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID6 = None
        ID7 = None
        procs8 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:55:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
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
                    # grammar/ShyRecognizerBackend.g:55:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless257)

                    self.match(self.input, DOWN, None)
                    ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless259)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID6.text , dict ( ) 
                    #action end



                elif alt2 == 2:
                    # grammar/ShyRecognizerBackend.g:57:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless287)

                    self.match(self.input, DOWN, None)
                    ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless289)

                    self._state.following.append(self.FOLLOW_procs_in_stateless291)
                    procs8 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID7.text , procs8 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "procs"
    # grammar/ShyRecognizerBackend.g:61:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc9 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:64:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:64:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:64:9: ( proc )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == TREE_PROC) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyRecognizerBackend.g:64:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs346)
                        proc9 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc9 is not None) and [proc9.title] or [None])[0] ] = ((proc9 is not None) and [proc9.content] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:67:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID10 = None
        proc_args11 = None

        proc_vars12 = None

        statements13 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:70:5: ( ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:70:9: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc391)

                self.match(self.input, DOWN, None)
                ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_proc405)

                #action start
                retval.title = ID10.text 
                #action end


                # grammar/ShyRecognizerBackend.g:73:13: ( proc_args )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_PROC_ARGS) :
                    alt4 = 1
                if alt4 == 1:
                    # grammar/ShyRecognizerBackend.g:73:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc439)
                    proc_args11 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args11 
                    #action end





                # grammar/ShyRecognizerBackend.g:76:13: ( proc_vars )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_PROC_VARS) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:76:15: proc_vars
                    pass 
                    self._state.following.append(self.FOLLOW_proc_vars_in_proc489)
                    proc_vars12 = self.proc_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = proc_vars12 
                    #action end





                # grammar/ShyRecognizerBackend.g:79:13: ( statements )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_STATEMENTS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:79:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc539)
                    statements13 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements13 
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
    # grammar/ShyRecognizerBackend.g:85:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS vars_hint ) ;
    def proc_args(self, ):
        value = None


        vars_hint14 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:87:5: ( ^( TREE_PROC_ARGS vars_hint ) )
                # grammar/ShyRecognizerBackend.g:87:9: ^( TREE_PROC_ARGS vars_hint )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args612)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_vars_hint_in_proc_args614)
                vars_hint14 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = vars_hint14 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "proc_vars"
    # grammar/ShyRecognizerBackend.g:91:1: proc_vars returns [ value ] : ^( TREE_PROC_VARS vars_hint ) ;
    def proc_vars(self, ):
        value = None


        vars_hint15 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:93:5: ( ^( TREE_PROC_VARS vars_hint ) )
                # grammar/ShyRecognizerBackend.g:93:9: ^( TREE_PROC_VARS vars_hint )
                pass 
                self.match(self.input, TREE_PROC_VARS, self.FOLLOW_TREE_PROC_VARS_in_proc_vars659)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_vars_hint_in_proc_vars661)
                vars_hint15 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = vars_hint15 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:97:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement16 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:100:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:100:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements716)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:100:28: ( statement )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((TREE_STATEMENT_ASSIGN <= LA7_0 <= TREE_STATEMENT_CALL) or (TREE_STATEMENT_IF <= LA7_0 <= TREE_STATEMENT_WITH)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerBackend.g:100:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements720)
                        statement16 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement16 ) 
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
    # grammar/ShyRecognizerBackend.g:105:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with );
    def statement(self, ):
        value = None


        statement_call17 = None

        statement_if18 = None

        statement_assign19 = None

        statement_with20 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:107:5: ( statement_call | statement_if | statement_assign | statement_with )
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
                    # grammar/ShyRecognizerBackend.g:107:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement776)
                    statement_call17 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call17 
                    #action end



                elif alt8 == 2:
                    # grammar/ShyRecognizerBackend.g:109:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement800)
                    statement_if18 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if18 
                    #action end



                elif alt8 == 3:
                    # grammar/ShyRecognizerBackend.g:111:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement824)
                    statement_assign19 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign19 
                    #action end



                elif alt8 == 4:
                    # grammar/ShyRecognizerBackend.g:113:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement848)
                    statement_with20 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with20 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:117:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID21 = None
        statements22 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:119:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:119:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with891)

                self.match(self.input, DOWN, None)
                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with893)

                self._state.following.append(self.FOLLOW_statements_in_statement_with895)
                statements22 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID21.text : statements22 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:123:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID24 = None
        arbitrary_value23 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:125:5: ( ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:125:9: ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign936)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign938)
                arbitrary_value23 = self.arbitrary_value()

                self._state.following.pop()

                #action start
                value = { 'assign' : [ arbitrary_value23 , list ( ) ] } 
                #action end


                # grammar/ShyRecognizerBackend.g:127:13: ( ID )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == ID) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerBackend.g:127:15: ID
                        pass 
                        ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign968)

                        #action start
                        value [ 'assign' ] [ - 1 ] . append ( ID24.text ) 
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
    # grammar/ShyRecognizerBackend.g:133:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) ;
    def statement_if(self, ):
        value = None


        statement_elif25 = None

        statement_else26 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:136:5: ( ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) )
                # grammar/ShyRecognizerBackend.g:136:9: ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1051)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:137:13: ( statement_elif )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_STATEMENT_ELIF) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:137:15: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1067)
                        statement_elif25 = self.statement_elif()

                        self._state.following.pop()

                        #action start
                        value [ 'if' ] . append ( statement_elif25 ) 
                        #action end



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1


                # grammar/ShyRecognizerBackend.g:140:13: ( statement_else )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_STATEMENT_ELSE) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:140:15: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1117)
                    statement_else26 = self.statement_else()

                    self._state.following.pop()

                    #action start
                    value [ 'else' ] = statement_else26 
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
    # grammar/ShyRecognizerBackend.g:146:1: statement_elif returns [ value ] : ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) );
    def statement_elif(self, ):
        value = None


        condition_any27 = None

        statements28 = None

        condition_all29 = None

        statements30 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:148:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) )
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
                    # grammar/ShyRecognizerBackend.g:148:9: ^( TREE_STATEMENT_ELIF condition_any statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1190)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_any_in_statement_elif1192)
                    condition_any27 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1194)
                    statements28 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'any' : condition_any27 ,
                       'ops' : statements28 }
                                
                    #action end



                elif alt12 == 2:
                    # grammar/ShyRecognizerBackend.g:153:9: ^( TREE_STATEMENT_ELIF condition_all statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1222)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_all_in_statement_elif1224)
                    condition_all29 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1226)
                    statements30 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'all' : condition_all29 ,
                       'ops' : statements30 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerBackend.g:160:1: statement_else returns [ value ] : ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        value = None


        statements31 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:162:5: ( ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerBackend.g:162:9: ^( TREE_STATEMENT_ELSE statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1271)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statements_in_statement_else1273)
                statements31 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = statements31 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_else"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:166:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call32 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:169:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:169:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1328)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:170:13: ( statement_call )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_STATEMENT_CALL) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:170:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1344)
                        statement_call32 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call32 ) 
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
    # grammar/ShyRecognizerBackend.g:175:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call33 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:178:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:178:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1419)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:179:13: ( statement_call )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TREE_STATEMENT_CALL) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:179:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all1435)
                        statement_call33 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call33 ) 
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
    # grammar/ShyRecognizerBackend.g:184:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args34 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:186:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:186:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1500)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1502)
                    statement_call_args34 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args34 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:190:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value35 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:193:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:193:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:193:9: ( arbitrary_value )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA15_0 <= ID) or LA15_0 == MINUS or LA15_0 == NUMBER) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:193:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1557)
                        arbitrary_value35 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value35 ) 
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
    # grammar/ShyRecognizerBackend.g:198:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID36 = None
        EXPRESSION37 = None
        num_whole38 = None

        num_fract39 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:200:5: ( ID | EXPRESSION | num_whole | num_fract )
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
                    # grammar/ShyRecognizerBackend.g:200:9: ID
                    pass 
                    ID36 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1610)

                    #action start
                    value = ID36.text 
                    #action end



                elif alt16 == 2:
                    # grammar/ShyRecognizerBackend.g:201:9: EXPRESSION
                    pass 
                    EXPRESSION37 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1622)

                    #action start
                    value = EXPRESSION37.text 
                    #action end



                elif alt16 == 3:
                    # grammar/ShyRecognizerBackend.g:202:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1634)
                    num_whole38 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole38 
                    #action end



                elif alt16 == 4:
                    # grammar/ShyRecognizerBackend.g:203:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1646)
                    num_fract39 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract39 
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
    # grammar/ShyRecognizerBackend.g:206:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID40 = None
        consts_items41 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:209:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:209:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1687)

                self.match(self.input, DOWN, None)
                ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1689)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1691)
                consts_items41 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID40.text , consts_items41 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:213:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item42 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:216:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:216:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:216:9: ( consts_item )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA17_0 <= TREE_NUM_WHOLE)) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:216:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1746)
                        consts_item42 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item42 is not None) and [consts_item42.name] or [None])[0] ] = ((consts_item42 is not None) and [consts_item42.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:221:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID43 = None
        ID45 = None
        ID47 = None
        EXPRESSION48 = None
        num_whole44 = None

        num_fract46 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:223:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerBackend.g:223:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1801)

                    self.match(self.input, DOWN, None)
                    ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1803)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1805)
                    num_whole44 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID43.text , num_whole44 
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:225:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1833)

                    self.match(self.input, DOWN, None)
                    ID45 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1835)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1837)
                    num_fract46 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID45.text , num_fract46 
                    #action end



                elif alt18 == 3:
                    # grammar/ShyRecognizerBackend.g:227:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1865)

                    self.match(self.input, DOWN, None)
                    ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1867)

                    EXPRESSION48 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1869)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID47.text , EXPRESSION48.text 
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
    # grammar/ShyRecognizerBackend.g:231:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID49 = None
        types_items50 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:234:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:234:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1924)

                self.match(self.input, DOWN, None)
                ID49 = self.match(self.input, ID, self.FOLLOW_ID_in_types1926)

                self._state.following.append(self.FOLLOW_types_items_in_types1928)
                types_items50 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID49.text , types_items50 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:238:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item51 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:241:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:241:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:241:9: ( types_item )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == TREE_TYPES_ITEM) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerBackend.g:241:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1983)
                        types_item51 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item51 is not None) and [types_item51.name] or [None])[0] ] = ((types_item51 is not None) and [types_item51.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:246:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID52 = None
        vars_hint53 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:248:5: ( ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerBackend.g:248:9: ^( TREE_TYPES_ITEM ID vars_hint )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2038)

                self.match(self.input, DOWN, None)
                ID52 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2040)

                self._state.following.append(self.FOLLOW_vars_hint_in_types_item2042)
                vars_hint53 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID52.text , vars_hint53 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerBackend.g:252:1: vars_hint returns [ value ] : TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        value = None


        var_hint54 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:255:5: ( TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerBackend.g:255:9: TREE_VARS_HINT ( var_hint )*
                pass 
                self.match(self.input, TREE_VARS_HINT, self.FOLLOW_TREE_VARS_HINT_in_vars_hint2095)

                # grammar/ShyRecognizerBackend.g:255:24: ( var_hint )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_VAR_HINT) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:255:26: var_hint
                        pass 
                        self._state.following.append(self.FOLLOW_var_hint_in_vars_hint2099)
                        var_hint54 = self.var_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( var_hint54 ) 
                        #action end



                    else:
                        break #loop20





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "vars_hint"



    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerBackend.g:258:1: var_hint returns [ value ] : ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        value = None


        var55 = None

        var56 = None

        hint57 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:261:5: ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == TREE_VAR_HINT) :
                    LA23_1 = self.input.LA(2)

                    if (LA23_1 == 2) :
                        LA23_2 = self.input.LA(3)

                        if (LA23_2 == TREE_HINT_NONE) :
                            alt23 = 1
                        elif (LA23_2 == TREE_HINT) :
                            alt23 = 2
                        else:
                            nvae = NoViableAltException("", 23, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 23, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerBackend.g:261:9: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint2144)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_var_hint2146)

                    # grammar/ShyRecognizerBackend.g:261:41: ( var )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == TREE_VAR) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerBackend.g:261:43: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint2150)
                            var55 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var55 ] = dict ( ) 
                            #action end



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    self.match(self.input, UP, None)



                elif alt23 == 2:
                    # grammar/ShyRecognizerBackend.g:264:9: ^( TREE_VAR_HINT hint ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint2190)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_var_hint2192)
                    hint57 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:264:31: ( var )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == TREE_VAR) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerBackend.g:264:33: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint2196)
                            var56 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var56 ] = hint57 
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

    # $ANTLR end "var_hint"



    # $ANTLR start "var"
    # grammar/ShyRecognizerBackend.g:269:1: var returns [ value ] : ^( TREE_VAR ID ) ;
    def var(self, ):
        value = None


        ID58 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:271:5: ( ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerBackend.g:271:9: ^( TREE_VAR ID )
                pass 
                self.match(self.input, TREE_VAR, self.FOLLOW_TREE_VAR_in_var2253)

                self.match(self.input, DOWN, None)
                ID58 = self.match(self.input, ID, self.FOLLOW_ID_in_var2255)

                self.match(self.input, UP, None)


                #action start
                value = ID58.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:274:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID59 = None
        ID60 = None
        hint_args61 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:277:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == TREE_HINT) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == 2) :
                        LA24_2 = self.input.LA(3)

                        if (LA24_2 == ID) :
                            LA24_3 = self.input.LA(4)

                            if (LA24_3 == 3) :
                                alt24 = 1
                            elif (LA24_3 == ID or LA24_3 == UNDERSCORE) :
                                alt24 = 2
                            else:
                                nvae = NoViableAltException("", 24, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerBackend.g:277:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2298)

                    self.match(self.input, DOWN, None)
                    ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2300)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID59.text ] = list ( ) 
                    #action end



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:279:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2328)

                    self.match(self.input, DOWN, None)
                    ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2330)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2332)
                    hint_args61 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID60.text ] = hint_args61 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:283:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg62 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:286:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:286:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:286:9: ( hint_arg )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ID or LA25_0 == UNDERSCORE) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerBackend.g:286:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2387)
                        hint_arg62 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg62 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:289:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID63 = None
        UNDERSCORE64 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:291:5: ( ID | UNDERSCORE )
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == ID) :
                    alt26 = 1
                elif (LA26_0 == UNDERSCORE) :
                    alt26 = 2
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # grammar/ShyRecognizerBackend.g:291:9: ID
                    pass 
                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2420)

                    #action start
                    value = ID63.text 
                    #action end



                elif alt26 == 2:
                    # grammar/ShyRecognizerBackend.g:292:9: UNDERSCORE
                    pass 
                    UNDERSCORE64 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2432)

                    #action start
                    value = UNDERSCORE64.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:295:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS65 = None
        NUMBER66 = None
        NUMBER67 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:297:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == MINUS) :
                    alt27 = 1
                elif (LA27_0 == NUMBER) :
                    alt27 = 2
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammar/ShyRecognizerBackend.g:297:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:297:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:297:11: MINUS NUMBER
                    pass 
                    MINUS65 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2463)

                    NUMBER66 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2465)




                    #action start
                    value = int ( MINUS65.text + NUMBER66.text ) 
                    #action end



                elif alt27 == 2:
                    # grammar/ShyRecognizerBackend.g:299:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:299:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:299:11: NUMBER
                    pass 
                    NUMBER67 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2493)




                    #action start
                    value = int ( NUMBER67.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:303:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS68 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:305:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:305:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:305:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:305:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS68 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2538)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2544)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2546)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2552)




                    #action start
                                
                    value = Fraction ( int ( MINUS68.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt28 == 2:
                    # grammar/ShyRecognizerBackend.g:310:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:310:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:310:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2584)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2586)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2592)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 38, 44, 53, 61])
    FOLLOW_stateless_in_start114 = frozenset([1, 38, 44, 53, 61])
    FOLLOW_consts_in_start141 = frozenset([1, 38, 44, 53, 61])
    FOLLOW_types_in_start167 = frozenset([1, 38, 44, 53, 61])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless287 = frozenset([2])
    FOLLOW_ID_in_stateless289 = frozenset([50])
    FOLLOW_procs_in_stateless291 = frozenset([3])
    FOLLOW_proc_in_procs346 = frozenset([1, 50])
    FOLLOW_TREE_PROC_in_proc391 = frozenset([2])
    FOLLOW_ID_in_proc405 = frozenset([3, 51, 52, 54])
    FOLLOW_proc_args_in_proc439 = frozenset([3, 52, 54])
    FOLLOW_proc_vars_in_proc489 = frozenset([3, 54])
    FOLLOW_statements_in_proc539 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args612 = frozenset([2])
    FOLLOW_vars_hint_in_proc_args614 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars659 = frozenset([2])
    FOLLOW_vars_hint_in_proc_vars661 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements716 = frozenset([2])
    FOLLOW_statement_in_statements720 = frozenset([3, 55, 56, 59, 60])
    FOLLOW_statement_call_in_statement776 = frozenset([1])
    FOLLOW_statement_if_in_statement800 = frozenset([1])
    FOLLOW_statement_assign_in_statement824 = frozenset([1])
    FOLLOW_statement_with_in_statement848 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with891 = frozenset([2])
    FOLLOW_ID_in_statement_with893 = frozenset([54])
    FOLLOW_statements_in_statement_with895 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign936 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign938 = frozenset([19])
    FOLLOW_ID_in_statement_assign968 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1051 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if1067 = frozenset([3, 57, 58])
    FOLLOW_statement_else_in_statement_if1117 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1190 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif1192 = frozenset([54])
    FOLLOW_statements_in_statement_elif1194 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1222 = frozenset([2])
    FOLLOW_condition_all_in_statement_elif1224 = frozenset([54])
    FOLLOW_statements_in_statement_elif1226 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1271 = frozenset([2])
    FOLLOW_statements_in_statement_else1273 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1328 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1344 = frozenset([3, 56])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1419 = frozenset([2])
    FOLLOW_statement_call_in_condition_all1435 = frozenset([3, 56])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1500 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call1502 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args1557 = frozenset([1, 18, 19, 23, 26])
    FOLLOW_ID_in_arbitrary_value1610 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1622 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1634 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1646 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1687 = frozenset([2])
    FOLLOW_ID_in_consts1689 = frozenset([41, 45, 46])
    FOLLOW_consts_items_in_consts1691 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1746 = frozenset([1, 41, 45, 46])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1801 = frozenset([2])
    FOLLOW_ID_in_consts_item1803 = frozenset([23, 26])
    FOLLOW_num_whole_in_consts_item1805 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1833 = frozenset([2])
    FOLLOW_ID_in_consts_item1835 = frozenset([23, 26])
    FOLLOW_num_fract_in_consts_item1837 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1865 = frozenset([2])
    FOLLOW_ID_in_consts_item1867 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1869 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1924 = frozenset([2])
    FOLLOW_ID_in_types1926 = frozenset([62])
    FOLLOW_types_items_in_types1928 = frozenset([3])
    FOLLOW_types_item_in_types_items1983 = frozenset([1, 62])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2038 = frozenset([2])
    FOLLOW_ID_in_types_item2040 = frozenset([64])
    FOLLOW_vars_hint_in_types_item2042 = frozenset([3])
    FOLLOW_TREE_VARS_HINT_in_vars_hint2095 = frozenset([1, 65])
    FOLLOW_var_hint_in_vars_hint2099 = frozenset([1, 65])
    FOLLOW_TREE_VAR_HINT_in_var_hint2144 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_var_hint2146 = frozenset([63])
    FOLLOW_var_in_var_hint2150 = frozenset([3, 63])
    FOLLOW_TREE_VAR_HINT_in_var_hint2190 = frozenset([2])
    FOLLOW_hint_in_var_hint2192 = frozenset([63])
    FOLLOW_var_in_var_hint2196 = frozenset([3, 63])
    FOLLOW_TREE_VAR_in_var2253 = frozenset([2])
    FOLLOW_ID_in_var2255 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2298 = frozenset([2])
    FOLLOW_ID_in_hint2300 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2328 = frozenset([2])
    FOLLOW_ID_in_hint2330 = frozenset([19, 67])
    FOLLOW_hint_args_in_hint2332 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2387 = frozenset([1, 19, 67])
    FOLLOW_ID_in_hint_arg2420 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2432 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2463 = frozenset([26])
    FOLLOW_NUMBER_in_num_whole2465 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2493 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2538 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2544 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2546 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2552 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2584 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2586 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2592 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
