# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-24 20:23:55

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
ELIF=14
ELSE=15
EXPRESSION=16
ID=17
IF=18
INDENT=19
MINUS=20
MODULE=21
NEWLINE=22
NUMBER=23
OPS=24
PASTE=25
PROC=26
REPLACE=27
STATELESS=28
STRING=29
TREE_ARBITRARY_TOKEN=30
TREE_CONDITION_ANY=31
TREE_CONSTS=32
TREE_COPY=33
TREE_COPY_PASTE=34
TREE_EXPRESSION=35
TREE_HINT=36
TREE_HINT_NONE=37
TREE_MODULE=38
TREE_NUM_FRACT=39
TREE_NUM_WHOLE=40
TREE_PASTE=41
TREE_PASTE_REPLACE=42
TREE_PASTE_WITH=43
TREE_PROC=44
TREE_PROC_ARGS=45
TREE_PROC_VARS=46
TREE_STATELESS=47
TREE_STATEMENTS=48
TREE_STATEMENT_CALL=49
TREE_STATEMENT_CALL_ARGS=50
TREE_STATEMENT_ELIF=51
TREE_STATEMENT_ELSE=52
TREE_STATEMENT_IF=53
TREE_TYPES=54
TREE_TYPES_ITEM=55
TREE_VAR=56
TREE_VARS_HINT=57
TREE_VAR_HINT=58
TYPES=59
UNDERSCORE=60
VARS=61
WHITESPACE=62
WITH=63

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", "EXPRESSION", 
    "ID", "IF", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", "OPS", 
    "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", 
    "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_TYPES", "TREE_TYPES_ITEM", 
    "TREE_VAR", "TREE_VARS_HINT", "TREE_VAR_HINT", "TYPES", "UNDERSCORE", 
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
    # grammar/ShyRecognizerBackend.g:113:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) ;
    def statement_if(self, ):
        value = None


        statement_elif19 = None

        statement_else20 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:116:5: ( ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) )
                # grammar/ShyRecognizerBackend.g:116:9: ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? )
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


                # grammar/ShyRecognizerBackend.g:120:13: ( statement_else )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == TREE_STATEMENT_ELSE) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerBackend.g:120:15: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if919)
                    statement_else20 = self.statement_else()

                    self._state.following.pop()

                    #action start
                    value [ 'else' ] = statement_else20 
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
    # grammar/ShyRecognizerBackend.g:126:1: statement_elif returns [ value ] : ^( TREE_STATEMENT_ELIF condition_any statements ) ;
    def statement_elif(self, ):
        value = None


        condition_any21 = None

        statements22 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:128:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) )
                # grammar/ShyRecognizerBackend.g:128:9: ^( TREE_STATEMENT_ELIF condition_any statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif992)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_condition_any_in_statement_elif994)
                condition_any21 = self.condition_any()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_statements_in_statement_elif996)
                statements22 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = {
                   'any' : condition_any21 ,
                   'ops' : statements22 }
                            
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerBackend.g:135:1: statement_else returns [ value ] : ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        value = None


        statements23 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:137:5: ( ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerBackend.g:137:9: ^( TREE_STATEMENT_ELSE statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1041)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statements_in_statement_else1043)
                statements23 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = statements23 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_else"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:141:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call24 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:144:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:144:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1098)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:145:13: ( statement_call )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == TREE_STATEMENT_CALL) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:145:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1114)
                        statement_call24 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call24 ) 
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

    # $ANTLR end "condition_any"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:150:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL ID statement_call_args ) ;
    def statement_call(self, ):
        value = None


        ID25 = None
        statement_call_args26 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:152:5: ( ^( TREE_STATEMENT_CALL ID statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:152:9: ^( TREE_STATEMENT_CALL ID statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1179)

                self.match(self.input, DOWN, None)
                ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call1181)

                self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1183)
                statement_call_args26 = self.statement_call_args()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { ID25.text : statement_call_args26 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:156:1: statement_call_args returns [ value ] : TREE_STATEMENT_CALL_ARGS ( statement_call_arg )* ;
    def statement_call_args(self, ):
        value = None


        statement_call_arg27 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:159:5: ( TREE_STATEMENT_CALL_ARGS ( statement_call_arg )* )
                # grammar/ShyRecognizerBackend.g:159:9: TREE_STATEMENT_CALL_ARGS ( statement_call_arg )*
                pass 
                self.match(self.input, TREE_STATEMENT_CALL_ARGS, self.FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args1236)

                # grammar/ShyRecognizerBackend.g:160:13: ( statement_call_arg )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA12_0 <= ID) or LA12_0 == MINUS or LA12_0 == NUMBER) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerBackend.g:160:15: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1253)
                        statement_call_arg27 = self.statement_call_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call_arg27 ) 
                        #action end



                    else:
                        break #loop12





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerBackend.g:165:1: statement_call_arg returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        value = None


        ID28 = None
        EXPRESSION29 = None
        num_whole30 = None

        num_fract31 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:167:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt13 = 4
                LA13 = self.input.LA(1)
                if LA13 == ID:
                    alt13 = 1
                elif LA13 == EXPRESSION:
                    alt13 = 2
                elif LA13 == MINUS:
                    LA13_3 = self.input.LA(2)

                    if (LA13_3 == NUMBER) :
                        LA13_5 = self.input.LA(3)

                        if (LA13_5 == DIVIDE) :
                            alt13 = 4
                        elif (LA13_5 == 3 or (EXPRESSION <= LA13_5 <= ID) or LA13_5 == MINUS or LA13_5 == NUMBER) :
                            alt13 = 3
                        else:
                            nvae = NoViableAltException("", 13, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 13, 3, self.input)

                        raise nvae


                elif LA13 == NUMBER:
                    LA13_4 = self.input.LA(2)

                    if (LA13_4 == DIVIDE) :
                        alt13 = 4
                    elif (LA13_4 == 3 or (EXPRESSION <= LA13_4 <= ID) or LA13_4 == MINUS or LA13_4 == NUMBER) :
                        alt13 = 3
                    else:
                        nvae = NoViableAltException("", 13, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # grammar/ShyRecognizerBackend.g:167:9: ID
                    pass 
                    ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1314)

                    #action start
                    value = { ID28.text : { } } 
                    #action end



                elif alt13 == 2:
                    # grammar/ShyRecognizerBackend.g:168:9: EXPRESSION
                    pass 
                    EXPRESSION29 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1326)

                    #action start
                    value = EXPRESSION29.text 
                    #action end



                elif alt13 == 3:
                    # grammar/ShyRecognizerBackend.g:169:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1338)
                    num_whole30 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole30 
                    #action end



                elif alt13 == 4:
                    # grammar/ShyRecognizerBackend.g:170:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1350)
                    num_fract31 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract31 
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
    # grammar/ShyRecognizerBackend.g:173:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID32 = None
        consts_items33 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:176:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:176:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1391)

                self.match(self.input, DOWN, None)
                ID32 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1393)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1395)
                consts_items33 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID32.text , consts_items33 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:180:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item34 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:183:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:183:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:183:9: ( consts_item )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA14_0 <= TREE_NUM_WHOLE)) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:183:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1450)
                        consts_item34 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item34 is not None) and [consts_item34.name] or [None])[0] ] = ((consts_item34 is not None) and [consts_item34.value] or [None])[0] 
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

    # $ANTLR end "consts_items"


    class consts_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerBackend.g:188:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID35 = None
        ID37 = None
        ID39 = None
        EXPRESSION40 = None
        num_whole36 = None

        num_fract38 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:190:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt15 = 3
                LA15 = self.input.LA(1)
                if LA15 == TREE_NUM_WHOLE:
                    alt15 = 1
                elif LA15 == TREE_NUM_FRACT:
                    alt15 = 2
                elif LA15 == TREE_EXPRESSION:
                    alt15 = 3
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:190:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1505)

                    self.match(self.input, DOWN, None)
                    ID35 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1507)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1509)
                    num_whole36 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID35.text , num_whole36 
                    #action end



                elif alt15 == 2:
                    # grammar/ShyRecognizerBackend.g:192:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1537)

                    self.match(self.input, DOWN, None)
                    ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1539)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1541)
                    num_fract38 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID37.text , num_fract38 
                    #action end



                elif alt15 == 3:
                    # grammar/ShyRecognizerBackend.g:194:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1569)

                    self.match(self.input, DOWN, None)
                    ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1571)

                    EXPRESSION40 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1573)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID39.text , EXPRESSION40.text 
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
    # grammar/ShyRecognizerBackend.g:198:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID41 = None
        types_items42 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:201:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:201:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1628)

                self.match(self.input, DOWN, None)
                ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_types1630)

                self._state.following.append(self.FOLLOW_types_items_in_types1632)
                types_items42 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID41.text , types_items42 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:205:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item43 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:208:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:208:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:208:9: ( types_item )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == TREE_TYPES_ITEM) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:208:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1687)
                        types_item43 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item43 is not None) and [types_item43.name] or [None])[0] ] = ((types_item43 is not None) and [types_item43.value] or [None])[0] 
                        #action end



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1





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
    # grammar/ShyRecognizerBackend.g:213:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID44 = None
        vars_hint45 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:215:5: ( ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerBackend.g:215:9: ^( TREE_TYPES_ITEM ID vars_hint )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item1742)

                self.match(self.input, DOWN, None)
                ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1744)

                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1746)
                vars_hint45 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID44.text , vars_hint45 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerBackend.g:219:1: vars_hint returns [ value ] : TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        value = None


        var_hint46 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:222:5: ( TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerBackend.g:222:9: TREE_VARS_HINT ( var_hint )*
                pass 
                self.match(self.input, TREE_VARS_HINT, self.FOLLOW_TREE_VARS_HINT_in_vars_hint1799)

                # grammar/ShyRecognizerBackend.g:222:24: ( var_hint )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_VAR_HINT) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:222:26: var_hint
                        pass 
                        self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1803)
                        var_hint46 = self.var_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( var_hint46 ) 
                        #action end



                    else:
                        break #loop17





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "vars_hint"



    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerBackend.g:225:1: var_hint returns [ value ] : ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        value = None


        var47 = None

        var48 = None

        hint49 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:228:5: ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == TREE_VAR_HINT) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == 2) :
                        LA20_2 = self.input.LA(3)

                        if (LA20_2 == TREE_HINT_NONE) :
                            alt20 = 1
                        elif (LA20_2 == TREE_HINT) :
                            alt20 = 2
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
                    # grammar/ShyRecognizerBackend.g:228:9: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1848)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_var_hint1850)

                    # grammar/ShyRecognizerBackend.g:228:41: ( var )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == TREE_VAR) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerBackend.g:228:43: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1854)
                            var47 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var47 ] = dict ( ) 
                            #action end



                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


                    self.match(self.input, UP, None)



                elif alt20 == 2:
                    # grammar/ShyRecognizerBackend.g:231:9: ^( TREE_VAR_HINT hint ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1894)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1896)
                    hint49 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:231:31: ( var )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == TREE_VAR) :
                            alt19 = 1


                        if alt19 == 1:
                            # grammar/ShyRecognizerBackend.g:231:33: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1900)
                            var48 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var48 ] = hint49 
                            #action end



                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1


                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var_hint"



    # $ANTLR start "var"
    # grammar/ShyRecognizerBackend.g:236:1: var returns [ value ] : ^( TREE_VAR ID ) ;
    def var(self, ):
        value = None


        ID50 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:238:5: ( ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerBackend.g:238:9: ^( TREE_VAR ID )
                pass 
                self.match(self.input, TREE_VAR, self.FOLLOW_TREE_VAR_in_var1957)

                self.match(self.input, DOWN, None)
                ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_var1959)

                self.match(self.input, UP, None)


                #action start
                value = ID50.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:241:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID51 = None
        ID52 = None
        hint_args53 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:244:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == TREE_HINT) :
                    LA21_1 = self.input.LA(2)

                    if (LA21_1 == 2) :
                        LA21_2 = self.input.LA(3)

                        if (LA21_2 == ID) :
                            LA21_3 = self.input.LA(4)

                            if (LA21_3 == 3) :
                                alt21 = 1
                            elif (LA21_3 == ID or LA21_3 == UNDERSCORE) :
                                alt21 = 2
                            else:
                                nvae = NoViableAltException("", 21, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 21, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 21, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae


                if alt21 == 1:
                    # grammar/ShyRecognizerBackend.g:244:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2002)

                    self.match(self.input, DOWN, None)
                    ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2004)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID51.text ] = list ( ) 
                    #action end



                elif alt21 == 2:
                    # grammar/ShyRecognizerBackend.g:246:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2032)

                    self.match(self.input, DOWN, None)
                    ID52 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2034)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2036)
                    hint_args53 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID52.text ] = hint_args53 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:250:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg54 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:253:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:253:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:253:9: ( hint_arg )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == ID or LA22_0 == UNDERSCORE) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerBackend.g:253:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2091)
                        hint_arg54 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg54 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:256:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID55 = None
        UNDERSCORE56 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:258:5: ( ID | UNDERSCORE )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == ID) :
                    alt23 = 1
                elif (LA23_0 == UNDERSCORE) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerBackend.g:258:9: ID
                    pass 
                    ID55 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2124)

                    #action start
                    value = ID55.text 
                    #action end



                elif alt23 == 2:
                    # grammar/ShyRecognizerBackend.g:259:9: UNDERSCORE
                    pass 
                    UNDERSCORE56 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2136)

                    #action start
                    value = UNDERSCORE56.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:262:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS57 = None
        NUMBER58 = None
        NUMBER59 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:264:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:264:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:264:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:264:11: MINUS NUMBER
                    pass 
                    MINUS57 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2167)

                    NUMBER58 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2169)




                    #action start
                    value = int ( MINUS57.text + NUMBER58.text ) 
                    #action end



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:266:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:266:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:266:11: NUMBER
                    pass 
                    NUMBER59 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2197)




                    #action start
                    value = int ( NUMBER59.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:270:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS60 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:272:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == MINUS) :
                    alt25 = 1
                elif (LA25_0 == NUMBER) :
                    alt25 = 2
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # grammar/ShyRecognizerBackend.g:272:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:272:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:272:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS60 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2242)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2248)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2250)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2256)




                    #action start
                                
                    value = Fraction ( int ( MINUS60.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt25 == 2:
                    # grammar/ShyRecognizerBackend.g:277:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:277:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:277:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2288)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2290)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2296)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 32, 38, 47, 54])
    FOLLOW_stateless_in_start114 = frozenset([1, 32, 38, 47, 54])
    FOLLOW_consts_in_start141 = frozenset([1, 32, 38, 47, 54])
    FOLLOW_types_in_start167 = frozenset([1, 32, 38, 47, 54])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless287 = frozenset([2])
    FOLLOW_ID_in_stateless289 = frozenset([44])
    FOLLOW_procs_in_stateless291 = frozenset([3])
    FOLLOW_proc_in_procs346 = frozenset([1, 44])
    FOLLOW_TREE_PROC_in_proc391 = frozenset([2])
    FOLLOW_ID_in_proc405 = frozenset([3, 45, 46, 48])
    FOLLOW_proc_args_in_proc439 = frozenset([3, 46, 48])
    FOLLOW_proc_vars_in_proc489 = frozenset([3, 48])
    FOLLOW_statements_in_proc539 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args612 = frozenset([2])
    FOLLOW_vars_hint_in_proc_args614 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars659 = frozenset([2])
    FOLLOW_vars_hint_in_proc_vars661 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements716 = frozenset([2])
    FOLLOW_statement_in_statements720 = frozenset([3, 49, 53])
    FOLLOW_statement_call_in_statement776 = frozenset([1])
    FOLLOW_statement_if_in_statement800 = frozenset([1])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if853 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if869 = frozenset([3, 51, 52])
    FOLLOW_statement_else_in_statement_if919 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif992 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif994 = frozenset([48])
    FOLLOW_statements_in_statement_elif996 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1041 = frozenset([2])
    FOLLOW_statements_in_statement_else1043 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1098 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1114 = frozenset([3, 49])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1179 = frozenset([2])
    FOLLOW_ID_in_statement_call1181 = frozenset([50])
    FOLLOW_statement_call_args_in_statement_call1183 = frozenset([3])
    FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args1236 = frozenset([1, 16, 17, 20, 23])
    FOLLOW_statement_call_arg_in_statement_call_args1253 = frozenset([1, 16, 17, 20, 23])
    FOLLOW_ID_in_statement_call_arg1314 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1326 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1338 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1350 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1391 = frozenset([2])
    FOLLOW_ID_in_consts1393 = frozenset([35, 39, 40])
    FOLLOW_consts_items_in_consts1395 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1450 = frozenset([1, 35, 39, 40])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1505 = frozenset([2])
    FOLLOW_ID_in_consts_item1507 = frozenset([20, 23])
    FOLLOW_num_whole_in_consts_item1509 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1537 = frozenset([2])
    FOLLOW_ID_in_consts_item1539 = frozenset([20, 23])
    FOLLOW_num_fract_in_consts_item1541 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1569 = frozenset([2])
    FOLLOW_ID_in_consts_item1571 = frozenset([16])
    FOLLOW_EXPRESSION_in_consts_item1573 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1628 = frozenset([2])
    FOLLOW_ID_in_types1630 = frozenset([55])
    FOLLOW_types_items_in_types1632 = frozenset([3])
    FOLLOW_types_item_in_types_items1687 = frozenset([1, 55])
    FOLLOW_TREE_TYPES_ITEM_in_types_item1742 = frozenset([2])
    FOLLOW_ID_in_types_item1744 = frozenset([57])
    FOLLOW_vars_hint_in_types_item1746 = frozenset([3])
    FOLLOW_TREE_VARS_HINT_in_vars_hint1799 = frozenset([1, 58])
    FOLLOW_var_hint_in_vars_hint1803 = frozenset([1, 58])
    FOLLOW_TREE_VAR_HINT_in_var_hint1848 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_var_hint1850 = frozenset([56])
    FOLLOW_var_in_var_hint1854 = frozenset([3, 56])
    FOLLOW_TREE_VAR_HINT_in_var_hint1894 = frozenset([2])
    FOLLOW_hint_in_var_hint1896 = frozenset([56])
    FOLLOW_var_in_var_hint1900 = frozenset([3, 56])
    FOLLOW_TREE_VAR_in_var1957 = frozenset([2])
    FOLLOW_ID_in_var1959 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2002 = frozenset([2])
    FOLLOW_ID_in_hint2004 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2032 = frozenset([2])
    FOLLOW_ID_in_hint2034 = frozenset([17, 60])
    FOLLOW_hint_args_in_hint2036 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2091 = frozenset([1, 17, 60])
    FOLLOW_ID_in_hint_arg2124 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2136 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2167 = frozenset([23])
    FOLLOW_NUMBER_in_num_whole2169 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2197 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2242 = frozenset([23])
    FOLLOW_NUMBER_in_num_fract2248 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract2250 = frozenset([23])
    FOLLOW_NUMBER_in_num_fract2256 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2288 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract2290 = frozenset([23])
    FOLLOW_NUMBER_in_num_fract2296 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
