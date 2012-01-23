# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-23 18:29:34

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
PASTE=20
PROC=21
REPLACE=22
STATELESS=23
STRING=24
TREE_ARBITRARY_TOKEN=25
TREE_CONSTS=26
TREE_COPY=27
TREE_COPY_PASTE=28
TREE_EXPRESSION=29
TREE_HINT=30
TREE_HINT_NONE=31
TREE_MODULE=32
TREE_NUM_FRACT=33
TREE_NUM_WHOLE=34
TREE_PASTE=35
TREE_PASTE_REPLACE=36
TREE_PASTE_WITH=37
TREE_PROC=38
TREE_PROC_ARGS=39
TREE_STATELESS=40
TREE_TYPES=41
TREE_TYPES_ITEM=42
TREE_TYPES_ITEM_ATTR=43
TREE_TYPES_ITEM_HINT=44
TREE_TYPES_ITEM_HINTS=45
TYPES=46
UNDERSCORE=47
WHITESPACE=48
WITH=49

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NEWLINE", "NUMBER", "PASTE", "PROC", "REPLACE", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_STATELESS", "TREE_TYPES", "TREE_TYPES_ITEM", 
    "TREE_TYPES_ITEM_ATTR", "TREE_TYPES_ITEM_HINT", "TREE_TYPES_ITEM_HINTS", 
    "TYPES", "UNDERSCORE", "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:67:1: proc returns [ title , content ] : ( ^( TREE_PROC ID ) | ^( TREE_PROC ID proc_args ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID10 = None
        ID11 = None
        proc_args12 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:69:5: ( ^( TREE_PROC ID ) | ^( TREE_PROC ID proc_args ) )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == TREE_PROC) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 2) :
                        LA4_2 = self.input.LA(3)

                        if (LA4_2 == ID) :
                            LA4_3 = self.input.LA(4)

                            if (LA4_3 == 3) :
                                alt4 = 1
                            elif (LA4_3 == TREE_PROC_ARGS) :
                                alt4 = 2
                            else:
                                nvae = NoViableAltException("", 4, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 4, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # grammar/ShyRecognizerBackend.g:69:9: ^( TREE_PROC ID )
                    pass 
                    self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc381)

                    self.match(self.input, DOWN, None)
                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_proc383)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID10.text , dict ( ) 
                    #action end



                elif alt4 == 2:
                    # grammar/ShyRecognizerBackend.g:71:9: ^( TREE_PROC ID proc_args )
                    pass 
                    self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc411)

                    self.match(self.input, DOWN, None)
                    ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_proc413)

                    self._state.following.append(self.FOLLOW_proc_args_in_proc415)
                    proc_args12 = self.proc_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID11.text , { 'args' : proc_args12 } 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "proc"



    # $ANTLR start "proc_args"
    # grammar/ShyRecognizerBackend.g:75:1: proc_args returns [ value ] : ^( TREE_PROC_ARGS ( ID )+ ) ;
    def proc_args(self, ):
        value = None


        ID13 = None

        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:78:5: ( ^( TREE_PROC_ARGS ( ID )+ ) )
                # grammar/ShyRecognizerBackend.g:78:9: ^( TREE_PROC_ARGS ( ID )+ )
                pass 
                self.match(self.input, TREE_PROC_ARGS, self.FOLLOW_TREE_PROC_ARGS_in_proc_args470)

                self.match(self.input, DOWN, None)
                # grammar/ShyRecognizerBackend.g:78:27: ( ID )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == ID) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/ShyRecognizerBackend.g:78:29: ID
                        pass 
                        ID13 = self.match(self.input, ID, self.FOLLOW_ID_in_proc_args474)

                        #action start
                        value [ ID13.text ] = dict ( ) 
                        #action end



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1


                self.match(self.input, UP, None)





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "proc_args"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:81:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID14 = None
        consts_items15 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:84:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:84:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts521)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_consts523)

                self._state.following.append(self.FOLLOW_consts_items_in_consts525)
                consts_items15 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID14.text , consts_items15 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:88:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item16 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:91:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:91:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:91:9: ( consts_item )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA6_0 <= TREE_NUM_WHOLE)) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyRecognizerBackend.g:91:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items580)
                        consts_item16 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item16 is not None) and [consts_item16.name] or [None])[0] ] = ((consts_item16 is not None) and [consts_item16.value] or [None])[0] 
                        #action end



                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1





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
    # grammar/ShyRecognizerBackend.g:96:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID17 = None
        ID19 = None
        ID21 = None
        EXPRESSION22 = None
        num_whole18 = None

        num_fract20 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:98:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt7 = 3
                LA7 = self.input.LA(1)
                if LA7 == TREE_NUM_WHOLE:
                    alt7 = 1
                elif LA7 == TREE_NUM_FRACT:
                    alt7 = 2
                elif LA7 == TREE_EXPRESSION:
                    alt7 = 3
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:98:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item635)

                    self.match(self.input, DOWN, None)
                    ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item637)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item639)
                    num_whole18 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID17.text , num_whole18 
                    #action end



                elif alt7 == 2:
                    # grammar/ShyRecognizerBackend.g:100:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item667)

                    self.match(self.input, DOWN, None)
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item669)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item671)
                    num_fract20 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID19.text , num_fract20 
                    #action end



                elif alt7 == 3:
                    # grammar/ShyRecognizerBackend.g:102:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item699)

                    self.match(self.input, DOWN, None)
                    ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item701)

                    EXPRESSION22 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item703)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID21.text , EXPRESSION22.text 
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
    # grammar/ShyRecognizerBackend.g:106:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID23 = None
        types_items24 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:109:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:109:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types758)

                self.match(self.input, DOWN, None)
                ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_types760)

                self._state.following.append(self.FOLLOW_types_items_in_types762)
                types_items24 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID23.text , types_items24 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:113:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item25 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:116:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:116:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:116:9: ( types_item )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == TREE_TYPES_ITEM) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerBackend.g:116:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items817)
                        types_item25 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item25 is not None) and [types_item25.name] or [None])[0] ] = ((types_item25 is not None) and [types_item25.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:121:1: types_item returns [ name , value ] : ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) );
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID26 = None
        ID28 = None
        types_item_hints27 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:123:5: ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == TREE_TYPES_ITEM) :
                    LA9_1 = self.input.LA(2)

                    if (LA9_1 == 2) :
                        LA9_2 = self.input.LA(3)

                        if (LA9_2 == ID) :
                            LA9_3 = self.input.LA(4)

                            if (LA9_3 == TREE_TYPES_ITEM_HINTS) :
                                LA9_4 = self.input.LA(5)

                                if (LA9_4 == 3) :
                                    alt9 = 2
                                elif (LA9_4 == TREE_TYPES_ITEM_HINT) :
                                    alt9 = 1
                                else:
                                    nvae = NoViableAltException("", 9, 4, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 9, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 9, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 9, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammar/ShyRecognizerBackend.g:123:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item872)

                    self.match(self.input, DOWN, None)
                    ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item874)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item876)

                    self._state.following.append(self.FOLLOW_types_item_hints_in_types_item878)
                    types_item_hints27 = self.types_item_hints()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID26.text , types_item_hints27 
                    #action end



                elif alt9 == 2:
                    # grammar/ShyRecognizerBackend.g:125:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item906)

                    self.match(self.input, DOWN, None)
                    ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item908)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item910)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID28.text , dict ( ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "types_item_hints"
    # grammar/ShyRecognizerBackend.g:129:1: types_item_hints returns [ value ] : ( types_item_hint )+ ;
    def types_item_hints(self, ):
        value = None


        types_item_hint29 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:132:5: ( ( types_item_hint )+ )
                # grammar/ShyRecognizerBackend.g:132:9: ( types_item_hint )+
                pass 
                # grammar/ShyRecognizerBackend.g:132:9: ( types_item_hint )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == TREE_TYPES_ITEM_HINT) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerBackend.g:132:11: types_item_hint
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_hint_in_types_item_hints965)
                        types_item_hint29 = self.types_item_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( types_item_hint29 ) 
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

    # $ANTLR end "types_item_hints"



    # $ANTLR start "types_item_hint"
    # grammar/ShyRecognizerBackend.g:135:1: types_item_hint returns [ value ] : ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        value = None


        types_item_attr30 = None

        types_item_attr31 = None

        hint32 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:138:5: ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == TREE_TYPES_ITEM_HINT) :
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
                    # grammar/ShyRecognizerBackend.g:138:9: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint1010)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_types_item_hint1012)

                    # grammar/ShyRecognizerBackend.g:138:48: ( types_item_attr )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == TREE_TYPES_ITEM_ATTR) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/ShyRecognizerBackend.g:138:50: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint1016)
                            types_item_attr30 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr30 ] = dict ( ) 
                            #action end



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    self.match(self.input, UP, None)



                elif alt13 == 2:
                    # grammar/ShyRecognizerBackend.g:141:9: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint1056)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint1058)
                    hint32 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:141:38: ( types_item_attr )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == TREE_TYPES_ITEM_ATTR) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyRecognizerBackend.g:141:40: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint1062)
                            types_item_attr31 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr31 ] = hint32 
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

    # $ANTLR end "types_item_hint"



    # $ANTLR start "types_item_attr"
    # grammar/ShyRecognizerBackend.g:146:1: types_item_attr returns [ value ] : ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        value = None


        ID33 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:148:5: ( ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/ShyRecognizerBackend.g:148:9: ^( TREE_TYPES_ITEM_ATTR ID )
                pass 
                self.match(self.input, TREE_TYPES_ITEM_ATTR, self.FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr1119)

                self.match(self.input, DOWN, None)
                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr1121)

                self.match(self.input, UP, None)


                #action start
                value = ID33.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "types_item_attr"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:151:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID34 = None
        ID35 = None
        hint_args36 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:154:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
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
                    # grammar/ShyRecognizerBackend.g:154:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1164)

                    self.match(self.input, DOWN, None)
                    ID34 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1166)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID34.text ] = list ( ) 
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:156:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1194)

                    self.match(self.input, DOWN, None)
                    ID35 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1196)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint1198)
                    hint_args36 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID35.text ] = hint_args36 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:160:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg37 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:163:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:163:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:163:9: ( hint_arg )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == ID or LA15_0 == UNDERSCORE) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerBackend.g:163:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args1253)
                        hint_arg37 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg37 ) 
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
    # grammar/ShyRecognizerBackend.g:166:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID38 = None
        UNDERSCORE39 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:168:5: ( ID | UNDERSCORE )
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
                    # grammar/ShyRecognizerBackend.g:168:9: ID
                    pass 
                    ID38 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1286)

                    #action start
                    value = ID38.text 
                    #action end



                elif alt16 == 2:
                    # grammar/ShyRecognizerBackend.g:169:9: UNDERSCORE
                    pass 
                    UNDERSCORE39 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1298)

                    #action start
                    value = UNDERSCORE39.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:172:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS40 = None
        NUMBER41 = None
        NUMBER42 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:174:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:174:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:174:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:174:11: MINUS NUMBER
                    pass 
                    MINUS40 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1329)

                    NUMBER41 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1331)




                    #action start
                    value = int ( MINUS40.text + NUMBER41.text ) 
                    #action end



                elif alt17 == 2:
                    # grammar/ShyRecognizerBackend.g:176:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:176:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:176:11: NUMBER
                    pass 
                    NUMBER42 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1359)




                    #action start
                    value = int ( NUMBER42.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:180:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS43 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:182:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:182:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:182:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:182:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS43 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1404)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1410)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1412)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1418)




                    #action start
                                
                    value = Fraction ( int ( MINUS43.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt18 == 2:
                    # grammar/ShyRecognizerBackend.g:187:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:187:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:187:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1450)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1452)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1458)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 26, 32, 40, 41])
    FOLLOW_stateless_in_start114 = frozenset([1, 26, 32, 40, 41])
    FOLLOW_consts_in_start141 = frozenset([1, 26, 32, 40, 41])
    FOLLOW_types_in_start167 = frozenset([1, 26, 32, 40, 41])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless287 = frozenset([2])
    FOLLOW_ID_in_stateless289 = frozenset([38])
    FOLLOW_procs_in_stateless291 = frozenset([3])
    FOLLOW_proc_in_procs346 = frozenset([1, 38])
    FOLLOW_TREE_PROC_in_proc381 = frozenset([2])
    FOLLOW_ID_in_proc383 = frozenset([3])
    FOLLOW_TREE_PROC_in_proc411 = frozenset([2])
    FOLLOW_ID_in_proc413 = frozenset([39])
    FOLLOW_proc_args_in_proc415 = frozenset([3])
    FOLLOW_TREE_PROC_ARGS_in_proc_args470 = frozenset([2])
    FOLLOW_ID_in_proc_args474 = frozenset([3, 14])
    FOLLOW_TREE_CONSTS_in_consts521 = frozenset([2])
    FOLLOW_ID_in_consts523 = frozenset([29, 33, 34])
    FOLLOW_consts_items_in_consts525 = frozenset([3])
    FOLLOW_consts_item_in_consts_items580 = frozenset([1, 29, 33, 34])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item635 = frozenset([2])
    FOLLOW_ID_in_consts_item637 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item639 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item667 = frozenset([2])
    FOLLOW_ID_in_consts_item669 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item671 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item699 = frozenset([2])
    FOLLOW_ID_in_consts_item701 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item703 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types758 = frozenset([2])
    FOLLOW_ID_in_types760 = frozenset([42])
    FOLLOW_types_items_in_types762 = frozenset([3])
    FOLLOW_types_item_in_types_items817 = frozenset([1, 42])
    FOLLOW_TREE_TYPES_ITEM_in_types_item872 = frozenset([2])
    FOLLOW_ID_in_types_item874 = frozenset([45])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item876 = frozenset([44])
    FOLLOW_types_item_hints_in_types_item878 = frozenset([3])
    FOLLOW_TREE_TYPES_ITEM_in_types_item906 = frozenset([2])
    FOLLOW_ID_in_types_item908 = frozenset([45])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item910 = frozenset([3])
    FOLLOW_types_item_hint_in_types_item_hints965 = frozenset([1, 44])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint1010 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_types_item_hint1012 = frozenset([43])
    FOLLOW_types_item_attr_in_types_item_hint1016 = frozenset([3, 43])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint1056 = frozenset([2])
    FOLLOW_hint_in_types_item_hint1058 = frozenset([43])
    FOLLOW_types_item_attr_in_types_item_hint1062 = frozenset([3, 43])
    FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr1119 = frozenset([2])
    FOLLOW_ID_in_types_item_attr1121 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1164 = frozenset([2])
    FOLLOW_ID_in_hint1166 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1194 = frozenset([2])
    FOLLOW_ID_in_hint1196 = frozenset([14, 47])
    FOLLOW_hint_args_in_hint1198 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args1253 = frozenset([1, 14, 47])
    FOLLOW_ID_in_hint_arg1286 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1298 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1329 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole1331 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1359 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1404 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1410 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1412 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1418 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1450 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1452 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1458 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
