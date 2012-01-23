# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-23 18:51:37

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
ARGS=4
ARROW_LEFT=5
ARROW_RIGHT=6
CONSTS=7
COPY=8
CURLY_CLOSE=9
CURLY_OPEN=10
DEDENT=11
DIVIDE=12
EXPRESSION=13
ID=14
INDENT=15
MINUS=16
MODULE=17
NEWLINE=18
NUMBER=19
PASTE=20
PROC=21
REPLACE=22
STATELESS=23
STRING=24
TREE_ARBITRARY_TOKEN=25
TREE_CONSTS=26
TREE_COPY=27
TREE_COPY_PASTE=28
TREE_EXPRESSION=29
TREE_HINT=30
TREE_HINT_NONE=31
TREE_MODULE=32
TREE_NUM_FRACT=33
TREE_NUM_WHOLE=34
TREE_PASTE=35
TREE_PASTE_REPLACE=36
TREE_PASTE_WITH=37
TREE_PROC=38
TREE_PROC_ARGS=39
TREE_STATELESS=40
TREE_TYPES=41
TREE_TYPES_ITEM=42
TREE_VAR=43
TREE_VARS_HINT=44
TREE_VAR_HINT=45
TYPES=46
UNDERSCORE=47
WHITESPACE=48
WITH=49

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NEWLINE", "NUMBER", "PASTE", "PROC", "REPLACE", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_STATELESS", "TREE_TYPES", "TREE_TYPES_ITEM", 
    "TREE_VAR", "TREE_VARS_HINT", "TREE_VAR_HINT", "TYPES", "UNDERSCORE", 
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

        self.dfa15 = self.DFA15(
            self, 15,
            eot = self.DFA15_eot,
            eof = self.DFA15_eof,
            min = self.DFA15_min,
            max = self.DFA15_max,
            accept = self.DFA15_accept,
            special = self.DFA15_special,
            transition = self.DFA15_transition
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
                    # elements: ID, proc
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
    # grammar/ShyRecognizerFrontend.g:37:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE proc_args DEDENT NEWLINE -> ^( TREE_PROC ID proc_args ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC19 = None
        ID20 = None
        NEWLINE21 = None
        PROC22 = None
        ID23 = None
        NEWLINE24 = None
        INDENT25 = None
        NEWLINE26 = None
        DEDENT28 = None
        NEWLINE29 = None
        proc_args27 = None


        PROC19_tree = None
        ID20_tree = None
        NEWLINE21_tree = None
        PROC22_tree = None
        ID23_tree = None
        NEWLINE24_tree = None
        INDENT25_tree = None
        NEWLINE26_tree = None
        DEDENT28_tree = None
        NEWLINE29_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_proc_args = RewriteRuleSubtreeStream(self._adaptor, "rule proc_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:38:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE proc_args DEDENT NEWLINE -> ^( TREE_PROC ID proc_args ) )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == PROC) :
                    LA4_1 = self.input.LA(2)

                    if (LA4_1 == ID) :
                        LA4_2 = self.input.LA(3)

                        if (LA4_2 == NEWLINE) :
                            LA4_3 = self.input.LA(4)

                            if (LA4_3 == INDENT) :
                                alt4 = 2
                            elif (LA4_3 == DEDENT or LA4_3 == PROC) :
                                alt4 = 1
                            else:
                                nvae = NoViableAltException("", 4, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 4, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
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




                elif alt4 == 2:
                    # grammar/ShyRecognizerFrontend.g:40:9: PROC ID NEWLINE INDENT NEWLINE proc_args DEDENT NEWLINE
                    pass 
                    PROC22 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc267) 
                    stream_PROC.add(PROC22)


                    ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_proc269) 
                    stream_ID.add(ID23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc271) 
                    stream_NEWLINE.add(NEWLINE24)


                    INDENT25 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc273) 
                    stream_INDENT.add(INDENT25)


                    NEWLINE26 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc275) 
                    stream_NEWLINE.add(NEWLINE26)


                    self._state.following.append(self.FOLLOW_proc_args_in_proc277)
                    proc_args27 = self.proc_args()

                    self._state.following.pop()
                    stream_proc_args.add(proc_args27.tree)


                    DEDENT28 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc279) 
                    stream_DEDENT.add(DEDENT28)


                    NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc281) 
                    stream_NEWLINE.add(NEWLINE29)


                    # AST Rewrite
                    # elements: ID, proc_args
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
                    # 41:9: -> ^( TREE_PROC ID proc_args )
                    # grammar/ShyRecognizerFrontend.g:41:12: ^( TREE_PROC ID proc_args )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_proc_args.nextTree())

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


    class proc_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_args_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc_args"
    # grammar/ShyRecognizerFrontend.g:44:1: proc_args : ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS30 = None
        vars_hint31 = None


        ARGS30_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:45:5: ( ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:45:9: ARGS vars_hint
                pass 
                ARGS30 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args320) 
                stream_ARGS.add(ARGS30)


                self._state.following.append(self.FOLLOW_vars_hint_in_proc_args322)
                vars_hint31 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint31.tree)


                # AST Rewrite
                # elements: vars_hint
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
                # 45:24: -> ^( TREE_PROC_ARGS vars_hint )
                # grammar/ShyRecognizerFrontend.g:45:27: ^( TREE_PROC_ARGS vars_hint )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC_ARGS, "TREE_PROC_ARGS")
                , root_1)

                self._adaptor.addChild(root_1, stream_vars_hint.nextTree())

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

    # $ANTLR end "proc_args"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:48:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS32 = None
        ID33 = None
        NEWLINE34 = None
        INDENT35 = None
        NEWLINE36 = None
        DEDENT38 = None
        NEWLINE39 = None
        consts_items37 = None


        CONSTS32_tree = None
        ID33_tree = None
        NEWLINE34_tree = None
        INDENT35_tree = None
        NEWLINE36_tree = None
        DEDENT38_tree = None
        NEWLINE39_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:49:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:49:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS32 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts351) 
                stream_CONSTS.add(CONSTS32)


                ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_consts353) 
                stream_ID.add(ID33)


                NEWLINE34 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts355) 
                stream_NEWLINE.add(NEWLINE34)


                INDENT35 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts365) 
                stream_INDENT.add(INDENT35)


                NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts367) 
                stream_NEWLINE.add(NEWLINE36)


                self._state.following.append(self.FOLLOW_consts_items_in_consts369)
                consts_items37 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items37.tree)


                DEDENT38 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts371) 
                stream_DEDENT.add(DEDENT38)


                NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts373) 
                stream_NEWLINE.add(NEWLINE39)


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
                # 51:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:51:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:53:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item40 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:53:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:53:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:53:16: ( consts_item )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == ID) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:53:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items405)
                        consts_item40 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item40.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:54:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID41 = None
        NEWLINE43 = None
        ID44 = None
        NEWLINE46 = None
        ID47 = None
        EXPRESSION48 = None
        NEWLINE49 = None
        num_whole42 = None

        num_fract45 = None


        ID41_tree = None
        NEWLINE43_tree = None
        ID44_tree = None
        NEWLINE46_tree = None
        ID47_tree = None
        EXPRESSION48_tree = None
        NEWLINE49_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:55:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt6 = 3
                LA6_0 = self.input.LA(1)

                if (LA6_0 == ID) :
                    LA6 = self.input.LA(2)
                    if LA6 == EXPRESSION:
                        alt6 = 3
                    elif LA6 == MINUS:
                        LA6_3 = self.input.LA(3)

                        if (LA6_3 == NUMBER) :
                            LA6_4 = self.input.LA(4)

                            if (LA6_4 == DIVIDE) :
                                alt6 = 2
                            elif (LA6_4 == NEWLINE) :
                                alt6 = 1
                            else:
                                nvae = NoViableAltException("", 6, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 6, 3, self.input)

                            raise nvae


                    elif LA6 == NUMBER:
                        LA6_4 = self.input.LA(3)

                        if (LA6_4 == DIVIDE) :
                            alt6 = 2
                        elif (LA6_4 == NEWLINE) :
                            alt6 = 1
                        else:
                            nvae = NoViableAltException("", 6, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammar/ShyRecognizerFrontend.g:55:9: ID num_whole NEWLINE
                    pass 
                    ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item421) 
                    stream_ID.add(ID41)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item423)
                    num_whole42 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole42.tree)


                    NEWLINE43 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item425) 
                    stream_NEWLINE.add(NEWLINE43)


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
                    # 55:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:55:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt6 == 2:
                    # grammar/ShyRecognizerFrontend.g:56:9: ID num_fract NEWLINE
                    pass 
                    ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item447) 
                    stream_ID.add(ID44)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item449)
                    num_fract45 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract45.tree)


                    NEWLINE46 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item451) 
                    stream_NEWLINE.add(NEWLINE46)


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
                    # 56:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:56:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt6 == 3:
                    # grammar/ShyRecognizerFrontend.g:57:9: ID EXPRESSION NEWLINE
                    pass 
                    ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item473) 
                    stream_ID.add(ID47)


                    EXPRESSION48 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item475) 
                    stream_EXPRESSION.add(EXPRESSION48)


                    NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item477) 
                    stream_NEWLINE.add(NEWLINE49)


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
                    # 57:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:57:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:60:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES50 = None
        ID51 = None
        NEWLINE52 = None
        INDENT53 = None
        NEWLINE54 = None
        DEDENT56 = None
        NEWLINE57 = None
        types_items55 = None


        TYPES50_tree = None
        ID51_tree = None
        NEWLINE52_tree = None
        INDENT53_tree = None
        NEWLINE54_tree = None
        DEDENT56_tree = None
        NEWLINE57_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:61:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:61:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES50 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types508) 
                stream_TYPES.add(TYPES50)


                ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_types510) 
                stream_ID.add(ID51)


                NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types512) 
                stream_NEWLINE.add(NEWLINE52)


                INDENT53 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types522) 
                stream_INDENT.add(INDENT53)


                NEWLINE54 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types524) 
                stream_NEWLINE.add(NEWLINE54)


                self._state.following.append(self.FOLLOW_types_items_in_types526)
                types_items55 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items55.tree)


                DEDENT56 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types528) 
                stream_DEDENT.add(DEDENT56)


                NEWLINE57 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types530) 
                stream_NEWLINE.add(NEWLINE57)


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
                # 63:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:63:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:65:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item58 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:65:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:65:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:65:15: ( types_item )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == ID) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerFrontend.g:65:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items562)
                        types_item58 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item58.tree)



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1




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
    # grammar/ShyRecognizerFrontend.g:66:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID59 = None
        vars_hint60 = None


        ID59_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:66:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:66:14: ID vars_hint
                pass 
                ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item572) 
                stream_ID.add(ID59)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item574)
                vars_hint60 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint60.tree)


                # AST Rewrite
                # elements: vars_hint, ID
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
                # 66:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:66:30: ^( TREE_TYPES_ITEM ID vars_hint )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES_ITEM, "TREE_TYPES_ITEM")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_vars_hint.nextTree())

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


    class vars_hint_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.vars_hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "vars_hint"
    # grammar/ShyRecognizerFrontend.g:68:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE62 = None
        INDENT63 = None
        NEWLINE64 = None
        NEWLINE66 = None
        DEDENT67 = None
        NEWLINE68 = None
        var_hint61 = None

        var_hint65 = None


        NEWLINE62_tree = None
        INDENT63_tree = None
        NEWLINE64_tree = None
        NEWLINE66_tree = None
        DEDENT67_tree = None
        NEWLINE68_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:69:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:69:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:69:9: ( var_hint )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == CURLY_OPEN or LA8_0 == ID) :
                    alt8 = 1
                if alt8 == 1:
                    # grammar/ShyRecognizerFrontend.g:69:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint601)
                    var_hint61 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint61.tree)





                NEWLINE62 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint605) 
                stream_NEWLINE.add(NEWLINE62)


                # grammar/ShyRecognizerFrontend.g:70:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == INDENT) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerFrontend.g:70:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT63 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint617) 
                    stream_INDENT.add(INDENT63)


                    NEWLINE64 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint619) 
                    stream_NEWLINE.add(NEWLINE64)


                    # grammar/ShyRecognizerFrontend.g:70:26: ( var_hint NEWLINE )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == CURLY_OPEN or LA9_0 == ID) :
                            alt9 = 1


                        if alt9 == 1:
                            # grammar/ShyRecognizerFrontend.g:70:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint623)
                            var_hint65 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint65.tree)


                            NEWLINE66 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint625) 
                            stream_NEWLINE.add(NEWLINE66)



                        else:
                            if cnt9 >= 1:
                                break #loop9

                            eee = EarlyExitException(9, self.input)
                            raise eee

                        cnt9 += 1


                    DEDENT67 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint631) 
                    stream_DEDENT.add(DEDENT67)


                    NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint633) 
                    stream_NEWLINE.add(NEWLINE68)





                # AST Rewrite
                # elements: var_hint
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
                # 71:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:71:27: ( var_hint )*
                while stream_var_hint.hasNext():
                    self._adaptor.addChild(root_0, stream_var_hint.nextTree())


                stream_var_hint.reset();




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

    # $ANTLR end "vars_hint"


    class var_hint_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.var_hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "var_hint"
    # grammar/ShyRecognizerFrontend.g:73:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE73 = None
        INDENT74 = None
        NEWLINE75 = None
        NEWLINE77 = None
        DEDENT78 = None
        var69 = None

        hint70 = None

        var71 = None

        hint72 = None

        var76 = None


        NEWLINE73_tree = None
        INDENT74_tree = None
        NEWLINE75_tree = None
        NEWLINE77_tree = None
        DEDENT78_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:74:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt15 = 3
                alt15 = self.dfa15.predict(self.input)
                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:74:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:74:9: ( var )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == ID) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/ShyRecognizerFrontend.g:74:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint672)
                            var69 = self.var()

                            self._state.following.pop()
                            stream_var.add(var69.tree)



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    # AST Rewrite
                    # elements: var
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
                    # 75:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:75:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:75:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:76:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint707)
                    hint70 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint70.tree)


                    # grammar/ShyRecognizerFrontend.g:76:14: ( var )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == ID) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyRecognizerFrontend.g:76:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint709)
                            var71 = self.var()

                            self._state.following.pop()
                            stream_var.add(var71.tree)



                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    # AST Rewrite
                    # elements: hint, var
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
                    # 77:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:77:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:77:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 3:
                    # grammar/ShyRecognizerFrontend.g:78:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint743)
                    hint72 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint72.tree)


                    NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint745) 
                    stream_NEWLINE.add(NEWLINE73)


                    INDENT74 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint747) 
                    stream_INDENT.add(INDENT74)


                    NEWLINE75 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint749) 
                    stream_NEWLINE.add(NEWLINE75)


                    # grammar/ShyRecognizerFrontend.g:78:37: ( ( var )+ NEWLINE )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == ID) :
                            alt14 = 1


                        if alt14 == 1:
                            # grammar/ShyRecognizerFrontend.g:78:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:78:39: ( var )+
                            cnt13 = 0
                            while True: #loop13
                                alt13 = 2
                                LA13_0 = self.input.LA(1)

                                if (LA13_0 == ID) :
                                    alt13 = 1


                                if alt13 == 1:
                                    # grammar/ShyRecognizerFrontend.g:78:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint753)
                                    var76 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var76.tree)



                                else:
                                    if cnt13 >= 1:
                                        break #loop13

                                    eee = EarlyExitException(13, self.input)
                                    raise eee

                                cnt13 += 1


                            NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint757) 
                            stream_NEWLINE.add(NEWLINE77)



                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                    DEDENT78 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint763) 
                    stream_DEDENT.add(DEDENT78)


                    # AST Rewrite
                    # elements: hint, var
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
                    # 79:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:79:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:79:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

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

    # $ANTLR end "var_hint"


    class var_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.var_return, self).__init__()

            self.tree = None





    # $ANTLR start "var"
    # grammar/ShyRecognizerFrontend.g:81:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID79 = None

        ID79_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:81:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:81:7: ID
                pass 
                ID79 = self.match(self.input, ID, self.FOLLOW_ID_in_var797) 
                stream_ID.add(ID79)


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
                # 81:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:81:13: ^( TREE_VAR ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_VAR, "TREE_VAR")
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

    # $ANTLR end "var"


    class hint_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "hint"
    # grammar/ShyRecognizerFrontend.g:83:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN80 = None
        ID81 = None
        CURLY_CLOSE82 = None
        CURLY_OPEN83 = None
        ID84 = None
        CURLY_CLOSE86 = None
        hint_arg85 = None


        CURLY_OPEN80_tree = None
        ID81_tree = None
        CURLY_CLOSE82_tree = None
        CURLY_OPEN83_tree = None
        ID84_tree = None
        CURLY_CLOSE86_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:84:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == CURLY_OPEN) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == ID) :
                        LA17_2 = self.input.LA(3)

                        if (LA17_2 == CURLY_CLOSE) :
                            alt17 = 1
                        elif (LA17_2 == ID or LA17_2 == UNDERSCORE) :
                            alt17 = 2
                        else:
                            nvae = NoViableAltException("", 17, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 17, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:84:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN80 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint822) 
                    stream_CURLY_OPEN.add(CURLY_OPEN80)


                    ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_hint824) 
                    stream_ID.add(ID81)


                    CURLY_CLOSE82 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint826) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE82)


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
                    # 84:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:84:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:85:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN83 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint846) 
                    stream_CURLY_OPEN.add(CURLY_OPEN83)


                    ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_hint848) 
                    stream_ID.add(ID84)


                    # grammar/ShyRecognizerFrontend.g:85:23: ( hint_arg )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == ID or LA16_0 == UNDERSCORE) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:85:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint850)
                            hint_arg85 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg85.tree)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    CURLY_CLOSE86 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint854) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE86)


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
                    # 85:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:85:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:85:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:87:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set87 = None

        set87_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:87:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set87 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set87))

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
    # grammar/ShyRecognizerFrontend.g:89:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS88 = None
        NUMBER89 = None

        MINUS88_tree = None
        NUMBER89_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:89:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:89:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:89:13: ( MINUS )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == MINUS) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:89:13: MINUS
                    pass 
                    MINUS88 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole893)
                    MINUS88_tree = self._adaptor.createWithPayload(MINUS88)
                    self._adaptor.addChild(root_0, MINUS88_tree)






                NUMBER89 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole897)
                NUMBER89_tree = self._adaptor.createWithPayload(NUMBER89)
                self._adaptor.addChild(root_0, NUMBER89_tree)





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
    # grammar/ShyRecognizerFrontend.g:90:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS90 = None
        NUMBER91 = None
        DIVIDE92 = None
        NUMBER93 = None

        MINUS90_tree = None
        NUMBER91_tree = None
        DIVIDE92_tree = None
        NUMBER93_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:90:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:90:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:90:13: ( MINUS )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MINUS) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:90:13: MINUS
                    pass 
                    MINUS90 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract905)
                    MINUS90_tree = self._adaptor.createWithPayload(MINUS90)
                    self._adaptor.addChild(root_0, MINUS90_tree)






                NUMBER91 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract909)
                NUMBER91_tree = self._adaptor.createWithPayload(NUMBER91)
                self._adaptor.addChild(root_0, NUMBER91_tree)



                DIVIDE92 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract911)
                DIVIDE92_tree = self._adaptor.createWithPayload(DIVIDE92)
                self._adaptor.addChild(root_0, DIVIDE92_tree)



                NUMBER93 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract913)
                NUMBER93_tree = self._adaptor.createWithPayload(NUMBER93)
                self._adaptor.addChild(root_0, NUMBER93_tree)





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



    # lookup tables for DFA #15

    DFA15_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA15_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA15_min = DFA.unpack(
        u"\1\12\1\uffff\1\16\1\11\1\16\1\11\2\uffff\1\16"
        )

    DFA15_max = DFA.unpack(
        u"\1\16\1\uffff\1\16\1\57\1\22\1\57\2\uffff\1\22"
        )

    DFA15_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA15_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA15_transition = [
        DFA.unpack(u"\1\2\3\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\4\uffff\1\5\40\uffff\1\5"),
        DFA.unpack(u"\1\6\3\uffff\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\5\40\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\7")
    ]

    # class definition for DFA #15

    class DFA15(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 7, 17, 23, 46])
    FOLLOW_stateless_in_start86 = frozenset([1, 7, 17, 23, 46])
    FOLLOW_consts_in_start90 = frozenset([1, 7, 17, 23, 46])
    FOLLOW_types_in_start94 = frozenset([1, 7, 17, 23, 46])
    FOLLOW_MODULE_in_module113 = frozenset([14])
    FOLLOW_ID_in_module115 = frozenset([18])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([14])
    FOLLOW_ID_in_stateless148 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1])
    FOLLOW_STATELESS_in_stateless178 = frozenset([14])
    FOLLOW_ID_in_stateless180 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless182 = frozenset([15])
    FOLLOW_INDENT_in_stateless184 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless186 = frozenset([21])
    FOLLOW_proc_in_stateless188 = frozenset([11, 21])
    FOLLOW_DEDENT_in_stateless192 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless194 = frozenset([1])
    FOLLOW_PROC_in_proc235 = frozenset([14])
    FOLLOW_ID_in_proc237 = frozenset([18])
    FOLLOW_NEWLINE_in_proc239 = frozenset([1])
    FOLLOW_PROC_in_proc267 = frozenset([14])
    FOLLOW_ID_in_proc269 = frozenset([18])
    FOLLOW_NEWLINE_in_proc271 = frozenset([15])
    FOLLOW_INDENT_in_proc273 = frozenset([18])
    FOLLOW_NEWLINE_in_proc275 = frozenset([4])
    FOLLOW_proc_args_in_proc277 = frozenset([11])
    FOLLOW_DEDENT_in_proc279 = frozenset([18])
    FOLLOW_NEWLINE_in_proc281 = frozenset([1])
    FOLLOW_ARGS_in_proc_args320 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_proc_args322 = frozenset([1])
    FOLLOW_CONSTS_in_consts351 = frozenset([14])
    FOLLOW_ID_in_consts353 = frozenset([18])
    FOLLOW_NEWLINE_in_consts355 = frozenset([15])
    FOLLOW_INDENT_in_consts365 = frozenset([18])
    FOLLOW_NEWLINE_in_consts367 = frozenset([14])
    FOLLOW_consts_items_in_consts369 = frozenset([11])
    FOLLOW_DEDENT_in_consts371 = frozenset([18])
    FOLLOW_NEWLINE_in_consts373 = frozenset([1])
    FOLLOW_consts_item_in_consts_items405 = frozenset([1, 14])
    FOLLOW_ID_in_consts_item421 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item423 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item425 = frozenset([1])
    FOLLOW_ID_in_consts_item447 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item449 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item451 = frozenset([1])
    FOLLOW_ID_in_consts_item473 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item475 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item477 = frozenset([1])
    FOLLOW_TYPES_in_types508 = frozenset([14])
    FOLLOW_ID_in_types510 = frozenset([18])
    FOLLOW_NEWLINE_in_types512 = frozenset([15])
    FOLLOW_INDENT_in_types522 = frozenset([18])
    FOLLOW_NEWLINE_in_types524 = frozenset([14])
    FOLLOW_types_items_in_types526 = frozenset([11])
    FOLLOW_DEDENT_in_types528 = frozenset([18])
    FOLLOW_NEWLINE_in_types530 = frozenset([1])
    FOLLOW_types_item_in_types_items562 = frozenset([1, 14])
    FOLLOW_ID_in_types_item572 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_types_item574 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint601 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint605 = frozenset([1, 15])
    FOLLOW_INDENT_in_vars_hint617 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint619 = frozenset([10, 14])
    FOLLOW_var_hint_in_vars_hint623 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint625 = frozenset([10, 11, 14])
    FOLLOW_DEDENT_in_vars_hint631 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint633 = frozenset([1])
    FOLLOW_var_in_var_hint672 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint707 = frozenset([14])
    FOLLOW_var_in_var_hint709 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint743 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint745 = frozenset([15])
    FOLLOW_INDENT_in_var_hint747 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint749 = frozenset([14])
    FOLLOW_var_in_var_hint753 = frozenset([14, 18])
    FOLLOW_NEWLINE_in_var_hint757 = frozenset([11, 14])
    FOLLOW_DEDENT_in_var_hint763 = frozenset([1])
    FOLLOW_ID_in_var797 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint822 = frozenset([14])
    FOLLOW_ID_in_hint824 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint826 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint846 = frozenset([14])
    FOLLOW_ID_in_hint848 = frozenset([14, 47])
    FOLLOW_hint_arg_in_hint850 = frozenset([9, 14, 47])
    FOLLOW_CURLY_CLOSE_in_hint854 = frozenset([1])
    FOLLOW_MINUS_in_num_whole893 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole897 = frozenset([1])
    FOLLOW_MINUS_in_num_fract905 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract909 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract911 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract913 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
