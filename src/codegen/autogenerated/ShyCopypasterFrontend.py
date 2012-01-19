# $ANTLR 3.4 grammar/ShyCopypasterFrontend.g 2012-01-19 19:44:54

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
    # grammar/ShyCopypasterFrontend.g:26:1: block : ( pure_block | COPY copy_body ( paste )+ -> ^( TREE_COPY copy_body ( paste )+ ) );
    def block(self, ):
        retval = self.block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COPY3 = None
        pure_block2 = None

        copy_body4 = None

        paste5 = None


        COPY3_tree = None
        stream_COPY = RewriteRuleTokenStream(self._adaptor, "token COPY")
        stream_copy_body = RewriteRuleSubtreeStream(self._adaptor, "rule copy_body")
        stream_paste = RewriteRuleSubtreeStream(self._adaptor, "rule paste")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:27:5: ( pure_block | COPY copy_body ( paste )+ -> ^( TREE_COPY copy_body ( paste )+ ) )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == CONSTS or (CURLY_CLOSE <= LA3_0 <= CURLY_OPEN) or (DIVIDE <= LA3_0 <= MODULE) or LA3_0 == NUMBER or (TYPES <= LA3_0 <= UNDERSCORE)) :
                    alt3 = 1
                elif (LA3_0 == COPY) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyCopypasterFrontend.g:27:9: pure_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_pure_block_in_block97)
                    pure_block2 = self.pure_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, pure_block2.tree)



                elif alt3 == 2:
                    # grammar/ShyCopypasterFrontend.g:28:9: COPY copy_body ( paste )+
                    pass 
                    COPY3 = self.match(self.input, COPY, self.FOLLOW_COPY_in_block107) 
                    stream_COPY.add(COPY3)


                    self._state.following.append(self.FOLLOW_copy_body_in_block109)
                    copy_body4 = self.copy_body()

                    self._state.following.pop()
                    stream_copy_body.add(copy_body4.tree)


                    # grammar/ShyCopypasterFrontend.g:28:24: ( paste )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == PASTE) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyCopypasterFrontend.g:28:24: paste
                            pass 
                            self._state.following.append(self.FOLLOW_paste_in_block111)
                            paste5 = self.paste()

                            self._state.following.pop()
                            stream_paste.add(paste5.tree)



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    # AST Rewrite
                    # elements: copy_body, paste
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
                    # 28:32: -> ^( TREE_COPY copy_body ( paste )+ )
                    # grammar/ShyCopypasterFrontend.g:28:35: ^( TREE_COPY copy_body ( paste )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_COPY, "TREE_COPY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_copy_body.nextTree())

                    # grammar/ShyCopypasterFrontend.g:28:58: ( paste )+
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

    # $ANTLR end "block"


    class copy_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.copy_body_return, self).__init__()

            self.tree = None





    # $ANTLR start "copy_body"
    # grammar/ShyCopypasterFrontend.g:31:1: copy_body : NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ( pure_block )+ ;
    def copy_body(self, ):
        retval = self.copy_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE6 = None
        INDENT7 = None
        NEWLINE8 = None
        DEDENT10 = None
        NEWLINE11 = None
        pure_block9 = None


        NEWLINE6_tree = None
        INDENT7_tree = None
        NEWLINE8_tree = None
        DEDENT10_tree = None
        NEWLINE11_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_pure_block = RewriteRuleSubtreeStream(self._adaptor, "rule pure_block")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:32:5: ( NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE -> ( pure_block )+ )
                # grammar/ShyCopypasterFrontend.g:32:9: NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE
                pass 
                NEWLINE6 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_body147) 
                stream_NEWLINE.add(NEWLINE6)


                INDENT7 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_copy_body149) 
                stream_INDENT.add(INDENT7)


                NEWLINE8 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_body151) 
                stream_NEWLINE.add(NEWLINE8)


                # grammar/ShyCopypasterFrontend.g:32:32: ( pure_block )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == CONSTS or (CURLY_CLOSE <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= MODULE) or LA4_0 == NUMBER or (TYPES <= LA4_0 <= UNDERSCORE)) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyCopypasterFrontend.g:32:32: pure_block
                        pass 
                        self._state.following.append(self.FOLLOW_pure_block_in_copy_body153)
                        pure_block9 = self.pure_block()

                        self._state.following.pop()
                        stream_pure_block.add(pure_block9.tree)



                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                DEDENT10 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_copy_body157) 
                stream_DEDENT.add(DEDENT10)


                NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_body159) 
                stream_NEWLINE.add(NEWLINE11)


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
                # 32:60: -> ( pure_block )+
                # grammar/ShyCopypasterFrontend.g:32:63: ( pure_block )+
                if not (stream_pure_block.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_pure_block.hasNext():
                    self._adaptor.addChild(root_0, stream_pure_block.nextTree())


                stream_pure_block.reset()




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

    # $ANTLR end "copy_body"


    class paste_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.paste_return, self).__init__()

            self.tree = None





    # $ANTLR start "paste"
    # grammar/ShyCopypasterFrontend.g:35:1: paste : PASTE REPLACE paste_replace WITH paste_with -> ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        retval = self.paste_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PASTE12 = None
        REPLACE13 = None
        WITH15 = None
        paste_replace14 = None

        paste_with16 = None


        PASTE12_tree = None
        REPLACE13_tree = None
        WITH15_tree = None
        stream_PASTE = RewriteRuleTokenStream(self._adaptor, "token PASTE")
        stream_REPLACE = RewriteRuleTokenStream(self._adaptor, "token REPLACE")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_paste_with = RewriteRuleSubtreeStream(self._adaptor, "rule paste_with")
        stream_paste_replace = RewriteRuleSubtreeStream(self._adaptor, "rule paste_replace")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:36:5: ( PASTE REPLACE paste_replace WITH paste_with -> ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterFrontend.g:36:9: PASTE REPLACE paste_replace WITH paste_with
                pass 
                PASTE12 = self.match(self.input, PASTE, self.FOLLOW_PASTE_in_paste184) 
                stream_PASTE.add(PASTE12)


                REPLACE13 = self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_paste186) 
                stream_REPLACE.add(REPLACE13)


                self._state.following.append(self.FOLLOW_paste_replace_in_paste188)
                paste_replace14 = self.paste_replace()

                self._state.following.pop()
                stream_paste_replace.add(paste_replace14.tree)


                WITH15 = self.match(self.input, WITH, self.FOLLOW_WITH_in_paste190) 
                stream_WITH.add(WITH15)


                self._state.following.append(self.FOLLOW_paste_with_in_paste192)
                paste_with16 = self.paste_with()

                self._state.following.pop()
                stream_paste_with.add(paste_with16.tree)


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
                # 37:9: -> ^( TREE_PASTE paste_replace paste_with )
                # grammar/ShyCopypasterFrontend.g:37:12: ^( TREE_PASTE paste_replace paste_with )
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


    class pure_block_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.pure_block_return, self).__init__()

            self.tree = None





    # $ANTLR start "pure_block"
    # grammar/ShyCopypasterFrontend.g:40:1: pure_block : ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE );
    def pure_block(self, ):
        retval = self.pure_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE18 = None
        INDENT19 = None
        NEWLINE20 = None
        DEDENT22 = None
        NEWLINE23 = None
        arbitrary_token17 = None

        pure_block21 = None


        NEWLINE18_tree = None
        INDENT19_tree = None
        NEWLINE20_tree = None
        DEDENT22_tree = None
        NEWLINE23_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:41:5: ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == CONSTS or (CURLY_CLOSE <= LA7_0 <= CURLY_OPEN) or (DIVIDE <= LA7_0 <= ID) or (MINUS <= LA7_0 <= MODULE) or LA7_0 == NUMBER or (TYPES <= LA7_0 <= UNDERSCORE)) :
                    alt7 = 1
                elif (LA7_0 == INDENT) :
                    alt7 = 2
                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammar/ShyCopypasterFrontend.g:41:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    # grammar/ShyCopypasterFrontend.g:41:9: ( arbitrary_token )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == CONSTS or (CURLY_CLOSE <= LA5_0 <= CURLY_OPEN) or (DIVIDE <= LA5_0 <= ID) or (MINUS <= LA5_0 <= MODULE) or LA5_0 == NUMBER or (TYPES <= LA5_0 <= UNDERSCORE)) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammar/ShyCopypasterFrontend.g:41:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_pure_block231)
                            arbitrary_token17 = self.arbitrary_token()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, arbitrary_token17.tree)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block235)
                    NEWLINE18_tree = self._adaptor.createWithPayload(NEWLINE18)
                    self._adaptor.addChild(root_0, NEWLINE18_tree)




                elif alt7 == 2:
                    # grammar/ShyCopypasterFrontend.g:42:9: INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    INDENT19 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_pure_block245)
                    INDENT19_tree = self._adaptor.createWithPayload(INDENT19)
                    self._adaptor.addChild(root_0, INDENT19_tree)



                    NEWLINE20 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block247)
                    NEWLINE20_tree = self._adaptor.createWithPayload(NEWLINE20)
                    self._adaptor.addChild(root_0, NEWLINE20_tree)



                    # grammar/ShyCopypasterFrontend.g:42:24: ( pure_block )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == CONSTS or (CURLY_CLOSE <= LA6_0 <= CURLY_OPEN) or (DIVIDE <= LA6_0 <= MODULE) or LA6_0 == NUMBER or (TYPES <= LA6_0 <= UNDERSCORE)) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyCopypasterFrontend.g:42:24: pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_pure_block249)
                            pure_block21 = self.pure_block()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, pure_block21.tree)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT22 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_pure_block253)
                    DEDENT22_tree = self._adaptor.createWithPayload(DEDENT22)
                    self._adaptor.addChild(root_0, DEDENT22_tree)



                    NEWLINE23 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block255)
                    NEWLINE23_tree = self._adaptor.createWithPayload(NEWLINE23)
                    self._adaptor.addChild(root_0, NEWLINE23_tree)




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


    class paste_replace_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.paste_replace_return, self).__init__()

            self.tree = None





    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterFrontend.g:45:1: paste_replace : ID -> ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        retval = self.paste_replace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID24 = None

        ID24_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:46:5: ( ID -> ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterFrontend.g:46:9: ID
                pass 
                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace274) 
                stream_ID.add(ID24)


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
                # 46:12: -> ^( TREE_PASTE_REPLACE ID )
                # grammar/ShyCopypasterFrontend.g:46:15: ^( TREE_PASTE_REPLACE ID )
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
    # grammar/ShyCopypasterFrontend.g:49:1: paste_with : ( arbitrary_token )+ NEWLINE -> ^( TREE_PASTE_WITH ( arbitrary_token )+ ) ;
    def paste_with(self, ):
        retval = self.paste_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE26 = None
        arbitrary_token25 = None


        NEWLINE26_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_arbitrary_token = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_token")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:50:5: ( ( arbitrary_token )+ NEWLINE -> ^( TREE_PASTE_WITH ( arbitrary_token )+ ) )
                # grammar/ShyCopypasterFrontend.g:50:9: ( arbitrary_token )+ NEWLINE
                pass 
                # grammar/ShyCopypasterFrontend.g:50:9: ( arbitrary_token )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == CONSTS or (CURLY_CLOSE <= LA8_0 <= CURLY_OPEN) or (DIVIDE <= LA8_0 <= ID) or (MINUS <= LA8_0 <= MODULE) or LA8_0 == NUMBER or (TYPES <= LA8_0 <= UNDERSCORE)) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyCopypasterFrontend.g:50:9: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_paste_with303)
                        arbitrary_token25 = self.arbitrary_token()

                        self._state.following.pop()
                        stream_arbitrary_token.add(arbitrary_token25.tree)



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                NEWLINE26 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with307) 
                stream_NEWLINE.add(NEWLINE26)


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
                # 50:35: -> ^( TREE_PASTE_WITH ( arbitrary_token )+ )
                # grammar/ShyCopypasterFrontend.g:50:38: ^( TREE_PASTE_WITH ( arbitrary_token )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                , root_1)

                # grammar/ShyCopypasterFrontend.g:50:57: ( arbitrary_token )+
                if not (stream_arbitrary_token.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_arbitrary_token.hasNext():
                    self._adaptor.addChild(root_1, stream_arbitrary_token.nextTree())


                stream_arbitrary_token.reset()

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
    # grammar/ShyCopypasterFrontend.g:53:1: arbitrary_token : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        retval = self.arbitrary_token_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set27 = None

        set27_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:54:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                # grammar/ShyCopypasterFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set27 = self.input.LT(1)

                if self.input.LA(1) == CONSTS or (CURLY_CLOSE <= self.input.LA(1) <= CURLY_OPEN) or (DIVIDE <= self.input.LA(1) <= ID) or (MINUS <= self.input.LA(1) <= MODULE) or self.input.LA(1) == NUMBER or (TYPES <= self.input.LA(1) <= UNDERSCORE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set27))

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
    FOLLOW_pure_block_in_block97 = frozenset([1])
    FOLLOW_COPY_in_block107 = frozenset([15])
    FOLLOW_copy_body_in_block109 = frozenset([17])
    FOLLOW_paste_in_block111 = frozenset([1, 17])
    FOLLOW_NEWLINE_in_copy_body147 = frozenset([12])
    FOLLOW_INDENT_in_copy_body149 = frozenset([15])
    FOLLOW_NEWLINE_in_copy_body151 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_copy_body153 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_copy_body157 = frozenset([15])
    FOLLOW_NEWLINE_in_copy_body159 = frozenset([1])
    FOLLOW_PASTE_in_paste184 = frozenset([18])
    FOLLOW_REPLACE_in_paste186 = frozenset([11])
    FOLLOW_paste_replace_in_paste188 = frozenset([40])
    FOLLOW_WITH_in_paste190 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 16, 37, 38])
    FOLLOW_paste_with_in_paste192 = frozenset([1])
    FOLLOW_arbitrary_token_in_pure_block231 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_pure_block235 = frozenset([1])
    FOLLOW_INDENT_in_pure_block245 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block247 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_pure_block249 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_pure_block253 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block255 = frozenset([1])
    FOLLOW_ID_in_paste_replace274 = frozenset([1])
    FOLLOW_arbitrary_token_in_paste_with303 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_paste_with307 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyCopypasterFrontendLexer", ShyCopypasterFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
