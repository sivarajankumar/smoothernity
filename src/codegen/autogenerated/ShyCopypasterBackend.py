# $ANTLR 3.4 grammar/ShyCopypasterBackend.g 2012-01-26 18:24:48

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ALL=4
ANY=5
ARGS=6
ARROW_LEFT=7
ARROW_RIGHT=8
CONSTS=9
COPY=10
CURLY_CLOSE=11
CURLY_OPEN=12
DEDENT=13
DIVIDE=14
DO=15
ELIF=16
ELSE=17
EXPRESSION=18
ID=19
IF=20
INDENT=21
MINUS=22
MODULE=23
NEWLINE=24
NUMBER=25
OPS=26
PASTE=27
PROC=28
REPLACE=29
STATELESS=30
STRING=31
TREE_ARBITRARY_TOKEN=32
TREE_CONDITION_ALL=33
TREE_CONDITION_ANY=34
TREE_CONSTS=35
TREE_COPY=36
TREE_COPY_PASTE=37
TREE_EXPRESSION=38
TREE_HINT=39
TREE_HINT_NONE=40
TREE_MODULE=41
TREE_NUM_FRACT=42
TREE_NUM_WHOLE=43
TREE_PASTE=44
TREE_PASTE_REPLACE=45
TREE_PASTE_WITH=46
TREE_PROC=47
TREE_PROC_ARGS=48
TREE_PROC_VARS=49
TREE_STATELESS=50
TREE_STATEMENTS=51
TREE_STATEMENT_CALL=52
TREE_STATEMENT_CALL_ARGS=53
TREE_STATEMENT_ELIF=54
TREE_STATEMENT_ELSE=55
TREE_STATEMENT_IF=56
TREE_TYPES=57
TREE_TYPES_ITEM=58
TREE_VAR=59
TREE_VARS_HINT=60
TREE_VAR_HINT=61
TYPES=62
UNDERSCORE=63
VARS=64
WHITESPACE=65
WITH=66

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", 
    "OPS", "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", 
    "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", 
    "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", 
    "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", 
    "TREE_PASTE_WITH", "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", 
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_VAR", "TREE_VARS_HINT", "TREE_VAR_HINT", "TYPES", 
    "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
]




