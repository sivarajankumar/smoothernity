# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-24 15:12:04

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
ARGS=4
ARROW_LEFT=5
ARROW_RIGHT=6
CONSTS=7
COPY=8
CURLY_CLOSE=9
CURLY_OPEN=10
DEDENT=11
DIVIDE=12
DO=13
EXPRESSION=14
ID=15
IF=16
INDENT=17
MINUS=18
MODULE=19
NEWLINE=20
NUMBER=21
OPS=22
PASTE=23
PROC=24
REPLACE=25
STATELESS=26
STRING=27
TREE_ARBITRARY_TOKEN=28
TREE_CONDITION_ANY=29
TREE_CONSTS=30
TREE_COPY=31
TREE_COPY_PASTE=32
TREE_EXPRESSION=33
TREE_HINT=34
TREE_HINT_NONE=35
TREE_MODULE=36
TREE_NUM_FRACT=37
TREE_NUM_WHOLE=38
TREE_PASTE=39
TREE_PASTE_REPLACE=40
TREE_PASTE_WITH=41
TREE_PROC=42
TREE_PROC_ARGS=43
TREE_PROC_VARS=44
TREE_STATELESS=45
TREE_STATEMENTS=46
TREE_STATEMENT_CALL=47
TREE_STATEMENT_CALL_ARGS=48
TREE_STATEMENT_ELIF=49
TREE_STATEMENT_IF=50
TREE_TYPES=51
TREE_TYPES_ITEM=52
TREE_VAR=53
TREE_VARS_HINT=54
TREE_VAR_HINT=55
TYPES=56
UNDERSCORE=57
VARS=58
WHITESPACE=59
WITH=60

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "EXPRESSION", "ID", "IF", "INDENT", 
    "MINUS", "MODULE", "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", 
    "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_IF", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VAR", "TREE_VARS_HINT", 
    "TREE_VAR_HINT", "TYPES", "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
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

                    if (LA7_0 == TREE_STATEMENT_CALL or LA7_0 == TREE_STATEMENT_IF) :
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
    # grammar/ShyRecognizerBackend.g:105:1: statement returns [ value ] : ( statement_call | statement_if );
    def statement(self, ):
        value = None


        statement_call17 = None

        statement_if18 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:107:5: ( statement_call | statement_if )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == TREE_STATEMENT_CALL) :
                    alt8 = 1
                elif (LA8_0 == TREE_STATEMENT_IF) :
                    alt8 = 2
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




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerBackend.g:113:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( statement_elif )+ ) ;
    def statement_if(self, ):
        value = None


        statement_elif19 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:116:5: ( ^( TREE_STATEMENT_IF ( statement_elif )+ ) )
                # grammar/ShyRecognizerBackend.g:116:9: ^( TREE_STATEMENT_IF ( statement_elif )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if853)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:117:13: ( statement_elif )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == TREE_STATEMENT_ELIF) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerBackend.g:117:15: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if869)
                        statement_elif19 = self.statement_elif()

                        self._state.following.pop()

                        #action start
                        value [ 'if' ] . append ( statement_elif19 ) 
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

    # $ANTLR end "statement_if"



    # $ANTLR start "statement_elif"
    # grammar/ShyRecognizerBackend.g:123:1: statement_elif returns [ value ] : ^( TREE_STATEMENT_ELIF condition_any statements ) ;
    def statement_elif(self, ):
        value = None


        condition_any20 = None

        statements21 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:125:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) )
                # grammar/ShyRecognizerBackend.g:125:9: ^( TREE_STATEMENT_ELIF condition_any statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif942)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_condition_any_in_statement_elif944)
                condition_any20 = self.condition_any()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_statements_in_statement_elif946)
                statements21 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = {
                   'any' : condition_any20 ,
                   'ops' : statements21 }
                            
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:132:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call22 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:135:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:135:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1001)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:136:13: ( statement_call )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_STATEMENT_CALL) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:136:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1017)
                        statement_call22 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call22 ) 
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

    # $ANTLR end "condition_any"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:141:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL ID statement_call_args ) ;
    def statement_call(self, ):
        value = None


        ID23 = None
        statement_call_args24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:143:5: ( ^( TREE_STATEMENT_CALL ID statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:143:9: ^( TREE_STATEMENT_CALL ID statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1082)

                self.match(self.input, DOWN, None)
                ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call1084)

                self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1086)
                statement_call_args24 = self.statement_call_args()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { ID23.text : statement_call_args24 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:147:1: statement_call_args returns [ value ] : TREE_STATEMENT_CALL_ARGS ( statement_call_arg )* ;
    def statement_call_args(self, ):
        value = None


        statement_call_arg25 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:150:5: ( TREE_STATEMENT_CALL_ARGS ( statement_call_arg )* )
                # grammar/ShyRecognizerBackend.g:150:9: TREE_STATEMENT_CALL_ARGS ( statement_call_arg )*
                pass 
                self.match(self.input, TREE_STATEMENT_CALL_ARGS, self.FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args1139)

                # grammar/ShyRecognizerBackend.g:151:13: ( statement_call_arg )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA11_0 <= ID) or LA11_0 == MINUS or LA11_0 == NUMBER) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:151:15: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1156)
                        statement_call_arg25 = self.statement_call_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call_arg25 ) 
                        #action end



                    else:
                        break #loop11





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerBackend.g:156:1: statement_call_arg returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        value = None


        ID26 = None
        EXPRESSION27 = None
        num_whole28 = None

        num_fract29 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:158:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt12 = 4
                LA12 = self.input.LA(1)
                if LA12 == ID:
                    alt12 = 1
                elif LA12 == EXPRESSION:
                    alt12 = 2
                elif LA12 == MINUS:
                    LA12_3 = self.input.LA(2)

                    if (LA12_3 == NUMBER) :
                        LA12_5 = self.input.LA(3)

                        if (LA12_5 == DIVIDE) :
                            alt12 = 4
                        elif (LA12_5 == 3 or (EXPRESSION <= LA12_5 <= ID) or LA12_5 == MINUS or LA12_5 == NUMBER) :
                            alt12 = 3
                        else:
                            nvae = NoViableAltException("", 12, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 12, 3, self.input)

                        raise nvae


                elif LA12 == NUMBER:
                    LA12_4 = self.input.LA(2)

                    if (LA12_4 == DIVIDE) :
                        alt12 = 4
                    elif (LA12_4 == 3 or (EXPRESSION <= LA12_4 <= ID) or LA12_4 == MINUS or LA12_4 == NUMBER) :
                        alt12 = 3
                    else:
                        nvae = NoViableAltException("", 12, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:158:9: ID
                    pass 
                    ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1217)

                    #action start
                    value = { ID26.text : { } } 
                    #action end



                elif alt12 == 2:
                    # grammar/ShyRecognizerBackend.g:159:9: EXPRESSION
                    pass 
                    EXPRESSION27 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1229)

                    #action start
                    value = EXPRESSION27.text 
                    #action end



                elif alt12 == 3:
                    # grammar/ShyRecognizerBackend.g:160:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1241)
                    num_whole28 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole28 
                    #action end



                elif alt12 == 4:
                    # grammar/ShyRecognizerBackend.g:161:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1253)
                    num_fract29 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract29 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_arg"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:164:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID30 = None
        consts_items31 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:167:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:167:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1294)

                self.match(self.input, DOWN, None)
                ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1296)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1298)
                consts_items31 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID30.text , consts_items31 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:171:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item32 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:174:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:174:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:174:9: ( consts_item )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA13_0 <= TREE_NUM_WHOLE)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:174:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1353)
                        consts_item32 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item32 is not None) and [consts_item32.name] or [None])[0] ] = ((consts_item32 is not None) and [consts_item32.value] or [None])[0] 
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

    # $ANTLR end "consts_items"


    class consts_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerBackend.g:179:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID33 = None
        ID35 = None
        ID37 = None
        EXPRESSION38 = None
        num_whole34 = None

        num_fract36 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:181:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt14 = 3
                LA14 = self.input.LA(1)
                if LA14 == TREE_NUM_WHOLE:
                    alt14 = 1
                elif LA14 == TREE_NUM_FRACT:
                    alt14 = 2
                elif LA14 == TREE_EXPRESSION:
                    alt14 = 3
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyRecognizerBackend.g:181:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1408)

                    self.match(self.input, DOWN, None)
                    ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1410)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1412)
                    num_whole34 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID33.text , num_whole34 
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:183:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1440)

                    self.match(self.input, DOWN, None)
                    ID35 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1442)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1444)
                    num_fract36 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID35.text , num_fract36 
                    #action end



                elif alt14 == 3:
                    # grammar/ShyRecognizerBackend.g:185:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1472)

                    self.match(self.input, DOWN, None)
                    ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1474)

                    EXPRESSION38 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1476)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID37.text , EXPRESSION38.text 
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
    # grammar/ShyRecognizerBackend.g:189:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID39 = None
        types_items40 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:192:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:192:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1531)

                self.match(self.input, DOWN, None)
                ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_types1533)

                self._state.following.append(self.FOLLOW_types_items_in_types1535)
                types_items40 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID39.text , types_items40 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:196:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item41 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:199:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:199:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:199:9: ( types_item )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == TREE_TYPES_ITEM) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:199:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1590)
                        types_item41 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item41 is not None) and [types_item41.name] or [None])[0] ] = ((types_item41 is not None) and [types_item41.value] or [None])[0] 
                        #action end



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1





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
    # grammar/ShyRecognizerBackend.g:204:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID42 = None
        vars_hint43 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:206:5: ( ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerBackend.g:206:9: ^( TREE_TYPES_ITEM ID vars_hint )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item1645)

                self.match(self.input, DOWN, None)
                ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1647)

                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1649)
                vars_hint43 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID42.text , vars_hint43 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerBackend.g:210:1: vars_hint returns [ value ] : TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        value = None


        var_hint44 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:213:5: ( TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerBackend.g:213:9: TREE_VARS_HINT ( var_hint )*
                pass 
                self.match(self.input, TREE_VARS_HINT, self.FOLLOW_TREE_VARS_HINT_in_vars_hint1702)

                # grammar/ShyRecognizerBackend.g:213:24: ( var_hint )*
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == TREE_VAR_HINT) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:213:26: var_hint
                        pass 
                        self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1706)
                        var_hint44 = self.var_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( var_hint44 ) 
                        #action end



                    else:
                        break #loop16





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "vars_hint"



    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerBackend.g:216:1: var_hint returns [ value ] : ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        value = None


        var45 = None

        var46 = None

        hint47 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:219:5: ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == TREE_VAR_HINT) :
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == 2) :
                        LA19_2 = self.input.LA(3)

                        if (LA19_2 == TREE_HINT_NONE) :
                            alt19 = 1
                        elif (LA19_2 == TREE_HINT) :
                            alt19 = 2
                        else:
                            nvae = NoViableAltException("", 19, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 19, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:219:9: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1751)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_var_hint1753)

                    # grammar/ShyRecognizerBackend.g:219:41: ( var )+
                    cnt17 = 0
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == TREE_VAR) :
                            alt17 = 1


                        if alt17 == 1:
                            # grammar/ShyRecognizerBackend.g:219:43: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1757)
                            var45 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var45 ] = dict ( ) 
                            #action end



                        else:
                            if cnt17 >= 1:
                                break #loop17

                            eee = EarlyExitException(17, self.input)
                            raise eee

                        cnt17 += 1


                    self.match(self.input, UP, None)



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:222:9: ^( TREE_VAR_HINT hint ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1797)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1799)
                    hint47 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:222:31: ( var )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == TREE_VAR) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerBackend.g:222:33: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1803)
                            var46 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var46 ] = hint47 
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

    # $ANTLR end "var_hint"



    # $ANTLR start "var"
    # grammar/ShyRecognizerBackend.g:227:1: var returns [ value ] : ^( TREE_VAR ID ) ;
    def var(self, ):
        value = None


        ID48 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:229:5: ( ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerBackend.g:229:9: ^( TREE_VAR ID )
                pass 
                self.match(self.input, TREE_VAR, self.FOLLOW_TREE_VAR_in_var1860)

                self.match(self.input, DOWN, None)
                ID48 = self.match(self.input, ID, self.FOLLOW_ID_in_var1862)

                self.match(self.input, UP, None)


                #action start
                value = ID48.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:232:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID49 = None
        ID50 = None
        hint_args51 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:235:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == TREE_HINT) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == 2) :
                        LA20_2 = self.input.LA(3)

                        if (LA20_2 == ID) :
                            LA20_3 = self.input.LA(4)

                            if (LA20_3 == 3) :
                                alt20 = 1
                            elif (LA20_3 == ID or LA20_3 == UNDERSCORE) :
                                alt20 = 2
                            else:
                                nvae = NoViableAltException("", 20, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 20, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammar/ShyRecognizerBackend.g:235:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1905)

                    self.match(self.input, DOWN, None)
                    ID49 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1907)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID49.text ] = list ( ) 
                    #action end



                elif alt20 == 2:
                    # grammar/ShyRecognizerBackend.g:237:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1935)

                    self.match(self.input, DOWN, None)
                    ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1937)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint1939)
                    hint_args51 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID50.text ] = hint_args51 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:241:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg52 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:244:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:244:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:244:9: ( hint_arg )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == ID or LA21_0 == UNDERSCORE) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:244:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args1994)
                        hint_arg52 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg52 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:247:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID53 = None
        UNDERSCORE54 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:249:5: ( ID | UNDERSCORE )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == ID) :
                    alt22 = 1
                elif (LA22_0 == UNDERSCORE) :
                    alt22 = 2
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # grammar/ShyRecognizerBackend.g:249:9: ID
                    pass 
                    ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2027)

                    #action start
                    value = ID53.text 
                    #action end



                elif alt22 == 2:
                    # grammar/ShyRecognizerBackend.g:250:9: UNDERSCORE
                    pass 
                    UNDERSCORE54 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2039)

                    #action start
                    value = UNDERSCORE54.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:253:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS55 = None
        NUMBER56 = None
        NUMBER57 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:255:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == MINUS) :
                    alt23 = 1
                elif (LA23_0 == NUMBER) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerBackend.g:255:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:255:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:255:11: MINUS NUMBER
                    pass 
                    MINUS55 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2070)

                    NUMBER56 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2072)




                    #action start
                    value = int ( MINUS55.text + NUMBER56.text ) 
                    #action end



                elif alt23 == 2:
                    # grammar/ShyRecognizerBackend.g:257:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:257:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:257:11: NUMBER
                    pass 
                    NUMBER57 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2100)




                    #action start
                    value = int ( NUMBER57.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:261:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS58 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:263:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == MINUS) :
                    alt24 = 1
                elif (LA24_0 == NUMBER) :
                    alt24 = 2
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerBackend.g:263:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:263:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:263:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS58 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2145)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2151)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2153)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2159)




                    #action start
                                
                    value = Fraction ( int ( MINUS58.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:268:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:268:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:268:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2191)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2193)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2199)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 30, 36, 45, 51])
    FOLLOW_stateless_in_start114 = frozenset([1, 30, 36, 45, 51])
    FOLLOW_consts_in_start141 = frozenset([1, 30, 36, 45, 51])
    FOLLOW_types_in_start167 = frozenset([1, 30, 36, 45, 51])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless287 = frozenset([2])
    FOLLOW_ID_in_stateless289 = frozenset([42])
    FOLLOW_procs_in_stateless291 = frozenset([3])
    FOLLOW_proc_in_procs346 = frozenset([1, 42])
    FOLLOW_TREE_PROC_in_proc391 = frozenset([2])
    FOLLOW_ID_in_proc405 = frozenset([3, 43, 44, 46])
    FOLLOW_proc_args_in_proc439 = frozenset([3, 44, 46])
    FOLLOW_proc_vars_in_proc489 = frozenset([3, 46])
    FOLLOW_statements_in_proc539 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args612 = frozenset([2])
    FOLLOW_vars_hint_in_proc_args614 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars659 = frozenset([2])
    FOLLOW_vars_hint_in_proc_vars661 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements716 = frozenset([2])
    FOLLOW_statement_in_statements720 = frozenset([3, 47, 50])
    FOLLOW_statement_call_in_statement776 = frozenset([1])
    FOLLOW_statement_if_in_statement800 = frozenset([1])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if853 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if869 = frozenset([3, 49])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif942 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif944 = frozenset([46])
    FOLLOW_statements_in_statement_elif946 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1001 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1017 = frozenset([3, 47])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1082 = frozenset([2])
    FOLLOW_ID_in_statement_call1084 = frozenset([48])
    FOLLOW_statement_call_args_in_statement_call1086 = frozenset([3])
    FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args1139 = frozenset([1, 14, 15, 18, 21])
    FOLLOW_statement_call_arg_in_statement_call_args1156 = frozenset([1, 14, 15, 18, 21])
    FOLLOW_ID_in_statement_call_arg1217 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1229 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1241 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1253 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1294 = frozenset([2])
    FOLLOW_ID_in_consts1296 = frozenset([33, 37, 38])
    FOLLOW_consts_items_in_consts1298 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1353 = frozenset([1, 33, 37, 38])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1408 = frozenset([2])
    FOLLOW_ID_in_consts_item1410 = frozenset([18, 21])
    FOLLOW_num_whole_in_consts_item1412 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1440 = frozenset([2])
    FOLLOW_ID_in_consts_item1442 = frozenset([18, 21])
    FOLLOW_num_fract_in_consts_item1444 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1472 = frozenset([2])
    FOLLOW_ID_in_consts_item1474 = frozenset([14])
    FOLLOW_EXPRESSION_in_consts_item1476 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1531 = frozenset([2])
    FOLLOW_ID_in_types1533 = frozenset([52])
    FOLLOW_types_items_in_types1535 = frozenset([3])
    FOLLOW_types_item_in_types_items1590 = frozenset([1, 52])
    FOLLOW_TREE_TYPES_ITEM_in_types_item1645 = frozenset([2])
    FOLLOW_ID_in_types_item1647 = frozenset([54])
    FOLLOW_vars_hint_in_types_item1649 = frozenset([3])
    FOLLOW_TREE_VARS_HINT_in_vars_hint1702 = frozenset([1, 55])
    FOLLOW_var_hint_in_vars_hint1706 = frozenset([1, 55])
    FOLLOW_TREE_VAR_HINT_in_var_hint1751 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_var_hint1753 = frozenset([53])
    FOLLOW_var_in_var_hint1757 = frozenset([3, 53])
    FOLLOW_TREE_VAR_HINT_in_var_hint1797 = frozenset([2])
    FOLLOW_hint_in_var_hint1799 = frozenset([53])
    FOLLOW_var_in_var_hint1803 = frozenset([3, 53])
    FOLLOW_TREE_VAR_in_var1860 = frozenset([2])
    FOLLOW_ID_in_var1862 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1905 = frozenset([2])
    FOLLOW_ID_in_hint1907 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1935 = frozenset([2])
    FOLLOW_ID_in_hint1937 = frozenset([15, 57])
    FOLLOW_hint_args_in_hint1939 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args1994 = frozenset([1, 15, 57])
    FOLLOW_ID_in_hint_arg2027 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2039 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2070 = frozenset([21])
    FOLLOW_NUMBER_in_num_whole2072 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2100 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2145 = frozenset([21])
    FOLLOW_NUMBER_in_num_fract2151 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract2153 = frozenset([21])
    FOLLOW_NUMBER_in_num_fract2159 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2191 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract2193 = frozenset([21])
    FOLLOW_NUMBER_in_num_fract2199 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
