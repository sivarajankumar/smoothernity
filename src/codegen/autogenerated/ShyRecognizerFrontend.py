# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-26 19:29:46

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
ALL=4
ANY=5
ARGS=6
ARROW_LEFT=7
ARROW_RIGHT=8
CONSTS=9
COPY=10
CURLY_CLOSE=11
CURLY_OPEN=12
DEDENT=13
DIVIDE=14
DO=15
ELIF=16
ELSE=17
EXPRESSION=18
ID=19
IF=20
INDENT=21
MINUS=22
MODULE=23
NEWLINE=24
NUMBER=25
OPS=26
PASTE=27
PROC=28
REPLACE=29
STATELESS=30
STRING=31
TREE_ARBITRARY_TOKEN=32
TREE_CONDITION_ALL=33
TREE_CONDITION_ANY=34
TREE_CONSTS=35
TREE_COPY=36
TREE_COPY_PASTE=37
TREE_EXPRESSION=38
TREE_HINT=39
TREE_HINT_NONE=40
TREE_MODULE=41
TREE_NUM_FRACT=42
TREE_NUM_WHOLE=43
TREE_PASTE=44
TREE_PASTE_REPLACE=45
TREE_PASTE_WITH=46
TREE_PROC=47
TREE_PROC_ARGS=48
TREE_PROC_VARS=49
TREE_STATELESS=50
TREE_STATEMENTS=51
TREE_STATEMENT_CALL=52
TREE_STATEMENT_ELIF=53
TREE_STATEMENT_ELSE=54
TREE_STATEMENT_IF=55
TREE_TYPES=56
TREE_TYPES_ITEM=57
TREE_VAR=58
TREE_VARS_HINT=59
TREE_VAR_HINT=60
TYPES=61
UNDERSCORE=62
VARS=63
WHITESPACE=64
WITH=65

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", 
    "OPS", "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", 
    "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", 
    "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", 
    "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", 
    "TREE_PASTE_WITH", "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", 
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_TYPES", "TREE_TYPES_ITEM", 
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

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )

        self.dfa19 = self.DFA19(
            self, 19,
            eot = self.DFA19_eot,
            eof = self.DFA19_eof,
            min = self.DFA19_min,
            max = self.DFA19_max,
            accept = self.DFA19_accept,
            special = self.DFA19_special,
            transition = self.DFA19_transition
            )

        self.dfa35 = self.DFA35(
            self, 35,
            eot = self.DFA35_eot,
            eof = self.DFA35_eof,
            min = self.DFA35_min,
            max = self.DFA35_max,
            accept = self.DFA35_accept,
            special = self.DFA35_special,
            transition = self.DFA35_transition
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
                    # elements: proc_args, proc_vars, proc_ops, ID
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
    # grammar/ShyRecognizerFrontend.g:52:1: proc_ops : OPS NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENTS ( statement )+ ) ;
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
                # grammar/ShyRecognizerFrontend.g:53:5: ( OPS NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENTS ( statement )+ ) )
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

                    if ((ID <= LA8_0 <= IF)) :
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
                # 54:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:54:12: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:54:31: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:57:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE41 = None
        statement_call_single_line40 = None

        statement_call_multi_line42 = None

        statement_if43 = None


        NEWLINE41_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:58:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if )
                alt9 = 3
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:58:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement449)
                    statement_call_single_line40 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line40.tree)


                    NEWLINE41 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement451) 
                    stream_NEWLINE.add(NEWLINE41)


                    # AST Rewrite
                    # elements: statement_call_single_line
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
                    # 59:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt9 == 2:
                    # grammar/ShyRecognizerFrontend.g:60:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement477)
                    statement_call_multi_line42 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line42.tree)



                elif alt9 == 3:
                    # grammar/ShyRecognizerFrontend.g:61:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement487)
                    statement_if43 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if43.tree)



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


    class statement_if_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_if_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerFrontend.g:64:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head44 = None

        statement_elif45 = None

        statement_else46 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:65:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:65:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if506)
                statement_if_head44 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head44.tree)


                # grammar/ShyRecognizerFrontend.g:66:9: ( statement_elif )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ELIF) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:66:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if516)
                        statement_elif45 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif45.tree)



                    else:
                        break #loop10


                # grammar/ShyRecognizerFrontend.g:67:9: ( statement_else )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == ELSE) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerFrontend.g:67:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if528)
                    statement_else46 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else46.tree)





                # AST Rewrite
                # elements: statement_else, statement_elif, statement_if_head
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
                # 68:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:68:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:70:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:71:17: ( statement_else )?
                if stream_statement_else.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_else.nextTree())


                stream_statement_else.reset();

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

    # $ANTLR end "statement_if"


    class statement_if_head_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_if_head_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_if_head"
    # grammar/ShyRecognizerFrontend.g:75:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF47 = None
        statement_elif_body48 = None


        IF47_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:76:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:76:9: IF statement_elif_body
                pass 
                IF47 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head636) 
                stream_IF.add(IF47)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head638)
                statement_elif_body48 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body48.tree)


                # AST Rewrite
                # elements: statement_elif_body
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
                # 77:9: -> statement_elif_body
                self._adaptor.addChild(root_0, stream_statement_elif_body.nextTree())




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

    # $ANTLR end "statement_if_head"


    class statement_elif_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_elif_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_elif"
    # grammar/ShyRecognizerFrontend.g:80:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF49 = None
        statement_elif_body50 = None


        ELIF49_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:81:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:81:9: ELIF statement_elif_body
                pass 
                ELIF49 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif670) 
                stream_ELIF.add(ELIF49)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif672)
                statement_elif_body50 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body50.tree)


                # AST Rewrite
                # elements: statement_elif_body
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
                # 82:9: -> statement_elif_body
                self._adaptor.addChild(root_0, stream_statement_elif_body.nextTree())




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

    # $ANTLR end "statement_elif"


    class statement_elif_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_elif_body_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_elif_body"
    # grammar/ShyRecognizerFrontend.g:85:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE52 = None
        DO53 = None
        NEWLINE54 = None
        INDENT55 = None
        NEWLINE56 = None
        DEDENT58 = None
        NEWLINE59 = None
        condition51 = None

        statement57 = None


        NEWLINE52_tree = None
        DO53_tree = None
        NEWLINE54_tree = None
        INDENT55_tree = None
        NEWLINE56_tree = None
        DEDENT58_tree = None
        NEWLINE59_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:86:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:86:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body704)
                condition51 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition51.tree)


                # grammar/ShyRecognizerFrontend.g:86:19: ( NEWLINE )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == NEWLINE) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:86:19: NEWLINE
                    pass 
                    NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body706) 
                    stream_NEWLINE.add(NEWLINE52)





                DO53 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body710) 
                stream_DO.add(DO53)


                NEWLINE54 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body712) 
                stream_NEWLINE.add(NEWLINE54)


                INDENT55 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body726) 
                stream_INDENT.add(INDENT55)


                NEWLINE56 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body728) 
                stream_NEWLINE.add(NEWLINE56)


                # grammar/ShyRecognizerFrontend.g:87:28: ( statement )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((ID <= LA13_0 <= IF)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:87:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_elif_body730)
                        statement57 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement57.tree)



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                DEDENT58 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body734) 
                stream_DEDENT.add(DEDENT58)


                NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body736) 
                stream_NEWLINE.add(NEWLINE59)


                # AST Rewrite
                # elements: statement, condition
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
                # 88:9: -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:88:13: ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                self._adaptor.addChild(root_1, stream_condition.nextTree())

                # grammar/ShyRecognizerFrontend.g:90:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:90:36: ( statement )+
                if not (stream_statement.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_statement.hasNext():
                    self._adaptor.addChild(root_2, stream_statement.nextTree())


                stream_statement.reset()

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

    # $ANTLR end "statement_elif_body"


    class statement_else_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_else_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerFrontend.g:94:1: statement_else : ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE60 = None
        NEWLINE61 = None
        INDENT62 = None
        NEWLINE63 = None
        DEDENT65 = None
        NEWLINE66 = None
        statement64 = None


        ELSE60_tree = None
        NEWLINE61_tree = None
        INDENT62_tree = None
        NEWLINE63_tree = None
        DEDENT65_tree = None
        NEWLINE66_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:95:5: ( ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:95:9: ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELSE60 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else828) 
                stream_ELSE.add(ELSE60)


                NEWLINE61 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else830) 
                stream_NEWLINE.add(NEWLINE61)


                INDENT62 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else844) 
                stream_INDENT.add(INDENT62)


                NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else846) 
                stream_NEWLINE.add(NEWLINE63)


                # grammar/ShyRecognizerFrontend.g:96:28: ( statement )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((ID <= LA14_0 <= IF)) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:96:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_else848)
                        statement64 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement64.tree)



                    else:
                        if cnt14 >= 1:
                            break #loop14

                        eee = EarlyExitException(14, self.input)
                        raise eee

                    cnt14 += 1


                DEDENT65 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else852) 
                stream_DEDENT.add(DEDENT65)


                NEWLINE66 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else854) 
                stream_NEWLINE.add(NEWLINE66)


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
                # 97:9: -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:97:13: ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:98:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:98:36: ( statement )+
                if not (stream_statement.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_statement.hasNext():
                    self._adaptor.addChild(root_2, stream_statement.nextTree())


                stream_statement.reset()

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

    # $ANTLR end "statement_else"


    class condition_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.condition_return, self).__init__()

            self.tree = None





    # $ANTLR start "condition"
    # grammar/ShyRecognizerFrontend.g:102:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY68 = None
        ALL70 = None
        condition_call67 = None

        condition_calls69 = None

        condition_calls71 = None


        ANY68_tree = None
        ALL70_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:103:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt15 = 3
                LA15 = self.input.LA(1)
                if LA15 == ID:
                    alt15 = 1
                elif LA15 == ANY:
                    alt15 = 2
                elif LA15 == ALL:
                    alt15 = 3
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:103:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition928)
                    condition_call67 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call67.tree)


                    # AST Rewrite
                    # elements: condition_call
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
                    # 104:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:104:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:105:9: ANY condition_calls
                    pass 
                    ANY68 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition957) 
                    stream_ANY.add(ANY68)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition959)
                    condition_calls69 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls69.tree)


                    # AST Rewrite
                    # elements: condition_calls
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
                    # 106:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:106:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 3:
                    # grammar/ShyRecognizerFrontend.g:107:9: ALL condition_calls
                    pass 
                    ALL70 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition988) 
                    stream_ALL.add(ALL70)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition990)
                    condition_calls71 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls71.tree)


                    # AST Rewrite
                    # elements: condition_calls
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
                    # 108:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:108:13: ^( TREE_CONDITION_ALL condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ALL, "TREE_CONDITION_ALL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

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

    # $ANTLR end "condition"


    class condition_calls_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.condition_calls_return, self).__init__()

            self.tree = None





    # $ANTLR start "condition_calls"
    # grammar/ShyRecognizerFrontend.g:111:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE73 = None
        INDENT74 = None
        NEWLINE75 = None
        DEDENT77 = None
        NEWLINE78 = None
        condition_call72 = None

        condition_call_line76 = None


        NEWLINE73_tree = None
        INDENT74_tree = None
        NEWLINE75_tree = None
        DEDENT77_tree = None
        NEWLINE78_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:112:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == ID) :
                    alt17 = 1
                elif (LA17_0 == NEWLINE) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:112:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1028)
                    condition_call72 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call72.tree)



                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:113:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1038) 
                    stream_NEWLINE.add(NEWLINE73)


                    INDENT74 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1040) 
                    stream_INDENT.add(INDENT74)


                    NEWLINE75 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1042) 
                    stream_NEWLINE.add(NEWLINE75)


                    # grammar/ShyRecognizerFrontend.g:113:32: ( condition_call_line )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == ID) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:113:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1044)
                            condition_call_line76 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line76.tree)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    DEDENT77 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1048) 
                    stream_DEDENT.add(DEDENT77)


                    NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1050) 
                    stream_NEWLINE.add(NEWLINE78)


                    # AST Rewrite
                    # elements: condition_call_line
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
                    # 114:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:114:13: ( condition_call_line )+
                    if not (stream_condition_call_line.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_condition_call_line.hasNext():
                        self._adaptor.addChild(root_0, stream_condition_call_line.nextTree())


                    stream_condition_call_line.reset()




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

    # $ANTLR end "condition_calls"


    class condition_call_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.condition_call_return, self).__init__()

            self.tree = None





    # $ANTLR start "condition_call"
    # grammar/ShyRecognizerFrontend.g:117:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line79 = None

        statement_call_multi_line80 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:118:5: ( statement_call_single_line | statement_call_multi_line )
                alt18 = 2
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:118:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1084)
                    statement_call_single_line79 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line79.tree)



                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:119:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1094)
                    statement_call_multi_line80 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line80.tree)



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

    # $ANTLR end "condition_call"


    class condition_call_line_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.condition_call_line_return, self).__init__()

            self.tree = None





    # $ANTLR start "condition_call_line"
    # grammar/ShyRecognizerFrontend.g:122:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE82 = None
        statement_call_single_line81 = None

        statement_call_multi_line83 = None


        NEWLINE82_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:123:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt19 = 2
                alt19 = self.dfa19.predict(self.input)
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:123:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1113)
                    statement_call_single_line81 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line81.tree)


                    NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1115) 
                    stream_NEWLINE.add(NEWLINE82)


                    # AST Rewrite
                    # elements: statement_call_single_line
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
                    # 124:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt19 == 2:
                    # grammar/ShyRecognizerFrontend.g:125:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1141)
                    statement_call_multi_line83 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line83.tree)



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

    # $ANTLR end "condition_call_line"


    class statement_call_single_line_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_single_line_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_single_line"
    # grammar/ShyRecognizerFrontend.g:128:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID84 = None
        statement_call_args85 = None


        ID84_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:129:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:129:9: ID ( statement_call_args )?
                pass 
                ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1160) 
                stream_ID.add(ID84)


                # grammar/ShyRecognizerFrontend.g:129:12: ( statement_call_args )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER) :
                    alt20 = 1
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:129:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1162)
                    statement_call_args85 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args85.tree)





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
                # 130:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:130:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:130:39: ( statement_call_args )?
                if stream_statement_call_args.hasNext():
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

    # $ANTLR end "statement_call_single_line"


    class statement_call_multi_line_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_multi_line_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_multi_line"
    # grammar/ShyRecognizerFrontend.g:133:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID86 = None
        NEWLINE88 = None
        INDENT89 = None
        NEWLINE90 = None
        NEWLINE92 = None
        DEDENT93 = None
        NEWLINE94 = None
        statement_call_args87 = None

        statement_call_args91 = None


        ID86_tree = None
        NEWLINE88_tree = None
        INDENT89_tree = None
        NEWLINE90_tree = None
        NEWLINE92_tree = None
        DEDENT93_tree = None
        NEWLINE94_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:134:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:134:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID86 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1206) 
                stream_ID.add(ID86)


                # grammar/ShyRecognizerFrontend.g:134:12: ( statement_call_args )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                    alt21 = 1
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:134:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1208)
                    statement_call_args87 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args87.tree)





                NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1212) 
                stream_NEWLINE.add(NEWLINE88)


                INDENT89 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1222) 
                stream_INDENT.add(INDENT89)


                NEWLINE90 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1224) 
                stream_NEWLINE.add(NEWLINE90)


                # grammar/ShyRecognizerFrontend.g:135:24: ( statement_call_args NEWLINE )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerFrontend.g:135:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1228)
                        statement_call_args91 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args91.tree)


                        NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1230) 
                        stream_NEWLINE.add(NEWLINE92)



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1


                DEDENT93 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1236) 
                stream_DEDENT.add(DEDENT93)


                NEWLINE94 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1238) 
                stream_NEWLINE.add(NEWLINE94)


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
                # 136:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:136:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:136:39: ( statement_call_args )*
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

    # $ANTLR end "statement_call_multi_line"


    class statement_call_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_args_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_args"
    # grammar/ShyRecognizerFrontend.g:139:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg95 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:139:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:139:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:139:23: ( statement_call_arg )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerFrontend.g:139:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1274)
                        statement_call_arg95 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg95.tree)



                    else:
                        if cnt23 >= 1:
                            break #loop23

                        eee = EarlyExitException(23, self.input)
                        raise eee

                    cnt23 += 1




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


    class statement_call_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_arg_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerFrontend.g:141:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID96 = None
        EXPRESSION97 = None
        num_whole98 = None

        num_fract99 = None


        ID96_tree = None
        EXPRESSION97_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:142:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt24 = 4
                LA24 = self.input.LA(1)
                if LA24 == ID:
                    alt24 = 1
                elif LA24 == EXPRESSION:
                    alt24 = 2
                elif LA24 == MINUS:
                    LA24_3 = self.input.LA(2)

                    if (LA24_3 == NUMBER) :
                        LA24_4 = self.input.LA(3)

                        if (LA24_4 == DIVIDE) :
                            alt24 = 4
                        elif (LA24_4 == DO or (EXPRESSION <= LA24_4 <= ID) or LA24_4 == MINUS or (NEWLINE <= LA24_4 <= NUMBER)) :
                            alt24 = 3
                        else:
                            nvae = NoViableAltException("", 24, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 24, 3, self.input)

                        raise nvae


                elif LA24 == NUMBER:
                    LA24_4 = self.input.LA(2)

                    if (LA24_4 == DIVIDE) :
                        alt24 = 4
                    elif (LA24_4 == DO or (EXPRESSION <= LA24_4 <= ID) or LA24_4 == MINUS or (NEWLINE <= LA24_4 <= NUMBER)) :
                        alt24 = 3
                    else:
                        nvae = NoViableAltException("", 24, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerFrontend.g:142:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID96 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1291)
                    ID96_tree = self._adaptor.createWithPayload(ID96)
                    self._adaptor.addChild(root_0, ID96_tree)




                elif alt24 == 2:
                    # grammar/ShyRecognizerFrontend.g:143:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION97 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1301)
                    EXPRESSION97_tree = self._adaptor.createWithPayload(EXPRESSION97)
                    self._adaptor.addChild(root_0, EXPRESSION97_tree)




                elif alt24 == 3:
                    # grammar/ShyRecognizerFrontend.g:144:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1311)
                    num_whole98 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole98.tree)



                elif alt24 == 4:
                    # grammar/ShyRecognizerFrontend.g:145:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1321)
                    num_fract99 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract99.tree)



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

    # $ANTLR end "statement_call_arg"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:148:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS100 = None
        ID101 = None
        NEWLINE102 = None
        INDENT103 = None
        NEWLINE104 = None
        DEDENT106 = None
        NEWLINE107 = None
        consts_items105 = None


        CONSTS100_tree = None
        ID101_tree = None
        NEWLINE102_tree = None
        INDENT103_tree = None
        NEWLINE104_tree = None
        DEDENT106_tree = None
        NEWLINE107_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:149:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:149:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS100 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1340) 
                stream_CONSTS.add(CONSTS100)


                ID101 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1342) 
                stream_ID.add(ID101)


                NEWLINE102 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1344) 
                stream_NEWLINE.add(NEWLINE102)


                INDENT103 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1354) 
                stream_INDENT.add(INDENT103)


                NEWLINE104 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1356) 
                stream_NEWLINE.add(NEWLINE104)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1358)
                consts_items105 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items105.tree)


                DEDENT106 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1360) 
                stream_DEDENT.add(DEDENT106)


                NEWLINE107 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1362) 
                stream_NEWLINE.add(NEWLINE107)


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
                # 151:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:151:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:153:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item108 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:153:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:153:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:153:16: ( consts_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ID) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:153:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1394)
                        consts_item108 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item108.tree)



                    else:
                        if cnt25 >= 1:
                            break #loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1




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
    # grammar/ShyRecognizerFrontend.g:154:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID109 = None
        NEWLINE111 = None
        ID112 = None
        NEWLINE114 = None
        ID115 = None
        EXPRESSION116 = None
        NEWLINE117 = None
        num_whole110 = None

        num_fract113 = None


        ID109_tree = None
        NEWLINE111_tree = None
        ID112_tree = None
        NEWLINE114_tree = None
        ID115_tree = None
        EXPRESSION116_tree = None
        NEWLINE117_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:155:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt26 = 3
                LA26_0 = self.input.LA(1)

                if (LA26_0 == ID) :
                    LA26 = self.input.LA(2)
                    if LA26 == EXPRESSION:
                        alt26 = 3
                    elif LA26 == MINUS:
                        LA26_3 = self.input.LA(3)

                        if (LA26_3 == NUMBER) :
                            LA26_4 = self.input.LA(4)

                            if (LA26_4 == DIVIDE) :
                                alt26 = 2
                            elif (LA26_4 == NEWLINE) :
                                alt26 = 1
                            else:
                                nvae = NoViableAltException("", 26, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 26, 3, self.input)

                            raise nvae


                    elif LA26 == NUMBER:
                        LA26_4 = self.input.LA(3)

                        if (LA26_4 == DIVIDE) :
                            alt26 = 2
                        elif (LA26_4 == NEWLINE) :
                            alt26 = 1
                        else:
                            nvae = NoViableAltException("", 26, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 26, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:155:9: ID num_whole NEWLINE
                    pass 
                    ID109 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1410) 
                    stream_ID.add(ID109)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1412)
                    num_whole110 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole110.tree)


                    NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1414) 
                    stream_NEWLINE.add(NEWLINE111)


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
                    # 155:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:155:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt26 == 2:
                    # grammar/ShyRecognizerFrontend.g:156:9: ID num_fract NEWLINE
                    pass 
                    ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1436) 
                    stream_ID.add(ID112)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1438)
                    num_fract113 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract113.tree)


                    NEWLINE114 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1440) 
                    stream_NEWLINE.add(NEWLINE114)


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
                    # 156:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:156:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt26 == 3:
                    # grammar/ShyRecognizerFrontend.g:157:9: ID EXPRESSION NEWLINE
                    pass 
                    ID115 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1462) 
                    stream_ID.add(ID115)


                    EXPRESSION116 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1464) 
                    stream_EXPRESSION.add(EXPRESSION116)


                    NEWLINE117 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1466) 
                    stream_NEWLINE.add(NEWLINE117)


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
                    # 157:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:157:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:160:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES118 = None
        ID119 = None
        NEWLINE120 = None
        INDENT121 = None
        NEWLINE122 = None
        DEDENT124 = None
        NEWLINE125 = None
        types_items123 = None


        TYPES118_tree = None
        ID119_tree = None
        NEWLINE120_tree = None
        INDENT121_tree = None
        NEWLINE122_tree = None
        DEDENT124_tree = None
        NEWLINE125_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:161:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:161:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES118 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1497) 
                stream_TYPES.add(TYPES118)


                ID119 = self.match(self.input, ID, self.FOLLOW_ID_in_types1499) 
                stream_ID.add(ID119)


                NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1501) 
                stream_NEWLINE.add(NEWLINE120)


                INDENT121 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1511) 
                stream_INDENT.add(INDENT121)


                NEWLINE122 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1513) 
                stream_NEWLINE.add(NEWLINE122)


                self._state.following.append(self.FOLLOW_types_items_in_types1515)
                types_items123 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items123.tree)


                DEDENT124 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1517) 
                stream_DEDENT.add(DEDENT124)


                NEWLINE125 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1519) 
                stream_NEWLINE.add(NEWLINE125)


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
                # 163:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:163:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:165:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item126 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:165:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:165:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:165:15: ( types_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == ID) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerFrontend.g:165:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1551)
                        types_item126 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item126.tree)



                    else:
                        if cnt27 >= 1:
                            break #loop27

                        eee = EarlyExitException(27, self.input)
                        raise eee

                    cnt27 += 1




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
    # grammar/ShyRecognizerFrontend.g:166:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID127 = None
        vars_hint128 = None


        ID127_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:166:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:166:14: ID vars_hint
                pass 
                ID127 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1561) 
                stream_ID.add(ID127)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1563)
                vars_hint128 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint128.tree)


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
                # 166:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:166:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:168:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE130 = None
        INDENT131 = None
        NEWLINE132 = None
        NEWLINE134 = None
        DEDENT135 = None
        NEWLINE136 = None
        var_hint129 = None

        var_hint133 = None


        NEWLINE130_tree = None
        INDENT131_tree = None
        NEWLINE132_tree = None
        NEWLINE134_tree = None
        DEDENT135_tree = None
        NEWLINE136_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:169:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:169:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:169:9: ( var_hint )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == CURLY_OPEN or LA28_0 == ID) :
                    alt28 = 1
                if alt28 == 1:
                    # grammar/ShyRecognizerFrontend.g:169:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1590)
                    var_hint129 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint129.tree)





                NEWLINE130 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1594) 
                stream_NEWLINE.add(NEWLINE130)


                # grammar/ShyRecognizerFrontend.g:170:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == INDENT) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:170:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT131 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1606) 
                    stream_INDENT.add(INDENT131)


                    NEWLINE132 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1608) 
                    stream_NEWLINE.add(NEWLINE132)


                    # grammar/ShyRecognizerFrontend.g:170:26: ( var_hint NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == CURLY_OPEN or LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:170:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1612)
                            var_hint133 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint133.tree)


                            NEWLINE134 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1614) 
                            stream_NEWLINE.add(NEWLINE134)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT135 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1620) 
                    stream_DEDENT.add(DEDENT135)


                    NEWLINE136 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1622) 
                    stream_NEWLINE.add(NEWLINE136)





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
                # 171:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:171:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:173:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE141 = None
        INDENT142 = None
        NEWLINE143 = None
        NEWLINE145 = None
        DEDENT146 = None
        var137 = None

        hint138 = None

        var139 = None

        hint140 = None

        var144 = None


        NEWLINE141_tree = None
        INDENT142_tree = None
        NEWLINE143_tree = None
        NEWLINE145_tree = None
        DEDENT146_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt35 = 3
                alt35 = self.dfa35.predict(self.input)
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:174:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:174:9: ( var )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == ID) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:174:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1661)
                            var137 = self.var()

                            self._state.following.pop()
                            stream_var.add(var137.tree)



                        else:
                            if cnt31 >= 1:
                                break #loop31

                            eee = EarlyExitException(31, self.input)
                            raise eee

                        cnt31 += 1


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
                    # 175:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:175:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:175:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:176:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1696)
                    hint138 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint138.tree)


                    # grammar/ShyRecognizerFrontend.g:176:14: ( var )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:176:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1698)
                            var139 = self.var()

                            self._state.following.pop()
                            stream_var.add(var139.tree)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


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
                    # 177:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:177:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:177:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 3:
                    # grammar/ShyRecognizerFrontend.g:178:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1732)
                    hint140 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint140.tree)


                    NEWLINE141 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1734) 
                    stream_NEWLINE.add(NEWLINE141)


                    INDENT142 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1736) 
                    stream_INDENT.add(INDENT142)


                    NEWLINE143 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1738) 
                    stream_NEWLINE.add(NEWLINE143)


                    # grammar/ShyRecognizerFrontend.g:178:37: ( ( var )+ NEWLINE )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == ID) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerFrontend.g:178:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:178:39: ( var )+
                            cnt33 = 0
                            while True: #loop33
                                alt33 = 2
                                LA33_0 = self.input.LA(1)

                                if (LA33_0 == ID) :
                                    alt33 = 1


                                if alt33 == 1:
                                    # grammar/ShyRecognizerFrontend.g:178:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1742)
                                    var144 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var144.tree)



                                else:
                                    if cnt33 >= 1:
                                        break #loop33

                                    eee = EarlyExitException(33, self.input)
                                    raise eee

                                cnt33 += 1


                            NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1746) 
                            stream_NEWLINE.add(NEWLINE145)



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


                    DEDENT146 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1752) 
                    stream_DEDENT.add(DEDENT146)


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
                    # 179:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:179:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:179:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:181:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID147 = None

        ID147_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:181:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:181:7: ID
                pass 
                ID147 = self.match(self.input, ID, self.FOLLOW_ID_in_var1786) 
                stream_ID.add(ID147)


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
                # 181:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:181:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:183:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN148 = None
        ID149 = None
        CURLY_CLOSE150 = None
        CURLY_OPEN151 = None
        ID152 = None
        CURLY_CLOSE154 = None
        hint_arg153 = None


        CURLY_OPEN148_tree = None
        ID149_tree = None
        CURLY_CLOSE150_tree = None
        CURLY_OPEN151_tree = None
        ID152_tree = None
        CURLY_CLOSE154_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:184:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == CURLY_OPEN) :
                    LA37_1 = self.input.LA(2)

                    if (LA37_1 == ID) :
                        LA37_2 = self.input.LA(3)

                        if (LA37_2 == CURLY_CLOSE) :
                            alt37 = 1
                        elif (LA37_2 == ID or LA37_2 == UNDERSCORE) :
                            alt37 = 2
                        else:
                            nvae = NoViableAltException("", 37, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 37, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:184:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN148 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1811) 
                    stream_CURLY_OPEN.add(CURLY_OPEN148)


                    ID149 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1813) 
                    stream_ID.add(ID149)


                    CURLY_CLOSE150 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1815) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE150)


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
                    # 184:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:184:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt37 == 2:
                    # grammar/ShyRecognizerFrontend.g:185:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN151 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1835) 
                    stream_CURLY_OPEN.add(CURLY_OPEN151)


                    ID152 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1837) 
                    stream_ID.add(ID152)


                    # grammar/ShyRecognizerFrontend.g:185:23: ( hint_arg )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID or LA36_0 == UNDERSCORE) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:185:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1839)
                            hint_arg153 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg153.tree)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


                    CURLY_CLOSE154 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1843) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE154)


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
                    # 185:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:185:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:185:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:187:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set155 = None

        set155_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:187:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set155 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set155))

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
    # grammar/ShyRecognizerFrontend.g:189:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS156 = None
        NUMBER157 = None

        MINUS156_tree = None
        NUMBER157_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:189:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:189:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:189:13: ( MINUS )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == MINUS) :
                    alt38 = 1
                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:189:13: MINUS
                    pass 
                    MINUS156 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1882)
                    MINUS156_tree = self._adaptor.createWithPayload(MINUS156)
                    self._adaptor.addChild(root_0, MINUS156_tree)






                NUMBER157 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1886)
                NUMBER157_tree = self._adaptor.createWithPayload(NUMBER157)
                self._adaptor.addChild(root_0, NUMBER157_tree)





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
    # grammar/ShyRecognizerFrontend.g:190:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS158 = None
        NUMBER159 = None
        DIVIDE160 = None
        NUMBER161 = None

        MINUS158_tree = None
        NUMBER159_tree = None
        DIVIDE160_tree = None
        NUMBER161_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:190:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:190:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:190:13: ( MINUS )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == MINUS) :
                    alt39 = 1
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:190:13: MINUS
                    pass 
                    MINUS158 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1894)
                    MINUS158_tree = self._adaptor.createWithPayload(MINUS158)
                    self._adaptor.addChild(root_0, MINUS158_tree)






                NUMBER159 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1898)
                NUMBER159_tree = self._adaptor.createWithPayload(NUMBER159)
                self._adaptor.addChild(root_0, NUMBER159_tree)



                DIVIDE160 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1900)
                DIVIDE160_tree = self._adaptor.createWithPayload(DIVIDE160)
                self._adaptor.addChild(root_0, DIVIDE160_tree)



                NUMBER161 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1902)
                NUMBER161_tree = self._adaptor.createWithPayload(NUMBER161)
                self._adaptor.addChild(root_0, NUMBER161_tree)





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



    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\23\1\22\1\uffff\2\22\1\31\1\16\1\15\1\31\2\uffff\1\22"
        )

    DFA9_max = DFA.unpack(
        u"\1\24\1\31\1\uffff\4\31\1\25\1\31\2\uffff\1\31"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\3\6\uffff\1\2\1\1\1\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA9_transition = [
        DFA.unpack(u"\1\1\1\2"),
        DFA.unpack(u"\1\4\1\3\2\uffff\1\5\1\uffff\1\7\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\3\2\uffff\1\5\1\uffff\1\7\1\6"),
        DFA.unpack(u"\1\4\1\3\2\uffff\1\5\1\uffff\1\7\1\6"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\10\3\uffff\1\4\1\3\2\uffff\1\5\1\uffff\1\7\1\6"),
        DFA.unpack(u"\1\12\5\uffff\2\12\1\11"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\3\2\uffff\1\5\1\uffff\1\7\1\6")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\23\3\17\1\31\1\16\1\17\1\uffff\1\31\1\uffff\1\17"
        )

    DFA18_max = DFA.unpack(
        u"\1\23\5\31\1\25\1\uffff\1\31\1\uffff\1\31"
        )

    DFA18_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA18_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA18_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\10\1\7\2\uffff\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1"
        u"\5"),
        DFA.unpack(u"\1\7\5\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #19

    DFA19_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA19_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA19_min = DFA.unpack(
        u"\1\23\3\22\1\31\1\16\1\15\1\31\2\uffff\1\22"
        )

    DFA19_max = DFA.unpack(
        u"\1\23\5\31\1\25\1\31\2\uffff\1\31"
        )

    DFA19_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA19_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA19_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\7\3\uffff\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\11\5\uffff\1\11\1\uffff\1\10"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\2\2\uffff\1\4\1\uffff\1\6\1\5")
    ]

    # class definition for DFA #19

    class DFA19(DFA):
        pass


    # lookup tables for DFA #35

    DFA35_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA35_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA35_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA35_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\76\1\30\1\76\2\uffff\1\30"
        )

    DFA35_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA35_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA35_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\7\uffff\1\5\52\uffff\1\5"),
        DFA.unpack(u"\1\6\4\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\52\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\4\uffff\1\7")
    ]

    # class definition for DFA #35

    class DFA35(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 23, 30, 61])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 23, 30, 61])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 23, 30, 61])
    FOLLOW_types_in_start94 = frozenset([1, 9, 23, 30, 61])
    FOLLOW_MODULE_in_module113 = frozenset([19])
    FOLLOW_ID_in_module115 = frozenset([24])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([19])
    FOLLOW_ID_in_stateless148 = frozenset([24])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless154 = frozenset([24])
    FOLLOW_NEWLINE_in_stateless156 = frozenset([28])
    FOLLOW_proc_in_stateless158 = frozenset([13, 28])
    FOLLOW_DEDENT_in_stateless162 = frozenset([24])
    FOLLOW_NEWLINE_in_stateless164 = frozenset([1])
    FOLLOW_PROC_in_proc209 = frozenset([19])
    FOLLOW_ID_in_proc211 = frozenset([24])
    FOLLOW_NEWLINE_in_proc213 = frozenset([1])
    FOLLOW_PROC_in_proc241 = frozenset([19])
    FOLLOW_ID_in_proc243 = frozenset([24])
    FOLLOW_NEWLINE_in_proc245 = frozenset([21])
    FOLLOW_INDENT_in_proc247 = frozenset([24])
    FOLLOW_NEWLINE_in_proc249 = frozenset([6, 13, 26, 63])
    FOLLOW_proc_args_in_proc263 = frozenset([13, 26, 63])
    FOLLOW_proc_vars_in_proc267 = frozenset([13, 26])
    FOLLOW_proc_ops_in_proc271 = frozenset([13])
    FOLLOW_DEDENT_in_proc283 = frozenset([24])
    FOLLOW_NEWLINE_in_proc285 = frozenset([1])
    FOLLOW_ARGS_in_proc_args334 = frozenset([12, 19, 24])
    FOLLOW_vars_hint_in_proc_args336 = frozenset([1])
    FOLLOW_VARS_in_proc_vars365 = frozenset([12, 19, 24])
    FOLLOW_vars_hint_in_proc_vars367 = frozenset([1])
    FOLLOW_OPS_in_proc_ops396 = frozenset([24])
    FOLLOW_NEWLINE_in_proc_ops398 = frozenset([21])
    FOLLOW_INDENT_in_proc_ops400 = frozenset([24])
    FOLLOW_NEWLINE_in_proc_ops402 = frozenset([19, 20])
    FOLLOW_statement_in_proc_ops404 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_proc_ops408 = frozenset([24])
    FOLLOW_NEWLINE_in_proc_ops410 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement449 = frozenset([24])
    FOLLOW_NEWLINE_in_statement451 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement477 = frozenset([1])
    FOLLOW_statement_if_in_statement487 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if506 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if516 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if528 = frozenset([1])
    FOLLOW_IF_in_statement_if_head636 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head638 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif670 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif672 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body704 = frozenset([15, 24])
    FOLLOW_NEWLINE_in_statement_elif_body706 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body710 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif_body712 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body726 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif_body728 = frozenset([19, 20])
    FOLLOW_statement_in_statement_elif_body730 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_elif_body734 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif_body736 = frozenset([1])
    FOLLOW_ELSE_in_statement_else828 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else830 = frozenset([21])
    FOLLOW_INDENT_in_statement_else844 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else846 = frozenset([19, 20])
    FOLLOW_statement_in_statement_else848 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_else852 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else854 = frozenset([1])
    FOLLOW_condition_call_in_condition928 = frozenset([1])
    FOLLOW_ANY_in_condition957 = frozenset([19, 24])
    FOLLOW_condition_calls_in_condition959 = frozenset([1])
    FOLLOW_ALL_in_condition988 = frozenset([19, 24])
    FOLLOW_condition_calls_in_condition990 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1028 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1038 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1040 = frozenset([24])
    FOLLOW_NEWLINE_in_condition_calls1042 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1044 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1048 = frozenset([24])
    FOLLOW_NEWLINE_in_condition_calls1050 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1084 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1094 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1113 = frozenset([24])
    FOLLOW_NEWLINE_in_condition_call_line1115 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1141 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1160 = frozenset([1, 18, 19, 22, 25])
    FOLLOW_statement_call_args_in_statement_call_single_line1162 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1206 = frozenset([18, 19, 22, 24, 25])
    FOLLOW_statement_call_args_in_statement_call_multi_line1208 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1212 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1222 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1224 = frozenset([18, 19, 22, 25])
    FOLLOW_statement_call_args_in_statement_call_multi_line1228 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1230 = frozenset([13, 18, 19, 22, 25])
    FOLLOW_DEDENT_in_statement_call_multi_line1236 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1238 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args1274 = frozenset([1, 18, 19, 22, 25])
    FOLLOW_ID_in_statement_call_arg1291 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1301 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1311 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1321 = frozenset([1])
    FOLLOW_CONSTS_in_consts1340 = frozenset([19])
    FOLLOW_ID_in_consts1342 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1344 = frozenset([21])
    FOLLOW_INDENT_in_consts1354 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1356 = frozenset([19])
    FOLLOW_consts_items_in_consts1358 = frozenset([13])
    FOLLOW_DEDENT_in_consts1360 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1362 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1394 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1410 = frozenset([22, 25])
    FOLLOW_num_whole_in_consts_item1412 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1414 = frozenset([1])
    FOLLOW_ID_in_consts_item1436 = frozenset([22, 25])
    FOLLOW_num_fract_in_consts_item1438 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1440 = frozenset([1])
    FOLLOW_ID_in_consts_item1462 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1464 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1466 = frozenset([1])
    FOLLOW_TYPES_in_types1497 = frozenset([19])
    FOLLOW_ID_in_types1499 = frozenset([24])
    FOLLOW_NEWLINE_in_types1501 = frozenset([21])
    FOLLOW_INDENT_in_types1511 = frozenset([24])
    FOLLOW_NEWLINE_in_types1513 = frozenset([19])
    FOLLOW_types_items_in_types1515 = frozenset([13])
    FOLLOW_DEDENT_in_types1517 = frozenset([24])
    FOLLOW_NEWLINE_in_types1519 = frozenset([1])
    FOLLOW_types_item_in_types_items1551 = frozenset([1, 19])
    FOLLOW_ID_in_types_item1561 = frozenset([12, 19, 24])
    FOLLOW_vars_hint_in_types_item1563 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1590 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1594 = frozenset([1, 21])
    FOLLOW_INDENT_in_vars_hint1606 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1608 = frozenset([12, 19])
    FOLLOW_var_hint_in_vars_hint1612 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1614 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_vars_hint1620 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1622 = frozenset([1])
    FOLLOW_var_in_var_hint1661 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1696 = frozenset([19])
    FOLLOW_var_in_var_hint1698 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1732 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1734 = frozenset([21])
    FOLLOW_INDENT_in_var_hint1736 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1738 = frozenset([19])
    FOLLOW_var_in_var_hint1742 = frozenset([19, 24])
    FOLLOW_NEWLINE_in_var_hint1746 = frozenset([13, 19])
    FOLLOW_DEDENT_in_var_hint1752 = frozenset([1])
    FOLLOW_ID_in_var1786 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1811 = frozenset([19])
    FOLLOW_ID_in_hint1813 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint1815 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1835 = frozenset([19])
    FOLLOW_ID_in_hint1837 = frozenset([19, 62])
    FOLLOW_hint_arg_in_hint1839 = frozenset([11, 19, 62])
    FOLLOW_CURLY_CLOSE_in_hint1843 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1882 = frozenset([25])
    FOLLOW_NUMBER_in_num_whole1886 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1894 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1898 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract1900 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1902 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
