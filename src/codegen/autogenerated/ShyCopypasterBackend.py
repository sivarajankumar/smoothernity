# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-18 19:28:50

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CONSTS=4
COPY=5
CURLY_CLOSE=6
CURLY_OPEN=7
DEDENT=8
DIVIDE=9
EXPRESSION=10
ID=11
INDENT=12
MINUS=13
MODULE=14
NEWLINE=15
NUMBER=16
PASTE=17
REPLACE=18
TREE_ARBITRARY_TOKEN=19
TREE_CONSTS=20
TREE_COPY=21
TREE_COPY_PASTE=22
TREE_EXPRESSION=23
TREE_HINT=24
TREE_HINT_NONE=25
TREE_MODULE=26
TREE_NUM_FRACT=27
TREE_NUM_WHOLE=28
TREE_PASTE=29
TREE_PASTE_REPLACE=30
TREE_PASTE_WITH=31
TREE_TYPES=32
TREE_TYPES_ITEM=33
TREE_TYPES_ITEM_ATTR=34
TREE_TYPES_ITEM_HINT=35
TREE_TYPES_ITEM_HINTS=36
TYPES=37
UNDERSCORE=38
WHITESPACE=39
WITH=40

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "COPY", "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", 
    "ID", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", "PASTE", "REPLACE", 
    "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_TYPES_ITEM_ATTR", "TREE_TYPES_ITEM_HINT", 
    "TREE_TYPES_ITEM_HINTS", "TYPES", "UNDERSCORE", "WHITESPACE", "WITH"
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
    # grammar/ShyCopypasterBackend.g:10:1: start returns [ value ] : ( block )* ;
    def start(self, ):
        value = None


        block1 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:13:5: ( ( block )* )
                # grammar/ShyCopypasterBackend.g:13:7: ( block )*
                pass 
                # grammar/ShyCopypasterBackend.g:13:7: ( block )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CONSTS or (CURLY_CLOSE <= LA1_0 <= CURLY_OPEN) or (DIVIDE <= LA1_0 <= MODULE) or LA1_0 == NUMBER or (TYPES <= LA1_0 <= UNDERSCORE)) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammar/ShyCopypasterBackend.g:13:9: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_start78)
                        block1 = self.block()

                        self._state.following.pop()

                        #action start
                        value += block1 
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



    # $ANTLR start "block"
    # grammar/ShyCopypasterBackend.g:16:1: block returns [ value ] : ( ( arbitrary_token )+ NEWLINE | INDENT a= NEWLINE (b= block )+ DEDENT c= NEWLINE );
    def block(self, ):
        value = None


        a = None
        c = None
        NEWLINE3 = None
        INDENT4 = None
        DEDENT5 = None
        b = None

        arbitrary_token2 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:19:5: ( ( arbitrary_token )+ NEWLINE | INDENT a= NEWLINE (b= block )+ DEDENT c= NEWLINE )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == CONSTS or (CURLY_CLOSE <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= ID) or (MINUS <= LA4_0 <= MODULE) or LA4_0 == NUMBER or (TYPES <= LA4_0 <= UNDERSCORE)) :
                    alt4 = 1
                elif (LA4_0 == INDENT) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # grammar/ShyCopypasterBackend.g:19:7: ( arbitrary_token )+ NEWLINE
                    pass 
                    # grammar/ShyCopypasterBackend.g:19:7: ( arbitrary_token )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= ID) or (MINUS <= LA2_0 <= MODULE) or LA2_0 == NUMBER or (TYPES <= LA2_0 <= UNDERSCORE)) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyCopypasterBackend.g:19:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_block121)
                            arbitrary_token2 = self.arbitrary_token()

                            self._state.following.pop()

                            #action start
                            value . append ( arbitrary_token2 ) 
                            #action end



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    NEWLINE3 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block135)

                    #action start
                    value += [ NEWLINE3.text ] 
                    #action end



                elif alt4 == 2:
                    # grammar/ShyCopypasterBackend.g:21:7: INDENT a= NEWLINE (b= block )+ DEDENT c= NEWLINE
                    pass 
                    INDENT4 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_block145)

                    a = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block151)

                    #action start
                    value += [ INDENT4.text , a.text ] 
                    #action end


                    # grammar/ShyCopypasterBackend.g:22:7: (b= block )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == CONSTS or (CURLY_CLOSE <= LA3_0 <= CURLY_OPEN) or (DIVIDE <= LA3_0 <= MODULE) or LA3_0 == NUMBER or (TYPES <= LA3_0 <= UNDERSCORE)) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammar/ShyCopypasterBackend.g:22:9: b= block
                            pass 
                            self._state.following.append(self.FOLLOW_block_in_block167)
                            b = self.block()

                            self._state.following.pop()

                            #action start
                            value += b 
                            #action end



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    DEDENT5 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_block182)

                    c = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block188)

                    #action start
                    value += [ DEDENT5.text , c.text ] 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "block"



    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterBackend.g:26:1: arbitrary_token returns [ value ] : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        value = None


        CONSTS6 = None
        MODULE7 = None
        TYPES8 = None
        CURLY_OPEN9 = None
        CURLY_CLOSE10 = None
        DIVIDE11 = None
        MINUS12 = None
        UNDERSCORE13 = None
        ID14 = None
        NUMBER15 = None
        EXPRESSION16 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:28:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                alt5 = 11
                LA5 = self.input.LA(1)
                if LA5 == CONSTS:
                    alt5 = 1
                elif LA5 == MODULE:
                    alt5 = 2
                elif LA5 == TYPES:
                    alt5 = 3
                elif LA5 == CURLY_OPEN:
                    alt5 = 4
                elif LA5 == CURLY_CLOSE:
                    alt5 = 5
                elif LA5 == DIVIDE:
                    alt5 = 6
                elif LA5 == MINUS:
                    alt5 = 7
                elif LA5 == UNDERSCORE:
                    alt5 = 8
                elif LA5 == ID:
                    alt5 = 9
                elif LA5 == NUMBER:
                    alt5 = 10
                elif LA5 == EXPRESSION:
                    alt5 = 11
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyCopypasterBackend.g:28:7: CONSTS
                    pass 
                    CONSTS6 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_arbitrary_token215)

                    #action start
                    value = CONSTS6.text 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyCopypasterBackend.g:29:7: MODULE
                    pass 
                    MODULE7 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_arbitrary_token225)

                    #action start
                    value = MODULE7.text 
                    #action end



                elif alt5 == 3:
                    # grammar/ShyCopypasterBackend.g:30:7: TYPES
                    pass 
                    TYPES8 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_arbitrary_token235)

                    #action start
                    value = TYPES8.text 
                    #action end



                elif alt5 == 4:
                    # grammar/ShyCopypasterBackend.g:32:7: CURLY_OPEN
                    pass 
                    CURLY_OPEN9 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_arbitrary_token246)

                    #action start
                    value = CURLY_OPEN9.text 
                    #action end



                elif alt5 == 5:
                    # grammar/ShyCopypasterBackend.g:33:7: CURLY_CLOSE
                    pass 
                    CURLY_CLOSE10 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_arbitrary_token256)

                    #action start
                    value = CURLY_CLOSE10.text 
                    #action end



                elif alt5 == 6:
                    # grammar/ShyCopypasterBackend.g:34:7: DIVIDE
                    pass 
                    DIVIDE11 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_arbitrary_token266)

                    #action start
                    value = DIVIDE11.text 
                    #action end



                elif alt5 == 7:
                    # grammar/ShyCopypasterBackend.g:35:7: MINUS
                    pass 
                    MINUS12 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arbitrary_token276)

                    #action start
                    value = MINUS12.text 
                    #action end



                elif alt5 == 8:
                    # grammar/ShyCopypasterBackend.g:36:7: UNDERSCORE
                    pass 
                    UNDERSCORE13 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_arbitrary_token286)

                    #action start
                    value = UNDERSCORE13.text 
                    #action end



                elif alt5 == 9:
                    # grammar/ShyCopypasterBackend.g:37:7: ID
                    pass 
                    ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_token296)

                    #action start
                    value = ID14.text 
                    #action end



                elif alt5 == 10:
                    # grammar/ShyCopypasterBackend.g:38:7: NUMBER
                    pass 
                    NUMBER15 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_arbitrary_token306)

                    #action start
                    value = NUMBER15.text 
                    #action end



                elif alt5 == 11:
                    # grammar/ShyCopypasterBackend.g:39:7: EXPRESSION
                    pass 
                    EXPRESSION16 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_token316)

                    #action start
                    value = EXPRESSION16.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_token"



 

    FOLLOW_block_in_start78 = frozenset([1, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_arbitrary_token_in_block121 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_block135 = frozenset([1])
    FOLLOW_INDENT_in_block145 = frozenset([15])
    FOLLOW_NEWLINE_in_block151 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_block_in_block167 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_block182 = frozenset([15])
    FOLLOW_NEWLINE_in_block188 = frozenset([1])
    FOLLOW_CONSTS_in_arbitrary_token215 = frozenset([1])
    FOLLOW_MODULE_in_arbitrary_token225 = frozenset([1])
    FOLLOW_TYPES_in_arbitrary_token235 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_arbitrary_token246 = frozenset([1])
    FOLLOW_CURLY_CLOSE_in_arbitrary_token256 = frozenset([1])
    FOLLOW_DIVIDE_in_arbitrary_token266 = frozenset([1])
    FOLLOW_MINUS_in_arbitrary_token276 = frozenset([1])
    FOLLOW_UNDERSCORE_in_arbitrary_token286 = frozenset([1])
    FOLLOW_ID_in_arbitrary_token296 = frozenset([1])
    FOLLOW_NUMBER_in_arbitrary_token306 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_token316 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
