# $ANTLR 3.4 grammar/Frontend.g 2012-01-09 23:39:21

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
T__8=8
T__9=9
ID=4
NEWLINE=5
NUMBER=6
WHITESPACE=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ID", "NEWLINE", "NUMBER", "WHITESPACE", "'consts'", "'module'"
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

                    if (LA1_0 == 9) :
                        alt1 = 1
                    elif (LA1_0 == 8) :
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
        stream_9 = RewriteRuleTokenStream(self._adaptor, "token 9")

        try:
            try:
                # grammar/Frontend.g:37:8: ( 'module' ID NEWLINE -> ^( 'module' ID ) )
                # grammar/Frontend.g:37:10: 'module' ID NEWLINE
                pass 
                string_literal3 = self.match(self.input, 9, self.FOLLOW_9_in_module118) 
                stream_9.add(string_literal3)


                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_module120) 
                stream_ID.add(ID4)


                NEWLINE5 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module122) 
                stream_NEWLINE.add(NEWLINE5)


                # AST Rewrite
                # elements: 9, ID
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
                stream_9.nextNode()
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
    # grammar/Frontend.g:38:1: consts : ( 'consts' ID NEWLINE -> ^( 'consts' ID ) | 'consts' ID NEWLINE consts_values -> ^( 'consts' ID consts_values ) );
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        string_literal6 = None
        ID7 = None
        NEWLINE8 = None
        string_literal9 = None
        ID10 = None
        NEWLINE11 = None
        consts_values12 = None


        string_literal6_tree = None
        ID7_tree = None
        NEWLINE8_tree = None
        string_literal9_tree = None
        ID10_tree = None
        NEWLINE11_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_8 = RewriteRuleTokenStream(self._adaptor, "token 8")
        stream_consts_values = RewriteRuleSubtreeStream(self._adaptor, "rule consts_values")
        try:
            try:
                # grammar/Frontend.g:38:8: ( 'consts' ID NEWLINE -> ^( 'consts' ID ) | 'consts' ID NEWLINE consts_values -> ^( 'consts' ID consts_values ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 8) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == ID) :
                        LA2_2 = self.input.LA(3)

                        if (LA2_2 == NEWLINE) :
                            LA2_3 = self.input.LA(4)

                            if (LA2_3 == EOF or (8 <= LA2_3 <= 9)) :
                                alt2 = 1
                            elif (LA2_3 == ID) :
                                alt2 = 2
                            else:
                                nvae = NoViableAltException("", 2, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 2, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 2, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # grammar/Frontend.g:38:10: 'consts' ID NEWLINE
                    pass 
                    string_literal6 = self.match(self.input, 8, self.FOLLOW_8_in_consts140) 
                    stream_8.add(string_literal6)


                    ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_consts142) 
                    stream_ID.add(ID7)


                    NEWLINE8 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts144) 
                    stream_NEWLINE.add(NEWLINE8)


                    # AST Rewrite
                    # elements: ID, 8
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
                    stream_8.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt2 == 2:
                    # grammar/Frontend.g:39:10: 'consts' ID NEWLINE consts_values
                    pass 
                    string_literal9 = self.match(self.input, 8, self.FOLLOW_8_in_consts165) 
                    stream_8.add(string_literal9)


                    ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_consts167) 
                    stream_ID.add(ID10)


                    NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts169) 
                    stream_NEWLINE.add(NEWLINE11)


                    self._state.following.append(self.FOLLOW_consts_values_in_consts171)
                    consts_values12 = self.consts_values()

                    self._state.following.pop()
                    stream_consts_values.add(consts_values12.tree)


                    # AST Rewrite
                    # elements: consts_values, ID, 8
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
                    # 39:44: -> ^( 'consts' ID consts_values )
                    # grammar/Frontend.g:39:47: ^( 'consts' ID consts_values )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_8.nextNode()
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
    # grammar/Frontend.g:41:1: consts_values : ( consts_value )+ ;
    def consts_values(self, ):
        retval = self.consts_values_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_value13 = None



        try:
            try:
                # grammar/Frontend.g:41:15: ( ( consts_value )+ )
                # grammar/Frontend.g:41:17: ( consts_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:41:17: ( consts_value )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == ID) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/Frontend.g:41:17: consts_value
                        pass 
                        self._state.following.append(self.FOLLOW_consts_value_in_consts_values198)
                        consts_value13 = self.consts_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_value13.tree)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1




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
    # grammar/Frontend.g:42:1: consts_value : ID NUMBER NEWLINE -> ^( ID NUMBER ) ;
    def consts_value(self, ):
        retval = self.consts_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID14 = None
        NUMBER15 = None
        NEWLINE16 = None

        ID14_tree = None
        NUMBER15_tree = None
        NEWLINE16_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_NUMBER = RewriteRuleTokenStream(self._adaptor, "token NUMBER")

        try:
            try:
                # grammar/Frontend.g:42:14: ( ID NUMBER NEWLINE -> ^( ID NUMBER ) )
                # grammar/Frontend.g:42:16: ID NUMBER NEWLINE
                pass 
                ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_value208) 
                stream_ID.add(ID14)


                NUMBER15 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_consts_value210) 
                stream_NUMBER.add(NUMBER15)


                NEWLINE16 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_value212) 
                stream_NEWLINE.add(NEWLINE16)


                # AST Rewrite
                # elements: NUMBER, ID
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
                # 42:34: -> ^( ID NUMBER )
                # grammar/Frontend.g:42:37: ^( ID NUMBER )
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



 

    FOLLOW_module_in_start102 = frozenset([1, 8, 9])
    FOLLOW_consts_in_start106 = frozenset([1, 8, 9])
    FOLLOW_9_in_module118 = frozenset([4])
    FOLLOW_ID_in_module120 = frozenset([5])
    FOLLOW_NEWLINE_in_module122 = frozenset([1])
    FOLLOW_8_in_consts140 = frozenset([4])
    FOLLOW_ID_in_consts142 = frozenset([5])
    FOLLOW_NEWLINE_in_consts144 = frozenset([1])
    FOLLOW_8_in_consts165 = frozenset([4])
    FOLLOW_ID_in_consts167 = frozenset([5])
    FOLLOW_NEWLINE_in_consts169 = frozenset([4])
    FOLLOW_consts_values_in_consts171 = frozenset([1])
    FOLLOW_consts_value_in_consts_values198 = frozenset([1, 4])
    FOLLOW_ID_in_consts_value208 = frozenset([6])
    FOLLOW_NUMBER_in_consts_value210 = frozenset([5])
    FOLLOW_NEWLINE_in_consts_value212 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
