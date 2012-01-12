# $ANTLR 3.4 grammar/Backend.g 2012-01-12 18:23:08

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
WHITESPACE=13

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NUMBER", "WHITESPACE"
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
    # grammar/Backend.g:15:1: start returns [ value ] : ( module | consts )* ;
    def start(self, ):
        value = None


        module1 = None

        consts2 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:18:5: ( ( module | consts )* )
                # grammar/Backend.g:18:9: ( module | consts )*
                pass 
                # grammar/Backend.g:18:9: ( module | consts )*
                while True: #loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == MODULE) :
                        alt1 = 1
                    elif (LA1_0 == CONSTS) :
                        alt1 = 2


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
    # grammar/Backend.g:33:1: module returns [ value ] : ^( MODULE ID ) ;
    def module(self, ):
        value = None


        ID3 = None

        try:
            try:
                # grammar/Backend.g:35:5: ( ^( MODULE ID ) )
                # grammar/Backend.g:35:9: ^( MODULE ID )
                pass 
                self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module168)

                self.match(self.input, DOWN, None)
                ID3 = self.match(self.input, ID, self.FOLLOW_ID_in_module170)

                self.match(self.input, UP, None)


                #action start
                value = ID3.text 
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
    # grammar/Backend.g:38:1: consts returns [ title , content ] : ^( CONSTS ID consts_values ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID4 = None
        consts_values5 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/Backend.g:41:5: ( ^( CONSTS ID consts_values ) )
                # grammar/Backend.g:41:9: ^( CONSTS ID consts_values )
                pass 
                self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts213)

                self.match(self.input, DOWN, None)
                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_consts215)

                self._state.following.append(self.FOLLOW_consts_values_in_consts217)
                consts_values5 = self.consts_values()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                retval.title , retval.content = ID4.text , consts_values5 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_values"
    # grammar/Backend.g:45:1: consts_values returns [ value ] : ( consts_value )+ ;
    def consts_values(self, ):
        value = None


        consts_value6 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:48:5: ( ( consts_value )+ )
                # grammar/Backend.g:48:9: ( consts_value )+
                pass 
                # grammar/Backend.g:48:9: ( consts_value )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/Backend.g:48:11: consts_value
                        pass 
                        self._state.following.append(self.FOLLOW_consts_value_in_consts_values272)
                        consts_value6 = self.consts_value()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_value6 is not None) and [consts_value6.name] or [None])[0] ] = ((consts_value6 is not None) and [consts_value6.value] or [None])[0] 
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

    # $ANTLR end "consts_values"


    class consts_value_return(TreeRuleReturnScope):
        def __init__(self):
            super(Backend.consts_value_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_value"
    # grammar/Backend.g:53:1: consts_value returns [ name , value ] : ( ^( ID num_whole ) | ^( ID num_fract ) | ^( ID EXPRESSION ) );
    def consts_value(self, ):
        retval = self.consts_value_return()
        retval.start = self.input.LT(1)


        ID7 = None
        ID9 = None
        ID11 = None
        EXPRESSION12 = None
        num_whole8 = None

        num_fract10 = None


        try:
            try:
                # grammar/Backend.g:55:5: ( ^( ID num_whole ) | ^( ID num_fract ) | ^( ID EXPRESSION ) )
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
                    # grammar/Backend.g:55:9: ^( ID num_whole )
                    pass 
                    ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value327)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_num_whole_in_consts_value329)
                    num_whole8 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID7.text , num_whole8 
                    #action end



                elif alt3 == 2:
                    # grammar/Backend.g:57:9: ^( ID num_fract )
                    pass 
                    ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value357)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_num_fract_in_consts_value359)
                    num_fract10 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID9.text , num_fract10 
                    #action end



                elif alt3 == 3:
                    # grammar/Backend.g:59:9: ^( ID EXPRESSION )
                    pass 
                    ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value387)

                    self.match(self.input, DOWN, None)
                    EXPRESSION12 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_value389)

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID11.text , EXPRESSION12.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts_value"



    # $ANTLR start "num_whole"
    # grammar/Backend.g:63:1: num_whole returns [ value ] : ( ( MINUS NUMBER ) | ( NUMBER ) );
    def num_whole(self, ):
        value = None


        MINUS13 = None
        NUMBER14 = None
        NUMBER15 = None

        try:
            try:
                # grammar/Backend.g:65:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == MINUS) :
                    alt4 = 1
                elif (LA4_0 == NUMBER) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # grammar/Backend.g:65:9: ( MINUS NUMBER )
                    pass 
                    # grammar/Backend.g:65:9: ( MINUS NUMBER )
                    # grammar/Backend.g:65:11: MINUS NUMBER
                    pass 
                    MINUS13 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole434)

                    NUMBER14 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole436)




                    #action start
                    value = int ( MINUS13.text + NUMBER14.text ) 
                    #action end



                elif alt4 == 2:
                    # grammar/Backend.g:67:9: ( NUMBER )
                    pass 
                    # grammar/Backend.g:67:9: ( NUMBER )
                    # grammar/Backend.g:67:11: NUMBER
                    pass 
                    NUMBER15 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole464)




                    #action start
                    value = int ( NUMBER15.text ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "num_whole"



    # $ANTLR start "num_fract"
    # grammar/Backend.g:71:1: num_fract returns [ value ] : ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) );
    def num_fract(self, ):
        value = None


        n = None
        d = None
        MINUS16 = None

        try:
            try:
                # grammar/Backend.g:73:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == MINUS) :
                    alt5 = 1
                elif (LA5_0 == NUMBER) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/Backend.g:73:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/Backend.g:73:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/Backend.g:73:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS16 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract509)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract515)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract517)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract523)




                    #action start
                                
                    value = Fraction ( int ( MINUS16.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt5 == 2:
                    # grammar/Backend.g:78:9: (n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/Backend.g:78:9: (n= NUMBER DIVIDE d= NUMBER )
                    # grammar/Backend.g:78:11: n= NUMBER DIVIDE d= NUMBER
                    pass 
                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract555)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract557)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract563)




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



 

    FOLLOW_module_in_start86 = frozenset([1, 4, 11])
    FOLLOW_consts_in_start113 = frozenset([1, 4, 11])
    FOLLOW_MODULE_in_module168 = frozenset([2])
    FOLLOW_ID_in_module170 = frozenset([3])
    FOLLOW_CONSTS_in_consts213 = frozenset([2])
    FOLLOW_ID_in_consts215 = frozenset([8])
    FOLLOW_consts_values_in_consts217 = frozenset([3])
    FOLLOW_consts_value_in_consts_values272 = frozenset([1, 8])
    FOLLOW_ID_in_consts_value327 = frozenset([2])
    FOLLOW_num_whole_in_consts_value329 = frozenset([3])
    FOLLOW_ID_in_consts_value357 = frozenset([2])
    FOLLOW_num_fract_in_consts_value359 = frozenset([3])
    FOLLOW_ID_in_consts_value387 = frozenset([2])
    FOLLOW_EXPRESSION_in_consts_value389 = frozenset([3])
    FOLLOW_MINUS_in_num_whole434 = frozenset([12])
    FOLLOW_NUMBER_in_num_whole436 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole464 = frozenset([1])
    FOLLOW_MINUS_in_num_fract509 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract515 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract517 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract523 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract555 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract557 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract563 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
