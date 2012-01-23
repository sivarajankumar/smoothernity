# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-23 14:34:22

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
ARROW_LEFT=4
ARROW_RIGHT=5
CONSTS=6
COPY=7
CURLY_CLOSE=8
CURLY_OPEN=9
DEDENT=10
DIVIDE=11
EXPRESSION=12
ID=13
INDENT=14
MINUS=15
MODULE=16
NEWLINE=17
NUMBER=18
PASTE=19
PROC=20
REPLACE=21
STATELESS=22
STRING=23
TREE_ARBITRARY_TOKEN=24
TREE_CONSTS=25
TREE_COPY=26
TREE_COPY_PASTE=27
TREE_EXPRESSION=28
TREE_HINT=29
TREE_HINT_NONE=30
TREE_MODULE=31
TREE_NUM_FRACT=32
TREE_NUM_WHOLE=33
TREE_PASTE=34
TREE_PASTE_REPLACE=35
TREE_PASTE_WITH=36
TREE_PROC=37
TREE_STATELESS=38
TREE_TYPES=39
TREE_TYPES_ITEM=40
TREE_TYPES_ITEM_ATTR=41
TREE_TYPES_ITEM_HINT=42
TREE_TYPES_ITEM_HINTS=43
TYPES=44
UNDERSCORE=45
WHITESPACE=46
WITH=47

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", "CURLY_OPEN", 
    "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", "MODULE", 
    "NEWLINE", "NUMBER", "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", 
    "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_STATELESS", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_TYPES_ITEM_ATTR", 
    "TREE_TYPES_ITEM_HINT", "TREE_TYPES_ITEM_HINTS", "TYPES", "UNDERSCORE", 
    "WHITESPACE", "WITH"
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
    # grammar/ShyRecognizerBackend.g:67:1: proc returns [ title , content ] : ^( TREE_PROC ID ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        ID10 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:69:5: ( ^( TREE_PROC ID ) )
                # grammar/ShyRecognizerBackend.g:69:9: ^( TREE_PROC ID )
                pass 
                self.match(self.input, TREE_PROC, self.FOLLOW_TREE_PROC_in_proc381)

                self.match(self.input, DOWN, None)
                ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_proc383)

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID10.text , dict ( ) 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "proc"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:73:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID11 = None
        consts_items12 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:76:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:76:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts438)

                self.match(self.input, DOWN, None)
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_consts440)

                self._state.following.append(self.FOLLOW_consts_items_in_consts442)
                consts_items12 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID11.text , consts_items12 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:80:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item13 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:83:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:83:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:83:9: ( consts_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA4_0 <= TREE_NUM_WHOLE)) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerBackend.g:83:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items497)
                        consts_item13 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item13 is not None) and [consts_item13.name] or [None])[0] ] = ((consts_item13 is not None) and [consts_item13.value] or [None])[0] 
                        #action end



                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1





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
    # grammar/ShyRecognizerBackend.g:88:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID14 = None
        ID16 = None
        ID18 = None
        EXPRESSION19 = None
        num_whole15 = None

        num_fract17 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:90:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt5 = 3
                LA5 = self.input.LA(1)
                if LA5 == TREE_NUM_WHOLE:
                    alt5 = 1
                elif LA5 == TREE_NUM_FRACT:
                    alt5 = 2
                elif LA5 == TREE_EXPRESSION:
                    alt5 = 3
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:90:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item552)

                    self.match(self.input, DOWN, None)
                    ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item554)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item556)
                    num_whole15 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID14.text , num_whole15 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyRecognizerBackend.g:92:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item584)

                    self.match(self.input, DOWN, None)
                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item586)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item588)
                    num_fract17 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID16.text , num_fract17 
                    #action end



                elif alt5 == 3:
                    # grammar/ShyRecognizerBackend.g:94:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item616)

                    self.match(self.input, DOWN, None)
                    ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item618)

                    EXPRESSION19 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item620)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID18.text , EXPRESSION19.text 
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
    # grammar/ShyRecognizerBackend.g:98:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID20 = None
        types_items21 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:101:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:101:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types675)

                self.match(self.input, DOWN, None)
                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_types677)

                self._state.following.append(self.FOLLOW_types_items_in_types679)
                types_items21 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID20.text , types_items21 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:105:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item22 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:108:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:108:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:108:9: ( types_item )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TREE_TYPES_ITEM) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyRecognizerBackend.g:108:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items734)
                        types_item22 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item22 is not None) and [types_item22.name] or [None])[0] ] = ((types_item22 is not None) and [types_item22.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:113:1: types_item returns [ name , value ] : ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) );
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID23 = None
        ID25 = None
        types_item_hints24 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:115:5: ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == TREE_TYPES_ITEM) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == 2) :
                        LA7_2 = self.input.LA(3)

                        if (LA7_2 == ID) :
                            LA7_3 = self.input.LA(4)

                            if (LA7_3 == TREE_TYPES_ITEM_HINTS) :
                                LA7_4 = self.input.LA(5)

                                if (LA7_4 == 3) :
                                    alt7 = 2
                                elif (LA7_4 == TREE_TYPES_ITEM_HINT) :
                                    alt7 = 1
                                else:
                                    nvae = NoViableAltException("", 7, 4, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 7, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 7, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammar/ShyRecognizerBackend.g:115:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item789)

                    self.match(self.input, DOWN, None)
                    ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item791)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item793)

                    self._state.following.append(self.FOLLOW_types_item_hints_in_types_item795)
                    types_item_hints24 = self.types_item_hints()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID23.text , types_item_hints24 
                    #action end



                elif alt7 == 2:
                    # grammar/ShyRecognizerBackend.g:117:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item823)

                    self.match(self.input, DOWN, None)
                    ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item825)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item827)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID25.text , dict ( ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "types_item_hints"
    # grammar/ShyRecognizerBackend.g:121:1: types_item_hints returns [ value ] : ( types_item_hint )+ ;
    def types_item_hints(self, ):
        value = None


        types_item_hint26 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:124:5: ( ( types_item_hint )+ )
                # grammar/ShyRecognizerBackend.g:124:9: ( types_item_hint )+
                pass 
                # grammar/ShyRecognizerBackend.g:124:9: ( types_item_hint )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == TREE_TYPES_ITEM_HINT) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerBackend.g:124:11: types_item_hint
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_hint_in_types_item_hints882)
                        types_item_hint26 = self.types_item_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( types_item_hint26 ) 
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

    # $ANTLR end "types_item_hints"



    # $ANTLR start "types_item_hint"
    # grammar/ShyRecognizerBackend.g:127:1: types_item_hint returns [ value ] : ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        value = None


        types_item_attr27 = None

        types_item_attr28 = None

        hint29 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:130:5: ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == TREE_TYPES_ITEM_HINT) :
                    LA11_1 = self.input.LA(2)

                    if (LA11_1 == 2) :
                        LA11_2 = self.input.LA(3)

                        if (LA11_2 == TREE_HINT_NONE) :
                            alt11 = 1
                        elif (LA11_2 == TREE_HINT) :
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
                    # grammar/ShyRecognizerBackend.g:130:9: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint927)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_types_item_hint929)

                    # grammar/ShyRecognizerBackend.g:130:48: ( types_item_attr )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == TREE_TYPES_ITEM_ATTR) :
                            alt9 = 1


                        if alt9 == 1:
                            # grammar/ShyRecognizerBackend.g:130:50: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint933)
                            types_item_attr27 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr27 ] = dict ( ) 
                            #action end



                        else:
                            if cnt9 >= 1:
                                break #loop9

                            eee = EarlyExitException(9, self.input)
                            raise eee

                        cnt9 += 1


                    self.match(self.input, UP, None)



                elif alt11 == 2:
                    # grammar/ShyRecognizerBackend.g:133:9: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint973)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint975)
                    hint29 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:133:38: ( types_item_attr )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == TREE_TYPES_ITEM_ATTR) :
                            alt10 = 1


                        if alt10 == 1:
                            # grammar/ShyRecognizerBackend.g:133:40: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint979)
                            types_item_attr28 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr28 ] = hint29 
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

    # $ANTLR end "types_item_hint"



    # $ANTLR start "types_item_attr"
    # grammar/ShyRecognizerBackend.g:138:1: types_item_attr returns [ value ] : ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        value = None


        ID30 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:140:5: ( ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/ShyRecognizerBackend.g:140:9: ^( TREE_TYPES_ITEM_ATTR ID )
                pass 
                self.match(self.input, TREE_TYPES_ITEM_ATTR, self.FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr1036)

                self.match(self.input, DOWN, None)
                ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr1038)

                self.match(self.input, UP, None)


                #action start
                value = ID30.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "types_item_attr"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:143:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID31 = None
        ID32 = None
        hint_args33 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:146:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == TREE_HINT) :
                    LA12_1 = self.input.LA(2)

                    if (LA12_1 == 2) :
                        LA12_2 = self.input.LA(3)

                        if (LA12_2 == ID) :
                            LA12_3 = self.input.LA(4)

                            if (LA12_3 == 3) :
                                alt12 = 1
                            elif (LA12_3 == ID or LA12_3 == UNDERSCORE) :
                                alt12 = 2
                            else:
                                nvae = NoViableAltException("", 12, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerBackend.g:146:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1081)

                    self.match(self.input, DOWN, None)
                    ID31 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1083)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID31.text ] = list ( ) 
                    #action end



                elif alt12 == 2:
                    # grammar/ShyRecognizerBackend.g:148:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint1111)

                    self.match(self.input, DOWN, None)
                    ID32 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1113)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint1115)
                    hint_args33 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID32.text ] = hint_args33 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:152:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg34 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:155:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:155:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:155:9: ( hint_arg )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == ID or LA13_0 == UNDERSCORE) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerBackend.g:155:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args1170)
                        hint_arg34 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg34 ) 
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

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:158:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID35 = None
        UNDERSCORE36 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:160:5: ( ID | UNDERSCORE )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == ID) :
                    alt14 = 1
                elif (LA14_0 == UNDERSCORE) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyRecognizerBackend.g:160:9: ID
                    pass 
                    ID35 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1203)

                    #action start
                    value = ID35.text 
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:161:9: UNDERSCORE
                    pass 
                    UNDERSCORE36 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1215)

                    #action start
                    value = UNDERSCORE36.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:164:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS37 = None
        NUMBER38 = None
        NUMBER39 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:166:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == MINUS) :
                    alt15 = 1
                elif (LA15_0 == NUMBER) :
                    alt15 = 2
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerBackend.g:166:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:166:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:166:11: MINUS NUMBER
                    pass 
                    MINUS37 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1246)

                    NUMBER38 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1248)




                    #action start
                    value = int ( MINUS37.text + NUMBER38.text ) 
                    #action end



                elif alt15 == 2:
                    # grammar/ShyRecognizerBackend.g:168:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:168:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:168:11: NUMBER
                    pass 
                    NUMBER39 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1276)




                    #action start
                    value = int ( NUMBER39.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:172:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS40 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:174:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == MINUS) :
                    alt16 = 1
                elif (LA16_0 == NUMBER) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammar/ShyRecognizerBackend.g:174:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:174:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:174:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS40 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1321)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1327)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1329)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1335)




                    #action start
                                
                    value = Fraction ( int ( MINUS40.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt16 == 2:
                    # grammar/ShyRecognizerBackend.g:179:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:179:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:179:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1367)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1369)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1375)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 25, 31, 38, 39])
    FOLLOW_stateless_in_start114 = frozenset([1, 25, 31, 38, 39])
    FOLLOW_consts_in_start141 = frozenset([1, 25, 31, 38, 39])
    FOLLOW_types_in_start167 = frozenset([1, 25, 31, 38, 39])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless287 = frozenset([2])
    FOLLOW_ID_in_stateless289 = frozenset([37])
    FOLLOW_procs_in_stateless291 = frozenset([3])
    FOLLOW_proc_in_procs346 = frozenset([1, 37])
    FOLLOW_TREE_PROC_in_proc381 = frozenset([2])
    FOLLOW_ID_in_proc383 = frozenset([3])
    FOLLOW_TREE_CONSTS_in_consts438 = frozenset([2])
    FOLLOW_ID_in_consts440 = frozenset([28, 32, 33])
    FOLLOW_consts_items_in_consts442 = frozenset([3])
    FOLLOW_consts_item_in_consts_items497 = frozenset([1, 28, 32, 33])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item552 = frozenset([2])
    FOLLOW_ID_in_consts_item554 = frozenset([15, 18])
    FOLLOW_num_whole_in_consts_item556 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item584 = frozenset([2])
    FOLLOW_ID_in_consts_item586 = frozenset([15, 18])
    FOLLOW_num_fract_in_consts_item588 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item616 = frozenset([2])
    FOLLOW_ID_in_consts_item618 = frozenset([12])
    FOLLOW_EXPRESSION_in_consts_item620 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types675 = frozenset([2])
    FOLLOW_ID_in_types677 = frozenset([40])
    FOLLOW_types_items_in_types679 = frozenset([3])
    FOLLOW_types_item_in_types_items734 = frozenset([1, 40])
    FOLLOW_TREE_TYPES_ITEM_in_types_item789 = frozenset([2])
    FOLLOW_ID_in_types_item791 = frozenset([43])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item793 = frozenset([42])
    FOLLOW_types_item_hints_in_types_item795 = frozenset([3])
    FOLLOW_TREE_TYPES_ITEM_in_types_item823 = frozenset([2])
    FOLLOW_ID_in_types_item825 = frozenset([43])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item827 = frozenset([3])
    FOLLOW_types_item_hint_in_types_item_hints882 = frozenset([1, 42])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint927 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_types_item_hint929 = frozenset([41])
    FOLLOW_types_item_attr_in_types_item_hint933 = frozenset([3, 41])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint973 = frozenset([2])
    FOLLOW_hint_in_types_item_hint975 = frozenset([41])
    FOLLOW_types_item_attr_in_types_item_hint979 = frozenset([3, 41])
    FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr1036 = frozenset([2])
    FOLLOW_ID_in_types_item_attr1038 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1081 = frozenset([2])
    FOLLOW_ID_in_hint1083 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint1111 = frozenset([2])
    FOLLOW_ID_in_hint1113 = frozenset([13, 45])
    FOLLOW_hint_args_in_hint1115 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args1170 = frozenset([1, 13, 45])
    FOLLOW_ID_in_hint_arg1203 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1215 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1246 = frozenset([18])
    FOLLOW_NUMBER_in_num_whole1248 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1276 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1321 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1327 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract1329 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1335 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1367 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract1369 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1375 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
