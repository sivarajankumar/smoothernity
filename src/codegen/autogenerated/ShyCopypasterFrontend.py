# $ANTLR 3.4 grammar/ShyCopypasterFrontend.g 2012-01-19 19:33:50

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
    # grammar/ShyCopypasterFrontend.g:26:1: block : ( pure_block | COPY NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE ( PASTE REPLACE paste_replace WITH paste_with )+ -> ^( TREE_COPY ( pure_block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ ) );
    def block(self, ):
        retval = self.block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COPY3 = None
        NEWLINE4 = None
        INDENT5 = None
        NEWLINE6 = None
        DEDENT8 = None
        NEWLINE9 = None
        PASTE10 = None
        REPLACE11 = None
        WITH13 = None
        pure_block2 = None

        pure_block7 = None

        paste_replace12 = None

        paste_with14 = None


        COPY3_tree = None
        NEWLINE4_tree = None
        INDENT5_tree = None
        NEWLINE6_tree = None
        DEDENT8_tree = None
        NEWLINE9_tree = None
        PASTE10_tree = None
        REPLACE11_tree = None
        WITH13_tree = None
        stream_PASTE = RewriteRuleTokenStream(self._adaptor, "token PASTE")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_COPY = RewriteRuleTokenStream(self._adaptor, "token COPY")
        stream_REPLACE = RewriteRuleTokenStream(self._adaptor, "token REPLACE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_paste_with = RewriteRuleSubtreeStream(self._adaptor, "rule paste_with")
        stream_paste_replace = RewriteRuleSubtreeStream(self._adaptor, "rule paste_replace")
        stream_pure_block = RewriteRuleSubtreeStream(self._adaptor, "rule pure_block")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:27:5: ( pure_block | COPY NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE ( PASTE REPLACE paste_replace WITH paste_with )+ -> ^( TREE_COPY ( pure_block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ ) )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == CONSTS or (CURLY_CLOSE <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= MODULE) or LA4_0 == NUMBER or (TYPES <= LA4_0 <= UNDERSCORE)) :
                    alt4 = 1
                elif (LA4_0 == COPY) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # grammar/ShyCopypasterFrontend.g:27:9: pure_block
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_pure_block_in_block97)
                    pure_block2 = self.pure_block()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, pure_block2.tree)



                elif alt4 == 2:
                    # grammar/ShyCopypasterFrontend.g:28:9: COPY NEWLINE INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE ( PASTE REPLACE paste_replace WITH paste_with )+
                    pass 
                    COPY3 = self.match(self.input, COPY, self.FOLLOW_COPY_in_block107) 
                    stream_COPY.add(COPY3)


                    NEWLINE4 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block109) 
                    stream_NEWLINE.add(NEWLINE4)


                    INDENT5 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_block111) 
                    stream_INDENT.add(INDENT5)


                    NEWLINE6 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block113) 
                    stream_NEWLINE.add(NEWLINE6)


                    # grammar/ShyCopypasterFrontend.g:28:37: ( pure_block )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= CURLY_OPEN) or (DIVIDE <= LA2_0 <= MODULE) or LA2_0 == NUMBER or (TYPES <= LA2_0 <= UNDERSCORE)) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyCopypasterFrontend.g:28:37: pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_block115)
                            pure_block7 = self.pure_block()

                            self._state.following.pop()
                            stream_pure_block.add(pure_block7.tree)



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    DEDENT8 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_block119) 
                    stream_DEDENT.add(DEDENT8)


                    NEWLINE9 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block121) 
                    stream_NEWLINE.add(NEWLINE9)


                    # grammar/ShyCopypasterFrontend.g:29:9: ( PASTE REPLACE paste_replace WITH paste_with )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == PASTE) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammar/ShyCopypasterFrontend.g:29:11: PASTE REPLACE paste_replace WITH paste_with
                            pass 
                            PASTE10 = self.match(self.input, PASTE, self.FOLLOW_PASTE_in_block133) 
                            stream_PASTE.add(PASTE10)


                            REPLACE11 = self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_block135) 
                            stream_REPLACE.add(REPLACE11)


                            self._state.following.append(self.FOLLOW_paste_replace_in_block137)
                            paste_replace12 = self.paste_replace()

                            self._state.following.pop()
                            stream_paste_replace.add(paste_replace12.tree)


                            WITH13 = self.match(self.input, WITH, self.FOLLOW_WITH_in_block139) 
                            stream_WITH.add(WITH13)


                            self._state.following.append(self.FOLLOW_paste_with_in_block141)
                            paste_with14 = self.paste_with()

                            self._state.following.pop()
                            stream_paste_with.add(paste_with14.tree)



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    # AST Rewrite
                    # elements: paste_replace, paste_with, pure_block
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
                    # 30:9: -> ^( TREE_COPY ( pure_block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ )
                    # grammar/ShyCopypasterFrontend.g:31:13: ^( TREE_COPY ( pure_block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_COPY, "TREE_COPY")
                    , root_1)

                    # grammar/ShyCopypasterFrontend.g:31:26: ( pure_block )+
                    if not (stream_pure_block.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_pure_block.hasNext():
                        self._adaptor.addChild(root_1, stream_pure_block.nextTree())


                    stream_pure_block.reset()

                    # grammar/ShyCopypasterFrontend.g:32:17: ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+
                    if not (stream_paste_replace.hasNext() or stream_paste_with.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_paste_replace.hasNext() or stream_paste_with.hasNext():
                        # grammar/ShyCopypasterFrontend.g:32:17: ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_PASTE, "TREE_PASTE")
                        , root_2)

                        # grammar/ShyCopypasterFrontend.g:33:21: ^( TREE_PASTE_REPLACE paste_replace )
                        root_3 = self._adaptor.nil()
                        root_3 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_PASTE_REPLACE, "TREE_PASTE_REPLACE")
                        , root_3)

                        self._adaptor.addChild(root_3, stream_paste_replace.nextTree())

                        self._adaptor.addChild(root_2, root_3)

                        # grammar/ShyCopypasterFrontend.g:34:21: ^( TREE_PASTE_WITH paste_with )
                        root_3 = self._adaptor.nil()
                        root_3 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                        , root_3)

                        self._adaptor.addChild(root_3, stream_paste_with.nextTree())

                        self._adaptor.addChild(root_2, root_3)

                        self._adaptor.addChild(root_1, root_2)


                    stream_paste_replace.reset()
                    stream_paste_with.reset()

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
    # grammar/ShyCopypasterFrontend.g:39:1: pure_block : ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE );
    def pure_block(self, ):
        retval = self.pure_block_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE16 = None
        INDENT17 = None
        NEWLINE18 = None
        DEDENT20 = None
        NEWLINE21 = None
        arbitrary_token15 = None

        pure_block19 = None


        NEWLINE16_tree = None
        INDENT17_tree = None
        NEWLINE18_tree = None
        DEDENT20_tree = None
        NEWLINE21_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:40:5: ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE )
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
                    # grammar/ShyCopypasterFrontend.g:40:9: ( arbitrary_token )+ NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    # grammar/ShyCopypasterFrontend.g:40:9: ( arbitrary_token )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == CONSTS or (CURLY_CLOSE <= LA5_0 <= CURLY_OPEN) or (DIVIDE <= LA5_0 <= ID) or (MINUS <= LA5_0 <= MODULE) or LA5_0 == NUMBER or (TYPES <= LA5_0 <= UNDERSCORE)) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammar/ShyCopypasterFrontend.g:40:9: arbitrary_token
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_token_in_pure_block305)
                            arbitrary_token15 = self.arbitrary_token()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, arbitrary_token15.tree)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    NEWLINE16 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block309)
                    NEWLINE16_tree = self._adaptor.createWithPayload(NEWLINE16)
                    self._adaptor.addChild(root_0, NEWLINE16_tree)




                elif alt7 == 2:
                    # grammar/ShyCopypasterFrontend.g:41:9: INDENT NEWLINE ( pure_block )+ DEDENT NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    INDENT17 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_pure_block319)
                    INDENT17_tree = self._adaptor.createWithPayload(INDENT17)
                    self._adaptor.addChild(root_0, INDENT17_tree)



                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block321)
                    NEWLINE18_tree = self._adaptor.createWithPayload(NEWLINE18)
                    self._adaptor.addChild(root_0, NEWLINE18_tree)



                    # grammar/ShyCopypasterFrontend.g:41:24: ( pure_block )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == CONSTS or (CURLY_CLOSE <= LA6_0 <= CURLY_OPEN) or (DIVIDE <= LA6_0 <= MODULE) or LA6_0 == NUMBER or (TYPES <= LA6_0 <= UNDERSCORE)) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyCopypasterFrontend.g:41:24: pure_block
                            pass 
                            self._state.following.append(self.FOLLOW_pure_block_in_pure_block323)
                            pure_block19 = self.pure_block()

                            self._state.following.pop()
                            self._adaptor.addChild(root_0, pure_block19.tree)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT20 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_pure_block327)
                    DEDENT20_tree = self._adaptor.createWithPayload(DEDENT20)
                    self._adaptor.addChild(root_0, DEDENT20_tree)



                    NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_pure_block329)
                    NEWLINE21_tree = self._adaptor.createWithPayload(NEWLINE21)
                    self._adaptor.addChild(root_0, NEWLINE21_tree)




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
    # grammar/ShyCopypasterFrontend.g:44:1: paste_replace : ID ;
    def paste_replace(self, ):
        retval = self.paste_replace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID22 = None

        ID22_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:44:15: ( ID )
                # grammar/ShyCopypasterFrontend.g:44:17: ID
                pass 
                root_0 = self._adaptor.nil()


                ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace342)
                ID22_tree = self._adaptor.createWithPayload(ID22)
                self._adaptor.addChild(root_0, ID22_tree)





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
    # grammar/ShyCopypasterFrontend.g:45:1: paste_with : ( arbitrary_token )+ NEWLINE -> ( arbitrary_token )+ ;
    def paste_with(self, ):
        retval = self.paste_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE24 = None
        arbitrary_token23 = None


        NEWLINE24_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_arbitrary_token = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_token")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:45:12: ( ( arbitrary_token )+ NEWLINE -> ( arbitrary_token )+ )
                # grammar/ShyCopypasterFrontend.g:45:14: ( arbitrary_token )+ NEWLINE
                pass 
                # grammar/ShyCopypasterFrontend.g:45:14: ( arbitrary_token )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == CONSTS or (CURLY_CLOSE <= LA8_0 <= CURLY_OPEN) or (DIVIDE <= LA8_0 <= ID) or (MINUS <= LA8_0 <= MODULE) or LA8_0 == NUMBER or (TYPES <= LA8_0 <= UNDERSCORE)) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyCopypasterFrontend.g:45:14: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_paste_with350)
                        arbitrary_token23 = self.arbitrary_token()

                        self._state.following.pop()
                        stream_arbitrary_token.add(arbitrary_token23.tree)



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with354) 
                stream_NEWLINE.add(NEWLINE24)


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
                # 45:40: -> ( arbitrary_token )+
                # grammar/ShyCopypasterFrontend.g:45:43: ( arbitrary_token )+
                if not (stream_arbitrary_token.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_arbitrary_token.hasNext():
                    self._adaptor.addChild(root_0, stream_arbitrary_token.nextTree())


                stream_arbitrary_token.reset()




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
    # grammar/ShyCopypasterFrontend.g:47:1: arbitrary_token : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        retval = self.arbitrary_token_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set25 = None

        set25_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:48:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                # grammar/ShyCopypasterFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set25 = self.input.LT(1)

                if self.input.LA(1) == CONSTS or (CURLY_CLOSE <= self.input.LA(1) <= CURLY_OPEN) or (DIVIDE <= self.input.LA(1) <= ID) or (MINUS <= self.input.LA(1) <= MODULE) or self.input.LA(1) == NUMBER or (TYPES <= self.input.LA(1) <= UNDERSCORE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set25))

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
    FOLLOW_NEWLINE_in_block109 = frozenset([12])
    FOLLOW_INDENT_in_block111 = frozenset([15])
    FOLLOW_NEWLINE_in_block113 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_block115 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_block119 = frozenset([15])
    FOLLOW_NEWLINE_in_block121 = frozenset([17])
    FOLLOW_PASTE_in_block133 = frozenset([18])
    FOLLOW_REPLACE_in_block135 = frozenset([11])
    FOLLOW_paste_replace_in_block137 = frozenset([40])
    FOLLOW_WITH_in_block139 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 16, 37, 38])
    FOLLOW_paste_with_in_block141 = frozenset([1, 17])
    FOLLOW_arbitrary_token_in_pure_block305 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_pure_block309 = frozenset([1])
    FOLLOW_INDENT_in_pure_block319 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block321 = frozenset([4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_pure_block_in_pure_block323 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_pure_block327 = frozenset([15])
    FOLLOW_NEWLINE_in_pure_block329 = frozenset([1])
    FOLLOW_ID_in_paste_replace342 = frozenset([1])
    FOLLOW_arbitrary_token_in_paste_with350 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_paste_with354 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyCopypasterFrontendLexer", ShyCopypasterFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
