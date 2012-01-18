# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-18 15:03:36

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



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




class ShyCopypasterBackend(TreeParser):
    grammarFileName = "grammar/ShyCopypasterBackend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyCopypasterBackend, self).__init__(input, state, *args, **kwargs)




        self.delegates = []






    # $ANTLR start "start"
    # grammar/ShyCopypasterBackend.g:10:1: start returns [ value ] : ( INDENT | DEDENT | NEWLINE | ID )+ ;
    def start(self, ):
        value = None


        INDENT1 = None
        DEDENT2 = None
        NEWLINE3 = None
        ID4 = None

        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:13:5: ( ( INDENT | DEDENT | NEWLINE | ID )+ )
                # grammar/ShyCopypasterBackend.g:13:9: ( INDENT | DEDENT | NEWLINE | ID )+
                pass 
                # grammar/ShyCopypasterBackend.g:13:9: ( INDENT | DEDENT | NEWLINE | ID )+
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
                    elif LA1 == ID:
                        alt1 = 4

                    if alt1 == 1:
                        # grammar/ShyCopypasterBackend.g:13:11: INDENT
                        pass 
                        INDENT1 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_start80)

                        #action start
                        value . append ( INDENT1.text ) 
                        #action end



                    elif alt1 == 2:
                        # grammar/ShyCopypasterBackend.g:14:11: DEDENT
                        pass 
                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_start94)

                        #action start
                        value . append ( DEDENT2.text ) 
                        #action end



                    elif alt1 == 3:
                        # grammar/ShyCopypasterBackend.g:15:11: NEWLINE
                        pass 
                        NEWLINE3 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_start108)

                        #action start
                        value . append ( NEWLINE3.text ) 
                        #action end



                    elif alt1 == 4:
                        # grammar/ShyCopypasterBackend.g:16:11: ID
                        pass 
                        ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_start122)

                        #action start
                        value . append ( ID4.text ) 
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



 

    FOLLOW_INDENT_in_start80 = frozenset([1, 7, 10, 11, 14])
    FOLLOW_DEDENT_in_start94 = frozenset([1, 7, 10, 11, 14])
    FOLLOW_NEWLINE_in_start108 = frozenset([1, 7, 10, 11, 14])
    FOLLOW_ID_in_start122 = frozenset([1, 7, 10, 11, 14])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
