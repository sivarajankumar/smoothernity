# $ANTLR 3.4 grammar/ShyCopypasterFrontend.g 2012-01-19 21:21:48

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

                    if ((CONSTS <= LA1_0 <= CURLY_OPEN) or (DIVIDE <= LA1_0 <= MODULE) or LA1_0 == NUMBER or (TYPES <= LA1_0 <= UNDERSCORE)) :
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
                    # grammar/ShyCopypasterFrontend.g:27:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    # grammar/ShyCopypasterFrontend.g:27:9: ( arbitrary_token )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= ID) or (MINUS <= LA2_0 <= MODULE) or LA2_0 == NUMBER or (TYPES <= LA2_0 <= UNDERSCORE)) :
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

                        if ((CONSTS <= LA3_0 <= CURLY_OPEN) or (DIVIDE <= LA3_0 <= MODULE) or LA3_0 == NUMBER or (TYPES <= LA3_0 <= UNDERSCORE)) :
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

                if (LA8_0 == CONSTS or (CURLY_CLOSE <= LA8_0 <= CURLY_OPEN) or (DIVIDE <= LA8_0 <= ID) or (MINUS <= LA8_0 <= MODULE) or LA8_0 == NUMBER or (TYPES <= LA8_0 <= UNDERSCORE)) :
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

                        if (LA6_0 == CONSTS or (CURLY_CLOSE <= LA6_0 <= CURLY_OPEN) or (DIVIDE <= LA6_0 <= ID) or (MINUS <= LA6_0 <= MODULE) or LA6_0 == NUMBER or (TYPES <= LA6_0 <= UNDERSCORE)) :
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

                        if (LA7_0 == CONSTS or (CURLY_CLOSE <= LA7_0 <= CURLY_OPEN) or (DIVIDE <= LA7_0 <= MODULE) or LA7_0 == NUMBER or (TYPES <= LA7_0 <= UNDERSCORE)) :
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
                elif (LA11_0 == CONSTS or (CURLY_CLOSE <= LA11_0 <= CURLY_OPEN) or (DIVIDE <= LA11_0 <= ID) or (MINUS <= LA11_0 <= MODULE) or LA11_0 == NUMBER or (TYPES <= LA11_0 <= UNDERSCORE)) :
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

                        if (LA9_0 == CONSTS or (CURLY_CLOSE <= LA9_0 <= CURLY_OPEN) or (DIVIDE <= LA9_0 <= MODULE) or LA9_0 == NUMBER or (TYPES <= LA9_0 <= UNDERSCORE)) :
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

                        if (LA10_0 == CONSTS or (CURLY_CLOSE <= LA10_0 <= CURLY_OPEN) or (DIVIDE <= LA10_0 <= ID) or (MINUS <= LA10_0 <= MODULE) or LA10_0 == NUMBER or (TYPES <= LA10_0 <= UNDERSCORE)) :
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
    # grammar/ShyCopypasterFrontend.g:42:1: copy_paste : PASTE paste -> ^( TREE_COPY_PASTE paste ) ;
    def copy_paste(self, ):
        retval = self.copy_paste_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PASTE27 = None
        paste28 = None


        PASTE27_tree = None
        stream_PASTE = RewriteRuleTokenStream(self._adaptor, "token PASTE")
        stream_paste = RewriteRuleSubtreeStream(self._adaptor, "rule paste")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:43:5: ( PASTE paste -> ^( TREE_COPY_PASTE paste ) )
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
                # 43:21: -> ^( TREE_COPY_PASTE paste )
                # grammar/ShyCopypasterFrontend.g:43:24: ^( TREE_COPY_PASTE paste )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_COPY_PASTE, "TREE_COPY_PASTE")
                , root_1)

                self._adaptor.addChild(root_1, stream_paste.nextTree())

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
    # grammar/ShyCopypasterFrontend.g:46:1: paste : REPLACE paste_replace WITH paste_with -> ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        retval = self.paste_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REPLACE29 = None
        WITH31 = None
        paste_replace30 = None

        paste_with32 = None


        REPLACE29_tree = None
        WITH31_tree = None
        stream_REPLACE = RewriteRuleTokenStream(self._adaptor, "token REPLACE")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_paste_with = RewriteRuleSubtreeStream(self._adaptor, "rule paste_with")
        stream_paste_replace = RewriteRuleSubtreeStream(self._adaptor, "rule paste_replace")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:47:5: ( REPLACE paste_replace WITH paste_with -> ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterFrontend.g:47:9: REPLACE paste_replace WITH paste_with
                pass 
                REPLACE29 = self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_paste296) 
                stream_REPLACE.add(REPLACE29)


                self._state.following.append(self.FOLLOW_paste_replace_in_paste298)
                paste_replace30 = self.paste_replace()

                self._state.following.pop()
                stream_paste_replace.add(paste_replace30.tree)


                WITH31 = self.match(self.input, WITH, self.FOLLOW_WITH_in_paste300) 
                stream_WITH.add(WITH31)


                self._state.following.append(self.FOLLOW_paste_with_in_paste302)
                paste_with32 = self.paste_with()

                self._state.following.pop()
                stream_paste_with.add(paste_with32.tree)


                # AST Rewrite
                # elements: paste_with, paste_replace
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
                # 48:9: -> ^( TREE_PASTE paste_replace paste_with )
                # grammar/ShyCopypasterFrontend.g:48:12: ^( TREE_PASTE paste_replace paste_with )
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
    # grammar/ShyCopypasterFrontend.g:51:1: paste_replace : ID -> ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        retval = self.paste_replace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID33 = None

        ID33_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:52:5: ( ID -> ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterFrontend.g:52:9: ID
                pass 
                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace341) 
                stream_ID.add(ID33)


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
                # 52:12: -> ^( TREE_PASTE_REPLACE ID )
                # grammar/ShyCopypasterFrontend.g:52:15: ^( TREE_PASTE_REPLACE ID )
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
    # grammar/ShyCopypasterFrontend.g:55:1: paste_with : ( ( arbitrary_token )+ NEWLINE -> ^( TREE_PASTE_WITH ( arbitrary_token )+ ) | NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ^( TREE_PASTE_WITH ( pure_block )+ ) );
    def paste_with(self, ):
        retval = self.paste_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE35 = None
        NEWLINE36 = None
        INDENT37 = None
        NEWLINE38 = None
        DEDENT40 = None
        NEWLINE41 = None
        arbitrary_token34 = None

        pure_block39 = None


        NEWLINE35_tree = None
        NEWLINE36_tree = None
        INDENT37_tree = None
        NEWLINE38_tree = None
        DEDENT40_tree = None
        NEWLINE41_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_arbitrary_token = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_token")
        stream_pure_block = RewriteRuleSubtreeStream(self._adaptor, "rule pure_block")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:56:5: ( ( arbitrary_token )+ NEWLINE -> ^( TREE_PASTE_WITH ( arbitrary_token )+ ) | NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ^( TREE_PASTE_WITH ( pure_block )+ ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == CONSTS or (CURLY_CLOSE <= LA14_0 <= CURLY_OPEN) or (DIVIDE <= LA14_0 <= ID) or (MINUS <= LA14_0 <= MODULE) or LA14_0 == NUMBER or (TYPES <= LA14_0 <= UNDERSCORE)) :
                    alt14 = 1
                elif (LA14_0 == NEWLINE) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyCopypasterFrontend.g:56:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    # grammar/ShyCopypasterFrontend.g:56:9: ( arbitrary_token )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == CONSTS or (CURLY_CLOSE <= LA12_0 <= CURLY_OPEN) or (DIVIDE <= LA12_0 <= ID) or (MINUS <= LA12_0 <= MODULE) or LA12_0 == NUMBER or (TYPES <= LA12_0 <= UNDERSCORE)) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyCopypasterFrontend.g:56:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_paste_with370)
                            arbitrary_token34 = self.arbitrary_token()

                            self._state.following.pop()
                            stream_arbitrary_token.add(arbitrary_token34.tree)



                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    NEWLINE35 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with374) 
                    stream_NEWLINE.add(NEWLINE35)


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
                    # 57:9: -> ^( TREE_PASTE_WITH ( arbitrary_token )+ )
                    # grammar/ShyCopypasterFrontend.g:57:12: ^( TREE_PASTE_WITH ( arbitrary_token )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                    , root_1)

                    # grammar/ShyCopypasterFrontend.g:57:31: ( arbitrary_token )+
                    if not (stream_arbitrary_token.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_token.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_token.nextTree())


                    stream_arbitrary_token.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt14 == 2:
                    # grammar/ShyCopypasterFrontend.g:58:9: NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE
                    pass 
                    NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with405) 
                    stream_NEWLINE.add(NEWLINE36)


                    INDENT37 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_paste_with407) 
                    stream_INDENT.add(INDENT37)


                    NEWLINE38 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with409) 
                    stream_NEWLINE.add(NEWLINE38)


                    # grammar/ShyCopypasterFrontend.g:58:32: ( pure_block )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == CONSTS or (CURLY_CLOSE <= LA13_0 <= CURLY_OPEN) or (DIVIDE <= LA13_0 <= MODULE) or LA13_0 == NUMBER or (TYPES <= LA13_0 <= UNDERSCORE)) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyCopypasterFrontend.g:58:32: pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_paste_with411)
                            pure_block39 = self.pure_block()

                            self._state.following.pop()
                            stream_pure_block.add(pure_block39.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    DEDENT40 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_paste_with415) 
                    stream_DEDENT.add(DEDENT40)


                    NEWLINE41 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with417) 
                    stream_NEWLINE.add(NEWLINE41)


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
                    # 59:9: -> ^( TREE_PASTE_WITH ( pure_block )+ )
                    # grammar/ShyCopypasterFrontend.g:59:12: ^( TREE_PASTE_WITH ( pure_block )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                    , root_1)

                    # grammar/ShyCopypasterFrontend.g:59:31: ( pure_block )+
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
    # grammar/ShyCopypasterFrontend.g:62:1: arbitrary_token : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        retval = self.arbitrary_token_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set42 = None

        set42_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:63:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                # grammar/ShyCopypasterFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set42 = self.input.LT(1)

                if self.input.LA(1) == CONSTS or (CURLY_CLOSE <= self.input.LA(1) <= CURLY_OPEN) or (DIVIDE <= self.input.LA(1) <= ID) or (MINUS <= self.input.LA(1) <= MODULE) or self.input.LA(1) == NUMBER or (TYPES <= self.input.LA(1) <= UNDERSCORE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set42))

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



 

    FOLLOW_block_in_start80 = frozenset([1, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_arbitrary_token_in_block97 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_block101 = frozenset([1])
    FOLLOW_INDENT_in_block111 = frozenset([15])
    FOLLOW_NEWLINE_in_block113 = frozenset([4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_block_in_block115 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_block119 = frozenset([15])
    FOLLOW_NEWLINE_in_block121 = frozenset([1])
    FOLLOW_COPY_in_block131 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_copy_body_in_block133 = frozenset([17])
    FOLLOW_copy_paste_in_block135 = frozenset([1, 17])
    FOLLOW_arbitrary_token_in_pure_block171 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_pure_block175 = frozenset([1])
    FOLLOW_INDENT_in_pure_block185 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block187 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_pure_block189 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_pure_block193 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block195 = frozenset([1])
    FOLLOW_NEWLINE_in_copy_body214 = frozenset([12])
    FOLLOW_INDENT_in_copy_body216 = frozenset([15])
    FOLLOW_NEWLINE_in_copy_body218 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_copy_body220 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_copy_body224 = frozenset([15])
    FOLLOW_NEWLINE_in_copy_body226 = frozenset([1])
    FOLLOW_arbitrary_token_in_copy_body242 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_copy_body246 = frozenset([1])
    FOLLOW_PASTE_in_copy_paste265 = frozenset([18])
    FOLLOW_paste_in_copy_paste267 = frozenset([1])
    FOLLOW_REPLACE_in_paste296 = frozenset([11])
    FOLLOW_paste_replace_in_paste298 = frozenset([40])
    FOLLOW_WITH_in_paste300 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_paste_with_in_paste302 = frozenset([1])
    FOLLOW_ID_in_paste_replace341 = frozenset([1])
    FOLLOW_arbitrary_token_in_paste_with370 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_paste_with374 = frozenset([1])
    FOLLOW_NEWLINE_in_paste_with405 = frozenset([12])
    FOLLOW_INDENT_in_paste_with407 = frozenset([15])
    FOLLOW_NEWLINE_in_paste_with409 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_paste_with411 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_paste_with415 = frozenset([15])
    FOLLOW_NEWLINE_in_paste_with417 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyCopypasterFrontendLexer", ShyCopypasterFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
