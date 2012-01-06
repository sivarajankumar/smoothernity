# $ANTLR 3.4 grammar/Backend.g 2012-01-06 11:00:11

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__7=7
ID=4
NEWLINE=5
WHITESPACE=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ID", "NEWLINE", "WHITESPACE", "'module'"
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
    # grammar/Backend.g:10:1: start returns [ value ] : ( module )* ;
    def start(self, ):
        value = None


        module1 = None


        value = dict ( ) 
        try:
            try:
                # grammar/Backend.g:13:5: ( ( module )* )
                # grammar/Backend.g:13:9: ( module )*
                pass 
                # grammar/Backend.g:13:9: ( module )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 7) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammar/Backend.g:13:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start79)
                        module1 = self.module()

                        self._state.following.pop()

                        #action start
                                    
                        if 'module' not in value :
                            value [ 'module' ] = dict ( )
                        value [ 'module' ] [ module1 ] = { }
                                    
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
    # grammar/Backend.g:22:1: module returns [ value ] : ^( 'module' ID ) ;
    def module(self, ):
        value = None


        ID2 = None

        try:
            try:
                # grammar/Backend.g:24:5: ( ^( 'module' ID ) )
                # grammar/Backend.g:24:9: ^( 'module' ID )
                pass 
                self.match(self.input, 7, self.FOLLOW_7_in_module135)

                self.match(self.input, DOWN, None)
                ID2 = self.match(self.input, ID, self.FOLLOW_ID_in_module137)

                self.match(self.input, UP, None)


                #action start
                value = ID2.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "module"



 

    FOLLOW_module_in_start79 = frozenset([1, 7])
    FOLLOW_7_in_module135 = frozenset([2])
    FOLLOW_ID_in_module137 = frozenset([3])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
