# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-31 18:58:04

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
TYPES=68
UNDERSCORE=69
VARS=70
WHITESPACE=71
WITH=72

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
    "TREE_TYPES_ITEM", "TYPES", "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:22:1: start returns [ value ] : ( module | stateless | consts | types | messages )* ;
    def start(self, ):
        value = None


        module1 = None

        stateless2 = None

        consts3 = None

        types4 = None

        messages5 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:25:5: ( ( module | stateless | consts | types | messages )* )
                # grammar/ShyRecognizerBackend.g:25:9: ( module | stateless | consts | types | messages )*
                pass 
                # grammar/ShyRecognizerBackend.g:25:9: ( module | stateless | consts | types | messages )*
                while True: #loop1
                    alt1 = 6
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
    # grammar/ShyRecognizerBackend.g:53:1: module returns [ value ] : ^( TREE_MODULE ID ) ;
    def module(self, ):
        value = None


        ID6 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:55:5: ( ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerBackend.g:55:9: ^( TREE_MODULE ID )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module248)

                self.match(self.input, DOWN, None)
                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_module250)

                self.match(self.input, UP, None)


                #action start
                value = ID6.text 
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
    # grammar/ShyRecognizerBackend.g:58:1: stateless returns [ title , content ] : ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        ID7 = None
        ID8 = None
        procs9 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:60:5: ( ^( TREE_STATELESS ID ) | ^( TREE_STATELESS ID procs ) )
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
                    # grammar/ShyRecognizerBackend.g:60:9: ^( TREE_STATELESS ID )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless283)

                    self.match(self.input, DOWN, None)
                    ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless285)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID7.text , dict ( ) 
                    #action end



                elif alt2 == 2:
                    # grammar/ShyRecognizerBackend.g:62:9: ^( TREE_STATELESS ID procs )
                    pass 
                    self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless313)

                    self.match(self.input, DOWN, None)
                    ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless315)

                    self._state.following.append(self.FOLLOW_procs_in_stateless317)
                    procs9 = self.procs()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID8.text , procs9 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "stateless"



    # $ANTLR start "procs"
    # grammar/ShyRecognizerBackend.g:66:1: procs returns [ value ] : ( proc )+ ;
    def procs(self, ):
        value = None


        proc10 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:69:5: ( ( proc )+ )
                # grammar/ShyRecognizerBackend.g:69:9: ( proc )+
                pass 
                # grammar/ShyRecognizerBackend.g:69:9: ( proc )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == TREE_PROC) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyRecognizerBackend.g:69:11: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_procs372)
                        proc10 = self.proc()

                        self._state.following.pop()

                        #action start
                        value [ ((proc10 is not None) and [proc10.title] or [None])[0] ] = ((proc10 is not None) and [proc10.content] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:72:1: proc returns [ title , content ] : ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID11 = None
        proc_args12 = None

        proc_vars13 = None

        statements14 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:75:5: ( ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? ) )
                # grammar/ShyRecognizerBackend.g:75:9: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( statements )? )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc417)

                self.match(self.input, DOWN, None)
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_proc431)

                #action start
                retval.title = ID11.text 
                #action end


                # grammar/ShyRecognizerBackend.g:78:13: ( proc_args )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_PROC_ARGS) :
                    alt4 = 1
                if alt4 == 1:
                    # grammar/ShyRecognizerBackend.g:78:15: proc_args
                    pass 
                    self._state.following.append(self.FOLLOW_proc_args_in_proc465)
                    proc_args12 = self.proc_args()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'args' ] = proc_args12 
                    #action end





                # grammar/ShyRecognizerBackend.g:81:13: ( proc_vars )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_PROC_VARS) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:81:15: proc_vars
                    pass 
                    self._state.following.append(self.FOLLOW_proc_vars_in_proc515)
                    proc_vars13 = self.proc_vars()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'vars' ] = proc_vars13 
                    #action end





                # grammar/ShyRecognizerBackend.g:84:13: ( statements )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == TREE_STATEMENTS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerBackend.g:84:15: statements
                    pass 
                    self._state.following.append(self.FOLLOW_statements_in_proc565)
                    statements14 = self.statements()

                    self._state.following.pop()

                    #action start
                    retval.content [ 'ops' ] = statements14 
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
    # grammar/ShyRecognizerBackend.g:90:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        value = None


        attrs_hints15 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:92:5: ( ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:92:9: ^( TREE_PROC_ARGS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args638)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args640)
                attrs_hints15 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = attrs_hints15 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"



    # $ANTLR start "proc_vars"
    # grammar/ShyRecognizerBackend.g:96:1: proc_vars returns [ value ] : ^( TREE_PROC_VARS attrs_hints ) ;
    def proc_vars(self, ):
        value = None


        attrs_hints16 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:98:5: ( ^( TREE_PROC_VARS attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:98:9: ^( TREE_PROC_VARS attrs_hints )
                pass 
                self.match(self.input, TREE_PROC_VARS, self.FOLLOW_TREE_PROC_VARS_in_proc_vars685)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_vars687)
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

    # $ANTLR end "proc_vars"



    # $ANTLR start "statements"
    # grammar/ShyRecognizerBackend.g:102:1: statements returns [ value ] : ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        value = None


        statement17 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:105:5: ( ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerBackend.g:105:9: ^( TREE_STATEMENTS ( statement )+ )
                pass 
                self.match(self.input, TREE_STATEMENTS, self.FOLLOW_TREE_STATEMENTS_in_statements742)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:105:28: ( statement )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((TREE_STATEMENT_ASSIGN <= LA7_0 <= TREE_STATEMENT_CALL) or (TREE_STATEMENT_IF <= LA7_0 <= TREE_STATEMENT_WITH)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerBackend.g:105:30: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements746)
                        statement17 = self.statement()

                        self._state.following.pop()

                        #action start
                        value . append ( statement17 ) 
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
    # grammar/ShyRecognizerBackend.g:110:1: statement returns [ value ] : ( statement_call | statement_if | statement_assign | statement_with );
    def statement(self, ):
        value = None


        statement_call18 = None

        statement_if19 = None

        statement_assign20 = None

        statement_with21 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:112:5: ( statement_call | statement_if | statement_assign | statement_with )
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
                    # grammar/ShyRecognizerBackend.g:112:9: statement_call
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_statement802)
                    statement_call18 = self.statement_call()

                    self._state.following.pop()

                    #action start
                    value = statement_call18 
                    #action end



                elif alt8 == 2:
                    # grammar/ShyRecognizerBackend.g:114:9: statement_if
                    pass 
                    self._state.following.append(self.FOLLOW_statement_if_in_statement826)
                    statement_if19 = self.statement_if()

                    self._state.following.pop()

                    #action start
                    value = statement_if19 
                    #action end



                elif alt8 == 3:
                    # grammar/ShyRecognizerBackend.g:116:9: statement_assign
                    pass 
                    self._state.following.append(self.FOLLOW_statement_assign_in_statement850)
                    statement_assign20 = self.statement_assign()

                    self._state.following.pop()

                    #action start
                    value = statement_assign20 
                    #action end



                elif alt8 == 4:
                    # grammar/ShyRecognizerBackend.g:118:9: statement_with
                    pass 
                    self._state.following.append(self.FOLLOW_statement_with_in_statement874)
                    statement_with21 = self.statement_with()

                    self._state.following.pop()

                    #action start
                    value = statement_with21 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement"



    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerBackend.g:122:1: statement_with returns [ value ] : ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        value = None


        ID22 = None
        statements23 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:124:5: ( ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerBackend.g:124:9: ^( TREE_STATEMENT_WITH ID statements )
                pass 
                self.match(self.input, TREE_STATEMENT_WITH, self.FOLLOW_TREE_STATEMENT_WITH_in_statement_with917)

                self.match(self.input, DOWN, None)
                ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with919)

                self._state.following.append(self.FOLLOW_statements_in_statement_with921)
                statements23 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'with' : { ID22.text : statements23 } } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_with"



    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerBackend.g:128:1: statement_assign returns [ value ] : ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) ;
    def statement_assign(self, ):
        value = None


        ID25 = None
        arbitrary_value24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:130:5: ( ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:130:9: ^( TREE_STATEMENT_ASSIGN arbitrary_value ( ID )+ )
                pass 
                self.match(self.input, TREE_STATEMENT_ASSIGN, self.FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign962)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign964)
                arbitrary_value24 = self.arbitrary_value()

                self._state.following.pop()

                #action start
                value = { 'assign' : [ arbitrary_value24 , list ( ) ] } 
                #action end


                # grammar/ShyRecognizerBackend.g:132:13: ( ID )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == ID) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerBackend.g:132:15: ID
                        pass 
                        ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign994)

                        #action start
                        value [ 'assign' ] [ - 1 ] . append ( ID25.text ) 
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
    # grammar/ShyRecognizerBackend.g:138:1: statement_if returns [ value ] : ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) ;
    def statement_if(self, ):
        value = None


        statement_elif26 = None

        statement_else27 = None


        value = { 'if' : [ ] } 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:141:5: ( ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? ) )
                # grammar/ShyRecognizerBackend.g:141:9: ^( TREE_STATEMENT_IF ( statement_elif )+ ( statement_else )? )
                pass 
                self.match(self.input, TREE_STATEMENT_IF, self.FOLLOW_TREE_STATEMENT_IF_in_statement_if1077)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:142:13: ( statement_elif )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_STATEMENT_ELIF) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:142:15: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1093)
                        statement_elif26 = self.statement_elif()

                        self._state.following.pop()

                        #action start
                        value [ 'if' ] . append ( statement_elif26 ) 
                        #action end



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1


                # grammar/ShyRecognizerBackend.g:145:13: ( statement_else )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_STATEMENT_ELSE) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerBackend.g:145:15: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1143)
                    statement_else27 = self.statement_else()

                    self._state.following.pop()

                    #action start
                    value [ 'else' ] = statement_else27 
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
    # grammar/ShyRecognizerBackend.g:151:1: statement_elif returns [ value ] : ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) );
    def statement_elif(self, ):
        value = None


        condition_any28 = None

        statements29 = None

        condition_all30 = None

        statements31 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:153:5: ( ^( TREE_STATEMENT_ELIF condition_any statements ) | ^( TREE_STATEMENT_ELIF condition_all statements ) )
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
                    # grammar/ShyRecognizerBackend.g:153:9: ^( TREE_STATEMENT_ELIF condition_any statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1216)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_any_in_statement_elif1218)
                    condition_any28 = self.condition_any()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1220)
                    statements29 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'any' : condition_any28 ,
                       'ops' : statements29 }
                                
                    #action end



                elif alt12 == 2:
                    # grammar/ShyRecognizerBackend.g:158:9: ^( TREE_STATEMENT_ELIF condition_all statements )
                    pass 
                    self.match(self.input, TREE_STATEMENT_ELIF, self.FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1248)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_condition_all_in_statement_elif1250)
                    condition_all30 = self.condition_all()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_statements_in_statement_elif1252)
                    statements31 = self.statements()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = {
                       'all' : condition_all30 ,
                       'ops' : statements31 }
                                
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_elif"



    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerBackend.g:165:1: statement_else returns [ value ] : ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        value = None


        statements32 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:167:5: ( ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerBackend.g:167:9: ^( TREE_STATEMENT_ELSE statements )
                pass 
                self.match(self.input, TREE_STATEMENT_ELSE, self.FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1297)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_statements_in_statement_else1299)
                statements32 = self.statements()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = statements32 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_else"



    # $ANTLR start "condition_any"
    # grammar/ShyRecognizerBackend.g:171:1: condition_any returns [ value ] : ^( TREE_CONDITION_ANY ( statement_call )+ ) ;
    def condition_any(self, ):
        value = None


        statement_call33 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:174:5: ( ^( TREE_CONDITION_ANY ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:174:9: ^( TREE_CONDITION_ANY ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ANY, self.FOLLOW_TREE_CONDITION_ANY_in_condition_any1354)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:175:13: ( statement_call )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == TREE_STATEMENT_CALL) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:175:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_any1370)
                        statement_call33 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call33 ) 
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
    # grammar/ShyRecognizerBackend.g:180:1: condition_all returns [ value ] : ^( TREE_CONDITION_ALL ( statement_call )+ ) ;
    def condition_all(self, ):
        value = None


        statement_call34 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:183:5: ( ^( TREE_CONDITION_ALL ( statement_call )+ ) )
                # grammar/ShyRecognizerBackend.g:183:9: ^( TREE_CONDITION_ALL ( statement_call )+ )
                pass 
                self.match(self.input, TREE_CONDITION_ALL, self.FOLLOW_TREE_CONDITION_ALL_in_condition_all1445)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:184:13: ( statement_call )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == TREE_STATEMENT_CALL) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerBackend.g:184:15: statement_call
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_in_condition_all1461)
                        statement_call34 = self.statement_call()

                        self._state.following.pop()

                        #action start
                        value . append ( statement_call34 ) 
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
    # grammar/ShyRecognizerBackend.g:189:1: statement_call returns [ value ] : ^( TREE_STATEMENT_CALL statement_call_args ) ;
    def statement_call(self, ):
        value = None


        statement_call_args35 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:191:5: ( ^( TREE_STATEMENT_CALL statement_call_args ) )
                # grammar/ShyRecognizerBackend.g:191:9: ^( TREE_STATEMENT_CALL statement_call_args )
                pass 
                self.match(self.input, TREE_STATEMENT_CALL, self.FOLLOW_TREE_STATEMENT_CALL_in_statement_call1526)

                if self.input.LA(1) == DOWN:
                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1528)
                    statement_call_args35 = self.statement_call_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)



                #action start
                value = { 'call' : statement_call_args35 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "statement_call"



    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerBackend.g:195:1: statement_call_args returns [ value ] : ( arbitrary_value )* ;
    def statement_call_args(self, ):
        value = None


        arbitrary_value36 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:198:5: ( ( arbitrary_value )* )
                # grammar/ShyRecognizerBackend.g:198:9: ( arbitrary_value )*
                pass 
                # grammar/ShyRecognizerBackend.g:198:9: ( arbitrary_value )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA15_0 <= ID) or LA15_0 == MINUS or LA15_0 == NUMBER) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:198:11: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1583)
                        arbitrary_value36 = self.arbitrary_value()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_value36 ) 
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
    # grammar/ShyRecognizerBackend.g:203:1: arbitrary_value returns [ value ] : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        value = None


        ID37 = None
        EXPRESSION38 = None
        num_whole39 = None

        num_fract40 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:205:5: ( ID | EXPRESSION | num_whole | num_fract )
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
                    # grammar/ShyRecognizerBackend.g:205:9: ID
                    pass 
                    ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1636)

                    #action start
                    value = ID37.text 
                    #action end



                elif alt16 == 2:
                    # grammar/ShyRecognizerBackend.g:206:9: EXPRESSION
                    pass 
                    EXPRESSION38 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1648)

                    #action start
                    value = EXPRESSION38.text 
                    #action end



                elif alt16 == 3:
                    # grammar/ShyRecognizerBackend.g:207:9: num_whole
                    pass 
                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1660)
                    num_whole39 = self.num_whole()

                    self._state.following.pop()

                    #action start
                    value = num_whole39 
                    #action end



                elif alt16 == 4:
                    # grammar/ShyRecognizerBackend.g:208:9: num_fract
                    pass 
                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1672)
                    num_fract40 = self.num_fract()

                    self._state.following.pop()

                    #action start
                    value = num_fract40 
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
    # grammar/ShyRecognizerBackend.g:211:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID41 = None
        consts_items42 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:214:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:214:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts1713)

                self.match(self.input, DOWN, None)
                ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1715)

                self._state.following.append(self.FOLLOW_consts_items_in_consts1717)
                consts_items42 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID41.text , consts_items42 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:218:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item43 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:221:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:221:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:221:9: ( consts_item )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA17_0 <= TREE_NUM_WHOLE)) :
                        alt17 = 1


                    if alt17 == 1:
                        # grammar/ShyRecognizerBackend.g:221:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1772)
                        consts_item43 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item43 is not None) and [consts_item43.name] or [None])[0] ] = ((consts_item43 is not None) and [consts_item43.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:226:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID44 = None
        ID46 = None
        ID48 = None
        EXPRESSION49 = None
        num_whole45 = None

        num_fract47 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:228:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerBackend.g:228:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item1827)

                    self.match(self.input, DOWN, None)
                    ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1829)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1831)
                    num_whole45 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID44.text , num_whole45 
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:230:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item1859)

                    self.match(self.input, DOWN, None)
                    ID46 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1861)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1863)
                    num_fract47 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID46.text , num_fract47 
                    #action end



                elif alt18 == 3:
                    # grammar/ShyRecognizerBackend.g:232:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item1891)

                    self.match(self.input, DOWN, None)
                    ID48 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1893)

                    EXPRESSION49 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1895)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID48.text , EXPRESSION49.text 
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
    # grammar/ShyRecognizerBackend.g:236:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID50 = None
        types_items51 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:239:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:239:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types1950)

                self.match(self.input, DOWN, None)
                ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_types1952)

                self._state.following.append(self.FOLLOW_types_items_in_types1954)
                types_items51 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID50.text , types_items51 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:243:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item52 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:246:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:246:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:246:9: ( types_item )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == TREE_TYPES_ITEM) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerBackend.g:246:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items2009)
                        types_item52 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item52 is not None) and [types_item52.name] or [None])[0] ] = ((types_item52 is not None) and [types_item52.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:251:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID53 = None
        attrs_hints54 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:253:5: ( ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:253:9: ^( TREE_TYPES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item2064)

                self.match(self.input, DOWN, None)
                ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2066)

                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2068)
                attrs_hints54 = self.attrs_hints()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID53.text , attrs_hints54 
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
    # grammar/ShyRecognizerBackend.g:257:1: messages returns [ title , content ] : ^( TREE_MESSAGES ID messages_items ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        ID55 = None
        messages_items56 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:260:5: ( ^( TREE_MESSAGES ID messages_items ) )
                # grammar/ShyRecognizerBackend.g:260:9: ^( TREE_MESSAGES ID messages_items )
                pass 
                self.match(self.input, TREE_MESSAGES, self.FOLLOW_TREE_MESSAGES_in_messages2123)

                self.match(self.input, DOWN, None)
                ID55 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2125)

                self._state.following.append(self.FOLLOW_messages_items_in_messages2127)
                messages_items56 = self.messages_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID55.text , messages_items56 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "messages"



    # $ANTLR start "messages_items"
    # grammar/ShyRecognizerBackend.g:264:1: messages_items returns [ value ] : ( messages_item )+ ;
    def messages_items(self, ):
        value = None


        messages_item57 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:267:5: ( ( messages_item )+ )
                # grammar/ShyRecognizerBackend.g:267:9: ( messages_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:267:9: ( messages_item )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == TREE_MESSAGES_ITEM) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerBackend.g:267:11: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages_items2182)
                        messages_item57 = self.messages_item()

                        self._state.following.pop()

                        #action start
                        value [ ((messages_item57 is not None) and [messages_item57.name] or [None])[0] ] = ((messages_item57 is not None) and [messages_item57.value] or [None])[0] 
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
    # grammar/ShyRecognizerBackend.g:272:1: messages_item returns [ name , value ] : ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        ID58 = None
        attrs_hints59 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:274:5: ( ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerBackend.g:274:9: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                pass 
                self.match(self.input, TREE_MESSAGES_ITEM, self.FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2237)

                self.match(self.input, DOWN, None)
                ID58 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2239)

                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2241)
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

    # $ANTLR end "messages_item"



    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerBackend.g:278:1: attrs_hints returns [ value ] : TREE_ATTRS_HINTS ( attr_hint )* ;
    def attrs_hints(self, ):
        value = None


        attr_hint60 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:281:5: ( TREE_ATTRS_HINTS ( attr_hint )* )
                # grammar/ShyRecognizerBackend.g:281:9: TREE_ATTRS_HINTS ( attr_hint )*
                pass 
                self.match(self.input, TREE_ATTRS_HINTS, self.FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2294)

                # grammar/ShyRecognizerBackend.g:281:26: ( attr_hint )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == TREE_ATTR_HINT) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerBackend.g:281:28: attr_hint
                        pass 
                        self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2298)
                        attr_hint60 = self.attr_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( attr_hint60 ) 
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
    # grammar/ShyRecognizerBackend.g:284:1: attr_hint returns [ value ] : ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        value = None


        ID61 = None
        ID62 = None
        hint63 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:287:5: ( ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
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
                    # grammar/ShyRecognizerBackend.g:287:9: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2343)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_attr_hint2345)

                    # grammar/ShyRecognizerBackend.g:287:42: ( ^( TREE_ATTR ID ) )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == TREE_ATTR) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerBackend.g:287:44: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2351)

                            self.match(self.input, DOWN, None)
                            ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2353)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID61.text ] = dict ( ) 
                            #action end



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    self.match(self.input, UP, None)



                elif alt24 == 2:
                    # grammar/ShyRecognizerBackend.g:290:9: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    pass 
                    self.match(self.input, TREE_ATTR_HINT, self.FOLLOW_TREE_ATTR_HINT_in_attr_hint2395)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2397)
                    hint63 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:290:32: ( ^( TREE_ATTR ID ) )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == TREE_ATTR) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerBackend.g:290:34: ^( TREE_ATTR ID )
                            pass 
                            self.match(self.input, TREE_ATTR, self.FOLLOW_TREE_ATTR_in_attr_hint2403)

                            self.match(self.input, DOWN, None)
                            ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2405)

                            self.match(self.input, UP, None)


                            #action start
                            value [ ID62.text ] = hint63 
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
    # grammar/ShyRecognizerBackend.g:295:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID64 = None
        ID65 = None
        hint_args66 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:298:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
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
                    # grammar/ShyRecognizerBackend.g:298:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2474)

                    self.match(self.input, DOWN, None)
                    ID64 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2476)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID64.text ] = list ( ) 
                    #action end



                elif alt25 == 2:
                    # grammar/ShyRecognizerBackend.g:300:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint2504)

                    self.match(self.input, DOWN, None)
                    ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2506)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint2508)
                    hint_args66 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID65.text ] = hint_args66 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:304:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg67 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:307:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:307:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:307:9: ( hint_arg )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ID or LA26_0 == UNDERSCORE) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerBackend.g:307:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args2563)
                        hint_arg67 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg67 ) 
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
    # grammar/ShyRecognizerBackend.g:310:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID68 = None
        UNDERSCORE69 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:312:5: ( ID | UNDERSCORE )
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
                    # grammar/ShyRecognizerBackend.g:312:9: ID
                    pass 
                    ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg2596)

                    #action start
                    value = ID68.text 
                    #action end



                elif alt27 == 2:
                    # grammar/ShyRecognizerBackend.g:313:9: UNDERSCORE
                    pass 
                    UNDERSCORE69 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg2608)

                    #action start
                    value = UNDERSCORE69.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:316:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS70 = None
        NUMBER71 = None
        NUMBER72 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:318:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:318:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:318:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:318:11: MINUS NUMBER
                    pass 
                    MINUS70 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2639)

                    NUMBER71 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2641)




                    #action start
                    value = int ( MINUS70.text + NUMBER71.text ) 
                    #action end



                elif alt28 == 2:
                    # grammar/ShyRecognizerBackend.g:320:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:320:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:320:11: NUMBER
                    pass 
                    NUMBER72 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2669)




                    #action start
                    value = int ( NUMBER72.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:324:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS73 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:326:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:326:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:326:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:326:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS73 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2714)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2720)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2722)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2728)




                    #action start
                                
                    value = Fraction ( int ( MINUS73.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt29 == 2:
                    # grammar/ShyRecognizerBackend.g:331:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:331:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:331:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2760)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2762)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2768)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 41, 47, 49, 58, 66])
    FOLLOW_stateless_in_start114 = frozenset([1, 41, 47, 49, 58, 66])
    FOLLOW_consts_in_start141 = frozenset([1, 41, 47, 49, 58, 66])
    FOLLOW_types_in_start167 = frozenset([1, 41, 47, 49, 58, 66])
    FOLLOW_messages_in_start193 = frozenset([1, 41, 47, 49, 58, 66])
    FOLLOW_TREE_MODULE_in_module248 = frozenset([2])
    FOLLOW_ID_in_module250 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless283 = frozenset([2])
    FOLLOW_ID_in_stateless285 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless313 = frozenset([2])
    FOLLOW_ID_in_stateless315 = frozenset([55])
    FOLLOW_procs_in_stateless317 = frozenset([3])
    FOLLOW_proc_in_procs372 = frozenset([1, 55])
    FOLLOW_TREE_PROC_in_proc417 = frozenset([2])
    FOLLOW_ID_in_proc431 = frozenset([3, 56, 57, 59])
    FOLLOW_proc_args_in_proc465 = frozenset([3, 57, 59])
    FOLLOW_proc_vars_in_proc515 = frozenset([3, 59])
    FOLLOW_statements_in_proc565 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args638 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_args640 = frozenset([3])
    FOLLOW_TREE_PROC_VARS_in_proc_vars685 = frozenset([2])
    FOLLOW_attrs_hints_in_proc_vars687 = frozenset([3])
    FOLLOW_TREE_STATEMENTS_in_statements742 = frozenset([2])
    FOLLOW_statement_in_statements746 = frozenset([3, 60, 61, 64, 65])
    FOLLOW_statement_call_in_statement802 = frozenset([1])
    FOLLOW_statement_if_in_statement826 = frozenset([1])
    FOLLOW_statement_assign_in_statement850 = frozenset([1])
    FOLLOW_statement_with_in_statement874 = frozenset([1])
    FOLLOW_TREE_STATEMENT_WITH_in_statement_with917 = frozenset([2])
    FOLLOW_ID_in_statement_with919 = frozenset([59])
    FOLLOW_statements_in_statement_with921 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ASSIGN_in_statement_assign962 = frozenset([2])
    FOLLOW_arbitrary_value_in_statement_assign964 = frozenset([19])
    FOLLOW_ID_in_statement_assign994 = frozenset([3, 19])
    FOLLOW_TREE_STATEMENT_IF_in_statement_if1077 = frozenset([2])
    FOLLOW_statement_elif_in_statement_if1093 = frozenset([3, 62, 63])
    FOLLOW_statement_else_in_statement_if1143 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1216 = frozenset([2])
    FOLLOW_condition_any_in_statement_elif1218 = frozenset([59])
    FOLLOW_statements_in_statement_elif1220 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELIF_in_statement_elif1248 = frozenset([2])
    FOLLOW_condition_all_in_statement_elif1250 = frozenset([59])
    FOLLOW_statements_in_statement_elif1252 = frozenset([3])
    FOLLOW_TREE_STATEMENT_ELSE_in_statement_else1297 = frozenset([2])
    FOLLOW_statements_in_statement_else1299 = frozenset([3])
    FOLLOW_TREE_CONDITION_ANY_in_condition_any1354 = frozenset([2])
    FOLLOW_statement_call_in_condition_any1370 = frozenset([3, 61])
    FOLLOW_TREE_CONDITION_ALL_in_condition_all1445 = frozenset([2])
    FOLLOW_statement_call_in_condition_all1461 = frozenset([3, 61])
    FOLLOW_TREE_STATEMENT_CALL_in_statement_call1526 = frozenset([2])
    FOLLOW_statement_call_args_in_statement_call1528 = frozenset([3])
    FOLLOW_arbitrary_value_in_statement_call_args1583 = frozenset([1, 18, 19, 23, 26])
    FOLLOW_ID_in_arbitrary_value1636 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1648 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1660 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1672 = frozenset([1])
    FOLLOW_TREE_CONSTS_in_consts1713 = frozenset([2])
    FOLLOW_ID_in_consts1715 = frozenset([44, 50, 51])
    FOLLOW_consts_items_in_consts1717 = frozenset([3])
    FOLLOW_consts_item_in_consts_items1772 = frozenset([1, 44, 50, 51])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item1827 = frozenset([2])
    FOLLOW_ID_in_consts_item1829 = frozenset([23, 26])
    FOLLOW_num_whole_in_consts_item1831 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item1859 = frozenset([2])
    FOLLOW_ID_in_consts_item1861 = frozenset([23, 26])
    FOLLOW_num_fract_in_consts_item1863 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item1891 = frozenset([2])
    FOLLOW_ID_in_consts_item1893 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1895 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types1950 = frozenset([2])
    FOLLOW_ID_in_types1952 = frozenset([67])
    FOLLOW_types_items_in_types1954 = frozenset([3])
    FOLLOW_types_item_in_types_items2009 = frozenset([1, 67])
    FOLLOW_TREE_TYPES_ITEM_in_types_item2064 = frozenset([2])
    FOLLOW_ID_in_types_item2066 = frozenset([37])
    FOLLOW_attrs_hints_in_types_item2068 = frozenset([3])
    FOLLOW_TREE_MESSAGES_in_messages2123 = frozenset([2])
    FOLLOW_ID_in_messages2125 = frozenset([48])
    FOLLOW_messages_items_in_messages2127 = frozenset([3])
    FOLLOW_messages_item_in_messages_items2182 = frozenset([1, 48])
    FOLLOW_TREE_MESSAGES_ITEM_in_messages_item2237 = frozenset([2])
    FOLLOW_ID_in_messages_item2239 = frozenset([37])
    FOLLOW_attrs_hints_in_messages_item2241 = frozenset([3])
    FOLLOW_TREE_ATTRS_HINTS_in_attrs_hints2294 = frozenset([1, 38])
    FOLLOW_attr_hint_in_attrs_hints2298 = frozenset([1, 38])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2343 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_attr_hint2345 = frozenset([36])
    FOLLOW_TREE_ATTR_in_attr_hint2351 = frozenset([2])
    FOLLOW_ID_in_attr_hint2353 = frozenset([3])
    FOLLOW_TREE_ATTR_HINT_in_attr_hint2395 = frozenset([2])
    FOLLOW_hint_in_attr_hint2397 = frozenset([36])
    FOLLOW_TREE_ATTR_in_attr_hint2403 = frozenset([2])
    FOLLOW_ID_in_attr_hint2405 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2474 = frozenset([2])
    FOLLOW_ID_in_hint2476 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint2504 = frozenset([2])
    FOLLOW_ID_in_hint2506 = frozenset([19, 69])
    FOLLOW_hint_args_in_hint2508 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args2563 = frozenset([1, 19, 69])
    FOLLOW_ID_in_hint_arg2596 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg2608 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2639 = frozenset([26])
    FOLLOW_NUMBER_in_num_whole2641 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole2669 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2714 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2720 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2722 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2728 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract2760 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2762 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2768 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
