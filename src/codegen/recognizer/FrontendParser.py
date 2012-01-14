# $ANTLR 3.4 grammar/Frontend.g 2012-01-14 20:31:53

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
CURLY_CLOSE=5
CURLY_OPEN=6
DEDENT=7
DIVIDE=8
EXPRESSION=9
ID=10
INDENT=11
MINUS=12
MODULE=13
NEWLINE=14
NUMBER=15
TREE_CONSTS=16
TREE_EXPRESSION=17
TREE_HINT=18
TREE_HINT_NONE=19
TREE_MODULE=20
TREE_NUM_FRACT=21
TREE_NUM_WHOLE=22
TREE_TYPES=23
TREE_TYPES_ITEM=24
TREE_TYPES_ITEM_ATTR=25
TREE_TYPES_ITEM_HINT=26
TREE_TYPES_ITEM_HINTS=27
TYPES=28
UNDERSCORE=29
WHITESPACE=30

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CONSTS", "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", 
    "ID", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", "TREE_CONSTS", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_TYPES_ITEM_ATTR", 
    "TREE_TYPES_ITEM_HINT", "TREE_TYPES_ITEM_HINTS", "TYPES", "UNDERSCORE", 
    "WHITESPACE"
]




class FrontendParser(Parser):
    grammarFileName = "grammar/Frontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(FrontendParser, self).__init__(input, state, *args, **kwargs)

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )

        self.dfa12 = self.DFA12(
            self, 12,
            eot = self.DFA12_eot,
            eof = self.DFA12_eof,
            min = self.DFA12_min,
            max = self.DFA12_max,
            accept = self.DFA12_accept,
            special = self.DFA12_special,
            transition = self.DFA12_transition
            )




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
    # grammar/Frontend.g:38:1: module : MODULE ID NEWLINE -> ^( TREE_MODULE ID ) ;
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
                # grammar/Frontend.g:38:8: ( MODULE ID NEWLINE -> ^( TREE_MODULE ID ) )
                # grammar/Frontend.g:38:10: MODULE ID NEWLINE
                pass 
                MODULE4 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module123) 
                stream_MODULE.add(MODULE4)


                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_module125) 
                stream_ID.add(ID5)


                NEWLINE6 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module127) 
                stream_NEWLINE.add(NEWLINE6)


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
                # 38:28: -> ^( TREE_MODULE ID )
                # grammar/Frontend.g:38:31: ^( TREE_MODULE ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MODULE, "TREE_MODULE")
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
    # grammar/Frontend.g:40:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
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
                # grammar/Frontend.g:41:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/Frontend.g:41:7: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS7 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts150) 
                stream_CONSTS.add(CONSTS7)


                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts152) 
                stream_ID.add(ID8)


                NEWLINE9 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts154) 
                stream_NEWLINE.add(NEWLINE9)


                INDENT10 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts162) 
                stream_INDENT.add(INDENT10)


                NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts164) 
                stream_NEWLINE.add(NEWLINE11)


                self._state.following.append(self.FOLLOW_consts_items_in_consts166)
                consts_items12 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items12.tree)


                DEDENT13 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts168) 
                stream_DEDENT.add(DEDENT13)


                NEWLINE14 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts170) 
                stream_NEWLINE.add(NEWLINE14)


                # AST Rewrite
                # elements: ID, consts_items
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
                # 43:7: -> ^( TREE_CONSTS ID consts_items )
                # grammar/Frontend.g:43:10: ^( TREE_CONSTS ID consts_items )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_CONSTS, "TREE_CONSTS")
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
    # grammar/Frontend.g:45:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item15 = None



        try:
            try:
                # grammar/Frontend.g:45:14: ( ( consts_item )+ )
                # grammar/Frontend.g:45:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:45:16: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/Frontend.g:45:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items200)
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
    # grammar/Frontend.g:46:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
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
                # grammar/Frontend.g:47:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/Frontend.g:47:7: ID num_whole NEWLINE
                    pass 
                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item214) 
                    stream_ID.add(ID16)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item216)
                    num_whole17 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole17.tree)


                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item218) 
                    stream_NEWLINE.add(NEWLINE18)


                    # AST Rewrite
                    # elements: num_whole, ID
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
                    # 47:28: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/Frontend.g:47:31: ^( TREE_NUM_WHOLE ID num_whole )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_NUM_WHOLE, "TREE_NUM_WHOLE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_num_whole.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 2:
                    # grammar/Frontend.g:48:7: ID num_fract NEWLINE
                    pass 
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item238) 
                    stream_ID.add(ID19)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item240)
                    num_fract20 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract20.tree)


                    NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item242) 
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
                    # 48:28: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/Frontend.g:48:31: ^( TREE_NUM_FRACT ID num_fract )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_NUM_FRACT, "TREE_NUM_FRACT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_num_fract.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 3:
                    # grammar/Frontend.g:49:7: ID EXPRESSION NEWLINE
                    pass 
                    ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item262) 
                    stream_ID.add(ID22)


                    EXPRESSION23 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item264) 
                    stream_EXPRESSION.add(EXPRESSION23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item266) 
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
                    # 49:29: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/Frontend.g:49:32: ^( TREE_EXPRESSION ID EXPRESSION )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_EXPRESSION, "TREE_EXPRESSION")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

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
    # grammar/Frontend.g:52:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
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
                # grammar/Frontend.g:53:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/Frontend.g:53:7: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES25 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types295) 
                stream_TYPES.add(TYPES25)


                ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_types297) 
                stream_ID.add(ID26)


                NEWLINE27 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types299) 
                stream_NEWLINE.add(NEWLINE27)


                INDENT28 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types307) 
                stream_INDENT.add(INDENT28)


                NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types309) 
                stream_NEWLINE.add(NEWLINE29)


                self._state.following.append(self.FOLLOW_types_items_in_types311)
                types_items30 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items30.tree)


                DEDENT31 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types313) 
                stream_DEDENT.add(DEDENT31)


                NEWLINE32 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types315) 
                stream_NEWLINE.add(NEWLINE32)


                # AST Rewrite
                # elements: types_items, ID
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
                # 55:7: -> ^( TREE_TYPES ID types_items )
                # grammar/Frontend.g:55:10: ^( TREE_TYPES ID types_items )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
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
    # grammar/Frontend.g:57:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item33 = None



        try:
            try:
                # grammar/Frontend.g:57:13: ( ( types_item )+ )
                # grammar/Frontend.g:57:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:57:15: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/Frontend.g:57:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items345)
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
    # grammar/Frontend.g:58:1: types_item : ( ID types_item_hint NEWLINE -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS types_item_hint ) ) | ID NEWLINE INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) ) | ID types_item_hint NEWLINE INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) ) );
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID34 = None
        NEWLINE36 = None
        ID37 = None
        NEWLINE38 = None
        INDENT39 = None
        NEWLINE40 = None
        NEWLINE42 = None
        DEDENT43 = None
        NEWLINE44 = None
        ID45 = None
        NEWLINE47 = None
        INDENT48 = None
        NEWLINE49 = None
        NEWLINE51 = None
        DEDENT52 = None
        NEWLINE53 = None
        types_item_hint35 = None

        types_item_hint41 = None

        types_item_hint46 = None

        types_item_hint50 = None


        ID34_tree = None
        NEWLINE36_tree = None
        ID37_tree = None
        NEWLINE38_tree = None
        INDENT39_tree = None
        NEWLINE40_tree = None
        NEWLINE42_tree = None
        DEDENT43_tree = None
        NEWLINE44_tree = None
        ID45_tree = None
        NEWLINE47_tree = None
        INDENT48_tree = None
        NEWLINE49_tree = None
        NEWLINE51_tree = None
        DEDENT52_tree = None
        NEWLINE53_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item_hint = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_hint")
        try:
            try:
                # grammar/Frontend.g:59:5: ( ID types_item_hint NEWLINE -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS types_item_hint ) ) | ID NEWLINE INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) ) | ID types_item_hint NEWLINE INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) ) )
                alt7 = 3
                alt7 = self.dfa7.predict(self.input)
                if alt7 == 1:
                    # grammar/Frontend.g:59:7: ID types_item_hint NEWLINE
                    pass 
                    ID34 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item359) 
                    stream_ID.add(ID34)


                    self._state.following.append(self.FOLLOW_types_item_hint_in_types_item361)
                    types_item_hint35 = self.types_item_hint()

                    self._state.following.pop()
                    stream_types_item_hint.add(types_item_hint35.tree)


                    NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item363) 
                    stream_NEWLINE.add(NEWLINE36)


                    # AST Rewrite
                    # elements: ID, types_item_hint
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
                    # 60:7: -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS types_item_hint ) )
                    # grammar/Frontend.g:60:10: ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS types_item_hint ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM, "TREE_TYPES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/Frontend.g:60:32: ^( TREE_TYPES_ITEM_HINTS types_item_hint )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINTS, "TREE_TYPES_ITEM_HINTS")
                    , root_2)

                    self._adaptor.addChild(root_2, stream_types_item_hint.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt7 == 2:
                    # grammar/Frontend.g:61:7: ID NEWLINE INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item395) 
                    stream_ID.add(ID37)


                    NEWLINE38 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item397) 
                    stream_NEWLINE.add(NEWLINE38)


                    INDENT39 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item399) 
                    stream_INDENT.add(INDENT39)


                    NEWLINE40 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item401) 
                    stream_NEWLINE.add(NEWLINE40)


                    # grammar/Frontend.g:61:33: ( types_item_hint NEWLINE )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == CURLY_OPEN or LA5_0 == ID) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammar/Frontend.g:61:35: types_item_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_hint_in_types_item405)
                            types_item_hint41 = self.types_item_hint()

                            self._state.following.pop()
                            stream_types_item_hint.add(types_item_hint41.tree)


                            NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item407) 
                            stream_NEWLINE.add(NEWLINE42)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    DEDENT43 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item413) 
                    stream_DEDENT.add(DEDENT43)


                    NEWLINE44 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item415) 
                    stream_NEWLINE.add(NEWLINE44)


                    # AST Rewrite
                    # elements: ID, types_item_hint
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
                    # 62:7: -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) )
                    # grammar/Frontend.g:62:10: ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM, "TREE_TYPES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/Frontend.g:62:32: ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINTS, "TREE_TYPES_ITEM_HINTS")
                    , root_2)

                    # grammar/Frontend.g:62:57: ( types_item_hint )+
                    if not (stream_types_item_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_hint.hasNext():
                        self._adaptor.addChild(root_2, stream_types_item_hint.nextTree())


                    stream_types_item_hint.reset()

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt7 == 3:
                    # grammar/Frontend.g:63:7: ID types_item_hint NEWLINE INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    ID45 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item449) 
                    stream_ID.add(ID45)


                    self._state.following.append(self.FOLLOW_types_item_hint_in_types_item451)
                    types_item_hint46 = self.types_item_hint()

                    self._state.following.pop()
                    stream_types_item_hint.add(types_item_hint46.tree)


                    NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item453) 
                    stream_NEWLINE.add(NEWLINE47)


                    INDENT48 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item461) 
                    stream_INDENT.add(INDENT48)


                    NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item463) 
                    stream_NEWLINE.add(NEWLINE49)


                    # grammar/Frontend.g:64:22: ( types_item_hint NEWLINE )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == CURLY_OPEN or LA6_0 == ID) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/Frontend.g:64:24: types_item_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_hint_in_types_item467)
                            types_item_hint50 = self.types_item_hint()

                            self._state.following.pop()
                            stream_types_item_hint.add(types_item_hint50.tree)


                            NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item469) 
                            stream_NEWLINE.add(NEWLINE51)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT52 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item475) 
                    stream_DEDENT.add(DEDENT52)


                    NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item477) 
                    stream_NEWLINE.add(NEWLINE53)


                    # AST Rewrite
                    # elements: ID, types_item_hint
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
                    # 65:7: -> ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) )
                    # grammar/Frontend.g:65:10: ^( TREE_TYPES_ITEM ID ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM, "TREE_TYPES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/Frontend.g:65:32: ^( TREE_TYPES_ITEM_HINTS ( types_item_hint )+ )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINTS, "TREE_TYPES_ITEM_HINTS")
                    , root_2)

                    # grammar/Frontend.g:65:57: ( types_item_hint )+
                    if not (stream_types_item_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_hint.hasNext():
                        self._adaptor.addChild(root_2, stream_types_item_hint.nextTree())


                    stream_types_item_hint.reset()

                    self._adaptor.addChild(root_1, root_2)

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


    class types_item_hint_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.types_item_hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item_hint"
    # grammar/Frontend.g:67:1: types_item_hint : ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        retval = self.types_item_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE58 = None
        INDENT59 = None
        NEWLINE60 = None
        NEWLINE62 = None
        DEDENT63 = None
        types_item_attr54 = None

        hint55 = None

        types_item_attr56 = None

        hint57 = None

        types_item_attr61 = None


        NEWLINE58_tree = None
        INDENT59_tree = None
        NEWLINE60_tree = None
        NEWLINE62_tree = None
        DEDENT63_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        stream_types_item_attr = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_attr")
        try:
            try:
                # grammar/Frontend.g:68:5: ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
                alt12 = 3
                alt12 = self.dfa12.predict(self.input)
                if alt12 == 1:
                    # grammar/Frontend.g:68:7: ( types_item_attr )+
                    pass 
                    # grammar/Frontend.g:68:7: ( types_item_attr )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == ID) :
                            alt8 = 1


                        if alt8 == 1:
                            # grammar/Frontend.g:68:7: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint520)
                            types_item_attr54 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr54.tree)



                        else:
                            if cnt8 >= 1:
                                break #loop8

                            eee = EarlyExitException(8, self.input)
                            raise eee

                        cnt8 += 1


                    # AST Rewrite
                    # elements: types_item_attr
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
                    # 69:7: -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    # grammar/Frontend.g:69:10: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/Frontend.g:69:49: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 2:
                    # grammar/Frontend.g:70:7: hint ( types_item_attr )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint551)
                    hint55 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint55.tree)


                    # grammar/Frontend.g:70:12: ( types_item_attr )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == ID) :
                            alt9 = 1


                        if alt9 == 1:
                            # grammar/Frontend.g:70:12: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint553)
                            types_item_attr56 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr56.tree)



                        else:
                            if cnt9 >= 1:
                                break #loop9

                            eee = EarlyExitException(9, self.input)
                            raise eee

                        cnt9 += 1


                    # AST Rewrite
                    # elements: hint, types_item_attr
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
                    # 71:7: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/Frontend.g:71:10: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/Frontend.g:71:39: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 3:
                    # grammar/Frontend.g:72:7: hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint583)
                    hint57 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint57.tree)


                    NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint585) 
                    stream_NEWLINE.add(NEWLINE58)


                    INDENT59 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item_hint587) 
                    stream_INDENT.add(INDENT59)


                    NEWLINE60 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint589) 
                    stream_NEWLINE.add(NEWLINE60)


                    # grammar/Frontend.g:73:9: ( ( types_item_attr )+ NEWLINE )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == ID) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/Frontend.g:73:11: ( types_item_attr )+ NEWLINE
                            pass 
                            # grammar/Frontend.g:73:11: ( types_item_attr )+
                            cnt10 = 0
                            while True: #loop10
                                alt10 = 2
                                LA10_0 = self.input.LA(1)

                                if (LA10_0 == ID) :
                                    alt10 = 1


                                if alt10 == 1:
                                    # grammar/Frontend.g:73:11: types_item_attr
                                    pass 
                                    self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint602)
                                    types_item_attr61 = self.types_item_attr()

                                    self._state.following.pop()
                                    stream_types_item_attr.add(types_item_attr61.tree)



                                else:
                                    if cnt10 >= 1:
                                        break #loop10

                                    eee = EarlyExitException(10, self.input)
                                    raise eee

                                cnt10 += 1


                            NEWLINE62 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint606) 
                            stream_NEWLINE.add(NEWLINE62)



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    DEDENT63 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item_hint612) 
                    stream_DEDENT.add(DEDENT63)


                    # AST Rewrite
                    # elements: hint, types_item_attr
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
                    # 74:7: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/Frontend.g:74:10: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/Frontend.g:74:39: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

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

    # $ANTLR end "types_item_hint"


    class types_item_attr_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.types_item_attr_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item_attr"
    # grammar/Frontend.g:76:1: types_item_attr : ID -> ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID64 = None

        ID64_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/Frontend.g:76:17: ( ID -> ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/Frontend.g:76:19: ID
                pass 
                ID64 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr644) 
                stream_ID.add(ID64)


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
                # 76:22: -> ^( TREE_TYPES_ITEM_ATTR ID )
                # grammar/Frontend.g:76:25: ^( TREE_TYPES_ITEM_ATTR ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES_ITEM_ATTR, "TREE_TYPES_ITEM_ATTR")
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

    # $ANTLR end "types_item_attr"


    class hint_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "hint"
    # grammar/Frontend.g:78:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN65 = None
        ID66 = None
        CURLY_CLOSE67 = None
        CURLY_OPEN68 = None
        ID69 = None
        CURLY_CLOSE71 = None
        hint_arg70 = None


        CURLY_OPEN65_tree = None
        ID66_tree = None
        CURLY_CLOSE67_tree = None
        CURLY_OPEN68_tree = None
        ID69_tree = None
        CURLY_CLOSE71_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/Frontend.g:79:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == CURLY_OPEN) :
                    LA14_1 = self.input.LA(2)

                    if (LA14_1 == ID) :
                        LA14_2 = self.input.LA(3)

                        if (LA14_2 == CURLY_CLOSE) :
                            alt14 = 1
                        elif (LA14_2 == ID or LA14_2 == UNDERSCORE) :
                            alt14 = 2
                        else:
                            nvae = NoViableAltException("", 14, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/Frontend.g:79:7: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN65 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint667) 
                    stream_CURLY_OPEN.add(CURLY_OPEN65)


                    ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_hint669) 
                    stream_ID.add(ID66)


                    CURLY_CLOSE67 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint671) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE67)


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
                    # 79:33: -> ^( TREE_HINT ID )
                    # grammar/Frontend.g:79:36: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt14 == 2:
                    # grammar/Frontend.g:80:7: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN68 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint689) 
                    stream_CURLY_OPEN.add(CURLY_OPEN68)


                    ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_hint691) 
                    stream_ID.add(ID69)


                    # grammar/Frontend.g:80:21: ( hint_arg )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == ID or LA13_0 == UNDERSCORE) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/Frontend.g:80:21: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint693)
                            hint_arg70 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg70.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    CURLY_CLOSE71 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint697) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE71)


                    # AST Rewrite
                    # elements: hint_arg, ID
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
                    # 80:44: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/Frontend.g:80:47: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/Frontend.g:80:63: ( hint_arg )+
                    if not (stream_hint_arg.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_hint_arg.hasNext():
                        self._adaptor.addChild(root_1, stream_hint_arg.nextTree())


                    stream_hint_arg.reset()

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

    # $ANTLR end "hint"


    class hint_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.hint_arg_return, self).__init__()

            self.tree = None





    # $ANTLR start "hint_arg"
    # grammar/Frontend.g:82:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set72 = None

        set72_tree = None

        try:
            try:
                # grammar/Frontend.g:82:10: ( ID | UNDERSCORE )
                # grammar/Frontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set72 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set72))

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

    # $ANTLR end "hint_arg"


    class num_whole_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.num_whole_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_whole"
    # grammar/Frontend.g:84:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS73 = None
        NUMBER74 = None

        MINUS73_tree = None
        NUMBER74_tree = None

        try:
            try:
                # grammar/Frontend.g:84:11: ( ( MINUS )? NUMBER )
                # grammar/Frontend.g:84:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:84:13: ( MINUS )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == MINUS) :
                    alt15 = 1
                if alt15 == 1:
                    # grammar/Frontend.g:84:13: MINUS
                    pass 
                    MINUS73 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole736)
                    MINUS73_tree = self._adaptor.createWithPayload(MINUS73)
                    self._adaptor.addChild(root_0, MINUS73_tree)






                NUMBER74 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole740)
                NUMBER74_tree = self._adaptor.createWithPayload(NUMBER74)
                self._adaptor.addChild(root_0, NUMBER74_tree)





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
    # grammar/Frontend.g:85:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS75 = None
        NUMBER76 = None
        DIVIDE77 = None
        NUMBER78 = None

        MINUS75_tree = None
        NUMBER76_tree = None
        DIVIDE77_tree = None
        NUMBER78_tree = None

        try:
            try:
                # grammar/Frontend.g:85:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/Frontend.g:85:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/Frontend.g:85:13: ( MINUS )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == MINUS) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/Frontend.g:85:13: MINUS
                    pass 
                    MINUS75 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract748)
                    MINUS75_tree = self._adaptor.createWithPayload(MINUS75)
                    self._adaptor.addChild(root_0, MINUS75_tree)






                NUMBER76 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract752)
                NUMBER76_tree = self._adaptor.createWithPayload(NUMBER76)
                self._adaptor.addChild(root_0, NUMBER76_tree)



                DIVIDE77 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract754)
                DIVIDE77_tree = self._adaptor.createWithPayload(DIVIDE77)
                self._adaptor.addChild(root_0, DIVIDE77_tree)



                NUMBER78 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract756)
                NUMBER78_tree = self._adaptor.createWithPayload(NUMBER78)
                self._adaptor.addChild(root_0, NUMBER78_tree)





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



    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\23\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\23\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\12\1\6\1\uffff\2\12\1\7\1\5\2\uffff\1\12\1\5\1\12\1\13\1\12"
        u"\1\16\2\12\1\7\1\16"
        )

    DFA7_max = DFA.unpack(
        u"\1\12\1\16\1\uffff\1\16\1\12\1\13\1\35\2\uffff\1\16\1\35\1\16\1"
        u"\13\2\16\1\12\1\16\1\12\1\16"
        )

    DFA7_accept = DFA.unpack(
        u"\2\uffff\1\2\4\uffff\1\3\1\1\12\uffff"
        )

    DFA7_special = DFA.unpack(
        u"\23\uffff"
        )


    DFA7_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\4\3\uffff\1\3\3\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\3\uffff\1\5"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\10\2\uffff\1\10\1\7"),
        DFA.unpack(u"\1\11\4\uffff\1\12\22\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13\3\uffff\1\14"),
        DFA.unpack(u"\1\15\4\uffff\1\12\22\uffff\1\12"),
        DFA.unpack(u"\1\13\3\uffff\1\5"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\13\3\uffff\1\14"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\20\3\uffff\1\21"),
        DFA.unpack(u"\1\22\2\uffff\1\20"),
        DFA.unpack(u"\1\5")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


    # lookup tables for DFA #12

    DFA12_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA12_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA12_min = DFA.unpack(
        u"\1\6\1\uffff\1\12\1\5\1\12\1\5\2\uffff\1\12"
        )

    DFA12_max = DFA.unpack(
        u"\1\12\1\uffff\1\12\1\35\1\16\1\35\2\uffff\1\16"
        )

    DFA12_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA12_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA12_transition = [
        DFA.unpack(u"\1\2\3\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\4\uffff\1\5\22\uffff\1\5"),
        DFA.unpack(u"\1\6\3\uffff\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\5\22\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\7")
    ]

    # class definition for DFA #12

    class DFA12(DFA):
        pass


 

    FOLLOW_module_in_start102 = frozenset([1, 4, 13, 28])
    FOLLOW_consts_in_start106 = frozenset([1, 4, 13, 28])
    FOLLOW_types_in_start110 = frozenset([1, 4, 13, 28])
    FOLLOW_MODULE_in_module123 = frozenset([10])
    FOLLOW_ID_in_module125 = frozenset([14])
    FOLLOW_NEWLINE_in_module127 = frozenset([1])
    FOLLOW_CONSTS_in_consts150 = frozenset([10])
    FOLLOW_ID_in_consts152 = frozenset([14])
    FOLLOW_NEWLINE_in_consts154 = frozenset([11])
    FOLLOW_INDENT_in_consts162 = frozenset([14])
    FOLLOW_NEWLINE_in_consts164 = frozenset([10])
    FOLLOW_consts_items_in_consts166 = frozenset([7])
    FOLLOW_DEDENT_in_consts168 = frozenset([14])
    FOLLOW_NEWLINE_in_consts170 = frozenset([1])
    FOLLOW_consts_item_in_consts_items200 = frozenset([1, 10])
    FOLLOW_ID_in_consts_item214 = frozenset([12, 15])
    FOLLOW_num_whole_in_consts_item216 = frozenset([14])
    FOLLOW_NEWLINE_in_consts_item218 = frozenset([1])
    FOLLOW_ID_in_consts_item238 = frozenset([12, 15])
    FOLLOW_num_fract_in_consts_item240 = frozenset([14])
    FOLLOW_NEWLINE_in_consts_item242 = frozenset([1])
    FOLLOW_ID_in_consts_item262 = frozenset([9])
    FOLLOW_EXPRESSION_in_consts_item264 = frozenset([14])
    FOLLOW_NEWLINE_in_consts_item266 = frozenset([1])
    FOLLOW_TYPES_in_types295 = frozenset([10])
    FOLLOW_ID_in_types297 = frozenset([14])
    FOLLOW_NEWLINE_in_types299 = frozenset([11])
    FOLLOW_INDENT_in_types307 = frozenset([14])
    FOLLOW_NEWLINE_in_types309 = frozenset([10])
    FOLLOW_types_items_in_types311 = frozenset([7])
    FOLLOW_DEDENT_in_types313 = frozenset([14])
    FOLLOW_NEWLINE_in_types315 = frozenset([1])
    FOLLOW_types_item_in_types_items345 = frozenset([1, 10])
    FOLLOW_ID_in_types_item359 = frozenset([6, 10])
    FOLLOW_types_item_hint_in_types_item361 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item363 = frozenset([1])
    FOLLOW_ID_in_types_item395 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item397 = frozenset([11])
    FOLLOW_INDENT_in_types_item399 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item401 = frozenset([6, 10])
    FOLLOW_types_item_hint_in_types_item405 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item407 = frozenset([6, 7, 10])
    FOLLOW_DEDENT_in_types_item413 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item415 = frozenset([1])
    FOLLOW_ID_in_types_item449 = frozenset([6, 10])
    FOLLOW_types_item_hint_in_types_item451 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item453 = frozenset([11])
    FOLLOW_INDENT_in_types_item461 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item463 = frozenset([6, 10])
    FOLLOW_types_item_hint_in_types_item467 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item469 = frozenset([6, 7, 10])
    FOLLOW_DEDENT_in_types_item475 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item477 = frozenset([1])
    FOLLOW_types_item_attr_in_types_item_hint520 = frozenset([1, 10])
    FOLLOW_hint_in_types_item_hint551 = frozenset([10])
    FOLLOW_types_item_attr_in_types_item_hint553 = frozenset([1, 10])
    FOLLOW_hint_in_types_item_hint583 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item_hint585 = frozenset([11])
    FOLLOW_INDENT_in_types_item_hint587 = frozenset([14])
    FOLLOW_NEWLINE_in_types_item_hint589 = frozenset([10])
    FOLLOW_types_item_attr_in_types_item_hint602 = frozenset([10, 14])
    FOLLOW_NEWLINE_in_types_item_hint606 = frozenset([7, 10])
    FOLLOW_DEDENT_in_types_item_hint612 = frozenset([1])
    FOLLOW_ID_in_types_item_attr644 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint667 = frozenset([10])
    FOLLOW_ID_in_hint669 = frozenset([5])
    FOLLOW_CURLY_CLOSE_in_hint671 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint689 = frozenset([10])
    FOLLOW_ID_in_hint691 = frozenset([10, 29])
    FOLLOW_hint_arg_in_hint693 = frozenset([5, 10, 29])
    FOLLOW_CURLY_CLOSE_in_hint697 = frozenset([1])
    FOLLOW_MINUS_in_num_whole736 = frozenset([15])
    FOLLOW_NUMBER_in_num_whole740 = frozenset([1])
    FOLLOW_MINUS_in_num_fract748 = frozenset([15])
    FOLLOW_NUMBER_in_num_fract752 = frozenset([8])
    FOLLOW_DIVIDE_in_num_fract754 = frozenset([15])
    FOLLOW_NUMBER_in_num_fract756 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
