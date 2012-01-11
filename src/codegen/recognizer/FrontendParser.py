# $ANTLR 3.4 grammar/Frontend.g 2012-01-11 20:50:10

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
CONSTS=4
DEDENT=5
ID=6
INDENT=7
MODULE=8
NUMBER=9
WHITESPACE=10

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "ID", "INDENT", "MODULE", "NUMBER", "WHITESPACE"
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

                    if (LA1_0 == MODULE) :
                        alt1 = 1
                    elif (LA1_0 == CONSTS) :
                        alt1 = 2


                    if alt1 == 1:
                        # grammar/Frontend.g:36:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start102)
                        module1 = self.module()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, module1.tree)



                    elif alt1 == 2:
                        # grammar/Frontend.g:36:20: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start106)
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
    # grammar/Frontend.g:37:1: module : MODULE ID -> ^( MODULE ID ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE3 = None
        ID4 = None

        MODULE3_tree = None
        ID4_tree = None
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/Frontend.g:37:8: ( MODULE ID -> ^( MODULE ID ) )
                # grammar/Frontend.g:37:10: MODULE ID
                pass 
                MODULE3 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module118) 
                stream_MODULE.add(MODULE3)


                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_module120) 
                stream_ID.add(ID4)


                # AST Rewrite
                # elements: ID, MODULE
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
                # 37:20: -> ^( MODULE ID )
                # grammar/Frontend.g:37:23: ^( MODULE ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_MODULE.nextNode()
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
    # grammar/Frontend.g:38:1: consts : CONSTS ID INDENT consts_values DEDENT -> ^( CONSTS ID consts_values ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS5 = None
        ID6 = None
        INDENT7 = None
        DEDENT9 = None
        consts_values8 = None


        CONSTS5_tree = None
        ID6_tree = None
        INDENT7_tree = None
        DEDENT9_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_values = RewriteRuleSubtreeStream(self._adaptor, "rule consts_values")
        try:
            try:
                # grammar/Frontend.g:38:8: ( CONSTS ID INDENT consts_values DEDENT -> ^( CONSTS ID consts_values ) )
                # grammar/Frontend.g:38:10: CONSTS ID INDENT consts_values DEDENT
                pass 
                CONSTS5 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts138) 
                stream_CONSTS.add(CONSTS5)


                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_consts140) 
                stream_ID.add(ID6)


                INDENT7 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts142) 
                stream_INDENT.add(INDENT7)


                self._state.following.append(self.FOLLOW_consts_values_in_consts144)
                consts_values8 = self.consts_values()

                self._state.following.pop()
                stream_consts_values.add(consts_values8.tree)


                DEDENT9 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts146) 
                stream_DEDENT.add(DEDENT9)


                # AST Rewrite
                # elements: ID, CONSTS, consts_values
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
                # 38:48: -> ^( CONSTS ID consts_values )
                # grammar/Frontend.g:38:51: ^( CONSTS ID consts_values )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_CONSTS.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_consts_values.nextTree())

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


    class consts_values_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.consts_values_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_values"
    # grammar/Frontend.g:40:1: consts_values : ( consts_value )+ ;
    def consts_values(self, ):
        retval = self.consts_values_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_value10 = None



        try:
            try:
                # grammar/Frontend.g:40:15: ( ( consts_value )+ )
                # grammar/Frontend.g:40:17: ( consts_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:40:17: ( consts_value )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/Frontend.g:40:17: consts_value
                        pass 
                        self._state.following.append(self.FOLLOW_consts_value_in_consts_values173)
                        consts_value10 = self.consts_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_value10.tree)



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

    # $ANTLR end "consts_values"


    class consts_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.consts_value_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_value"
    # grammar/Frontend.g:41:1: consts_value : ID NUMBER -> ^( ID NUMBER ) ;
    def consts_value(self, ):
        retval = self.consts_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID11 = None
        NUMBER12 = None

        ID11_tree = None
        NUMBER12_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_NUMBER = RewriteRuleTokenStream(self._adaptor, "token NUMBER")

        try:
            try:
                # grammar/Frontend.g:41:14: ( ID NUMBER -> ^( ID NUMBER ) )
                # grammar/Frontend.g:41:16: ID NUMBER
                pass 
                ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value183) 
                stream_ID.add(ID11)


                NUMBER12 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_consts_value185) 
                stream_NUMBER.add(NUMBER12)


                # AST Rewrite
                # elements: ID, NUMBER
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
                # 41:26: -> ^( ID NUMBER )
                # grammar/Frontend.g:41:29: ^( ID NUMBER )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_NUMBER.nextNode()
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

    # $ANTLR end "consts_value"



 

    FOLLOW_module_in_start102 = frozenset([1, 4, 8])
    FOLLOW_consts_in_start106 = frozenset([1, 4, 8])
    FOLLOW_MODULE_in_module118 = frozenset([6])
    FOLLOW_ID_in_module120 = frozenset([1])
    FOLLOW_CONSTS_in_consts138 = frozenset([6])
    FOLLOW_ID_in_consts140 = frozenset([7])
    FOLLOW_INDENT_in_consts142 = frozenset([6])
    FOLLOW_consts_values_in_consts144 = frozenset([5])
    FOLLOW_DEDENT_in_consts146 = frozenset([1])
    FOLLOW_consts_value_in_consts_values173 = frozenset([1, 6])
    FOLLOW_ID_in_consts_value183 = frozenset([9])
    FOLLOW_NUMBER_in_consts_value185 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
