# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-19 20:53:40

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
    # grammar/ShyCopypasterBackend.g:16:1: block returns [ value ] : ( arbitrary_tokens NEWLINE | INDENT nl1= NEWLINE (b1= block )+ DEDENT nl2= NEWLINE | copy );
    def block(self, ):
        value = None


        nl1 = None
        nl2 = None
        NEWLINE3 = None
        INDENT4 = None
        DEDENT5 = None
        b1 = None

        arbitrary_tokens2 = None

        copy6 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:19:5: ( arbitrary_tokens NEWLINE | INDENT nl1= NEWLINE (b1= block )+ DEDENT nl2= NEWLINE | copy )
                alt3 = 3
                LA3 = self.input.LA(1)
                if LA3 == CONSTS or LA3 == CURLY_CLOSE or LA3 == CURLY_OPEN or LA3 == DIVIDE or LA3 == EXPRESSION or LA3 == ID or LA3 == MINUS or LA3 == MODULE or LA3 == NUMBER or LA3 == TYPES or LA3 == UNDERSCORE:
                    alt3 = 1
                elif LA3 == INDENT:
                    alt3 = 2
                elif LA3 == TREE_COPY:
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyCopypasterBackend.g:19:9: arbitrary_tokens NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_arbitrary_tokens_in_block123)
                    arbitrary_tokens2 = self.arbitrary_tokens()

                    self._state.following.pop()

                    #action start
                    value += arbitrary_tokens2 
                    #action end


                    NEWLINE3 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block147)

                    #action start
                    value += [ NEWLINE3.text ] 
                    #action end



                elif alt3 == 2:
                    # grammar/ShyCopypasterBackend.g:23:9: INDENT nl1= NEWLINE (b1= block )+ DEDENT nl2= NEWLINE
                    pass 
                    INDENT4 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_block171)

                    nl1 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block177)

                    #action start
                    value += [ INDENT4.text , nl1.text ] 
                    #action end


                    # grammar/ShyCopypasterBackend.g:25:9: (b1= block )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= MODULE) or LA2_0 == NUMBER or LA2_0 == TREE_COPY or (TYPES <= LA2_0 <= UNDERSCORE)) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyCopypasterBackend.g:25:11: b1= block
                            pass 
                            self._state.following.append(self.FOLLOW_block_in_block207)
                            b1 = self.block()

                            self._state.following.pop()

                            #action start
                            value += b1 
                            #action end



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    DEDENT5 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_block244)

                    nl2 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block250)

                    #action start
                    value += [ DEDENT5.text , nl2.text ] 
                    #action end



                elif alt3 == 3:
                    # grammar/ShyCopypasterBackend.g:30:9: copy
                    pass 
                    self._state.following.append(self.FOLLOW_copy_in_block274)
                    copy6 = self.copy()

                    self._state.following.pop()

                    #action start
                    value += copy6 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "block"



    # $ANTLR start "pure_block"
    # grammar/ShyCopypasterBackend.g:33:1: pure_block returns [ value ] : ( arbitrary_tokens NEWLINE | INDENT nl1= NEWLINE (pb1= pure_block )+ DEDENT nl2= NEWLINE );
    def pure_block(self, ):
        value = None


        nl1 = None
        nl2 = None
        NEWLINE8 = None
        INDENT9 = None
        DEDENT10 = None
        pb1 = None

        arbitrary_tokens7 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:36:5: ( arbitrary_tokens NEWLINE | INDENT nl1= NEWLINE (pb1= pure_block )+ DEDENT nl2= NEWLINE )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == CONSTS or (CURLY_CLOSE <= LA5_0 <= CURLY_OPEN) or (DIVIDE <= LA5_0 <= ID) or (MINUS <= LA5_0 <= MODULE) or LA5_0 == NUMBER or (TYPES <= LA5_0 <= UNDERSCORE)) :
                    alt5 = 1
                elif (LA5_0 == INDENT) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyCopypasterBackend.g:36:9: arbitrary_tokens NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_arbitrary_tokens_in_pure_block313)
                    arbitrary_tokens7 = self.arbitrary_tokens()

                    self._state.following.pop()

                    #action start
                    value += arbitrary_tokens7 
                    #action end


                    NEWLINE8 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block337)

                    #action start
                    value += [ NEWLINE8.text ] 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyCopypasterBackend.g:40:9: INDENT nl1= NEWLINE (pb1= pure_block )+ DEDENT nl2= NEWLINE
                    pass 
                    INDENT9 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_pure_block361)

                    nl1 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block367)

                    #action start
                    value += [ INDENT9.text , nl1.text ] 
                    #action end


                    # grammar/ShyCopypasterBackend.g:42:9: (pb1= pure_block )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == CONSTS or (CURLY_CLOSE <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= MODULE) or LA4_0 == NUMBER or (TYPES <= LA4_0 <= UNDERSCORE)) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammar/ShyCopypasterBackend.g:42:11: pb1= pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_pure_block397)
                            pb1 = self.pure_block()

                            self._state.following.pop()

                            #action start
                            value += pb1 
                            #action end



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    DEDENT10 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_pure_block434)

                    nl2 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block440)

                    #action start
                    value += [ DEDENT10.text , nl2.text ] 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "pure_block"



    # $ANTLR start "copy"
    # grammar/ShyCopypasterBackend.g:49:1: copy returns [ value ] : ^( TREE_COPY copy_body pastes ) ;
    def copy(self, ):
        value = None


        copy_body11 = None

        pastes12 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:51:5: ( ^( TREE_COPY copy_body pastes ) )
                # grammar/ShyCopypasterBackend.g:51:9: ^( TREE_COPY copy_body pastes )
                pass 
                self.match(self.input, TREE_COPY, self.FOLLOW_TREE_COPY_in_copy483)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_copy_body_in_copy485)
                copy_body11 = self.copy_body()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_pastes_in_copy487)
                pastes12 = self.pastes()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = [ { 'copy' : copy_body11 , 'paste' : pastes12 } ] 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "copy"



    # $ANTLR start "copy_body"
    # grammar/ShyCopypasterBackend.g:55:1: copy_body returns [ value ] : ( pure_block )+ ;
    def copy_body(self, ):
        value = None


        pure_block13 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:58:5: ( ( pure_block )+ )
                # grammar/ShyCopypasterBackend.g:58:9: ( pure_block )+
                pass 
                # grammar/ShyCopypasterBackend.g:58:9: ( pure_block )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == CONSTS or (CURLY_CLOSE <= LA6_0 <= CURLY_OPEN) or (DIVIDE <= LA6_0 <= MODULE) or LA6_0 == NUMBER or (TYPES <= LA6_0 <= UNDERSCORE)) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyCopypasterBackend.g:58:11: pure_block
                        pass 
                        self._state.following.append(self.FOLLOW_pure_block_in_copy_body538)
                        pure_block13 = self.pure_block()

                        self._state.following.pop()

                        #action start
                        value += pure_block13 
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

    # $ANTLR end "copy_body"



    # $ANTLR start "pastes"
    # grammar/ShyCopypasterBackend.g:61:1: pastes returns [ value ] : ( paste )+ ;
    def pastes(self, ):
        value = None


        paste14 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:64:5: ( ( paste )+ )
                # grammar/ShyCopypasterBackend.g:64:9: ( paste )+
                pass 
                # grammar/ShyCopypasterBackend.g:64:9: ( paste )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == TREE_PASTE) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyCopypasterBackend.g:64:11: paste
                        pass 
                        self._state.following.append(self.FOLLOW_paste_in_pastes583)
                        paste14 = self.paste()

                        self._state.following.pop()

                        #action start
                        value . append ( paste14 ) 
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

    # $ANTLR end "pastes"



    # $ANTLR start "paste"
    # grammar/ShyCopypasterBackend.g:67:1: paste returns [ value ] : ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        value = None


        paste_replace15 = None

        paste_with16 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:69:5: ( ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterBackend.g:69:9: ^( TREE_PASTE paste_replace paste_with )
                pass 
                self.match(self.input, TREE_PASTE, self.FOLLOW_TREE_PASTE_in_paste618)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_paste_replace_in_paste620)
                paste_replace15 = self.paste_replace()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_paste_with_in_paste622)
                paste_with16 = self.paste_with()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = [ paste_replace15 , paste_with16 ] 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste"



    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterBackend.g:73:1: paste_replace returns [ value ] : ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        value = None


        ID17 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:75:5: ( ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterBackend.g:75:9: ^( TREE_PASTE_REPLACE ID )
                pass 
                self.match(self.input, TREE_PASTE_REPLACE, self.FOLLOW_TREE_PASTE_REPLACE_in_paste_replace663)

                self.match(self.input, DOWN, None)
                ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace665)

                self.match(self.input, UP, None)


                #action start
                value = ID17.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_replace"



    # $ANTLR start "paste_with"
    # grammar/ShyCopypasterBackend.g:78:1: paste_with returns [ value ] : ^( TREE_PASTE_WITH arbitrary_tokens ) ;
    def paste_with(self, ):
        value = None


        arbitrary_tokens18 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:80:5: ( ^( TREE_PASTE_WITH arbitrary_tokens ) )
                # grammar/ShyCopypasterBackend.g:80:9: ^( TREE_PASTE_WITH arbitrary_tokens )
                pass 
                self.match(self.input, TREE_PASTE_WITH, self.FOLLOW_TREE_PASTE_WITH_in_paste_with698)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_tokens_in_paste_with700)
                arbitrary_tokens18 = self.arbitrary_tokens()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = arbitrary_tokens18 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_with"



    # $ANTLR start "arbitrary_tokens"
    # grammar/ShyCopypasterBackend.g:84:1: arbitrary_tokens returns [ value ] : ( arbitrary_token )+ ;
    def arbitrary_tokens(self, ):
        value = None


        arbitrary_token19 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:87:5: ( ( arbitrary_token )+ )
                # grammar/ShyCopypasterBackend.g:87:9: ( arbitrary_token )+
                pass 
                # grammar/ShyCopypasterBackend.g:87:9: ( arbitrary_token )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == CONSTS or (CURLY_CLOSE <= LA8_0 <= CURLY_OPEN) or (DIVIDE <= LA8_0 <= ID) or (MINUS <= LA8_0 <= MODULE) or LA8_0 == NUMBER or (TYPES <= LA8_0 <= UNDERSCORE)) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyCopypasterBackend.g:87:11: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_arbitrary_tokens751)
                        arbitrary_token19 = self.arbitrary_token()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_token19 ) 
                        #action end



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_tokens"



    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterBackend.g:92:1: arbitrary_token returns [ value ] : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        value = None


        CONSTS20 = None
        MODULE21 = None
        TYPES22 = None
        CURLY_OPEN23 = None
        CURLY_CLOSE24 = None
        DIVIDE25 = None
        MINUS26 = None
        UNDERSCORE27 = None
        ID28 = None
        NUMBER29 = None
        EXPRESSION30 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:94:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                alt9 = 11
                LA9 = self.input.LA(1)
                if LA9 == CONSTS:
                    alt9 = 1
                elif LA9 == MODULE:
                    alt9 = 2
                elif LA9 == TYPES:
                    alt9 = 3
                elif LA9 == CURLY_OPEN:
                    alt9 = 4
                elif LA9 == CURLY_CLOSE:
                    alt9 = 5
                elif LA9 == DIVIDE:
                    alt9 = 6
                elif LA9 == MINUS:
                    alt9 = 7
                elif LA9 == UNDERSCORE:
                    alt9 = 8
                elif LA9 == ID:
                    alt9 = 9
                elif LA9 == NUMBER:
                    alt9 = 10
                elif LA9 == EXPRESSION:
                    alt9 = 11
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammar/ShyCopypasterBackend.g:94:9: CONSTS
                    pass 
                    CONSTS20 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_arbitrary_token804)

                    #action start
                    value = CONSTS20.text 
                    #action end



                elif alt9 == 2:
                    # grammar/ShyCopypasterBackend.g:95:9: MODULE
                    pass 
                    MODULE21 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_arbitrary_token816)

                    #action start
                    value = MODULE21.text 
                    #action end



                elif alt9 == 3:
                    # grammar/ShyCopypasterBackend.g:96:9: TYPES
                    pass 
                    TYPES22 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_arbitrary_token828)

                    #action start
                    value = TYPES22.text 
                    #action end



                elif alt9 == 4:
                    # grammar/ShyCopypasterBackend.g:98:9: CURLY_OPEN
                    pass 
                    CURLY_OPEN23 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_arbitrary_token841)

                    #action start
                    value = CURLY_OPEN23.text 
                    #action end



                elif alt9 == 5:
                    # grammar/ShyCopypasterBackend.g:99:9: CURLY_CLOSE
                    pass 
                    CURLY_CLOSE24 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_arbitrary_token853)

                    #action start
                    value = CURLY_CLOSE24.text 
                    #action end



                elif alt9 == 6:
                    # grammar/ShyCopypasterBackend.g:100:9: DIVIDE
                    pass 
                    DIVIDE25 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_arbitrary_token865)

                    #action start
                    value = DIVIDE25.text 
                    #action end



                elif alt9 == 7:
                    # grammar/ShyCopypasterBackend.g:101:9: MINUS
                    pass 
                    MINUS26 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arbitrary_token877)

                    #action start
                    value = MINUS26.text 
                    #action end



                elif alt9 == 8:
                    # grammar/ShyCopypasterBackend.g:102:9: UNDERSCORE
                    pass 
                    UNDERSCORE27 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_arbitrary_token889)

                    #action start
                    value = UNDERSCORE27.text 
                    #action end



                elif alt9 == 9:
                    # grammar/ShyCopypasterBackend.g:103:9: ID
                    pass 
                    ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_token901)

                    #action start
                    value = ID28.text 
                    #action end



                elif alt9 == 10:
                    # grammar/ShyCopypasterBackend.g:104:9: NUMBER
                    pass 
                    NUMBER29 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_arbitrary_token913)

                    #action start
                    value = NUMBER29.text 
                    #action end



                elif alt9 == 11:
                    # grammar/ShyCopypasterBackend.g:105:9: EXPRESSION
                    pass 
                    EXPRESSION30 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_token925)

                    #action start
                    value = EXPRESSION30.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_token"



 

    FOLLOW_block_in_start80 = frozenset([1, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 21, 37, 38])
    FOLLOW_arbitrary_tokens_in_block123 = frozenset([15])
    FOLLOW_NEWLINE_in_block147 = frozenset([1])
    FOLLOW_INDENT_in_block171 = frozenset([15])
    FOLLOW_NEWLINE_in_block177 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 21, 37, 38])
    FOLLOW_block_in_block207 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 21, 37, 38])
    FOLLOW_DEDENT_in_block244 = frozenset([15])
    FOLLOW_NEWLINE_in_block250 = frozenset([1])
    FOLLOW_copy_in_block274 = frozenset([1])
    FOLLOW_arbitrary_tokens_in_pure_block313 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block337 = frozenset([1])
    FOLLOW_INDENT_in_pure_block361 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block367 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_pure_block397 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_pure_block434 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block440 = frozenset([1])
    FOLLOW_TREE_COPY_in_copy483 = frozenset([2])
    FOLLOW_copy_body_in_copy485 = frozenset([29])
    FOLLOW_pastes_in_copy487 = frozenset([3])
    FOLLOW_pure_block_in_copy_body538 = frozenset([1, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_paste_in_pastes583 = frozenset([1, 29])
    FOLLOW_TREE_PASTE_in_paste618 = frozenset([2])
    FOLLOW_paste_replace_in_paste620 = frozenset([31])
    FOLLOW_paste_with_in_paste622 = frozenset([3])
    FOLLOW_TREE_PASTE_REPLACE_in_paste_replace663 = frozenset([2])
    FOLLOW_ID_in_paste_replace665 = frozenset([3])
    FOLLOW_TREE_PASTE_WITH_in_paste_with698 = frozenset([2])
    FOLLOW_arbitrary_tokens_in_paste_with700 = frozenset([3])
    FOLLOW_arbitrary_token_in_arbitrary_tokens751 = frozenset([1, 4, 6, 7, 9, 10, 11, 13, 14, 16, 37, 38])
    FOLLOW_CONSTS_in_arbitrary_token804 = frozenset([1])
    FOLLOW_MODULE_in_arbitrary_token816 = frozenset([1])
    FOLLOW_TYPES_in_arbitrary_token828 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_arbitrary_token841 = frozenset([1])
    FOLLOW_CURLY_CLOSE_in_arbitrary_token853 = frozenset([1])
    FOLLOW_DIVIDE_in_arbitrary_token865 = frozenset([1])
    FOLLOW_MINUS_in_arbitrary_token877 = frozenset([1])
    FOLLOW_UNDERSCORE_in_arbitrary_token889 = frozenset([1])
    FOLLOW_ID_in_arbitrary_token901 = frozenset([1])
    FOLLOW_NUMBER_in_arbitrary_token913 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_token925 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
