# $ANTLR 3.4 grammar/Frontend.g 2012-01-06 13:08:34

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



class FrontendParserException ( Exception ) :
    def __init__ ( self , text ) :
        Exception . __init__ ( self , text )



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__7=7
T__8=8
ID=4
NEWLINE=5
WHITESPACE=6

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ID", "NEWLINE", "WHITESPACE", "'consts'", "'module'"
]




class FrontendParser(Parser):
    grammarFileName = "grammar/Frontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(FrontendParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    def emitErrorMessage ( self , msg ) :
        raise FrontendParserException ( msg )


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # grammar/Frontend.g:36:1: start : ( module | consts )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        module1 = None

        consts2 = None



        try:
            try:
                # grammar/Frontend.g:36:7: ( ( module | consts )* )
                # grammar/Frontend.g:36:9: ( module | consts )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:36:9: ( module | consts )*
                while True: #loop1
                    alt1 = 3
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == 8) :
                        alt1 = 1
                    elif (LA1_0 == 7) :
                        alt1 = 2


                    if alt1 == 1:
                        # grammar/Frontend.g:36:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start90)
                        module1 = self.module()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, module1.tree)



                    elif alt1 == 2:
                        # grammar/Frontend.g:36:20: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start94)
                        consts2 = self.consts()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts2.tree)



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


    class module_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.module_return, self).__init__()

            self.tree = None





    # $ANTLR start "module"
    # grammar/Frontend.g:37:1: module : 'module' ID NEWLINE -> ^( 'module' ID ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal3 = None
        ID4 = None
        NEWLINE5 = None

        string_literal3_tree = None
        ID4_tree = None
        NEWLINE5_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_8 = RewriteRuleTokenStream(self._adaptor, "token 8")

        try:
            try:
                # grammar/Frontend.g:37:8: ( 'module' ID NEWLINE -> ^( 'module' ID ) )
                # grammar/Frontend.g:37:10: 'module' ID NEWLINE
                pass 
                string_literal3 = self.match(self.input, 8, self.FOLLOW_8_in_module106) 
                stream_8.add(string_literal3)


                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_module108) 
                stream_ID.add(ID4)


                NEWLINE5 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module110) 
                stream_NEWLINE.add(NEWLINE5)


                # AST Rewrite
                # elements: 8, ID
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
                # 37:30: -> ^( 'module' ID )
                # grammar/Frontend.g:37:33: ^( 'module' ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_8.nextNode()
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

    # $ANTLR end "module"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/Frontend.g:38:1: consts : 'consts' ID NEWLINE -> ^( 'consts' ID ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal6 = None
        ID7 = None
        NEWLINE8 = None

        string_literal6_tree = None
        ID7_tree = None
        NEWLINE8_tree = None
        stream_7 = RewriteRuleTokenStream(self._adaptor, "token 7")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/Frontend.g:38:8: ( 'consts' ID NEWLINE -> ^( 'consts' ID ) )
                # grammar/Frontend.g:38:10: 'consts' ID NEWLINE
                pass 
                string_literal6 = self.match(self.input, 7, self.FOLLOW_7_in_consts128) 
                stream_7.add(string_literal6)


                ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_consts130) 
                stream_ID.add(ID7)


                NEWLINE8 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts132) 
                stream_NEWLINE.add(NEWLINE8)


                # AST Rewrite
                # elements: ID, 7
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
                # 38:30: -> ^( 'consts' ID )
                # grammar/Frontend.g:38:33: ^( 'consts' ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_7.nextNode()
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

    # $ANTLR end "consts"



 

    FOLLOW_module_in_start90 = frozenset([1, 7, 8])
    FOLLOW_consts_in_start94 = frozenset([1, 7, 8])
    FOLLOW_8_in_module106 = frozenset([4])
    FOLLOW_ID_in_module108 = frozenset([5])
    FOLLOW_NEWLINE_in_module110 = frozenset([1])
    FOLLOW_7_in_consts128 = frozenset([4])
    FOLLOW_ID_in_consts130 = frozenset([5])
    FOLLOW_NEWLINE_in_consts132 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
