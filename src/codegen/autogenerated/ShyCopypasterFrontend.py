# $ANTLR 3.4 grammar/ShyCopypasterFrontend.g 2012-01-31 18:11:02

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



class ShyCopypasterFrontendException ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )



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
MESSAGES=22
MINUS=23
MODULE=24
NEWLINE=25
NUMBER=26
OPS=27
PASTE=28
PROC=29
REPLACE=30
REPLY=31
REQUEST=32
STATELESS=33
STRING=34
TREE_ARBITRARY_TOKEN=35
TREE_CONDITION_ALL=36
TREE_CONDITION_ANY=37
TREE_CONSTS=38
TREE_COPY=39
TREE_COPY_PASTE=40
TREE_EXPRESSION=41
TREE_HINT=42
TREE_HINT_NONE=43
TREE_MODULE=44
TREE_NUM_FRACT=45
TREE_NUM_WHOLE=46
TREE_PASTE=47
TREE_PASTE_REPLACE=48
TREE_PASTE_WITH=49
TREE_PROC=50
TREE_PROC_ARGS=51
TREE_PROC_VARS=52
TREE_STATELESS=53
TREE_STATEMENTS=54
TREE_STATEMENT_ASSIGN=55
TREE_STATEMENT_CALL=56
TREE_STATEMENT_ELIF=57
TREE_STATEMENT_ELSE=58
TREE_STATEMENT_IF=59
TREE_STATEMENT_WITH=60
TREE_TYPES=61
TREE_TYPES_ITEM=62
TREE_VAR=63
TREE_VARS_HINT=64
TREE_VAR_HINT=65
TYPES=66
UNDERSCORE=67
VARS=68
WHITESPACE=69
WITH=70

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "NEWLINE", 
    "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "REPLY", "REQUEST", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WITH", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_VAR", "TREE_VARS_HINT", "TREE_VAR_HINT", "TYPES", 
    "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
]




