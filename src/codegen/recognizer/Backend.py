# $ANTLR 3.4 grammar/Backend.g 2012-01-12 09:16:15

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
ID=7
INDENT=8
MINUS=9
MODULE=10
NUMBER=11
WHITESPACE=12

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "DIVIDE", "ID", "INDENT", "MINUS", "MODULE", "NUMBER", 
    "WHITESPACE"
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
    # grammar/Backend.g:38:1: consts returns [ title , content ] : ( ^( CONSTS ID ) | ^( CONSTS ID consts_values ) );
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID4 = None
        ID5 = None
        consts_values6 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/Backend.g:41:5: ( ^( CONSTS ID ) | ^( CONSTS ID consts_values ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == CONSTS) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 2) :
                        LA2_2 = self.input.LA(3)

                        if (LA2_2 == ID) :
                            LA2_3 = self.input.LA(4)

                            if (LA2_3 == 3) :
                                alt2 = 1
                            elif (LA2_3 == ID) :
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
                    # grammar/Backend.g:41:9: ^( CONSTS ID )
                    pass 
                    self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts213)

                    self.match(self.input, DOWN, None)
                    ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_consts215)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID4.text , dict ( ) 
                    #action end



                elif alt2 == 2:
                    # grammar/Backend.g:43:9: ^( CONSTS ID consts_values )
                    pass 
                    self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts243)

                    self.match(self.input, DOWN, None)
                    ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_consts245)

                    self._state.following.append(self.FOLLOW_consts_values_in_consts247)
                    consts_values6 = self.consts_values()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID5.text , consts_values6 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts"



    # $ANTLR start "consts_values"
    # grammar/Backend.g:47:1: consts_values returns [ value ] : ( consts_value )+ ;
    def consts_values(self, ):
        value = None


        consts_value7 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:50:5: ( ( consts_value )+ )
                # grammar/Backend.g:50:9: ( consts_value )+
                pass 
                # grammar/Backend.g:50:9: ( consts_value )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == ID) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/Backend.g:50:11: consts_value
                        pass 
                        self._state.following.append(self.FOLLOW_consts_value_in_consts_values302)
                        consts_value7 = self.consts_value()

                        self._state.following.pop()

                        #action start
                        value [ ((consts_value7 is not None) and [consts_value7.name] or [None])[0] ] = ((consts_value7 is not None) and [consts_value7.value] or [None])[0] 
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

    # $ANTLR end "consts_values"


    class consts_value_return(TreeRuleReturnScope):
        def __init__(self):
            super(Backend.consts_value_return, self).__init__()

            self.name = None
            self.value = None





    # $ANTLR start "consts_value"
    # grammar/Backend.g:55:1: consts_value returns [ name , value ] : ( ^( ID num_whole ) | ^( ID num_fract ) );
    def consts_value(self, ):
        retval = self.consts_value_return()
        retval.start = self.input.LT(1)


        ID8 = None
        ID10 = None
        num_whole9 = None

        num_fract11 = None


        try:
            try:
                # grammar/Backend.g:57:5: ( ^( ID num_whole ) | ^( ID num_fract ) )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == ID) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == 2) :
                        LA4_2 = self.input.LA(3)

                        if (LA4_2 == MINUS) :
                            LA4_3 = self.input.LA(4)

                            if (LA4_3 == NUMBER) :
                                LA4_5 = self.input.LA(5)

                                if (LA4_5 == DIVIDE) :
                                    alt4 = 2
                                elif (LA4_5 == 3) :
                                    alt4 = 1
                                else:
                                    nvae = NoViableAltException("", 4, 5, self.input)

                                    raise nvae


                            else:
                                nvae = NoViableAltException("", 4, 3, self.input)

                                raise nvae


                        elif (LA4_2 == NUMBER) :
                            LA4_4 = self.input.LA(4)

                            if (LA4_4 == DIVIDE) :
                                alt4 = 2
                            elif (LA4_4 == 3) :
                                alt4 = 1
                            else:
                                nvae = NoViableAltException("", 4, 4, self.input)

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
                    # grammar/Backend.g:57:9: ^( ID num_whole )
                    pass 
                    ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value357)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_num_whole_in_consts_value359)
                    num_whole9 = self.num_whole()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID8.text , num_whole9 
                    #action end



                elif alt4 == 2:
                    # grammar/Backend.g:59:9: ^( ID num_fract )
                    pass 
                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value387)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_num_fract_in_consts_value389)
                    num_fract11 = self.num_fract()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    retval.name , retval.value = ID10.text , num_fract11 
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


        MINUS12 = None
        NUMBER13 = None
        NUMBER14 = None

        try:
            try:
                # grammar/Backend.g:65:5: ( ( MINUS NUMBER ) | ( NUMBER ) )
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
                    # grammar/Backend.g:65:9: ( MINUS NUMBER )
                    pass 
                    # grammar/Backend.g:65:9: ( MINUS NUMBER )
                    # grammar/Backend.g:65:11: MINUS NUMBER
                    pass 
                    MINUS12 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole434)

                    NUMBER13 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole436)




                    #action start
                    value = int ( MINUS12.text + NUMBER13.text ) 
                    #action end



                elif alt5 == 2:
                    # grammar/Backend.g:67:9: ( NUMBER )
                    pass 
                    # grammar/Backend.g:67:9: ( NUMBER )
                    # grammar/Backend.g:67:11: NUMBER
                    pass 
                    NUMBER14 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole464)




                    #action start
                    value = int ( NUMBER14.text ) 
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
        MINUS15 = None

        try:
            try:
                # grammar/Backend.g:73:5: ( ( MINUS n= NUMBER DIVIDE d= NUMBER ) | (n= NUMBER DIVIDE d= NUMBER ) )
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
                    # grammar/Backend.g:73:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    pass 
                    # grammar/Backend.g:73:9: ( MINUS n= NUMBER DIVIDE d= NUMBER )
                    # grammar/Backend.g:73:11: MINUS n= NUMBER DIVIDE d= NUMBER
                    pass 
                    MINUS15 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract509)

                    n = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract515)

                    self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract517)

                    d = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract523)




                    #action start
                                
                    value = Fraction ( int ( MINUS15.text + n.text ) ,
                        int ( d.text ) )
                                
                    #action end



                elif alt6 == 2:
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



 

    FOLLOW_module_in_start86 = frozenset([1, 4, 10])
    FOLLOW_consts_in_start113 = frozenset([1, 4, 10])
    FOLLOW_MODULE_in_module168 = frozenset([2])
    FOLLOW_ID_in_module170 = frozenset([3])
    FOLLOW_CONSTS_in_consts213 = frozenset([2])
    FOLLOW_ID_in_consts215 = frozenset([3])
    FOLLOW_CONSTS_in_consts243 = frozenset([2])
    FOLLOW_ID_in_consts245 = frozenset([7])
    FOLLOW_consts_values_in_consts247 = frozenset([3])
    FOLLOW_consts_value_in_consts_values302 = frozenset([1, 7])
    FOLLOW_ID_in_consts_value357 = frozenset([2])
    FOLLOW_num_whole_in_consts_value359 = frozenset([3])
    FOLLOW_ID_in_consts_value387 = frozenset([2])
    FOLLOW_num_fract_in_consts_value389 = frozenset([3])
    FOLLOW_MINUS_in_num_whole434 = frozenset([11])
    FOLLOW_NUMBER_in_num_whole436 = frozenset([1])
    FOLLOW_NUMBER_in_num_whole464 = frozenset([1])
    FOLLOW_MINUS_in_num_fract509 = frozenset([11])
    FOLLOW_NUMBER_in_num_fract515 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract517 = frozenset([11])
    FOLLOW_NUMBER_in_num_fract523 = frozenset([1])
    FOLLOW_NUMBER_in_num_fract555 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract557 = frozenset([11])
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
