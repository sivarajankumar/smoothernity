# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-19 16:41:24

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

                    if ((CONSTS <= LA1_0 <= CURLY_OPEN) or (DIVIDE <= LA1_0 <= MODULE) or LA1_0 == NUMBER or (TYPES <= LA1_0 <= UNDERSCORE)) :
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
    # grammar/ShyCopypasterBackend.g:16:1: block returns [ value ] : ( ( arbitrary_token )+ NEWLINE | INDENT a= NEWLINE (b= block )+ DEDENT c= NEWLINE | COPY ( block )+ PASTE REPLACE ID WITH block );
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
                # grammar/ShyCopypasterBackend.g:19:5: ( ( arbitrary_token )+ NEWLINE | INDENT a= NEWLINE (b= block )+ DEDENT c= NEWLINE | COPY ( block )+ PASTE REPLACE ID WITH block )
                alt5 = 3
                LA5 = self.input.LA(1)
                if LA5 == CONSTS or LA5 == CURLY_CLOSE or LA5 == CURLY_OPEN or LA5 == DIVIDE or LA5 == EXPRESSION or LA5 == ID or LA5 == MINUS or LA5 == MODULE or LA5 == NUMBER or LA5 == TYPES or LA5 == UNDERSCORE:
                    alt5 = 1
                elif LA5 == INDENT:
                    alt5 = 2
                elif LA5 == COPY:
                    alt5 = 3
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
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



                elif alt5 == 2:
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

                        if ((CONSTS <= LA3_0 <= CURLY_OPEN) or (DIVIDE <= LA3_0 <= MODULE) or LA3_0 == NUMBER or (TYPES <= LA3_0 <= UNDERSCORE)) :
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



                elif alt5 == 3:
                    # grammar/ShyCopypasterBackend.g:24:7: COPY ( block )+ PASTE REPLACE ID WITH block
                    pass 
                    self.match(self.input, COPY, self.FOLLOW_COPY_in_block198)

                    # grammar/ShyCopypasterBackend.g:24:12: ( block )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if ((CONSTS <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= MODULE) or LA4_0 == NUMBER or (TYPES <= LA4_0 <= UNDERSCORE)) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammar/ShyCopypasterBackend.g:24:12: block
                            pass 
                            self._state.following.append(self.FOLLOW_block_in_block200)
                            self.block()

                            self._state.following.pop()


                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    self.match(self.input, PASTE, self.FOLLOW_PASTE_in_block204)

                    self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_block206)

                    self.match(self.input, ID, self.FOLLOW_ID_in_block208)

                    self.match(self.input, WITH, self.FOLLOW_WITH_in_block210)

                    self._state.following.append(self.FOLLOW_block_in_block212)
                    self.block()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "block"



    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterBackend.g:27:1: arbitrary_token returns [ value ] : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
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
                # grammar/ShyCopypasterBackend.g:29:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                alt6 = 11
                LA6 = self.input.LA(1)
                if LA6 == CONSTS:
                    alt6 = 1
                elif LA6 == MODULE:
                    alt6 = 2
                elif LA6 == TYPES:
                    alt6 = 3
                elif LA6 == CURLY_OPEN:
                    alt6 = 4
                elif LA6 == CURLY_CLOSE:
                    alt6 = 5
                elif LA6 == DIVIDE:
                    alt6 = 6
                elif LA6 == MINUS:
                    alt6 = 7
                elif LA6 == UNDERSCORE:
                    alt6 = 8
                elif LA6 == ID:
                    alt6 = 9
                elif LA6 == NUMBER:
                    alt6 = 10
                elif LA6 == EXPRESSION:
                    alt6 = 11
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammar/ShyCopypasterBackend.g:29:7: CONSTS
                    pass 
                    CONSTS6 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_arbitrary_token237)

                    #action start
                    value = CONSTS6.text 
                    #action end



                elif alt6 == 2:
                    # grammar/ShyCopypasterBackend.g:30:7: MODULE
                    pass 
                    MODULE7 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_arbitrary_token247)

                    #action start
                    value = MODULE7.text 
                    #action end



                elif alt6 == 3:
                    # grammar/ShyCopypasterBackend.g:31:7: TYPES
                    pass 
                    TYPES8 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_arbitrary_token257)

                    #action start
                    value = TYPES8.text 
                    #action end



                elif alt6 == 4:
                    # grammar/ShyCopypasterBackend.g:33:7: CURLY_OPEN
                    pass 
                    CURLY_OPEN9 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_arbitrary_token268)

                    #action start
                    value = CURLY_OPEN9.text 
                    #action end



                elif alt6 == 5:
                    # grammar/ShyCopypasterBackend.g:34:7: CURLY_CLOSE
                    pass 
                    CURLY_CLOSE10 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_arbitrary_token278)

                    #action start
                    value = CURLY_CLOSE10.text 
                    #action end



                elif alt6 == 6:
                    # grammar/ShyCopypasterBackend.g:35:7: DIVIDE
                    pass 
                    DIVIDE11 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_arbitrary_token288)

                    #action start
                    value = DIVIDE11.text 
                    #action end



                elif alt6 == 7:
                    # grammar/ShyCopypasterBackend.g:36:7: MINUS
                    pass 
                    MINUS12 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arbitrary_token298)

                    #action start
                    value = MINUS12.text 
                    #action end



                elif alt6 == 8:
                    # grammar/ShyCopypasterBackend.g:37:7: UNDERSCORE
                    pass 
                    UNDERSCORE13 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_arbitrary_token308)

                    #action start
                    value = UNDERSCORE13.text 
                    #action end



                elif alt6 == 9:
                    # grammar/ShyCopypasterBackend.g:38:7: ID
                    pass 
                    ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_token318)

                    #action start
                    value = ID14.text 
                    #action end



                elif alt6 == 10:
                    # grammar/ShyCopypasterBackend.g:39:7: NUMBER
                    pass 
                    NUMBER15 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_arbitrary_token328)

                    #action start
                    value = NUMBER15.text 
                    #action end



                elif alt6 == 11:
                    # grammar/ShyCopypasterBackend.g:40:7: EXPRESSION
                    pass 
                    EXPRESSION16 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_token338)

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



 

    FOLLOW_block_in_start78 = frozenset([1, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_arbitrary_token_in_block121 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_block135 = frozenset([1])
    FOLLOW_INDENT_in_block145 = frozenset([15])
    FOLLOW_NEWLINE_in_block151 = frozenset([4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_block_in_block167 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_block182 = frozenset([15])
    FOLLOW_NEWLINE_in_block188 = frozenset([1])
    FOLLOW_COPY_in_block198 = frozenset([4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_block_in_block200 = frozenset([4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 37, 38])
    FOLLOW_PASTE_in_block204 = frozenset([18])
    FOLLOW_REPLACE_in_block206 = frozenset([11])
    FOLLOW_ID_in_block208 = frozenset([40])
    FOLLOW_WITH_in_block210 = frozenset([4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_block_in_block212 = frozenset([1])
    FOLLOW_CONSTS_in_arbitrary_token237 = frozenset([1])
    FOLLOW_MODULE_in_arbitrary_token247 = frozenset([1])
    FOLLOW_TYPES_in_arbitrary_token257 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_arbitrary_token268 = frozenset([1])
    FOLLOW_CURLY_CLOSE_in_arbitrary_token278 = frozenset([1])
    FOLLOW_DIVIDE_in_arbitrary_token288 = frozenset([1])
    FOLLOW_MINUS_in_arbitrary_token298 = frozenset([1])
    FOLLOW_UNDERSCORE_in_arbitrary_token308 = frozenset([1])
    FOLLOW_ID_in_arbitrary_token318 = frozenset([1])
    FOLLOW_NUMBER_in_arbitrary_token328 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_token338 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
