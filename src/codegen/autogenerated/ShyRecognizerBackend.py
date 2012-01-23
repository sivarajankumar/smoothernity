# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-23 19:33:18

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
TREE_STATEMENT=44
TREE_TYPES=45
TREE_TYPES_ITEM=46
TREE_VAR=47
TREE_VARS_HINT=48
TREE_VAR_HINT=49
TYPES=50
UNDERSCORE=51
VARS=52
WHITESPACE=53
WITH=54

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
    "TREE_STATEMENT", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VAR", "TREE_VARS_HINT", 
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
                value = statement16 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_ops"



    # $ANTLR start "statement"
    # grammar/ShyRecognizerBackend.g:103:1: statement returns [ value ] : ^( TREE_STATEMENT ID ) ;
    def statement(self, ):
        value = None


        ID17 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:105:5: ( ^( TREE_STATEMENT ID ) )
                # grammar/ShyRecognizerBackend.g:105:9: ^( TREE_STATEMENT ID )
                pass 
                self.match(self.input, TREE_STATEMENT, self.FOLLOW_TREE_STATEMENT_in_statement753)

                self.match(self.input, DOWN, None)
                ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_statement755)

                self.match(self.input, UP, None)


                #action start
                value = [ { ID17.text : [ ] } ] 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:109:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID18 = None
        consts_items19 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:112:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:112:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts810)

                self.match(self.input, DOWN, None)
                ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_consts812)

                self._state.following.append(self.FOLLOW_consts_items_in_consts814)
                consts_items19 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID18.text , consts_items19 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:116:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item20 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:119:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:119:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:119:9: ( consts_item )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA7_0 <= TREE_NUM_WHOLE)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerBackend.g:119:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items869)
                        consts_item20 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item20 is not None) and [consts_item20.name] or [None])[0] ] = ((consts_item20 is not None) and [consts_item20.value] or [None])[0] 
                        #action end



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1





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
    # grammar/ShyRecognizerBackend.g:124:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID21 = None
        ID23 = None
        ID25 = None
        EXPRESSION26 = None
        num_whole22 = None

        num_fract24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:126:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt8 = 3
                LA8 = self.input.LA(1)
                if LA8 == TREE_NUM_WHOLE:
                    alt8 = 1
                elif LA8 == TREE_NUM_FRACT:
                    alt8 = 2
                elif LA8 == TREE_EXPRESSION:
                    alt8 = 3
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # grammar/ShyRecognizerBackend.g:126:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item924)

                    self.match(self.input, DOWN, None)
                    ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item926)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item928)
                    num_whole22 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID21.text , num_whole22 
                    #action end



                elif alt8 == 2:
                    # grammar/ShyRecognizerBackend.g:128:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item956)

                    self.match(self.input, DOWN, None)
                    ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item958)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item960)
                    num_fract24 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID23.text , num_fract24 
                    #action end



                elif alt8 == 3:
                    # grammar/ShyRecognizerBackend.g:130:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item988)

                    self.match(self.input, DOWN, None)
                    ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item990)

                    EXPRESSION26 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item992)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID25.text , EXPRESSION26.text 
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
    # grammar/ShyRecognizerBackend.g:134:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID27 = None
        types_items28 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:137:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:137:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1047)

                self.match(self.input, DOWN, None)
                ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_types1049)

                self._state.following.append(self.FOLLOW_types_items_in_types1051)
                types_items28 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID27.text , types_items28 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:141:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item29 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:144:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:144:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:144:9: ( types_item )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == TREE_TYPES_ITEM) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerBackend.g:144:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1106)
                        types_item29 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item29 is not None) and [types_item29.name] or [None])[0] ] = ((types_item29 is not None) and [types_item29.value] or [None])[0] 
                        #action end



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1





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
    # grammar/ShyRecognizerBackend.g:149:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID30 = None
        vars_hint31 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:151:5: ( ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerBackend.g:151:9: ^( TREE_TYPES_ITEM ID vars_hint )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item1161)

                self.match(self.input, DOWN, None)
                ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1163)

                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1165)
                vars_hint31 = self.vars_hint()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID30.text , vars_hint31 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerBackend.g:155:1: vars_hint returns [ value ] : TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        value = None


        var_hint32 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:158:5: ( TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerBackend.g:158:9: TREE_VARS_HINT ( var_hint )*
                pass 
                self.match(self.input, TREE_VARS_HINT, self.FOLLOW_TREE_VARS_HINT_in_vars_hint1218)

                # grammar/ShyRecognizerBackend.g:158:24: ( var_hint )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_VAR_HINT) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:158:26: var_hint
                        pass 
                        self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1222)
                        var_hint32 = self.var_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( var_hint32 ) 
                        #action end



                    else:
                        break #loop10





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "vars_hint"



    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerBackend.g:161:1: var_hint returns [ value ] : ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        value = None


        var33 = None

        var34 = None

        hint35 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:164:5: ( ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | ^( TREE_VAR_HINT hint ( var )+ ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == TREE_VAR_HINT) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == 2) :
                        LA13_2 = self.input.LA(3)

                        if (LA13_2 == TREE_HINT_NONE) :
                            alt13 = 1
                        elif (LA13_2 == TREE_HINT) :
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
                    # grammar/ShyRecognizerBackend.g:164:9: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1267)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_var_hint1269)

                    # grammar/ShyRecognizerBackend.g:164:41: ( var )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == TREE_VAR) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/ShyRecognizerBackend.g:164:43: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1273)
                            var33 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var33 ] = dict ( ) 
                            #action end



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    self.match(self.input, UP, None)



                elif alt13 == 2:
                    # grammar/ShyRecognizerBackend.g:167:9: ^( TREE_VAR_HINT hint ( var )+ )
                    pass 
                    self.match(self.input, TREE_VAR_HINT, self.FOLLOW_TREE_VAR_HINT_in_var_hint1313)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1315)
                    hint35 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:167:31: ( var )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == TREE_VAR) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyRecognizerBackend.g:167:33: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1319)
                            var34 = self.var()

                            self._state.following.pop()

                            #action start
                            value [ var34 ] = hint35 
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

    # $ANTLR end "var_hint"



    # $ANTLR start "var"
    # grammar/ShyRecognizerBackend.g:172:1: var returns [ value ] : ^( TREE_VAR ID ) ;
    def var(self, ):
        value = None


        ID36 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:174:5: ( ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerBackend.g:174:9: ^( TREE_VAR ID )
                pass 
                self.match(self.input, TREE_VAR, self.FOLLOW_TREE_VAR_in_var1376)

                self.match(self.input, DOWN, None)
                ID36 = self.match(self.input, ID, self.FOLLOW_ID_in_var1378)

                self.match(self.input, UP, None)


                #action start
                value = ID36.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "var"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:177:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID37 = None
        ID38 = None
        hint_args39 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:180:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == TREE_HINT) :
                    LA14_1 = self.input.LA(2)

                    if (LA14_1 == 2) :
                        LA14_2 = self.input.LA(3)

                        if (LA14_2 == ID) :
                            LA14_3 = self.input.LA(4)

                            if (LA14_3 == 3) :
                                alt14 = 1
                            elif (LA14_3 == ID or LA14_3 == UNDERSCORE) :
                                alt14 = 2
                            else:
                                nvae = NoViableAltException("", 14, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerBackend.g:180:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1421)

                    self.match(self.input, DOWN, None)
                    ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1423)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID37.text ] = list ( ) 
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:182:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1451)

                    self.match(self.input, DOWN, None)
                    ID38 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1453)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint1455)
                    hint_args39 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID38.text ] = hint_args39 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:186:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg40 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:189:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:189:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:189:9: ( hint_arg )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == ID or LA15_0 == UNDERSCORE) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:189:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args1510)
                        hint_arg40 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg40 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:192:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID41 = None
        UNDERSCORE42 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:194:5: ( ID | UNDERSCORE )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == ID) :
                    alt16 = 1
                elif (LA16_0 == UNDERSCORE) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammar/ShyRecognizerBackend.g:194:9: ID
                    pass 
                    ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1543)

                    #action start
                    value = ID41.text 
                    #action end



                elif alt16 == 2:
                    # grammar/ShyRecognizerBackend.g:195:9: UNDERSCORE
                    pass 
                    UNDERSCORE42 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1555)

                    #action start
                    value = UNDERSCORE42.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:198:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS43 = None
        NUMBER44 = None
        NUMBER45 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:200:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == MINUS) :
                    alt17 = 1
                elif (LA17_0 == NUMBER) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerBackend.g:200:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:200:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:200:11: MINUS NUMBER
                    pass 
                    MINUS43 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1586)

                    NUMBER44 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1588)




                    #action start
                    value = int ( MINUS43.text + NUMBER44.text ) 
                    #action end



                elif alt17 == 2:
                    # grammar/ShyRecognizerBackend.g:202:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:202:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:202:11: NUMBER
                    pass 
                    NUMBER45 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1616)




                    #action start
                    value = int ( NUMBER45.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:206:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS46 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:208:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:208:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:208:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:208:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS46 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1661)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1667)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1669)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1675)




                    #action start
                                
                    value = Fraction ( int ( MINUS46.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:213:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:213:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:213:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1707)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1709)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1715)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 27, 33, 43, 45])
    FOLLOW_stateless_in_start114 = frozenset([1, 27, 33, 43, 45])
    FOLLOW_consts_in_start141 = frozenset([1, 27, 33, 43, 45])
    FOLLOW_types_in_start167 = frozenset([1, 27, 33, 43, 45])
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
    FOLLOW_TREE_STATEMENT_in_statement753 = frozenset([2])
    FOLLOW_ID_in_statement755 = frozenset([3])
    FOLLOW_TREE_CONSTS_in_consts810 = frozenset([2])
    FOLLOW_ID_in_consts812 = frozenset([30, 34, 35])
    FOLLOW_consts_items_in_consts814 = frozenset([3])
    FOLLOW_consts_item_in_consts_items869 = frozenset([1, 30, 34, 35])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item924 = frozenset([2])
    FOLLOW_ID_in_consts_item926 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item928 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item956 = frozenset([2])
    FOLLOW_ID_in_consts_item958 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item960 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item988 = frozenset([2])
    FOLLOW_ID_in_consts_item990 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item992 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1047 = frozenset([2])
    FOLLOW_ID_in_types1049 = frozenset([46])
    FOLLOW_types_items_in_types1051 = frozenset([3])
    FOLLOW_types_item_in_types_items1106 = frozenset([1, 46])
    FOLLOW_TREE_TYPES_ITEM_in_types_item1161 = frozenset([2])
    FOLLOW_ID_in_types_item1163 = frozenset([48])
    FOLLOW_vars_hint_in_types_item1165 = frozenset([3])
    FOLLOW_TREE_VARS_HINT_in_vars_hint1218 = frozenset([1, 49])
    FOLLOW_var_hint_in_vars_hint1222 = frozenset([1, 49])
    FOLLOW_TREE_VAR_HINT_in_var_hint1267 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_var_hint1269 = frozenset([47])
    FOLLOW_var_in_var_hint1273 = frozenset([3, 47])
    FOLLOW_TREE_VAR_HINT_in_var_hint1313 = frozenset([2])
    FOLLOW_hint_in_var_hint1315 = frozenset([47])
    FOLLOW_var_in_var_hint1319 = frozenset([3, 47])
    FOLLOW_TREE_VAR_in_var1376 = frozenset([2])
    FOLLOW_ID_in_var1378 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1421 = frozenset([2])
    FOLLOW_ID_in_hint1423 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1451 = frozenset([2])
    FOLLOW_ID_in_hint1453 = frozenset([14, 51])
    FOLLOW_hint_args_in_hint1455 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args1510 = frozenset([1, 14, 51])
    FOLLOW_ID_in_hint_arg1543 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1555 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1586 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole1588 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1616 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1661 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1667 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1669 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1675 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1707 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1709 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1715 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
