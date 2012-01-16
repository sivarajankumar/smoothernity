# $ANTLR 3.4 recognizer/Backend.g 2012-01-16 18:03:51

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset


from fractions import Fraction



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CONSTS=4
CURLY_CLOSE=5
CURLY_OPEN=6
DEDENT=7
DIVIDE=8
EXPRESSION=9
ID=10
INDENT=11
MINUS=12
MODULE=13
NEWLINE=14
NUMBER=15
TREE_CONSTS=16
TREE_EXPRESSION=17
TREE_HINT=18
TREE_HINT_NONE=19
TREE_MODULE=20
TREE_NUM_FRACT=21
TREE_NUM_WHOLE=22
TREE_TYPES=23
TREE_TYPES_ITEM=24
TREE_TYPES_ITEM_ATTR=25
TREE_TYPES_ITEM_HINT=26
TREE_TYPES_ITEM_HINTS=27
TYPES=28
UNDERSCORE=29
WHITESPACE=30

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", 
    "ID", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", "TREE_CONSTS", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_TYPES_ITEM_ATTR", 
    "TREE_TYPES_ITEM_HINT", "TREE_TYPES_ITEM_HINTS", "TYPES", "UNDERSCORE", 
    "WHITESPACE"
]




class Backend(TreeParser):
    grammarFileName = "recognizer/Backend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(Backend, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # recognizer/Backend.g:15:1: start returns [ value ] : ( module | consts | types )* ;
    def start(self, ):
        value = None


        module1 = None

        consts2 = None

        types3 = None


        value = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:18:5: ( ( module | consts | types )* )
                # recognizer/Backend.g:18:9: ( module | consts | types )*
                pass 
                # recognizer/Backend.g:18:9: ( module | consts | types )*
                while True: #loop1
                    alt1 = 4
                    LA1 = self.input.LA(1)
                    if LA1 == TREE_MODULE:
                        alt1 = 1
                    elif LA1 == TREE_CONSTS:
                        alt1 = 2
                    elif LA1 == TREE_TYPES:
                        alt1 = 3

                    if alt1 == 1:
                        # recognizer/Backend.g:18:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start86)
                        module1 = self.module()

                        self._state.following.pop()

                        #action start
                                    
                        if 'module' not in value :
                            value [ 'module' ] = dict ( )
                        value [ 'module' ] [ module1 ] = dict ( )
                                    
                        #action end



                    elif alt1 == 2:
                        # recognizer/Backend.g:24:11: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start113)
                        consts2 = self.consts()

                        self._state.following.pop()

                        #action start
                                    
                        if 'consts' not in value :
                            value [ 'consts' ] = dict ( )
                        value [ 'consts' ] [ ((consts2 is not None) and [consts2.title] or [None])[0] ] = ((consts2 is not None) and [consts2.content] or [None])[0]
                                    
                        #action end



                    elif alt1 == 3:
                        # recognizer/Backend.g:30:11: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start139)
                        types3 = self.types()

                        self._state.following.pop()

                        #action start
                                    
                        if 'types' not in value :
                            value [ 'types' ] = dict ( )
                        value [ 'types' ] [ ((types3 is not None) and [types3.title] or [None])[0] ] = ((types3 is not None) and [types3.content] or [None])[0]
                                    
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
    # recognizer/Backend.g:39:1: module returns [ value ] : ^( TREE_MODULE ID ) ;
    def module(self, ):
        value = None


        ID4 = None

        try:
            try:
                # recognizer/Backend.g:41:5: ( ^( TREE_MODULE ID ) )
                # recognizer/Backend.g:41:9: ^( TREE_MODULE ID )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module194)

                self.match(self.input, DOWN, None)
                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_module196)

                self.match(self.input, UP, None)


                #action start
                value = ID4.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module"


    class consts_return(TreeRuleReturnScope):
        def __init__(self):
            super(Backend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # recognizer/Backend.g:44:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID5 = None
        consts_items6 = None


        retval.content = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:47:5: ( ^( TREE_CONSTS ID consts_items ) )
                # recognizer/Backend.g:47:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts239)

                self.match(self.input, DOWN, None)
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_consts241)

                self._state.following.append(self.FOLLOW_consts_items_in_consts243)
                consts_items6 = self.consts_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID5.text , consts_items6 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_items"
    # recognizer/Backend.g:51:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item7 = None


        value = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:54:5: ( ( consts_item )+ )
                # recognizer/Backend.g:54:9: ( consts_item )+
                pass 
                # recognizer/Backend.g:54:9: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA2_0 <= TREE_NUM_WHOLE)) :
                        alt2 = 1


                    if alt2 == 1:
                        # recognizer/Backend.g:54:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items298)
                        consts_item7 = self.consts_item()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_item7 is not None) and [consts_item7.name] or [None])[0] ] = ((consts_item7 is not None) and [consts_item7.value] or [None])[0] 
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
            super(Backend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # recognizer/Backend.g:59:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        ID8 = None
        ID10 = None
        ID12 = None
        EXPRESSION13 = None
        num_whole9 = None

        num_fract11 = None


        try:
            try:
                # recognizer/Backend.g:61:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # recognizer/Backend.g:61:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item353)

                    self.match(self.input, DOWN, None)
                    ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item355)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item357)
                    num_whole9 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID8.text , num_whole9 
                    #action end



                elif alt3 == 2:
                    # recognizer/Backend.g:63:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item385)

                    self.match(self.input, DOWN, None)
                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item387)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item389)
                    num_fract11 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID10.text , num_fract11 
                    #action end



                elif alt3 == 3:
                    # recognizer/Backend.g:65:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item417)

                    self.match(self.input, DOWN, None)
                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item419)

                    EXPRESSION13 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item421)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID12.text , EXPRESSION13.text 
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
            super(Backend.types_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "types"
    # recognizer/Backend.g:69:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID14 = None
        types_items15 = None


        retval.content = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:72:5: ( ^( TREE_TYPES ID types_items ) )
                # recognizer/Backend.g:72:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types476)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_types478)

                self._state.following.append(self.FOLLOW_types_items_in_types480)
                types_items15 = self.types_items()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID14.text , types_items15 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types"



    # $ANTLR start "types_items"
    # recognizer/Backend.g:76:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item16 = None


        value = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:79:5: ( ( types_item )+ )
                # recognizer/Backend.g:79:9: ( types_item )+
                pass 
                # recognizer/Backend.g:79:9: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == TREE_TYPES_ITEM) :
                        alt4 = 1


                    if alt4 == 1:
                        # recognizer/Backend.g:79:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items535)
                        types_item16 = self.types_item()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item16 is not None) and [types_item16.name] or [None])[0] ] = ((types_item16 is not None) and [types_item16.value] or [None])[0] 
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
            super(Backend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # recognizer/Backend.g:84:1: types_item returns [ name , value ] : ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) );
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID17 = None
        ID19 = None
        types_item_hints18 = None


        try:
            try:
                # recognizer/Backend.g:86:5: ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) )
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
                    # recognizer/Backend.g:86:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item590)

                    self.match(self.input, DOWN, None)
                    ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item592)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item594)

                    self._state.following.append(self.FOLLOW_types_item_hints_in_types_item596)
                    types_item_hints18 = self.types_item_hints()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID17.text , types_item_hints18 
                    #action end



                elif alt5 == 2:
                    # recognizer/Backend.g:88:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item624)

                    self.match(self.input, DOWN, None)
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item626)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item628)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID19.text , dict ( ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "types_item_hints"
    # recognizer/Backend.g:92:1: types_item_hints returns [ value ] : ( types_item_hint )+ ;
    def types_item_hints(self, ):
        value = None


        types_item_hint20 = None


        value = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:95:5: ( ( types_item_hint )+ )
                # recognizer/Backend.g:95:9: ( types_item_hint )+
                pass 
                # recognizer/Backend.g:95:9: ( types_item_hint )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TREE_TYPES_ITEM_HINT) :
                        alt6 = 1


                    if alt6 == 1:
                        # recognizer/Backend.g:95:11: types_item_hint
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_hint_in_types_item_hints683)
                        types_item_hint20 = self.types_item_hint()

                        self._state.following.pop()

                        #action start
                        value . update ( types_item_hint20 ) 
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
    # recognizer/Backend.g:98:1: types_item_hint returns [ value ] : ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        value = None


        types_item_attr21 = None

        types_item_attr22 = None

        hint23 = None


        value = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:101:5: ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
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
                    # recognizer/Backend.g:101:9: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint728)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_types_item_hint730)

                    # recognizer/Backend.g:101:48: ( types_item_attr )+
                    cnt7 = 0
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == TREE_TYPES_ITEM_ATTR) :
                            alt7 = 1


                        if alt7 == 1:
                            # recognizer/Backend.g:101:50: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint734)
                            types_item_attr21 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr21 ] = dict ( ) 
                            #action end



                        else:
                            if cnt7 >= 1:
                                break #loop7

                            eee = EarlyExitException(7, self.input)
                            raise eee

                        cnt7 += 1


                    self.match(self.input, UP, None)



                elif alt9 == 2:
                    # recognizer/Backend.g:104:9: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint774)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint776)
                    hint23 = self.hint()

                    self._state.following.pop()

                    # recognizer/Backend.g:104:38: ( types_item_attr )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == TREE_TYPES_ITEM_ATTR) :
                            alt8 = 1


                        if alt8 == 1:
                            # recognizer/Backend.g:104:40: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint780)
                            types_item_attr22 = self.types_item_attr()

                            self._state.following.pop()

                            #action start
                            value [ types_item_attr22 ] = hint23 
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
    # recognizer/Backend.g:109:1: types_item_attr returns [ value ] : ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        value = None


        ID24 = None

        try:
            try:
                # recognizer/Backend.g:111:5: ( ^( TREE_TYPES_ITEM_ATTR ID ) )
                # recognizer/Backend.g:111:9: ^( TREE_TYPES_ITEM_ATTR ID )
                pass 
                self.match(self.input, TREE_TYPES_ITEM_ATTR, self.FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr837)

                self.match(self.input, DOWN, None)
                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr839)

                self.match(self.input, UP, None)


                #action start
                value = ID24.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "types_item_attr"



    # $ANTLR start "hint"
    # recognizer/Backend.g:114:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID25 = None
        ID26 = None
        hint_args27 = None


        value = dict ( ) 
        try:
            try:
                # recognizer/Backend.g:117:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
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
                    # recognizer/Backend.g:117:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint882)

                    self.match(self.input, DOWN, None)
                    ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_hint884)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID25.text ] = list ( ) 
                    #action end



                elif alt10 == 2:
                    # recognizer/Backend.g:119:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint912)

                    self.match(self.input, DOWN, None)
                    ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_hint914)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint916)
                    hint_args27 = self.hint_args()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID26.text ] = hint_args27 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint"



    # $ANTLR start "hint_args"
    # recognizer/Backend.g:123:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg28 = None


        value = list ( ) 
        try:
            try:
                # recognizer/Backend.g:126:5: ( ( hint_arg )+ )
                # recognizer/Backend.g:126:9: ( hint_arg )+
                pass 
                # recognizer/Backend.g:126:9: ( hint_arg )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ID or LA11_0 == UNDERSCORE) :
                        alt11 = 1


                    if alt11 == 1:
                        # recognizer/Backend.g:126:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args971)
                        hint_arg28 = self.hint_arg()

                        self._state.following.pop()

                        #action start
                        value . append ( hint_arg28 ) 
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
    # recognizer/Backend.g:129:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID29 = None
        UNDERSCORE30 = None

        try:
            try:
                # recognizer/Backend.g:131:5: ( ID | UNDERSCORE )
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
                    # recognizer/Backend.g:131:9: ID
                    pass 
                    ID29 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1004)

                    #action start
                    value = ID29.text 
                    #action end



                elif alt12 == 2:
                    # recognizer/Backend.g:132:9: UNDERSCORE
                    pass 
                    UNDERSCORE30 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1016)

                    #action start
                    value = UNDERSCORE30.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "hint_arg"



    # $ANTLR start "num_whole"
    # recognizer/Backend.g:135:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS31 = None
        NUMBER32 = None
        NUMBER33 = None

        try:
            try:
                # recognizer/Backend.g:137:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # recognizer/Backend.g:137:9: ( MINUS NUMBER )
                    pass 
                    # recognizer/Backend.g:137:9: ( MINUS NUMBER )
                    # recognizer/Backend.g:137:11: MINUS NUMBER
                    pass 
                    MINUS31 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1047)

                    NUMBER32 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1049)




                    #action start
                    value = int ( MINUS31.text + NUMBER32.text ) 
                    #action end



                elif alt13 == 2:
                    # recognizer/Backend.g:139:9: ( NUMBER )
                    pass 
                    # recognizer/Backend.g:139:9: ( NUMBER )
                    # recognizer/Backend.g:139:11: NUMBER
                    pass 
                    NUMBER33 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1077)




                    #action start
                    value = int ( NUMBER33.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # recognizer/Backend.g:143:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS34 = None

        try:
            try:
                # recognizer/Backend.g:145:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # recognizer/Backend.g:145:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # recognizer/Backend.g:145:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # recognizer/Backend.g:145:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS34 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1122)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1128)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1130)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1136)




                    #action start
                                
                    value = Fraction ( int ( MINUS34.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt14 == 2:
                    # recognizer/Backend.g:150:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # recognizer/Backend.g:150:9: (n= NUMBER DIVIDE d= NUMBER )
                    # recognizer/Backend.g:150:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1168)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1170)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1176)




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



 

    FOLLOW_module_in_start86 = frozenset([1, 16, 20, 23])
    FOLLOW_consts_in_start113 = frozenset([1, 16, 20, 23])
    FOLLOW_types_in_start139 = frozenset([1, 16, 20, 23])
    FOLLOW_TREE_MODULE_in_module194 = frozenset([2])
    FOLLOW_ID_in_module196 = frozenset([3])
    FOLLOW_TREE_CONSTS_in_consts239 = frozenset([2])
    FOLLOW_ID_in_consts241 = frozenset([17, 21, 22])
    FOLLOW_consts_items_in_consts243 = frozenset([3])
    FOLLOW_consts_item_in_consts_items298 = frozenset([1, 17, 21, 22])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item353 = frozenset([2])
    FOLLOW_ID_in_consts_item355 = frozenset([12, 15])
    FOLLOW_num_whole_in_consts_item357 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item385 = frozenset([2])
    FOLLOW_ID_in_consts_item387 = frozenset([12, 15])
    FOLLOW_num_fract_in_consts_item389 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item417 = frozenset([2])
    FOLLOW_ID_in_consts_item419 = frozenset([9])
    FOLLOW_EXPRESSION_in_consts_item421 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types476 = frozenset([2])
    FOLLOW_ID_in_types478 = frozenset([24])
    FOLLOW_types_items_in_types480 = frozenset([3])
    FOLLOW_types_item_in_types_items535 = frozenset([1, 24])
    FOLLOW_TREE_TYPES_ITEM_in_types_item590 = frozenset([2])
    FOLLOW_ID_in_types_item592 = frozenset([27])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item594 = frozenset([26])
    FOLLOW_types_item_hints_in_types_item596 = frozenset([3])
    FOLLOW_TREE_TYPES_ITEM_in_types_item624 = frozenset([2])
    FOLLOW_ID_in_types_item626 = frozenset([27])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item628 = frozenset([3])
    FOLLOW_types_item_hint_in_types_item_hints683 = frozenset([1, 26])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint728 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_types_item_hint730 = frozenset([25])
    FOLLOW_types_item_attr_in_types_item_hint734 = frozenset([3, 25])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint774 = frozenset([2])
    FOLLOW_hint_in_types_item_hint776 = frozenset([25])
    FOLLOW_types_item_attr_in_types_item_hint780 = frozenset([3, 25])
    FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr837 = frozenset([2])
    FOLLOW_ID_in_types_item_attr839 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint882 = frozenset([2])
    FOLLOW_ID_in_hint884 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint912 = frozenset([2])
    FOLLOW_ID_in_hint914 = frozenset([10, 29])
    FOLLOW_hint_args_in_hint916 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args971 = frozenset([1, 10, 29])
    FOLLOW_ID_in_hint_arg1004 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1016 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1047 = frozenset([15])
    FOLLOW_NUMBER_in_num_whole1049 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1077 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1122 = frozenset([15])
    FOLLOW_NUMBER_in_num_fract1128 = frozenset([8])
    FOLLOW_DIVIDE_in_num_fract1130 = frozenset([15])
    FOLLOW_NUMBER_in_num_fract1136 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1168 = frozenset([8])
    FOLLOW_DIVIDE_in_num_fract1170 = frozenset([15])
    FOLLOW_NUMBER_in_num_fract1176 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
