# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-26 19:29:49

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
MINUS=22
MODULE=23
NEWLINE=24
NUMBER=25
OPS=26
PASTE=27
PROC=28
REPLACE=29
STATELESS=30
STRING=31
TREE_ARBITRARY_TOKEN=32
TREE_CONDITION_ALL=33
TREE_CONDITION_ANY=34
TREE_CONSTS=35
TREE_COPY=36
TREE_COPY_PASTE=37
TREE_EXPRESSION=38
TREE_HINT=39
TREE_HINT_NONE=40
TREE_MODULE=41
TREE_NUM_FRACT=42
TREE_NUM_WHOLE=43
TREE_PASTE=44
TREE_PASTE_REPLACE=45
TREE_PASTE_WITH=46
TREE_PROC=47
TREE_PROC_ARGS=48
TREE_PROC_VARS=49
TREE_STATELESS=50
TREE_STATEMENTS=51
TREE_STATEMENT_CALL=52
TREE_STATEMENT_ELIF=53
TREE_STATEMENT_ELSE=54
TREE_STATEMENT_IF=55
TREE_TYPES=56
TREE_TYPES_ITEM=57
TREE_VAR=58
TREE_VARS_HINT=59
TREE_VAR_HINT=60
TYPES=61
UNDERSCORE=62
VARS=63
WHITESPACE=64
WITH=65

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", 
    "OPS", "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", 
    "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", 
    "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", 
    "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", 
    "TREE_PASTE_WITH", "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", 
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", 
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
    # grammar/ShyRecognizerBackend.g:126:1: statement_elif returns [ value ] : ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) );
    def statement_elif(self, ):
        value = None


        condition_any21 = None

        statements22 = None

        condition_all23 = None

        statements24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:128:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_STATEMENT_ELIF) :
                    LA11_1 = self.input.LA(2)

                    if (LA11_1 == 2) :
                        LA11_2 = self.input.LA(3)

                        if (LA11_2 == TREE_CONDITION_ANY) :
                            alt11 = 1
                        elif (LA11_2 == TREE_CONDITION_ALL) :
                            alt11 = 2
                        else:
                            nvae = NoViableAltException("", 11, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 11, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
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



                elif alt11 == 2:
                    # grammar/ShyRecognizerBackend.g:133:9: ^( TREE_STATEMENT_ELIF condition_all statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1024)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_all_in_statement_elif1026)
                    condition_all23 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1028)
                    statements24 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'all' : condition_all23 ,
                       'ops' : statements24 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerBackend.g:140:1: statement_else returns [ value ] : ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        value = None


        statements25 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:142:5: ( ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerBackend.g:142:9: ^( TREE_STATEMENT_ELSE statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1073)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statements_in_statement_else1075)
                statements25 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = statements25 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_else"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:146:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call26 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:149:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:149:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1130)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:150:13: ( statement_call )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == TREE_STATEMENT_CALL) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerBackend.g:150:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1146)
                        statement_call26 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call26 ) 
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

    # $ANTLR end "condition_any"



    # $ANTLR start "condition_all"
    # grammar/ShyRecognizerBackend.g:155:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call27 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:158:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:158:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1221)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:159:13: ( statement_call )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_STATEMENT_CALL) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:159:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all1237)
                        statement_call27 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call27 ) 
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

    # $ANTLR end "condition_all"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:164:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args28 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:166:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:166:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1302)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1304)
                    statement_call_args28 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args28 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:170:1: statement_call_args returns [ value ] : ( statement_call_arg )* ;
    def statement_call_args(self, ):
        value = None


        statement_call_arg29 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:173:5: ( ( statement_call_arg )* )
                # grammar/ShyRecognizerBackend.g:173:9: ( statement_call_arg )*
                pass 
                # grammar/ShyRecognizerBackend.g:173:9: ( statement_call_arg )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA14_0 <= ID) or LA14_0 == MINUS or LA14_0 == NUMBER) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:173:11: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1359)
                        statement_call_arg29 = self.statement_call_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call_arg29 ) 
                        #action end



                    else:
                        break #loop14





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerBackend.g:178:1: statement_call_arg returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        value = None


        ID30 = None
        EXPRESSION31 = None
        num_whole32 = None

        num_fract33 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:180:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt15 = 4
                LA15 = self.input.LA(1)
                if LA15 == ID:
                    alt15 = 1
                elif LA15 == EXPRESSION:
                    alt15 = 2
                elif LA15 == MINUS:
                    LA15_3 = self.input.LA(2)

                    if (LA15_3 == NUMBER) :
                        LA15_5 = self.input.LA(3)

                        if (LA15_5 == DIVIDE) :
                            alt15 = 4
                        elif (LA15_5 == 3 or (EXPRESSION <= LA15_5 <= ID) or LA15_5 == MINUS or LA15_5 == NUMBER) :
                            alt15 = 3
                        else:
                            nvae = NoViableAltException("", 15, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 15, 3, self.input)

                        raise nvae


                elif LA15 == NUMBER:
                    LA15_4 = self.input.LA(2)

                    if (LA15_4 == DIVIDE) :
                        alt15 = 4
                    elif (LA15_4 == 3 or (EXPRESSION <= LA15_4 <= ID) or LA15_4 == MINUS or LA15_4 == NUMBER) :
                        alt15 = 3
                    else:
                        nvae = NoViableAltException("", 15, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:180:9: ID
                    pass 
                    ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1412)

                    #action start
                    value = ID30.text 
                    #action end



                elif alt15 == 2:
                    # grammar/ShyRecognizerBackend.g:181:9: EXPRESSION
                    pass 
                    EXPRESSION31 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1424)

                    #action start
                    value = EXPRESSION31.text 
                    #action end



                elif alt15 == 3:
                    # grammar/ShyRecognizerBackend.g:182:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1436)
                    num_whole32 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole32 
                    #action end



                elif alt15 == 4:
                    # grammar/ShyRecognizerBackend.g:183:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1448)
                    num_fract33 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract33 
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
    # grammar/ShyRecognizerBackend.g:186:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID34 = None
        consts_items35 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:189:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:189:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1489)

                self.match(self.input, DOWN, None)
                ID34 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1491)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1493)
                consts_items35 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID34.text , consts_items35 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:193:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item36 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:196:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:196:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:196:9: ( consts_item )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA16_0 <= TREE_NUM_WHOLE)) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:196:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1548)
                        consts_item36 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item36 is not None) and [consts_item36.name] or [None])[0] ] = ((consts_item36 is not None) and [consts_item36.value] or [None])[0] 
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

    # $ANTLR end "consts_items"


    class consts_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerBackend.g:201:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID37 = None
        ID39 = None
        ID41 = None
        EXPRESSION42 = None
        num_whole38 = None

        num_fract40 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:203:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt17 = 3
                LA17 = self.input.LA(1)
                if LA17 == TREE_NUM_WHOLE:
                    alt17 = 1
                elif LA17 == TREE_NUM_FRACT:
                    alt17 = 2
                elif LA17 == TREE_EXPRESSION:
                    alt17 = 3
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerBackend.g:203:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1603)

                    self.match(self.input, DOWN, None)
                    ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1605)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1607)
                    num_whole38 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID37.text , num_whole38 
                    #action end



                elif alt17 == 2:
                    # grammar/ShyRecognizerBackend.g:205:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1635)

                    self.match(self.input, DOWN, None)
                    ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1637)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1639)
                    num_fract40 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID39.text , num_fract40 
                    #action end



                elif alt17 == 3:
                    # grammar/ShyRecognizerBackend.g:207:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1667)

                    self.match(self.input, DOWN, None)
                    ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1669)

                    EXPRESSION42 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1671)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID41.text , EXPRESSION42.text 
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
    # grammar/ShyRecognizerBackend.g:211:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID43 = None
        types_items44 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:214:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:214:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1726)

                self.match(self.input, DOWN, None)
                ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_types1728)

                self._state.following.append(self.FOLLOW_types_items_in_types1730)
                types_items44 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID43.text , types_items44 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:218:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item45 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:221:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:221:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:221:9: ( types_item )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == TREE_TYPES_ITEM) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerBackend.g:221:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1785)
                        types_item45 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item45 is not None) and [types_item45.name] or [None])[0] ] = ((types_item45 is not None) and [types_item45.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:226:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID46 = None
        vars_hint47 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:228:5: ( ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerBackend.g:228:9: ^( TREE_TYPES_ITEM ID vars_hint )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item1840)

                self.match(self.input, DOWN, None)
                ID46 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1842)

                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1844)
                vars_hint47 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID46.text , vars_hint47 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerBackend.g:232:1: vars_hint returns [ value ] : TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        value = None


        var_hint48 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:235:5: ( TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerBackend.g:235:9: TREE_VARS_HINT ( var_hint )*
                pass 
                self.match(self.input, TREE_VARS_HINT, self.FOLLOW_TREE_VARS_HINT_in_vars_hint1897)

                # grammar/ShyRecognizerBackend.g:235:24: ( var_hint )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == TREE_VAR_HINT) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerBackend.g:235:26: var_hint
                        pass 
                        self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1901)
                        var_hint48 = self.var_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( var_hint48 ) 
                        #action end



                    else:
                        break #loop19





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "vars_hint"



    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerBackend.g:238:1: var_hint returns [ value ] : ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        value = None


        var49 = None

        var50 = None

        hint51 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:241:5: ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == TREE_VAR_HINT) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == 2) :
                        LA22_2 = self.input.LA(3)

                        if (LA22_2 == TREE_HINT_NONE) :
                            alt22 = 1
                        elif (LA22_2 == TREE_HINT) :
                            alt22 = 2
                        else:
                            nvae = NoViableAltException("", 22, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # grammar/ShyRecognizerBackend.g:241:9: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1946)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_var_hint1948)

                    # grammar/ShyRecognizerBackend.g:241:41: ( var )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == TREE_VAR) :
                            alt20 = 1


                        if alt20 == 1:
                            # grammar/ShyRecognizerBackend.g:241:43: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1952)
                            var49 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var49 ] = dict ( ) 
                            #action end



                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


                    self.match(self.input, UP, None)



                elif alt22 == 2:
                    # grammar/ShyRecognizerBackend.g:244:9: ^( TREE_VAR_HINT hint ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1992)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1994)
                    hint51 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:244:31: ( var )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == TREE_VAR) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerBackend.g:244:33: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1998)
                            var50 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var50 ] = hint51 
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

    # $ANTLR end "var_hint"



    # $ANTLR start "var"
    # grammar/ShyRecognizerBackend.g:249:1: var returns [ value ] : ^( TREE_VAR ID ) ;
    def var(self, ):
        value = None


        ID52 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:251:5: ( ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerBackend.g:251:9: ^( TREE_VAR ID )
                pass 
                self.match(self.input, TREE_VAR, self.FOLLOW_TREE_VAR_in_var2055)

                self.match(self.input, DOWN, None)
                ID52 = self.match(self.input, ID, self.FOLLOW_ID_in_var2057)

                self.match(self.input, UP, None)


                #action start
                value = ID52.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:254:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID53 = None
        ID54 = None
        hint_args55 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:257:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == TREE_HINT) :
                    LA23_1 = self.input.LA(2)

                    if (LA23_1 == 2) :
                        LA23_2 = self.input.LA(3)

                        if (LA23_2 == ID) :
                            LA23_3 = self.input.LA(4)

                            if (LA23_3 == 3) :
                                alt23 = 1
                            elif (LA23_3 == ID or LA23_3 == UNDERSCORE) :
                                alt23 = 2
                            else:
                                nvae = NoViableAltException("", 23, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerBackend.g:257:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2100)

                    self.match(self.input, DOWN, None)
                    ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2102)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID53.text ] = list ( ) 
                    #action end



                elif alt23 == 2:
                    # grammar/ShyRecognizerBackend.g:259:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2130)

                    self.match(self.input, DOWN, None)
                    ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2132)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2134)
                    hint_args55 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID54.text ] = hint_args55 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:263:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg56 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:266:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:266:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:266:9: ( hint_arg )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ID or LA24_0 == UNDERSCORE) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerBackend.g:266:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2189)
                        hint_arg56 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg56 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:269:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID57 = None
        UNDERSCORE58 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:271:5: ( ID | UNDERSCORE )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == ID) :
                    alt25 = 1
                elif (LA25_0 == UNDERSCORE) :
                    alt25 = 2
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # grammar/ShyRecognizerBackend.g:271:9: ID
                    pass 
                    ID57 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2222)

                    #action start
                    value = ID57.text 
                    #action end



                elif alt25 == 2:
                    # grammar/ShyRecognizerBackend.g:272:9: UNDERSCORE
                    pass 
                    UNDERSCORE58 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2234)

                    #action start
                    value = UNDERSCORE58.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:275:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS59 = None
        NUMBER60 = None
        NUMBER61 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:277:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == MINUS) :
                    alt26 = 1
                elif (LA26_0 == NUMBER) :
                    alt26 = 2
                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # grammar/ShyRecognizerBackend.g:277:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:277:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:277:11: MINUS NUMBER
                    pass 
                    MINUS59 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2265)

                    NUMBER60 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2267)




                    #action start
                    value = int ( MINUS59.text + NUMBER60.text ) 
                    #action end



                elif alt26 == 2:
                    # grammar/ShyRecognizerBackend.g:279:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:279:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:279:11: NUMBER
                    pass 
                    NUMBER61 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2295)




                    #action start
                    value = int ( NUMBER61.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:283:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS62 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:285:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:285:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:285:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:285:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS62 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2340)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2346)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2348)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2354)




                    #action start
                                
                    value = Fraction ( int ( MINUS62.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt27 == 2:
                    # grammar/ShyRecognizerBackend.g:290:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:290:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:290:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2386)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2388)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2394)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 35, 41, 50, 56])
    FOLLOW_stateless_in_start114 = frozenset([1, 35, 41, 50, 56])
    FOLLOW_consts_in_start141 = frozenset([1, 35, 41, 50, 56])
    FOLLOW_types_in_start167 = frozenset([1, 35, 41, 50, 56])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless287 = frozenset([2])
    FOLLOW_ID_in_stateless289 = frozenset([47])
    FOLLOW_procs_in_stateless291 = frozenset([3])
    FOLLOW_proc_in_procs346 = frozenset([1, 47])
    FOLLOW_TREE_PROC_in_proc391 = frozenset([2])
    FOLLOW_ID_in_proc405 = frozenset([3, 48, 49, 51])
    FOLLOW_proc_args_in_proc439 = frozenset([3, 49, 51])
    FOLLOW_proc_vars_in_proc489 = frozenset([3, 51])
    FOLLOW_statements_in_proc539 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args612 = frozenset([2])
    FOLLOW_vars_hint_in_proc_args614 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars659 = frozenset([2])
    FOLLOW_vars_hint_in_proc_vars661 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements716 = frozenset([2])
    FOLLOW_statement_in_statements720 = frozenset([3, 52, 55])
    FOLLOW_statement_call_in_statement776 = frozenset([1])
    FOLLOW_statement_if_in_statement800 = frozenset([1])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if853 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if869 = frozenset([3, 53, 54])
    FOLLOW_statement_else_in_statement_if919 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif992 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif994 = frozenset([51])
    FOLLOW_statements_in_statement_elif996 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1024 = frozenset([2])
    FOLLOW_condition_all_in_statement_elif1026 = frozenset([51])
    FOLLOW_statements_in_statement_elif1028 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1073 = frozenset([2])
    FOLLOW_statements_in_statement_else1075 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1130 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1146 = frozenset([3, 52])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1221 = frozenset([2])
    FOLLOW_statement_call_in_condition_all1237 = frozenset([3, 52])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1302 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call1304 = frozenset([3])
    FOLLOW_statement_call_arg_in_statement_call_args1359 = frozenset([1, 18, 19, 22, 25])
    FOLLOW_ID_in_statement_call_arg1412 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1424 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1436 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1448 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1489 = frozenset([2])
    FOLLOW_ID_in_consts1491 = frozenset([38, 42, 43])
    FOLLOW_consts_items_in_consts1493 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1548 = frozenset([1, 38, 42, 43])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1603 = frozenset([2])
    FOLLOW_ID_in_consts_item1605 = frozenset([22, 25])
    FOLLOW_num_whole_in_consts_item1607 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1635 = frozenset([2])
    FOLLOW_ID_in_consts_item1637 = frozenset([22, 25])
    FOLLOW_num_fract_in_consts_item1639 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1667 = frozenset([2])
    FOLLOW_ID_in_consts_item1669 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1671 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1726 = frozenset([2])
    FOLLOW_ID_in_types1728 = frozenset([57])
    FOLLOW_types_items_in_types1730 = frozenset([3])
    FOLLOW_types_item_in_types_items1785 = frozenset([1, 57])
    FOLLOW_TREE_TYPES_ITEM_in_types_item1840 = frozenset([2])
    FOLLOW_ID_in_types_item1842 = frozenset([59])
    FOLLOW_vars_hint_in_types_item1844 = frozenset([3])
    FOLLOW_TREE_VARS_HINT_in_vars_hint1897 = frozenset([1, 60])
    FOLLOW_var_hint_in_vars_hint1901 = frozenset([1, 60])
    FOLLOW_TREE_VAR_HINT_in_var_hint1946 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_var_hint1948 = frozenset([58])
    FOLLOW_var_in_var_hint1952 = frozenset([3, 58])
    FOLLOW_TREE_VAR_HINT_in_var_hint1992 = frozenset([2])
    FOLLOW_hint_in_var_hint1994 = frozenset([58])
    FOLLOW_var_in_var_hint1998 = frozenset([3, 58])
    FOLLOW_TREE_VAR_in_var2055 = frozenset([2])
    FOLLOW_ID_in_var2057 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2100 = frozenset([2])
    FOLLOW_ID_in_hint2102 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2130 = frozenset([2])
    FOLLOW_ID_in_hint2132 = frozenset([19, 62])
    FOLLOW_hint_args_in_hint2134 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2189 = frozenset([1, 19, 62])
    FOLLOW_ID_in_hint_arg2222 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2234 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2265 = frozenset([25])
    FOLLOW_NUMBER_in_num_whole2267 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2295 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2340 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract2346 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2348 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract2354 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2386 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2388 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract2394 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
