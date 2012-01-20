# $ANTLR 3.4 grammar/ShyRecognizerBackend.g 2012-01-20 16:49:13

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
REPLACE=20
STRING=21
TREE_ARBITRARY_TOKEN=22
TREE_CONSTS=23
TREE_COPY=24
TREE_COPY_PASTE=25
TREE_EXPRESSION=26
TREE_HINT=27
TREE_HINT_NONE=28
TREE_MODULE=29
TREE_NUM_FRACT=30
TREE_NUM_WHOLE=31
TREE_PASTE=32
TREE_PASTE_REPLACE=33
TREE_PASTE_WITH=34
TREE_TYPES=35
TREE_TYPES_ITEM=36
TREE_TYPES_ITEM_ATTR=37
TREE_TYPES_ITEM_HINT=38
TREE_TYPES_ITEM_HINTS=39
TYPES=40
UNDERSCORE=41
WHITESPACE=42
WITH=43

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", "CURLY_OPEN", 
    "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", "MODULE", 
    "NEWLINE", "NUMBER", "PASTE", "REPLACE", "STRING", "TREE_ARBITRARY_TOKEN", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_TYPES_ITEM_ATTR", "TREE_TYPES_ITEM_HINT", "TREE_TYPES_ITEM_HINTS", 
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
    # grammar/ShyRecognizerBackend.g:22:1: start returns [ value ] : ( module | consts | types )* ;
    def start(self, ):
        value = None


        module1 = None

        consts2 = None

        types3 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:25:5: ( ( module | consts | types )* )
                # grammar/ShyRecognizerBackend.g:25:9: ( module | consts | types )*
                pass 
                # grammar/ShyRecognizerBackend.g:25:9: ( module | consts | types )*
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
                        # grammar/ShyRecognizerBackend.g:30:11: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start114)
                        consts2 = self.consts()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'consts' ,
                            ((consts2 is not None) and [consts2.title] or [None])[0] , ((consts2 is not None) and [consts2.content] or [None])[0] )
                                    
                        #action end



                    elif alt1 == 3:
                        # grammar/ShyRecognizerBackend.g:35:11: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start140)
                        types3 = self.types()

                        self._state.following.pop()

                        #action start
                                    
                        update_start_dict ( value , 'types' ,
                            ((types3 is not None) and [types3.title] or [None])[0] , ((types3 is not None) and [types3.content] or [None])[0] )
                                    
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
    # grammar/ShyRecognizerBackend.g:43:1: module returns [ value ] : ^( TREE_MODULE ID ) ;
    def module(self, ):
        value = None


        ID4 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:45:5: ( ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerBackend.g:45:9: ^( TREE_MODULE ID )
                pass 
                self.match(self.input, TREE_MODULE, self.FOLLOW_TREE_MODULE_in_module195)

                self.match(self.input, DOWN, None)
                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_module197)

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
            super(ShyRecognizerBackend.consts_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerBackend.g:48:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID5 = None
        consts_items6 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:51:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerBackend.g:51:9: ^( TREE_CONSTS ID consts_items )
                pass 
                self.match(self.input, TREE_CONSTS, self.FOLLOW_TREE_CONSTS_in_consts240)

                self.match(self.input, DOWN, None)
                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_consts242)

                self._state.following.append(self.FOLLOW_consts_items_in_consts244)
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
    # grammar/ShyRecognizerBackend.g:55:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item7 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:58:5: ( ( consts_item )+ )
                # grammar/ShyRecognizerBackend.g:58:9: ( consts_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:58:9: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA2_0 <= TREE_NUM_WHOLE)) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyRecognizerBackend.g:58:11: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items299)
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
            super(ShyRecognizerBackend.consts_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerBackend.g:63:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
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
                # grammar/ShyRecognizerBackend.g:65:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerBackend.g:65:9: ^( TREE_NUM_WHOLE ID num_whole )
                    pass 
                    self.match(self.input, TREE_NUM_WHOLE, self.FOLLOW_TREE_NUM_WHOLE_in_consts_item354)

                    self.match(self.input, DOWN, None)
                    ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item356)

                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item358)
                    num_whole9 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID8.text , num_whole9 
                    #action end



                elif alt3 == 2:
                    # grammar/ShyRecognizerBackend.g:67:9: ^( TREE_NUM_FRACT ID num_fract )
                    pass 
                    self.match(self.input, TREE_NUM_FRACT, self.FOLLOW_TREE_NUM_FRACT_in_consts_item386)

                    self.match(self.input, DOWN, None)
                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item388)

                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item390)
                    num_fract11 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID10.text , num_fract11 
                    #action end



                elif alt3 == 3:
                    # grammar/ShyRecognizerBackend.g:69:9: ^( TREE_EXPRESSION ID EXPRESSION )
                    pass 
                    self.match(self.input, TREE_EXPRESSION, self.FOLLOW_TREE_EXPRESSION_in_consts_item418)

                    self.match(self.input, DOWN, None)
                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item420)

                    EXPRESSION13 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item422)

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
            super(ShyRecognizerBackend.types_return, self).__init__()

            self.title = None
            self.content = None





    # $ANTLR start "types"
    # grammar/ShyRecognizerBackend.g:73:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID14 = None
        types_items15 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:76:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerBackend.g:76:9: ^( TREE_TYPES ID types_items )
                pass 
                self.match(self.input, TREE_TYPES, self.FOLLOW_TREE_TYPES_in_types477)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_types479)

                self._state.following.append(self.FOLLOW_types_items_in_types481)
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
    # grammar/ShyRecognizerBackend.g:80:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item16 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:83:5: ( ( types_item )+ )
                # grammar/ShyRecognizerBackend.g:83:9: ( types_item )+
                pass 
                # grammar/ShyRecognizerBackend.g:83:9: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == TREE_TYPES_ITEM) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerBackend.g:83:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items536)
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
            super(ShyRecognizerBackend.types_item_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerBackend.g:88:1: types_item returns [ name , value ] : ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) );
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID17 = None
        ID19 = None
        types_item_hints18 = None


        try:
            try:
                # grammar/ShyRecognizerBackend.g:90:5: ( ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints ) | ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ) )
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
                    # grammar/ShyRecognizerBackend.g:90:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS types_item_hints )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item591)

                    self.match(self.input, DOWN, None)
                    ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item593)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item595)

                    self._state.following.append(self.FOLLOW_types_item_hints_in_types_item597)
                    types_item_hints18 = self.types_item_hints()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID17.text , types_item_hints18 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyRecognizerBackend.g:92:9: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item625)

                    self.match(self.input, DOWN, None)
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item627)

                    self.match(self.input, TREE_TYPES_ITEM_HINTS, self.FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item629)

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
    # grammar/ShyRecognizerBackend.g:96:1: types_item_hints returns [ value ] : ( types_item_hint )+ ;
    def types_item_hints(self, ):
        value = None


        types_item_hint20 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:99:5: ( ( types_item_hint )+ )
                # grammar/ShyRecognizerBackend.g:99:9: ( types_item_hint )+
                pass 
                # grammar/ShyRecognizerBackend.g:99:9: ( types_item_hint )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TREE_TYPES_ITEM_HINT) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyRecognizerBackend.g:99:11: types_item_hint
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_hint_in_types_item_hints684)
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
    # grammar/ShyRecognizerBackend.g:102:1: types_item_hint returns [ value ] : ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        value = None


        types_item_attr21 = None

        types_item_attr22 = None

        hint23 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:105:5: ( ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
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
                    # grammar/ShyRecognizerBackend.g:105:9: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint729)

                    self.match(self.input, DOWN, None)
                    self.match(self.input, TREE_HINT_NONE, self.FOLLOW_TREE_HINT_NONE_in_types_item_hint731)

                    # grammar/ShyRecognizerBackend.g:105:48: ( types_item_attr )+
                    cnt7 = 0
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == TREE_TYPES_ITEM_ATTR) :
                            alt7 = 1


                        if alt7 == 1:
                            # grammar/ShyRecognizerBackend.g:105:50: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint735)
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
                    # grammar/ShyRecognizerBackend.g:108:9: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    pass 
                    self.match(self.input, TREE_TYPES_ITEM_HINT, self.FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint775)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint777)
                    hint23 = self.hint()

                    self._state.following.pop()

                    # grammar/ShyRecognizerBackend.g:108:38: ( types_item_attr )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == TREE_TYPES_ITEM_ATTR) :
                            alt8 = 1


                        if alt8 == 1:
                            # grammar/ShyRecognizerBackend.g:108:40: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint781)
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
    # grammar/ShyRecognizerBackend.g:113:1: types_item_attr returns [ value ] : ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        value = None


        ID24 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:115:5: ( ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/ShyRecognizerBackend.g:115:9: ^( TREE_TYPES_ITEM_ATTR ID )
                pass 
                self.match(self.input, TREE_TYPES_ITEM_ATTR, self.FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr838)

                self.match(self.input, DOWN, None)
                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr840)

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
    # grammar/ShyRecognizerBackend.g:118:1: hint returns [ value ] : ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) );
    def hint(self, ):
        value = None


        ID25 = None
        ID26 = None
        hint_args27 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:121:5: ( ^( TREE_HINT ID ) | ^( TREE_HINT ID hint_args ) )
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
                    # grammar/ShyRecognizerBackend.g:121:9: ^( TREE_HINT ID )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint883)

                    self.match(self.input, DOWN, None)
                    ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_hint885)

                    self.match(self.input, UP, None)


                    #action start
                    value [ ID25.text ] = list ( ) 
                    #action end



                elif alt10 == 2:
                    # grammar/ShyRecognizerBackend.g:123:9: ^( TREE_HINT ID hint_args )
                    pass 
                    self.match(self.input, TREE_HINT, self.FOLLOW_TREE_HINT_in_hint913)

                    self.match(self.input, DOWN, None)
                    ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_hint915)

                    self._state.following.append(self.FOLLOW_hint_args_in_hint917)
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
    # grammar/ShyRecognizerBackend.g:127:1: hint_args returns [ value ] : ( hint_arg )+ ;
    def hint_args(self, ):
        value = None


        hint_arg28 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyRecognizerBackend.g:130:5: ( ( hint_arg )+ )
                # grammar/ShyRecognizerBackend.g:130:9: ( hint_arg )+
                pass 
                # grammar/ShyRecognizerBackend.g:130:9: ( hint_arg )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ID or LA11_0 == UNDERSCORE) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerBackend.g:130:11: hint_arg
                        pass 
                        self._state.following.append(self.FOLLOW_hint_arg_in_hint_args972)
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
    # grammar/ShyRecognizerBackend.g:133:1: hint_arg returns [ value ] : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        value = None


        ID29 = None
        UNDERSCORE30 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:135:5: ( ID | UNDERSCORE )
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
                    # grammar/ShyRecognizerBackend.g:135:9: ID
                    pass 
                    ID29 = self.match(self.input, ID, self.FOLLOW_ID_in_hint_arg1005)

                    #action start
                    value = ID29.text 
                    #action end



                elif alt12 == 2:
                    # grammar/ShyRecognizerBackend.g:136:9: UNDERSCORE
                    pass 
                    UNDERSCORE30 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_hint_arg1017)

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
    # grammar/ShyRecognizerBackend.g:139:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS31 = None
        NUMBER32 = None
        NUMBER33 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:141:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:141:9: ( MINUS NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:141:9: ( MINUS NUMBER )
                    # grammar/ShyRecognizerBackend.g:141:11: MINUS NUMBER
                    pass 
                    MINUS31 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1048)

                    NUMBER32 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1050)




                    #action start
                    value = int ( MINUS31.text + NUMBER32.text ) 
                    #action end



                elif alt13 == 2:
                    # grammar/ShyRecognizerBackend.g:143:9: ( NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:143:9: ( NUMBER )
                    # grammar/ShyRecognizerBackend.g:143:11: NUMBER
                    pass 
                    NUMBER33 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1078)




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
    # grammar/ShyRecognizerBackend.g:147:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS34 = None

        try:
            try:
                # grammar/ShyRecognizerBackend.g:149:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/ShyRecognizerBackend.g:149:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:149:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:149:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS34 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1123)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1129)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1131)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1137)




                    #action start
                                
                    value = Fraction ( int ( MINUS34.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt14 == 2:
                    # grammar/ShyRecognizerBackend.g:154:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/ShyRecognizerBackend.g:154:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/ShyRecognizerBackend.g:154:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1169)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1171)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1177)




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



 

    FOLLOW_module_in_start87 = frozenset([1, 23, 29, 35])
    FOLLOW_consts_in_start114 = frozenset([1, 23, 29, 35])
    FOLLOW_types_in_start140 = frozenset([1, 23, 29, 35])
    FOLLOW_TREE_MODULE_in_module195 = frozenset([2])
    FOLLOW_ID_in_module197 = frozenset([3])
    FOLLOW_TREE_CONSTS_in_consts240 = frozenset([2])
    FOLLOW_ID_in_consts242 = frozenset([26, 30, 31])
    FOLLOW_consts_items_in_consts244 = frozenset([3])
    FOLLOW_consts_item_in_consts_items299 = frozenset([1, 26, 30, 31])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item354 = frozenset([2])
    FOLLOW_ID_in_consts_item356 = frozenset([15, 18])
    FOLLOW_num_whole_in_consts_item358 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item386 = frozenset([2])
    FOLLOW_ID_in_consts_item388 = frozenset([15, 18])
    FOLLOW_num_fract_in_consts_item390 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item418 = frozenset([2])
    FOLLOW_ID_in_consts_item420 = frozenset([12])
    FOLLOW_EXPRESSION_in_consts_item422 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types477 = frozenset([2])
    FOLLOW_ID_in_types479 = frozenset([36])
    FOLLOW_types_items_in_types481 = frozenset([3])
    FOLLOW_types_item_in_types_items536 = frozenset([1, 36])
    FOLLOW_TREE_TYPES_ITEM_in_types_item591 = frozenset([2])
    FOLLOW_ID_in_types_item593 = frozenset([39])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item595 = frozenset([38])
    FOLLOW_types_item_hints_in_types_item597 = frozenset([3])
    FOLLOW_TREE_TYPES_ITEM_in_types_item625 = frozenset([2])
    FOLLOW_ID_in_types_item627 = frozenset([39])
    FOLLOW_TREE_TYPES_ITEM_HINTS_in_types_item629 = frozenset([3])
    FOLLOW_types_item_hint_in_types_item_hints684 = frozenset([1, 38])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint729 = frozenset([2])
    FOLLOW_TREE_HINT_NONE_in_types_item_hint731 = frozenset([37])
    FOLLOW_types_item_attr_in_types_item_hint735 = frozenset([3, 37])
    FOLLOW_TREE_TYPES_ITEM_HINT_in_types_item_hint775 = frozenset([2])
    FOLLOW_hint_in_types_item_hint777 = frozenset([37])
    FOLLOW_types_item_attr_in_types_item_hint781 = frozenset([3, 37])
    FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr838 = frozenset([2])
    FOLLOW_ID_in_types_item_attr840 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint883 = frozenset([2])
    FOLLOW_ID_in_hint885 = frozenset([3])
    FOLLOW_TREE_HINT_in_hint913 = frozenset([2])
    FOLLOW_ID_in_hint915 = frozenset([13, 41])
    FOLLOW_hint_args_in_hint917 = frozenset([3])
    FOLLOW_hint_arg_in_hint_args972 = frozenset([1, 13, 41])
    FOLLOW_ID_in_hint_arg1005 = frozenset([1])
    FOLLOW_UNDERSCORE_in_hint_arg1017 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1048 = frozenset([18])
    FOLLOW_NUMBER_in_num_whole1050 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole1078 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1123 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1129 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract1131 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1137 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract1169 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract1171 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract1177 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyRecognizerBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
