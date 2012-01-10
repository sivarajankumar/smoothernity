# $ANTLR 3.4 grammar/Backend.g 2012-01-10 21:15:14

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__10=10
T__11=11
ID=4
NEWLINE=5
NL=6
NUMBER=7
SP=8
WHITESPACE=9

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ID", "NEWLINE", "NL", "NUMBER", "SP", "WHITESPACE", "'consts'", "'module'"
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
    # grammar/Backend.g:10:1: start returns [ value ] : ( module | consts )* ;
    def start(self, ):
        value = None


        module1 = None

        consts2 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:13:5: ( ( module | consts )* )
                # grammar/Backend.g:13:9: ( module | consts )*
                pass 
                # grammar/Backend.g:13:9: ( module | consts )*
                while True: #loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 11) :
                        alt1 = 1
                    elif (LA1_0 == 10) :
                        alt1 = 2


                    if alt1 == 1:
                        # grammar/Backend.g:13:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start80)
                        module1 = self.module()

                        self._state.following.pop()

                        #action start
                                    
                        if 'module' not in value :
                            value [ 'module' ] = dict ( )
                        value [ 'module' ] [ module1 ] = dict ( )
                                    
                        #action end



                    elif alt1 == 2:
                        # grammar/Backend.g:19:11: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start107)
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
    # grammar/Backend.g:28:1: module returns [ value ] : ^( 'module' ID ) ;
    def module(self, ):
        value = None


        ID3 = None

        try:
            try:
                # grammar/Backend.g:30:5: ( ^( 'module' ID ) )
                # grammar/Backend.g:30:9: ^( 'module' ID )
                pass 
                self.match(self.input, 11, self.FOLLOW_11_in_module162)

                self.match(self.input, DOWN, None)
                ID3 = self.match(self.input, ID, self.FOLLOW_ID_in_module164)

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
    # grammar/Backend.g:33:1: consts returns [ title , content ] : ( ^( 'consts' ID ) | ^( 'consts' ID consts_values ) );
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        ID4 = None
        ID5 = None
        consts_values6 = None


        retval.content = dict ( ) 
        try:
            try:
                # grammar/Backend.g:36:5: ( ^( 'consts' ID ) | ^( 'consts' ID consts_values ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 10) :
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
                    # grammar/Backend.g:36:9: ^( 'consts' ID )
                    pass 
                    self.match(self.input, 10, self.FOLLOW_10_in_consts207)

                    self.match(self.input, DOWN, None)
                    ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_consts209)

                    self.match(self.input, UP, None)


                    #action start
                    retval.title , retval.content = ID4.text , dict ( ) 
                    #action end



                elif alt2 == 2:
                    # grammar/Backend.g:38:9: ^( 'consts' ID consts_values )
                    pass 
                    self.match(self.input, 10, self.FOLLOW_10_in_consts237)

                    self.match(self.input, DOWN, None)
                    ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_consts239)

                    self._state.following.append(self.FOLLOW_consts_values_in_consts241)
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
    # grammar/Backend.g:42:1: consts_values returns [ value ] : ( consts_value )+ ;
    def consts_values(self, ):
        value = None


        consts_value7 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:45:5: ( ( consts_value )+ )
                # grammar/Backend.g:45:9: ( consts_value )+
                pass 
                # grammar/Backend.g:45:9: ( consts_value )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == ID) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/Backend.g:45:11: consts_value
                        pass 
                        self._state.following.append(self.FOLLOW_consts_value_in_consts_values296)
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
    # grammar/Backend.g:48:1: consts_value returns [ name , value ] : ^( ID NUMBER ) ;
    def consts_value(self, ):
        retval = self.consts_value_return()
        retval.start = self.input.LT(1)


        ID8 = None
        NUMBER9 = None

        try:
            try:
                # grammar/Backend.g:50:5: ( ^( ID NUMBER ) )
                # grammar/Backend.g:50:9: ^( ID NUMBER )
                pass 
                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value331)

                self.match(self.input, DOWN, None)
                NUMBER9 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_consts_value333)

                self.match(self.input, UP, None)


                #action start
                retval.name , retval.value = ID8.text , int ( NUMBER9.text ) 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "consts_value"



 

    FOLLOW_module_in_start80 = frozenset([1, 10, 11])
    FOLLOW_consts_in_start107 = frozenset([1, 10, 11])
    FOLLOW_11_in_module162 = frozenset([2])
    FOLLOW_ID_in_module164 = frozenset([3])
    FOLLOW_10_in_consts207 = frozenset([2])
    FOLLOW_ID_in_consts209 = frozenset([3])
    FOLLOW_10_in_consts237 = frozenset([2])
    FOLLOW_ID_in_consts239 = frozenset([4])
    FOLLOW_consts_values_in_consts241 = frozenset([3])
    FOLLOW_consts_value_in_consts_values296 = frozenset([1, 4])
    FOLLOW_ID_in_consts_value331 = frozenset([2])
    FOLLOW_NUMBER_in_consts_value333 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
