# $ANTLR 3.4 grammar/Backend.g 2012-01-13 18:45:43

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
DEDENT=5
DIVIDE=6
EXPRESSION=7
ID=8
INDENT=9
MINUS=10
MODULE=11
NEWLINE=12
NUMBER=13
TREE_CONSTS=14
TREE_EXPRESSION=15
TREE_MODULE=16
TREE_NUM_FRACT=17
TREE_NUM_WHOLE=18
TREE_TYPES=19
TREE_TYPES_ITEM=20
TREE_TYPES_ITEM_ATTR=21
TREE_TYPES_ITEM_ATTRS=22
TYPES=23
WHITESPACE=24

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NEWLINE", "NUMBER", "TREE_CONSTS", "TREE_EXPRESSION", "TREE_MODULE", 
    "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_TYPES", "TREE_TYPES_ITEM", 
    "TREE_TYPES_ITEM_ATTR", "TREE_TYPES_ITEM_ATTRS", "TYPES", "WHITESPACE"
]




class Backend(TreeParser):
    grammarFileName = "grammar/Backend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(Backend, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # grammar/Backend.g:15:1: start returns [ value ] : ( module | consts | types )* ;
    def start(self, ):
        value = None


        module1 = None

        consts2 = None

        types3 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:18:5: ( ( module | consts | types )* )
                # grammar/Backend.g:18:9: ( module | consts | types )*
                pass 
                # grammar/Backend.g:18:9: ( module | consts | types )*
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
                        # grammar/Backend.g:18:11: module
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
                        # grammar/Backend.g:24:11: consts
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
                        # grammar/Backend.g:30:11: types
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
    # grammar/Backend.g:39:1: module returns [ value ] : ^( TREE_MODULE ID ) ;
    def module(self, ):
        value = None


        ID4 = None

        try:
            try:
                # grammar/Backend.g:41:5: ( ^( TREE_MODULE ID ) )
                # grammar/Backend.g:41:9: ^( TREE_MODULE ID )
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
    # grammar/Backend.g:44:1: consts returns [ title , content ] : ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID5 = None
        consts_items6 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/Backend.g:47:5: ( ^( TREE_CONSTS ID consts_items ) )
                # grammar/Backend.g:47:9: ^( TREE_CONSTS ID consts_items )
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
    # grammar/Backend.g:51:1: consts_items returns [ value ] : ( consts_item )+ ;
    def consts_items(self, ):
        value = None


        consts_item7 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:54:5: ( ( consts_item )+ )
                # grammar/Backend.g:54:9: ( consts_item )+
                pass 
                # grammar/Backend.g:54:9: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == TREE_EXPRESSION or (TREE_NUM_FRACT <= LA2_0 <= TREE_NUM_WHOLE)) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/Backend.g:54:11: consts_item
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
    # grammar/Backend.g:59:1: consts_item returns [ name , value ] : ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) );
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
                # grammar/Backend.g:61:5: ( ^( TREE_NUM_WHOLE ID num_whole ) | ^( TREE_NUM_FRACT ID num_fract ) | ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/Backend.g:61:9: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/Backend.g:63:9: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/Backend.g:65:9: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/Backend.g:69:1: types returns [ title , content ] : ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID14 = None
        types_items15 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/Backend.g:72:5: ( ^( TREE_TYPES ID types_items ) )
                # grammar/Backend.g:72:9: ^( TREE_TYPES ID types_items )
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
    # grammar/Backend.g:76:1: types_items returns [ value ] : ( types_item )+ ;
    def types_items(self, ):
        value = None


        types_item16 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:79:5: ( ( types_item )+ )
                # grammar/Backend.g:79:9: ( types_item )+
                pass 
                # grammar/Backend.g:79:9: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == TREE_TYPES_ITEM) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/Backend.g:79:11: types_item
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
    # grammar/Backend.g:84:1: types_item returns [ name , value ] : ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_ATTRS types_item_attrs ) ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID17 = None
        types_item_attrs18 = None


        try:
            try:
                # grammar/Backend.g:86:5: ( ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_ATTRS types_item_attrs ) ) )
                # grammar/Backend.g:86:9: ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_ATTRS types_item_attrs ) )
                pass 
                self.match(self.input, TREE_TYPES_ITEM, self.FOLLOW_TREE_TYPES_ITEM_in_types_item590)

                self.match(self.input, DOWN, None)
                ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item592)

                self.match(self.input, TREE_TYPES_ITEM_ATTRS, self.FOLLOW_TREE_TYPES_ITEM_ATTRS_in_types_item596)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_types_item_attrs_in_types_item598)
                types_item_attrs18 = self.types_item_attrs()

                self._state.following.pop()

                self.match(self.input, UP, None)


                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID17.text , types_item_attrs18 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item"



    # $ANTLR start "types_item_attrs"
    # grammar/Backend.g:90:1: types_item_attrs returns [ value ] : ( types_item_attr )+ ;
    def types_item_attrs(self, ):
        value = None


        types_item_attr19 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:93:5: ( ( types_item_attr )+ )
                # grammar/Backend.g:93:9: ( types_item_attr )+
                pass 
                # grammar/Backend.g:93:9: ( types_item_attr )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == TREE_TYPES_ITEM_ATTR) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/Backend.g:93:11: types_item_attr
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_attrs655)
                        types_item_attr19 = self.types_item_attr()

                        self._state.following.pop()

                        #action start
                        value [ ((types_item_attr19 is not None) and [types_item_attr19.name] or [None])[0] ] = ((types_item_attr19 is not None) and [types_item_attr19.value] or [None])[0] 
                        #action end



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "types_item_attrs"


    class types_item_attr_return(TreeRuleReturnScope):
        def __init__(self):
            super(Backend.types_item_attr_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "types_item_attr"
    # grammar/Backend.g:98:1: types_item_attr returns [ name , value ] : ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        ID20 = None

        try:
            try:
                # grammar/Backend.g:100:5: ( ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/Backend.g:100:9: ^( TREE_TYPES_ITEM_ATTR ID )
                pass 
                self.match(self.input, TREE_TYPES_ITEM_ATTR, self.FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr710)

                self.match(self.input, DOWN, None)
                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr712)

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID20.text , dict ( ) 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "types_item_attr"



    # $ANTLR start "num_whole"
    # grammar/Backend.g:103:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS21 = None
        NUMBER22 = None
        NUMBER23 = None

        try:
            try:
                # grammar/Backend.g:105:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == MINUS) :
                    alt6 = 1
                elif (LA6_0 == NUMBER) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammar/Backend.g:105:9: ( MINUS NUMBER )
                    pass 
                    # grammar/Backend.g:105:9: ( MINUS NUMBER )
                    # grammar/Backend.g:105:11: MINUS NUMBER
                    pass 
                    MINUS21 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole745)

                    NUMBER22 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole747)




                    #action start
                    value = int ( MINUS21.text + NUMBER22.text ) 
                    #action end



                elif alt6 == 2:
                    # grammar/Backend.g:107:9: ( NUMBER )
                    pass 
                    # grammar/Backend.g:107:9: ( NUMBER )
                    # grammar/Backend.g:107:11: NUMBER
                    pass 
                    NUMBER23 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole775)




                    #action start
                    value = int ( NUMBER23.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/Backend.g:111:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS24 = None

        try:
            try:
                # grammar/Backend.g:113:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == MINUS) :
                    alt7 = 1
                elif (LA7_0 == NUMBER) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammar/Backend.g:113:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/Backend.g:113:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/Backend.g:113:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS24 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract820)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract826)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract828)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract834)




                    #action start
                                
                    value = Fraction ( int ( MINUS24.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt7 == 2:
                    # grammar/Backend.g:118:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/Backend.g:118:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/Backend.g:118:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract866)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract868)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract874)




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



 

    FOLLOW_module_in_start86 = frozenset([1, 14, 16, 19])
    FOLLOW_consts_in_start113 = frozenset([1, 14, 16, 19])
    FOLLOW_types_in_start139 = frozenset([1, 14, 16, 19])
    FOLLOW_TREE_MODULE_in_module194 = frozenset([2])
    FOLLOW_ID_in_module196 = frozenset([3])
    FOLLOW_TREE_CONSTS_in_consts239 = frozenset([2])
    FOLLOW_ID_in_consts241 = frozenset([15, 17, 18])
    FOLLOW_consts_items_in_consts243 = frozenset([3])
    FOLLOW_consts_item_in_consts_items298 = frozenset([1, 15, 17, 18])
    FOLLOW_TREE_NUM_WHOLE_in_consts_item353 = frozenset([2])
    FOLLOW_ID_in_consts_item355 = frozenset([10, 13])
    FOLLOW_num_whole_in_consts_item357 = frozenset([3])
    FOLLOW_TREE_NUM_FRACT_in_consts_item385 = frozenset([2])
    FOLLOW_ID_in_consts_item387 = frozenset([10, 13])
    FOLLOW_num_fract_in_consts_item389 = frozenset([3])
    FOLLOW_TREE_EXPRESSION_in_consts_item417 = frozenset([2])
    FOLLOW_ID_in_consts_item419 = frozenset([7])
    FOLLOW_EXPRESSION_in_consts_item421 = frozenset([3])
    FOLLOW_TREE_TYPES_in_types476 = frozenset([2])
    FOLLOW_ID_in_types478 = frozenset([20])
    FOLLOW_types_items_in_types480 = frozenset([3])
    FOLLOW_types_item_in_types_items535 = frozenset([1, 20])
    FOLLOW_TREE_TYPES_ITEM_in_types_item590 = frozenset([2])
    FOLLOW_ID_in_types_item592 = frozenset([22])
    FOLLOW_TREE_TYPES_ITEM_ATTRS_in_types_item596 = frozenset([2])
    FOLLOW_types_item_attrs_in_types_item598 = frozenset([3])
    FOLLOW_types_item_attr_in_types_item_attrs655 = frozenset([1, 21])
    FOLLOW_TREE_TYPES_ITEM_ATTR_in_types_item_attr710 = frozenset([2])
    FOLLOW_ID_in_types_item_attr712 = frozenset([3])
    FOLLOW_MINUS_in_num_whole745 = frozenset([13])
    FOLLOW_NUMBER_in_num_whole747 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole775 = frozenset([1])
    FOLLOW_MINUS_in_num_fract820 = frozenset([13])
    FOLLOW_NUMBER_in_num_fract826 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract828 = frozenset([13])
    FOLLOW_NUMBER_in_num_fract834 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract866 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract868 = frozenset([13])
    FOLLOW_NUMBER_in_num_fract874 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
