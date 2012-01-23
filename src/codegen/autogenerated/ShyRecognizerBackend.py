# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-23 14:21:26

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
TREE_STATELESS=37
TREE_TYPES=38
TREE_TYPES_ITEM=39
TREE_TYPES_ITEM_ATTR=40
TREE_TYPES_ITEM_HINT=41
TREE_TYPES_ITEM_HINTS=42
TYPES=43
UNDERSCORE=44
WHITESPACE=45
WITH=46

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", "CURLY_OPEN", 
    "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", "MODULE", 
    "NEWLINE", "NUMBER", "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", 
    "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_STATELESS", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_TYPES_ITEM_ATTR", 
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
                            stateless2 , dict ( ) )
                                    
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



    # $ANTLR start "stateless"
    # grammar/ShyRecognizerBackend.g:53:1: stateless returns [ value ] : ^( TREE_STATELESS ID ) ;
    def stateless(self, ):
        value = None


        ID6 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:55:5: ( ^( TREE_STATELESS ID ) )
                # grammar/ShyRecognizerBackend.g:55:9: ^( TREE_STATELESS ID )
                pass 
                self.match(self.input, TREE_STATELESS, self.FOLLOW_TREE_STATELESS_in_stateless257)

                self.match(self.input, DOWN, None)
                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless259)

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

    # $ANTLR end "stateless"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:58:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID7 = None
        consts_items8 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:61:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:61:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts302)

                self.match(self.input, DOWN, None)
                ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_consts304)

                self._state.following.append(self.FOLLOW_consts_items_in_consts306)
                consts_items8 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID7.text , consts_items8 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerBackend.g:65:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item9 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:68:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:68:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:68:9: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA2_0 <= TREE_NUM_WHOLE)) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyRecognizerBackend.g:68:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items361)
                        consts_item9 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item9 is not None) and [consts_item9.name] or [None])[0] ] = ((consts_item9 is not None) and [consts_item9.value] or [None])[0] 
                        #action end



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1





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
    # grammar/ShyRecognizerBackend.g:73:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID10 = None
        ID12 = None
        ID14 = None
        EXPRESSION15 = None
        num_whole11 = None

        num_fract13 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:75:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt3 = 3
                LA3 = self.input.LA(1)
                if LA3 == TREE_NUM_WHOLE:
                    alt3 = 1
                elif LA3 == TREE_NUM_FRACT:
                    alt3 = 2
                elif LA3 == TREE_EXPRESSION:
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyRecognizerBackend.g:75:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item416)

                    self.match(self.input, DOWN, None)
                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item418)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item420)
                    num_whole11 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID10.text , num_whole11 
                    #action end



                elif alt3 == 2:
                    # grammar/ShyRecognizerBackend.g:77:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item448)

                    self.match(self.input, DOWN, None)
                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item450)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item452)
                    num_fract13 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID12.text , num_fract13 
                    #action end



                elif alt3 == 3:
                    # grammar/ShyRecognizerBackend.g:79:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item480)

                    self.match(self.input, DOWN, None)
                    ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item482)

                    EXPRESSION15 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item484)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID14.text , EXPRESSION15.text 
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
    # grammar/ShyRecognizerBackend.g:83:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID16 = None
        types_items17 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:86:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:86:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types539)

                self.match(self.input, DOWN, None)
                ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_types541)

                self._state.following.append(self.FOLLOW_types_items_in_types543)
                types_items17 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID16.text , types_items17 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # grammar/ShyRecognizerBackend.g:90:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item18 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:93:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:93:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:93:9: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == TREE_TYPES_ITEM) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerBackend.g:93:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items598)
                        types_item18 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item18 is not None) and [types_item18.name] or [None])[0] ] = ((types_item18 is not None) and [types_item18.value] or [None])[0] 
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

    # $ANTLR end "types_items"


    class types_item_return(TreeRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:98:1: types_item returns [ name , value ] : ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) );
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID19 = None
        ID21 = None
        types_item_hints20 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:100:5: ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == TREE_TYPES_ITEM) :
                    LA5_1 = self.input.LA(2)

                    if (LA5_1 == 2) :
                        LA5_2 = self.input.LA(3)

                        if (LA5_2 == ID) :
                            LA5_3 = self.input.LA(4)

                            if (LA5_3 == TREE_TYPES_ITEM_HINTS) :
                                LA5_4 = self.input.LA(5)

                                if (LA5_4 == 3) :
                                    alt5 = 2
                                elif (LA5_4 == TREE_TYPES_ITEM_HINT) :
                                    alt5 = 1
                                else:
                                    nvae = NoViableAltException("", 5, 4, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 5, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 5, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 5, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyRecognizerBackend.g:100:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item653)

                    self.match(self.input, DOWN, None)
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item655)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item657)

                    self._state.following.append(self.FOLLOW_types_item_hints_in_types_item659)
                    types_item_hints20 = self.types_item_hints()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID19.text , types_item_hints20 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyRecognizerBackend.g:102:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item687)

                    self.match(self.input, DOWN, None)
                    ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item689)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item691)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID21.text , dict ( ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "types_item_hints"
    # grammar/ShyRecognizerBackend.g:106:1: types_item_hints returns [ value ] : ( types_item_hint )+ ;
    def types_item_hints(self, ):
        value = None


        types_item_hint22 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:109:5: ( ( types_item_hint )+ )
                # grammar/ShyRecognizerBackend.g:109:9: ( types_item_hint )+
                pass 
                # grammar/ShyRecognizerBackend.g:109:9: ( types_item_hint )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TREE_TYPES_ITEM_HINT) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyRecognizerBackend.g:109:11: types_item_hint
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_hint_in_types_item_hints746)
                        types_item_hint22 = self.types_item_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( types_item_hint22 ) 
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

    # $ANTLR end "types_item_hints"



    # $ANTLR start "types_item_hint"
    # grammar/ShyRecognizerBackend.g:112:1: types_item_hint returns [ value ] : ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        value = None


        types_item_attr23 = None

        types_item_attr24 = None

        hint25 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:115:5: ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == TREE_TYPES_ITEM_HINT) :
                    LA9_1 = self.input.LA(2)

                    if (LA9_1 == 2) :
                        LA9_2 = self.input.LA(3)

                        if (LA9_2 == TREE_HINT_NONE) :
                            alt9 = 1
                        elif (LA9_2 == TREE_HINT) :
                            alt9 = 2
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
                    # grammar/ShyRecognizerBackend.g:115:9: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint791)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_types_item_hint793)

                    # grammar/ShyRecognizerBackend.g:115:48: ( types_item_attr )+
                    cnt7 = 0
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == TREE_TYPES_ITEM_ATTR) :
                            alt7 = 1


                        if alt7 == 1:
                            # grammar/ShyRecognizerBackend.g:115:50: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint797)
                            types_item_attr23 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr23 ] = dict ( ) 
                            #action end



                        else:
                            if cnt7 >= 1:
                                break #loop7

                            eee = EarlyExitException(7, self.input)
                            raise eee

                        cnt7 += 1


                    self.match(self.input, UP, None)



                elif alt9 == 2:
                    # grammar/ShyRecognizerBackend.g:118:9: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint837)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint839)
                    hint25 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:118:38: ( types_item_attr )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == TREE_TYPES_ITEM_ATTR) :
                            alt8 = 1


                        if alt8 == 1:
                            # grammar/ShyRecognizerBackend.g:118:40: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint843)
                            types_item_attr24 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr24 ] = hint25 
                            #action end



                        else:
                            if cnt8 >= 1:
                                break #loop8

                            eee = EarlyExitException(8, self.input)
                            raise eee

                        cnt8 += 1


                    self.match(self.input, UP, None)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "types_item_hint"



    # $ANTLR start "types_item_attr"
    # grammar/ShyRecognizerBackend.g:123:1: types_item_attr returns [ value ] : ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        value = None


        ID26 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:125:5: ( ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/ShyRecognizerBackend.g:125:9: ^( TREE_TYPES_ITEM_ATTR ID )
                pass 
                self.match(self.input, TREE_TYPES_ITEM_ATTR, self.FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr900)

                self.match(self.input, DOWN, None)
                ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr902)

                self.match(self.input, UP, None)


                #action start
                value = ID26.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "types_item_attr"



    # $ANTLR start "hint"
    # grammar/ShyRecognizerBackend.g:128:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID27 = None
        ID28 = None
        hint_args29 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:131:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == TREE_HINT) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == 2) :
                        LA10_2 = self.input.LA(3)

                        if (LA10_2 == ID) :
                            LA10_3 = self.input.LA(4)

                            if (LA10_3 == 3) :
                                alt10 = 1
                            elif (LA10_3 == ID or LA10_3 == UNDERSCORE) :
                                alt10 = 2
                            else:
                                nvae = NoViableAltException("", 10, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 10, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 10, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # grammar/ShyRecognizerBackend.g:131:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint945)

                    self.match(self.input, DOWN, None)
                    ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_hint947)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID27.text ] = list ( ) 
                    #action end



                elif alt10 == 2:
                    # grammar/ShyRecognizerBackend.g:133:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint975)

                    self.match(self.input, DOWN, None)
                    ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_hint977)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint979)
                    hint_args29 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID28.text ] = hint_args29 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # grammar/ShyRecognizerBackend.g:137:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg30 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:140:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:140:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:140:9: ( hint_arg )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ID or LA11_0 == UNDERSCORE) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:140:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args1034)
                        hint_arg30 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg30 ) 
                        #action end



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_args"



    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerBackend.g:143:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID31 = None
        UNDERSCORE32 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:145:5: ( ID | UNDERSCORE )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == ID) :
                    alt12 = 1
                elif (LA12_0 == UNDERSCORE) :
                    alt12 = 2
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # grammar/ShyRecognizerBackend.g:145:9: ID
                    pass 
                    ID31 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1067)

                    #action start
                    value = ID31.text 
                    #action end



                elif alt12 == 2:
                    # grammar/ShyRecognizerBackend.g:146:9: UNDERSCORE
                    pass 
                    UNDERSCORE32 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1079)

                    #action start
                    value = UNDERSCORE32.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerBackend.g:149:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS33 = None
        NUMBER34 = None
        NUMBER35 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:151:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == MINUS) :
                    alt13 = 1
                elif (LA13_0 == NUMBER) :
                    alt13 = 2
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # grammar/ShyRecognizerBackend.g:151:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:151:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:151:11: MINUS NUMBER
                    pass 
                    MINUS33 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1110)

                    NUMBER34 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1112)




                    #action start
                    value = int ( MINUS33.text + NUMBER34.text ) 
                    #action end



                elif alt13 == 2:
                    # grammar/ShyRecognizerBackend.g:153:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:153:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:153:11: NUMBER
                    pass 
                    NUMBER35 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1140)




                    #action start
                    value = int ( NUMBER35.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerBackend.g:157:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS36 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:159:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == MINUS) :
                    alt14 = 1
                elif (LA14_0 == NUMBER) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyRecognizerBackend.g:159:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:159:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:159:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS36 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1185)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1191)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1193)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1199)




                    #action start
                                
                    value = Fraction ( int ( MINUS36.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:164:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:164:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:164:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1231)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1233)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1239)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 25, 31, 37, 38])
    FOLLOW_stateless_in_start114 = frozenset([1, 25, 31, 37, 38])
    FOLLOW_consts_in_start141 = frozenset([1, 25, 31, 37, 38])
    FOLLOW_types_in_start167 = frozenset([1, 25, 31, 37, 38])
    FOLLOW_TREE_MODULE_in_module222 = frozenset([2])
    FOLLOW_ID_in_module224 = frozenset([3])
    FOLLOW_TREE_STATELESS_in_stateless257 = frozenset([2])
    FOLLOW_ID_in_stateless259 = frozenset([3])
    FOLLOW_TREE_CONSTS_in_consts302 = frozenset([2])
    FOLLOW_ID_in_consts304 = frozenset([28, 32, 33])
    FOLLOW_consts_items_in_consts306 = frozenset([3])
    FOLLOW_consts_item_in_consts_items361 = frozenset([1, 28, 32, 33])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item416 = frozenset([2])
    FOLLOW_ID_in_consts_item418 = frozenset([15, 18])
    FOLLOW_num_whole_in_consts_item420 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item448 = frozenset([2])
    FOLLOW_ID_in_consts_item450 = frozenset([15, 18])
    FOLLOW_num_fract_in_consts_item452 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item480 = frozenset([2])
    FOLLOW_ID_in_consts_item482 = frozenset([12])
    FOLLOW_EXPRESSION_in_consts_item484 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types539 = frozenset([2])
    FOLLOW_ID_in_types541 = frozenset([39])
    FOLLOW_types_items_in_types543 = frozenset([3])
    FOLLOW_types_item_in_types_items598 = frozenset([1, 39])
    FOLLOW_TREE_TYPES_ITEM_in_types_item653 = frozenset([2])
    FOLLOW_ID_in_types_item655 = frozenset([42])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item657 = frozenset([41])
    FOLLOW_types_item_hints_in_types_item659 = frozenset([3])
    FOLLOW_TREE_TYPES_ITEM_in_types_item687 = frozenset([2])
    FOLLOW_ID_in_types_item689 = frozenset([42])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item691 = frozenset([3])
    FOLLOW_types_item_hint_in_types_item_hints746 = frozenset([1, 41])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint791 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_types_item_hint793 = frozenset([40])
    FOLLOW_types_item_attr_in_types_item_hint797 = frozenset([3, 40])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint837 = frozenset([2])
    FOLLOW_hint_in_types_item_hint839 = frozenset([40])
    FOLLOW_types_item_attr_in_types_item_hint843 = frozenset([3, 40])
    FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr900 = frozenset([2])
    FOLLOW_ID_in_types_item_attr902 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint945 = frozenset([2])
    FOLLOW_ID_in_hint947 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint975 = frozenset([2])
    FOLLOW_ID_in_hint977 = frozenset([13, 44])
    FOLLOW_hint_args_in_hint979 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args1034 = frozenset([1, 13, 44])
    FOLLOW_ID_in_hint_arg1067 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1079 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1110 = frozenset([18])
    FOLLOW_NUMBER_in_num_whole1112 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1140 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1185 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1191 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract1193 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1199 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1231 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract1233 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1239 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
