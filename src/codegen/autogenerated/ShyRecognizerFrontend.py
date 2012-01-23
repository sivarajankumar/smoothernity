# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-23 20:35:23

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

        self.dfa23 = self.DFA23(
            self, 23,
            eot = self.DFA23_eot,
            eof = self.DFA23_eof,
            min = self.DFA23_min,
            max = self.DFA23_max,
            accept = self.DFA23_accept,
            special = self.DFA23_special,
            transition = self.DFA23_transition
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
    # grammar/ShyRecognizerFrontend.g:30:1: stateless : STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS8 = None
        ID9 = None
        NEWLINE10 = None
        INDENT11 = None
        NEWLINE12 = None
        DEDENT14 = None
        NEWLINE15 = None
        proc13 = None


        STATELESS8_tree = None
        ID9_tree = None
        NEWLINE10_tree = None
        INDENT11_tree = None
        NEWLINE12_tree = None
        DEDENT14_tree = None
        NEWLINE15_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:31:5: ( STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:31:9: STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                STATELESS8 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless146) 
                stream_STATELESS.add(STATELESS8)


                ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless148) 
                stream_ID.add(ID9)


                NEWLINE10 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless150) 
                stream_NEWLINE.add(NEWLINE10)


                # grammar/ShyRecognizerFrontend.g:31:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == INDENT) :
                    alt3 = 1
                if alt3 == 1:
                    # grammar/ShyRecognizerFrontend.g:31:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT11 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless154) 
                    stream_INDENT.add(INDENT11)


                    NEWLINE12 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless156) 
                    stream_NEWLINE.add(NEWLINE12)


                    # grammar/ShyRecognizerFrontend.g:31:47: ( proc )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == PROC) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyRecognizerFrontend.g:31:47: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless158)
                            proc13 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc13.tree)



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    DEDENT14 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless162) 
                    stream_DEDENT.add(DEDENT14)


                    NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless164) 
                    stream_NEWLINE.add(NEWLINE15)





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
                # 32:9: -> ^( TREE_STATELESS ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:32:12: ^( TREE_STATELESS ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:32:33: ( proc )*
                while stream_proc.hasNext():
                    self._adaptor.addChild(root_1, stream_proc.nextTree())


                stream_proc.reset();

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
    # grammar/ShyRecognizerFrontend.g:35:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC16 = None
        ID17 = None
        NEWLINE18 = None
        PROC19 = None
        ID20 = None
        NEWLINE21 = None
        INDENT22 = None
        NEWLINE23 = None
        DEDENT27 = None
        NEWLINE28 = None
        proc_args24 = None

        proc_vars25 = None

        proc_ops26 = None


        PROC16_tree = None
        ID17_tree = None
        NEWLINE18_tree = None
        PROC19_tree = None
        ID20_tree = None
        NEWLINE21_tree = None
        INDENT22_tree = None
        NEWLINE23_tree = None
        DEDENT27_tree = None
        NEWLINE28_tree = None
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
                # grammar/ShyRecognizerFrontend.g:36:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? ) )
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
                    # grammar/ShyRecognizerFrontend.g:36:9: PROC ID NEWLINE
                    pass 
                    PROC16 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc209) 
                    stream_PROC.add(PROC16)


                    ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_proc211) 
                    stream_ID.add(ID17)


                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc213) 
                    stream_NEWLINE.add(NEWLINE18)


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
                    # 37:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:37:12: ^( TREE_PROC ID )
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
                    # grammar/ShyRecognizerFrontend.g:38:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? ( proc_ops )? DEDENT NEWLINE
                    pass 
                    PROC19 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc241) 
                    stream_PROC.add(PROC19)


                    ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_proc243) 
                    stream_ID.add(ID20)


                    NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc245) 
                    stream_NEWLINE.add(NEWLINE21)


                    INDENT22 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc247) 
                    stream_INDENT.add(INDENT22)


                    NEWLINE23 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc249) 
                    stream_NEWLINE.add(NEWLINE23)


                    # grammar/ShyRecognizerFrontend.g:39:13: ( proc_args )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ARGS) :
                        alt4 = 1
                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:39:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc263)
                        proc_args24 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args24.tree)





                    # grammar/ShyRecognizerFrontend.g:39:25: ( proc_vars )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == VARS) :
                        alt5 = 1
                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:39:25: proc_vars
                        pass 
                        self._state.following.append(self.FOLLOW_proc_vars_in_proc267)
                        proc_vars25 = self.proc_vars()

                        self._state.following.pop()
                        stream_proc_vars.add(proc_vars25.tree)





                    # grammar/ShyRecognizerFrontend.g:39:37: ( proc_ops )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == OPS) :
                        alt6 = 1
                    if alt6 == 1:
                        # grammar/ShyRecognizerFrontend.g:39:37: proc_ops
                        pass 
                        self._state.following.append(self.FOLLOW_proc_ops_in_proc271)
                        proc_ops26 = self.proc_ops()

                        self._state.following.pop()
                        stream_proc_ops.add(proc_ops26.tree)





                    DEDENT27 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc283) 
                    stream_DEDENT.add(DEDENT27)


                    NEWLINE28 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc285) 
                    stream_NEWLINE.add(NEWLINE28)


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
                    # 41:9: -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? )
                    # grammar/ShyRecognizerFrontend.g:41:12: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ( proc_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:41:28: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:41:40: ( proc_vars )?
                    if stream_proc_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_vars.nextTree())


                    stream_proc_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:41:52: ( proc_ops )?
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
    # grammar/ShyRecognizerFrontend.g:44:1: proc_args : ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS29 = None
        vars_hint30 = None


        ARGS29_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:45:5: ( ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:45:9: ARGS vars_hint
                pass 
                ARGS29 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args334) 
                stream_ARGS.add(ARGS29)


                self._state.following.append(self.FOLLOW_vars_hint_in_proc_args336)
                vars_hint30 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint30.tree)


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


    class proc_vars_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_vars_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc_vars"
    # grammar/ShyRecognizerFrontend.g:48:1: proc_vars : VARS vars_hint -> ^( TREE_PROC_VARS vars_hint ) ;
    def proc_vars(self, ):
        retval = self.proc_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS31 = None
        vars_hint32 = None


        VARS31_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:49:5: ( VARS vars_hint -> ^( TREE_PROC_VARS vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:49:9: VARS vars_hint
                pass 
                VARS31 = self.match(self.input, VARS, self.FOLLOW_VARS_in_proc_vars365) 
                stream_VARS.add(VARS31)


                self._state.following.append(self.FOLLOW_vars_hint_in_proc_vars367)
                vars_hint32 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint32.tree)


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
                # 49:24: -> ^( TREE_PROC_VARS vars_hint )
                # grammar/ShyRecognizerFrontend.g:49:27: ^( TREE_PROC_VARS vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:52:1: proc_ops : OPS NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_PROC_OPS ( statement )+ ) ;
    def proc_ops(self, ):
        retval = self.proc_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS33 = None
        NEWLINE34 = None
        INDENT35 = None
        NEWLINE36 = None
        DEDENT38 = None
        NEWLINE39 = None
        statement37 = None


        OPS33_tree = None
        NEWLINE34_tree = None
        INDENT35_tree = None
        NEWLINE36_tree = None
        DEDENT38_tree = None
        NEWLINE39_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:53:5: ( OPS NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_PROC_OPS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:53:9: OPS NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                OPS33 = self.match(self.input, OPS, self.FOLLOW_OPS_in_proc_ops396) 
                stream_OPS.add(OPS33)


                NEWLINE34 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops398) 
                stream_NEWLINE.add(NEWLINE34)


                INDENT35 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc_ops400) 
                stream_INDENT.add(INDENT35)


                NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops402) 
                stream_NEWLINE.add(NEWLINE36)


                # grammar/ShyRecognizerFrontend.g:53:36: ( statement )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == ID) :
                        alt8 = 1


                    if alt8 == 1:
                        # grammar/ShyRecognizerFrontend.g:53:36: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_proc_ops404)
                        statement37 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement37.tree)



                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                DEDENT38 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc_ops408) 
                stream_DEDENT.add(DEDENT38)


                NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops410) 
                stream_NEWLINE.add(NEWLINE39)


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
                # 54:9: -> ^( TREE_PROC_OPS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:54:12: ^( TREE_PROC_OPS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC_OPS, "TREE_PROC_OPS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:54:29: ( statement )+
                if not (stream_statement.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_statement.hasNext():
                    self._adaptor.addChild(root_1, stream_statement.nextTree())


                stream_statement.reset()

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
    # grammar/ShyRecognizerFrontend.g:57:1: statement : statement_call ;
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call40 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:58:5: ( statement_call )
                # grammar/ShyRecognizerFrontend.g:58:9: statement_call
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_statement_call_in_statement449)
                statement_call40 = self.statement_call()

                self._state.following.pop()
                self._adaptor.addChild(root_0, statement_call40.tree)




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
    # grammar/ShyRecognizerFrontend.g:61:1: statement_call : ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID41 = None
        NEWLINE43 = None
        INDENT44 = None
        NEWLINE45 = None
        NEWLINE47 = None
        DEDENT48 = None
        NEWLINE49 = None
        statement_call_args42 = None

        statement_call_args46 = None


        ID41_tree = None
        NEWLINE43_tree = None
        INDENT44_tree = None
        NEWLINE45_tree = None
        NEWLINE47_tree = None
        DEDENT48_tree = None
        NEWLINE49_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:62:5: ( ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:62:9: ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call468) 
                stream_ID.add(ID41)


                # grammar/ShyRecognizerFrontend.g:62:12: ( statement_call_args )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == ID) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:62:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call470)
                    statement_call_args42 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args42.tree)





                NEWLINE43 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call474) 
                stream_NEWLINE.add(NEWLINE43)


                # grammar/ShyRecognizerFrontend.g:63:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == INDENT) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerFrontend.g:63:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT44 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call487) 
                    stream_INDENT.add(INDENT44)


                    NEWLINE45 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call489) 
                    stream_NEWLINE.add(NEWLINE45)


                    # grammar/ShyRecognizerFrontend.g:63:26: ( statement_call_args NEWLINE )+
                    cnt10 = 0
                    while True: #loop10
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == ID) :
                            alt10 = 1


                        if alt10 == 1:
                            # grammar/ShyRecognizerFrontend.g:63:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call493)
                            statement_call_args46 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args46.tree)


                            NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call495) 
                            stream_NEWLINE.add(NEWLINE47)



                        else:
                            if cnt10 >= 1:
                                break #loop10

                            eee = EarlyExitException(10, self.input)
                            raise eee

                        cnt10 += 1


                    DEDENT48 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call501) 
                    stream_DEDENT.add(DEDENT48)


                    NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call503) 
                    stream_NEWLINE.add(NEWLINE49)





                # AST Rewrite
                # elements: statement_call_args, ID
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
                # 64:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:64:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:65:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:68:1: statement_call_args : ( ID )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID50 = None

        ID50_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:68:21: ( ( ID )+ )
                # grammar/ShyRecognizerFrontend.g:68:23: ( ID )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:68:23: ( ID )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == ID) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:68:23: ID
                        pass 
                        ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_args561)
                        ID50_tree = self._adaptor.createWithPayload(ID50)
                        self._adaptor.addChild(root_0, ID50_tree)




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

    # $ANTLR end "statement_call_args"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:70:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS51 = None
        ID52 = None
        NEWLINE53 = None
        INDENT54 = None
        NEWLINE55 = None
        DEDENT57 = None
        NEWLINE58 = None
        consts_items56 = None


        CONSTS51_tree = None
        ID52_tree = None
        NEWLINE53_tree = None
        INDENT54_tree = None
        NEWLINE55_tree = None
        DEDENT57_tree = None
        NEWLINE58_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:71:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:71:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS51 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts578) 
                stream_CONSTS.add(CONSTS51)


                ID52 = self.match(self.input, ID, self.FOLLOW_ID_in_consts580) 
                stream_ID.add(ID52)


                NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts582) 
                stream_NEWLINE.add(NEWLINE53)


                INDENT54 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts592) 
                stream_INDENT.add(INDENT54)


                NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts594) 
                stream_NEWLINE.add(NEWLINE55)


                self._state.following.append(self.FOLLOW_consts_items_in_consts596)
                consts_items56 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items56.tree)


                DEDENT57 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts598) 
                stream_DEDENT.add(DEDENT57)


                NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts600) 
                stream_NEWLINE.add(NEWLINE58)


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
                # 73:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:73:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:75:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item59 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:75:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:75:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:75:16: ( consts_item )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == ID) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:75:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items632)
                        consts_item59 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item59.tree)



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1




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
    # grammar/ShyRecognizerFrontend.g:76:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID60 = None
        NEWLINE62 = None
        ID63 = None
        NEWLINE65 = None
        ID66 = None
        EXPRESSION67 = None
        NEWLINE68 = None
        num_whole61 = None

        num_fract64 = None


        ID60_tree = None
        NEWLINE62_tree = None
        ID63_tree = None
        NEWLINE65_tree = None
        ID66_tree = None
        EXPRESSION67_tree = None
        NEWLINE68_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:77:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt14 = 3
                LA14_0 = self.input.LA(1)

                if (LA14_0 == ID) :
                    LA14 = self.input.LA(2)
                    if LA14 == EXPRESSION:
                        alt14 = 3
                    elif LA14 == MINUS:
                        LA14_3 = self.input.LA(3)

                        if (LA14_3 == NUMBER) :
                            LA14_4 = self.input.LA(4)

                            if (LA14_4 == DIVIDE) :
                                alt14 = 2
                            elif (LA14_4 == NEWLINE) :
                                alt14 = 1
                            else:
                                nvae = NoViableAltException("", 14, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 14, 3, self.input)

                            raise nvae


                    elif LA14 == NUMBER:
                        LA14_4 = self.input.LA(3)

                        if (LA14_4 == DIVIDE) :
                            alt14 = 2
                        elif (LA14_4 == NEWLINE) :
                            alt14 = 1
                        else:
                            nvae = NoViableAltException("", 14, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 14, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:77:9: ID num_whole NEWLINE
                    pass 
                    ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item648) 
                    stream_ID.add(ID60)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item650)
                    num_whole61 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole61.tree)


                    NEWLINE62 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item652) 
                    stream_NEWLINE.add(NEWLINE62)


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
                    # 77:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:77:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt14 == 2:
                    # grammar/ShyRecognizerFrontend.g:78:9: ID num_fract NEWLINE
                    pass 
                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item674) 
                    stream_ID.add(ID63)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item676)
                    num_fract64 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract64.tree)


                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item678) 
                    stream_NEWLINE.add(NEWLINE65)


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
                    # 78:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:78:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt14 == 3:
                    # grammar/ShyRecognizerFrontend.g:79:9: ID EXPRESSION NEWLINE
                    pass 
                    ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item700) 
                    stream_ID.add(ID66)


                    EXPRESSION67 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item702) 
                    stream_EXPRESSION.add(EXPRESSION67)


                    NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item704) 
                    stream_NEWLINE.add(NEWLINE68)


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
                    # 79:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:79:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:82:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES69 = None
        ID70 = None
        NEWLINE71 = None
        INDENT72 = None
        NEWLINE73 = None
        DEDENT75 = None
        NEWLINE76 = None
        types_items74 = None


        TYPES69_tree = None
        ID70_tree = None
        NEWLINE71_tree = None
        INDENT72_tree = None
        NEWLINE73_tree = None
        DEDENT75_tree = None
        NEWLINE76_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:83:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES69 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types735) 
                stream_TYPES.add(TYPES69)


                ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_types737) 
                stream_ID.add(ID70)


                NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types739) 
                stream_NEWLINE.add(NEWLINE71)


                INDENT72 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types749) 
                stream_INDENT.add(INDENT72)


                NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types751) 
                stream_NEWLINE.add(NEWLINE73)


                self._state.following.append(self.FOLLOW_types_items_in_types753)
                types_items74 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items74.tree)


                DEDENT75 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types755) 
                stream_DEDENT.add(DEDENT75)


                NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types757) 
                stream_NEWLINE.add(NEWLINE76)


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
                # 85:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:85:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:87:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item77 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:87:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:87:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:87:15: ( types_item )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == ID) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:87:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items789)
                        types_item77 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item77.tree)



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1




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
    # grammar/ShyRecognizerFrontend.g:88:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID78 = None
        vars_hint79 = None


        ID78_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:88:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:88:14: ID vars_hint
                pass 
                ID78 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item799) 
                stream_ID.add(ID78)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item801)
                vars_hint79 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint79.tree)


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
                # 88:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:88:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:90:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE81 = None
        INDENT82 = None
        NEWLINE83 = None
        NEWLINE85 = None
        DEDENT86 = None
        NEWLINE87 = None
        var_hint80 = None

        var_hint84 = None


        NEWLINE81_tree = None
        INDENT82_tree = None
        NEWLINE83_tree = None
        NEWLINE85_tree = None
        DEDENT86_tree = None
        NEWLINE87_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:91:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:91:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:91:9: ( var_hint )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == CURLY_OPEN or LA16_0 == ID) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:91:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint828)
                    var_hint80 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint80.tree)





                NEWLINE81 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint832) 
                stream_NEWLINE.add(NEWLINE81)


                # grammar/ShyRecognizerFrontend.g:92:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == INDENT) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:92:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT82 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint844) 
                    stream_INDENT.add(INDENT82)


                    NEWLINE83 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint846) 
                    stream_NEWLINE.add(NEWLINE83)


                    # grammar/ShyRecognizerFrontend.g:92:26: ( var_hint NEWLINE )+
                    cnt17 = 0
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if (LA17_0 == CURLY_OPEN or LA17_0 == ID) :
                            alt17 = 1


                        if alt17 == 1:
                            # grammar/ShyRecognizerFrontend.g:92:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint850)
                            var_hint84 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint84.tree)


                            NEWLINE85 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint852) 
                            stream_NEWLINE.add(NEWLINE85)



                        else:
                            if cnt17 >= 1:
                                break #loop17

                            eee = EarlyExitException(17, self.input)
                            raise eee

                        cnt17 += 1


                    DEDENT86 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint858) 
                    stream_DEDENT.add(DEDENT86)


                    NEWLINE87 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint860) 
                    stream_NEWLINE.add(NEWLINE87)





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
                # 93:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:93:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:95:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE92 = None
        INDENT93 = None
        NEWLINE94 = None
        NEWLINE96 = None
        DEDENT97 = None
        var88 = None

        hint89 = None

        var90 = None

        hint91 = None

        var95 = None


        NEWLINE92_tree = None
        INDENT93_tree = None
        NEWLINE94_tree = None
        NEWLINE96_tree = None
        DEDENT97_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:96:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt23 = 3
                alt23 = self.dfa23.predict(self.input)
                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:96:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:96:9: ( var )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == ID) :
                            alt19 = 1


                        if alt19 == 1:
                            # grammar/ShyRecognizerFrontend.g:96:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint899)
                            var88 = self.var()

                            self._state.following.pop()
                            stream_var.add(var88.tree)



                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1


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
                    # 97:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:97:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:97:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt23 == 2:
                    # grammar/ShyRecognizerFrontend.g:98:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint934)
                    hint89 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint89.tree)


                    # grammar/ShyRecognizerFrontend.g:98:14: ( var )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == ID) :
                            alt20 = 1


                        if alt20 == 1:
                            # grammar/ShyRecognizerFrontend.g:98:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint936)
                            var90 = self.var()

                            self._state.following.pop()
                            stream_var.add(var90.tree)



                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


                    # AST Rewrite
                    # elements: var, hint
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
                    # 99:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:99:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:99:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt23 == 3:
                    # grammar/ShyRecognizerFrontend.g:100:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint970)
                    hint91 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint91.tree)


                    NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint972) 
                    stream_NEWLINE.add(NEWLINE92)


                    INDENT93 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint974) 
                    stream_INDENT.add(INDENT93)


                    NEWLINE94 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint976) 
                    stream_NEWLINE.add(NEWLINE94)


                    # grammar/ShyRecognizerFrontend.g:100:37: ( ( var )+ NEWLINE )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == ID) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:100:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:100:39: ( var )+
                            cnt21 = 0
                            while True: #loop21
                                alt21 = 2
                                LA21_0 = self.input.LA(1)

                                if (LA21_0 == ID) :
                                    alt21 = 1


                                if alt21 == 1:
                                    # grammar/ShyRecognizerFrontend.g:100:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint980)
                                    var95 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var95.tree)



                                else:
                                    if cnt21 >= 1:
                                        break #loop21

                                    eee = EarlyExitException(21, self.input)
                                    raise eee

                                cnt21 += 1


                            NEWLINE96 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint984) 
                            stream_NEWLINE.add(NEWLINE96)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    DEDENT97 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint990) 
                    stream_DEDENT.add(DEDENT97)


                    # AST Rewrite
                    # elements: var, hint
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
    # grammar/ShyRecognizerFrontend.g:103:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID98 = None

        ID98_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:103:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:103:7: ID
                pass 
                ID98 = self.match(self.input, ID, self.FOLLOW_ID_in_var1024) 
                stream_ID.add(ID98)


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
                # 103:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:103:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:105:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN99 = None
        ID100 = None
        CURLY_CLOSE101 = None
        CURLY_OPEN102 = None
        ID103 = None
        CURLY_CLOSE105 = None
        hint_arg104 = None


        CURLY_OPEN99_tree = None
        ID100_tree = None
        CURLY_CLOSE101_tree = None
        CURLY_OPEN102_tree = None
        ID103_tree = None
        CURLY_CLOSE105_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:106:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == CURLY_OPEN) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 == ID) :
                        LA25_2 = self.input.LA(3)

                        if (LA25_2 == CURLY_CLOSE) :
                            alt25 = 1
                        elif (LA25_2 == ID or LA25_2 == UNDERSCORE) :
                            alt25 = 2
                        else:
                            nvae = NoViableAltException("", 25, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # grammar/ShyRecognizerFrontend.g:106:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN99 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1049) 
                    stream_CURLY_OPEN.add(CURLY_OPEN99)


                    ID100 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1051) 
                    stream_ID.add(ID100)


                    CURLY_CLOSE101 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1053) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE101)


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
                    # 106:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:106:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt25 == 2:
                    # grammar/ShyRecognizerFrontend.g:107:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN102 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1073) 
                    stream_CURLY_OPEN.add(CURLY_OPEN102)


                    ID103 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1075) 
                    stream_ID.add(ID103)


                    # grammar/ShyRecognizerFrontend.g:107:23: ( hint_arg )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == ID or LA24_0 == UNDERSCORE) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:107:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1077)
                            hint_arg104 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg104.tree)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    CURLY_CLOSE105 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1081) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE105)


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
                    # 107:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:107:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:107:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:109:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set106 = None

        set106_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:109:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set106 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set106))

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
    # grammar/ShyRecognizerFrontend.g:111:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS107 = None
        NUMBER108 = None

        MINUS107_tree = None
        NUMBER108_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:111:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:111:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:111:13: ( MINUS )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == MINUS) :
                    alt26 = 1
                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:111:13: MINUS
                    pass 
                    MINUS107 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1120)
                    MINUS107_tree = self._adaptor.createWithPayload(MINUS107)
                    self._adaptor.addChild(root_0, MINUS107_tree)






                NUMBER108 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1124)
                NUMBER108_tree = self._adaptor.createWithPayload(NUMBER108)
                self._adaptor.addChild(root_0, NUMBER108_tree)





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
    # grammar/ShyRecognizerFrontend.g:112:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS109 = None
        NUMBER110 = None
        DIVIDE111 = None
        NUMBER112 = None

        MINUS109_tree = None
        NUMBER110_tree = None
        DIVIDE111_tree = None
        NUMBER112_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:112:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:112:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:112:13: ( MINUS )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == MINUS) :
                    alt27 = 1
                if alt27 == 1:
                    # grammar/ShyRecognizerFrontend.g:112:13: MINUS
                    pass 
                    MINUS109 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1132)
                    MINUS109_tree = self._adaptor.createWithPayload(MINUS109)
                    self._adaptor.addChild(root_0, MINUS109_tree)






                NUMBER110 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1136)
                NUMBER110_tree = self._adaptor.createWithPayload(NUMBER110)
                self._adaptor.addChild(root_0, NUMBER110_tree)



                DIVIDE111 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1138)
                DIVIDE111_tree = self._adaptor.createWithPayload(DIVIDE111)
                self._adaptor.addChild(root_0, DIVIDE111_tree)



                NUMBER112 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1140)
                NUMBER112_tree = self._adaptor.createWithPayload(NUMBER112)
                self._adaptor.addChild(root_0, NUMBER112_tree)





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



    # lookup tables for DFA #23

    DFA23_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA23_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA23_min = DFA.unpack(
        u"\1\12\1\uffff\1\16\1\11\1\16\1\11\2\uffff\1\16"
        )

    DFA23_max = DFA.unpack(
        u"\1\16\1\uffff\1\16\1\64\1\22\1\64\2\uffff\1\22"
        )

    DFA23_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA23_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA23_transition = [
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

    # class definition for DFA #23

    class DFA23(DFA):
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
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1, 15])
    FOLLOW_INDENT_in_stateless154 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless156 = frozenset([22])
    FOLLOW_proc_in_stateless158 = frozenset([11, 22])
    FOLLOW_DEDENT_in_stateless162 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless164 = frozenset([1])
    FOLLOW_PROC_in_proc209 = frozenset([14])
    FOLLOW_ID_in_proc211 = frozenset([18])
    FOLLOW_NEWLINE_in_proc213 = frozenset([1])
    FOLLOW_PROC_in_proc241 = frozenset([14])
    FOLLOW_ID_in_proc243 = frozenset([18])
    FOLLOW_NEWLINE_in_proc245 = frozenset([15])
    FOLLOW_INDENT_in_proc247 = frozenset([18])
    FOLLOW_NEWLINE_in_proc249 = frozenset([4, 11, 20, 53])
    FOLLOW_proc_args_in_proc263 = frozenset([11, 20, 53])
    FOLLOW_proc_vars_in_proc267 = frozenset([11, 20])
    FOLLOW_proc_ops_in_proc271 = frozenset([11])
    FOLLOW_DEDENT_in_proc283 = frozenset([18])
    FOLLOW_NEWLINE_in_proc285 = frozenset([1])
    FOLLOW_ARGS_in_proc_args334 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_proc_args336 = frozenset([1])
    FOLLOW_VARS_in_proc_vars365 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_proc_vars367 = frozenset([1])
    FOLLOW_OPS_in_proc_ops396 = frozenset([18])
    FOLLOW_NEWLINE_in_proc_ops398 = frozenset([15])
    FOLLOW_INDENT_in_proc_ops400 = frozenset([18])
    FOLLOW_NEWLINE_in_proc_ops402 = frozenset([14])
    FOLLOW_statement_in_proc_ops404 = frozenset([11, 14])
    FOLLOW_DEDENT_in_proc_ops408 = frozenset([18])
    FOLLOW_NEWLINE_in_proc_ops410 = frozenset([1])
    FOLLOW_statement_call_in_statement449 = frozenset([1])
    FOLLOW_ID_in_statement_call468 = frozenset([14, 18])
    FOLLOW_statement_call_args_in_statement_call470 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call474 = frozenset([1, 15])
    FOLLOW_INDENT_in_statement_call487 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call489 = frozenset([14])
    FOLLOW_statement_call_args_in_statement_call493 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call495 = frozenset([11, 14])
    FOLLOW_DEDENT_in_statement_call501 = frozenset([18])
    FOLLOW_NEWLINE_in_statement_call503 = frozenset([1])
    FOLLOW_ID_in_statement_call_args561 = frozenset([1, 14])
    FOLLOW_CONSTS_in_consts578 = frozenset([14])
    FOLLOW_ID_in_consts580 = frozenset([18])
    FOLLOW_NEWLINE_in_consts582 = frozenset([15])
    FOLLOW_INDENT_in_consts592 = frozenset([18])
    FOLLOW_NEWLINE_in_consts594 = frozenset([14])
    FOLLOW_consts_items_in_consts596 = frozenset([11])
    FOLLOW_DEDENT_in_consts598 = frozenset([18])
    FOLLOW_NEWLINE_in_consts600 = frozenset([1])
    FOLLOW_consts_item_in_consts_items632 = frozenset([1, 14])
    FOLLOW_ID_in_consts_item648 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item650 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item652 = frozenset([1])
    FOLLOW_ID_in_consts_item674 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item676 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item678 = frozenset([1])
    FOLLOW_ID_in_consts_item700 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item702 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item704 = frozenset([1])
    FOLLOW_TYPES_in_types735 = frozenset([14])
    FOLLOW_ID_in_types737 = frozenset([18])
    FOLLOW_NEWLINE_in_types739 = frozenset([15])
    FOLLOW_INDENT_in_types749 = frozenset([18])
    FOLLOW_NEWLINE_in_types751 = frozenset([14])
    FOLLOW_types_items_in_types753 = frozenset([11])
    FOLLOW_DEDENT_in_types755 = frozenset([18])
    FOLLOW_NEWLINE_in_types757 = frozenset([1])
    FOLLOW_types_item_in_types_items789 = frozenset([1, 14])
    FOLLOW_ID_in_types_item799 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_types_item801 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint828 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint832 = frozenset([1, 15])
    FOLLOW_INDENT_in_vars_hint844 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint846 = frozenset([10, 14])
    FOLLOW_var_hint_in_vars_hint850 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint852 = frozenset([10, 11, 14])
    FOLLOW_DEDENT_in_vars_hint858 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint860 = frozenset([1])
    FOLLOW_var_in_var_hint899 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint934 = frozenset([14])
    FOLLOW_var_in_var_hint936 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint970 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint972 = frozenset([15])
    FOLLOW_INDENT_in_var_hint974 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint976 = frozenset([14])
    FOLLOW_var_in_var_hint980 = frozenset([14, 18])
    FOLLOW_NEWLINE_in_var_hint984 = frozenset([11, 14])
    FOLLOW_DEDENT_in_var_hint990 = frozenset([1])
    FOLLOW_ID_in_var1024 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1049 = frozenset([14])
    FOLLOW_ID_in_hint1051 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint1053 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1073 = frozenset([14])
    FOLLOW_ID_in_hint1075 = frozenset([14, 52])
    FOLLOW_hint_arg_in_hint1077 = frozenset([9, 14, 52])
    FOLLOW_CURLY_CLOSE_in_hint1081 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1120 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole1124 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1132 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1136 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1138 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract1140 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
