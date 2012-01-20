# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-20 17:40:59

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
ARROW_LEFT=4
ARROW_RIGHT=5
CONSTS=6
COPY=7
CURLY_CLOSE=8
CURLY_OPEN=9
DEDENT=10
DIVIDE=11
EXPRESSION=12
ID=13
INDENT=14
MINUS=15
MODULE=16
NEWLINE=17
NUMBER=18
PASTE=19
REPLACE=20
STATELESS=21
STRING=22
TREE_ARBITRARY_TOKEN=23
TREE_CONSTS=24
TREE_COPY=25
TREE_COPY_PASTE=26
TREE_EXPRESSION=27
TREE_HINT=28
TREE_HINT_NONE=29
TREE_MODULE=30
TREE_NUM_FRACT=31
TREE_NUM_WHOLE=32
TREE_PASTE=33
TREE_PASTE_REPLACE=34
TREE_PASTE_WITH=35
TREE_STATELESS=36
TREE_TYPES=37
TREE_TYPES_ITEM=38
TREE_TYPES_ITEM_ATTR=39
TREE_TYPES_ITEM_HINT=40
TREE_TYPES_ITEM_HINTS=41
TYPES=42
UNDERSCORE=43
WHITESPACE=44
WITH=45

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", "CURLY_OPEN", 
    "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", "MODULE", 
    "NEWLINE", "NUMBER", "PASTE", "REPLACE", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_STATELESS", 
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
    # grammar/ShyRecognizerFrontend.g:24:1: start : ( module | stateless | consts | types )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        module1 = None

        stateless2 = None

        consts3 = None

        types4 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:24:7: ( ( module | stateless | consts | types )* )
                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types )*
                while True: #loop1
                    alt1 = 5
                    LA1 = self.input.LA(1)
                    if LA1 == MODULE:
                        alt1 = 1
                    elif LA1 == STATELESS:
                        alt1 = 2
                    elif LA1 == CONSTS:
                        alt1 = 3
                    elif LA1 == TYPES:
                        alt1 = 4

                    if alt1 == 1:
                        # grammar/ShyRecognizerFrontend.g:24:11: module
                        pass 
                        self._state.following.append(self.FOLLOW_module_in_start82)
                        module1 = self.module()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, module1.tree)



                    elif alt1 == 2:
                        # grammar/ShyRecognizerFrontend.g:24:20: stateless
                        pass 
                        self._state.following.append(self.FOLLOW_stateless_in_start86)
                        stateless2 = self.stateless()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stateless2.tree)



                    elif alt1 == 3:
                        # grammar/ShyRecognizerFrontend.g:24:32: consts
                        pass 
                        self._state.following.append(self.FOLLOW_consts_in_start90)
                        consts3 = self.consts()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts3.tree)



                    elif alt1 == 4:
                        # grammar/ShyRecognizerFrontend.g:24:41: types
                        pass 
                        self._state.following.append(self.FOLLOW_types_in_start94)
                        types4 = self.types()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types4.tree)



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

        MODULE5 = None
        ID6 = None
        NEWLINE7 = None

        MODULE5_tree = None
        ID6_tree = None
        NEWLINE7_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:26:8: ( MODULE ID NEWLINE -> ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerFrontend.g:26:10: MODULE ID NEWLINE
                pass 
                MODULE5 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module107) 
                stream_MODULE.add(MODULE5)


                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_module109) 
                stream_ID.add(ID6)


                NEWLINE7 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module111) 
                stream_NEWLINE.add(NEWLINE7)


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


    class stateless_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.stateless_return, self).__init__()

            self.tree = None





    # $ANTLR start "stateless"
    # grammar/ShyRecognizerFrontend.g:28:1: stateless : STATELESS ID NEWLINE -> ^( TREE_STATELESS ID ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS8 = None
        ID9 = None
        NEWLINE10 = None

        STATELESS8_tree = None
        ID9_tree = None
        NEWLINE10_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:28:11: ( STATELESS ID NEWLINE -> ^( TREE_STATELESS ID ) )
                # grammar/ShyRecognizerFrontend.g:28:13: STATELESS ID NEWLINE
                pass 
                STATELESS8 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless130) 
                stream_STATELESS.add(STATELESS8)


                ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless132) 
                stream_ID.add(ID9)


                NEWLINE10 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless134) 
                stream_NEWLINE.add(NEWLINE10)


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
                # 28:34: -> ^( TREE_STATELESS ID )
                # grammar/ShyRecognizerFrontend.g:28:37: ^( TREE_STATELESS ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
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

    # $ANTLR end "stateless"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:30:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS11 = None
        ID12 = None
        NEWLINE13 = None
        INDENT14 = None
        NEWLINE15 = None
        DEDENT17 = None
        NEWLINE18 = None
        consts_items16 = None


        CONSTS11_tree = None
        ID12_tree = None
        NEWLINE13_tree = None
        INDENT14_tree = None
        NEWLINE15_tree = None
        DEDENT17_tree = None
        NEWLINE18_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:31:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:31:7: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS11 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts157) 
                stream_CONSTS.add(CONSTS11)


                ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_consts159) 
                stream_ID.add(ID12)


                NEWLINE13 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts161) 
                stream_NEWLINE.add(NEWLINE13)


                INDENT14 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts169) 
                stream_INDENT.add(INDENT14)


                NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts171) 
                stream_NEWLINE.add(NEWLINE15)


                self._state.following.append(self.FOLLOW_consts_items_in_consts173)
                consts_items16 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items16.tree)


                DEDENT17 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts175) 
                stream_DEDENT.add(DEDENT17)


                NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts177) 
                stream_NEWLINE.add(NEWLINE18)


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
                # 33:7: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:33:10: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:35:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item19 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:35:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:35:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:35:16: ( consts_item )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == ID) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyRecognizerFrontend.g:35:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items207)
                        consts_item19 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item19.tree)



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
    # grammar/ShyRecognizerFrontend.g:36:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID20 = None
        NEWLINE22 = None
        ID23 = None
        NEWLINE25 = None
        ID26 = None
        EXPRESSION27 = None
        NEWLINE28 = None
        num_whole21 = None

        num_fract24 = None


        ID20_tree = None
        NEWLINE22_tree = None
        ID23_tree = None
        NEWLINE25_tree = None
        ID26_tree = None
        EXPRESSION27_tree = None
        NEWLINE28_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:37:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerFrontend.g:37:7: ID num_whole NEWLINE
                    pass 
                    ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item221) 
                    stream_ID.add(ID20)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item223)
                    num_whole21 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole21.tree)


                    NEWLINE22 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item225) 
                    stream_NEWLINE.add(NEWLINE22)


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
                    # 37:28: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:37:31: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/ShyRecognizerFrontend.g:38:7: ID num_fract NEWLINE
                    pass 
                    ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item245) 
                    stream_ID.add(ID23)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item247)
                    num_fract24 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract24.tree)


                    NEWLINE25 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item249) 
                    stream_NEWLINE.add(NEWLINE25)


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
                    # 38:28: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:38:31: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:39:7: ID EXPRESSION NEWLINE
                    pass 
                    ID26 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item269) 
                    stream_ID.add(ID26)


                    EXPRESSION27 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item271) 
                    stream_EXPRESSION.add(EXPRESSION27)


                    NEWLINE28 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item273) 
                    stream_NEWLINE.add(NEWLINE28)


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
                    # 39:29: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:39:32: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:42:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES29 = None
        ID30 = None
        NEWLINE31 = None
        INDENT32 = None
        NEWLINE33 = None
        DEDENT35 = None
        NEWLINE36 = None
        types_items34 = None


        TYPES29_tree = None
        ID30_tree = None
        NEWLINE31_tree = None
        INDENT32_tree = None
        NEWLINE33_tree = None
        DEDENT35_tree = None
        NEWLINE36_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:43:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:43:7: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES29 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types302) 
                stream_TYPES.add(TYPES29)


                ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_types304) 
                stream_ID.add(ID30)


                NEWLINE31 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types306) 
                stream_NEWLINE.add(NEWLINE31)


                INDENT32 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types314) 
                stream_INDENT.add(INDENT32)


                NEWLINE33 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types316) 
                stream_NEWLINE.add(NEWLINE33)


                self._state.following.append(self.FOLLOW_types_items_in_types318)
                types_items34 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items34.tree)


                DEDENT35 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types320) 
                stream_DEDENT.add(DEDENT35)


                NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types322) 
                stream_NEWLINE.add(NEWLINE36)


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
                # 45:7: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:45:10: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:47:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item37 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:47:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:47:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:47:15: ( types_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:47:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items352)
                        types_item37 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item37.tree)



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
    # grammar/ShyRecognizerFrontend.g:48:1: types_item : ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID38 = None
        NEWLINE40 = None
        INDENT41 = None
        NEWLINE42 = None
        NEWLINE44 = None
        DEDENT45 = None
        NEWLINE46 = None
        types_item_hint39 = None

        types_item_hint43 = None


        ID38_tree = None
        NEWLINE40_tree = None
        INDENT41_tree = None
        NEWLINE42_tree = None
        NEWLINE44_tree = None
        DEDENT45_tree = None
        NEWLINE46_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item_hint = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:49:5: ( ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* ) )
                # grammar/ShyRecognizerFrontend.g:49:7: ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID38 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item366) 
                stream_ID.add(ID38)


                # grammar/ShyRecognizerFrontend.g:49:10: ( types_item_hint )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == CURLY_OPEN or LA5_0 == ID) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerFrontend.g:49:10: types_item_hint
                    pass 
                    self._state.following.append(self.FOLLOW_types_item_hint_in_types_item368)
                    types_item_hint39 = self.types_item_hint()

                    self._state.following.pop()
                    stream_types_item_hint.add(types_item_hint39.tree)





                NEWLINE40 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item372) 
                stream_NEWLINE.add(NEWLINE40)


                # grammar/ShyRecognizerFrontend.g:50:7: ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == INDENT) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerFrontend.g:50:9: INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT41 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item382) 
                    stream_INDENT.add(INDENT41)


                    NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item384) 
                    stream_NEWLINE.add(NEWLINE42)


                    # grammar/ShyRecognizerFrontend.g:50:24: ( types_item_hint NEWLINE )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == CURLY_OPEN or LA6_0 == ID) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyRecognizerFrontend.g:50:26: types_item_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_hint_in_types_item388)
                            types_item_hint43 = self.types_item_hint()

                            self._state.following.pop()
                            stream_types_item_hint.add(types_item_hint43.tree)


                            NEWLINE44 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item390) 
                            stream_NEWLINE.add(NEWLINE44)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT45 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item396) 
                    stream_DEDENT.add(DEDENT45)


                    NEWLINE46 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item398) 
                    stream_NEWLINE.add(NEWLINE46)





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
                # 51:7: -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* )
                # grammar/ShyRecognizerFrontend.g:51:10: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* )
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

                # grammar/ShyRecognizerFrontend.g:51:54: ( types_item_hint )*
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
    # grammar/ShyRecognizerFrontend.g:53:1: types_item_hint : ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        retval = self.types_item_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE51 = None
        INDENT52 = None
        NEWLINE53 = None
        NEWLINE55 = None
        DEDENT56 = None
        types_item_attr47 = None

        hint48 = None

        types_item_attr49 = None

        hint50 = None

        types_item_attr54 = None


        NEWLINE51_tree = None
        INDENT52_tree = None
        NEWLINE53_tree = None
        NEWLINE55_tree = None
        DEDENT56_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        stream_types_item_attr = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_attr")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:54:5: ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
                alt12 = 3
                alt12 = self.dfa12.predict(self.input)
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:54:7: ( types_item_attr )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:54:7: ( types_item_attr )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == ID) :
                            alt8 = 1


                        if alt8 == 1:
                            # grammar/ShyRecognizerFrontend.g:54:7: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint441)
                            types_item_attr47 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr47.tree)



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
                    # 55:7: -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:55:10: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:55:49: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 2:
                    # grammar/ShyRecognizerFrontend.g:56:7: hint ( types_item_attr )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint472)
                    hint48 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint48.tree)


                    # grammar/ShyRecognizerFrontend.g:56:12: ( types_item_attr )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == ID) :
                            alt9 = 1


                        if alt9 == 1:
                            # grammar/ShyRecognizerFrontend.g:56:12: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint474)
                            types_item_attr49 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr49.tree)



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
                    # 57:7: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:57:10: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:57:39: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 3:
                    # grammar/ShyRecognizerFrontend.g:58:7: hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint504)
                    hint50 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint50.tree)


                    NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint506) 
                    stream_NEWLINE.add(NEWLINE51)


                    INDENT52 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item_hint508) 
                    stream_INDENT.add(INDENT52)


                    NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint510) 
                    stream_NEWLINE.add(NEWLINE53)


                    # grammar/ShyRecognizerFrontend.g:59:9: ( ( types_item_attr )+ NEWLINE )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == ID) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/ShyRecognizerFrontend.g:59:11: ( types_item_attr )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:59:11: ( types_item_attr )+
                            cnt10 = 0
                            while True: #loop10
                                alt10 = 2
                                LA10_0 = self.input.LA(1)

                                if (LA10_0 == ID) :
                                    alt10 = 1


                                if alt10 == 1:
                                    # grammar/ShyRecognizerFrontend.g:59:11: types_item_attr
                                    pass 
                                    self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint523)
                                    types_item_attr54 = self.types_item_attr()

                                    self._state.following.pop()
                                    stream_types_item_attr.add(types_item_attr54.tree)



                                else:
                                    if cnt10 >= 1:
                                        break #loop10

                                    eee = EarlyExitException(10, self.input)
                                    raise eee

                                cnt10 += 1


                            NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint527) 
                            stream_NEWLINE.add(NEWLINE55)



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    DEDENT56 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item_hint533) 
                    stream_DEDENT.add(DEDENT56)


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
                    # 60:7: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:60:10: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:60:39: ( types_item_attr )+
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
    # grammar/ShyRecognizerFrontend.g:62:1: types_item_attr : ID -> ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID57 = None

        ID57_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:62:17: ( ID -> ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/ShyRecognizerFrontend.g:62:19: ID
                pass 
                ID57 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr565) 
                stream_ID.add(ID57)


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
                # 62:22: -> ^( TREE_TYPES_ITEM_ATTR ID )
                # grammar/ShyRecognizerFrontend.g:62:25: ^( TREE_TYPES_ITEM_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:64:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN58 = None
        ID59 = None
        CURLY_CLOSE60 = None
        CURLY_OPEN61 = None
        ID62 = None
        CURLY_CLOSE64 = None
        hint_arg63 = None


        CURLY_OPEN58_tree = None
        ID59_tree = None
        CURLY_CLOSE60_tree = None
        CURLY_OPEN61_tree = None
        ID62_tree = None
        CURLY_CLOSE64_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:65:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:65:7: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN58 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint588) 
                    stream_CURLY_OPEN.add(CURLY_OPEN58)


                    ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_hint590) 
                    stream_ID.add(ID59)


                    CURLY_CLOSE60 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint592) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE60)


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
                    # 65:33: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:65:36: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:66:7: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN61 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint610) 
                    stream_CURLY_OPEN.add(CURLY_OPEN61)


                    ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_hint612) 
                    stream_ID.add(ID62)


                    # grammar/ShyRecognizerFrontend.g:66:21: ( hint_arg )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == ID or LA13_0 == UNDERSCORE) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyRecognizerFrontend.g:66:21: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint614)
                            hint_arg63 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg63.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    CURLY_CLOSE64 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint618) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE64)


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
                    # 66:44: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:66:47: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:66:63: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:68:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set65 = None

        set65_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:68:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set65 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set65))

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
    # grammar/ShyRecognizerFrontend.g:70:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS66 = None
        NUMBER67 = None

        MINUS66_tree = None
        NUMBER67_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:70:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:70:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:70:13: ( MINUS )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == MINUS) :
                    alt15 = 1
                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:70:13: MINUS
                    pass 
                    MINUS66 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole657)
                    MINUS66_tree = self._adaptor.createWithPayload(MINUS66)
                    self._adaptor.addChild(root_0, MINUS66_tree)






                NUMBER67 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole661)
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

    # $ANTLR end "num_whole"


    class num_fract_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.num_fract_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerFrontend.g:71:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS68 = None
        NUMBER69 = None
        DIVIDE70 = None
        NUMBER71 = None

        MINUS68_tree = None
        NUMBER69_tree = None
        DIVIDE70_tree = None
        NUMBER71_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:71:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:71:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:71:13: ( MINUS )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == MINUS) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:71:13: MINUS
                    pass 
                    MINUS68 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract669)
                    MINUS68_tree = self._adaptor.createWithPayload(MINUS68)
                    self._adaptor.addChild(root_0, MINUS68_tree)






                NUMBER69 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract673)
                NUMBER69_tree = self._adaptor.createWithPayload(NUMBER69)
                self._adaptor.addChild(root_0, NUMBER69_tree)



                DIVIDE70 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract675)
                DIVIDE70_tree = self._adaptor.createWithPayload(DIVIDE70)
                self._adaptor.addChild(root_0, DIVIDE70_tree)



                NUMBER71 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract677)
                NUMBER71_tree = self._adaptor.createWithPayload(NUMBER71)
                self._adaptor.addChild(root_0, NUMBER71_tree)





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
        u"\1\11\1\uffff\1\15\1\10\1\15\1\10\2\uffff\1\15"
        )

    DFA12_max = DFA.unpack(
        u"\1\15\1\uffff\1\15\1\53\1\21\1\53\2\uffff\1\21"
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
        DFA.unpack(u"\1\4\4\uffff\1\5\35\uffff\1\5"),
        DFA.unpack(u"\1\6\3\uffff\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\5\35\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\7")
    ]

    # class definition for DFA #12

    class DFA12(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 6, 16, 21, 42])
    FOLLOW_stateless_in_start86 = frozenset([1, 6, 16, 21, 42])
    FOLLOW_consts_in_start90 = frozenset([1, 6, 16, 21, 42])
    FOLLOW_types_in_start94 = frozenset([1, 6, 16, 21, 42])
    FOLLOW_MODULE_in_module107 = frozenset([13])
    FOLLOW_ID_in_module109 = frozenset([17])
    FOLLOW_NEWLINE_in_module111 = frozenset([1])
    FOLLOW_STATELESS_in_stateless130 = frozenset([13])
    FOLLOW_ID_in_stateless132 = frozenset([17])
    FOLLOW_NEWLINE_in_stateless134 = frozenset([1])
    FOLLOW_CONSTS_in_consts157 = frozenset([13])
    FOLLOW_ID_in_consts159 = frozenset([17])
    FOLLOW_NEWLINE_in_consts161 = frozenset([14])
    FOLLOW_INDENT_in_consts169 = frozenset([17])
    FOLLOW_NEWLINE_in_consts171 = frozenset([13])
    FOLLOW_consts_items_in_consts173 = frozenset([10])
    FOLLOW_DEDENT_in_consts175 = frozenset([17])
    FOLLOW_NEWLINE_in_consts177 = frozenset([1])
    FOLLOW_consts_item_in_consts_items207 = frozenset([1, 13])
    FOLLOW_ID_in_consts_item221 = frozenset([15, 18])
    FOLLOW_num_whole_in_consts_item223 = frozenset([17])
    FOLLOW_NEWLINE_in_consts_item225 = frozenset([1])
    FOLLOW_ID_in_consts_item245 = frozenset([15, 18])
    FOLLOW_num_fract_in_consts_item247 = frozenset([17])
    FOLLOW_NEWLINE_in_consts_item249 = frozenset([1])
    FOLLOW_ID_in_consts_item269 = frozenset([12])
    FOLLOW_EXPRESSION_in_consts_item271 = frozenset([17])
    FOLLOW_NEWLINE_in_consts_item273 = frozenset([1])
    FOLLOW_TYPES_in_types302 = frozenset([13])
    FOLLOW_ID_in_types304 = frozenset([17])
    FOLLOW_NEWLINE_in_types306 = frozenset([14])
    FOLLOW_INDENT_in_types314 = frozenset([17])
    FOLLOW_NEWLINE_in_types316 = frozenset([13])
    FOLLOW_types_items_in_types318 = frozenset([10])
    FOLLOW_DEDENT_in_types320 = frozenset([17])
    FOLLOW_NEWLINE_in_types322 = frozenset([1])
    FOLLOW_types_item_in_types_items352 = frozenset([1, 13])
    FOLLOW_ID_in_types_item366 = frozenset([9, 13, 17])
    FOLLOW_types_item_hint_in_types_item368 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item372 = frozenset([1, 14])
    FOLLOW_INDENT_in_types_item382 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item384 = frozenset([9, 13])
    FOLLOW_types_item_hint_in_types_item388 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item390 = frozenset([9, 10, 13])
    FOLLOW_DEDENT_in_types_item396 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item398 = frozenset([1])
    FOLLOW_types_item_attr_in_types_item_hint441 = frozenset([1, 13])
    FOLLOW_hint_in_types_item_hint472 = frozenset([13])
    FOLLOW_types_item_attr_in_types_item_hint474 = frozenset([1, 13])
    FOLLOW_hint_in_types_item_hint504 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item_hint506 = frozenset([14])
    FOLLOW_INDENT_in_types_item_hint508 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item_hint510 = frozenset([13])
    FOLLOW_types_item_attr_in_types_item_hint523 = frozenset([13, 17])
    FOLLOW_NEWLINE_in_types_item_hint527 = frozenset([10, 13])
    FOLLOW_DEDENT_in_types_item_hint533 = frozenset([1])
    FOLLOW_ID_in_types_item_attr565 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint588 = frozenset([13])
    FOLLOW_ID_in_hint590 = frozenset([8])
    FOLLOW_CURLY_CLOSE_in_hint592 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint610 = frozenset([13])
    FOLLOW_ID_in_hint612 = frozenset([13, 43])
    FOLLOW_hint_arg_in_hint614 = frozenset([8, 13, 43])
    FOLLOW_CURLY_CLOSE_in_hint618 = frozenset([1])
    FOLLOW_MINUS_in_num_whole657 = frozenset([18])
    FOLLOW_NUMBER_in_num_whole661 = frozenset([1])
    FOLLOW_MINUS_in_num_fract669 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract673 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract675 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract677 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
