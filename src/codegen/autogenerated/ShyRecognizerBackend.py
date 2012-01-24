# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-24 14:05:34

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
EXPRESSION=13
ID=14
INDENT=15
MINUS=16
MODULE=17
NEWLINE=18
NUMBER=19
OPS=20
PASTE=21
PROC=22
REPLACE=23
STATELESS=24
STRING=25
TREE_ARBITRARY_TOKEN=26
TREE_CONSTS=27
TREE_COPY=28
TREE_COPY_PASTE=29
TREE_EXPRESSION=30
TREE_HINT=31
TREE_HINT_NONE=32
TREE_MODULE=33
TREE_NUM_FRACT=34
TREE_NUM_WHOLE=35
TREE_PASTE=36
TREE_PASTE_REPLACE=37
TREE_PASTE_WITH=38
TREE_PROC=39
TREE_PROC_ARGS=40
TREE_PROC_OPS=41
TREE_PROC_VARS=42
TREE_STATELESS=43
TREE_STATEMENT_CALL=44
TREE_STATEMENT_CALL_ARGS=45
TREE_TYPES=46
TREE_TYPES_ITEM=47
TREE_VAR=48
TREE_VARS_HINT=49
TREE_VAR_HINT=50
TYPES=51
UNDERSCORE=52
VARS=53
WHITESPACE=54
WITH=55

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_OPS", "TREE_PROC_VARS", "TREE_STATELESS", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", "TREE_TYPES", "TREE_TYPES_ITEM", 
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
    # grammar/ShyRecognizerBackend.g:67:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID10 = None
        proc_args11 = None

        proc_vars12 = None

        proc_ops13 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:70:5: ( ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? ) )
                # grammar/ShyRecognizerBackend.g:70:9: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? )
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





                # grammar/ShyRecognizerBackend.g:79:13: ( proc_ops )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_PROC_OPS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:79:15: proc_ops
                    pass 
                    self._state.following.append(self.FOLLOW_proc_ops_in_proc539)
                    proc_ops13 = self.proc_ops()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = proc_ops13 
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



    # $ANTLR start "proc_ops"
    # grammar/ShyRecognizerBackend.g:97:1: proc_ops returns [ value ] : ^( TREE_PROC_OPS ( statement )+ ) ;
    def proc_ops(self, ):
        value = None


        statement16 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:100:5: ( ^( TREE_PROC_OPS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:100:9: ^( TREE_PROC_OPS ( statement )+ )
                pass 
                self.match(self.input, TREE_PROC_OPS, self.FOLLOW_TREE_PROC_OPS_in_proc_ops716)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:100:26: ( statement )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == TREE_STATEMENT_CALL) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerBackend.g:100:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_proc_ops720)
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

    # $ANTLR end "proc_ops"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:105:1: statement returns [ value ] : statement_call ;
    def statement(self, ):
        value = None


        statement_call17 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:107:5: ( statement_call )
                # grammar/ShyRecognizerBackend.g:107:9: statement_call
                pass 
                self._state.following.append(self.FOLLOW_statement_call_in_statement776)
                statement_call17 = self.statement_call()

                self._state.following.pop()

                #action start
                value = statement_call17 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerBackend.g:111:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL ID statement_call_args ) ;
    def statement_call(self, ):
        value = None


        ID18 = None
        statement_call_args19 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:113:5: ( ^( TREE_STATEMENT_CALL ID statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:113:9: ^( TREE_STATEMENT_CALL ID statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call819)

                self.match(self.input, DOWN, None)
                ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call821)

                self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call823)
                statement_call_args19 = self.statement_call_args()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { ID18.text : statement_call_args19 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:117:1: statement_call_args returns [ value ] : TREE_STATEMENT_CALL_ARGS ( statement_call_arg )* ;
    def statement_call_args(self, ):
        value = None


        statement_call_arg20 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:120:5: ( TREE_STATEMENT_CALL_ARGS ( statement_call_arg )* )
                # grammar/ShyRecognizerBackend.g:120:9: TREE_STATEMENT_CALL_ARGS ( statement_call_arg )*
                pass 
                self.match(self.input, TREE_STATEMENT_CALL_ARGS, self.FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args876)

                # grammar/ShyRecognizerBackend.g:121:13: ( statement_call_arg )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == ID or LA8_0 == MINUS or LA8_0 == NUMBER) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerBackend.g:121:15: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args893)
                        statement_call_arg20 = self.statement_call_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call_arg20 ) 
                        #action end



                    else:
                        break #loop8





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"



    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerBackend.g:126:1: statement_call_arg returns [ value ] : ( ID | num_whole | num_fract );
    def statement_call_arg(self, ):
        value = None


        ID21 = None
        num_whole22 = None

        num_fract23 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:128:5: ( ID | num_whole | num_fract )
                alt9 = 3
                LA9 = self.input.LA(1)
                if LA9 == ID:
                    alt9 = 1
                elif LA9 == MINUS:
                    LA9_2 = self.input.LA(2)

                    if (LA9_2 == NUMBER) :
                        LA9_4 = self.input.LA(3)

                        if (LA9_4 == DIVIDE) :
                            alt9 = 3
                        elif (LA9_4 == 3 or LA9_4 == ID or LA9_4 == MINUS or LA9_4 == NUMBER) :
                            alt9 = 2
                        else:
                            nvae = NoViableAltException("", 9, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 9, 2, self.input)

                        raise nvae


                elif LA9 == NUMBER:
                    LA9_3 = self.input.LA(2)

                    if (LA9_3 == DIVIDE) :
                        alt9 = 3
                    elif (LA9_3 == 3 or LA9_3 == ID or LA9_3 == MINUS or LA9_3 == NUMBER) :
                        alt9 = 2
                    else:
                        nvae = NoViableAltException("", 9, 3, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:128:9: ID
                    pass 
                    ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg954)

                    #action start
                    value = { ID21.text : { } } 
                    #action end



                elif alt9 == 2:
                    # grammar/ShyRecognizerBackend.g:129:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg966)
                    num_whole22 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole22 
                    #action end



                elif alt9 == 3:
                    # grammar/ShyRecognizerBackend.g:130:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg978)
                    num_fract23 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract23 
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
    # grammar/ShyRecognizerBackend.g:133:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID24 = None
        consts_items25 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:136:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:136:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1019)

                self.match(self.input, DOWN, None)
                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1021)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1023)
                consts_items25 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID24.text , consts_items25 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:140:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item26 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:143:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:143:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:143:9: ( consts_item )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA10_0 <= TREE_NUM_WHOLE)) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:143:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1078)
                        consts_item26 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item26 is not None) and [consts_item26.name] or [None])[0] ] = ((consts_item26 is not None) and [consts_item26.value] or [None])[0] 
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

    # $ANTLR end "consts_items"


    class consts_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerBackend.g:148:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID27 = None
        ID29 = None
        ID31 = None
        EXPRESSION32 = None
        num_whole28 = None

        num_fract30 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:150:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt11 = 3
                LA11 = self.input.LA(1)
                if LA11 == TREE_NUM_WHOLE:
                    alt11 = 1
                elif LA11 == TREE_NUM_FRACT:
                    alt11 = 2
                elif LA11 == TREE_EXPRESSION:
                    alt11 = 3
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:150:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1133)

                    self.match(self.input, DOWN, None)
                    ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1135)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1137)
                    num_whole28 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID27.text , num_whole28 
                    #action end



                elif alt11 == 2:
                    # grammar/ShyRecognizerBackend.g:152:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1165)

                    self.match(self.input, DOWN, None)
                    ID29 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1167)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1169)
                    num_fract30 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID29.text , num_fract30 
                    #action end



                elif alt11 == 3:
                    # grammar/ShyRecognizerBackend.g:154:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1197)

                    self.match(self.input, DOWN, None)
                    ID31 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1199)

                    EXPRESSION32 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1201)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID31.text , EXPRESSION32.text 
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
    # grammar/ShyRecognizerBackend.g:158:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID33 = None
        types_items34 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:161:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:161:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1256)

                self.match(self.input, DOWN, None)
                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_types1258)

                self._state.following.append(self.FOLLOW_types_items_in_types1260)
                types_items34 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID33.text , types_items34 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:165:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item35 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:168:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:168:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:168:9: ( types_item )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == TREE_TYPES_ITEM) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerBackend.g:168:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1315)
                        types_item35 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item35 is not None) and [types_item35.name] or [None])[0] ] = ((types_item35 is not None) and [types_item35.value] or [None])[0] 
                        #action end



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1





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
    # grammar/ShyRecognizerBackend.g:173:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID36 = None
        vars_hint37 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:175:5: ( ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerBackend.g:175:9: ^( TREE_TYPES_ITEM ID vars_hint )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item1370)

                self.match(self.input, DOWN, None)
                ID36 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1372)

                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1374)
                vars_hint37 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID36.text , vars_hint37 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerBackend.g:179:1: vars_hint returns [ value ] : TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        value = None


        var_hint38 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:182:5: ( TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerBackend.g:182:9: TREE_VARS_HINT ( var_hint )*
                pass 
                self.match(self.input, TREE_VARS_HINT, self.FOLLOW_TREE_VARS_HINT_in_vars_hint1427)

                # grammar/ShyRecognizerBackend.g:182:24: ( var_hint )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_VAR_HINT) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:182:26: var_hint
                        pass 
                        self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1431)
                        var_hint38 = self.var_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( var_hint38 ) 
                        #action end



                    else:
                        break #loop13





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "vars_hint"



    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerBackend.g:185:1: var_hint returns [ value ] : ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        value = None


        var39 = None

        var40 = None

        hint41 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:188:5: ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == TREE_VAR_HINT) :
                    LA16_1 = self.input.LA(2)

                    if (LA16_1 == 2) :
                        LA16_2 = self.input.LA(3)

                        if (LA16_2 == TREE_HINT_NONE) :
                            alt16 = 1
                        elif (LA16_2 == TREE_HINT) :
                            alt16 = 2
                        else:
                            nvae = NoViableAltException("", 16, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 16, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammar/ShyRecognizerBackend.g:188:9: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1476)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_var_hint1478)

                    # grammar/ShyRecognizerBackend.g:188:41: ( var )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == TREE_VAR) :
                            alt14 = 1


                        if alt14 == 1:
                            # grammar/ShyRecognizerBackend.g:188:43: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1482)
                            var39 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var39 ] = dict ( ) 
                            #action end



                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                    self.match(self.input, UP, None)



                elif alt16 == 2:
                    # grammar/ShyRecognizerBackend.g:191:9: ^( TREE_VAR_HINT hint ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1522)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1524)
                    hint41 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:191:31: ( var )+
                    cnt15 = 0
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == TREE_VAR) :
                            alt15 = 1


                        if alt15 == 1:
                            # grammar/ShyRecognizerBackend.g:191:33: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1528)
                            var40 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var40 ] = hint41 
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

    # $ANTLR end "var_hint"



    # $ANTLR start "var"
    # grammar/ShyRecognizerBackend.g:196:1: var returns [ value ] : ^( TREE_VAR ID ) ;
    def var(self, ):
        value = None


        ID42 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:198:5: ( ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerBackend.g:198:9: ^( TREE_VAR ID )
                pass 
                self.match(self.input, TREE_VAR, self.FOLLOW_TREE_VAR_in_var1585)

                self.match(self.input, DOWN, None)
                ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_var1587)

                self.match(self.input, UP, None)


                #action start
                value = ID42.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:201:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID43 = None
        ID44 = None
        hint_args45 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:204:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == TREE_HINT) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == 2) :
                        LA17_2 = self.input.LA(3)

                        if (LA17_2 == ID) :
                            LA17_3 = self.input.LA(4)

                            if (LA17_3 == 3) :
                                alt17 = 1
                            elif (LA17_3 == ID or LA17_3 == UNDERSCORE) :
                                alt17 = 2
                            else:
                                nvae = NoViableAltException("", 17, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 17, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 17, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerBackend.g:204:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1630)

                    self.match(self.input, DOWN, None)
                    ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1632)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID43.text ] = list ( ) 
                    #action end



                elif alt17 == 2:
                    # grammar/ShyRecognizerBackend.g:206:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1660)

                    self.match(self.input, DOWN, None)
                    ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1662)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint1664)
                    hint_args45 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID44.text ] = hint_args45 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:210:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg46 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:213:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:213:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:213:9: ( hint_arg )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == ID or LA18_0 == UNDERSCORE) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerBackend.g:213:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args1719)
                        hint_arg46 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg46 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:216:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID47 = None
        UNDERSCORE48 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:218:5: ( ID | UNDERSCORE )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == ID) :
                    alt19 = 1
                elif (LA19_0 == UNDERSCORE) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:218:9: ID
                    pass 
                    ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1752)

                    #action start
                    value = ID47.text 
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:219:9: UNDERSCORE
                    pass 
                    UNDERSCORE48 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1764)

                    #action start
                    value = UNDERSCORE48.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:222:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS49 = None
        NUMBER50 = None
        NUMBER51 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:224:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == MINUS) :
                    alt20 = 1
                elif (LA20_0 == NUMBER) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammar/ShyRecognizerBackend.g:224:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:224:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:224:11: MINUS NUMBER
                    pass 
                    MINUS49 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1795)

                    NUMBER50 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1797)




                    #action start
                    value = int ( MINUS49.text + NUMBER50.text ) 
                    #action end



                elif alt20 == 2:
                    # grammar/ShyRecognizerBackend.g:226:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:226:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:226:11: NUMBER
                    pass 
                    NUMBER51 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1825)




                    #action start
                    value = int ( NUMBER51.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:230:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS52 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:232:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == MINUS) :
                    alt21 = 1
                elif (LA21_0 == NUMBER) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae


                if alt21 == 1:
                    # grammar/ShyRecognizerBackend.g:232:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:232:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:232:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS52 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1870)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1876)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1878)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1884)




                    #action start
                                
                    value = Fraction ( int ( MINUS52.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt21 == 2:
                    # grammar/ShyRecognizerBackend.g:237:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:237:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:237:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1916)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1918)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1924)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 27, 33, 43, 46])
    FOLLOW_stateless_in_start114 = frozenset([1, 27, 33, 43, 46])
    FOLLOW_consts_in_start141 = frozenset([1, 27, 33, 43, 46])
    FOLLOW_types_in_start167 = frozenset([1, 27, 33, 43, 46])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless287 = frozenset([2])
    FOLLOW_ID_in_stateless289 = frozenset([39])
    FOLLOW_procs_in_stateless291 = frozenset([3])
    FOLLOW_proc_in_procs346 = frozenset([1, 39])
    FOLLOW_TREE_PROC_in_proc391 = frozenset([2])
    FOLLOW_ID_in_proc405 = frozenset([3, 40, 41, 42])
    FOLLOW_proc_args_in_proc439 = frozenset([3, 41, 42])
    FOLLOW_proc_vars_in_proc489 = frozenset([3, 41])
    FOLLOW_proc_ops_in_proc539 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args612 = frozenset([2])
    FOLLOW_vars_hint_in_proc_args614 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars659 = frozenset([2])
    FOLLOW_vars_hint_in_proc_vars661 = frozenset([3])
    FOLLOW_TREE_PROC_OPS_in_proc_ops716 = frozenset([2])
    FOLLOW_statement_in_proc_ops720 = frozenset([3, 44])
    FOLLOW_statement_call_in_statement776 = frozenset([1])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call819 = frozenset([2])
    FOLLOW_ID_in_statement_call821 = frozenset([45])
    FOLLOW_statement_call_args_in_statement_call823 = frozenset([3])
    FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args876 = frozenset([1, 14, 16, 19])
    FOLLOW_statement_call_arg_in_statement_call_args893 = frozenset([1, 14, 16, 19])
    FOLLOW_ID_in_statement_call_arg954 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg966 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg978 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1019 = frozenset([2])
    FOLLOW_ID_in_consts1021 = frozenset([30, 34, 35])
    FOLLOW_consts_items_in_consts1023 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1078 = frozenset([1, 30, 34, 35])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1133 = frozenset([2])
    FOLLOW_ID_in_consts_item1135 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item1137 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1165 = frozenset([2])
    FOLLOW_ID_in_consts_item1167 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item1169 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1197 = frozenset([2])
    FOLLOW_ID_in_consts_item1199 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item1201 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1256 = frozenset([2])
    FOLLOW_ID_in_types1258 = frozenset([47])
    FOLLOW_types_items_in_types1260 = frozenset([3])
    FOLLOW_types_item_in_types_items1315 = frozenset([1, 47])
    FOLLOW_TREE_TYPES_ITEM_in_types_item1370 = frozenset([2])
    FOLLOW_ID_in_types_item1372 = frozenset([49])
    FOLLOW_vars_hint_in_types_item1374 = frozenset([3])
    FOLLOW_TREE_VARS_HINT_in_vars_hint1427 = frozenset([1, 50])
    FOLLOW_var_hint_in_vars_hint1431 = frozenset([1, 50])
    FOLLOW_TREE_VAR_HINT_in_var_hint1476 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_var_hint1478 = frozenset([48])
    FOLLOW_var_in_var_hint1482 = frozenset([3, 48])
    FOLLOW_TREE_VAR_HINT_in_var_hint1522 = frozenset([2])
    FOLLOW_hint_in_var_hint1524 = frozenset([48])
    FOLLOW_var_in_var_hint1528 = frozenset([3, 48])
    FOLLOW_TREE_VAR_in_var1585 = frozenset([2])
    FOLLOW_ID_in_var1587 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1630 = frozenset([2])
    FOLLOW_ID_in_hint1632 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1660 = frozenset([2])
    FOLLOW_ID_in_hint1662 = frozenset([14, 52])
    FOLLOW_hint_args_in_hint1664 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args1719 = frozenset([1, 14, 52])
    FOLLOW_ID_in_hint_arg1752 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1764 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1795 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole1797 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1825 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1870 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1876 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1878 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1884 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1916 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1918 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1924 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
