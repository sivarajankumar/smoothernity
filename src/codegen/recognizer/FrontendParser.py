# $ANTLR 3.4 grammar/Frontend.g 2012-01-12 19:51:52

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
NEWLINE=12
NUMBER=13
TYPES=14
WHITESPACE=15

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NEWLINE", "NUMBER", "TYPES", "WHITESPACE"
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
    # grammar/Frontend.g:38:1: module : MODULE ID NEWLINE -> ^( MODULE ID ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE4 = None
        ID5 = None
        NEWLINE6 = None

        MODULE4_tree = None
        ID5_tree = None
        NEWLINE6_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/Frontend.g:38:8: ( MODULE ID NEWLINE -> ^( MODULE ID ) )
                # grammar/Frontend.g:38:10: MODULE ID NEWLINE
                pass 
                MODULE4 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module123) 
                stream_MODULE.add(MODULE4)


                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_module125) 
                stream_ID.add(ID5)


                NEWLINE6 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module127) 
                stream_NEWLINE.add(NEWLINE6)


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
                # 38:28: -> ^( MODULE ID )
                # grammar/Frontend.g:38:31: ^( MODULE ID )
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
    # grammar/Frontend.g:40:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS7 = None
        ID8 = None
        NEWLINE9 = None
        INDENT10 = None
        NEWLINE11 = None
        DEDENT13 = None
        NEWLINE14 = None
        consts_items12 = None


        CONSTS7_tree = None
        ID8_tree = None
        NEWLINE9_tree = None
        INDENT10_tree = None
        NEWLINE11_tree = None
        DEDENT13_tree = None
        NEWLINE14_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/Frontend.g:41:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( CONSTS ID consts_items ) )
                # grammar/Frontend.g:41:7: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS7 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts150) 
                stream_CONSTS.add(CONSTS7)


                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts152) 
                stream_ID.add(ID8)


                NEWLINE9 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts154) 
                stream_NEWLINE.add(NEWLINE9)


                INDENT10 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts156) 
                stream_INDENT.add(INDENT10)


                NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts158) 
                stream_NEWLINE.add(NEWLINE11)


                self._state.following.append(self.FOLLOW_consts_items_in_consts160)
                consts_items12 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items12.tree)


                DEDENT13 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts162) 
                stream_DEDENT.add(DEDENT13)


                NEWLINE14 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts164) 
                stream_NEWLINE.add(NEWLINE14)


                # AST Rewrite
                # elements: consts_items, CONSTS, ID
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
                # 41:68: -> ^( CONSTS ID consts_items )
                # grammar/Frontend.g:41:71: ^( CONSTS ID consts_items )
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

        consts_item15 = None



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
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items188)
                        consts_item15 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item15.tree)



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
    # grammar/Frontend.g:44:1: consts_item : ( ID num_whole NEWLINE -> ^( ID num_whole ) | ID num_fract NEWLINE -> ^( ID num_fract ) | ID EXPRESSION NEWLINE -> ^( ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID16 = None
        NEWLINE18 = None
        ID19 = None
        NEWLINE21 = None
        ID22 = None
        EXPRESSION23 = None
        NEWLINE24 = None
        num_whole17 = None

        num_fract20 = None


        ID16_tree = None
        NEWLINE18_tree = None
        ID19_tree = None
        NEWLINE21_tree = None
        ID22_tree = None
        EXPRESSION23_tree = None
        NEWLINE24_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/Frontend.g:45:5: ( ID num_whole NEWLINE -> ^( ID num_whole ) | ID num_fract NEWLINE -> ^( ID num_fract ) | ID EXPRESSION NEWLINE -> ^( ID EXPRESSION ) )
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
                            elif (LA3_4 == NEWLINE) :
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
                        elif (LA3_4 == NEWLINE) :
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
                    # grammar/Frontend.g:45:7: ID num_whole NEWLINE
                    pass 
                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item202) 
                    stream_ID.add(ID16)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item204)
                    num_whole17 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole17.tree)


                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item206) 
                    stream_NEWLINE.add(NEWLINE18)


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
                    # 45:28: -> ^( ID num_whole )
                    # grammar/Frontend.g:45:31: ^( ID num_whole )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_ID.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_num_whole.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 2:
                    # grammar/Frontend.g:46:7: ID num_fract NEWLINE
                    pass 
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item224) 
                    stream_ID.add(ID19)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item226)
                    num_fract20 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract20.tree)


                    NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item228) 
                    stream_NEWLINE.add(NEWLINE21)


                    # AST Rewrite
                    # elements: ID, num_fract
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
                    # 46:28: -> ^( ID num_fract )
                    # grammar/Frontend.g:46:31: ^( ID num_fract )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_ID.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, stream_num_fract.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 3:
                    # grammar/Frontend.g:47:7: ID EXPRESSION NEWLINE
                    pass 
                    ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item246) 
                    stream_ID.add(ID22)


                    EXPRESSION23 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item248) 
                    stream_EXPRESSION.add(EXPRESSION23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item250) 
                    stream_NEWLINE.add(NEWLINE24)


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
                    # 47:29: -> ^( ID EXPRESSION )
                    # grammar/Frontend.g:47:32: ^( ID EXPRESSION )
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
    # grammar/Frontend.g:50:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES25 = None
        ID26 = None
        NEWLINE27 = None
        INDENT28 = None
        NEWLINE29 = None
        DEDENT31 = None
        NEWLINE32 = None
        types_items30 = None


        TYPES25_tree = None
        ID26_tree = None
        NEWLINE27_tree = None
        INDENT28_tree = None
        NEWLINE29_tree = None
        DEDENT31_tree = None
        NEWLINE32_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/Frontend.g:50:7: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TYPES ID types_items ) )
                # grammar/Frontend.g:50:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES25 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types273) 
                stream_TYPES.add(TYPES25)


                ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_types275) 
                stream_ID.add(ID26)


                NEWLINE27 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types277) 
                stream_NEWLINE.add(NEWLINE27)


                INDENT28 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types279) 
                stream_INDENT.add(INDENT28)


                NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types281) 
                stream_NEWLINE.add(NEWLINE29)


                self._state.following.append(self.FOLLOW_types_items_in_types283)
                types_items30 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items30.tree)


                DEDENT31 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types285) 
                stream_DEDENT.add(DEDENT31)


                NEWLINE32 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types287) 
                stream_NEWLINE.add(NEWLINE32)


                # AST Rewrite
                # elements: types_items, ID, TYPES
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
                # 50:68: -> ^( TYPES ID types_items )
                # grammar/Frontend.g:50:71: ^( TYPES ID types_items )
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

        types_item33 = None



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
                        self._state.following.append(self.FOLLOW_types_item_in_types_items307)
                        types_item33 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item33.tree)



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
    # grammar/Frontend.g:52:1: types_item : ID NEWLINE INDENT types_item_attrs DEDENT NEWLINE -> ^( ID types_item_attrs ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID34 = None
        NEWLINE35 = None
        INDENT36 = None
        DEDENT38 = None
        NEWLINE39 = None
        types_item_attrs37 = None


        ID34_tree = None
        NEWLINE35_tree = None
        INDENT36_tree = None
        DEDENT38_tree = None
        NEWLINE39_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item_attrs = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_attrs")
        try:
            try:
                # grammar/Frontend.g:52:12: ( ID NEWLINE INDENT types_item_attrs DEDENT NEWLINE -> ^( ID types_item_attrs ) )
                # grammar/Frontend.g:52:14: ID NEWLINE INDENT types_item_attrs DEDENT NEWLINE
                pass 
                ID34 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item317) 
                stream_ID.add(ID34)


                NEWLINE35 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item319) 
                stream_NEWLINE.add(NEWLINE35)


                INDENT36 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item321) 
                stream_INDENT.add(INDENT36)


                self._state.following.append(self.FOLLOW_types_item_attrs_in_types_item323)
                types_item_attrs37 = self.types_item_attrs()

                self._state.following.pop()
                stream_types_item_attrs.add(types_item_attrs37.tree)


                DEDENT38 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item325) 
                stream_DEDENT.add(DEDENT38)


                NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item327) 
                stream_NEWLINE.add(NEWLINE39)


                # AST Rewrite
                # elements: ID, types_item_attrs
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
                # 52:64: -> ^( ID types_item_attrs )
                # grammar/Frontend.g:52:67: ^( ID types_item_attrs )
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

        types_item_attr40 = None



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
                        self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_attrs345)
                        types_item_attr40 = self.types_item_attr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item_attr40.tree)



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
    # grammar/Frontend.g:54:1: types_item_attr : ID NEWLINE -> ID ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID41 = None
        NEWLINE42 = None

        ID41_tree = None
        NEWLINE42_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/Frontend.g:54:17: ( ID NEWLINE -> ID )
                # grammar/Frontend.g:54:19: ID NEWLINE
                pass 
                ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr355) 
                stream_ID.add(ID41)


                NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_attr357) 
                stream_NEWLINE.add(NEWLINE42)


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
                # 54:30: -> ID
                self._adaptor.addChild(root_0, 
                stream_ID.nextNode()
                )




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

        MINUS43 = None
        NUMBER44 = None

        MINUS43_tree = None
        NUMBER44_tree = None

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
                    MINUS43 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole370)
                    MINUS43_tree = self._adaptor.createWithPayload(MINUS43)
                    self._adaptor.addChild(root_0, MINUS43_tree)






                NUMBER44 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole374)
                NUMBER44_tree = self._adaptor.createWithPayload(NUMBER44)
                self._adaptor.addChild(root_0, NUMBER44_tree)





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

        MINUS45 = None
        NUMBER46 = None
        DIVIDE47 = None
        NUMBER48 = None

        MINUS45_tree = None
        NUMBER46_tree = None
        DIVIDE47_tree = None
        NUMBER48_tree = None

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
                    MINUS45 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract382)
                    MINUS45_tree = self._adaptor.createWithPayload(MINUS45)
                    self._adaptor.addChild(root_0, MINUS45_tree)






                NUMBER46 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract386)
                NUMBER46_tree = self._adaptor.createWithPayload(NUMBER46)
                self._adaptor.addChild(root_0, NUMBER46_tree)



                DIVIDE47 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract388)
                DIVIDE47_tree = self._adaptor.createWithPayload(DIVIDE47)
                self._adaptor.addChild(root_0, DIVIDE47_tree)



                NUMBER48 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract390)
                NUMBER48_tree = self._adaptor.createWithPayload(NUMBER48)
                self._adaptor.addChild(root_0, NUMBER48_tree)





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



 

    FOLLOW_module_in_start102 = frozenset([1, 4, 11, 14])
    FOLLOW_consts_in_start106 = frozenset([1, 4, 11, 14])
    FOLLOW_types_in_start110 = frozenset([1, 4, 11, 14])
    FOLLOW_MODULE_in_module123 = frozenset([8])
    FOLLOW_ID_in_module125 = frozenset([12])
    FOLLOW_NEWLINE_in_module127 = frozenset([1])
    FOLLOW_CONSTS_in_consts150 = frozenset([8])
    FOLLOW_ID_in_consts152 = frozenset([12])
    FOLLOW_NEWLINE_in_consts154 = frozenset([9])
    FOLLOW_INDENT_in_consts156 = frozenset([12])
    FOLLOW_NEWLINE_in_consts158 = frozenset([8])
    FOLLOW_consts_items_in_consts160 = frozenset([5])
    FOLLOW_DEDENT_in_consts162 = frozenset([12])
    FOLLOW_NEWLINE_in_consts164 = frozenset([1])
    FOLLOW_consts_item_in_consts_items188 = frozenset([1, 8])
    FOLLOW_ID_in_consts_item202 = frozenset([10, 13])
    FOLLOW_num_whole_in_consts_item204 = frozenset([12])
    FOLLOW_NEWLINE_in_consts_item206 = frozenset([1])
    FOLLOW_ID_in_consts_item224 = frozenset([10, 13])
    FOLLOW_num_fract_in_consts_item226 = frozenset([12])
    FOLLOW_NEWLINE_in_consts_item228 = frozenset([1])
    FOLLOW_ID_in_consts_item246 = frozenset([7])
    FOLLOW_EXPRESSION_in_consts_item248 = frozenset([12])
    FOLLOW_NEWLINE_in_consts_item250 = frozenset([1])
    FOLLOW_TYPES_in_types273 = frozenset([8])
    FOLLOW_ID_in_types275 = frozenset([12])
    FOLLOW_NEWLINE_in_types277 = frozenset([9])
    FOLLOW_INDENT_in_types279 = frozenset([12])
    FOLLOW_NEWLINE_in_types281 = frozenset([8])
    FOLLOW_types_items_in_types283 = frozenset([5])
    FOLLOW_DEDENT_in_types285 = frozenset([12])
    FOLLOW_NEWLINE_in_types287 = frozenset([1])
    FOLLOW_types_item_in_types_items307 = frozenset([1, 8])
    FOLLOW_ID_in_types_item317 = frozenset([12])
    FOLLOW_NEWLINE_in_types_item319 = frozenset([9])
    FOLLOW_INDENT_in_types_item321 = frozenset([8])
    FOLLOW_types_item_attrs_in_types_item323 = frozenset([5])
    FOLLOW_DEDENT_in_types_item325 = frozenset([12])
    FOLLOW_NEWLINE_in_types_item327 = frozenset([1])
    FOLLOW_types_item_attr_in_types_item_attrs345 = frozenset([1, 8])
    FOLLOW_ID_in_types_item_attr355 = frozenset([12])
    FOLLOW_NEWLINE_in_types_item_attr357 = frozenset([1])
    FOLLOW_MINUS_in_num_whole370 = frozenset([13])
    FOLLOW_NUMBER_in_num_whole374 = frozenset([1])
    FOLLOW_MINUS_in_num_fract382 = frozenset([13])
    FOLLOW_NUMBER_in_num_fract386 = frozenset([6])
    FOLLOW_DIVIDE_in_num_fract388 = frozenset([13])
    FOLLOW_NUMBER_in_num_fract390 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
