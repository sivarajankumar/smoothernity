# $ANTLR 3.4 grammar/ShyCopypasterFrontend.g 2012-01-19 17:25:03

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
    # grammar/ShyCopypasterFrontend.g:26:1: block : ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( block )+ DEDENT NEWLINE | COPY NEWLINE INDENT NEWLINE ( block )+ DEDENT NEWLINE ( PASTE REPLACE paste_replace WITH paste_with )+ -> ^( TREE_COPY ( block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ ) );
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
        NEWLINE10 = None
        INDENT11 = None
        NEWLINE12 = None
        DEDENT14 = None
        NEWLINE15 = None
        PASTE16 = None
        REPLACE17 = None
        WITH19 = None
        arbitrary_token2 = None

        block6 = None

        block13 = None

        paste_replace18 = None

        paste_with20 = None


        NEWLINE3_tree = None
        INDENT4_tree = None
        NEWLINE5_tree = None
        DEDENT7_tree = None
        NEWLINE8_tree = None
        COPY9_tree = None
        NEWLINE10_tree = None
        INDENT11_tree = None
        NEWLINE12_tree = None
        DEDENT14_tree = None
        NEWLINE15_tree = None
        PASTE16_tree = None
        REPLACE17_tree = None
        WITH19_tree = None
        stream_PASTE = RewriteRuleTokenStream(self._adaptor, "token PASTE")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_COPY = RewriteRuleTokenStream(self._adaptor, "token COPY")
        stream_REPLACE = RewriteRuleTokenStream(self._adaptor, "token REPLACE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_paste_with = RewriteRuleSubtreeStream(self._adaptor, "rule paste_with")
        stream_block = RewriteRuleSubtreeStream(self._adaptor, "rule block")
        stream_paste_replace = RewriteRuleSubtreeStream(self._adaptor, "rule paste_replace")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:27:5: ( ( arbitrary_token )+ NEWLINE | INDENT NEWLINE ( block )+ DEDENT NEWLINE | COPY NEWLINE INDENT NEWLINE ( block )+ DEDENT NEWLINE ( PASTE REPLACE paste_replace WITH paste_with )+ -> ^( TREE_COPY ( block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ ) )
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == CONSTS or LA6 == CURLY_CLOSE or LA6 == CURLY_OPEN or LA6 == DIVIDE or LA6 == EXPRESSION or LA6 == ID or LA6 == MINUS or LA6 == MODULE or LA6 == NUMBER or LA6 == TYPES or LA6 == UNDERSCORE:
                    alt6 = 1
                elif LA6 == INDENT:
                    alt6 = 2
                elif LA6 == COPY:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
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




                elif alt6 == 2:
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




                elif alt6 == 3:
                    # grammar/ShyCopypasterFrontend.g:29:9: COPY NEWLINE INDENT NEWLINE ( block )+ DEDENT NEWLINE ( PASTE REPLACE paste_replace WITH paste_with )+
                    pass 
                    COPY9 = self.match(self.input, COPY, self.FOLLOW_COPY_in_block131) 
                    stream_COPY.add(COPY9)


                    NEWLINE10 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block133) 
                    stream_NEWLINE.add(NEWLINE10)


                    INDENT11 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_block135) 
                    stream_INDENT.add(INDENT11)


                    NEWLINE12 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block137) 
                    stream_NEWLINE.add(NEWLINE12)


                    # grammar/ShyCopypasterFrontend.g:29:37: ( block )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if ((CONSTS <= LA4_0 <= CURLY_OPEN) or (DIVIDE <= LA4_0 <= MODULE) or LA4_0 == NUMBER or (TYPES <= LA4_0 <= UNDERSCORE)) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammar/ShyCopypasterFrontend.g:29:37: block
                            pass 
                            self._state.following.append(self.FOLLOW_block_in_block139)
                            block13 = self.block()

                            self._state.following.pop()
                            stream_block.add(block13.tree)



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    DEDENT14 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_block143) 
                    stream_DEDENT.add(DEDENT14)


                    NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_block145) 
                    stream_NEWLINE.add(NEWLINE15)


                    # grammar/ShyCopypasterFrontend.g:30:9: ( PASTE REPLACE paste_replace WITH paste_with )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == PASTE) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammar/ShyCopypasterFrontend.g:30:11: PASTE REPLACE paste_replace WITH paste_with
                            pass 
                            PASTE16 = self.match(self.input, PASTE, self.FOLLOW_PASTE_in_block157) 
                            stream_PASTE.add(PASTE16)


                            REPLACE17 = self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_block159) 
                            stream_REPLACE.add(REPLACE17)


                            self._state.following.append(self.FOLLOW_paste_replace_in_block161)
                            paste_replace18 = self.paste_replace()

                            self._state.following.pop()
                            stream_paste_replace.add(paste_replace18.tree)


                            WITH19 = self.match(self.input, WITH, self.FOLLOW_WITH_in_block163) 
                            stream_WITH.add(WITH19)


                            self._state.following.append(self.FOLLOW_paste_with_in_block165)
                            paste_with20 = self.paste_with()

                            self._state.following.pop()
                            stream_paste_with.add(paste_with20.tree)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    # AST Rewrite
                    # elements: paste_with, block, paste_replace
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
                    # 31:9: -> ^( TREE_COPY ( block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ )
                    # grammar/ShyCopypasterFrontend.g:32:13: ^( TREE_COPY ( block )+ ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_COPY, "TREE_COPY")
                    , root_1)

                    # grammar/ShyCopypasterFrontend.g:32:26: ( block )+
                    if not (stream_block.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_block.hasNext():
                        self._adaptor.addChild(root_1, stream_block.nextTree())


                    stream_block.reset()

                    # grammar/ShyCopypasterFrontend.g:33:17: ( ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) ) )+
                    if not (stream_paste_with.hasNext() or stream_paste_replace.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_paste_with.hasNext() or stream_paste_replace.hasNext():
                        # grammar/ShyCopypasterFrontend.g:33:17: ^( TREE_PASTE ^( TREE_PASTE_REPLACE paste_replace ) ^( TREE_PASTE_WITH paste_with ) )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_PASTE, "TREE_PASTE")
                        , root_2)

                        # grammar/ShyCopypasterFrontend.g:34:21: ^( TREE_PASTE_REPLACE paste_replace )
                        root_3 = self._adaptor.nil()
                        root_3 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_PASTE_REPLACE, "TREE_PASTE_REPLACE")
                        , root_3)

                        self._adaptor.addChild(root_3, stream_paste_replace.nextTree())

                        self._adaptor.addChild(root_2, root_3)

                        # grammar/ShyCopypasterFrontend.g:35:21: ^( TREE_PASTE_WITH paste_with )
                        root_3 = self._adaptor.nil()
                        root_3 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                        , root_3)

                        self._adaptor.addChild(root_3, stream_paste_with.nextTree())

                        self._adaptor.addChild(root_2, root_3)

                        self._adaptor.addChild(root_1, root_2)


                    stream_paste_with.reset()
                    stream_paste_replace.reset()

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


    class paste_replace_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.paste_replace_return, self).__init__()

            self.tree = None





    # $ANTLR start "paste_replace"
    # grammar/ShyCopypasterFrontend.g:40:1: paste_replace : ID ;
    def paste_replace(self, ):
        retval = self.paste_replace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID21 = None

        ID21_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:40:15: ( ID )
                # grammar/ShyCopypasterFrontend.g:40:17: ID
                pass 
                root_0 = self._adaptor.nil()


                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace323)
                ID21_tree = self._adaptor.createWithPayload(ID21)
                self._adaptor.addChild(root_0, ID21_tree)





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
    # grammar/ShyCopypasterFrontend.g:41:1: paste_with : ( arbitrary_token )+ NEWLINE -> ( arbitrary_token )+ ;
    def paste_with(self, ):
        retval = self.paste_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE23 = None
        arbitrary_token22 = None


        NEWLINE23_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_arbitrary_token = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_token")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:41:12: ( ( arbitrary_token )+ NEWLINE -> ( arbitrary_token )+ )
                # grammar/ShyCopypasterFrontend.g:41:14: ( arbitrary_token )+ NEWLINE
                pass 
                # grammar/ShyCopypasterFrontend.g:41:14: ( arbitrary_token )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == CONSTS or (CURLY_CLOSE <= LA7_0 <= CURLY_OPEN) or (DIVIDE <= LA7_0 <= ID) or (MINUS <= LA7_0 <= MODULE) or LA7_0 == NUMBER or (TYPES <= LA7_0 <= UNDERSCORE)) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyCopypasterFrontend.g:41:14: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_paste_with331)
                        arbitrary_token22 = self.arbitrary_token()

                        self._state.following.pop()
                        stream_arbitrary_token.add(arbitrary_token22.tree)



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1


                NEWLINE23 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste_with335) 
                stream_NEWLINE.add(NEWLINE23)


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
                # 41:40: -> ( arbitrary_token )+
                # grammar/ShyCopypasterFrontend.g:41:43: ( arbitrary_token )+
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
    # grammar/ShyCopypasterFrontend.g:43:1: arbitrary_token : ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        retval = self.arbitrary_token_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set24 = None

        set24_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:44:5: ( CONSTS | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | ID | NUMBER | EXPRESSION )
                # grammar/ShyCopypasterFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set24 = self.input.LT(1)

                if self.input.LA(1) == CONSTS or (CURLY_CLOSE <= self.input.LA(1) <= CURLY_OPEN) or (DIVIDE <= self.input.LA(1) <= ID) or (MINUS <= self.input.LA(1) <= MODULE) or self.input.LA(1) == NUMBER or (TYPES <= self.input.LA(1) <= UNDERSCORE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set24))

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
    FOLLOW_COPY_in_block131 = frozenset([15])
    FOLLOW_NEWLINE_in_block133 = frozenset([12])
    FOLLOW_INDENT_in_block135 = frozenset([15])
    FOLLOW_NEWLINE_in_block137 = frozenset([4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_block_in_block139 = frozenset([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 37, 38])
    FOLLOW_DEDENT_in_block143 = frozenset([15])
    FOLLOW_NEWLINE_in_block145 = frozenset([17])
    FOLLOW_PASTE_in_block157 = frozenset([18])
    FOLLOW_REPLACE_in_block159 = frozenset([11])
    FOLLOW_paste_replace_in_block161 = frozenset([40])
    FOLLOW_WITH_in_block163 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 16, 37, 38])
    FOLLOW_paste_with_in_block165 = frozenset([1, 17])
    FOLLOW_ID_in_paste_replace323 = frozenset([1])
    FOLLOW_arbitrary_token_in_paste_with331 = frozenset([4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 37, 38])
    FOLLOW_NEWLINE_in_paste_with335 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyCopypasterFrontendLexer", ShyCopypasterFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