class ShyCopypasterFrontend(Parser):
    grammarFileName = "grammar/ShyCopypasterFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyCopypasterFrontend, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    def emitErrorMessage ( self , msg ) :
        raise ShyCopypasterFrontendException ( msg )


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # grammar/ShyCopypasterFrontend.g:24:1: start : ( block )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        block1 = None



        try:
            try:
                # grammar/ShyCopypasterFrontend.g:24:7: ( ( block )* )
                # grammar/ShyCopypasterFrontend.g:24:9: ( block )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyCopypasterFrontend.g:24:9: ( block )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((ALL <= LA1_0 <= CURLY_OPEN) or (DIVIDE <= LA1_0 <= MODULE) or (NUMBER <= LA1_0 <= OPS) or LA1_0 == PROC or (REPLY <= LA1_0 <= STRING) or (TYPES <= LA1_0 <= VARS) or LA1_0 == WITH) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammar/ShyCopypasterFrontend.g:24:9: block
                        pass 
                        self._state.following.append(self.FOLLOW_block_in_start80)
                        block1 = self.block()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, block1.tree)



                    else:
                        break #loop1




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "start"


    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.block_return, self).__init__()

            self.tree = None





    # $ANTLR start "block"
    # grammar/ShyCopypasterFrontend.g:26:1: block : ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( block )+ DEDENT NEWLINE | COPY copy_body ( copy_paste )+ -> ^( TREE_COPY copy_body ( copy_paste )+ ) );
    def block(self, ):
        retval = self.block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE3 = None
        INDENT4 = None
        NEWLINE5 = None
        DEDENT7 = None
        NEWLINE8 = None
        COPY9 = None
        arbitrary_token2 = None

        block6 = None

        copy_body10 = None

        copy_paste11 = None


        NEWLINE3_tree = None
        INDENT4_tree = None
        NEWLINE5_tree = None
        DEDENT7_tree = None
        NEWLINE8_tree = None
        COPY9_tree = None
        stream_COPY = RewriteRuleTokenStream(self._adaptor, "token COPY")
        stream_copy_body = RewriteRuleSubtreeStream(self._adaptor, "rule copy_body")
        stream_copy_paste = RewriteRuleSubtreeStream(self._adaptor, "rule copy_paste")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:27:5: ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( block )+ DEDENT NEWLINE | COPY copy_body ( copy_paste )+ -> ^( TREE_COPY copy_body ( copy_paste )+ ) )
                alt5 = 3
                LA5 = self.input.LA(1)
                if LA5 == ALL or LA5 == ANY or LA5 == ARGS or LA5 == ARROW_LEFT or LA5 == ARROW_RIGHT or LA5 == CONSTS or LA5 == CURLY_CLOSE or LA5 == CURLY_OPEN or LA5 == DIVIDE or LA5 == DO or LA5 == ELIF or LA5 == ELSE or LA5 == EXPRESSION or LA5 == ID or LA5 == IF or LA5 == MESSAGES or LA5 == MINUS or LA5 == MODULE or LA5 == NUMBER or LA5 == OPS or LA5 == PROC or LA5 == REPLY or LA5 == REQUEST or LA5 == STATELESS or LA5 == STRING or LA5 == TYPES or LA5 == UNDERSCORE or LA5 == VARS or LA5 == WITH:
                    alt5 = 1
                elif LA5 == INDENT:
                    alt5 = 2
                elif LA5 == COPY:
                    alt5 = 3
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyCopypasterFrontend.g:27:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    # grammar/ShyCopypasterFrontend.g:27:9: ( arbitrary_token )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if ((ALL <= LA2_0 <= CONSTS) or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= IF) or (MESSAGES <= LA2_0 <= MODULE) or (NUMBER <= LA2_0 <= OPS) or LA2_0 == PROC or (REPLY <= LA2_0 <= STRING) or (TYPES <= LA2_0 <= VARS) or LA2_0 == WITH) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyCopypasterFrontend.g:27:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_block97)
                            arbitrary_token2 = self.arbitrary_token()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, arbitrary_token2.tree)



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    NEWLINE3 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block101)
                    NEWLINE3_tree = self._adaptor.createWithPayload(NEWLINE3)
                    self._adaptor.addChild(root_0, NEWLINE3_tree)




                elif alt5 == 2:
                    # grammar/ShyCopypasterFrontend.g:28:9: INDENT NEWLINE ( block )+ DEDENT NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    INDENT4 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_block111)
                    INDENT4_tree = self._adaptor.createWithPayload(INDENT4)
                    self._adaptor.addChild(root_0, INDENT4_tree)



                    NEWLINE5 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block113)
                    NEWLINE5_tree = self._adaptor.createWithPayload(NEWLINE5)
                    self._adaptor.addChild(root_0, NEWLINE5_tree)



                    # grammar/ShyCopypasterFrontend.g:28:24: ( block )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if ((ALL <= LA3_0 <= CURLY_OPEN) or (DIVIDE <= LA3_0 <= MODULE) or (NUMBER <= LA3_0 <= OPS) or LA3_0 == PROC or (REPLY <= LA3_0 <= STRING) or (TYPES <= LA3_0 <= VARS) or LA3_0 == WITH) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammar/ShyCopypasterFrontend.g:28:24: block
                            pass 
                            self._state.following.append(self.FOLLOW_block_in_block115)
                            block6 = self.block()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, block6.tree)



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    DEDENT7 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_block119)
                    DEDENT7_tree = self._adaptor.createWithPayload(DEDENT7)
                    self._adaptor.addChild(root_0, DEDENT7_tree)



                    NEWLINE8 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block121)
                    NEWLINE8_tree = self._adaptor.createWithPayload(NEWLINE8)
                    self._adaptor.addChild(root_0, NEWLINE8_tree)




                elif alt5 == 3:
                    # grammar/ShyCopypasterFrontend.g:29:9: COPY copy_body ( copy_paste )+
                    pass 
                    COPY9 = self.match(self.input, COPY, self.FOLLOW_COPY_in_block131) 
                    stream_COPY.add(COPY9)


                    self._state.following.append(self.FOLLOW_copy_body_in_block133)
                    copy_body10 = self.copy_body()

                    self._state.following.pop()
                    stream_copy_body.add(copy_body10.tree)


                    # grammar/ShyCopypasterFrontend.g:29:24: ( copy_paste )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == PASTE) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammar/ShyCopypasterFrontend.g:29:24: copy_paste
                            pass 
                            self._state.following.append(self.FOLLOW_copy_paste_in_block135)
                            copy_paste11 = self.copy_paste()

                            self._state.following.pop()
                            stream_copy_paste.add(copy_paste11.tree)



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    # AST Rewrite
                    # elements: copy_body, copy_paste
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 29:37: -> ^( TREE_COPY copy_body ( copy_paste )+ )
                    # grammar/ShyCopypasterFrontend.g:29:40: ^( TREE_COPY copy_body ( copy_paste )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_COPY, "TREE_COPY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_copy_body.nextTree())

                    # grammar/ShyCopypasterFrontend.g:29:63: ( copy_paste )+
                    if not (stream_copy_paste.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_copy_paste.hasNext():
                        self._adaptor.addChild(root_1, stream_copy_paste.nextTree())


                    stream_copy_paste.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "block"


    class pure_block_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.pure_block_return, self).__init__()

            self.tree = None





    # $ANTLR start "pure_block"
    # grammar/ShyCopypasterFrontend.g:32:1: pure_block : ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE );
    def pure_block(self, ):
        retval = self.pure_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE13 = None
        INDENT14 = None
        NEWLINE15 = None
        DEDENT17 = None
        NEWLINE18 = None
        arbitrary_token12 = None

        pure_block16 = None


        NEWLINE13_tree = None
        INDENT14_tree = None
        NEWLINE15_tree = None
        DEDENT17_tree = None
        NEWLINE18_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:33:5: ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if ((ALL <= LA8_0 <= CONSTS) or (CURLY_CLOSE <= LA8_0 <= CURLY_OPEN) or (DIVIDE <= LA8_0 <= IF) or (MESSAGES <= LA8_0 <= MODULE) or (NUMBER <= LA8_0 <= OPS) or LA8_0 == PROC or (REPLY <= LA8_0 <= STRING) or (TYPES <= LA8_0 <= VARS) or LA8_0 == WITH) :
                    alt8 = 1
                elif (LA8_0 == INDENT) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # grammar/ShyCopypasterFrontend.g:33:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    # grammar/ShyCopypasterFrontend.g:33:9: ( arbitrary_token )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if ((ALL <= LA6_0 <= CONSTS) or (CURLY_CLOSE <= LA6_0 <= CURLY_OPEN) or (DIVIDE <= LA6_0 <= IF) or (MESSAGES <= LA6_0 <= MODULE) or (NUMBER <= LA6_0 <= OPS) or LA6_0 == PROC or (REPLY <= LA6_0 <= STRING) or (TYPES <= LA6_0 <= VARS) or LA6_0 == WITH) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyCopypasterFrontend.g:33:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_pure_block171)
                            arbitrary_token12 = self.arbitrary_token()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, arbitrary_token12.tree)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    NEWLINE13 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block175)
                    NEWLINE13_tree = self._adaptor.createWithPayload(NEWLINE13)
                    self._adaptor.addChild(root_0, NEWLINE13_tree)




                elif alt8 == 2:
                    # grammar/ShyCopypasterFrontend.g:34:9: INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    INDENT14 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_pure_block185)
                    INDENT14_tree = self._adaptor.createWithPayload(INDENT14)
                    self._adaptor.addChild(root_0, INDENT14_tree)



                    NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block187)
                    NEWLINE15_tree = self._adaptor.createWithPayload(NEWLINE15)
                    self._adaptor.addChild(root_0, NEWLINE15_tree)



                    # grammar/ShyCopypasterFrontend.g:34:24: ( pure_block )+
                    cnt7 = 0
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if ((ALL <= LA7_0 <= CONSTS) or (CURLY_CLOSE <= LA7_0 <= CURLY_OPEN) or (DIVIDE <= LA7_0 <= MODULE) or (NUMBER <= LA7_0 <= OPS) or LA7_0 == PROC or (REPLY <= LA7_0 <= STRING) or (TYPES <= LA7_0 <= VARS) or LA7_0 == WITH) :
                            alt7 = 1


                        if alt7 == 1:
                            # grammar/ShyCopypasterFrontend.g:34:24: pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_pure_block189)
                            pure_block16 = self.pure_block()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, pure_block16.tree)



                        else:
                            if cnt7 >= 1:
                                break #loop7

                            eee = EarlyExitException(7, self.input)
                            raise eee

                        cnt7 += 1


                    DEDENT17 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_pure_block193)
                    DEDENT17_tree = self._adaptor.createWithPayload(DEDENT17)
                    self._adaptor.addChild(root_0, DEDENT17_tree)



                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block195)
                    NEWLINE18_tree = self._adaptor.createWithPayload(NEWLINE18)
                    self._adaptor.addChild(root_0, NEWLINE18_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "pure_block"


    class copy_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.copy_body_return, self).__init__()

            self.tree = None





    # $ANTLR start "copy_body"
    # grammar/ShyCopypasterFrontend.g:37:1: copy_body : ( NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ( pure_block )+ | ( arbitrary_token )+ NEWLINE );
    def copy_body(self, ):
        retval = self.copy_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE19 = None
        INDENT20 = None
        NEWLINE21 = None
        DEDENT23 = None
        NEWLINE24 = None
        NEWLINE26 = None
        pure_block22 = None

        arbitrary_token25 = None


        NEWLINE19_tree = None
        INDENT20_tree = None
        NEWLINE21_tree = None
        DEDENT23_tree = None
        NEWLINE24_tree = None
        NEWLINE26_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_pure_block = RewriteRuleSubtreeStream(self._adaptor, "rule pure_block")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:38:5: ( NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ( pure_block )+ | ( arbitrary_token )+ NEWLINE )
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == NEWLINE) :
                    alt11 = 1
                elif ((ALL <= LA11_0 <= CONSTS) or (CURLY_CLOSE <= LA11_0 <= CURLY_OPEN) or (DIVIDE <= LA11_0 <= IF) or (MESSAGES <= LA11_0 <= MODULE) or (NUMBER <= LA11_0 <= OPS) or LA11_0 == PROC or (REPLY <= LA11_0 <= STRING) or (TYPES <= LA11_0 <= VARS) or LA11_0 == WITH) :
                    alt11 = 2
                else:
                    nvae = NoViableAltException("", 11, 0, self.input)

                    raise nvae


                if alt11 == 1:
                    # grammar/ShyCopypasterFrontend.g:38:9: NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE
                    pass 
                    NEWLINE19 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_body214) 
                    stream_NEWLINE.add(NEWLINE19)


                    INDENT20 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_copy_body216) 
                    stream_INDENT.add(INDENT20)


                    NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_body218) 
                    stream_NEWLINE.add(NEWLINE21)


                    # grammar/ShyCopypasterFrontend.g:38:32: ( pure_block )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if ((ALL <= LA9_0 <= CONSTS) or (CURLY_CLOSE <= LA9_0 <= CURLY_OPEN) or (DIVIDE <= LA9_0 <= MODULE) or (NUMBER <= LA9_0 <= OPS) or LA9_0 == PROC or (REPLY <= LA9_0 <= STRING) or (TYPES <= LA9_0 <= VARS) or LA9_0 == WITH) :
                            alt9 = 1


                        if alt9 == 1:
                            # grammar/ShyCopypasterFrontend.g:38:32: pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_copy_body220)
                            pure_block22 = self.pure_block()

                            self._state.following.pop()
                            stream_pure_block.add(pure_block22.tree)



                        else:
                            if cnt9 >= 1:
                                break #loop9

                            eee = EarlyExitException(9, self.input)
                            raise eee

                        cnt9 += 1


                    DEDENT23 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_copy_body224) 
                    stream_DEDENT.add(DEDENT23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_body226) 
                    stream_NEWLINE.add(NEWLINE24)


                    # AST Rewrite
                    # elements: pure_block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 38:60: -> ( pure_block )+
                    # grammar/ShyCopypasterFrontend.g:38:63: ( pure_block )+
                    if not (stream_pure_block.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_pure_block.hasNext():
                        self._adaptor.addChild(root_0, stream_pure_block.nextTree())


                    stream_pure_block.reset()




                    retval.tree = root_0




                elif alt11 == 2:
                    # grammar/ShyCopypasterFrontend.g:39:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    # grammar/ShyCopypasterFrontend.g:39:9: ( arbitrary_token )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if ((ALL <= LA10_0 <= CONSTS) or (CURLY_CLOSE <= LA10_0 <= CURLY_OPEN) or (DIVIDE <= LA10_0 <= IF) or (MESSAGES <= LA10_0 <= MODULE) or (NUMBER <= LA10_0 <= OPS) or LA10_0 == PROC or (REPLY <= LA10_0 <= STRING) or (TYPES <= LA10_0 <= VARS) or LA10_0 == WITH) :
                            alt10 = 1


                        if alt10 == 1:
                            # grammar/ShyCopypasterFrontend.g:39:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_copy_body242)
                            arbitrary_token25 = self.arbitrary_token()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, arbitrary_token25.tree)



                        else:
                            if cnt10 >= 1:
                                break #loop10

                            eee = EarlyExitException(10, self.input)
                            raise eee

                        cnt10 += 1


                    NEWLINE26 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_body246)
                    NEWLINE26_tree = self._adaptor.createWithPayload(NEWLINE26)
                    self._adaptor.addChild(root_0, NEWLINE26_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "copy_body"


    class copy_paste_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.copy_paste_return, self).__init__()

            self.tree = None





    # $ANTLR start "copy_paste"
    # grammar/ShyCopypasterFrontend.g:42:1: copy_paste : ( PASTE paste -> ^( TREE_COPY_PASTE paste ) | PASTE NEWLINE INDENT NEWLINE ( paste )+ DEDENT NEWLINE -> ^( TREE_COPY_PASTE ( paste )+ ) );
    def copy_paste(self, ):
        retval = self.copy_paste_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PASTE27 = None
        PASTE29 = None
        NEWLINE30 = None
        INDENT31 = None
        NEWLINE32 = None
        DEDENT34 = None
        NEWLINE35 = None
        paste28 = None

        paste33 = None


        PASTE27_tree = None
        PASTE29_tree = None
        NEWLINE30_tree = None
        INDENT31_tree = None
        NEWLINE32_tree = None
        DEDENT34_tree = None
        NEWLINE35_tree = None
        stream_PASTE = RewriteRuleTokenStream(self._adaptor, "token PASTE")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_paste = RewriteRuleSubtreeStream(self._adaptor, "rule paste")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:43:5: ( PASTE paste -> ^( TREE_COPY_PASTE paste ) | PASTE NEWLINE INDENT NEWLINE ( paste )+ DEDENT NEWLINE -> ^( TREE_COPY_PASTE ( paste )+ ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == PASTE) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == NEWLINE) :
                        alt13 = 2
                    elif (LA13_1 == REPLACE) :
                        alt13 = 1
                    else:
                        nvae = NoViableAltException("", 13, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # grammar/ShyCopypasterFrontend.g:43:9: PASTE paste
                    pass 
                    PASTE27 = self.match(self.input, PASTE, self.FOLLOW_PASTE_in_copy_paste265) 
                    stream_PASTE.add(PASTE27)


                    self._state.following.append(self.FOLLOW_paste_in_copy_paste267)
                    paste28 = self.paste()

                    self._state.following.pop()
                    stream_paste.add(paste28.tree)


                    # AST Rewrite
                    # elements: paste
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 44:9: -> ^( TREE_COPY_PASTE paste )
                    # grammar/ShyCopypasterFrontend.g:44:12: ^( TREE_COPY_PASTE paste )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_COPY_PASTE, "TREE_COPY_PASTE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_paste.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 2:
                    # grammar/ShyCopypasterFrontend.g:45:9: PASTE NEWLINE INDENT NEWLINE ( paste )+ DEDENT NEWLINE
                    pass 
                    PASTE29 = self.match(self.input, PASTE, self.FOLLOW_PASTE_in_copy_paste295) 
                    stream_PASTE.add(PASTE29)


                    NEWLINE30 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_paste297) 
                    stream_NEWLINE.add(NEWLINE30)


                    INDENT31 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_copy_paste299) 
                    stream_INDENT.add(INDENT31)


                    NEWLINE32 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_paste301) 
                    stream_NEWLINE.add(NEWLINE32)


                    # grammar/ShyCopypasterFrontend.g:45:38: ( paste )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == REPLACE) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyCopypasterFrontend.g:45:38: paste
                            pass 
                            self._state.following.append(self.FOLLOW_paste_in_copy_paste303)
                            paste33 = self.paste()

                            self._state.following.pop()
                            stream_paste.add(paste33.tree)



                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    DEDENT34 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_copy_paste307) 
                    stream_DEDENT.add(DEDENT34)


                    NEWLINE35 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_paste309) 
                    stream_NEWLINE.add(NEWLINE35)


                    # AST Rewrite
                    # elements: paste
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 46:9: -> ^( TREE_COPY_PASTE ( paste )+ )
                    # grammar/ShyCopypasterFrontend.g:46:12: ^( TREE_COPY_PASTE ( paste )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_COPY_PASTE, "TREE_COPY_PASTE")
                    , root_1)

                    # grammar/ShyCopypasterFrontend.g:46:31: ( paste )+
                    if not (stream_paste.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_paste.hasNext():
                        self._adaptor.addChild(root_1, stream_paste.nextTree())


                    stream_paste.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "copy_paste"


    class paste_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.paste_return, self).__init__()

            self.tree = None





    # $ANTLR start "paste"
    # grammar/ShyCopypasterFrontend.g:49:1: paste : REPLACE paste_replace WITH paste_with -> ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        retval = self.paste_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REPLACE36 = None
        WITH38 = None
        paste_replace37 = None

        paste_with39 = None


        REPLACE36_tree = None
        WITH38_tree = None
        stream_REPLACE = RewriteRuleTokenStream(self._adaptor, "token REPLACE")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_paste_with = RewriteRuleSubtreeStream(self._adaptor, "rule paste_with")
        stream_paste_replace = RewriteRuleSubtreeStream(self._adaptor, "rule paste_replace")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:50:5: ( REPLACE paste_replace WITH paste_with -> ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterFrontend.g:50:9: REPLACE paste_replace WITH paste_with
                pass 
                REPLACE36 = self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_paste348) 
                stream_REPLACE.add(REPLACE36)


                self._state.following.append(self.FOLLOW_paste_replace_in_paste350)
                paste_replace37 = self.paste_replace()

                self._state.following.pop()
                stream_paste_replace.add(paste_replace37.tree)


                WITH38 = self.match(self.input, WITH, self.FOLLOW_WITH_in_paste352) 
                stream_WITH.add(WITH38)


                self._state.following.append(self.FOLLOW_paste_with_in_paste354)
                paste_with39 = self.paste_with()

                self._state.following.pop()
                stream_paste_with.add(paste_with39.tree)


                # AST Rewrite
                # elements: paste_replace, paste_with
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 51:9: -> ^( TREE_PASTE paste_replace paste_with )
                # grammar/ShyCopypasterFrontend.g:51:12: ^( TREE_PASTE paste_replace paste_with )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PASTE, "TREE_PASTE")
                , root_1)

                self._adaptor.addChild(root_1, stream_paste_replace.nextTree())

                self._adaptor.addChild(root_1, stream_paste_with.nextTree())

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "paste"


    class paste_replace_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.paste_replace_return, self).__init__()

            self.tree = None





    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterFrontend.g:54:1: paste_replace : ID -> ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        retval = self.paste_replace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID40 = None

        ID40_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:55:5: ( ID -> ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterFrontend.g:55:9: ID
                pass 
                ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace393) 
                stream_ID.add(ID40)


                # AST Rewrite
                # elements: ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 55:12: -> ^( TREE_PASTE_REPLACE ID )
                # grammar/ShyCopypasterFrontend.g:55:15: ^( TREE_PASTE_REPLACE ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PASTE_REPLACE, "TREE_PASTE_REPLACE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "paste_replace"


    class paste_with_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.paste_with_return, self).__init__()

            self.tree = None





    # $ANTLR start "paste_with"
    # grammar/ShyCopypasterFrontend.g:58:1: paste_with : ( ( arbitrary_token )+ NEWLINE -> ^( TREE_PASTE_WITH ( arbitrary_token )+ ) | NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ^( TREE_PASTE_WITH ( pure_block )+ ) );
    def paste_with(self, ):
        retval = self.paste_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE42 = None
        NEWLINE43 = None
        INDENT44 = None
        NEWLINE45 = None
        DEDENT47 = None
        NEWLINE48 = None
        arbitrary_token41 = None

        pure_block46 = None


        NEWLINE42_tree = None
        NEWLINE43_tree = None
        INDENT44_tree = None
        NEWLINE45_tree = None
        DEDENT47_tree = None
        NEWLINE48_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_arbitrary_token = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_token")
        stream_pure_block = RewriteRuleSubtreeStream(self._adaptor, "rule pure_block")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:59:5: ( ( arbitrary_token )+ NEWLINE -> ^( TREE_PASTE_WITH ( arbitrary_token )+ ) | NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ^( TREE_PASTE_WITH ( pure_block )+ ) )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((ALL <= LA16_0 <= CONSTS) or (CURLY_CLOSE <= LA16_0 <= CURLY_OPEN) or (DIVIDE <= LA16_0 <= IF) or (MESSAGES <= LA16_0 <= MODULE) or (NUMBER <= LA16_0 <= OPS) or LA16_0 == PROC or (REPLY <= LA16_0 <= STRING) or (TYPES <= LA16_0 <= VARS) or LA16_0 == WITH) :
                    alt16 = 1
                elif (LA16_0 == NEWLINE) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammar/ShyCopypasterFrontend.g:59:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    # grammar/ShyCopypasterFrontend.g:59:9: ( arbitrary_token )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if ((ALL <= LA14_0 <= CONSTS) or (CURLY_CLOSE <= LA14_0 <= CURLY_OPEN) or (DIVIDE <= LA14_0 <= IF) or (MESSAGES <= LA14_0 <= MODULE) or (NUMBER <= LA14_0 <= OPS) or LA14_0 == PROC or (REPLY <= LA14_0 <= STRING) or (TYPES <= LA14_0 <= VARS) or LA14_0 == WITH) :
                            alt14 = 1


                        if alt14 == 1:
                            # grammar/ShyCopypasterFrontend.g:59:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_paste_with422)
                            arbitrary_token41 = self.arbitrary_token()

                            self._state.following.pop()
                            stream_arbitrary_token.add(arbitrary_token41.tree)



                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                    NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with426) 
                    stream_NEWLINE.add(NEWLINE42)


                    # AST Rewrite
                    # elements: arbitrary_token
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 60:9: -> ^( TREE_PASTE_WITH ( arbitrary_token )+ )
                    # grammar/ShyCopypasterFrontend.g:60:12: ^( TREE_PASTE_WITH ( arbitrary_token )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                    , root_1)

                    # grammar/ShyCopypasterFrontend.g:60:31: ( arbitrary_token )+
                    if not (stream_arbitrary_token.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_token.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_token.nextTree())


                    stream_arbitrary_token.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt16 == 2:
                    # grammar/ShyCopypasterFrontend.g:61:9: NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE
                    pass 
                    NEWLINE43 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with457) 
                    stream_NEWLINE.add(NEWLINE43)


                    INDENT44 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_paste_with459) 
                    stream_INDENT.add(INDENT44)


                    NEWLINE45 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with461) 
                    stream_NEWLINE.add(NEWLINE45)


                    # grammar/ShyCopypasterFrontend.g:61:32: ( pure_block )+
                    cnt15 = 0
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if ((ALL <= LA15_0 <= CONSTS) or (CURLY_CLOSE <= LA15_0 <= CURLY_OPEN) or (DIVIDE <= LA15_0 <= MODULE) or (NUMBER <= LA15_0 <= OPS) or LA15_0 == PROC or (REPLY <= LA15_0 <= STRING) or (TYPES <= LA15_0 <= VARS) or LA15_0 == WITH) :
                            alt15 = 1


                        if alt15 == 1:
                            # grammar/ShyCopypasterFrontend.g:61:32: pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_paste_with463)
                            pure_block46 = self.pure_block()

                            self._state.following.pop()
                            stream_pure_block.add(pure_block46.tree)



                        else:
                            if cnt15 >= 1:
                                break #loop15

                            eee = EarlyExitException(15, self.input)
                            raise eee

                        cnt15 += 1


                    DEDENT47 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_paste_with467) 
                    stream_DEDENT.add(DEDENT47)


                    NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with469) 
                    stream_NEWLINE.add(NEWLINE48)


                    # AST Rewrite
                    # elements: pure_block
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 62:9: -> ^( TREE_PASTE_WITH ( pure_block )+ )
                    # grammar/ShyCopypasterFrontend.g:62:12: ^( TREE_PASTE_WITH ( pure_block )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                    , root_1)

                    # grammar/ShyCopypasterFrontend.g:62:31: ( pure_block )+
                    if not (stream_pure_block.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_pure_block.hasNext():
                        self._adaptor.addChild(root_1, stream_pure_block.nextTree())


                    stream_pure_block.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "paste_with"


    class arbitrary_token_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.arbitrary_token_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterFrontend.g:65:1: arbitrary_token : ( ALL | ANY | ARGS | CONSTS | DO | ELIF | ELSE | IF | MESSAGES | MODULE | OPS | PROC | REQUEST | REPLY | STATELESS | TYPES | VARS | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION | STRING );
    def arbitrary_token(self, ):
        retval = self.arbitrary_token_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set49 = None

        set49_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:66:5: ( ALL | ANY | ARGS | CONSTS | DO | ELIF | ELSE | IF | MESSAGES | MODULE | OPS | PROC | REQUEST | REPLY | STATELESS | TYPES | VARS | WITH | ARROW_LEFT | ARROW_RIGHT | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION | STRING )
                # grammar/ShyCopypasterFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set49 = self.input.LT(1)

                if (ALL <= self.input.LA(1) <= CONSTS) or (CURLY_CLOSE <= self.input.LA(1) <= CURLY_OPEN) or (DIVIDE <= self.input.LA(1) <= IF) or (MESSAGES <= self.input.LA(1) <= MODULE) or (NUMBER <= self.input.LA(1) <= OPS) or self.input.LA(1) == PROC or (REPLY <= self.input.LA(1) <= STRING) or (TYPES <= self.input.LA(1) <= VARS) or self.input.LA(1) == WITH:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set49))

                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arbitrary_token"



 

    FOLLOW_block_in_start80 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_arbitrary_token_in_block97 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_NEWLINE_in_block101 = frozenset([1])
    FOLLOW_INDENT_in_block111 = frozenset([25])
    FOLLOW_NEWLINE_in_block113 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_block_in_block115 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_DEDENT_in_block119 = frozenset([25])
    FOLLOW_NEWLINE_in_block121 = frozenset([1])
    FOLLOW_COPY_in_block131 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_copy_body_in_block133 = frozenset([28])
    FOLLOW_copy_paste_in_block135 = frozenset([1, 28])
    FOLLOW_arbitrary_token_in_pure_block171 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_NEWLINE_in_pure_block175 = frozenset([1])
    FOLLOW_INDENT_in_pure_block185 = frozenset([25])
    FOLLOW_NEWLINE_in_pure_block187 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_pure_block_in_pure_block189 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_DEDENT_in_pure_block193 = frozenset([25])
    FOLLOW_NEWLINE_in_pure_block195 = frozenset([1])
    FOLLOW_NEWLINE_in_copy_body214 = frozenset([21])
    FOLLOW_INDENT_in_copy_body216 = frozenset([25])
    FOLLOW_NEWLINE_in_copy_body218 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_pure_block_in_copy_body220 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_DEDENT_in_copy_body224 = frozenset([25])
    FOLLOW_NEWLINE_in_copy_body226 = frozenset([1])
    FOLLOW_arbitrary_token_in_copy_body242 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_NEWLINE_in_copy_body246 = frozenset([1])
    FOLLOW_PASTE_in_copy_paste265 = frozenset([30])
    FOLLOW_paste_in_copy_paste267 = frozenset([1])
    FOLLOW_PASTE_in_copy_paste295 = frozenset([25])
    FOLLOW_NEWLINE_in_copy_paste297 = frozenset([21])
    FOLLOW_INDENT_in_copy_paste299 = frozenset([25])
    FOLLOW_NEWLINE_in_copy_paste301 = frozenset([30])
    FOLLOW_paste_in_copy_paste303 = frozenset([13, 30])
    FOLLOW_DEDENT_in_copy_paste307 = frozenset([25])
    FOLLOW_NEWLINE_in_copy_paste309 = frozenset([1])
    FOLLOW_REPLACE_in_paste348 = frozenset([19])
    FOLLOW_paste_replace_in_paste350 = frozenset([70])
    FOLLOW_WITH_in_paste352 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_paste_with_in_paste354 = frozenset([1])
    FOLLOW_ID_in_paste_replace393 = frozenset([1])
    FOLLOW_arbitrary_token_in_paste_with422 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_NEWLINE_in_paste_with426 = frozenset([1])
    FOLLOW_NEWLINE_in_paste_with457 = frozenset([21])
    FOLLOW_INDENT_in_paste_with459 = frozenset([25])
    FOLLOW_NEWLINE_in_paste_with461 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_pure_block_in_paste_with463 = frozenset([4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 66, 67, 68, 70])
    FOLLOW_DEDENT_in_paste_with467 = frozenset([25])
    FOLLOW_NEWLINE_in_paste_with469 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyCopypasterFrontendLexer", ShyCopypasterFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
