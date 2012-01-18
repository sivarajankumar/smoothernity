# $ANTLR 3.4 grammar/ShyCopypasterFrontend.g 2012-01-18 18:59:32

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

                    if (LA1_0 == CONSTS or (CURLY_CLOSE <= LA1_0 <= NUMBER) or (TYPES <= LA1_0 <= UNDERSCORE)) :
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
    # grammar/ShyCopypasterFrontend.g:13:1: chunk : arbitrary_token -> ^( TREE_ARBITRARY_TOKEN arbitrary_token ) ;
    def chunk(self, ):
        retval = self.chunk_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_token2 = None


        stream_arbitrary_token = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_token")
        try:
            try:
                # grammar/ShyCopypasterFrontend.g:14:5: ( arbitrary_token -> ^( TREE_ARBITRARY_TOKEN arbitrary_token ) )
                # grammar/ShyCopypasterFrontend.g:14:7: arbitrary_token
                pass 
                self._state.following.append(self.FOLLOW_arbitrary_token_in_chunk81)
                arbitrary_token2 = self.arbitrary_token()

                self._state.following.pop()
                stream_arbitrary_token.add(arbitrary_token2.tree)


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
                # 14:23: -> ^( TREE_ARBITRARY_TOKEN arbitrary_token )
                # grammar/ShyCopypasterFrontend.g:14:26: ^( TREE_ARBITRARY_TOKEN arbitrary_token )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_ARBITRARY_TOKEN, "TREE_ARBITRARY_TOKEN")
                , root_1)

                self._adaptor.addChild(root_1, stream_arbitrary_token.nextTree())

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

    # $ANTLR end "chunk"


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

        arbitrary_token3 = None



        try:
            try:
                # grammar/ShyCopypasterFrontend.g:40:18: ( ( arbitrary_token )+ )
                # grammar/ShyCopypasterFrontend.g:40:20: ( arbitrary_token )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyCopypasterFrontend.g:40:20: ( arbitrary_token )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == CONSTS or (CURLY_CLOSE <= LA2_0 <= NUMBER) or (TYPES <= LA2_0 <= UNDERSCORE)) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyCopypasterFrontend.g:40:20: arbitrary_token
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_token_in_arbitrary_tokens110)
                        arbitrary_token3 = self.arbitrary_token()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_token3.tree)



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1




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

        set4 = None

        set4_tree = None

        try:
            try:
                # grammar/ShyCopypasterFrontend.g:43:5: ( CONSTS | DEDENT | INDENT | MODULE | TYPES | CURLY_OPEN | CURLY_CLOSE | DIVIDE | MINUS | UNDERSCORE | NEWLINE | ID | NUMBER | EXPRESSION )
                # grammar/ShyCopypasterFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set4 = self.input.LT(1)

                if self.input.LA(1) == CONSTS or (CURLY_CLOSE <= self.input.LA(1) <= NUMBER) or (TYPES <= self.input.LA(1) <= UNDERSCORE):
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set4))

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



 

    FOLLOW_chunk_in_start66 = frozenset([1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 37, 38])
    FOLLOW_arbitrary_token_in_chunk81 = frozenset([1])
    FOLLOW_arbitrary_token_in_arbitrary_tokens110 = frozenset([1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 37, 38])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyCopypasterFrontendLexer", ShyCopypasterFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
