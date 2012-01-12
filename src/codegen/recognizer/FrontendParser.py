# $ANTLR 3.4 grammar/Frontend.g 2012-01-12 19:00:29

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
DIVIDE=6
EXPRESSION=7
ID=8
INDENT=9
MINUS=10
MODULE=11
NUMBER=12
WHITESPACE=13

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NUMBER", "WHITESPACE"
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
    # grammar/Frontend.g:38:1: module : MODULE ID -> ^( MODULE ID ) ;
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
                # grammar/Frontend.g:38:8: ( MODULE ID -> ^( MODULE ID ) )
                # grammar/Frontend.g:38:10: MODULE ID
                pass 
                MODULE3 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module119) 
                stream_MODULE.add(MODULE3)


                ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_module121) 
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
                # 38:20: -> ^( MODULE ID )
                # grammar/Frontend.g:38:23: ^( MODULE ID )
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
    # grammar/Frontend.g:40:1: consts : CONSTS ID INDENT consts_items DEDENT -> ^( CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS5 = None
        ID6 = None
        INDENT7 = None
        DEDENT9 = None
        consts_items8 = None


        CONSTS5_tree = None
        ID6_tree = None
        INDENT7_tree = None
        DEDENT9_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/Frontend.g:41:5: ( CONSTS ID INDENT consts_items DEDENT -> ^( CONSTS ID consts_items ) )
                # grammar/Frontend.g:41:7: CONSTS ID INDENT consts_items DEDENT
                pass 
                CONSTS5 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts144) 
                stream_CONSTS.add(CONSTS5)


                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_consts146) 
                stream_ID.add(ID6)


                INDENT7 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts148) 
                stream_INDENT.add(INDENT7)


                self._state.following.append(self.FOLLOW_consts_items_in_consts150)
                consts_items8 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items8.tree)


                DEDENT9 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts152) 
                stream_DEDENT.add(DEDENT9)


                # AST Rewrite
                # elements: CONSTS, ID, consts_items
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
                # 41:44: -> ^( CONSTS ID consts_items )
                # grammar/Frontend.g:41:47: ^( CONSTS ID consts_items )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_CONSTS.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_consts_items.nextTree())

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


    class consts_items_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.consts_items_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_items"
    # grammar/Frontend.g:43:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item10 = None



        try:
            try:
                # grammar/Frontend.g:43:14: ( ( consts_item )+ )
                # grammar/Frontend.g:43:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:43:16: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/Frontend.g:43:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items176)
                        consts_item10 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item10.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/Frontend.g:44:1: consts_item : ( ID num_whole -> ^( ID num_whole ) | ID num_fract -> ^( ID num_fract ) | ID EXPRESSION -> ^( ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID11 = None
        ID13 = None
        ID15 = None
        EXPRESSION16 = None
        num_whole12 = None

        num_fract14 = None


        ID11_tree = None
        ID13_tree = None
        ID15_tree = None
        EXPRESSION16_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/Frontend.g:45:5: ( ID num_whole -> ^( ID num_whole ) | ID num_fract -> ^( ID num_fract ) | ID EXPRESSION -> ^( ID EXPRESSION ) )
                alt3 = 3
                LA3_0 = self.input.LA(1)

                if (LA3_0 == ID) :
                    LA3 = self.input.LA(2)
                    if LA3 == EXPRESSION:
                        alt3 = 3
                    elif LA3 == MINUS:
                        LA3_3 = self.input.LA(3)

                        if (LA3_3 == NUMBER) :
                            LA3_4 = self.input.LA(4)

                            if (LA3_4 == DIVIDE) :
                                alt3 = 2
                            elif (LA3_4 == DEDENT or LA3_4 == ID) :
                                alt3 = 1
                            else:
                                nvae = NoViableAltException("", 3, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 3, 3, self.input)

                            raise nvae


                    elif LA3 == NUMBER:
                        LA3_4 = self.input.LA(3)

                        if (LA3_4 == DIVIDE) :
                            alt3 = 2
                        elif (LA3_4 == DEDENT or LA3_4 == ID) :
                            alt3 = 1
                        else:
                            nvae = NoViableAltException("", 3, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/Frontend.g:45:7: ID num_whole
                    pass 
                    ID11 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item190) 
                    stream_ID.add(ID11)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item192)
                    num_whole12 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole12.tree)


                    # AST Rewrite
                    # elements: ID, num_whole
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
                    # 45:20: -> ^( ID num_whole )
                    # grammar/Frontend.g:45:23: ^( ID num_whole )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_ID.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_num_whole.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 2:
                    # grammar/Frontend.g:46:7: ID num_fract
                    pass 
                    ID13 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item210) 
                    stream_ID.add(ID13)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item212)
                    num_fract14 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract14.tree)


                    # AST Rewrite
                    # elements: num_fract, ID
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
                    # 46:20: -> ^( ID num_fract )
                    # grammar/Frontend.g:46:23: ^( ID num_fract )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_ID.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_num_fract.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 3:
                    # grammar/Frontend.g:47:7: ID EXPRESSION
                    pass 
                    ID15 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item230) 
                    stream_ID.add(ID15)


                    EXPRESSION16 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item232) 
                    stream_EXPRESSION.add(EXPRESSION16)


                    # AST Rewrite
                    # elements: EXPRESSION, ID
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
                    # 47:21: -> ^( ID EXPRESSION )
                    # grammar/Frontend.g:47:24: ^( ID EXPRESSION )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_ID.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_EXPRESSION.nextNode()
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

    # $ANTLR end "consts_item"


    class num_whole_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.num_whole_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_whole"
    # grammar/Frontend.g:50:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS17 = None
        NUMBER18 = None

        MINUS17_tree = None
        NUMBER18_tree = None

        try:
            try:
                # grammar/Frontend.g:50:11: ( ( MINUS )? NUMBER )
                # grammar/Frontend.g:50:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:50:13: ( MINUS )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == MINUS) :
                    alt4 = 1
                if alt4 == 1:
                    # grammar/Frontend.g:50:13: MINUS
                    pass 
                    MINUS17 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole255)
                    MINUS17_tree = self._adaptor.createWithPayload(MINUS17)
                    self._adaptor.addChild(root_0, MINUS17_tree)






                NUMBER18 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole259)
                NUMBER18_tree = self._adaptor.createWithPayload(NUMBER18)
                self._adaptor.addChild(root_0, NUMBER18_tree)





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

    # $ANTLR end "num_whole"


    class num_fract_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.num_fract_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_fract"
    # grammar/Frontend.g:51:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS19 = None
        NUMBER20 = None
        DIVIDE21 = None
        NUMBER22 = None

        MINUS19_tree = None
        NUMBER20_tree = None
        DIVIDE21_tree = None
        NUMBER22_tree = None

        try:
            try:
                # grammar/Frontend.g:51:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/Frontend.g:51:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:51:13: ( MINUS )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == MINUS) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/Frontend.g:51:13: MINUS
                    pass 
                    MINUS19 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract267)
                    MINUS19_tree = self._adaptor.createWithPayload(MINUS19)
                    self._adaptor.addChild(root_0, MINUS19_tree)






                NUMBER20 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract271)
                NUMBER20_tree = self._adaptor.createWithPayload(NUMBER20)
                self._adaptor.addChild(root_0, NUMBER20_tree)



                DIVIDE21 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract273)
                DIVIDE21_tree = self._adaptor.createWithPayload(DIVIDE21)
                self._adaptor.addChild(root_0, DIVIDE21_tree)



                NUMBER22 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract275)
                NUMBER22_tree = self._adaptor.createWithPayload(NUMBER22)
                self._adaptor.addChild(root_0, NUMBER22_tree)





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

    # $ANTLR end "num_fract"



 

    FOLLOW_module_in_start102 = frozenset([1, 4, 11])
    FOLLOW_consts_in_start106 = frozenset([1, 4, 11])
    FOLLOW_MODULE_in_module119 = frozenset([8])
    FOLLOW_ID_in_module121 = frozenset([1])
    FOLLOW_CONSTS_in_consts144 = frozenset([8])
    FOLLOW_ID_in_consts146 = frozenset([9])
    FOLLOW_INDENT_in_consts148 = frozenset([8])
    FOLLOW_consts_items_in_consts150 = frozenset([5])
    FOLLOW_DEDENT_in_consts152 = frozenset([1])
    FOLLOW_consts_item_in_consts_items176 = frozenset([1, 8])
    FOLLOW_ID_in_consts_item190 = frozenset([10, 12])
    FOLLOW_num_whole_in_consts_item192 = frozenset([1])
    FOLLOW_ID_in_consts_item210 = frozenset([10, 12])
    FOLLOW_num_fract_in_consts_item212 = frozenset([1])
    FOLLOW_ID_in_consts_item230 = frozenset([7])
    FOLLOW_EXPRESSION_in_consts_item232 = frozenset([1])
    FOLLOW_MINUS_in_num_whole255 = frozenset([12])
    FOLLOW_NUMBER_in_num_whole259 = frozenset([1])
    FOLLOW_MINUS_in_num_fract267 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract271 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract273 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract275 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
