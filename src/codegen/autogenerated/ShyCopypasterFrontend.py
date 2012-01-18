# $ANTLR 3.4 grammar/ShyCopypasterFrontend.g 2012-01-18 18:43:01

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




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


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # grammar/ShyCopypasterFrontend.g:11:1: start : ( chunk )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        chunk1 = None



        try:
            try:
                # grammar/ShyCopypasterFrontend.g:11:7: ( ( chunk )* )
                # grammar/ShyCopypasterFrontend.g:11:9: ( chunk )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyCopypasterFrontend.g:11:9: ( chunk )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((CONSTS <= LA1_0 <= NUMBER) or (TYPES <= LA1_0 <= UNDERSCORE)) :
                        alt1 = 1


                    if alt1 == 1:
                        # grammar/ShyCopypasterFrontend.g:11:9: chunk
                        pass 
                        self._state.following.append(self.FOLLOW_chunk_in_start66)
                        chunk1 = self.chunk()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, chunk1.tree)



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


    class chunk_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.chunk_return, self).__init__()

            self.tree = None





    # $ANTLR start "chunk"
    # grammar/ShyCopypasterFrontend.g:13:1: chunk : ( arbitrary_tokens -> ^( TREE_ARBITRARY_TOKEN arbitrary_tokens ) | copy_paste );
    def chunk(self, ):
        retval = self.chunk_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_tokens2 = None

        copy_paste3 = None


        stream_arbitrary_tokens = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_tokens")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:14:5: ( arbitrary_tokens -> ^( TREE_ARBITRARY_TOKEN arbitrary_tokens ) | copy_paste )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= NUMBER) or (TYPES <= LA2_0 <= UNDERSCORE)) :
                    alt2 = 1
                elif (LA2_0 == COPY) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # grammar/ShyCopypasterFrontend.g:14:7: arbitrary_tokens
                    pass 
                    self._state.following.append(self.FOLLOW_arbitrary_tokens_in_chunk81)
                    arbitrary_tokens2 = self.arbitrary_tokens()

                    self._state.following.pop()
                    stream_arbitrary_tokens.add(arbitrary_tokens2.tree)


                    # AST Rewrite
                    # elements: arbitrary_tokens
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
                    # 14:24: -> ^( TREE_ARBITRARY_TOKEN arbitrary_tokens )
                    # grammar/ShyCopypasterFrontend.g:14:27: ^( TREE_ARBITRARY_TOKEN arbitrary_tokens )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ARBITRARY_TOKEN, "TREE_ARBITRARY_TOKEN")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_arbitrary_tokens.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt2 == 2:
                    # grammar/ShyCopypasterFrontend.g:15:7: copy_paste
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_copy_paste_in_chunk99)
                    copy_paste3 = self.copy_paste()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, copy_paste3.tree)



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

    # $ANTLR end "chunk"


    class copy_paste_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.copy_paste_return, self).__init__()

            self.tree = None





    # $ANTLR start "copy_paste"
    # grammar/ShyCopypasterFrontend.g:18:1: copy_paste : COPY NEWLINE INDENT NEWLINE copy DEDENT NEWLINE ( paste )+ -> ^( TREE_COPY_PASTE copy ( paste )+ ) ;
    def copy_paste(self, ):
        retval = self.copy_paste_return()
        retval.start = self.input.LT(1)


        root_0 = None

        COPY4 = None
        NEWLINE5 = None
        INDENT6 = None
        NEWLINE7 = None
        DEDENT9 = None
        NEWLINE10 = None
        copy8 = None

        paste11 = None


        COPY4_tree = None
        NEWLINE5_tree = None
        INDENT6_tree = None
        NEWLINE7_tree = None
        DEDENT9_tree = None
        NEWLINE10_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_COPY = RewriteRuleTokenStream(self._adaptor, "token COPY")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_paste = RewriteRuleSubtreeStream(self._adaptor, "rule paste")
        stream_copy = RewriteRuleSubtreeStream(self._adaptor, "rule copy")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:19:5: ( COPY NEWLINE INDENT NEWLINE copy DEDENT NEWLINE ( paste )+ -> ^( TREE_COPY_PASTE copy ( paste )+ ) )
                # grammar/ShyCopypasterFrontend.g:19:7: COPY NEWLINE INDENT NEWLINE copy DEDENT NEWLINE ( paste )+
                pass 
                COPY4 = self.match(self.input, COPY, self.FOLLOW_COPY_in_copy_paste116) 
                stream_COPY.add(COPY4)


                NEWLINE5 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_paste118) 
                stream_NEWLINE.add(NEWLINE5)


                INDENT6 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_copy_paste120) 
                stream_INDENT.add(INDENT6)


                NEWLINE7 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_paste122) 
                stream_NEWLINE.add(NEWLINE7)


                self._state.following.append(self.FOLLOW_copy_in_copy_paste124)
                copy8 = self.copy()

                self._state.following.pop()
                stream_copy.add(copy8.tree)


                DEDENT9 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_copy_paste126) 
                stream_DEDENT.add(DEDENT9)


                NEWLINE10 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_copy_paste128) 
                stream_NEWLINE.add(NEWLINE10)


                # grammar/ShyCopypasterFrontend.g:19:55: ( paste )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == REPLACE) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyCopypasterFrontend.g:19:55: paste
                        pass 
                        self._state.following.append(self.FOLLOW_paste_in_copy_paste130)
                        paste11 = self.paste()

                        self._state.following.pop()
                        stream_paste.add(paste11.tree)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1


                # AST Rewrite
                # elements: paste, copy
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
                # 20:9: -> ^( TREE_COPY_PASTE copy ( paste )+ )
                # grammar/ShyCopypasterFrontend.g:20:12: ^( TREE_COPY_PASTE copy ( paste )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_COPY_PASTE, "TREE_COPY_PASTE")
                , root_1)

                self._adaptor.addChild(root_1, stream_copy.nextTree())

                # grammar/ShyCopypasterFrontend.g:20:36: ( paste )+
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


    class copy_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.copy_return, self).__init__()

            self.tree = None





    # $ANTLR start "copy"
    # grammar/ShyCopypasterFrontend.g:23:1: copy : arbitrary_tokens -> ^( TREE_COPY arbitrary_tokens ) ;
    def copy(self, ):
        retval = self.copy_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_tokens12 = None


        stream_arbitrary_tokens = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_tokens")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:24:5: ( arbitrary_tokens -> ^( TREE_COPY arbitrary_tokens ) )
                # grammar/ShyCopypasterFrontend.g:24:7: arbitrary_tokens
                pass 
                self._state.following.append(self.FOLLOW_arbitrary_tokens_in_copy172)
                arbitrary_tokens12 = self.arbitrary_tokens()

                self._state.following.pop()
                stream_arbitrary_tokens.add(arbitrary_tokens12.tree)


                # AST Rewrite
                # elements: arbitrary_tokens
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
                # 24:24: -> ^( TREE_COPY arbitrary_tokens )
                # grammar/ShyCopypasterFrontend.g:24:27: ^( TREE_COPY arbitrary_tokens )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_COPY, "TREE_COPY")
                , root_1)

                self._adaptor.addChild(root_1, stream_arbitrary_tokens.nextTree())

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

    # $ANTLR end "copy"


    class paste_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.paste_return, self).__init__()

            self.tree = None





    # $ANTLR start "paste"
    # grammar/ShyCopypasterFrontend.g:27:1: paste : REPLACE paste_replace WITH paste_with NEWLINE -> ^( TREE_PASTE paste_replace paste_with ) ;
    def paste(self, ):
        retval = self.paste_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REPLACE13 = None
        WITH15 = None
        NEWLINE17 = None
        paste_replace14 = None

        paste_with16 = None


        REPLACE13_tree = None
        WITH15_tree = None
        NEWLINE17_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_REPLACE = RewriteRuleTokenStream(self._adaptor, "token REPLACE")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_paste_with = RewriteRuleSubtreeStream(self._adaptor, "rule paste_with")
        stream_paste_replace = RewriteRuleSubtreeStream(self._adaptor, "rule paste_replace")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:28:5: ( REPLACE paste_replace WITH paste_with NEWLINE -> ^( TREE_PASTE paste_replace paste_with ) )
                # grammar/ShyCopypasterFrontend.g:28:7: REPLACE paste_replace WITH paste_with NEWLINE
                pass 
                REPLACE13 = self.match(self.input, REPLACE, self.FOLLOW_REPLACE_in_paste199) 
                stream_REPLACE.add(REPLACE13)


                self._state.following.append(self.FOLLOW_paste_replace_in_paste201)
                paste_replace14 = self.paste_replace()

                self._state.following.pop()
                stream_paste_replace.add(paste_replace14.tree)


                WITH15 = self.match(self.input, WITH, self.FOLLOW_WITH_in_paste203) 
                stream_WITH.add(WITH15)


                self._state.following.append(self.FOLLOW_paste_with_in_paste205)
                paste_with16 = self.paste_with()

                self._state.following.pop()
                stream_paste_with.add(paste_with16.tree)


                NEWLINE17 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_paste207) 
                stream_NEWLINE.add(NEWLINE17)


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
                # 29:9: -> ^( TREE_PASTE paste_replace paste_with )
                # grammar/ShyCopypasterFrontend.g:29:12: ^( TREE_PASTE paste_replace paste_with )
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
    # grammar/ShyCopypasterFrontend.g:32:1: paste_replace : ID -> ^( TREE_PASTE_REPLACE ID ) ;
    def paste_replace(self, ):
        retval = self.paste_replace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID18 = None

        ID18_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:33:5: ( ID -> ^( TREE_PASTE_REPLACE ID ) )
                # grammar/ShyCopypasterFrontend.g:33:7: ID
                pass 
                ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_paste_replace244) 
                stream_ID.add(ID18)


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
                # 33:10: -> ^( TREE_PASTE_REPLACE ID )
                # grammar/ShyCopypasterFrontend.g:33:13: ^( TREE_PASTE_REPLACE ID )
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
    # grammar/ShyCopypasterFrontend.g:36:1: paste_with : arbitrary_tokens -> ^( TREE_PASTE_WITH arbitrary_tokens ) ;
    def paste_with(self, ):
        retval = self.paste_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_tokens19 = None


        stream_arbitrary_tokens = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_tokens")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:37:5: ( arbitrary_tokens -> ^( TREE_PASTE_WITH arbitrary_tokens ) )
                # grammar/ShyCopypasterFrontend.g:37:7: arbitrary_tokens
                pass 
                self._state.following.append(self.FOLLOW_arbitrary_tokens_in_paste_with271)
                arbitrary_tokens19 = self.arbitrary_tokens()

                self._state.following.pop()
                stream_arbitrary_tokens.add(arbitrary_tokens19.tree)


                # AST Rewrite
                # elements: arbitrary_tokens
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
                # 37:24: -> ^( TREE_PASTE_WITH arbitrary_tokens )
                # grammar/ShyCopypasterFrontend.g:37:27: ^( TREE_PASTE_WITH arbitrary_tokens )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PASTE_WITH, "TREE_PASTE_WITH")
                , root_1)

                self._adaptor.addChild(root_1, stream_arbitrary_tokens.nextTree())

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


    class arbitrary_tokens_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.arbitrary_tokens_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_tokens"
    # grammar/ShyCopypasterFrontend.g:40:1: arbitrary_tokens : ( arbitrary_token )+ ;
    def arbitrary_tokens(self, ):
        retval = self.arbitrary_tokens_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_token20 = None



        try:
            try:
                # grammar/ShyCopypasterFrontend.g:40:18: ( ( arbitrary_token )+ )
                # grammar/ShyCopypasterFrontend.g:40:20: ( arbitrary_token )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyCopypasterFrontend.g:40:20: ( arbitrary_token )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4 = self.input.LA(1)
                    if LA4 == DEDENT:
                        alt4 = 1
                    elif LA4 == NEWLINE:
                        alt4 = 1
                    elif LA4 == CONSTS or LA4 == CURLY_CLOSE or LA4 == CURLY_OPEN or LA4 == DIVIDE or LA4 == EXPRESSION or LA4 == ID or LA4 == INDENT or LA4 == MINUS or LA4 == MODULE or LA4 == NUMBER or LA4 == TYPES or LA4 == UNDERSCORE:
                        alt4 = 1

                    if alt4 == 1:
                        # grammar/ShyCopypasterFrontend.g:40:20: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_arbitrary_tokens294)
                        arbitrary_token20 = self.arbitrary_token()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_token20.tree)



                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1




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

    # $ANTLR end "arbitrary_tokens"


    class arbitrary_token_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyCopypasterFrontend.arbitrary_token_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_token"
    # grammar/ShyCopypasterFrontend.g:42:1: arbitrary_token : ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION );
    def arbitrary_token(self, ):
        retval = self.arbitrary_token_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set21 = None

        set21_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:43:5: ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION )
                # grammar/ShyCopypasterFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set21 = self.input.LT(1)

                if self.input.LA(1) == CONSTS or (CURLY_CLOSE <= self.input.LA(1) <= NUMBER) or (TYPES <= self.input.LA(1) <= UNDERSCORE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set21))

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



 

    FOLLOW_chunk_in_start66 = frozenset([1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 37, 38])
    FOLLOW_arbitrary_tokens_in_chunk81 = frozenset([1])
    FOLLOW_copy_paste_in_chunk99 = frozenset([1])
    FOLLOW_COPY_in_copy_paste116 = frozenset([15])
    FOLLOW_NEWLINE_in_copy_paste118 = frozenset([12])
    FOLLOW_INDENT_in_copy_paste120 = frozenset([15])
    FOLLOW_NEWLINE_in_copy_paste122 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 37, 38])
    FOLLOW_copy_in_copy_paste124 = frozenset([8])
    FOLLOW_DEDENT_in_copy_paste126 = frozenset([15])
    FOLLOW_NEWLINE_in_copy_paste128 = frozenset([18])
    FOLLOW_paste_in_copy_paste130 = frozenset([1, 18])
    FOLLOW_arbitrary_tokens_in_copy172 = frozenset([1])
    FOLLOW_REPLACE_in_paste199 = frozenset([11])
    FOLLOW_paste_replace_in_paste201 = frozenset([40])
    FOLLOW_WITH_in_paste203 = frozenset([4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 37, 38])
    FOLLOW_paste_with_in_paste205 = frozenset([15])
    FOLLOW_NEWLINE_in_paste207 = frozenset([1])
    FOLLOW_ID_in_paste_replace244 = frozenset([1])
    FOLLOW_arbitrary_tokens_in_paste_with271 = frozenset([1])
    FOLLOW_arbitrary_token_in_arbitrary_tokens294 = frozenset([1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 37, 38])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyCopypasterFrontendLexer", ShyCopypasterFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
