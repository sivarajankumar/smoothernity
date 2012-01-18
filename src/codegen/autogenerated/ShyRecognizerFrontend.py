# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-18 18:43:00

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



class ShyRecognizerFrontendException ( Exception ) :
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




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

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
        raise ShyRecognizerFrontendException ( msg )


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # grammar/ShyRecognizerFrontend.g:24:1: start : ( module | consts | types )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        module1 = None

        consts2 = None

        types3 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:24:7: ( ( module | consts | types )* )
                # grammar/ShyRecognizerFrontend.g:24:9: ( module | consts | types )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:24:9: ( module | consts | types )*
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
                        # grammar/ShyRecognizerFrontend.g:24:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start82)
                        module1 = self.module()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, module1.tree)



                    elif alt1 == 2:
                        # grammar/ShyRecognizerFrontend.g:24:20: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start86)
                        consts2 = self.consts()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts2.tree)



                    elif alt1 == 3:
                        # grammar/ShyRecognizerFrontend.g:24:29: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start90)
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
            super(ShyRecognizerFrontend.module_return, self).__init__()

            self.tree = None





    # $ANTLR start "module"
    # grammar/ShyRecognizerFrontend.g:26:1: module : MODULE ID NEWLINE -> ^( TREE_MODULE ID ) ;
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
                # grammar/ShyRecognizerFrontend.g:26:8: ( MODULE ID NEWLINE -> ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerFrontend.g:26:10: MODULE ID NEWLINE
                pass 
                MODULE4 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module103) 
                stream_MODULE.add(MODULE4)


                ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_module105) 
                stream_ID.add(ID5)


                NEWLINE6 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module107) 
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
                # 26:28: -> ^( TREE_MODULE ID )
                # grammar/ShyRecognizerFrontend.g:26:31: ^( TREE_MODULE ID )
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
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:28:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
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
                # grammar/ShyRecognizerFrontend.g:29:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:29:7: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS7 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts130) 
                stream_CONSTS.add(CONSTS7)


                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_consts132) 
                stream_ID.add(ID8)


                NEWLINE9 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts134) 
                stream_NEWLINE.add(NEWLINE9)


                INDENT10 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts142) 
                stream_INDENT.add(INDENT10)


                NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts144) 
                stream_NEWLINE.add(NEWLINE11)


                self._state.following.append(self.FOLLOW_consts_items_in_consts146)
                consts_items12 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items12.tree)


                DEDENT13 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts148) 
                stream_DEDENT.add(DEDENT13)


                NEWLINE14 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts150) 
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
                # 31:7: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:31:10: ^( TREE_CONSTS ID consts_items )
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
            super(ShyRecognizerFrontend.consts_items_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_items"
    # grammar/ShyRecognizerFrontend.g:33:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item15 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:33:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:33:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:33:16: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyRecognizerFrontend.g:33:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items180)
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
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:34:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
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
                # grammar/ShyRecognizerFrontend.g:35:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerFrontend.g:35:7: ID num_whole NEWLINE
                    pass 
                    ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item194) 
                    stream_ID.add(ID16)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item196)
                    num_whole17 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole17.tree)


                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item198) 
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
                    # 35:28: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:35:31: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/ShyRecognizerFrontend.g:36:7: ID num_fract NEWLINE
                    pass 
                    ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item218) 
                    stream_ID.add(ID19)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item220)
                    num_fract20 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract20.tree)


                    NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item222) 
                    stream_NEWLINE.add(NEWLINE21)


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
                    # 36:28: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:36:31: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:37:7: ID EXPRESSION NEWLINE
                    pass 
                    ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item242) 
                    stream_ID.add(ID22)


                    EXPRESSION23 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item244) 
                    stream_EXPRESSION.add(EXPRESSION23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item246) 
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
                    # 37:29: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:37:32: ^( TREE_EXPRESSION ID EXPRESSION )
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
            super(ShyRecognizerFrontend.types_return, self).__init__()

            self.tree = None





    # $ANTLR start "types"
    # grammar/ShyRecognizerFrontend.g:40:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
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
                # grammar/ShyRecognizerFrontend.g:41:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:41:7: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES25 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types275) 
                stream_TYPES.add(TYPES25)


                ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_types277) 
                stream_ID.add(ID26)


                NEWLINE27 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types279) 
                stream_NEWLINE.add(NEWLINE27)


                INDENT28 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types287) 
                stream_INDENT.add(INDENT28)


                NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types289) 
                stream_NEWLINE.add(NEWLINE29)


                self._state.following.append(self.FOLLOW_types_items_in_types291)
                types_items30 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items30.tree)


                DEDENT31 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types293) 
                stream_DEDENT.add(DEDENT31)


                NEWLINE32 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types295) 
                stream_NEWLINE.add(NEWLINE32)


                # AST Rewrite
                # elements: ID, types_items
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
                # 43:7: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:43:10: ^( TREE_TYPES ID types_items )
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
            super(ShyRecognizerFrontend.types_items_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_items"
    # grammar/ShyRecognizerFrontend.g:45:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item33 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:45:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:45:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:45:15: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:45:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items325)
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
            super(ShyRecognizerFrontend.types_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerFrontend.g:46:1: types_item : ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID34 = None
        NEWLINE36 = None
        INDENT37 = None
        NEWLINE38 = None
        NEWLINE40 = None
        DEDENT41 = None
        NEWLINE42 = None
        types_item_hint35 = None

        types_item_hint39 = None


        ID34_tree = None
        NEWLINE36_tree = None
        INDENT37_tree = None
        NEWLINE38_tree = None
        NEWLINE40_tree = None
        DEDENT41_tree = None
        NEWLINE42_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item_hint = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:47:5: ( ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* ) )
                # grammar/ShyRecognizerFrontend.g:47:7: ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID34 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item339) 
                stream_ID.add(ID34)


                # grammar/ShyRecognizerFrontend.g:47:10: ( types_item_hint )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == CURLY_OPEN or LA5_0 == ID) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerFrontend.g:47:10: types_item_hint
                    pass 
                    self._state.following.append(self.FOLLOW_types_item_hint_in_types_item341)
                    types_item_hint35 = self.types_item_hint()

                    self._state.following.pop()
                    stream_types_item_hint.add(types_item_hint35.tree)





                NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item345) 
                stream_NEWLINE.add(NEWLINE36)


                # grammar/ShyRecognizerFrontend.g:48:7: ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == INDENT) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerFrontend.g:48:9: INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT37 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item355) 
                    stream_INDENT.add(INDENT37)


                    NEWLINE38 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item357) 
                    stream_NEWLINE.add(NEWLINE38)


                    # grammar/ShyRecognizerFrontend.g:48:24: ( types_item_hint NEWLINE )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == CURLY_OPEN or LA6_0 == ID) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyRecognizerFrontend.g:48:26: types_item_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_hint_in_types_item361)
                            types_item_hint39 = self.types_item_hint()

                            self._state.following.pop()
                            stream_types_item_hint.add(types_item_hint39.tree)


                            NEWLINE40 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item363) 
                            stream_NEWLINE.add(NEWLINE40)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT41 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item369) 
                    stream_DEDENT.add(DEDENT41)


                    NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item371) 
                    stream_NEWLINE.add(NEWLINE42)





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
                # 49:7: -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* )
                # grammar/ShyRecognizerFrontend.g:49:10: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES_ITEM, "TREE_TYPES_ITEM")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                self._adaptor.createFromType(TREE_TYPES_ITEM_HINTS, "TREE_TYPES_ITEM_HINTS")
                )

                # grammar/ShyRecognizerFrontend.g:49:54: ( types_item_hint )*
                while stream_types_item_hint.hasNext():
                    self._adaptor.addChild(root_1, stream_types_item_hint.nextTree())


                stream_types_item_hint.reset();

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
            super(ShyRecognizerFrontend.types_item_hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item_hint"
    # grammar/ShyRecognizerFrontend.g:51:1: types_item_hint : ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        retval = self.types_item_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE47 = None
        INDENT48 = None
        NEWLINE49 = None
        NEWLINE51 = None
        DEDENT52 = None
        types_item_attr43 = None

        hint44 = None

        types_item_attr45 = None

        hint46 = None

        types_item_attr50 = None


        NEWLINE47_tree = None
        INDENT48_tree = None
        NEWLINE49_tree = None
        NEWLINE51_tree = None
        DEDENT52_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        stream_types_item_attr = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_attr")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:52:5: ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
                alt12 = 3
                alt12 = self.dfa12.predict(self.input)
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:52:7: ( types_item_attr )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:52:7: ( types_item_attr )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == ID) :
                            alt8 = 1


                        if alt8 == 1:
                            # grammar/ShyRecognizerFrontend.g:52:7: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint414)
                            types_item_attr43 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr43.tree)



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
                    # 53:7: -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:53:10: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:53:49: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 2:
                    # grammar/ShyRecognizerFrontend.g:54:7: hint ( types_item_attr )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint445)
                    hint44 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint44.tree)


                    # grammar/ShyRecognizerFrontend.g:54:12: ( types_item_attr )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == ID) :
                            alt9 = 1


                        if alt9 == 1:
                            # grammar/ShyRecognizerFrontend.g:54:12: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint447)
                            types_item_attr45 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr45.tree)



                        else:
                            if cnt9 >= 1:
                                break #loop9

                            eee = EarlyExitException(9, self.input)
                            raise eee

                        cnt9 += 1


                    # AST Rewrite
                    # elements: types_item_attr, hint
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
                    # 55:7: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:55:10: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:55:39: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 3:
                    # grammar/ShyRecognizerFrontend.g:56:7: hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint477)
                    hint46 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint46.tree)


                    NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint479) 
                    stream_NEWLINE.add(NEWLINE47)


                    INDENT48 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item_hint481) 
                    stream_INDENT.add(INDENT48)


                    NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint483) 
                    stream_NEWLINE.add(NEWLINE49)


                    # grammar/ShyRecognizerFrontend.g:57:9: ( ( types_item_attr )+ NEWLINE )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == ID) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/ShyRecognizerFrontend.g:57:11: ( types_item_attr )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:57:11: ( types_item_attr )+
                            cnt10 = 0
                            while True: #loop10
                                alt10 = 2
                                LA10_0 = self.input.LA(1)

                                if (LA10_0 == ID) :
                                    alt10 = 1


                                if alt10 == 1:
                                    # grammar/ShyRecognizerFrontend.g:57:11: types_item_attr
                                    pass 
                                    self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint496)
                                    types_item_attr50 = self.types_item_attr()

                                    self._state.following.pop()
                                    stream_types_item_attr.add(types_item_attr50.tree)



                                else:
                                    if cnt10 >= 1:
                                        break #loop10

                                    eee = EarlyExitException(10, self.input)
                                    raise eee

                                cnt10 += 1


                            NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint500) 
                            stream_NEWLINE.add(NEWLINE51)



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    DEDENT52 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item_hint506) 
                    stream_DEDENT.add(DEDENT52)


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
                    # 58:7: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:58:10: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:58:39: ( types_item_attr )+
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
            super(ShyRecognizerFrontend.types_item_attr_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item_attr"
    # grammar/ShyRecognizerFrontend.g:60:1: types_item_attr : ID -> ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID53 = None

        ID53_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:60:17: ( ID -> ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/ShyRecognizerFrontend.g:60:19: ID
                pass 
                ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr538) 
                stream_ID.add(ID53)


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
                # 60:22: -> ^( TREE_TYPES_ITEM_ATTR ID )
                # grammar/ShyRecognizerFrontend.g:60:25: ^( TREE_TYPES_ITEM_ATTR ID )
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
            super(ShyRecognizerFrontend.hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "hint"
    # grammar/ShyRecognizerFrontend.g:62:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN54 = None
        ID55 = None
        CURLY_CLOSE56 = None
        CURLY_OPEN57 = None
        ID58 = None
        CURLY_CLOSE60 = None
        hint_arg59 = None


        CURLY_OPEN54_tree = None
        ID55_tree = None
        CURLY_CLOSE56_tree = None
        CURLY_OPEN57_tree = None
        ID58_tree = None
        CURLY_CLOSE60_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:63:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:63:7: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN54 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint561) 
                    stream_CURLY_OPEN.add(CURLY_OPEN54)


                    ID55 = self.match(self.input, ID, self.FOLLOW_ID_in_hint563) 
                    stream_ID.add(ID55)


                    CURLY_CLOSE56 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint565) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE56)


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
                    # 63:33: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:63:36: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:64:7: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN57 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint583) 
                    stream_CURLY_OPEN.add(CURLY_OPEN57)


                    ID58 = self.match(self.input, ID, self.FOLLOW_ID_in_hint585) 
                    stream_ID.add(ID58)


                    # grammar/ShyRecognizerFrontend.g:64:21: ( hint_arg )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == ID or LA13_0 == UNDERSCORE) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyRecognizerFrontend.g:64:21: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint587)
                            hint_arg59 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg59.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    CURLY_CLOSE60 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint591) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE60)


                    # AST Rewrite
                    # elements: ID, hint_arg
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
                    # 64:44: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:64:47: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:64:63: ( hint_arg )+
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
            super(ShyRecognizerFrontend.hint_arg_return, self).__init__()

            self.tree = None





    # $ANTLR start "hint_arg"
    # grammar/ShyRecognizerFrontend.g:66:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set61 = None

        set61_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:66:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set61 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set61))

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
            super(ShyRecognizerFrontend.num_whole_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_whole"
    # grammar/ShyRecognizerFrontend.g:68:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS62 = None
        NUMBER63 = None

        MINUS62_tree = None
        NUMBER63_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:68:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:68:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:68:13: ( MINUS )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == MINUS) :
                    alt15 = 1
                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:68:13: MINUS
                    pass 
                    MINUS62 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole630)
                    MINUS62_tree = self._adaptor.createWithPayload(MINUS62)
                    self._adaptor.addChild(root_0, MINUS62_tree)






                NUMBER63 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole634)
                NUMBER63_tree = self._adaptor.createWithPayload(NUMBER63)
                self._adaptor.addChild(root_0, NUMBER63_tree)





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
            super(ShyRecognizerFrontend.num_fract_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerFrontend.g:69:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS64 = None
        NUMBER65 = None
        DIVIDE66 = None
        NUMBER67 = None

        MINUS64_tree = None
        NUMBER65_tree = None
        DIVIDE66_tree = None
        NUMBER67_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:69:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:69:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:69:13: ( MINUS )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == MINUS) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:69:13: MINUS
                    pass 
                    MINUS64 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract642)
                    MINUS64_tree = self._adaptor.createWithPayload(MINUS64)
                    self._adaptor.addChild(root_0, MINUS64_tree)






                NUMBER65 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract646)
                NUMBER65_tree = self._adaptor.createWithPayload(NUMBER65)
                self._adaptor.addChild(root_0, NUMBER65_tree)



                DIVIDE66 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract648)
                DIVIDE66_tree = self._adaptor.createWithPayload(DIVIDE66)
                self._adaptor.addChild(root_0, DIVIDE66_tree)



                NUMBER67 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract650)
                NUMBER67_tree = self._adaptor.createWithPayload(NUMBER67)
                self._adaptor.addChild(root_0, NUMBER67_tree)





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



    # lookup tables for DFA #12

    DFA12_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA12_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA12_min = DFA.unpack(
        u"\1\7\1\uffff\1\13\1\6\1\13\1\6\2\uffff\1\13"
        )

    DFA12_max = DFA.unpack(
        u"\1\13\1\uffff\1\13\1\46\1\17\1\46\2\uffff\1\17"
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
        DFA.unpack(u"\1\4\4\uffff\1\5\32\uffff\1\5"),
        DFA.unpack(u"\1\6\3\uffff\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\5\32\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\7")
    ]

    # class definition for DFA #12

    class DFA12(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 4, 14, 37])
    FOLLOW_consts_in_start86 = frozenset([1, 4, 14, 37])
    FOLLOW_types_in_start90 = frozenset([1, 4, 14, 37])
    FOLLOW_MODULE_in_module103 = frozenset([11])
    FOLLOW_ID_in_module105 = frozenset([15])
    FOLLOW_NEWLINE_in_module107 = frozenset([1])
    FOLLOW_CONSTS_in_consts130 = frozenset([11])
    FOLLOW_ID_in_consts132 = frozenset([15])
    FOLLOW_NEWLINE_in_consts134 = frozenset([12])
    FOLLOW_INDENT_in_consts142 = frozenset([15])
    FOLLOW_NEWLINE_in_consts144 = frozenset([11])
    FOLLOW_consts_items_in_consts146 = frozenset([8])
    FOLLOW_DEDENT_in_consts148 = frozenset([15])
    FOLLOW_NEWLINE_in_consts150 = frozenset([1])
    FOLLOW_consts_item_in_consts_items180 = frozenset([1, 11])
    FOLLOW_ID_in_consts_item194 = frozenset([13, 16])
    FOLLOW_num_whole_in_consts_item196 = frozenset([15])
    FOLLOW_NEWLINE_in_consts_item198 = frozenset([1])
    FOLLOW_ID_in_consts_item218 = frozenset([13, 16])
    FOLLOW_num_fract_in_consts_item220 = frozenset([15])
    FOLLOW_NEWLINE_in_consts_item222 = frozenset([1])
    FOLLOW_ID_in_consts_item242 = frozenset([10])
    FOLLOW_EXPRESSION_in_consts_item244 = frozenset([15])
    FOLLOW_NEWLINE_in_consts_item246 = frozenset([1])
    FOLLOW_TYPES_in_types275 = frozenset([11])
    FOLLOW_ID_in_types277 = frozenset([15])
    FOLLOW_NEWLINE_in_types279 = frozenset([12])
    FOLLOW_INDENT_in_types287 = frozenset([15])
    FOLLOW_NEWLINE_in_types289 = frozenset([11])
    FOLLOW_types_items_in_types291 = frozenset([8])
    FOLLOW_DEDENT_in_types293 = frozenset([15])
    FOLLOW_NEWLINE_in_types295 = frozenset([1])
    FOLLOW_types_item_in_types_items325 = frozenset([1, 11])
    FOLLOW_ID_in_types_item339 = frozenset([7, 11, 15])
    FOLLOW_types_item_hint_in_types_item341 = frozenset([15])
    FOLLOW_NEWLINE_in_types_item345 = frozenset([1, 12])
    FOLLOW_INDENT_in_types_item355 = frozenset([15])
    FOLLOW_NEWLINE_in_types_item357 = frozenset([7, 11])
    FOLLOW_types_item_hint_in_types_item361 = frozenset([15])
    FOLLOW_NEWLINE_in_types_item363 = frozenset([7, 8, 11])
    FOLLOW_DEDENT_in_types_item369 = frozenset([15])
    FOLLOW_NEWLINE_in_types_item371 = frozenset([1])
    FOLLOW_types_item_attr_in_types_item_hint414 = frozenset([1, 11])
    FOLLOW_hint_in_types_item_hint445 = frozenset([11])
    FOLLOW_types_item_attr_in_types_item_hint447 = frozenset([1, 11])
    FOLLOW_hint_in_types_item_hint477 = frozenset([15])
    FOLLOW_NEWLINE_in_types_item_hint479 = frozenset([12])
    FOLLOW_INDENT_in_types_item_hint481 = frozenset([15])
    FOLLOW_NEWLINE_in_types_item_hint483 = frozenset([11])
    FOLLOW_types_item_attr_in_types_item_hint496 = frozenset([11, 15])
    FOLLOW_NEWLINE_in_types_item_hint500 = frozenset([8, 11])
    FOLLOW_DEDENT_in_types_item_hint506 = frozenset([1])
    FOLLOW_ID_in_types_item_attr538 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint561 = frozenset([11])
    FOLLOW_ID_in_hint563 = frozenset([6])
    FOLLOW_CURLY_CLOSE_in_hint565 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint583 = frozenset([11])
    FOLLOW_ID_in_hint585 = frozenset([11, 38])
    FOLLOW_hint_arg_in_hint587 = frozenset([6, 11, 38])
    FOLLOW_CURLY_CLOSE_in_hint591 = frozenset([1])
    FOLLOW_MINUS_in_num_whole630 = frozenset([16])
    FOLLOW_NUMBER_in_num_whole634 = frozenset([1])
    FOLLOW_MINUS_in_num_fract642 = frozenset([16])
    FOLLOW_NUMBER_in_num_fract646 = frozenset([9])
    FOLLOW_DIVIDE_in_num_fract648 = frozenset([16])
    FOLLOW_NUMBER_in_num_fract650 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
