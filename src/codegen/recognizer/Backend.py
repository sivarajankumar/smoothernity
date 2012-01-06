# $ANTLR 3.4 grammar/Backend.g 2012-01-06 13:08:37

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__7=7
T__8=8
ID=4
NEWLINE=5
WHITESPACE=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ID", "NEWLINE", "WHITESPACE", "'consts'", "'module'"
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

                    if (LA1_0 == 8) :
                        alt1 = 1
                    elif (LA1_0 == 7) :
                        alt1 = 2


                    if alt1 == 1:
                        # grammar/Backend.g:13:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start79)
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
                        self._state.following.append(self.FOLLOW_consts_in_start106)
                        consts2 = self.consts()

                        self._state.following.pop()

                        #action start
                                    
                        if 'consts' not in value :
                            value [ 'consts' ] = dict ( )
                        value [ 'consts' ] [ consts2 ] = dict ( )
                                    
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
                self.match(self.input, 8, self.FOLLOW_8_in_module161)

                self.match(self.input, DOWN, None)
                ID3 = self.match(self.input, ID, self.FOLLOW_ID_in_module163)

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



    # $ANTLR start "consts"
    # grammar/Backend.g:33:1: consts returns [ value ] : ^( 'consts' ID ) ;
    def consts(self, ):
        value = None


        ID4 = None

        try:
            try:
                # grammar/Backend.g:35:5: ( ^( 'consts' ID ) )
                # grammar/Backend.g:35:9: ^( 'consts' ID )
                pass 
                self.match(self.input, 7, self.FOLLOW_7_in_consts196)

                self.match(self.input, DOWN, None)
                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_consts198)

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

    # $ANTLR end "consts"



 

    FOLLOW_module_in_start79 = frozenset([1, 7, 8])
    FOLLOW_consts_in_start106 = frozenset([1, 7, 8])
    FOLLOW_8_in_module161 = frozenset([2])
    FOLLOW_ID_in_module163 = frozenset([3])
    FOLLOW_7_in_consts196 = frozenset([2])
    FOLLOW_ID_in_consts198 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
