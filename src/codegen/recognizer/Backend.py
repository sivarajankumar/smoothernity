# $ANTLR 3.4 grammar/Backend.g 2012-01-12 19:14:26

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
NUMBER=12
TYPES=13
WHITESPACE=14

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NUMBER", "TYPES", "WHITESPACE"
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
                    if LA1 == MODULE:
                        alt1 = 1
                    elif LA1 == CONSTS:
                        alt1 = 2
                    elif LA1 == TYPES:
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
    # grammar/Backend.g:39:1: module returns [ value ] : ^( MODULE ID ) ;
    def module(self, ):
        value = None


        ID4 = None

        try:
            try:
                # grammar/Backend.g:41:5: ( ^( MODULE ID ) )
                # grammar/Backend.g:41:9: ^( MODULE ID )
                pass 
                self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module194)

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
    # grammar/Backend.g:44:1: consts returns [ title , content ] : ^( CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID5 = None
        consts_items6 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/Backend.g:47:5: ( ^( CONSTS ID consts_items ) )
                # grammar/Backend.g:47:9: ^( CONSTS ID consts_items )
                pass 
                self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts239)

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

                    if (LA2_0 == ID) :
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
    # grammar/Backend.g:59:1: consts_item returns [ name , value ] : ( ^( ID num_whole ) | ^( ID num_fract ) | ^( ID EXPRESSION ) );
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
                # grammar/Backend.g:61:5: ( ^( ID num_whole ) | ^( ID num_fract ) | ^( ID EXPRESSION ) )
                alt3 = 3
                LA3_0 = self.input.LA(1)

                if (LA3_0 == ID) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == 2) :
                        LA3 = self.input.LA(3)
                        if LA3 == EXPRESSION:
                            alt3 = 3
                        elif LA3 == MINUS:
                            LA3_4 = self.input.LA(4)

                            if (LA3_4 == NUMBER) :
                                LA3_6 = self.input.LA(5)

                                if (LA3_6 == DIVIDE) :
                                    alt3 = 2
                                elif (LA3_6 == 3) :
                                    alt3 = 1
                                else:
                                    nvae = NoViableAltException("", 3, 6, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 3, 4, self.input)

                                raise nvae


                        elif LA3 == NUMBER:
                            LA3_5 = self.input.LA(4)

                            if (LA3_5 == DIVIDE) :
                                alt3 = 2
                            elif (LA3_5 == 3) :
                                alt3 = 1
                            else:
                                nvae = NoViableAltException("", 3, 5, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 3, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/Backend.g:61:9: ^( ID num_whole )
                    pass 
                    ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item353)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item355)
                    num_whole9 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID8.text , num_whole9 
                    #action end



                elif alt3 == 2:
                    # grammar/Backend.g:63:9: ^( ID num_fract )
                    pass 
                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item383)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item385)
                    num_fract11 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID10.text , num_fract11 
                    #action end



                elif alt3 == 3:
                    # grammar/Backend.g:65:9: ^( ID EXPRESSION )
                    pass 
                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item413)

                    self.match(self.input, DOWN, None)
                    EXPRESSION13 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item415)

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
    # grammar/Backend.g:69:1: types returns [ title , content ] : ^( TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        ID14 = None
        types_items15 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/Backend.g:72:5: ( ^( TYPES ID types_items ) )
                # grammar/Backend.g:72:9: ^( TYPES ID types_items )
                pass 
                self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types470)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_types472)

                self._state.following.append(self.FOLLOW_types_items_in_types474)
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

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/Backend.g:79:11: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items529)
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
    # grammar/Backend.g:84:1: types_item returns [ name , value ] : ^( ID types_item_attrs ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        ID17 = None
        types_item_attrs18 = None


        try:
            try:
                # grammar/Backend.g:86:5: ( ^( ID types_item_attrs ) )
                # grammar/Backend.g:86:9: ^( ID types_item_attrs )
                pass 
                ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item584)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_types_item_attrs_in_types_item586)
                types_item_attrs18 = self.types_item_attrs()

                self._state.following.pop()

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

                    if (LA5_0 == ID) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/Backend.g:93:11: types_item_attr
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_attrs641)
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
    # grammar/Backend.g:98:1: types_item_attr returns [ name , value ] : ID ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        ID20 = None

        try:
            try:
                # grammar/Backend.g:100:5: ( ID )
                # grammar/Backend.g:100:9: ID
                pass 
                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr694)

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
                    MINUS21 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole725)

                    NUMBER22 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole727)




                    #action start
                    value = int ( MINUS21.text + NUMBER22.text ) 
                    #action end



                elif alt6 == 2:
                    # grammar/Backend.g:107:9: ( NUMBER )
                    pass 
                    # grammar/Backend.g:107:9: ( NUMBER )
                    # grammar/Backend.g:107:11: NUMBER
                    pass 
                    NUMBER23 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole755)




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
                    MINUS24 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract800)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract806)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract808)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract814)




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
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract846)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract848)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract854)




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



 

    FOLLOW_module_in_start86 = frozenset([1, 4, 11, 13])
    FOLLOW_consts_in_start113 = frozenset([1, 4, 11, 13])
    FOLLOW_types_in_start139 = frozenset([1, 4, 11, 13])
    FOLLOW_MODULE_in_module194 = frozenset([2])
    FOLLOW_ID_in_module196 = frozenset([3])
    FOLLOW_CONSTS_in_consts239 = frozenset([2])
    FOLLOW_ID_in_consts241 = frozenset([8])
    FOLLOW_consts_items_in_consts243 = frozenset([3])
    FOLLOW_consts_item_in_consts_items298 = frozenset([1, 8])
    FOLLOW_ID_in_consts_item353 = frozenset([2])
    FOLLOW_num_whole_in_consts_item355 = frozenset([3])
    FOLLOW_ID_in_consts_item383 = frozenset([2])
    FOLLOW_num_fract_in_consts_item385 = frozenset([3])
    FOLLOW_ID_in_consts_item413 = frozenset([2])
    FOLLOW_EXPRESSION_in_consts_item415 = frozenset([3])
    FOLLOW_TYPES_in_types470 = frozenset([2])
    FOLLOW_ID_in_types472 = frozenset([8])
    FOLLOW_types_items_in_types474 = frozenset([3])
    FOLLOW_types_item_in_types_items529 = frozenset([1, 8])
    FOLLOW_ID_in_types_item584 = frozenset([2])
    FOLLOW_types_item_attrs_in_types_item586 = frozenset([3])
    FOLLOW_types_item_attr_in_types_item_attrs641 = frozenset([1, 8])
    FOLLOW_ID_in_types_item_attr694 = frozenset([1])
    FOLLOW_MINUS_in_num_whole725 = frozenset([12])
    FOLLOW_NUMBER_in_num_whole727 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole755 = frozenset([1])
    FOLLOW_MINUS_in_num_fract800 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract806 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract808 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract814 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract846 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract848 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract854 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
