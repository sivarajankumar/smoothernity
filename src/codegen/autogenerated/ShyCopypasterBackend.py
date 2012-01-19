# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-19 17:27:28

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
                # grammar/ShyCopypasterBackend.g:13:9: ( block )*
                pass 
                # grammar/ShyCopypasterBackend.g:13:9: ( block )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == CONSTS or (CURLY_CLOSE <= LA1_0 <= CURLY_OPEN) or (DIVIDE <= LA1_0 <= MODULE) or LA1_0 == NUMBER or LA1_0 == TREE_COPY or (TYPES <= LA1_0 <= UNDERSCORE)) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammar/ShyCopypasterBackend.g:13:11: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_start80)
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
    # grammar/ShyCopypasterBackend.g:16:1: block returns [ value ] : ( ( arbitrary_token )+ NEWLINE | INDENT nl1= NEWLINE (b1= block )+ DEDENT nl2= NEWLINE | ^( TREE_COPY (b2= block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE pr= paste_replace ) ^( TREE_PASTE_WITH pw= paste_with ) ) )+ ) );
    def block(self, ):
        value = None


        nl1 = None
        nl2 = None
        NEWLINE3 = None
        INDENT4 = None
        DEDENT5 = None
        b1 = None

        b2 = None

        pr = None

        pw = None

        arbitrary_token2 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:19:5: ( ( arbitrary_token )+ NEWLINE | INDENT nl1= NEWLINE (b1= block )+ DEDENT nl2= NEWLINE | ^( TREE_COPY (b2= block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE pr= paste_replace ) ^( TREE_PASTE_WITH pw= paste_with ) ) )+ ) )
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == CONSTS or LA6 == CURLY_CLOSE or LA6 == CURLY_OPEN or LA6 == DIVIDE or LA6 == EXPRESSION or LA6 == ID or LA6 == MINUS or LA6 == MODULE or LA6 == NUMBER or LA6 == TYPES or LA6 == UNDERSCORE:
                    alt6 = 1
                elif LA6 == INDENT:
                    alt6 = 2
                elif LA6 == TREE_COPY:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammar/ShyCopypasterBackend.g:19:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    # grammar/ShyCopypasterBackend.g:19:9: ( arbitrary_token )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= ID) or (MINUS <= LA2_0 <= MODULE) or LA2_0 == NUMBER or (TYPES <= LA2_0 <= UNDERSCORE)) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyCopypasterBackend.g:19:11: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_block125)
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


                    NEWLINE3 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block161)

                    #action start
                    value += [ NEWLINE3.text ] 
                    #action end



                elif alt6 == 2:
                    # grammar/ShyCopypasterBackend.g:24:9: INDENT nl1= NEWLINE (b1= block )+ DEDENT nl2= NEWLINE
                    pass 
                    INDENT4 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_block185)

                    nl1 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block191)

                    #action start
                    value += [ INDENT4.text , nl1.text ] 
                    #action end


                    # grammar/ShyCopypasterBackend.g:26:9: (b1= block )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == CONSTS or (CURLY_CLOSE <= LA3_0 <= CURLY_OPEN) or (DIVIDE <= LA3_0 <= MODULE) or LA3_0 == NUMBER or LA3_0 == TREE_COPY or (TYPES <= LA3_0 <= UNDERSCORE)) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammar/ShyCopypasterBackend.g:26:11: b1= block
                            pass 
                            self._state.following.append(self.FOLLOW_block_in_block221)
                            b1 = self.block()

                            self._state.following.pop()

                            #action start
                            value += b1 
                            #action end



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    DEDENT5 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_block258)

                    nl2 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block264)

                    #action start
                    value += [ DEDENT5.text , nl2.text ] 
                    #action end



                elif alt6 == 3:
                    # grammar/ShyCopypasterBackend.g:31:9: ^( TREE_COPY (b2= block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE pr= paste_replace ) ^( TREE_PASTE_WITH pw= paste_with ) ) )+ )
                    pass 
                    #action start
                    _copy , _paste = list ( ) , list ( ) 
                    #action end


                    self.match(self.input, TREE_COPY, self.FOLLOW_TREE_COPY_in_block300)

                    self.match(self.input, DOWN, None)
                    # grammar/ShyCopypasterBackend.g:33:13: (b2= block )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == CONSTS or (CURLY_CLOSE <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= MODULE) or LA4_0 == NUMBER or LA4_0 == TREE_COPY or (TYPES <= LA4_0 <= UNDERSCORE)) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammar/ShyCopypasterBackend.g:33:15: b2= block
                            pass 
                            self._state.following.append(self.FOLLOW_block_in_block320)
                            b2 = self.block()

                            self._state.following.pop()

                            #action start
                            _copy += b2 
                            #action end



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    # grammar/ShyCopypasterBackend.g:36:9: ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE pr= paste_replace ) ^( TREE_PASTE_WITH pw= paste_with ) ) )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == TREE_PASTE) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammar/ShyCopypasterBackend.g:36:11: ^( TREE_PASTE ^( TREE_PASTE_REPLACE pr= paste_replace ) ^( TREE_PASTE_WITH pw= paste_with ) )
                            pass 
                            self.match(self.input, TREE_PASTE, self.FOLLOW_TREE_PASTE_in_block369)

                            self.match(self.input, DOWN, None)
                            self.match(self.input, TREE_PASTE_REPLACE, self.FOLLOW_TREE_PASTE_REPLACE_in_block385)

                            self.match(self.input, DOWN, None)
                            self._state.following.append(self.FOLLOW_paste_replace_in_block391)
                            pr = self.paste_replace()

                            self._state.following.pop()

                            self.match(self.input, UP, None)


                            self.match(self.input, TREE_PASTE_WITH, self.FOLLOW_TREE_PASTE_WITH_in_block409)

                            self.match(self.input, DOWN, None)
                            self._state.following.append(self.FOLLOW_paste_with_in_block415)
                            pw = self.paste_with()

                            self._state.following.pop()

                            self.match(self.input, UP, None)


                            #action start
                            _paste += [ [ pr , pw ] ] 
                            #action end


                            self.match(self.input, UP, None)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    self.match(self.input, UP, None)


                    #action start
                    value . append ( { 'copy' : _copy , 'paste' : _paste } ) 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "block"



    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterBackend.g:44:1: paste_replace returns [ value ] : ID ;
    def paste_replace(self, ):
        value = None


        ID6 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:46:5: ( ID )
                # grammar/ShyCopypasterBackend.g:46:9: ID
                pass 
                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace492)

                #action start
                value = ID6.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_replace"



    # $ANTLR start "paste_with"
    # grammar/ShyCopypasterBackend.g:49:1: paste_with returns [ value ] : ( arbitrary_token )+ ;
    def paste_with(self, ):
        value = None


        arbitrary_token7 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:52:5: ( ( arbitrary_token )+ )
                # grammar/ShyCopypasterBackend.g:52:9: ( arbitrary_token )+
                pass 
                # grammar/ShyCopypasterBackend.g:52:9: ( arbitrary_token )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == CONSTS or (CURLY_CLOSE <= LA7_0 <= CURLY_OPEN) or (DIVIDE <= LA7_0 <= ID) or (MINUS <= LA7_0 <= MODULE) or LA7_0 == NUMBER or (TYPES <= LA7_0 <= UNDERSCORE)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyCopypasterBackend.g:52:11: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_paste_with533)
                        arbitrary_token7 = self.arbitrary_token()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_token7 ) 
                        #action end



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_with"



    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterBackend.g:57:1: arbitrary_token returns [ value ] : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        value = None


        CONSTS8 = None
        MODULE9 = None
        TYPES10 = None
        CURLY_OPEN11 = None
        CURLY_CLOSE12 = None
        DIVIDE13 = None
        MINUS14 = None
        UNDERSCORE15 = None
        ID16 = None
        NUMBER17 = None
        EXPRESSION18 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:59:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                alt8 = 11
                LA8 = self.input.LA(1)
                if LA8 == CONSTS:
                    alt8 = 1
                elif LA8 == MODULE:
                    alt8 = 2
                elif LA8 == TYPES:
                    alt8 = 3
                elif LA8 == CURLY_OPEN:
                    alt8 = 4
                elif LA8 == CURLY_CLOSE:
                    alt8 = 5
                elif LA8 == DIVIDE:
                    alt8 = 6
                elif LA8 == MINUS:
                    alt8 = 7
                elif LA8 == UNDERSCORE:
                    alt8 = 8
                elif LA8 == ID:
                    alt8 = 9
                elif LA8 == NUMBER:
                    alt8 = 10
                elif LA8 == EXPRESSION:
                    alt8 = 11
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # grammar/ShyCopypasterBackend.g:59:9: CONSTS
                    pass 
                    CONSTS8 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_arbitrary_token586)

                    #action start
                    value = CONSTS8.text 
                    #action end



                elif alt8 == 2:
                    # grammar/ShyCopypasterBackend.g:60:9: MODULE
                    pass 
                    MODULE9 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_arbitrary_token598)

                    #action start
                    value = MODULE9.text 
                    #action end



                elif alt8 == 3:
                    # grammar/ShyCopypasterBackend.g:61:9: TYPES
                    pass 
                    TYPES10 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_arbitrary_token610)

                    #action start
                    value = TYPES10.text 
                    #action end



                elif alt8 == 4:
                    # grammar/ShyCopypasterBackend.g:63:9: CURLY_OPEN
                    pass 
                    CURLY_OPEN11 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_arbitrary_token623)

                    #action start
                    value = CURLY_OPEN11.text 
                    #action end



                elif alt8 == 5:
                    # grammar/ShyCopypasterBackend.g:64:9: CURLY_CLOSE
                    pass 
                    CURLY_CLOSE12 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_arbitrary_token635)

                    #action start
                    value = CURLY_CLOSE12.text 
                    #action end



                elif alt8 == 6:
                    # grammar/ShyCopypasterBackend.g:65:9: DIVIDE
                    pass 
                    DIVIDE13 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_arbitrary_token647)

                    #action start
                    value = DIVIDE13.text 
                    #action end



                elif alt8 == 7:
                    # grammar/ShyCopypasterBackend.g:66:9: MINUS
                    pass 
                    MINUS14 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arbitrary_token659)

                    #action start
                    value = MINUS14.text 
                    #action end



                elif alt8 == 8:
                    # grammar/ShyCopypasterBackend.g:67:9: UNDERSCORE
                    pass 
                    UNDERSCORE15 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_arbitrary_token671)

                    #action start
                    value = UNDERSCORE15.text 
                    #action end



                elif alt8 == 9:
                    # grammar/ShyCopypasterBackend.g:68:9: ID
                    pass 
                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_token683)

                    #action start
                    value = ID16.text 
                    #action end



                elif alt8 == 10:
                    # grammar/ShyCopypasterBackend.g:69:9: NUMBER
                    pass 
                    NUMBER17 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_arbitrary_token695)

                    #action start
                    value = NUMBER17.text 
                    #action end



                elif alt8 == 11:
                    # grammar/ShyCopypasterBackend.g:70:9: EXPRESSION
                    pass 
                    EXPRESSION18 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_token707)

                    #action start
                    value = EXPRESSION18.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_token"



 

    FOLLOW_block_in_start80 = frozenset([1, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 21, 37, 38])
    FOLLOW_arbitrary_token_in_block125 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_block161 = frozenset([1])
    FOLLOW_INDENT_in_block185 = frozenset([15])
    FOLLOW_NEWLINE_in_block191 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 21, 37, 38])
    FOLLOW_block_in_block221 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 21, 37, 38])
    FOLLOW_DEDENT_in_block258 = frozenset([15])
    FOLLOW_NEWLINE_in_block264 = frozenset([1])
    FOLLOW_TREE_COPY_in_block300 = frozenset([2])
    FOLLOW_block_in_block320 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 21, 29, 37, 38])
    FOLLOW_TREE_PASTE_in_block369 = frozenset([2])
    FOLLOW_TREE_PASTE_REPLACE_in_block385 = frozenset([2])
    FOLLOW_paste_replace_in_block391 = frozenset([3])
    FOLLOW_TREE_PASTE_WITH_in_block409 = frozenset([2])
    FOLLOW_paste_with_in_block415 = frozenset([3])
    FOLLOW_ID_in_paste_replace492 = frozenset([1])
    FOLLOW_arbitrary_token_in_paste_with533 = frozenset([1, 4, 6, 7, 9, 10, 11, 13, 14, 16, 37, 38])
    FOLLOW_CONSTS_in_arbitrary_token586 = frozenset([1])
    FOLLOW_MODULE_in_arbitrary_token598 = frozenset([1])
    FOLLOW_TYPES_in_arbitrary_token610 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_arbitrary_token623 = frozenset([1])
    FOLLOW_CURLY_CLOSE_in_arbitrary_token635 = frozenset([1])
    FOLLOW_DIVIDE_in_arbitrary_token647 = frozenset([1])
    FOLLOW_MINUS_in_arbitrary_token659 = frozenset([1])
    FOLLOW_UNDERSCORE_in_arbitrary_token671 = frozenset([1])
    FOLLOW_ID_in_arbitrary_token683 = frozenset([1])
    FOLLOW_NUMBER_in_arbitrary_token695 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_token707 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
