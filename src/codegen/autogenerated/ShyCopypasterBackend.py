# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-18 19:00:31

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
    # grammar/ShyCopypasterBackend.g:10:1: start returns [ value ] : ( chunk )* ;
    def start(self, ):
        value = None


        chunk1 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:13:5: ( ( chunk )* )
                # grammar/ShyCopypasterBackend.g:13:7: ( chunk )*
                pass 
                # grammar/ShyCopypasterBackend.g:13:7: ( chunk )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == TREE_ARBITRARY_TOKEN or LA1_0 == TREE_COPY_PASTE) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammar/ShyCopypasterBackend.g:13:9: chunk
                        pass 
                        self._state.following.append(self.FOLLOW_chunk_in_start78)
                        chunk1 = self.chunk()

                        self._state.following.pop()

                        #action start
                        value . append ( chunk1 ) 
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



    # $ANTLR start "chunk"
    # grammar/ShyCopypasterBackend.g:16:1: chunk returns [ value ] : ( ^( TREE_ARBITRARY_TOKEN arbitrary_token ) | copy_paste );
    def chunk(self, ):
        value = None


        arbitrary_token2 = None

        copy_paste3 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:18:5: ( ^( TREE_ARBITRARY_TOKEN arbitrary_token ) | copy_paste )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == TREE_ARBITRARY_TOKEN) :
                    alt2 = 1
                elif (LA2_0 == TREE_COPY_PASTE) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # grammar/ShyCopypasterBackend.g:18:7: ^( TREE_ARBITRARY_TOKEN arbitrary_token )
                    pass 
                    self.match(self.input, TREE_ARBITRARY_TOKEN, self.FOLLOW_TREE_ARBITRARY_TOKEN_in_chunk111)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_arbitrary_token_in_chunk113)
                    arbitrary_token2 = self.arbitrary_token()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = [ arbitrary_token2 ] 
                    #action end



                elif alt2 == 2:
                    # grammar/ShyCopypasterBackend.g:19:7: copy_paste
                    pass 
                    self._state.following.append(self.FOLLOW_copy_paste_in_chunk125)
                    copy_paste3 = self.copy_paste()

                    self._state.following.pop()

                    #action start
                    value = copy_paste3 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "chunk"



    # $ANTLR start "copy_paste"
    # grammar/ShyCopypasterBackend.g:22:1: copy_paste returns [ value ] : ^( TREE_COPY_PASTE copy pastes ) ;
    def copy_paste(self, ):
        value = None


        copy4 = None

        pastes5 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:24:5: ( ^( TREE_COPY_PASTE copy pastes ) )
                # grammar/ShyCopypasterBackend.g:24:7: ^( TREE_COPY_PASTE copy pastes )
                pass 
                self.match(self.input, TREE_COPY_PASTE, self.FOLLOW_TREE_COPY_PASTE_in_copy_paste154)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_copy_in_copy_paste156)
                copy4 = self.copy()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_pastes_in_copy_paste158)
                pastes5 = self.pastes()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'copy' : copy4 , 'paste' : pastes5 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "copy_paste"



    # $ANTLR start "copy"
    # grammar/ShyCopypasterBackend.g:28:1: copy returns [ value ] : ^( TREE_COPY arbitrary_tokens ) ;
    def copy(self, ):
        value = None


        arbitrary_tokens6 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:30:5: ( ^( TREE_COPY arbitrary_tokens ) )
                # grammar/ShyCopypasterBackend.g:30:7: ^( TREE_COPY arbitrary_tokens )
                pass 
                self.match(self.input, TREE_COPY, self.FOLLOW_TREE_COPY_in_copy197)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_tokens_in_copy199)
                arbitrary_tokens6 = self.arbitrary_tokens()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = arbitrary_tokens6 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "copy"



    # $ANTLR start "pastes"
    # grammar/ShyCopypasterBackend.g:33:1: pastes returns [ value ] : ( paste )+ ;
    def pastes(self, ):
        value = None


        paste7 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:36:5: ( ( paste )+ )
                # grammar/ShyCopypasterBackend.g:36:7: ( paste )+
                pass 
                # grammar/ShyCopypasterBackend.g:36:7: ( paste )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == TREE_PASTE) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyCopypasterBackend.g:36:9: paste
                        pass 
                        self._state.following.append(self.FOLLOW_paste_in_pastes240)
                        paste7 = self.paste()

                        self._state.following.pop()

                        #action start
                        value . append ( paste7 ) 
                        #action end



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "pastes"



    # $ANTLR start "paste"
    # grammar/ShyCopypasterBackend.g:39:1: paste returns [ value ] : ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        value = None


        paste_replace8 = None

        paste_with9 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:41:5: ( ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterBackend.g:41:7: ^( TREE_PASTE paste_replace paste_with )
                pass 
                self.match(self.input, TREE_PASTE, self.FOLLOW_TREE_PASTE_in_paste273)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_paste_replace_in_paste275)
                paste_replace8 = self.paste_replace()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_paste_with_in_paste277)
                paste_with9 = self.paste_with()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { 'replace' : paste_replace8 , 'with' : paste_with9 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste"



    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterBackend.g:45:1: paste_replace returns [ value ] : ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        value = None


        ID10 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:47:5: ( ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterBackend.g:47:7: ^( TREE_PASTE_REPLACE ID )
                pass 
                self.match(self.input, TREE_PASTE_REPLACE, self.FOLLOW_TREE_PASTE_REPLACE_in_paste_replace316)

                self.match(self.input, DOWN, None)
                ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace318)

                self.match(self.input, UP, None)


                #action start
                value = ID10.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_replace"



    # $ANTLR start "paste_with"
    # grammar/ShyCopypasterBackend.g:50:1: paste_with returns [ value ] : ^( TREE_PASTE_WITH arbitrary_tokens ) ;
    def paste_with(self, ):
        value = None


        arbitrary_tokens11 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:52:5: ( ^( TREE_PASTE_WITH arbitrary_tokens ) )
                # grammar/ShyCopypasterBackend.g:52:7: ^( TREE_PASTE_WITH arbitrary_tokens )
                pass 
                self.match(self.input, TREE_PASTE_WITH, self.FOLLOW_TREE_PASTE_WITH_in_paste_with349)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_arbitrary_tokens_in_paste_with351)
                arbitrary_tokens11 = self.arbitrary_tokens()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = arbitrary_tokens11 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_with"



    # $ANTLR start "arbitrary_tokens"
    # grammar/ShyCopypasterBackend.g:55:1: arbitrary_tokens returns [ value ] : ( arbitrary_token )+ ;
    def arbitrary_tokens(self, ):
        value = None


        arbitrary_token12 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:58:5: ( ( arbitrary_token )+ )
                # grammar/ShyCopypasterBackend.g:58:7: ( arbitrary_token )+
                pass 
                # grammar/ShyCopypasterBackend.g:58:7: ( arbitrary_token )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == CONSTS or (CURLY_CLOSE <= LA4_0 <= NUMBER) or (TYPES <= LA4_0 <= UNDERSCORE)) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyCopypasterBackend.g:58:9: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_arbitrary_tokens392)
                        arbitrary_token12 = self.arbitrary_token()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_token12 ) 
                        #action end



                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_tokens"



    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterBackend.g:61:1: arbitrary_token returns [ value ] : ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        value = None


        CONSTS13 = None
        DEDENT14 = None
        INDENT15 = None
        MODULE16 = None
        TYPES17 = None
        CURLY_OPEN18 = None
        CURLY_CLOSE19 = None
        DIVIDE20 = None
        MINUS21 = None
        UNDERSCORE22 = None
        NEWLINE23 = None
        ID24 = None
        NUMBER25 = None
        EXPRESSION26 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:63:5: ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION )
                alt5 = 14
                LA5 = self.input.LA(1)
                if LA5 == CONSTS:
                    alt5 = 1
                elif LA5 == DEDENT:
                    alt5 = 2
                elif LA5 == INDENT:
                    alt5 = 3
                elif LA5 == MODULE:
                    alt5 = 4
                elif LA5 == TYPES:
                    alt5 = 5
                elif LA5 == CURLY_OPEN:
                    alt5 = 6
                elif LA5 == CURLY_CLOSE:
                    alt5 = 7
                elif LA5 == DIVIDE:
                    alt5 = 8
                elif LA5 == MINUS:
                    alt5 = 9
                elif LA5 == UNDERSCORE:
                    alt5 = 10
                elif LA5 == NEWLINE:
                    alt5 = 11
                elif LA5 == ID:
                    alt5 = 12
                elif LA5 == NUMBER:
                    alt5 = 13
                elif LA5 == EXPRESSION:
                    alt5 = 14
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyCopypasterBackend.g:63:7: CONSTS
                    pass 
                    CONSTS13 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_arbitrary_token423)

                    #action start
                    value = CONSTS13.text 
                    #action end



                elif alt5 == 2:
                    # grammar/ShyCopypasterBackend.g:64:7: DEDENT
                    pass 
                    DEDENT14 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_arbitrary_token433)

                    #action start
                    value = DEDENT14.text 
                    #action end



                elif alt5 == 3:
                    # grammar/ShyCopypasterBackend.g:65:7: INDENT
                    pass 
                    INDENT15 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_arbitrary_token443)

                    #action start
                    value = INDENT15.text 
                    #action end



                elif alt5 == 4:
                    # grammar/ShyCopypasterBackend.g:66:7: MODULE
                    pass 
                    MODULE16 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_arbitrary_token453)

                    #action start
                    value = MODULE16.text 
                    #action end



                elif alt5 == 5:
                    # grammar/ShyCopypasterBackend.g:67:7: TYPES
                    pass 
                    TYPES17 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_arbitrary_token463)

                    #action start
                    value = TYPES17.text 
                    #action end



                elif alt5 == 6:
                    # grammar/ShyCopypasterBackend.g:69:7: CURLY_OPEN
                    pass 
                    CURLY_OPEN18 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_arbitrary_token474)

                    #action start
                    value = CURLY_OPEN18.text 
                    #action end



                elif alt5 == 7:
                    # grammar/ShyCopypasterBackend.g:70:7: CURLY_CLOSE
                    pass 
                    CURLY_CLOSE19 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_arbitrary_token484)

                    #action start
                    value = CURLY_CLOSE19.text 
                    #action end



                elif alt5 == 8:
                    # grammar/ShyCopypasterBackend.g:71:7: DIVIDE
                    pass 
                    DIVIDE20 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_arbitrary_token494)

                    #action start
                    value = DIVIDE20.text 
                    #action end



                elif alt5 == 9:
                    # grammar/ShyCopypasterBackend.g:72:7: MINUS
                    pass 
                    MINUS21 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arbitrary_token504)

                    #action start
                    value = MINUS21.text 
                    #action end



                elif alt5 == 10:
                    # grammar/ShyCopypasterBackend.g:73:7: UNDERSCORE
                    pass 
                    UNDERSCORE22 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_arbitrary_token514)

                    #action start
                    value = UNDERSCORE22.text 
                    #action end



                elif alt5 == 11:
                    # grammar/ShyCopypasterBackend.g:74:7: NEWLINE
                    pass 
                    NEWLINE23 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_arbitrary_token524)

                    #action start
                    value = NEWLINE23.text 
                    #action end



                elif alt5 == 12:
                    # grammar/ShyCopypasterBackend.g:75:7: ID
                    pass 
                    ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_token534)

                    #action start
                    value = ID24.text 
                    #action end



                elif alt5 == 13:
                    # grammar/ShyCopypasterBackend.g:76:7: NUMBER
                    pass 
                    NUMBER25 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_arbitrary_token544)

                    #action start
                    value = NUMBER25.text 
                    #action end



                elif alt5 == 14:
                    # grammar/ShyCopypasterBackend.g:77:7: EXPRESSION
                    pass 
                    EXPRESSION26 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_token554)

                    #action start
                    value = EXPRESSION26.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_token"



 

    FOLLOW_chunk_in_start78 = frozenset([1, 19, 22])
    FOLLOW_TREE_ARBITRARY_TOKEN_in_chunk111 = frozenset([2])
    FOLLOW_arbitrary_token_in_chunk113 = frozenset([3])
    FOLLOW_copy_paste_in_chunk125 = frozenset([1])
    FOLLOW_TREE_COPY_PASTE_in_copy_paste154 = frozenset([2])
    FOLLOW_copy_in_copy_paste156 = frozenset([29])
    FOLLOW_pastes_in_copy_paste158 = frozenset([3])
    FOLLOW_TREE_COPY_in_copy197 = frozenset([2])
    FOLLOW_arbitrary_tokens_in_copy199 = frozenset([3])
    FOLLOW_paste_in_pastes240 = frozenset([1, 29])
    FOLLOW_TREE_PASTE_in_paste273 = frozenset([2])
    FOLLOW_paste_replace_in_paste275 = frozenset([31])
    FOLLOW_paste_with_in_paste277 = frozenset([3])
    FOLLOW_TREE_PASTE_REPLACE_in_paste_replace316 = frozenset([2])
    FOLLOW_ID_in_paste_replace318 = frozenset([3])
    FOLLOW_TREE_PASTE_WITH_in_paste_with349 = frozenset([2])
    FOLLOW_arbitrary_tokens_in_paste_with351 = frozenset([3])
    FOLLOW_arbitrary_token_in_arbitrary_tokens392 = frozenset([1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 37, 38])
    FOLLOW_CONSTS_in_arbitrary_token423 = frozenset([1])
    FOLLOW_DEDENT_in_arbitrary_token433 = frozenset([1])
    FOLLOW_INDENT_in_arbitrary_token443 = frozenset([1])
    FOLLOW_MODULE_in_arbitrary_token453 = frozenset([1])
    FOLLOW_TYPES_in_arbitrary_token463 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_arbitrary_token474 = frozenset([1])
    FOLLOW_CURLY_CLOSE_in_arbitrary_token484 = frozenset([1])
    FOLLOW_DIVIDE_in_arbitrary_token494 = frozenset([1])
    FOLLOW_MINUS_in_arbitrary_token504 = frozenset([1])
    FOLLOW_UNDERSCORE_in_arbitrary_token514 = frozenset([1])
    FOLLOW_NEWLINE_in_arbitrary_token524 = frozenset([1])
    FOLLOW_ID_in_arbitrary_token534 = frozenset([1])
    FOLLOW_NUMBER_in_arbitrary_token544 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_token554 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
