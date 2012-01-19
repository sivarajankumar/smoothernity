# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-19 20:13:33

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
    # grammar/ShyCopypasterBackend.g:16:1: block returns [ value ] : ( pure_block | copy );
    def block(self, ):
        value = None


        pure_block2 = None

        copy3 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:18:5: ( pure_block | copy )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= MODULE) or LA2_0 == NUMBER or (TYPES <= LA2_0 <= UNDERSCORE)) :
                    alt2 = 1
                elif (LA2_0 == TREE_COPY) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # grammar/ShyCopypasterBackend.g:18:9: pure_block
                    pass 
                    self._state.following.append(self.FOLLOW_pure_block_in_block113)
                    pure_block2 = self.pure_block()

                    self._state.following.pop()

                    #action start
                    value = pure_block2 
                    #action end



                elif alt2 == 2:
                    # grammar/ShyCopypasterBackend.g:19:9: copy
                    pass 
                    self._state.following.append(self.FOLLOW_copy_in_block125)
                    copy3 = self.copy()

                    self._state.following.pop()

                    #action start
                    value = copy3 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "block"



    # $ANTLR start "pure_block"
    # grammar/ShyCopypasterBackend.g:22:1: pure_block returns [ value ] : ( arbitrary_tokens NEWLINE | INDENT nl1= NEWLINE (pb1= pure_block )+ DEDENT nl2= NEWLINE );
    def pure_block(self, ):
        value = None


        nl1 = None
        nl2 = None
        NEWLINE5 = None
        INDENT6 = None
        DEDENT7 = None
        pb1 = None

        arbitrary_tokens4 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:25:5: ( arbitrary_tokens NEWLINE | INDENT nl1= NEWLINE (pb1= pure_block )+ DEDENT nl2= NEWLINE )
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
                    # grammar/ShyCopypasterBackend.g:25:9: arbitrary_tokens NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_arbitrary_tokens_in_pure_block164)
                    arbitrary_tokens4 = self.arbitrary_tokens()

                    self._state.following.pop()

                    #action start
                    value += arbitrary_tokens4 
                    #action end


                    NEWLINE5 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block188)

                    #action start
                    value += [ NEWLINE5.text ] 
                    #action end



                elif alt4 == 2:
                    # grammar/ShyCopypasterBackend.g:29:9: INDENT nl1= NEWLINE (pb1= pure_block )+ DEDENT nl2= NEWLINE
                    pass 
                    INDENT6 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_pure_block212)

                    nl1 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block218)

                    #action start
                    value += [ INDENT6.text , nl1.text ] 
                    #action end


                    # grammar/ShyCopypasterBackend.g:31:9: (pb1= pure_block )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == CONSTS or (CURLY_CLOSE <= LA3_0 <= CURLY_OPEN) or (DIVIDE <= LA3_0 <= MODULE) or LA3_0 == NUMBER or (TYPES <= LA3_0 <= UNDERSCORE)) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammar/ShyCopypasterBackend.g:31:11: pb1= pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_pure_block248)
                            pb1 = self.pure_block()

                            self._state.following.pop()

                            #action start
                            value += pb1 
                            #action end



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    DEDENT7 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_pure_block285)

                    nl2 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block291)

                    #action start
                    value += [ DEDENT7.text , nl2.text ] 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "pure_block"



    # $ANTLR start "copy"
    # grammar/ShyCopypasterBackend.g:38:1: copy returns [ value ] : ^( TREE_COPY copy_body pastes ) ;
    def copy(self, ):
        value = None


        copy_body8 = None

        pastes9 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:40:5: ( ^( TREE_COPY copy_body pastes ) )
                # grammar/ShyCopypasterBackend.g:40:9: ^( TREE_COPY copy_body pastes )
                pass 
                self.match(self.input, TREE_COPY, self.FOLLOW_TREE_COPY_in_copy334)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_copy_body_in_copy336)
                copy_body8 = self.copy_body()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_pastes_in_copy338)
                pastes9 = self.pastes()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = [ { 'copy' : copy_body8 , 'paste' : pastes9 } ] 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "copy"



    # $ANTLR start "copy_body"
    # grammar/ShyCopypasterBackend.g:44:1: copy_body returns [ value ] : ( pure_block )+ ;
    def copy_body(self, ):
        value = None


        pure_block10 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:47:5: ( ( pure_block )+ )
                # grammar/ShyCopypasterBackend.g:47:9: ( pure_block )+
                pass 
                # grammar/ShyCopypasterBackend.g:47:9: ( pure_block )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == CONSTS or (CURLY_CLOSE <= LA5_0 <= CURLY_OPEN) or (DIVIDE <= LA5_0 <= MODULE) or LA5_0 == NUMBER or (TYPES <= LA5_0 <= UNDERSCORE)) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/ShyCopypasterBackend.g:47:11: pure_block
                        pass 
                        self._state.following.append(self.FOLLOW_pure_block_in_copy_body389)
                        pure_block10 = self.pure_block()

                        self._state.following.pop()

                        #action start
                        value += pure_block10 
                        #action end



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "copy_body"



    # $ANTLR start "pastes"
    # grammar/ShyCopypasterBackend.g:50:1: pastes returns [ value ] : ( paste )+ ;
    def pastes(self, ):
        value = None


        paste11 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:53:5: ( ( paste )+ )
                # grammar/ShyCopypasterBackend.g:53:9: ( paste )+
                pass 
                # grammar/ShyCopypasterBackend.g:53:9: ( paste )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TREE_PASTE) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyCopypasterBackend.g:53:11: paste
                        pass 
                        self._state.following.append(self.FOLLOW_paste_in_pastes434)
                        paste11 = self.paste()

                        self._state.following.pop()

                        #action start
                        value . append ( paste11 ) 
                        #action end



                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "pastes"



    # $ANTLR start "paste"
    # grammar/ShyCopypasterBackend.g:56:1: paste returns [ value ] : ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        value = None


        paste_replace12 = None

        paste_with13 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:58:5: ( ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterBackend.g:58:9: ^( TREE_PASTE paste_replace paste_with )
                pass 
                self.match(self.input, TREE_PASTE, self.FOLLOW_TREE_PASTE_in_paste469)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_paste_replace_in_paste471)
                paste_replace12 = self.paste_replace()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_paste_with_in_paste473)
                paste_with13 = self.paste_with()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = [ paste_replace12 , paste_with13 ] 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste"



    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterBackend.g:62:1: paste_replace returns [ value ] : ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        value = None


        ID14 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:64:5: ( ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterBackend.g:64:9: ^( TREE_PASTE_REPLACE ID )
                pass 
                self.match(self.input, TREE_PASTE_REPLACE, self.FOLLOW_TREE_PASTE_REPLACE_in_paste_replace514)

                self.match(self.input, DOWN, None)
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace516)

                self.match(self.input, UP, None)


                #action start
                value = ID14.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_replace"



    # $ANTLR start "paste_with"
    # grammar/ShyCopypasterBackend.g:67:1: paste_with returns [ value ] : ^( TREE_PASTE_WITH arbitrary_tokens ) ;
    def paste_with(self, ):
        value = None


        arbitrary_tokens15 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:69:5: ( ^( TREE_PASTE_WITH arbitrary_tokens ) )
                # grammar/ShyCopypasterBackend.g:69:9: ^( TREE_PASTE_WITH arbitrary_tokens )
                pass 
                self.match(self.input, TREE_PASTE_WITH, self.FOLLOW_TREE_PASTE_WITH_in_paste_with549)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_tokens_in_paste_with551)
                arbitrary_tokens15 = self.arbitrary_tokens()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = arbitrary_tokens15 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_with"



    # $ANTLR start "arbitrary_tokens"
    # grammar/ShyCopypasterBackend.g:73:1: arbitrary_tokens returns [ value ] : ( arbitrary_token )+ ;
    def arbitrary_tokens(self, ):
        value = None


        arbitrary_token16 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:76:5: ( ( arbitrary_token )+ )
                # grammar/ShyCopypasterBackend.g:76:9: ( arbitrary_token )+
                pass 
                # grammar/ShyCopypasterBackend.g:76:9: ( arbitrary_token )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == CONSTS or (CURLY_CLOSE <= LA7_0 <= CURLY_OPEN) or (DIVIDE <= LA7_0 <= ID) or (MINUS <= LA7_0 <= MODULE) or LA7_0 == NUMBER or (TYPES <= LA7_0 <= UNDERSCORE)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyCopypasterBackend.g:76:11: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_arbitrary_tokens602)
                        arbitrary_token16 = self.arbitrary_token()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_token16 ) 
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

    # $ANTLR end "arbitrary_tokens"



    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterBackend.g:81:1: arbitrary_token returns [ value ] : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        value = None


        CONSTS17 = None
        MODULE18 = None
        TYPES19 = None
        CURLY_OPEN20 = None
        CURLY_CLOSE21 = None
        DIVIDE22 = None
        MINUS23 = None
        UNDERSCORE24 = None
        ID25 = None
        NUMBER26 = None
        EXPRESSION27 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:83:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
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
                    # grammar/ShyCopypasterBackend.g:83:9: CONSTS
                    pass 
                    CONSTS17 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_arbitrary_token655)

                    #action start
                    value = CONSTS17.text 
                    #action end



                elif alt8 == 2:
                    # grammar/ShyCopypasterBackend.g:84:9: MODULE
                    pass 
                    MODULE18 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_arbitrary_token667)

                    #action start
                    value = MODULE18.text 
                    #action end



                elif alt8 == 3:
                    # grammar/ShyCopypasterBackend.g:85:9: TYPES
                    pass 
                    TYPES19 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_arbitrary_token679)

                    #action start
                    value = TYPES19.text 
                    #action end



                elif alt8 == 4:
                    # grammar/ShyCopypasterBackend.g:87:9: CURLY_OPEN
                    pass 
                    CURLY_OPEN20 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_arbitrary_token692)

                    #action start
                    value = CURLY_OPEN20.text 
                    #action end



                elif alt8 == 5:
                    # grammar/ShyCopypasterBackend.g:88:9: CURLY_CLOSE
                    pass 
                    CURLY_CLOSE21 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_arbitrary_token704)

                    #action start
                    value = CURLY_CLOSE21.text 
                    #action end



                elif alt8 == 6:
                    # grammar/ShyCopypasterBackend.g:89:9: DIVIDE
                    pass 
                    DIVIDE22 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_arbitrary_token716)

                    #action start
                    value = DIVIDE22.text 
                    #action end



                elif alt8 == 7:
                    # grammar/ShyCopypasterBackend.g:90:9: MINUS
                    pass 
                    MINUS23 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arbitrary_token728)

                    #action start
                    value = MINUS23.text 
                    #action end



                elif alt8 == 8:
                    # grammar/ShyCopypasterBackend.g:91:9: UNDERSCORE
                    pass 
                    UNDERSCORE24 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_arbitrary_token740)

                    #action start
                    value = UNDERSCORE24.text 
                    #action end



                elif alt8 == 9:
                    # grammar/ShyCopypasterBackend.g:92:9: ID
                    pass 
                    ID25 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_token752)

                    #action start
                    value = ID25.text 
                    #action end



                elif alt8 == 10:
                    # grammar/ShyCopypasterBackend.g:93:9: NUMBER
                    pass 
                    NUMBER26 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_arbitrary_token764)

                    #action start
                    value = NUMBER26.text 
                    #action end



                elif alt8 == 11:
                    # grammar/ShyCopypasterBackend.g:94:9: EXPRESSION
                    pass 
                    EXPRESSION27 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_token776)

                    #action start
                    value = EXPRESSION27.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_token"



 

    FOLLOW_block_in_start80 = frozenset([1, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 21, 37, 38])
    FOLLOW_pure_block_in_block113 = frozenset([1])
    FOLLOW_copy_in_block125 = frozenset([1])
    FOLLOW_arbitrary_tokens_in_pure_block164 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block188 = frozenset([1])
    FOLLOW_INDENT_in_pure_block212 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block218 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_pure_block248 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_pure_block285 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block291 = frozenset([1])
    FOLLOW_TREE_COPY_in_copy334 = frozenset([2])
    FOLLOW_copy_body_in_copy336 = frozenset([29])
    FOLLOW_pastes_in_copy338 = frozenset([3])
    FOLLOW_pure_block_in_copy_body389 = frozenset([1, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_paste_in_pastes434 = frozenset([1, 29])
    FOLLOW_TREE_PASTE_in_paste469 = frozenset([2])
    FOLLOW_paste_replace_in_paste471 = frozenset([31])
    FOLLOW_paste_with_in_paste473 = frozenset([3])
    FOLLOW_TREE_PASTE_REPLACE_in_paste_replace514 = frozenset([2])
    FOLLOW_ID_in_paste_replace516 = frozenset([3])
    FOLLOW_TREE_PASTE_WITH_in_paste_with549 = frozenset([2])
    FOLLOW_arbitrary_tokens_in_paste_with551 = frozenset([3])
    FOLLOW_arbitrary_token_in_arbitrary_tokens602 = frozenset([1, 4, 6, 7, 9, 10, 11, 13, 14, 16, 37, 38])
    FOLLOW_CONSTS_in_arbitrary_token655 = frozenset([1])
    FOLLOW_MODULE_in_arbitrary_token667 = frozenset([1])
    FOLLOW_TYPES_in_arbitrary_token679 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_arbitrary_token692 = frozenset([1])
    FOLLOW_CURLY_CLOSE_in_arbitrary_token704 = frozenset([1])
    FOLLOW_DIVIDE_in_arbitrary_token716 = frozenset([1])
    FOLLOW_MINUS_in_arbitrary_token728 = frozenset([1])
    FOLLOW_UNDERSCORE_in_arbitrary_token740 = frozenset([1])
    FOLLOW_ID_in_arbitrary_token752 = frozenset([1])
    FOLLOW_NUMBER_in_arbitrary_token764 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_token776 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
