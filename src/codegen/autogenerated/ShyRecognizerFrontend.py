# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-23 20:00:12

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
OPS=20
PASTE=21
PROC=22
REPLACE=23
STATELESS=24
STRING=25
TREE_ARBITRARY_TOKEN=26
TREE_CONSTS=27
TREE_COPY=28
TREE_COPY_PASTE=29
TREE_EXPRESSION=30
TREE_HINT=31
TREE_HINT_NONE=32
TREE_MODULE=33
TREE_NUM_FRACT=34
TREE_NUM_WHOLE=35
TREE_PASTE=36
TREE_PASTE_REPLACE=37
TREE_PASTE_WITH=38
TREE_PROC=39
TREE_PROC_ARGS=40
TREE_PROC_OPS=41
TREE_PROC_VARS=42
TREE_STATELESS=43
TREE_STATEMENT_CALL=44
TREE_STATEMENT_CALL_ARGS=45
TREE_TYPES=46
TREE_TYPES_ITEM=47
TREE_VAR=48
TREE_VARS_HINT=49
TREE_VAR_HINT=50
TYPES=51
UNDERSCORE=52
VARS=53
WHITESPACE=54
WITH=55

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_OPS", "TREE_PROC_VARS", "TREE_STATELESS", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", "TREE_TYPES", "TREE_TYPES_ITEM", 
    "TREE_VAR", "TREE_VARS_HINT", "TREE_VAR_HINT", "TYPES", "UNDERSCORE", 
    "VARS", "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

        self.dfa22 = self.DFA22(
            self, 22,
            eot = self.DFA22_eot,
            eof = self.DFA22_eof,
            min = self.DFA22_min,
            max = self.DFA22_max,
            accept = self.DFA22_accept,
            special = self.DFA22_special,
            transition = self.DFA22_transition
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
    # grammar/ShyRecognizerFrontend.g:37:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? ) );
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
        DEDENT30 = None
        NEWLINE31 = None
        proc_args27 = None

        proc_vars28 = None

        proc_ops29 = None


        PROC19_tree = None
        ID20_tree = None
        NEWLINE21_tree = None
        PROC22_tree = None
        ID23_tree = None
        NEWLINE24_tree = None
        INDENT25_tree = None
        NEWLINE26_tree = None
        DEDENT30_tree = None
        NEWLINE31_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_proc_ops = RewriteRuleSubtreeStream(self._adaptor, "rule proc_ops")
        stream_proc_vars = RewriteRuleSubtreeStream(self._adaptor, "rule proc_vars")
        stream_proc_args = RewriteRuleSubtreeStream(self._adaptor, "rule proc_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:38:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? ) )
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == PROC) :
                    LA7_1 = self.input.LA(2)

                    if (LA7_1 == ID) :
                        LA7_2 = self.input.LA(3)

                        if (LA7_2 == NEWLINE) :
                            LA7_3 = self.input.LA(4)

                            if (LA7_3 == INDENT) :
                                alt7 = 2
                            elif (LA7_3 == DEDENT or LA7_3 == PROC) :
                                alt7 = 1
                            else:
                                nvae = NoViableAltException("", 7, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 7, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 7, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 7, 0, self.input)

                    raise nvae


                if alt7 == 1:
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




                elif alt7 == 2:
                    # grammar/ShyRecognizerFrontend.g:40:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? ( proc_ops )? DEDENT NEWLINE
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


                    # grammar/ShyRecognizerFrontend.g:41:13: ( proc_args )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ARGS) :
                        alt4 = 1
                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:41:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc289)
                        proc_args27 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args27.tree)





                    # grammar/ShyRecognizerFrontend.g:41:25: ( proc_vars )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == VARS) :
                        alt5 = 1
                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:41:25: proc_vars
                        pass 
                        self._state.following.append(self.FOLLOW_proc_vars_in_proc293)
                        proc_vars28 = self.proc_vars()

                        self._state.following.pop()
                        stream_proc_vars.add(proc_vars28.tree)





                    # grammar/ShyRecognizerFrontend.g:41:37: ( proc_ops )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == OPS) :
                        alt6 = 1
                    if alt6 == 1:
                        # grammar/ShyRecognizerFrontend.g:41:37: proc_ops
                        pass 
                        self._state.following.append(self.FOLLOW_proc_ops_in_proc297)
                        proc_ops29 = self.proc_ops()

                        self._state.following.pop()
                        stream_proc_ops.add(proc_ops29.tree)





                    DEDENT30 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc309) 
                    stream_DEDENT.add(DEDENT30)


                    NEWLINE31 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc311) 
                    stream_NEWLINE.add(NEWLINE31)


                    # AST Rewrite
                    # elements: proc_args, ID, proc_ops, proc_vars
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
                    # 43:9: -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? )
                    # grammar/ShyRecognizerFrontend.g:43:12: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:43:28: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:43:40: ( proc_vars )?
                    if stream_proc_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_vars.nextTree())


                    stream_proc_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:43:52: ( proc_ops )?
                    if stream_proc_ops.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_ops.nextTree())


                    stream_proc_ops.reset();

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
    # grammar/ShyRecognizerFrontend.g:46:1: proc_args : ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS32 = None
        vars_hint33 = None


        ARGS32_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:47:5: ( ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:47:9: ARGS vars_hint
                pass 
                ARGS32 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args360) 
                stream_ARGS.add(ARGS32)


                self._state.following.append(self.FOLLOW_vars_hint_in_proc_args362)
                vars_hint33 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint33.tree)


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
                # 47:24: -> ^( TREE_PROC_ARGS vars_hint )
                # grammar/ShyRecognizerFrontend.g:47:27: ^( TREE_PROC_ARGS vars_hint )
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


    class proc_vars_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_vars_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc_vars"
    # grammar/ShyRecognizerFrontend.g:50:1: proc_vars : VARS vars_hint -> ^( TREE_PROC_VARS vars_hint ) ;
    def proc_vars(self, ):
        retval = self.proc_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS34 = None
        vars_hint35 = None


        VARS34_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:51:5: ( VARS vars_hint -> ^( TREE_PROC_VARS vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:51:9: VARS vars_hint
                pass 
                VARS34 = self.match(self.input, VARS, self.FOLLOW_VARS_in_proc_vars391) 
                stream_VARS.add(VARS34)


                self._state.following.append(self.FOLLOW_vars_hint_in_proc_vars393)
                vars_hint35 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint35.tree)


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
                # 51:24: -> ^( TREE_PROC_VARS vars_hint )
                # grammar/ShyRecognizerFrontend.g:51:27: ^( TREE_PROC_VARS vars_hint )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC_VARS, "TREE_PROC_VARS")
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

    # $ANTLR end "proc_vars"


    class proc_ops_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_ops_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc_ops"
    # grammar/ShyRecognizerFrontend.g:54:1: proc_ops : OPS NEWLINE INDENT NEWLINE statement DEDENT NEWLINE -> ^( TREE_PROC_OPS statement ) ;
    def proc_ops(self, ):
        retval = self.proc_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS36 = None
        NEWLINE37 = None
        INDENT38 = None
        NEWLINE39 = None
        DEDENT41 = None
        NEWLINE42 = None
        statement40 = None


        OPS36_tree = None
        NEWLINE37_tree = None
        INDENT38_tree = None
        NEWLINE39_tree = None
        DEDENT41_tree = None
        NEWLINE42_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:55:5: ( OPS NEWLINE INDENT NEWLINE statement DEDENT NEWLINE -> ^( TREE_PROC_OPS statement ) )
                # grammar/ShyRecognizerFrontend.g:55:9: OPS NEWLINE INDENT NEWLINE statement DEDENT NEWLINE
                pass 
                OPS36 = self.match(self.input, OPS, self.FOLLOW_OPS_in_proc_ops422) 
                stream_OPS.add(OPS36)


                NEWLINE37 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops424) 
                stream_NEWLINE.add(NEWLINE37)


                INDENT38 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc_ops426) 
                stream_INDENT.add(INDENT38)


                NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops428) 
                stream_NEWLINE.add(NEWLINE39)


                self._state.following.append(self.FOLLOW_statement_in_proc_ops430)
                statement40 = self.statement()

                self._state.following.pop()
                stream_statement.add(statement40.tree)


                DEDENT41 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc_ops432) 
                stream_DEDENT.add(DEDENT41)


                NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops434) 
                stream_NEWLINE.add(NEWLINE42)


                # AST Rewrite
                # elements: statement
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
                # 56:9: -> ^( TREE_PROC_OPS statement )
                # grammar/ShyRecognizerFrontend.g:56:12: ^( TREE_PROC_OPS statement )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC_OPS, "TREE_PROC_OPS")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement.nextTree())

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

    # $ANTLR end "proc_ops"


    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement"
    # grammar/ShyRecognizerFrontend.g:59:1: statement : statement_call ;
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call43 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:60:5: ( statement_call )
                # grammar/ShyRecognizerFrontend.g:60:9: statement_call
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_statement_call_in_statement471)
                statement_call43 = self.statement_call()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement_call43.tree)




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

    # $ANTLR end "statement"


    class statement_call_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerFrontend.g:63:1: statement_call : ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID44 = None
        NEWLINE46 = None
        INDENT47 = None
        NEWLINE48 = None
        NEWLINE50 = None
        DEDENT51 = None
        NEWLINE52 = None
        statement_call_args45 = None

        statement_call_args49 = None


        ID44_tree = None
        NEWLINE46_tree = None
        INDENT47_tree = None
        NEWLINE48_tree = None
        NEWLINE50_tree = None
        DEDENT51_tree = None
        NEWLINE52_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:64:5: ( ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:64:9: ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call490) 
                stream_ID.add(ID44)


                # grammar/ShyRecognizerFrontend.g:64:12: ( statement_call_args )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ID) :
                    alt8 = 1
                if alt8 == 1:
                    # grammar/ShyRecognizerFrontend.g:64:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call492)
                    statement_call_args45 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args45.tree)





                NEWLINE46 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call496) 
                stream_NEWLINE.add(NEWLINE46)


                # grammar/ShyRecognizerFrontend.g:65:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == INDENT) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerFrontend.g:65:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT47 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call509) 
                    stream_INDENT.add(INDENT47)


                    NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call511) 
                    stream_NEWLINE.add(NEWLINE48)


                    # grammar/ShyRecognizerFrontend.g:65:26: ( statement_call_args NEWLINE )+
                    cnt9 = 0
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == ID) :
                            alt9 = 1


                        if alt9 == 1:
                            # grammar/ShyRecognizerFrontend.g:65:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call515)
                            statement_call_args49 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args49.tree)


                            NEWLINE50 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call517) 
                            stream_NEWLINE.add(NEWLINE50)



                        else:
                            if cnt9 >= 1:
                                break #loop9

                            eee = EarlyExitException(9, self.input)
                            raise eee

                        cnt9 += 1


                    DEDENT51 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call523) 
                    stream_DEDENT.add(DEDENT51)


                    NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call525) 
                    stream_NEWLINE.add(NEWLINE52)





                # AST Rewrite
                # elements: ID, statement_call_args
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
                # 66:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:66:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, 
                self._adaptor.createFromType(TREE_STATEMENT_CALL_ARGS, "TREE_STATEMENT_CALL_ARGS")
                )

                # grammar/ShyRecognizerFrontend.g:67:42: ( statement_call_args )*
                while stream_statement_call_args.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_call_args.nextTree())


                stream_statement_call_args.reset();

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

    # $ANTLR end "statement_call"


    class statement_call_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_args_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerFrontend.g:70:1: statement_call_args : ( ID )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID53 = None

        ID53_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:70:21: ( ( ID )+ )
                # grammar/ShyRecognizerFrontend.g:70:23: ( ID )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:70:23: ( ID )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ID) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:70:23: ID
                        pass 
                        ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_args583)
                        ID53_tree = self._adaptor.createWithPayload(ID53)
                        self._adaptor.addChild(root_0, ID53_tree)




                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1




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

    # $ANTLR end "statement_call_args"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:72:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS54 = None
        ID55 = None
        NEWLINE56 = None
        INDENT57 = None
        NEWLINE58 = None
        DEDENT60 = None
        NEWLINE61 = None
        consts_items59 = None


        CONSTS54_tree = None
        ID55_tree = None
        NEWLINE56_tree = None
        INDENT57_tree = None
        NEWLINE58_tree = None
        DEDENT60_tree = None
        NEWLINE61_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:73:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:73:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS54 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts600) 
                stream_CONSTS.add(CONSTS54)


                ID55 = self.match(self.input, ID, self.FOLLOW_ID_in_consts602) 
                stream_ID.add(ID55)


                NEWLINE56 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts604) 
                stream_NEWLINE.add(NEWLINE56)


                INDENT57 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts614) 
                stream_INDENT.add(INDENT57)


                NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts616) 
                stream_NEWLINE.add(NEWLINE58)


                self._state.following.append(self.FOLLOW_consts_items_in_consts618)
                consts_items59 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items59.tree)


                DEDENT60 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts620) 
                stream_DEDENT.add(DEDENT60)


                NEWLINE61 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts622) 
                stream_NEWLINE.add(NEWLINE61)


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
                # 75:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:75:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:77:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item62 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:77:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:77:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:77:16: ( consts_item )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == ID) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:77:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items654)
                        consts_item62 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item62.tree)



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1




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
    # grammar/ShyRecognizerFrontend.g:78:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID63 = None
        NEWLINE65 = None
        ID66 = None
        NEWLINE68 = None
        ID69 = None
        EXPRESSION70 = None
        NEWLINE71 = None
        num_whole64 = None

        num_fract67 = None


        ID63_tree = None
        NEWLINE65_tree = None
        ID66_tree = None
        NEWLINE68_tree = None
        ID69_tree = None
        EXPRESSION70_tree = None
        NEWLINE71_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:79:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt13 = 3
                LA13_0 = self.input.LA(1)

                if (LA13_0 == ID) :
                    LA13 = self.input.LA(2)
                    if LA13 == EXPRESSION:
                        alt13 = 3
                    elif LA13 == MINUS:
                        LA13_3 = self.input.LA(3)

                        if (LA13_3 == NUMBER) :
                            LA13_4 = self.input.LA(4)

                            if (LA13_4 == DIVIDE) :
                                alt13 = 2
                            elif (LA13_4 == NEWLINE) :
                                alt13 = 1
                            else:
                                nvae = NoViableAltException("", 13, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 13, 3, self.input)

                            raise nvae


                    elif LA13 == NUMBER:
                        LA13_4 = self.input.LA(3)

                        if (LA13_4 == DIVIDE) :
                            alt13 = 2
                        elif (LA13_4 == NEWLINE) :
                            alt13 = 1
                        else:
                            nvae = NoViableAltException("", 13, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 13, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # grammar/ShyRecognizerFrontend.g:79:9: ID num_whole NEWLINE
                    pass 
                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item670) 
                    stream_ID.add(ID63)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item672)
                    num_whole64 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole64.tree)


                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item674) 
                    stream_NEWLINE.add(NEWLINE65)


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
                    # 79:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:79:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt13 == 2:
                    # grammar/ShyRecognizerFrontend.g:80:9: ID num_fract NEWLINE
                    pass 
                    ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item696) 
                    stream_ID.add(ID66)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item698)
                    num_fract67 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract67.tree)


                    NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item700) 
                    stream_NEWLINE.add(NEWLINE68)


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
                    # 80:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:80:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt13 == 3:
                    # grammar/ShyRecognizerFrontend.g:81:9: ID EXPRESSION NEWLINE
                    pass 
                    ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item722) 
                    stream_ID.add(ID69)


                    EXPRESSION70 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item724) 
                    stream_EXPRESSION.add(EXPRESSION70)


                    NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item726) 
                    stream_NEWLINE.add(NEWLINE71)


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
                    # 81:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:81:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:84:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES72 = None
        ID73 = None
        NEWLINE74 = None
        INDENT75 = None
        NEWLINE76 = None
        DEDENT78 = None
        NEWLINE79 = None
        types_items77 = None


        TYPES72_tree = None
        ID73_tree = None
        NEWLINE74_tree = None
        INDENT75_tree = None
        NEWLINE76_tree = None
        DEDENT78_tree = None
        NEWLINE79_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:85:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:85:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES72 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types757) 
                stream_TYPES.add(TYPES72)


                ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_types759) 
                stream_ID.add(ID73)


                NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types761) 
                stream_NEWLINE.add(NEWLINE74)


                INDENT75 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types771) 
                stream_INDENT.add(INDENT75)


                NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types773) 
                stream_NEWLINE.add(NEWLINE76)


                self._state.following.append(self.FOLLOW_types_items_in_types775)
                types_items77 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items77.tree)


                DEDENT78 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types777) 
                stream_DEDENT.add(DEDENT78)


                NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types779) 
                stream_NEWLINE.add(NEWLINE79)


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
                # 87:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:87:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:89:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item80 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:89:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:89:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:89:15: ( types_item )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == ID) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:89:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items811)
                        types_item80 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item80.tree)



                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1




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
    # grammar/ShyRecognizerFrontend.g:90:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID81 = None
        vars_hint82 = None


        ID81_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:90:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:90:14: ID vars_hint
                pass 
                ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item821) 
                stream_ID.add(ID81)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item823)
                vars_hint82 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint82.tree)


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
                # 90:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:90:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:92:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE84 = None
        INDENT85 = None
        NEWLINE86 = None
        NEWLINE88 = None
        DEDENT89 = None
        NEWLINE90 = None
        var_hint83 = None

        var_hint87 = None


        NEWLINE84_tree = None
        INDENT85_tree = None
        NEWLINE86_tree = None
        NEWLINE88_tree = None
        DEDENT89_tree = None
        NEWLINE90_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:93:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:93:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:93:9: ( var_hint )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == CURLY_OPEN or LA15_0 == ID) :
                    alt15 = 1
                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:93:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint850)
                    var_hint83 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint83.tree)





                NEWLINE84 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint854) 
                stream_NEWLINE.add(NEWLINE84)


                # grammar/ShyRecognizerFrontend.g:94:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == INDENT) :
                    alt17 = 1
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:94:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT85 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint866) 
                    stream_INDENT.add(INDENT85)


                    NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint868) 
                    stream_NEWLINE.add(NEWLINE86)


                    # grammar/ShyRecognizerFrontend.g:94:26: ( var_hint NEWLINE )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == CURLY_OPEN or LA16_0 == ID) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:94:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint872)
                            var_hint87 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint87.tree)


                            NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint874) 
                            stream_NEWLINE.add(NEWLINE88)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    DEDENT89 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint880) 
                    stream_DEDENT.add(DEDENT89)


                    NEWLINE90 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint882) 
                    stream_NEWLINE.add(NEWLINE90)





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
                # 95:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:95:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:97:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE95 = None
        INDENT96 = None
        NEWLINE97 = None
        NEWLINE99 = None
        DEDENT100 = None
        var91 = None

        hint92 = None

        var93 = None

        hint94 = None

        var98 = None


        NEWLINE95_tree = None
        INDENT96_tree = None
        NEWLINE97_tree = None
        NEWLINE99_tree = None
        DEDENT100_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:98:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt22 = 3
                alt22 = self.dfa22.predict(self.input)
                if alt22 == 1:
                    # grammar/ShyRecognizerFrontend.g:98:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:98:9: ( var )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == ID) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerFrontend.g:98:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint921)
                            var91 = self.var()

                            self._state.following.pop()
                            stream_var.add(var91.tree)



                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


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
                    # 99:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:99:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:99:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt22 == 2:
                    # grammar/ShyRecognizerFrontend.g:100:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint956)
                    hint92 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint92.tree)


                    # grammar/ShyRecognizerFrontend.g:100:14: ( var )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == ID) :
                            alt19 = 1


                        if alt19 == 1:
                            # grammar/ShyRecognizerFrontend.g:100:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint958)
                            var93 = self.var()

                            self._state.following.pop()
                            stream_var.add(var93.tree)



                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1


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
                    # 101:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:101:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:101:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt22 == 3:
                    # grammar/ShyRecognizerFrontend.g:102:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint992)
                    hint94 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint94.tree)


                    NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint994) 
                    stream_NEWLINE.add(NEWLINE95)


                    INDENT96 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint996) 
                    stream_INDENT.add(INDENT96)


                    NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint998) 
                    stream_NEWLINE.add(NEWLINE97)


                    # grammar/ShyRecognizerFrontend.g:102:37: ( ( var )+ NEWLINE )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == ID) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:102:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:102:39: ( var )+
                            cnt20 = 0
                            while True: #loop20
                                alt20 = 2
                                LA20_0 = self.input.LA(1)

                                if (LA20_0 == ID) :
                                    alt20 = 1


                                if alt20 == 1:
                                    # grammar/ShyRecognizerFrontend.g:102:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1002)
                                    var98 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var98.tree)



                                else:
                                    if cnt20 >= 1:
                                        break #loop20

                                    eee = EarlyExitException(20, self.input)
                                    raise eee

                                cnt20 += 1


                            NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1006) 
                            stream_NEWLINE.add(NEWLINE99)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    DEDENT100 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1012) 
                    stream_DEDENT.add(DEDENT100)


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
                    # 103:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:103:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:103:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:105:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID101 = None

        ID101_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:105:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:105:7: ID
                pass 
                ID101 = self.match(self.input, ID, self.FOLLOW_ID_in_var1046) 
                stream_ID.add(ID101)


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
                # 105:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:105:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:107:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN102 = None
        ID103 = None
        CURLY_CLOSE104 = None
        CURLY_OPEN105 = None
        ID106 = None
        CURLY_CLOSE108 = None
        hint_arg107 = None


        CURLY_OPEN102_tree = None
        ID103_tree = None
        CURLY_CLOSE104_tree = None
        CURLY_OPEN105_tree = None
        ID106_tree = None
        CURLY_CLOSE108_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:108:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == CURLY_OPEN) :
                    LA24_1 = self.input.LA(2)

                    if (LA24_1 == ID) :
                        LA24_2 = self.input.LA(3)

                        if (LA24_2 == CURLY_CLOSE) :
                            alt24 = 1
                        elif (LA24_2 == ID or LA24_2 == UNDERSCORE) :
                            alt24 = 2
                        else:
                            nvae = NoViableAltException("", 24, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerFrontend.g:108:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN102 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1071) 
                    stream_CURLY_OPEN.add(CURLY_OPEN102)


                    ID103 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1073) 
                    stream_ID.add(ID103)


                    CURLY_CLOSE104 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1075) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE104)


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
                    # 108:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:108:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt24 == 2:
                    # grammar/ShyRecognizerFrontend.g:109:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN105 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1095) 
                    stream_CURLY_OPEN.add(CURLY_OPEN105)


                    ID106 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1097) 
                    stream_ID.add(ID106)


                    # grammar/ShyRecognizerFrontend.g:109:23: ( hint_arg )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == ID or LA23_0 == UNDERSCORE) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:109:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1099)
                            hint_arg107 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg107.tree)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    CURLY_CLOSE108 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1103) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE108)


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
                    # 109:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:109:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:109:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:111:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set109 = None

        set109_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:111:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set109 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set109))

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
    # grammar/ShyRecognizerFrontend.g:113:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS110 = None
        NUMBER111 = None

        MINUS110_tree = None
        NUMBER111_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:113:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:113:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:113:13: ( MINUS )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == MINUS) :
                    alt25 = 1
                if alt25 == 1:
                    # grammar/ShyRecognizerFrontend.g:113:13: MINUS
                    pass 
                    MINUS110 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1142)
                    MINUS110_tree = self._adaptor.createWithPayload(MINUS110)
                    self._adaptor.addChild(root_0, MINUS110_tree)






                NUMBER111 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1146)
                NUMBER111_tree = self._adaptor.createWithPayload(NUMBER111)
                self._adaptor.addChild(root_0, NUMBER111_tree)





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
    # grammar/ShyRecognizerFrontend.g:114:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS112 = None
        NUMBER113 = None
        DIVIDE114 = None
        NUMBER115 = None

        MINUS112_tree = None
        NUMBER113_tree = None
        DIVIDE114_tree = None
        NUMBER115_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:114:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:114:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:114:13: ( MINUS )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == MINUS) :
                    alt26 = 1
                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:114:13: MINUS
                    pass 
                    MINUS112 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1154)
                    MINUS112_tree = self._adaptor.createWithPayload(MINUS112)
                    self._adaptor.addChild(root_0, MINUS112_tree)






                NUMBER113 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1158)
                NUMBER113_tree = self._adaptor.createWithPayload(NUMBER113)
                self._adaptor.addChild(root_0, NUMBER113_tree)



                DIVIDE114 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1160)
                DIVIDE114_tree = self._adaptor.createWithPayload(DIVIDE114)
                self._adaptor.addChild(root_0, DIVIDE114_tree)



                NUMBER115 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1162)
                NUMBER115_tree = self._adaptor.createWithPayload(NUMBER115)
                self._adaptor.addChild(root_0, NUMBER115_tree)





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



    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA22_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\1\12\1\uffff\1\16\1\11\1\16\1\11\2\uffff\1\16"
        )

    DFA22_max = DFA.unpack(
        u"\1\16\1\uffff\1\16\1\64\1\22\1\64\2\uffff\1\22"
        )

    DFA22_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA22_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA22_transition = [
        DFA.unpack(u"\1\2\3\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\4\uffff\1\5\45\uffff\1\5"),
        DFA.unpack(u"\1\6\3\uffff\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\5\45\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\7")
    ]

    # class definition for DFA #22

    class DFA22(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 7, 17, 24, 51])
    FOLLOW_stateless_in_start86 = frozenset([1, 7, 17, 24, 51])
    FOLLOW_consts_in_start90 = frozenset([1, 7, 17, 24, 51])
    FOLLOW_types_in_start94 = frozenset([1, 7, 17, 24, 51])
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
    FOLLOW_NEWLINE_in_stateless186 = frozenset([22])
    FOLLOW_proc_in_stateless188 = frozenset([11, 22])
    FOLLOW_DEDENT_in_stateless192 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless194 = frozenset([1])
    FOLLOW_PROC_in_proc235 = frozenset([14])
    FOLLOW_ID_in_proc237 = frozenset([18])
    FOLLOW_NEWLINE_in_proc239 = frozenset([1])
    FOLLOW_PROC_in_proc267 = frozenset([14])
    FOLLOW_ID_in_proc269 = frozenset([18])
    FOLLOW_NEWLINE_in_proc271 = frozenset([15])
    FOLLOW_INDENT_in_proc273 = frozenset([18])
    FOLLOW_NEWLINE_in_proc275 = frozenset([4, 11, 20, 53])
    FOLLOW_proc_args_in_proc289 = frozenset([11, 20, 53])
    FOLLOW_proc_vars_in_proc293 = frozenset([11, 20])
    FOLLOW_proc_ops_in_proc297 = frozenset([11])
    FOLLOW_DEDENT_in_proc309 = frozenset([18])
    FOLLOW_NEWLINE_in_proc311 = frozenset([1])
    FOLLOW_ARGS_in_proc_args360 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_proc_args362 = frozenset([1])
    FOLLOW_VARS_in_proc_vars391 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_proc_vars393 = frozenset([1])
    FOLLOW_OPS_in_proc_ops422 = frozenset([18])
    FOLLOW_NEWLINE_in_proc_ops424 = frozenset([15])
    FOLLOW_INDENT_in_proc_ops426 = frozenset([18])
    FOLLOW_NEWLINE_in_proc_ops428 = frozenset([14])
    FOLLOW_statement_in_proc_ops430 = frozenset([11])
    FOLLOW_DEDENT_in_proc_ops432 = frozenset([18])
    FOLLOW_NEWLINE_in_proc_ops434 = frozenset([1])
    FOLLOW_statement_call_in_statement471 = frozenset([1])
    FOLLOW_ID_in_statement_call490 = frozenset([14, 18])
    FOLLOW_statement_call_args_in_statement_call492 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call496 = frozenset([1, 15])
    FOLLOW_INDENT_in_statement_call509 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call511 = frozenset([14])
    FOLLOW_statement_call_args_in_statement_call515 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call517 = frozenset([11, 14])
    FOLLOW_DEDENT_in_statement_call523 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call525 = frozenset([1])
    FOLLOW_ID_in_statement_call_args583 = frozenset([1, 14])
    FOLLOW_CONSTS_in_consts600 = frozenset([14])
    FOLLOW_ID_in_consts602 = frozenset([18])
    FOLLOW_NEWLINE_in_consts604 = frozenset([15])
    FOLLOW_INDENT_in_consts614 = frozenset([18])
    FOLLOW_NEWLINE_in_consts616 = frozenset([14])
    FOLLOW_consts_items_in_consts618 = frozenset([11])
    FOLLOW_DEDENT_in_consts620 = frozenset([18])
    FOLLOW_NEWLINE_in_consts622 = frozenset([1])
    FOLLOW_consts_item_in_consts_items654 = frozenset([1, 14])
    FOLLOW_ID_in_consts_item670 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item672 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item674 = frozenset([1])
    FOLLOW_ID_in_consts_item696 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item698 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item700 = frozenset([1])
    FOLLOW_ID_in_consts_item722 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item724 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item726 = frozenset([1])
    FOLLOW_TYPES_in_types757 = frozenset([14])
    FOLLOW_ID_in_types759 = frozenset([18])
    FOLLOW_NEWLINE_in_types761 = frozenset([15])
    FOLLOW_INDENT_in_types771 = frozenset([18])
    FOLLOW_NEWLINE_in_types773 = frozenset([14])
    FOLLOW_types_items_in_types775 = frozenset([11])
    FOLLOW_DEDENT_in_types777 = frozenset([18])
    FOLLOW_NEWLINE_in_types779 = frozenset([1])
    FOLLOW_types_item_in_types_items811 = frozenset([1, 14])
    FOLLOW_ID_in_types_item821 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_types_item823 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint850 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint854 = frozenset([1, 15])
    FOLLOW_INDENT_in_vars_hint866 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint868 = frozenset([10, 14])
    FOLLOW_var_hint_in_vars_hint872 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint874 = frozenset([10, 11, 14])
    FOLLOW_DEDENT_in_vars_hint880 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint882 = frozenset([1])
    FOLLOW_var_in_var_hint921 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint956 = frozenset([14])
    FOLLOW_var_in_var_hint958 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint992 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint994 = frozenset([15])
    FOLLOW_INDENT_in_var_hint996 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint998 = frozenset([14])
    FOLLOW_var_in_var_hint1002 = frozenset([14, 18])
    FOLLOW_NEWLINE_in_var_hint1006 = frozenset([11, 14])
    FOLLOW_DEDENT_in_var_hint1012 = frozenset([1])
    FOLLOW_ID_in_var1046 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1071 = frozenset([14])
    FOLLOW_ID_in_hint1073 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint1075 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1095 = frozenset([14])
    FOLLOW_ID_in_hint1097 = frozenset([14, 52])
    FOLLOW_hint_arg_in_hint1099 = frozenset([9, 14, 52])
    FOLLOW_CURLY_CLOSE_in_hint1103 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1142 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole1146 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1154 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1158 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1160 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1162 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
