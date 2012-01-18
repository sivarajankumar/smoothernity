# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-18 15:18:23

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
    # grammar/ShyCopypasterBackend.g:10:1: start returns [ value ] : ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION )* ;
    def start(self, ):
        value = None


        CONSTS1 = None
        DEDENT2 = None
        INDENT3 = None
        MODULE4 = None
        TYPES5 = None
        CURLY_OPEN6 = None
        CURLY_CLOSE7 = None
        DIVIDE8 = None
        MINUS9 = None
        UNDERSCORE10 = None
        NEWLINE11 = None
        ID12 = None
        NUMBER13 = None
        EXPRESSION14 = None

        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:13:5: ( ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION )* )
                # grammar/ShyCopypasterBackend.g:13:7: ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION )*
                pass 
                # grammar/ShyCopypasterBackend.g:13:7: ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION )*
                while True: #loop1
                    alt1 = 15
                    LA1 = self.input.LA(1)
                    if LA1 == CONSTS:
                        alt1 = 1
                    elif LA1 == DEDENT:
                        alt1 = 2
                    elif LA1 == INDENT:
                        alt1 = 3
                    elif LA1 == MODULE:
                        alt1 = 4
                    elif LA1 == TYPES:
                        alt1 = 5
                    elif LA1 == CURLY_OPEN:
                        alt1 = 6
                    elif LA1 == CURLY_CLOSE:
                        alt1 = 7
                    elif LA1 == DIVIDE:
                        alt1 = 8
                    elif LA1 == MINUS:
                        alt1 = 9
                    elif LA1 == UNDERSCORE:
                        alt1 = 10
                    elif LA1 == NEWLINE:
                        alt1 = 11
                    elif LA1 == ID:
                        alt1 = 12
                    elif LA1 == NUMBER:
                        alt1 = 13
                    elif LA1 == EXPRESSION:
                        alt1 = 14

                    if alt1 == 1:
                        # grammar/ShyCopypasterBackend.g:13:9: CONSTS
                        pass 
                        CONSTS1 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_start78)

                        #action start
                        value . append ( CONSTS1.text ) 
                        #action end



                    elif alt1 == 2:
                        # grammar/ShyCopypasterBackend.g:14:9: DEDENT
                        pass 
                        DEDENT2 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_start90)

                        #action start
                        value . append ( DEDENT2.text ) 
                        #action end



                    elif alt1 == 3:
                        # grammar/ShyCopypasterBackend.g:15:9: INDENT
                        pass 
                        INDENT3 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_start102)

                        #action start
                        value . append ( INDENT3.text ) 
                        #action end



                    elif alt1 == 4:
                        # grammar/ShyCopypasterBackend.g:16:9: MODULE
                        pass 
                        MODULE4 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_start114)

                        #action start
                        value . append ( MODULE4.text ) 
                        #action end



                    elif alt1 == 5:
                        # grammar/ShyCopypasterBackend.g:17:9: TYPES
                        pass 
                        TYPES5 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_start126)

                        #action start
                        value . append ( TYPES5.text ) 
                        #action end



                    elif alt1 == 6:
                        # grammar/ShyCopypasterBackend.g:19:9: CURLY_OPEN
                        pass 
                        CURLY_OPEN6 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_start139)

                        #action start
                        value . append ( CURLY_OPEN6.text ) 
                        #action end



                    elif alt1 == 7:
                        # grammar/ShyCopypasterBackend.g:20:9: CURLY_CLOSE
                        pass 
                        CURLY_CLOSE7 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_start151)

                        #action start
                        value . append ( CURLY_CLOSE7.text ) 
                        #action end



                    elif alt1 == 8:
                        # grammar/ShyCopypasterBackend.g:21:9: DIVIDE
                        pass 
                        DIVIDE8 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_start163)

                        #action start
                        value . append ( DIVIDE8.text ) 
                        #action end



                    elif alt1 == 9:
                        # grammar/ShyCopypasterBackend.g:22:9: MINUS
                        pass 
                        MINUS9 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_start175)

                        #action start
                        value . append ( MINUS9.text ) 
                        #action end



                    elif alt1 == 10:
                        # grammar/ShyCopypasterBackend.g:23:9: UNDERSCORE
                        pass 
                        UNDERSCORE10 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_start187)

                        #action start
                        value . append ( UNDERSCORE10.text ) 
                        #action end



                    elif alt1 == 11:
                        # grammar/ShyCopypasterBackend.g:24:9: NEWLINE
                        pass 
                        NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_start199)

                        #action start
                        value . append ( NEWLINE11.text ) 
                        #action end



                    elif alt1 == 12:
                        # grammar/ShyCopypasterBackend.g:25:9: ID
                        pass 
                        ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_start211)

                        #action start
                        value . append ( ID12.text ) 
                        #action end



                    elif alt1 == 13:
                        # grammar/ShyCopypasterBackend.g:26:9: NUMBER
                        pass 
                        NUMBER13 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_start223)

                        #action start
                        value . append ( NUMBER13.text ) 
                        #action end



                    elif alt1 == 14:
                        # grammar/ShyCopypasterBackend.g:27:9: EXPRESSION
                        pass 
                        EXPRESSION14 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_start235)

                        #action start
                        value . append ( EXPRESSION14.text ) 
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



 

    FOLLOW_CONSTS_in_start78 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_DEDENT_in_start90 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_INDENT_in_start102 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_MODULE_in_start114 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_TYPES_in_start126 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_CURLY_OPEN_in_start139 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_CURLY_CLOSE_in_start151 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_DIVIDE_in_start163 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_MINUS_in_start175 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_UNDERSCORE_in_start187 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_NEWLINE_in_start199 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_ID_in_start211 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_NUMBER_in_start223 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])
    FOLLOW_EXPRESSION_in_start235 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 28, 29])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
