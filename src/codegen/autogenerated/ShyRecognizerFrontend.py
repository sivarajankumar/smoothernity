# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-23 18:48:28

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

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
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
                    # elements: proc_args, ID
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
    # grammar/ShyRecognizerFrontend.g:44:1: proc_args : ARGS ( ID )+ NEWLINE -> ^( TREE_PROC_ARGS ( ID )+ ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS30 = None
        ID31 = None
        NEWLINE32 = None

        ARGS30_tree = None
        ID31_tree = None
        NEWLINE32_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:45:5: ( ARGS ( ID )+ NEWLINE -> ^( TREE_PROC_ARGS ( ID )+ ) )
                # grammar/ShyRecognizerFrontend.g:45:9: ARGS ( ID )+ NEWLINE
                pass 
                ARGS30 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args320) 
                stream_ARGS.add(ARGS30)


                # grammar/ShyRecognizerFrontend.g:45:14: ( ID )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == ID) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:45:14: ID
                        pass 
                        ID31 = self.match(self.input, ID, self.FOLLOW_ID_in_proc_args322) 
                        stream_ID.add(ID31)



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1


                NEWLINE32 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_args326) 
                stream_NEWLINE.add(NEWLINE32)


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
                # 45:27: -> ^( TREE_PROC_ARGS ( ID )+ )
                # grammar/ShyRecognizerFrontend.g:45:30: ^( TREE_PROC_ARGS ( ID )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC_ARGS, "TREE_PROC_ARGS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:45:48: ( ID )+
                if not (stream_ID.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_ID.hasNext():
                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )


                stream_ID.reset()

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

        CONSTS33 = None
        ID34 = None
        NEWLINE35 = None
        INDENT36 = None
        NEWLINE37 = None
        DEDENT39 = None
        NEWLINE40 = None
        consts_items38 = None


        CONSTS33_tree = None
        ID34_tree = None
        NEWLINE35_tree = None
        INDENT36_tree = None
        NEWLINE37_tree = None
        DEDENT39_tree = None
        NEWLINE40_tree = None
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
                CONSTS33 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts357) 
                stream_CONSTS.add(CONSTS33)


                ID34 = self.match(self.input, ID, self.FOLLOW_ID_in_consts359) 
                stream_ID.add(ID34)


                NEWLINE35 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts361) 
                stream_NEWLINE.add(NEWLINE35)


                INDENT36 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts371) 
                stream_INDENT.add(INDENT36)


                NEWLINE37 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts373) 
                stream_NEWLINE.add(NEWLINE37)


                self._state.following.append(self.FOLLOW_consts_items_in_consts375)
                consts_items38 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items38.tree)


                DEDENT39 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts377) 
                stream_DEDENT.add(DEDENT39)


                NEWLINE40 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts379) 
                stream_NEWLINE.add(NEWLINE40)


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

        consts_item41 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:53:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:53:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:53:16: ( consts_item )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == ID) :
                        alt6 = 1


                    if alt6 == 1:
                        # grammar/ShyRecognizerFrontend.g:53:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items411)
                        consts_item41 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item41.tree)



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

        ID42 = None
        NEWLINE44 = None
        ID45 = None
        NEWLINE47 = None
        ID48 = None
        EXPRESSION49 = None
        NEWLINE50 = None
        num_whole43 = None

        num_fract46 = None


        ID42_tree = None
        NEWLINE44_tree = None
        ID45_tree = None
        NEWLINE47_tree = None
        ID48_tree = None
        EXPRESSION49_tree = None
        NEWLINE50_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:55:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt7 = 3
                LA7_0 = self.input.LA(1)

                if (LA7_0 == ID) :
                    LA7 = self.input.LA(2)
                    if LA7 == EXPRESSION:
                        alt7 = 3
                    elif LA7 == MINUS:
                        LA7_3 = self.input.LA(3)

                        if (LA7_3 == NUMBER) :
                            LA7_4 = self.input.LA(4)

                            if (LA7_4 == DIVIDE) :
                                alt7 = 2
                            elif (LA7_4 == NEWLINE) :
                                alt7 = 1
                            else:
                                nvae = NoViableAltException("", 7, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 7, 3, self.input)

                            raise nvae


                    elif LA7 == NUMBER:
                        LA7_4 = self.input.LA(3)

                        if (LA7_4 == DIVIDE) :
                            alt7 = 2
                        elif (LA7_4 == NEWLINE) :
                            alt7 = 1
                        else:
                            nvae = NoViableAltException("", 7, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
                    # grammar/ShyRecognizerFrontend.g:55:9: ID num_whole NEWLINE
                    pass 
                    ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item427) 
                    stream_ID.add(ID42)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item429)
                    num_whole43 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole43.tree)


                    NEWLINE44 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item431) 
                    stream_NEWLINE.add(NEWLINE44)


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




                elif alt7 == 2:
                    # grammar/ShyRecognizerFrontend.g:56:9: ID num_fract NEWLINE
                    pass 
                    ID45 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item453) 
                    stream_ID.add(ID45)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item455)
                    num_fract46 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract46.tree)


                    NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item457) 
                    stream_NEWLINE.add(NEWLINE47)


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




                elif alt7 == 3:
                    # grammar/ShyRecognizerFrontend.g:57:9: ID EXPRESSION NEWLINE
                    pass 
                    ID48 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item479) 
                    stream_ID.add(ID48)


                    EXPRESSION49 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item481) 
                    stream_EXPRESSION.add(EXPRESSION49)


                    NEWLINE50 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item483) 
                    stream_NEWLINE.add(NEWLINE50)


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

        TYPES51 = None
        ID52 = None
        NEWLINE53 = None
        INDENT54 = None
        NEWLINE55 = None
        DEDENT57 = None
        NEWLINE58 = None
        types_items56 = None


        TYPES51_tree = None
        ID52_tree = None
        NEWLINE53_tree = None
        INDENT54_tree = None
        NEWLINE55_tree = None
        DEDENT57_tree = None
        NEWLINE58_tree = None
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
                TYPES51 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types514) 
                stream_TYPES.add(TYPES51)


                ID52 = self.match(self.input, ID, self.FOLLOW_ID_in_types516) 
                stream_ID.add(ID52)


                NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types518) 
                stream_NEWLINE.add(NEWLINE53)


                INDENT54 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types528) 
                stream_INDENT.add(INDENT54)


                NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types530) 
                stream_NEWLINE.add(NEWLINE55)


                self._state.following.append(self.FOLLOW_types_items_in_types532)
                types_items56 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items56.tree)


                DEDENT57 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types534) 
                stream_DEDENT.add(DEDENT57)


                NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types536) 
                stream_NEWLINE.add(NEWLINE58)


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

        types_item59 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:65:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:65:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:65:15: ( types_item )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == ID) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerFrontend.g:65:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items568)
                        types_item59 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item59.tree)



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1




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

        ID60 = None
        vars_hint61 = None


        ID60_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:66:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:66:14: ID vars_hint
                pass 
                ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item578) 
                stream_ID.add(ID60)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item580)
                vars_hint61 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint61.tree)


                # AST Rewrite
                # elements: ID, vars_hint
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

        NEWLINE63 = None
        INDENT64 = None
        NEWLINE65 = None
        NEWLINE67 = None
        DEDENT68 = None
        NEWLINE69 = None
        var_hint62 = None

        var_hint66 = None


        NEWLINE63_tree = None
        INDENT64_tree = None
        NEWLINE65_tree = None
        NEWLINE67_tree = None
        DEDENT68_tree = None
        NEWLINE69_tree = None
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
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == CURLY_OPEN or LA9_0 == ID) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:69:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint607)
                    var_hint62 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint62.tree)





                NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint611) 
                stream_NEWLINE.add(NEWLINE63)


                # grammar/ShyRecognizerFrontend.g:70:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == INDENT) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerFrontend.g:70:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT64 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint623) 
                    stream_INDENT.add(INDENT64)


                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint625) 
                    stream_NEWLINE.add(NEWLINE65)


                    # grammar/ShyRecognizerFrontend.g:70:26: ( var_hint NEWLINE )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == CURLY_OPEN or LA10_0 == ID) :
                            alt10 = 1


                        if alt10 == 1:
                            # grammar/ShyRecognizerFrontend.g:70:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint629)
                            var_hint66 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint66.tree)


                            NEWLINE67 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint631) 
                            stream_NEWLINE.add(NEWLINE67)



                        else:
                            if cnt10 >= 1:
                                break #loop10

                            eee = EarlyExitException(10, self.input)
                            raise eee

                        cnt10 += 1


                    DEDENT68 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint637) 
                    stream_DEDENT.add(DEDENT68)


                    NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint639) 
                    stream_NEWLINE.add(NEWLINE69)





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

        NEWLINE74 = None
        INDENT75 = None
        NEWLINE76 = None
        NEWLINE78 = None
        DEDENT79 = None
        var70 = None

        hint71 = None

        var72 = None

        hint73 = None

        var77 = None


        NEWLINE74_tree = None
        INDENT75_tree = None
        NEWLINE76_tree = None
        NEWLINE78_tree = None
        DEDENT79_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:74:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt16 = 3
                alt16 = self.dfa16.predict(self.input)
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:74:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:74:9: ( var )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == ID) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyRecognizerFrontend.g:74:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint678)
                            var70 = self.var()

                            self._state.following.pop()
                            stream_var.add(var70.tree)



                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


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




                elif alt16 == 2:
                    # grammar/ShyRecognizerFrontend.g:76:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint713)
                    hint71 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint71.tree)


                    # grammar/ShyRecognizerFrontend.g:76:14: ( var )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == ID) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyRecognizerFrontend.g:76:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint715)
                            var72 = self.var()

                            self._state.following.pop()
                            stream_var.add(var72.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


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




                elif alt16 == 3:
                    # grammar/ShyRecognizerFrontend.g:78:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint749)
                    hint73 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint73.tree)


                    NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint751) 
                    stream_NEWLINE.add(NEWLINE74)


                    INDENT75 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint753) 
                    stream_INDENT.add(INDENT75)


                    NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint755) 
                    stream_NEWLINE.add(NEWLINE76)


                    # grammar/ShyRecognizerFrontend.g:78:37: ( ( var )+ NEWLINE )+
                    cnt15 = 0
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == ID) :
                            alt15 = 1


                        if alt15 == 1:
                            # grammar/ShyRecognizerFrontend.g:78:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:78:39: ( var )+
                            cnt14 = 0
                            while True: #loop14
                                alt14 = 2
                                LA14_0 = self.input.LA(1)

                                if (LA14_0 == ID) :
                                    alt14 = 1


                                if alt14 == 1:
                                    # grammar/ShyRecognizerFrontend.g:78:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint759)
                                    var77 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var77.tree)



                                else:
                                    if cnt14 >= 1:
                                        break #loop14

                                    eee = EarlyExitException(14, self.input)
                                    raise eee

                                cnt14 += 1


                            NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint763) 
                            stream_NEWLINE.add(NEWLINE78)



                        else:
                            if cnt15 >= 1:
                                break #loop15

                            eee = EarlyExitException(15, self.input)
                            raise eee

                        cnt15 += 1


                    DEDENT79 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint769) 
                    stream_DEDENT.add(DEDENT79)


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

        ID80 = None

        ID80_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:81:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:81:7: ID
                pass 
                ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_var803) 
                stream_ID.add(ID80)


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

        CURLY_OPEN81 = None
        ID82 = None
        CURLY_CLOSE83 = None
        CURLY_OPEN84 = None
        ID85 = None
        CURLY_CLOSE87 = None
        hint_arg86 = None


        CURLY_OPEN81_tree = None
        ID82_tree = None
        CURLY_CLOSE83_tree = None
        CURLY_OPEN84_tree = None
        ID85_tree = None
        CURLY_CLOSE87_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:84:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == CURLY_OPEN) :
                    LA18_1 = self.input.LA(2)

                    if (LA18_1 == ID) :
                        LA18_2 = self.input.LA(3)

                        if (LA18_2 == CURLY_CLOSE) :
                            alt18 = 1
                        elif (LA18_2 == ID or LA18_2 == UNDERSCORE) :
                            alt18 = 2
                        else:
                            nvae = NoViableAltException("", 18, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 18, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:84:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN81 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint828) 
                    stream_CURLY_OPEN.add(CURLY_OPEN81)


                    ID82 = self.match(self.input, ID, self.FOLLOW_ID_in_hint830) 
                    stream_ID.add(ID82)


                    CURLY_CLOSE83 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint832) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE83)


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




                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:85:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN84 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint852) 
                    stream_CURLY_OPEN.add(CURLY_OPEN84)


                    ID85 = self.match(self.input, ID, self.FOLLOW_ID_in_hint854) 
                    stream_ID.add(ID85)


                    # grammar/ShyRecognizerFrontend.g:85:23: ( hint_arg )+
                    cnt17 = 0
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == ID or LA17_0 == UNDERSCORE) :
                            alt17 = 1


                        if alt17 == 1:
                            # grammar/ShyRecognizerFrontend.g:85:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint856)
                            hint_arg86 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg86.tree)



                        else:
                            if cnt17 >= 1:
                                break #loop17

                            eee = EarlyExitException(17, self.input)
                            raise eee

                        cnt17 += 1


                    CURLY_CLOSE87 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint860) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE87)


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

        set88 = None

        set88_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:87:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set88 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set88))

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

        MINUS89 = None
        NUMBER90 = None

        MINUS89_tree = None
        NUMBER90_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:89:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:89:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:89:13: ( MINUS )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == MINUS) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:89:13: MINUS
                    pass 
                    MINUS89 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole899)
                    MINUS89_tree = self._adaptor.createWithPayload(MINUS89)
                    self._adaptor.addChild(root_0, MINUS89_tree)






                NUMBER90 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole903)
                NUMBER90_tree = self._adaptor.createWithPayload(NUMBER90)
                self._adaptor.addChild(root_0, NUMBER90_tree)





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

        MINUS91 = None
        NUMBER92 = None
        DIVIDE93 = None
        NUMBER94 = None

        MINUS91_tree = None
        NUMBER92_tree = None
        DIVIDE93_tree = None
        NUMBER94_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:90:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:90:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:90:13: ( MINUS )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == MINUS) :
                    alt20 = 1
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:90:13: MINUS
                    pass 
                    MINUS91 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract911)
                    MINUS91_tree = self._adaptor.createWithPayload(MINUS91)
                    self._adaptor.addChild(root_0, MINUS91_tree)






                NUMBER92 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract915)
                NUMBER92_tree = self._adaptor.createWithPayload(NUMBER92)
                self._adaptor.addChild(root_0, NUMBER92_tree)



                DIVIDE93 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract917)
                DIVIDE93_tree = self._adaptor.createWithPayload(DIVIDE93)
                self._adaptor.addChild(root_0, DIVIDE93_tree)



                NUMBER94 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract919)
                NUMBER94_tree = self._adaptor.createWithPayload(NUMBER94)
                self._adaptor.addChild(root_0, NUMBER94_tree)





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



    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\1\12\1\uffff\1\16\1\11\1\16\1\11\2\uffff\1\16"
        )

    DFA16_max = DFA.unpack(
        u"\1\16\1\uffff\1\16\1\57\1\22\1\57\2\uffff\1\22"
        )

    DFA16_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA16_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA16_transition = [
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

    # class definition for DFA #16

    class DFA16(DFA):
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
    FOLLOW_ARGS_in_proc_args320 = frozenset([14])
    FOLLOW_ID_in_proc_args322 = frozenset([14, 18])
    FOLLOW_NEWLINE_in_proc_args326 = frozenset([1])
    FOLLOW_CONSTS_in_consts357 = frozenset([14])
    FOLLOW_ID_in_consts359 = frozenset([18])
    FOLLOW_NEWLINE_in_consts361 = frozenset([15])
    FOLLOW_INDENT_in_consts371 = frozenset([18])
    FOLLOW_NEWLINE_in_consts373 = frozenset([14])
    FOLLOW_consts_items_in_consts375 = frozenset([11])
    FOLLOW_DEDENT_in_consts377 = frozenset([18])
    FOLLOW_NEWLINE_in_consts379 = frozenset([1])
    FOLLOW_consts_item_in_consts_items411 = frozenset([1, 14])
    FOLLOW_ID_in_consts_item427 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item429 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item431 = frozenset([1])
    FOLLOW_ID_in_consts_item453 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item455 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item457 = frozenset([1])
    FOLLOW_ID_in_consts_item479 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item481 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item483 = frozenset([1])
    FOLLOW_TYPES_in_types514 = frozenset([14])
    FOLLOW_ID_in_types516 = frozenset([18])
    FOLLOW_NEWLINE_in_types518 = frozenset([15])
    FOLLOW_INDENT_in_types528 = frozenset([18])
    FOLLOW_NEWLINE_in_types530 = frozenset([14])
    FOLLOW_types_items_in_types532 = frozenset([11])
    FOLLOW_DEDENT_in_types534 = frozenset([18])
    FOLLOW_NEWLINE_in_types536 = frozenset([1])
    FOLLOW_types_item_in_types_items568 = frozenset([1, 14])
    FOLLOW_ID_in_types_item578 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_types_item580 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint607 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint611 = frozenset([1, 15])
    FOLLOW_INDENT_in_vars_hint623 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint625 = frozenset([10, 14])
    FOLLOW_var_hint_in_vars_hint629 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint631 = frozenset([10, 11, 14])
    FOLLOW_DEDENT_in_vars_hint637 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint639 = frozenset([1])
    FOLLOW_var_in_var_hint678 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint713 = frozenset([14])
    FOLLOW_var_in_var_hint715 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint749 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint751 = frozenset([15])
    FOLLOW_INDENT_in_var_hint753 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint755 = frozenset([14])
    FOLLOW_var_in_var_hint759 = frozenset([14, 18])
    FOLLOW_NEWLINE_in_var_hint763 = frozenset([11, 14])
    FOLLOW_DEDENT_in_var_hint769 = frozenset([1])
    FOLLOW_ID_in_var803 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint828 = frozenset([14])
    FOLLOW_ID_in_hint830 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint832 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint852 = frozenset([14])
    FOLLOW_ID_in_hint854 = frozenset([14, 47])
    FOLLOW_hint_arg_in_hint856 = frozenset([9, 14, 47])
    FOLLOW_CURLY_CLOSE_in_hint860 = frozenset([1])
    FOLLOW_MINUS_in_num_whole899 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole903 = frozenset([1])
    FOLLOW_MINUS_in_num_fract911 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract915 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract917 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract919 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
