# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-23 20:00:16

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
    # grammar/ShyRecognizerBackend.g:97:1: proc_ops returns [ value ] : ^( TREE_PROC_OPS statement ) ;
    def proc_ops(self, ):
        value = None


        statement16 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:99:5: ( ^( TREE_PROC_OPS statement ) )
                # grammar/ShyRecognizerBackend.g:99:9: ^( TREE_PROC_OPS statement )
                pass 
                self.match(self.input, TREE_PROC_OPS, self.FOLLOW_TREE_PROC_OPS_in_proc_ops706)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statement_in_proc_ops708)
                statement16 = self.statement()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = [ statement16 ] 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_ops"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:103:1: statement returns [ value ] : statement_call ;
    def statement(self, ):
        value = None


        statement_call17 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:105:5: ( statement_call )
                # grammar/ShyRecognizerBackend.g:105:9: statement_call
                pass 
                self._state.following.append(self.FOLLOW_statement_call_in_statement751)
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
    # grammar/ShyRecognizerBackend.g:109:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL ID statement_call_args ) ;
    def statement_call(self, ):
        value = None


        ID18 = None
        statement_call_args19 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:111:5: ( ^( TREE_STATEMENT_CALL ID statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:111:9: ^( TREE_STATEMENT_CALL ID statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call794)

                self.match(self.input, DOWN, None)
                ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call796)

                self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call798)
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
    # grammar/ShyRecognizerBackend.g:115:1: statement_call_args returns [ value ] : TREE_STATEMENT_CALL_ARGS ( ID )* ;
    def statement_call_args(self, ):
        value = None


        ID20 = None

        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:118:5: ( TREE_STATEMENT_CALL_ARGS ( ID )* )
                # grammar/ShyRecognizerBackend.g:118:9: TREE_STATEMENT_CALL_ARGS ( ID )*
                pass 
                self.match(self.input, TREE_STATEMENT_CALL_ARGS, self.FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args851)

                # grammar/ShyRecognizerBackend.g:119:13: ( ID )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == ID) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerBackend.g:119:15: ID
                        pass 
                        ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_args868)

                        #action start
                        value . append ( { ID20.text : { } } ) 
                        #action end



                    else:
                        break #loop7





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call_args"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:122:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID21 = None
        consts_items22 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:125:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:125:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts913)

                self.match(self.input, DOWN, None)
                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_consts915)

                self._state.following.append(self.FOLLOW_consts_items_in_consts917)
                consts_items22 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID21.text , consts_items22 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:129:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item23 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:132:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:132:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:132:9: ( consts_item )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA8_0 <= TREE_NUM_WHOLE)) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerBackend.g:132:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items972)
                        consts_item23 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item23 is not None) and [consts_item23.name] or [None])[0] ] = ((consts_item23 is not None) and [consts_item23.value] or [None])[0] 
                        #action end



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1





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
    # grammar/ShyRecognizerBackend.g:137:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID24 = None
        ID26 = None
        ID28 = None
        EXPRESSION29 = None
        num_whole25 = None

        num_fract27 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:139:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt9 = 3
                LA9 = self.input.LA(1)
                if LA9 == TREE_NUM_WHOLE:
                    alt9 = 1
                elif LA9 == TREE_NUM_FRACT:
                    alt9 = 2
                elif LA9 == TREE_EXPRESSION:
                    alt9 = 3
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:139:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1027)

                    self.match(self.input, DOWN, None)
                    ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1029)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1031)
                    num_whole25 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID24.text , num_whole25 
                    #action end



                elif alt9 == 2:
                    # grammar/ShyRecognizerBackend.g:141:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1059)

                    self.match(self.input, DOWN, None)
                    ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1061)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1063)
                    num_fract27 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID26.text , num_fract27 
                    #action end



                elif alt9 == 3:
                    # grammar/ShyRecognizerBackend.g:143:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1091)

                    self.match(self.input, DOWN, None)
                    ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1093)

                    EXPRESSION29 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1095)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID28.text , EXPRESSION29.text 
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
    # grammar/ShyRecognizerBackend.g:147:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID30 = None
        types_items31 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:150:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:150:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1150)

                self.match(self.input, DOWN, None)
                ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_types1152)

                self._state.following.append(self.FOLLOW_types_items_in_types1154)
                types_items31 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID30.text , types_items31 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:154:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item32 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:157:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:157:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:157:9: ( types_item )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_TYPES_ITEM) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:157:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1209)
                        types_item32 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item32 is not None) and [types_item32.name] or [None])[0] ] = ((types_item32 is not None) and [types_item32.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:162:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID33 = None
        vars_hint34 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:164:5: ( ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerBackend.g:164:9: ^( TREE_TYPES_ITEM ID vars_hint )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item1264)

                self.match(self.input, DOWN, None)
                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1266)

                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1268)
                vars_hint34 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID33.text , vars_hint34 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerBackend.g:168:1: vars_hint returns [ value ] : TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        value = None


        var_hint35 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:171:5: ( TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerBackend.g:171:9: TREE_VARS_HINT ( var_hint )*
                pass 
                self.match(self.input, TREE_VARS_HINT, self.FOLLOW_TREE_VARS_HINT_in_vars_hint1321)

                # grammar/ShyRecognizerBackend.g:171:24: ( var_hint )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == TREE_VAR_HINT) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:171:26: var_hint
                        pass 
                        self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1325)
                        var_hint35 = self.var_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( var_hint35 ) 
                        #action end



                    else:
                        break #loop11





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "vars_hint"



    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerBackend.g:174:1: var_hint returns [ value ] : ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        value = None


        var36 = None

        var37 = None

        hint38 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:177:5: ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == TREE_VAR_HINT) :
                    LA14_1 = self.input.LA(2)

                    if (LA14_1 == 2) :
                        LA14_2 = self.input.LA(3)

                        if (LA14_2 == TREE_HINT_NONE) :
                            alt14 = 1
                        elif (LA14_2 == TREE_HINT) :
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
                    # grammar/ShyRecognizerBackend.g:177:9: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1370)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_var_hint1372)

                    # grammar/ShyRecognizerBackend.g:177:41: ( var )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == TREE_VAR) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyRecognizerBackend.g:177:43: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1376)
                            var36 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var36 ] = dict ( ) 
                            #action end



                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    self.match(self.input, UP, None)



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:180:9: ^( TREE_VAR_HINT hint ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1416)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1418)
                    hint38 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:180:31: ( var )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == TREE_VAR) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyRecognizerBackend.g:180:33: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1422)
                            var37 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var37 ] = hint38 
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

    # $ANTLR end "var_hint"



    # $ANTLR start "var"
    # grammar/ShyRecognizerBackend.g:185:1: var returns [ value ] : ^( TREE_VAR ID ) ;
    def var(self, ):
        value = None


        ID39 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:187:5: ( ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerBackend.g:187:9: ^( TREE_VAR ID )
                pass 
                self.match(self.input, TREE_VAR, self.FOLLOW_TREE_VAR_in_var1479)

                self.match(self.input, DOWN, None)
                ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_var1481)

                self.match(self.input, UP, None)


                #action start
                value = ID39.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:190:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID40 = None
        ID41 = None
        hint_args42 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:193:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == TREE_HINT) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == 2) :
                        LA15_2 = self.input.LA(3)

                        if (LA15_2 == ID) :
                            LA15_3 = self.input.LA(4)

                            if (LA15_3 == 3) :
                                alt15 = 1
                            elif (LA15_3 == ID or LA15_3 == UNDERSCORE) :
                                alt15 = 2
                            else:
                                nvae = NoViableAltException("", 15, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 15, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 15, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:193:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1524)

                    self.match(self.input, DOWN, None)
                    ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1526)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID40.text ] = list ( ) 
                    #action end



                elif alt15 == 2:
                    # grammar/ShyRecognizerBackend.g:195:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1554)

                    self.match(self.input, DOWN, None)
                    ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1556)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint1558)
                    hint_args42 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID41.text ] = hint_args42 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:199:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg43 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:202:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:202:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:202:9: ( hint_arg )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ID or LA16_0 == UNDERSCORE) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerBackend.g:202:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args1613)
                        hint_arg43 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg43 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:205:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID44 = None
        UNDERSCORE45 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:207:5: ( ID | UNDERSCORE )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == ID) :
                    alt17 = 1
                elif (LA17_0 == UNDERSCORE) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerBackend.g:207:9: ID
                    pass 
                    ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1646)

                    #action start
                    value = ID44.text 
                    #action end



                elif alt17 == 2:
                    # grammar/ShyRecognizerBackend.g:208:9: UNDERSCORE
                    pass 
                    UNDERSCORE45 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1658)

                    #action start
                    value = UNDERSCORE45.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:211:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS46 = None
        NUMBER47 = None
        NUMBER48 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:213:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == MINUS) :
                    alt18 = 1
                elif (LA18_0 == NUMBER) :
                    alt18 = 2
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerBackend.g:213:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:213:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:213:11: MINUS NUMBER
                    pass 
                    MINUS46 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1689)

                    NUMBER47 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1691)




                    #action start
                    value = int ( MINUS46.text + NUMBER47.text ) 
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:215:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:215:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:215:11: NUMBER
                    pass 
                    NUMBER48 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1719)




                    #action start
                    value = int ( NUMBER48.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:219:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS49 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:221:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MINUS) :
                    alt19 = 1
                elif (LA19_0 == NUMBER) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerBackend.g:221:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:221:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:221:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS49 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1764)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1770)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1772)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1778)




                    #action start
                                
                    value = Fraction ( int ( MINUS49.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt19 == 2:
                    # grammar/ShyRecognizerBackend.g:226:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:226:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:226:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1810)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1812)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1818)




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
    FOLLOW_TREE_PROC_OPS_in_proc_ops706 = frozenset([2])
    FOLLOW_statement_in_proc_ops708 = frozenset([3])
    FOLLOW_statement_call_in_statement751 = frozenset([1])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call794 = frozenset([2])
    FOLLOW_ID_in_statement_call796 = frozenset([45])
    FOLLOW_statement_call_args_in_statement_call798 = frozenset([3])
    FOLLOW_TREE_STATEMENT_CALL_ARGS_in_statement_call_args851 = frozenset([1, 14])
    FOLLOW_ID_in_statement_call_args868 = frozenset([1, 14])
    FOLLOW_TREE_CONSTS_in_consts913 = frozenset([2])
    FOLLOW_ID_in_consts915 = frozenset([30, 34, 35])
    FOLLOW_consts_items_in_consts917 = frozenset([3])
    FOLLOW_consts_item_in_consts_items972 = frozenset([1, 30, 34, 35])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1027 = frozenset([2])
    FOLLOW_ID_in_consts_item1029 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item1031 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1059 = frozenset([2])
    FOLLOW_ID_in_consts_item1061 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item1063 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1091 = frozenset([2])
    FOLLOW_ID_in_consts_item1093 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item1095 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1150 = frozenset([2])
    FOLLOW_ID_in_types1152 = frozenset([47])
    FOLLOW_types_items_in_types1154 = frozenset([3])
    FOLLOW_types_item_in_types_items1209 = frozenset([1, 47])
    FOLLOW_TREE_TYPES_ITEM_in_types_item1264 = frozenset([2])
    FOLLOW_ID_in_types_item1266 = frozenset([49])
    FOLLOW_vars_hint_in_types_item1268 = frozenset([3])
    FOLLOW_TREE_VARS_HINT_in_vars_hint1321 = frozenset([1, 50])
    FOLLOW_var_hint_in_vars_hint1325 = frozenset([1, 50])
    FOLLOW_TREE_VAR_HINT_in_var_hint1370 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_var_hint1372 = frozenset([48])
    FOLLOW_var_in_var_hint1376 = frozenset([3, 48])
    FOLLOW_TREE_VAR_HINT_in_var_hint1416 = frozenset([2])
    FOLLOW_hint_in_var_hint1418 = frozenset([48])
    FOLLOW_var_in_var_hint1422 = frozenset([3, 48])
    FOLLOW_TREE_VAR_in_var1479 = frozenset([2])
    FOLLOW_ID_in_var1481 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1524 = frozenset([2])
    FOLLOW_ID_in_hint1526 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1554 = frozenset([2])
    FOLLOW_ID_in_hint1556 = frozenset([14, 52])
    FOLLOW_hint_args_in_hint1558 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args1613 = frozenset([1, 14, 52])
    FOLLOW_ID_in_hint_arg1646 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1658 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1689 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole1691 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1719 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1764 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1770 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1772 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1778 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1810 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1812 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1818 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
