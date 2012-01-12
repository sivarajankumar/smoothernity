# $ANTLR 3.4 grammar/Frontend.g 2012-01-12 19:14:24

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
TYPES=13
WHITESPACE=14

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NUMBER", "TYPES", "WHITESPACE"
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
    # grammar/Frontend.g:36:1: start : ( module | consts | types )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        module1 = None

        consts2 = None

        types3 = None



        try:
            try:
                # grammar/Frontend.g:36:7: ( ( module | consts | types )* )
                # grammar/Frontend.g:36:9: ( module | consts | types )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:36:9: ( module | consts | types )*
                while True: #loop1
                    alt1 = 4
                    LA1 = self.input.LA(1)
                    if LA1 == MODULE:
                        alt1 = 1
                    elif LA1 == CONSTS:
                        alt1 = 2
                    elif LA1 == TYPES:
                        alt1 = 3

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



                    elif alt1 == 3:
                        # grammar/Frontend.g:36:29: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start110)
                        types3 = self.types()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types3.tree)



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

        MODULE4 = None
        ID5 = None

        MODULE4_tree = None
        ID5_tree = None
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/Frontend.g:38:8: ( MODULE ID -> ^( MODULE ID ) )
                # grammar/Frontend.g:38:10: MODULE ID
                pass 
                MODULE4 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module123) 
                stream_MODULE.add(MODULE4)


                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_module125) 
                stream_ID.add(ID5)


                # AST Rewrite
                # elements: MODULE, ID
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

        CONSTS6 = None
        ID7 = None
        INDENT8 = None
        DEDENT10 = None
        consts_items9 = None


        CONSTS6_tree = None
        ID7_tree = None
        INDENT8_tree = None
        DEDENT10_tree = None
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
                CONSTS6 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts148) 
                stream_CONSTS.add(CONSTS6)


                ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_consts150) 
                stream_ID.add(ID7)


                INDENT8 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts152) 
                stream_INDENT.add(INDENT8)


                self._state.following.append(self.FOLLOW_consts_items_in_consts154)
                consts_items9 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items9.tree)


                DEDENT10 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts156) 
                stream_DEDENT.add(DEDENT10)


                # AST Rewrite
                # elements: ID, CONSTS, consts_items
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

        consts_item11 = None



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
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items180)
                        consts_item11 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item11.tree)



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

        ID12 = None
        ID14 = None
        ID16 = None
        EXPRESSION17 = None
        num_whole13 = None

        num_fract15 = None


        ID12_tree = None
        ID14_tree = None
        ID16_tree = None
        EXPRESSION17_tree = None
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
                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item194) 
                    stream_ID.add(ID12)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item196)
                    num_whole13 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole13.tree)


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
                    ID14 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item214) 
                    stream_ID.add(ID14)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item216)
                    num_fract15 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract15.tree)


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
                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item234) 
                    stream_ID.add(ID16)


                    EXPRESSION17 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item236) 
                    stream_EXPRESSION.add(EXPRESSION17)


                    # AST Rewrite
                    # elements: ID, EXPRESSION
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


    class types_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.types_return, self).__init__()

            self.tree = None





    # $ANTLR start "types"
    # grammar/Frontend.g:50:1: types : TYPES ID INDENT types_items DEDENT -> ^( TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES18 = None
        ID19 = None
        INDENT20 = None
        DEDENT22 = None
        types_items21 = None


        TYPES18_tree = None
        ID19_tree = None
        INDENT20_tree = None
        DEDENT22_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/Frontend.g:50:7: ( TYPES ID INDENT types_items DEDENT -> ^( TYPES ID types_items ) )
                # grammar/Frontend.g:50:9: TYPES ID INDENT types_items DEDENT
                pass 
                TYPES18 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types259) 
                stream_TYPES.add(TYPES18)


                ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_types261) 
                stream_ID.add(ID19)


                INDENT20 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types263) 
                stream_INDENT.add(INDENT20)


                self._state.following.append(self.FOLLOW_types_items_in_types265)
                types_items21 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items21.tree)


                DEDENT22 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types267) 
                stream_DEDENT.add(DEDENT22)


                # AST Rewrite
                # elements: TYPES, types_items, ID
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
                # 50:44: -> ^( TYPES ID types_items )
                # grammar/Frontend.g:50:47: ^( TYPES ID types_items )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_TYPES.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_types_items.nextTree())

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

    # $ANTLR end "types"


    class types_items_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.types_items_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_items"
    # grammar/Frontend.g:51:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item23 = None



        try:
            try:
                # grammar/Frontend.g:51:13: ( ( types_item )+ )
                # grammar/Frontend.g:51:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:51:15: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/Frontend.g:51:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items287)
                        types_item23 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item23.tree)



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

    # $ANTLR end "types_items"


    class types_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.types_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item"
    # grammar/Frontend.g:52:1: types_item : ID INDENT types_item_attrs DEDENT -> ^( ID types_item_attrs ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID24 = None
        INDENT25 = None
        DEDENT27 = None
        types_item_attrs26 = None


        ID24_tree = None
        INDENT25_tree = None
        DEDENT27_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item_attrs = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_attrs")
        try:
            try:
                # grammar/Frontend.g:52:12: ( ID INDENT types_item_attrs DEDENT -> ^( ID types_item_attrs ) )
                # grammar/Frontend.g:52:14: ID INDENT types_item_attrs DEDENT
                pass 
                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item297) 
                stream_ID.add(ID24)


                INDENT25 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item299) 
                stream_INDENT.add(INDENT25)


                self._state.following.append(self.FOLLOW_types_item_attrs_in_types_item301)
                types_item_attrs26 = self.types_item_attrs()

                self._state.following.pop()
                stream_types_item_attrs.add(types_item_attrs26.tree)


                DEDENT27 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item303) 
                stream_DEDENT.add(DEDENT27)


                # AST Rewrite
                # elements: types_item_attrs, ID
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
                # 52:48: -> ^( ID types_item_attrs )
                # grammar/Frontend.g:52:51: ^( ID types_item_attrs )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                stream_ID.nextNode()
                , root_1)

                self._adaptor.addChild(root_1, stream_types_item_attrs.nextTree())

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

    # $ANTLR end "types_item"


    class types_item_attrs_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.types_item_attrs_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item_attrs"
    # grammar/Frontend.g:53:1: types_item_attrs : ( types_item_attr )+ ;
    def types_item_attrs(self, ):
        retval = self.types_item_attrs_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item_attr28 = None



        try:
            try:
                # grammar/Frontend.g:53:18: ( ( types_item_attr )+ )
                # grammar/Frontend.g:53:20: ( types_item_attr )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:53:20: ( types_item_attr )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == ID) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/Frontend.g:53:20: types_item_attr
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_attrs321)
                        types_item_attr28 = self.types_item_attr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item_attr28.tree)



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1




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

    # $ANTLR end "types_item_attrs"


    class types_item_attr_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.types_item_attr_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item_attr"
    # grammar/Frontend.g:54:1: types_item_attr : ID ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID29 = None

        ID29_tree = None

        try:
            try:
                # grammar/Frontend.g:54:17: ( ID )
                # grammar/Frontend.g:54:19: ID
                pass 
                root_0 = self._adaptor.nil()


                ID29 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr331)
                ID29_tree = self._adaptor.createWithPayload(ID29)
                self._adaptor.addChild(root_0, ID29_tree)





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

    # $ANTLR end "types_item_attr"


    class num_whole_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.num_whole_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_whole"
    # grammar/Frontend.g:56:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS30 = None
        NUMBER31 = None

        MINUS30_tree = None
        NUMBER31_tree = None

        try:
            try:
                # grammar/Frontend.g:56:11: ( ( MINUS )? NUMBER )
                # grammar/Frontend.g:56:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:56:13: ( MINUS )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == MINUS) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/Frontend.g:56:13: MINUS
                    pass 
                    MINUS30 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole340)
                    MINUS30_tree = self._adaptor.createWithPayload(MINUS30)
                    self._adaptor.addChild(root_0, MINUS30_tree)






                NUMBER31 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole344)
                NUMBER31_tree = self._adaptor.createWithPayload(NUMBER31)
                self._adaptor.addChild(root_0, NUMBER31_tree)





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
    # grammar/Frontend.g:57:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS32 = None
        NUMBER33 = None
        DIVIDE34 = None
        NUMBER35 = None

        MINUS32_tree = None
        NUMBER33_tree = None
        DIVIDE34_tree = None
        NUMBER35_tree = None

        try:
            try:
                # grammar/Frontend.g:57:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/Frontend.g:57:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:57:13: ( MINUS )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == MINUS) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/Frontend.g:57:13: MINUS
                    pass 
                    MINUS32 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract352)
                    MINUS32_tree = self._adaptor.createWithPayload(MINUS32)
                    self._adaptor.addChild(root_0, MINUS32_tree)






                NUMBER33 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract356)
                NUMBER33_tree = self._adaptor.createWithPayload(NUMBER33)
                self._adaptor.addChild(root_0, NUMBER33_tree)



                DIVIDE34 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract358)
                DIVIDE34_tree = self._adaptor.createWithPayload(DIVIDE34)
                self._adaptor.addChild(root_0, DIVIDE34_tree)



                NUMBER35 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract360)
                NUMBER35_tree = self._adaptor.createWithPayload(NUMBER35)
                self._adaptor.addChild(root_0, NUMBER35_tree)





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



 

    FOLLOW_module_in_start102 = frozenset([1, 4, 11, 13])
    FOLLOW_consts_in_start106 = frozenset([1, 4, 11, 13])
    FOLLOW_types_in_start110 = frozenset([1, 4, 11, 13])
    FOLLOW_MODULE_in_module123 = frozenset([8])
    FOLLOW_ID_in_module125 = frozenset([1])
    FOLLOW_CONSTS_in_consts148 = frozenset([8])
    FOLLOW_ID_in_consts150 = frozenset([9])
    FOLLOW_INDENT_in_consts152 = frozenset([8])
    FOLLOW_consts_items_in_consts154 = frozenset([5])
    FOLLOW_DEDENT_in_consts156 = frozenset([1])
    FOLLOW_consts_item_in_consts_items180 = frozenset([1, 8])
    FOLLOW_ID_in_consts_item194 = frozenset([10, 12])
    FOLLOW_num_whole_in_consts_item196 = frozenset([1])
    FOLLOW_ID_in_consts_item214 = frozenset([10, 12])
    FOLLOW_num_fract_in_consts_item216 = frozenset([1])
    FOLLOW_ID_in_consts_item234 = frozenset([7])
    FOLLOW_EXPRESSION_in_consts_item236 = frozenset([1])
    FOLLOW_TYPES_in_types259 = frozenset([8])
    FOLLOW_ID_in_types261 = frozenset([9])
    FOLLOW_INDENT_in_types263 = frozenset([8])
    FOLLOW_types_items_in_types265 = frozenset([5])
    FOLLOW_DEDENT_in_types267 = frozenset([1])
    FOLLOW_types_item_in_types_items287 = frozenset([1, 8])
    FOLLOW_ID_in_types_item297 = frozenset([9])
    FOLLOW_INDENT_in_types_item299 = frozenset([8])
    FOLLOW_types_item_attrs_in_types_item301 = frozenset([5])
    FOLLOW_DEDENT_in_types_item303 = frozenset([1])
    FOLLOW_types_item_attr_in_types_item_attrs321 = frozenset([1, 8])
    FOLLOW_ID_in_types_item_attr331 = frozenset([1])
    FOLLOW_MINUS_in_num_whole340 = frozenset([12])
    FOLLOW_NUMBER_in_num_whole344 = frozenset([1])
    FOLLOW_MINUS_in_num_fract352 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract356 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract358 = frozenset([12])
    FOLLOW_NUMBER_in_num_fract360 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
