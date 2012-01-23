# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-23 14:34:18

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
PROC=20
REPLACE=21
STATELESS=22
STRING=23
TREE_ARBITRARY_TOKEN=24
TREE_CONSTS=25
TREE_COPY=26
TREE_COPY_PASTE=27
TREE_EXPRESSION=28
TREE_HINT=29
TREE_HINT_NONE=30
TREE_MODULE=31
TREE_NUM_FRACT=32
TREE_NUM_WHOLE=33
TREE_PASTE=34
TREE_PASTE_REPLACE=35
TREE_PASTE_WITH=36
TREE_PROC=37
TREE_STATELESS=38
TREE_TYPES=39
TREE_TYPES_ITEM=40
TREE_TYPES_ITEM_ATTR=41
TREE_TYPES_ITEM_HINT=42
TREE_TYPES_ITEM_HINTS=43
TYPES=44
UNDERSCORE=45
WHITESPACE=46
WITH=47

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", "CURLY_OPEN", 
    "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", "MODULE", 
    "NEWLINE", "NUMBER", "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", 
    "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_STATELESS", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_TYPES_ITEM_ATTR", 
    "TREE_TYPES_ITEM_HINT", "TREE_TYPES_ITEM_HINTS", "TYPES", "UNDERSCORE", 
    "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
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
                # grammar/ShyRecognizerFrontend.g:27:5: ( MODULE ID NEWLINE -> ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerFrontend.g:27:9: MODULE ID NEWLINE
                pass 
                MODULE5 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module113) 
                stream_MODULE.add(MODULE5)


                ID6 = self.match(self.input, ID, self.FOLLOW_ID_in_module115) 
                stream_ID.add(ID6)


                NEWLINE7 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module117) 
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
                # 27:27: -> ^( TREE_MODULE ID )
                # grammar/ShyRecognizerFrontend.g:27:30: ^( TREE_MODULE ID )
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
    # grammar/ShyRecognizerFrontend.g:30:1: stateless : ( STATELESS ID NEWLINE -> ^( TREE_STATELESS ID ) | STATELESS ID NEWLINE INDENT NEWLINE ( proc )+ DEDENT NEWLINE -> ^( TREE_STATELESS ID ( proc )+ ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS8 = None
        ID9 = None
        NEWLINE10 = None
        STATELESS11 = None
        ID12 = None
        NEWLINE13 = None
        INDENT14 = None
        NEWLINE15 = None
        DEDENT17 = None
        NEWLINE18 = None
        proc16 = None


        STATELESS8_tree = None
        ID9_tree = None
        NEWLINE10_tree = None
        STATELESS11_tree = None
        ID12_tree = None
        NEWLINE13_tree = None
        INDENT14_tree = None
        NEWLINE15_tree = None
        DEDENT17_tree = None
        NEWLINE18_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:31:5: ( STATELESS ID NEWLINE -> ^( TREE_STATELESS ID ) | STATELESS ID NEWLINE INDENT NEWLINE ( proc )+ DEDENT NEWLINE -> ^( TREE_STATELESS ID ( proc )+ ) )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == STATELESS) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == ID) :
                        LA3_2 = self.input.LA(3)

                        if (LA3_2 == NEWLINE) :
                            LA3_3 = self.input.LA(4)

                            if (LA3_3 == INDENT) :
                                alt3 = 2
                            elif (LA3_3 == EOF or LA3_3 == CONSTS or LA3_3 == MODULE or LA3_3 == STATELESS or LA3_3 == TYPES) :
                                alt3 = 1
                            else:
                                nvae = NoViableAltException("", 3, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 3, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyRecognizerFrontend.g:31:9: STATELESS ID NEWLINE
                    pass 
                    STATELESS8 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless146) 
                    stream_STATELESS.add(STATELESS8)


                    ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless148) 
                    stream_ID.add(ID9)


                    NEWLINE10 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless150) 
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
                    # 32:9: -> ^( TREE_STATELESS ID )
                    # grammar/ShyRecognizerFrontend.g:32:12: ^( TREE_STATELESS ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 2:
                    # grammar/ShyRecognizerFrontend.g:33:9: STATELESS ID NEWLINE INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    STATELESS11 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless178) 
                    stream_STATELESS.add(STATELESS11)


                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless180) 
                    stream_ID.add(ID12)


                    NEWLINE13 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless182) 
                    stream_NEWLINE.add(NEWLINE13)


                    INDENT14 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless184) 
                    stream_INDENT.add(INDENT14)


                    NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless186) 
                    stream_NEWLINE.add(NEWLINE15)


                    # grammar/ShyRecognizerFrontend.g:33:45: ( proc )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == PROC) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyRecognizerFrontend.g:33:45: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless188)
                            proc16 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc16.tree)



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    DEDENT17 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless192) 
                    stream_DEDENT.add(DEDENT17)


                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless194) 
                    stream_NEWLINE.add(NEWLINE18)


                    # AST Rewrite
                    # elements: proc, ID
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
                    # 34:9: -> ^( TREE_STATELESS ID ( proc )+ )
                    # grammar/ShyRecognizerFrontend.g:34:12: ^( TREE_STATELESS ID ( proc )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:34:33: ( proc )+
                    if not (stream_proc.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_proc.hasNext():
                        self._adaptor.addChild(root_1, stream_proc.nextTree())


                    stream_proc.reset()

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


    class proc_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc"
    # grammar/ShyRecognizerFrontend.g:37:1: proc : PROC ID NEWLINE -> ^( TREE_PROC ID ) ;
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC19 = None
        ID20 = None
        NEWLINE21 = None

        PROC19_tree = None
        ID20_tree = None
        NEWLINE21_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:38:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) )
                # grammar/ShyRecognizerFrontend.g:38:9: PROC ID NEWLINE
                pass 
                PROC19 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc235) 
                stream_PROC.add(PROC19)


                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_proc237) 
                stream_ID.add(ID20)


                NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc239) 
                stream_NEWLINE.add(NEWLINE21)


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
                # 39:9: -> ^( TREE_PROC ID )
                # grammar/ShyRecognizerFrontend.g:39:12: ^( TREE_PROC ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
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

    # $ANTLR end "proc"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:42:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS22 = None
        ID23 = None
        NEWLINE24 = None
        INDENT25 = None
        NEWLINE26 = None
        DEDENT28 = None
        NEWLINE29 = None
        consts_items27 = None


        CONSTS22_tree = None
        ID23_tree = None
        NEWLINE24_tree = None
        INDENT25_tree = None
        NEWLINE26_tree = None
        DEDENT28_tree = None
        NEWLINE29_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:43:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:43:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS22 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts276) 
                stream_CONSTS.add(CONSTS22)


                ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_consts278) 
                stream_ID.add(ID23)


                NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts280) 
                stream_NEWLINE.add(NEWLINE24)


                INDENT25 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts290) 
                stream_INDENT.add(INDENT25)


                NEWLINE26 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts292) 
                stream_NEWLINE.add(NEWLINE26)


                self._state.following.append(self.FOLLOW_consts_items_in_consts294)
                consts_items27 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items27.tree)


                DEDENT28 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts296) 
                stream_DEDENT.add(DEDENT28)


                NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts298) 
                stream_NEWLINE.add(NEWLINE29)


                # AST Rewrite
                # elements: consts_items, ID
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
                # 45:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:45:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:47:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item30 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:47:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:47:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:47:16: ( consts_item )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ID) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:47:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items330)
                        consts_item30 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item30.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:48:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID31 = None
        NEWLINE33 = None
        ID34 = None
        NEWLINE36 = None
        ID37 = None
        EXPRESSION38 = None
        NEWLINE39 = None
        num_whole32 = None

        num_fract35 = None


        ID31_tree = None
        NEWLINE33_tree = None
        ID34_tree = None
        NEWLINE36_tree = None
        ID37_tree = None
        EXPRESSION38_tree = None
        NEWLINE39_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:49:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt5 = 3
                LA5_0 = self.input.LA(1)

                if (LA5_0 == ID) :
                    LA5 = self.input.LA(2)
                    if LA5 == EXPRESSION:
                        alt5 = 3
                    elif LA5 == MINUS:
                        LA5_3 = self.input.LA(3)

                        if (LA5_3 == NUMBER) :
                            LA5_4 = self.input.LA(4)

                            if (LA5_4 == DIVIDE) :
                                alt5 = 2
                            elif (LA5_4 == NEWLINE) :
                                alt5 = 1
                            else:
                                nvae = NoViableAltException("", 5, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 5, 3, self.input)

                            raise nvae


                    elif LA5 == NUMBER:
                        LA5_4 = self.input.LA(3)

                        if (LA5_4 == DIVIDE) :
                            alt5 = 2
                        elif (LA5_4 == NEWLINE) :
                            alt5 = 1
                        else:
                            nvae = NoViableAltException("", 5, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 5, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae


                if alt5 == 1:
                    # grammar/ShyRecognizerFrontend.g:49:9: ID num_whole NEWLINE
                    pass 
                    ID31 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item346) 
                    stream_ID.add(ID31)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item348)
                    num_whole32 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole32.tree)


                    NEWLINE33 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item350) 
                    stream_NEWLINE.add(NEWLINE33)


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
                    # 49:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:49:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt5 == 2:
                    # grammar/ShyRecognizerFrontend.g:50:9: ID num_fract NEWLINE
                    pass 
                    ID34 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item372) 
                    stream_ID.add(ID34)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item374)
                    num_fract35 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract35.tree)


                    NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item376) 
                    stream_NEWLINE.add(NEWLINE36)


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
                    # 50:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:50:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt5 == 3:
                    # grammar/ShyRecognizerFrontend.g:51:9: ID EXPRESSION NEWLINE
                    pass 
                    ID37 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item398) 
                    stream_ID.add(ID37)


                    EXPRESSION38 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item400) 
                    stream_EXPRESSION.add(EXPRESSION38)


                    NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item402) 
                    stream_NEWLINE.add(NEWLINE39)


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
                    # 51:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:51:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:54:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES40 = None
        ID41 = None
        NEWLINE42 = None
        INDENT43 = None
        NEWLINE44 = None
        DEDENT46 = None
        NEWLINE47 = None
        types_items45 = None


        TYPES40_tree = None
        ID41_tree = None
        NEWLINE42_tree = None
        INDENT43_tree = None
        NEWLINE44_tree = None
        DEDENT46_tree = None
        NEWLINE47_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:55:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:55:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES40 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types433) 
                stream_TYPES.add(TYPES40)


                ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_types435) 
                stream_ID.add(ID41)


                NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types437) 
                stream_NEWLINE.add(NEWLINE42)


                INDENT43 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types447) 
                stream_INDENT.add(INDENT43)


                NEWLINE44 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types449) 
                stream_NEWLINE.add(NEWLINE44)


                self._state.following.append(self.FOLLOW_types_items_in_types451)
                types_items45 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items45.tree)


                DEDENT46 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types453) 
                stream_DEDENT.add(DEDENT46)


                NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types455) 
                stream_NEWLINE.add(NEWLINE47)


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
                # 57:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:57:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:59:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item48 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:59:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:59:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:59:15: ( types_item )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == ID) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyRecognizerFrontend.g:59:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items487)
                        types_item48 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item48.tree)



                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1




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
    # grammar/ShyRecognizerFrontend.g:60:1: types_item : ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID49 = None
        NEWLINE51 = None
        INDENT52 = None
        NEWLINE53 = None
        NEWLINE55 = None
        DEDENT56 = None
        NEWLINE57 = None
        types_item_hint50 = None

        types_item_hint54 = None


        ID49_tree = None
        NEWLINE51_tree = None
        INDENT52_tree = None
        NEWLINE53_tree = None
        NEWLINE55_tree = None
        DEDENT56_tree = None
        NEWLINE57_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item_hint = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:61:5: ( ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* ) )
                # grammar/ShyRecognizerFrontend.g:61:9: ID ( types_item_hint )? NEWLINE ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID49 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item503) 
                stream_ID.add(ID49)


                # grammar/ShyRecognizerFrontend.g:61:12: ( types_item_hint )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == CURLY_OPEN or LA7_0 == ID) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerFrontend.g:61:12: types_item_hint
                    pass 
                    self._state.following.append(self.FOLLOW_types_item_hint_in_types_item505)
                    types_item_hint50 = self.types_item_hint()

                    self._state.following.pop()
                    stream_types_item_hint.add(types_item_hint50.tree)





                NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item509) 
                stream_NEWLINE.add(NEWLINE51)


                # grammar/ShyRecognizerFrontend.g:62:9: ( INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == INDENT) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:62:11: INDENT NEWLINE ( types_item_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT52 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item521) 
                    stream_INDENT.add(INDENT52)


                    NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item523) 
                    stream_NEWLINE.add(NEWLINE53)


                    # grammar/ShyRecognizerFrontend.g:62:26: ( types_item_hint NEWLINE )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == CURLY_OPEN or LA8_0 == ID) :
                            alt8 = 1


                        if alt8 == 1:
                            # grammar/ShyRecognizerFrontend.g:62:28: types_item_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_hint_in_types_item527)
                            types_item_hint54 = self.types_item_hint()

                            self._state.following.pop()
                            stream_types_item_hint.add(types_item_hint54.tree)


                            NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item529) 
                            stream_NEWLINE.add(NEWLINE55)



                        else:
                            if cnt8 >= 1:
                                break #loop8

                            eee = EarlyExitException(8, self.input)
                            raise eee

                        cnt8 += 1


                    DEDENT56 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item535) 
                    stream_DEDENT.add(DEDENT56)


                    NEWLINE57 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item537) 
                    stream_NEWLINE.add(NEWLINE57)





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
                # 63:9: -> ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* )
                # grammar/ShyRecognizerFrontend.g:63:12: ^( TREE_TYPES_ITEM ID TREE_TYPES_ITEM_HINTS ( types_item_hint )* )
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

                # grammar/ShyRecognizerFrontend.g:63:56: ( types_item_hint )*
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
    # grammar/ShyRecognizerFrontend.g:65:1: types_item_hint : ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) );
    def types_item_hint(self, ):
        retval = self.types_item_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE62 = None
        INDENT63 = None
        NEWLINE64 = None
        NEWLINE66 = None
        DEDENT67 = None
        types_item_attr58 = None

        hint59 = None

        types_item_attr60 = None

        hint61 = None

        types_item_attr65 = None


        NEWLINE62_tree = None
        INDENT63_tree = None
        NEWLINE64_tree = None
        NEWLINE66_tree = None
        DEDENT67_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        stream_types_item_attr = RewriteRuleSubtreeStream(self._adaptor, "rule types_item_attr")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:66:5: ( ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ ) | hint ( types_item_attr )+ -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) | hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ ) )
                alt14 = 3
                alt14 = self.dfa14.predict(self.input)
                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:66:9: ( types_item_attr )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:66:9: ( types_item_attr )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == ID) :
                            alt10 = 1


                        if alt10 == 1:
                            # grammar/ShyRecognizerFrontend.g:66:9: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint584)
                            types_item_attr58 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr58.tree)



                        else:
                            if cnt10 >= 1:
                                break #loop10

                            eee = EarlyExitException(10, self.input)
                            raise eee

                        cnt10 += 1


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
                    # 67:9: -> ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:67:12: ^( TREE_TYPES_ITEM_HINT TREE_HINT_NONE ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:67:51: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt14 == 2:
                    # grammar/ShyRecognizerFrontend.g:68:9: hint ( types_item_attr )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint619)
                    hint59 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint59.tree)


                    # grammar/ShyRecognizerFrontend.g:68:14: ( types_item_attr )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == ID) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/ShyRecognizerFrontend.g:68:14: types_item_attr
                            pass 
                            self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint621)
                            types_item_attr60 = self.types_item_attr()

                            self._state.following.pop()
                            stream_types_item_attr.add(types_item_attr60.tree)



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


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
                    # 69:9: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:69:12: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:69:41: ( types_item_attr )+
                    if not (stream_types_item_attr.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_types_item_attr.hasNext():
                        self._adaptor.addChild(root_1, stream_types_item_attr.nextTree())


                    stream_types_item_attr.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt14 == 3:
                    # grammar/ShyRecognizerFrontend.g:70:9: hint NEWLINE INDENT NEWLINE ( ( types_item_attr )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_types_item_hint655)
                    hint61 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint61.tree)


                    NEWLINE62 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint657) 
                    stream_NEWLINE.add(NEWLINE62)


                    INDENT63 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types_item_hint659) 
                    stream_INDENT.add(INDENT63)


                    NEWLINE64 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint661) 
                    stream_NEWLINE.add(NEWLINE64)


                    # grammar/ShyRecognizerFrontend.g:71:13: ( ( types_item_attr )+ NEWLINE )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == ID) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyRecognizerFrontend.g:71:15: ( types_item_attr )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:71:15: ( types_item_attr )+
                            cnt12 = 0
                            while True: #loop12
                                alt12 = 2
                                LA12_0 = self.input.LA(1)

                                if (LA12_0 == ID) :
                                    alt12 = 1


                                if alt12 == 1:
                                    # grammar/ShyRecognizerFrontend.g:71:15: types_item_attr
                                    pass 
                                    self._state.following.append(self.FOLLOW_types_item_attr_in_types_item_hint678)
                                    types_item_attr65 = self.types_item_attr()

                                    self._state.following.pop()
                                    stream_types_item_attr.add(types_item_attr65.tree)



                                else:
                                    if cnt12 >= 1:
                                        break #loop12

                                    eee = EarlyExitException(12, self.input)
                                    raise eee

                                cnt12 += 1


                            NEWLINE66 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types_item_hint682) 
                            stream_NEWLINE.add(NEWLINE66)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    DEDENT67 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types_item_hint688) 
                    stream_DEDENT.add(DEDENT67)


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
                    # 72:9: -> ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    # grammar/ShyRecognizerFrontend.g:72:12: ^( TREE_TYPES_ITEM_HINT hint ( types_item_attr )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_TYPES_ITEM_HINT, "TREE_TYPES_ITEM_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:72:41: ( types_item_attr )+
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
    # grammar/ShyRecognizerFrontend.g:74:1: types_item_attr : ID -> ^( TREE_TYPES_ITEM_ATTR ID ) ;
    def types_item_attr(self, ):
        retval = self.types_item_attr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID68 = None

        ID68_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:74:17: ( ID -> ^( TREE_TYPES_ITEM_ATTR ID ) )
                # grammar/ShyRecognizerFrontend.g:74:19: ID
                pass 
                ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item_attr722) 
                stream_ID.add(ID68)


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
                # 74:22: -> ^( TREE_TYPES_ITEM_ATTR ID )
                # grammar/ShyRecognizerFrontend.g:74:25: ^( TREE_TYPES_ITEM_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:76:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN69 = None
        ID70 = None
        CURLY_CLOSE71 = None
        CURLY_OPEN72 = None
        ID73 = None
        CURLY_CLOSE75 = None
        hint_arg74 = None


        CURLY_OPEN69_tree = None
        ID70_tree = None
        CURLY_CLOSE71_tree = None
        CURLY_OPEN72_tree = None
        ID73_tree = None
        CURLY_CLOSE75_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:77:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == CURLY_OPEN) :
                    LA16_1 = self.input.LA(2)

                    if (LA16_1 == ID) :
                        LA16_2 = self.input.LA(3)

                        if (LA16_2 == CURLY_CLOSE) :
                            alt16 = 1
                        elif (LA16_2 == ID or LA16_2 == UNDERSCORE) :
                            alt16 = 2
                        else:
                            nvae = NoViableAltException("", 16, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 16, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:77:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN69 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint747) 
                    stream_CURLY_OPEN.add(CURLY_OPEN69)


                    ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_hint749) 
                    stream_ID.add(ID70)


                    CURLY_CLOSE71 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint751) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE71)


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
                    # 77:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:77:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt16 == 2:
                    # grammar/ShyRecognizerFrontend.g:78:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN72 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint771) 
                    stream_CURLY_OPEN.add(CURLY_OPEN72)


                    ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_hint773) 
                    stream_ID.add(ID73)


                    # grammar/ShyRecognizerFrontend.g:78:23: ( hint_arg )+
                    cnt15 = 0
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == ID or LA15_0 == UNDERSCORE) :
                            alt15 = 1


                        if alt15 == 1:
                            # grammar/ShyRecognizerFrontend.g:78:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint775)
                            hint_arg74 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg74.tree)



                        else:
                            if cnt15 >= 1:
                                break #loop15

                            eee = EarlyExitException(15, self.input)
                            raise eee

                        cnt15 += 1


                    CURLY_CLOSE75 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint779) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE75)


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
                    # 78:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:78:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:78:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:80:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set76 = None

        set76_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:80:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set76 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set76))

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
    # grammar/ShyRecognizerFrontend.g:82:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS77 = None
        NUMBER78 = None

        MINUS77_tree = None
        NUMBER78_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:82:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:82:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:82:13: ( MINUS )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == MINUS) :
                    alt17 = 1
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:82:13: MINUS
                    pass 
                    MINUS77 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole818)
                    MINUS77_tree = self._adaptor.createWithPayload(MINUS77)
                    self._adaptor.addChild(root_0, MINUS77_tree)






                NUMBER78 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole822)
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

    # $ANTLR end "num_whole"


    class num_fract_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.num_fract_return, self).__init__()

            self.tree = None





    # $ANTLR start "num_fract"
    # grammar/ShyRecognizerFrontend.g:83:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS79 = None
        NUMBER80 = None
        DIVIDE81 = None
        NUMBER82 = None

        MINUS79_tree = None
        NUMBER80_tree = None
        DIVIDE81_tree = None
        NUMBER82_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:83:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:83:13: ( MINUS )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == MINUS) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:83:13: MINUS
                    pass 
                    MINUS79 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract830)
                    MINUS79_tree = self._adaptor.createWithPayload(MINUS79)
                    self._adaptor.addChild(root_0, MINUS79_tree)






                NUMBER80 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract834)
                NUMBER80_tree = self._adaptor.createWithPayload(NUMBER80)
                self._adaptor.addChild(root_0, NUMBER80_tree)



                DIVIDE81 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract836)
                DIVIDE81_tree = self._adaptor.createWithPayload(DIVIDE81)
                self._adaptor.addChild(root_0, DIVIDE81_tree)



                NUMBER82 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract838)
                NUMBER82_tree = self._adaptor.createWithPayload(NUMBER82)
                self._adaptor.addChild(root_0, NUMBER82_tree)





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



    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\11\1\uffff\1\15\1\10\1\15\1\10\2\uffff\1\15"
        )

    DFA14_max = DFA.unpack(
        u"\1\15\1\uffff\1\15\1\55\1\21\1\55\2\uffff\1\21"
        )

    DFA14_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA14_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA14_transition = [
        DFA.unpack(u"\1\2\3\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\4\uffff\1\5\37\uffff\1\5"),
        DFA.unpack(u"\1\6\3\uffff\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\5\37\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\7")
    ]

    # class definition for DFA #14

    class DFA14(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 6, 16, 22, 44])
    FOLLOW_stateless_in_start86 = frozenset([1, 6, 16, 22, 44])
    FOLLOW_consts_in_start90 = frozenset([1, 6, 16, 22, 44])
    FOLLOW_types_in_start94 = frozenset([1, 6, 16, 22, 44])
    FOLLOW_MODULE_in_module113 = frozenset([13])
    FOLLOW_ID_in_module115 = frozenset([17])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([13])
    FOLLOW_ID_in_stateless148 = frozenset([17])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1])
    FOLLOW_STATELESS_in_stateless178 = frozenset([13])
    FOLLOW_ID_in_stateless180 = frozenset([17])
    FOLLOW_NEWLINE_in_stateless182 = frozenset([14])
    FOLLOW_INDENT_in_stateless184 = frozenset([17])
    FOLLOW_NEWLINE_in_stateless186 = frozenset([20])
    FOLLOW_proc_in_stateless188 = frozenset([10, 20])
    FOLLOW_DEDENT_in_stateless192 = frozenset([17])
    FOLLOW_NEWLINE_in_stateless194 = frozenset([1])
    FOLLOW_PROC_in_proc235 = frozenset([13])
    FOLLOW_ID_in_proc237 = frozenset([17])
    FOLLOW_NEWLINE_in_proc239 = frozenset([1])
    FOLLOW_CONSTS_in_consts276 = frozenset([13])
    FOLLOW_ID_in_consts278 = frozenset([17])
    FOLLOW_NEWLINE_in_consts280 = frozenset([14])
    FOLLOW_INDENT_in_consts290 = frozenset([17])
    FOLLOW_NEWLINE_in_consts292 = frozenset([13])
    FOLLOW_consts_items_in_consts294 = frozenset([10])
    FOLLOW_DEDENT_in_consts296 = frozenset([17])
    FOLLOW_NEWLINE_in_consts298 = frozenset([1])
    FOLLOW_consts_item_in_consts_items330 = frozenset([1, 13])
    FOLLOW_ID_in_consts_item346 = frozenset([15, 18])
    FOLLOW_num_whole_in_consts_item348 = frozenset([17])
    FOLLOW_NEWLINE_in_consts_item350 = frozenset([1])
    FOLLOW_ID_in_consts_item372 = frozenset([15, 18])
    FOLLOW_num_fract_in_consts_item374 = frozenset([17])
    FOLLOW_NEWLINE_in_consts_item376 = frozenset([1])
    FOLLOW_ID_in_consts_item398 = frozenset([12])
    FOLLOW_EXPRESSION_in_consts_item400 = frozenset([17])
    FOLLOW_NEWLINE_in_consts_item402 = frozenset([1])
    FOLLOW_TYPES_in_types433 = frozenset([13])
    FOLLOW_ID_in_types435 = frozenset([17])
    FOLLOW_NEWLINE_in_types437 = frozenset([14])
    FOLLOW_INDENT_in_types447 = frozenset([17])
    FOLLOW_NEWLINE_in_types449 = frozenset([13])
    FOLLOW_types_items_in_types451 = frozenset([10])
    FOLLOW_DEDENT_in_types453 = frozenset([17])
    FOLLOW_NEWLINE_in_types455 = frozenset([1])
    FOLLOW_types_item_in_types_items487 = frozenset([1, 13])
    FOLLOW_ID_in_types_item503 = frozenset([9, 13, 17])
    FOLLOW_types_item_hint_in_types_item505 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item509 = frozenset([1, 14])
    FOLLOW_INDENT_in_types_item521 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item523 = frozenset([9, 13])
    FOLLOW_types_item_hint_in_types_item527 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item529 = frozenset([9, 10, 13])
    FOLLOW_DEDENT_in_types_item535 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item537 = frozenset([1])
    FOLLOW_types_item_attr_in_types_item_hint584 = frozenset([1, 13])
    FOLLOW_hint_in_types_item_hint619 = frozenset([13])
    FOLLOW_types_item_attr_in_types_item_hint621 = frozenset([1, 13])
    FOLLOW_hint_in_types_item_hint655 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item_hint657 = frozenset([14])
    FOLLOW_INDENT_in_types_item_hint659 = frozenset([17])
    FOLLOW_NEWLINE_in_types_item_hint661 = frozenset([13])
    FOLLOW_types_item_attr_in_types_item_hint678 = frozenset([13, 17])
    FOLLOW_NEWLINE_in_types_item_hint682 = frozenset([10, 13])
    FOLLOW_DEDENT_in_types_item_hint688 = frozenset([1])
    FOLLOW_ID_in_types_item_attr722 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint747 = frozenset([13])
    FOLLOW_ID_in_hint749 = frozenset([8])
    FOLLOW_CURLY_CLOSE_in_hint751 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint771 = frozenset([13])
    FOLLOW_ID_in_hint773 = frozenset([13, 45])
    FOLLOW_hint_arg_in_hint775 = frozenset([8, 13, 45])
    FOLLOW_CURLY_CLOSE_in_hint779 = frozenset([1])
    FOLLOW_MINUS_in_num_whole818 = frozenset([18])
    FOLLOW_NUMBER_in_num_whole822 = frozenset([1])
    FOLLOW_MINUS_in_num_fract830 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract834 = frozenset([11])
    FOLLOW_DIVIDE_in_num_fract836 = frozenset([18])
    FOLLOW_NUMBER_in_num_fract838 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
