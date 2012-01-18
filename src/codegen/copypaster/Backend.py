# $ANTLR 3.4 copypaster/Backend.g 2012-01-16 18:05:36

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CHARS=4
DEDENT=5
INDENT=6
NEWLINE=7
WHITESPACE=8

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CHARS", "DEDENT", "INDENT", "NEWLINE", "WHITESPACE"
]




class Backend(TreeParser):
    grammarFileName = "copypaster/Backend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(Backend, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # copypaster/Backend.g:10:1: start returns [ value ] : ( INDENT | DEDENT | NEWLINE | CHARS )+ ;
    def start(self, ):
        value = None


        INDENT1 = None
        DEDENT2 = None
        NEWLINE3 = None
        CHARS4 = None

        value = list ( ) 
        try:
            try:
                # copypaster/Backend.g:13:5: ( ( INDENT | DEDENT | NEWLINE | CHARS )+ )
                # copypaster/Backend.g:13:9: ( INDENT | DEDENT | NEWLINE | CHARS )+
                pass 
                # copypaster/Backend.g:13:9: ( INDENT | DEDENT | NEWLINE | CHARS )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 5
                    LA1 = self.input.LA(1)
                    if LA1 == INDENT:
                        alt1 = 1
                    elif LA1 == DEDENT:
                        alt1 = 2
                    elif LA1 == NEWLINE:
                        alt1 = 3
                    elif LA1 == CHARS:
                        alt1 = 4

                    if alt1 == 1:
                        # copypaster/Backend.g:13:11: INDENT
                        pass 
                        INDENT1 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_start80)

                        #action start
                        value . append ( INDENT1.text ) 
                        #action end



                    elif alt1 == 2:
                        # copypaster/Backend.g:14:11: DEDENT
                        pass 
                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_start94)

                        #action start
                        value . append ( DEDENT2.text ) 
                        #action end



                    elif alt1 == 3:
                        # copypaster/Backend.g:15:11: NEWLINE
                        pass 
                        NEWLINE3 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_start108)

                        #action start
                        value . append ( NEWLINE3.text ) 
                        #action end



                    elif alt1 == 4:
                        # copypaster/Backend.g:16:11: CHARS
                        pass 
                        CHARS4 = self.match(self.input, CHARS, self.FOLLOW_CHARS_in_start122)

                        #action start
                        value . append ( CHARS4.text ) 
                        #action end



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "start"



 

    FOLLOW_INDENT_in_start80 = frozenset([1, 4, 5, 6, 7])
    FOLLOW_DEDENT_in_start94 = frozenset([1, 4, 5, 6, 7])
    FOLLOW_NEWLINE_in_start108 = frozenset([1, 4, 5, 6, 7])
    FOLLOW_CHARS_in_start122 = frozenset([1, 4, 5, 6, 7])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Backend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