class ShyCopypasterBackend(TreeParser):
    grammarFileName = "grammar/ShyCopypasterBackend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyCopypasterBackend, self).__init__(input, state, *args, **kwargs)

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )




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

                    if ((ALL <= LA1_0 <= CONSTS) or (CURLY_CLOSE <= LA1_0 <= CURLY_OPEN) or (DIVIDE <= LA1_0 <= MODULE) or (NUMBER <= LA1_0 <= OPS) or LA1_0 == PROC or (STATELESS <= LA1_0 <= STRING) or LA1_0 == TREE_COPY or (TYPES <= LA1_0 <= VARS) or LA1_0 == WITH) :
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
                if LA3 == ALL or LA3 == ANY or LA3 == ARGS or LA3 == ARROW_LEFT or LA3 == ARROW_RIGHT or LA3 == CONSTS or LA3 == CURLY_CLOSE or LA3 == CURLY_OPEN or LA3 == DIVIDE or LA3 == DO or LA3 == ELIF or LA3 == ELSE or LA3 == EXPRESSION or LA3 == ID or LA3 == IF or LA3 == MINUS or LA3 == MODULE or LA3 == NUMBER or LA3 == OPS or LA3 == PROC or LA3 == STATELESS or LA3 == STRING or LA3 == TYPES or LA3 == UNDERSCORE or LA3 == VARS or LA3 == WITH:
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

                        if ((ALL <= LA2_0 <= CONSTS) or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= MODULE) or (NUMBER <= LA2_0 <= OPS) or LA2_0 == PROC or (STATELESS <= LA2_0 <= STRING) or LA2_0 == TREE_COPY or (TYPES <= LA2_0 <= VARS) or LA2_0 == WITH) :
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

                if ((ALL <= LA5_0 <= CONSTS) or (CURLY_CLOSE <= LA5_0 <= CURLY_OPEN) or (DIVIDE <= LA5_0 <= IF) or (MINUS <= LA5_0 <= MODULE) or (NUMBER <= LA5_0 <= OPS) or LA5_0 == PROC or (STATELESS <= LA5_0 <= STRING) or (TYPES <= LA5_0 <= VARS) or LA5_0 == WITH) :
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

                        if ((ALL <= LA4_0 <= CONSTS) or (CURLY_CLOSE <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= MODULE) or (NUMBER <= LA4_0 <= OPS) or LA4_0 == PROC or (STATELESS <= LA4_0 <= STRING) or (TYPES <= LA4_0 <= VARS) or LA4_0 == WITH) :
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



    # $ANTLR start "pure_blocks"
    # grammar/ShyCopypasterBackend.g:49:1: pure_blocks returns [ value ] : ( pure_block )+ ;
    def pure_blocks(self, ):
        value = None


        pure_block11 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:52:5: ( ( pure_block )+ )
                # grammar/ShyCopypasterBackend.g:52:9: ( pure_block )+
                pass 
                # grammar/ShyCopypasterBackend.g:52:9: ( pure_block )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if ((ALL <= LA6_0 <= CONSTS) or (CURLY_CLOSE <= LA6_0 <= CURLY_OPEN) or (DIVIDE <= LA6_0 <= MODULE) or (NUMBER <= LA6_0 <= OPS) or LA6_0 == PROC or (STATELESS <= LA6_0 <= STRING) or (TYPES <= LA6_0 <= VARS) or LA6_0 == WITH) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyCopypasterBackend.g:52:11: pure_block
                        pass 
                        self._state.following.append(self.FOLLOW_pure_block_in_pure_blocks493)
                        pure_block11 = self.pure_block()

                        self._state.following.pop()

                        #action start
                        value += pure_block11 
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

    # $ANTLR end "pure_blocks"



    # $ANTLR start "copy"
    # grammar/ShyCopypasterBackend.g:57:1: copy returns [ value ] : ^( TREE_COPY copy_body copy_pastes ) ;
    def copy(self, ):
        value = None


        copy_body12 = None

        copy_pastes13 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:59:5: ( ^( TREE_COPY copy_body copy_pastes ) )
                # grammar/ShyCopypasterBackend.g:59:9: ^( TREE_COPY copy_body copy_pastes )
                pass 
                self.match(self.input, TREE_COPY, self.FOLLOW_TREE_COPY_in_copy548)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_copy_body_in_copy550)
                copy_body12 = self.copy_body()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_copy_pastes_in_copy552)
                copy_pastes13 = self.copy_pastes()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                        
                value = [ { 'copy' : copy_body12
                           , 'paste' : copy_pastes13 } ]
                        
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "copy"



    # $ANTLR start "copy_body"
    # grammar/ShyCopypasterBackend.g:66:1: copy_body returns [ value ] : ( pure_block )+ ;
    def copy_body(self, ):
        value = None


        pure_block14 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:69:5: ( ( pure_block )+ )
                # grammar/ShyCopypasterBackend.g:69:9: ( pure_block )+
                pass 
                # grammar/ShyCopypasterBackend.g:69:9: ( pure_block )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((ALL <= LA7_0 <= CONSTS) or (CURLY_CLOSE <= LA7_0 <= CURLY_OPEN) or (DIVIDE <= LA7_0 <= MODULE) or (NUMBER <= LA7_0 <= OPS) or LA7_0 == PROC or (STATELESS <= LA7_0 <= STRING) or (TYPES <= LA7_0 <= VARS) or LA7_0 == WITH) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyCopypasterBackend.g:69:11: pure_block
                        pass 
                        self._state.following.append(self.FOLLOW_pure_block_in_copy_body603)
                        pure_block14 = self.pure_block()

                        self._state.following.pop()

                        #action start
                        value += pure_block14 
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

    # $ANTLR end "copy_body"



    # $ANTLR start "copy_pastes"
    # grammar/ShyCopypasterBackend.g:72:1: copy_pastes returns [ value ] : ( copy_paste )+ ;
    def copy_pastes(self, ):
        value = None


        copy_paste15 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:75:5: ( ( copy_paste )+ )
                # grammar/ShyCopypasterBackend.g:75:9: ( copy_paste )+
                pass 
                # grammar/ShyCopypasterBackend.g:75:9: ( copy_paste )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == TREE_COPY_PASTE) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyCopypasterBackend.g:75:11: copy_paste
                        pass 
                        self._state.following.append(self.FOLLOW_copy_paste_in_copy_pastes648)
                        copy_paste15 = self.copy_paste()

                        self._state.following.pop()

                        #action start
                        value . append ( copy_paste15 ) 
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

    # $ANTLR end "copy_pastes"



    # $ANTLR start "copy_paste"
    # grammar/ShyCopypasterBackend.g:78:1: copy_paste returns [ value ] : ^( TREE_COPY_PASTE pastes ) ;
    def copy_paste(self, ):
        value = None


        pastes16 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:80:5: ( ^( TREE_COPY_PASTE pastes ) )
                # grammar/ShyCopypasterBackend.g:80:9: ^( TREE_COPY_PASTE pastes )
                pass 
                self.match(self.input, TREE_COPY_PASTE, self.FOLLOW_TREE_COPY_PASTE_in_copy_paste683)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_pastes_in_copy_paste685)
                pastes16 = self.pastes()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = pastes16 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "copy_paste"



    # $ANTLR start "pastes"
    # grammar/ShyCopypasterBackend.g:83:1: pastes returns [ value ] : ( paste )+ ;
    def pastes(self, ):
        value = None


        paste17 = None


        value = dict ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:86:5: ( ( paste )+ )
                # grammar/ShyCopypasterBackend.g:86:9: ( paste )+
                pass 
                # grammar/ShyCopypasterBackend.g:86:9: ( paste )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == TREE_PASTE) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyCopypasterBackend.g:86:11: paste
                        pass 
                        self._state.following.append(self.FOLLOW_paste_in_pastes728)
                        paste17 = self.paste()

                        self._state.following.pop()

                        #action start
                        value . update ( paste17 ) 
                        #action end



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "pastes"



    # $ANTLR start "paste"
    # grammar/ShyCopypasterBackend.g:89:1: paste returns [ value ] : ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        value = None


        paste_replace18 = None

        paste_with19 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:91:5: ( ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterBackend.g:91:9: ^( TREE_PASTE paste_replace paste_with )
                pass 
                self.match(self.input, TREE_PASTE, self.FOLLOW_TREE_PASTE_in_paste763)

                self.match(self.input, DOWN, None)
                self._state.following.append(self.FOLLOW_paste_replace_in_paste765)
                paste_replace18 = self.paste_replace()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_paste_with_in_paste767)
                paste_with19 = self.paste_with()

                self._state.following.pop()

                self.match(self.input, UP, None)


                #action start
                value = { paste_replace18 : paste_with19 } 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste"



    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterBackend.g:95:1: paste_replace returns [ value ] : ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        value = None


        ID20 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:97:5: ( ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterBackend.g:97:9: ^( TREE_PASTE_REPLACE ID )
                pass 
                self.match(self.input, TREE_PASTE_REPLACE, self.FOLLOW_TREE_PASTE_REPLACE_in_paste_replace808)

                self.match(self.input, DOWN, None)
                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace810)

                self.match(self.input, UP, None)


                #action start
                value = ID20.text 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_replace"



    # $ANTLR start "paste_with"
    # grammar/ShyCopypasterBackend.g:100:1: paste_with returns [ value ] : ( ^( TREE_PASTE_WITH arbitrary_tokens ) | ^( TREE_PASTE_WITH pure_blocks ) );
    def paste_with(self, ):
        value = None


        arbitrary_tokens21 = None

        pure_blocks22 = None


        try:
            try:
                # grammar/ShyCopypasterBackend.g:102:5: ( ^( TREE_PASTE_WITH arbitrary_tokens ) | ^( TREE_PASTE_WITH pure_blocks ) )
                alt10 = 2
                alt10 = self.dfa10.predict(self.input)
                if alt10 == 1:
                    # grammar/ShyCopypasterBackend.g:102:9: ^( TREE_PASTE_WITH arbitrary_tokens )
                    pass 
                    self.match(self.input, TREE_PASTE_WITH, self.FOLLOW_TREE_PASTE_WITH_in_paste_with843)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_arbitrary_tokens_in_paste_with845)
                    arbitrary_tokens21 = self.arbitrary_tokens()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = arbitrary_tokens21 
                    #action end



                elif alt10 == 2:
                    # grammar/ShyCopypasterBackend.g:104:9: ^( TREE_PASTE_WITH pure_blocks )
                    pass 
                    self.match(self.input, TREE_PASTE_WITH, self.FOLLOW_TREE_PASTE_WITH_in_paste_with869)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_pure_blocks_in_paste_with871)
                    pure_blocks22 = self.pure_blocks()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = pure_blocks22 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "paste_with"



    # $ANTLR start "arbitrary_tokens"
    # grammar/ShyCopypasterBackend.g:108:1: arbitrary_tokens returns [ value ] : ( arbitrary_token )+ ;
    def arbitrary_tokens(self, ):
        value = None


        arbitrary_token23 = None


        value = list ( ) 
        try:
            try:
                # grammar/ShyCopypasterBackend.g:111:5: ( ( arbitrary_token )+ )
                # grammar/ShyCopypasterBackend.g:111:9: ( arbitrary_token )+
                pass 
                # grammar/ShyCopypasterBackend.g:111:9: ( arbitrary_token )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((ALL <= LA11_0 <= CONSTS) or (CURLY_CLOSE <= LA11_0 <= CURLY_OPEN) or (DIVIDE <= LA11_0 <= IF) or (MINUS <= LA11_0 <= MODULE) or (NUMBER <= LA11_0 <= OPS) or LA11_0 == PROC or (STATELESS <= LA11_0 <= STRING) or (TYPES <= LA11_0 <= VARS) or LA11_0 == WITH) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyCopypasterBackend.g:111:11: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_arbitrary_tokens922)
                        arbitrary_token23 = self.arbitrary_token()

                        self._state.following.pop()

                        #action start
                        value . append ( arbitrary_token23 ) 
                        #action end



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_tokens"



    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterBackend.g:116:1: arbitrary_token returns [ value ] : ( ALL | ANY | ARGS | CONSTS | DO | ELIF | ELSE | IF | MODULE | OPS | PROC | STATELESS | TYPES | VARS | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION | STRING );
    def arbitrary_token(self, ):
        value = None


        ALL24 = None
        ANY25 = None
        ARGS26 = None
        CONSTS27 = None
        DO28 = None
        ELIF29 = None
        ELSE30 = None
        IF31 = None
        MODULE32 = None
        OPS33 = None
        PROC34 = None
        STATELESS35 = None
        TYPES36 = None
        VARS37 = None
        WITH38 = None
        ARROW_LEFT39 = None
        ARROW_RIGHT40 = None
        CURLY_OPEN41 = None
        CURLY_CLOSE42 = None
        DIVIDE43 = None
        MINUS44 = None
        UNDERSCORE45 = None
        ID46 = None
        NUMBER47 = None
        EXPRESSION48 = None
        STRING49 = None

        try:
            try:
                # grammar/ShyCopypasterBackend.g:118:5: ( ALL | ANY | ARGS | CONSTS | DO | ELIF | ELSE | IF | MODULE | OPS | PROC | STATELESS | TYPES | VARS | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION | STRING )
                alt12 = 26
                LA12 = self.input.LA(1)
                if LA12 == ALL:
                    alt12 = 1
                elif LA12 == ANY:
                    alt12 = 2
                elif LA12 == ARGS:
                    alt12 = 3
                elif LA12 == CONSTS:
                    alt12 = 4
                elif LA12 == DO:
                    alt12 = 5
                elif LA12 == ELIF:
                    alt12 = 6
                elif LA12 == ELSE:
                    alt12 = 7
                elif LA12 == IF:
                    alt12 = 8
                elif LA12 == MODULE:
                    alt12 = 9
                elif LA12 == OPS:
                    alt12 = 10
                elif LA12 == PROC:
                    alt12 = 11
                elif LA12 == STATELESS:
                    alt12 = 12
                elif LA12 == TYPES:
                    alt12 = 13
                elif LA12 == VARS:
                    alt12 = 14
                elif LA12 == WITH:
                    alt12 = 15
                elif LA12 == ARROW_LEFT:
                    alt12 = 16
                elif LA12 == ARROW_RIGHT:
                    alt12 = 17
                elif LA12 == CURLY_OPEN:
                    alt12 = 18
                elif LA12 == CURLY_CLOSE:
                    alt12 = 19
                elif LA12 == DIVIDE:
                    alt12 = 20
                elif LA12 == MINUS:
                    alt12 = 21
                elif LA12 == UNDERSCORE:
                    alt12 = 22
                elif LA12 == ID:
                    alt12 = 23
                elif LA12 == NUMBER:
                    alt12 = 24
                elif LA12 == EXPRESSION:
                    alt12 = 25
                elif LA12 == STRING:
                    alt12 = 26
                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # grammar/ShyCopypasterBackend.g:118:9: ALL
                    pass 
                    ALL24 = self.match(self.input, ALL, self.FOLLOW_ALL_in_arbitrary_token975)

                    #action start
                    value = ALL24.text 
                    #action end



                elif alt12 == 2:
                    # grammar/ShyCopypasterBackend.g:119:9: ANY
                    pass 
                    ANY25 = self.match(self.input, ANY, self.FOLLOW_ANY_in_arbitrary_token987)

                    #action start
                    value = ANY25.text 
                    #action end



                elif alt12 == 3:
                    # grammar/ShyCopypasterBackend.g:120:9: ARGS
                    pass 
                    ARGS26 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_arbitrary_token999)

                    #action start
                    value = ARGS26.text 
                    #action end



                elif alt12 == 4:
                    # grammar/ShyCopypasterBackend.g:121:9: CONSTS
                    pass 
                    CONSTS27 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_arbitrary_token1011)

                    #action start
                    value = CONSTS27.text 
                    #action end



                elif alt12 == 5:
                    # grammar/ShyCopypasterBackend.g:122:9: DO
                    pass 
                    DO28 = self.match(self.input, DO, self.FOLLOW_DO_in_arbitrary_token1023)

                    #action start
                    value = DO28.text 
                    #action end



                elif alt12 == 6:
                    # grammar/ShyCopypasterBackend.g:123:9: ELIF
                    pass 
                    ELIF29 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_arbitrary_token1035)

                    #action start
                    value = ELIF29.text 
                    #action end



                elif alt12 == 7:
                    # grammar/ShyCopypasterBackend.g:124:9: ELSE
                    pass 
                    ELSE30 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_arbitrary_token1047)

                    #action start
                    value = ELSE30.text 
                    #action end



                elif alt12 == 8:
                    # grammar/ShyCopypasterBackend.g:125:9: IF
                    pass 
                    IF31 = self.match(self.input, IF, self.FOLLOW_IF_in_arbitrary_token1059)

                    #action start
                    value = IF31.text 
                    #action end



                elif alt12 == 9:
                    # grammar/ShyCopypasterBackend.g:126:9: MODULE
                    pass 
                    MODULE32 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_arbitrary_token1071)

                    #action start
                    value = MODULE32.text 
                    #action end



                elif alt12 == 10:
                    # grammar/ShyCopypasterBackend.g:127:9: OPS
                    pass 
                    OPS33 = self.match(self.input, OPS, self.FOLLOW_OPS_in_arbitrary_token1083)

                    #action start
                    value = OPS33.text 
                    #action end



                elif alt12 == 11:
                    # grammar/ShyCopypasterBackend.g:128:9: PROC
                    pass 
                    PROC34 = self.match(self.input, PROC, self.FOLLOW_PROC_in_arbitrary_token1095)

                    #action start
                    value = PROC34.text 
                    #action end



                elif alt12 == 12:
                    # grammar/ShyCopypasterBackend.g:129:9: STATELESS
                    pass 
                    STATELESS35 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_arbitrary_token1107)

                    #action start
                    value = STATELESS35.text 
                    #action end



                elif alt12 == 13:
                    # grammar/ShyCopypasterBackend.g:130:9: TYPES
                    pass 
                    TYPES36 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_arbitrary_token1119)

                    #action start
                    value = TYPES36.text 
                    #action end



                elif alt12 == 14:
                    # grammar/ShyCopypasterBackend.g:131:9: VARS
                    pass 
                    VARS37 = self.match(self.input, VARS, self.FOLLOW_VARS_in_arbitrary_token1131)

                    #action start
                    value = VARS37.text 
                    #action end



                elif alt12 == 15:
                    # grammar/ShyCopypasterBackend.g:132:9: WITH
                    pass 
                    WITH38 = self.match(self.input, WITH, self.FOLLOW_WITH_in_arbitrary_token1143)

                    #action start
                    value = WITH38.text 
                    #action end



                elif alt12 == 16:
                    # grammar/ShyCopypasterBackend.g:134:9: ARROW_LEFT
                    pass 
                    ARROW_LEFT39 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_arbitrary_token1156)

                    #action start
                    value = ARROW_LEFT39.text 
                    #action end



                elif alt12 == 17:
                    # grammar/ShyCopypasterBackend.g:135:9: ARROW_RIGHT
                    pass 
                    ARROW_RIGHT40 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_arbitrary_token1168)

                    #action start
                    value = ARROW_RIGHT40.text 
                    #action end



                elif alt12 == 18:
                    # grammar/ShyCopypasterBackend.g:136:9: CURLY_OPEN
                    pass 
                    CURLY_OPEN41 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_arbitrary_token1180)

                    #action start
                    value = CURLY_OPEN41.text 
                    #action end



                elif alt12 == 19:
                    # grammar/ShyCopypasterBackend.g:137:9: CURLY_CLOSE
                    pass 
                    CURLY_CLOSE42 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_arbitrary_token1192)

                    #action start
                    value = CURLY_CLOSE42.text 
                    #action end



                elif alt12 == 20:
                    # grammar/ShyCopypasterBackend.g:138:9: DIVIDE
                    pass 
                    DIVIDE43 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_arbitrary_token1204)

                    #action start
                    value = DIVIDE43.text 
                    #action end



                elif alt12 == 21:
                    # grammar/ShyCopypasterBackend.g:139:9: MINUS
                    pass 
                    MINUS44 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arbitrary_token1216)

                    #action start
                    value = MINUS44.text 
                    #action end



                elif alt12 == 22:
                    # grammar/ShyCopypasterBackend.g:140:9: UNDERSCORE
                    pass 
                    UNDERSCORE45 = self.match(self.input, UNDERSCORE, self.FOLLOW_UNDERSCORE_in_arbitrary_token1228)

                    #action start
                    value = UNDERSCORE45.text 
                    #action end



                elif alt12 == 23:
                    # grammar/ShyCopypasterBackend.g:141:9: ID
                    pass 
                    ID46 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_token1240)

                    #action start
                    value = ID46.text 
                    #action end



                elif alt12 == 24:
                    # grammar/ShyCopypasterBackend.g:142:9: NUMBER
                    pass 
                    NUMBER47 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_arbitrary_token1252)

                    #action start
                    value = NUMBER47.text 
                    #action end



                elif alt12 == 25:
                    # grammar/ShyCopypasterBackend.g:143:9: EXPRESSION
                    pass 
                    EXPRESSION48 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_token1264)

                    #action start
                    value = EXPRESSION48.text 
                    #action end



                elif alt12 == 26:
                    # grammar/ShyCopypasterBackend.g:144:9: STRING
                    pass 
                    STRING49 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_token1276)

                    #action start
                    value = STRING49.text 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "arbitrary_token"



    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\37\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\37\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\56\1\2\1\4\32\3\2\uffff"
        )

    DFA10_max = DFA.unpack(
        u"\1\56\1\2\33\102\2\uffff"
        )

    DFA10_accept = DFA.unpack(
        u"\35\uffff\1\2\1\1"
        )

    DFA10_special = DFA.unpack(
        u"\37\uffff"
        )


    DFA10_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1\uffff"
        u"\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\35\1\27\1\13\1\uffff\1\32"
        u"\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1\20\1"
        u"\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u"\1\36\1\3\1\4\1\5\1\22\1\23\1\6\1\uffff\1\25\1\24\1"
        u"\uffff\1\26\1\7\1\10\1\11\1\33\1\31\1\12\1\uffff\1\27\1\13\1\35"
        u"\1\32\1\14\1\uffff\1\15\1\uffff\1\16\1\34\36\uffff\1\17\1\30\1"
        u"\20\1\uffff\1\21"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


 

    FOLLOW_block_in_start80 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 31, 36, 62, 63, 64, 66])
    FOLLOW_arbitrary_tokens_in_block123 = frozenset([24])
    FOLLOW_NEWLINE_in_block147 = frozenset([1])
    FOLLOW_INDENT_in_block171 = frozenset([24])
    FOLLOW_NEWLINE_in_block177 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 31, 36, 62, 63, 64, 66])
    FOLLOW_block_in_block207 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 31, 36, 62, 63, 64, 66])
    FOLLOW_DEDENT_in_block244 = frozenset([24])
    FOLLOW_NEWLINE_in_block250 = frozenset([1])
    FOLLOW_copy_in_block274 = frozenset([1])
    FOLLOW_arbitrary_tokens_in_pure_block313 = frozenset([24])
    FOLLOW_NEWLINE_in_pure_block337 = frozenset([1])
    FOLLOW_INDENT_in_pure_block361 = frozenset([24])
    FOLLOW_NEWLINE_in_pure_block367 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 31, 62, 63, 64, 66])
    FOLLOW_pure_block_in_pure_block397 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 31, 62, 63, 64, 66])
    FOLLOW_DEDENT_in_pure_block434 = frozenset([24])
    FOLLOW_NEWLINE_in_pure_block440 = frozenset([1])
    FOLLOW_pure_block_in_pure_blocks493 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 31, 62, 63, 64, 66])
    FOLLOW_TREE_COPY_in_copy548 = frozenset([2])
    FOLLOW_copy_body_in_copy550 = frozenset([37])
    FOLLOW_copy_pastes_in_copy552 = frozenset([3])
    FOLLOW_pure_block_in_copy_body603 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 28, 30, 31, 62, 63, 64, 66])
    FOLLOW_copy_paste_in_copy_pastes648 = frozenset([1, 37])
    FOLLOW_TREE_COPY_PASTE_in_copy_paste683 = frozenset([2])
    FOLLOW_pastes_in_copy_paste685 = frozenset([3])
    FOLLOW_paste_in_pastes728 = frozenset([1, 44])
    FOLLOW_TREE_PASTE_in_paste763 = frozenset([2])
    FOLLOW_paste_replace_in_paste765 = frozenset([46])
    FOLLOW_paste_with_in_paste767 = frozenset([3])
    FOLLOW_TREE_PASTE_REPLACE_in_paste_replace808 = frozenset([2])
    FOLLOW_ID_in_paste_replace810 = frozenset([3])
    FOLLOW_TREE_PASTE_WITH_in_paste_with843 = frozenset([2])
    FOLLOW_arbitrary_tokens_in_paste_with845 = frozenset([3])
    FOLLOW_TREE_PASTE_WITH_in_paste_with869 = frozenset([2])
    FOLLOW_pure_blocks_in_paste_with871 = frozenset([3])
    FOLLOW_arbitrary_token_in_arbitrary_tokens922 = frozenset([1, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 28, 30, 31, 62, 63, 64, 66])
    FOLLOW_ALL_in_arbitrary_token975 = frozenset([1])
    FOLLOW_ANY_in_arbitrary_token987 = frozenset([1])
    FOLLOW_ARGS_in_arbitrary_token999 = frozenset([1])
    FOLLOW_CONSTS_in_arbitrary_token1011 = frozenset([1])
    FOLLOW_DO_in_arbitrary_token1023 = frozenset([1])
    FOLLOW_ELIF_in_arbitrary_token1035 = frozenset([1])
    FOLLOW_ELSE_in_arbitrary_token1047 = frozenset([1])
    FOLLOW_IF_in_arbitrary_token1059 = frozenset([1])
    FOLLOW_MODULE_in_arbitrary_token1071 = frozenset([1])
    FOLLOW_OPS_in_arbitrary_token1083 = frozenset([1])
    FOLLOW_PROC_in_arbitrary_token1095 = frozenset([1])
    FOLLOW_STATELESS_in_arbitrary_token1107 = frozenset([1])
    FOLLOW_TYPES_in_arbitrary_token1119 = frozenset([1])
    FOLLOW_VARS_in_arbitrary_token1131 = frozenset([1])
    FOLLOW_WITH_in_arbitrary_token1143 = frozenset([1])
    FOLLOW_ARROW_LEFT_in_arbitrary_token1156 = frozenset([1])
    FOLLOW_ARROW_RIGHT_in_arbitrary_token1168 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_arbitrary_token1180 = frozenset([1])
    FOLLOW_CURLY_CLOSE_in_arbitrary_token1192 = frozenset([1])
    FOLLOW_DIVIDE_in_arbitrary_token1204 = frozenset([1])
    FOLLOW_MINUS_in_arbitrary_token1216 = frozenset([1])
    FOLLOW_UNDERSCORE_in_arbitrary_token1228 = frozenset([1])
    FOLLOW_ID_in_arbitrary_token1240 = frozenset([1])
    FOLLOW_NUMBER_in_arbitrary_token1252 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_token1264 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_token1276 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(ShyCopypasterBackend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
