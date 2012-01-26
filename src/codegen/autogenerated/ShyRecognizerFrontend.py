# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-26 18:24:43

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
TREE_STATEMENT_CALL_ARGS=53
TREE_STATEMENT_ELIF=54
TREE_STATEMENT_ELSE=55
TREE_STATEMENT_IF=56
TREE_TYPES=57
TREE_TYPES_ITEM=58
TREE_VAR=59
TREE_VARS_HINT=60
TREE_VAR_HINT=61
TYPES=62
UNDERSCORE=63
VARS=64
WHITESPACE=65
WITH=66

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
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_VAR", "TREE_VARS_HINT", "TREE_VAR_HINT", "TYPES", 
    "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

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
                    # elements: proc_ops, proc_args, proc_vars, ID
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
    # grammar/ShyRecognizerFrontend.g:57:1: statement : ( statement_call | statement_if );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call40 = None

        statement_if41 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:58:5: ( statement_call | statement_if )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == ID) :
                    alt9 = 1
                elif (LA9_0 == IF) :
                    alt9 = 2
                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:58:9: statement_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_in_statement449)
                    statement_call40 = self.statement_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call40.tree)



                elif alt9 == 2:
                    # grammar/ShyRecognizerFrontend.g:59:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement459)
                    statement_if41 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if41.tree)



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
    # grammar/ShyRecognizerFrontend.g:62:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head42 = None

        statement_elif43 = None

        statement_else44 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:63:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:63:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if478)
                statement_if_head42 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head42.tree)


                # grammar/ShyRecognizerFrontend.g:64:9: ( statement_elif )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ELIF) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:64:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if488)
                        statement_elif43 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif43.tree)



                    else:
                        break #loop10


                # grammar/ShyRecognizerFrontend.g:65:9: ( statement_else )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == ELSE) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerFrontend.g:65:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if500)
                    statement_else44 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else44.tree)





                # AST Rewrite
                # elements: statement_if_head, statement_elif, statement_else
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
                # 66:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:66:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:68:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:69:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:73:1: statement_if_head : IF condition INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF45 = None
        INDENT47 = None
        NEWLINE48 = None
        DEDENT50 = None
        NEWLINE51 = None
        condition46 = None

        statement49 = None


        IF45_tree = None
        INDENT47_tree = None
        NEWLINE48_tree = None
        DEDENT50_tree = None
        NEWLINE51_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:74:5: ( IF condition INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:74:9: IF condition INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                IF45 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head608) 
                stream_IF.add(IF45)


                self._state.following.append(self.FOLLOW_condition_in_statement_if_head610)
                condition46 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition46.tree)


                INDENT47 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_if_head624) 
                stream_INDENT.add(INDENT47)


                NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head626) 
                stream_NEWLINE.add(NEWLINE48)


                # grammar/ShyRecognizerFrontend.g:75:28: ( statement )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((ID <= LA12_0 <= IF)) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:75:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_if_head628)
                        statement49 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement49.tree)



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1


                DEDENT50 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_if_head632) 
                stream_DEDENT.add(DEDENT50)


                NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head634) 
                stream_NEWLINE.add(NEWLINE51)


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
                # 76:9: -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:76:13: ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                self._adaptor.addChild(root_1, stream_condition.nextTree())

                # grammar/ShyRecognizerFrontend.g:78:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:78:36: ( statement )+
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

    # $ANTLR end "statement_if_head"


    class statement_elif_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_elif_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_elif"
    # grammar/ShyRecognizerFrontend.g:82:1: statement_elif : ELIF condition INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF52 = None
        INDENT54 = None
        NEWLINE55 = None
        DEDENT57 = None
        NEWLINE58 = None
        condition53 = None

        statement56 = None


        ELIF52_tree = None
        INDENT54_tree = None
        NEWLINE55_tree = None
        DEDENT57_tree = None
        NEWLINE58_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:5: ( ELIF condition INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:83:9: ELIF condition INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELIF52 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif726) 
                stream_ELIF.add(ELIF52)


                self._state.following.append(self.FOLLOW_condition_in_statement_elif728)
                condition53 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition53.tree)


                INDENT54 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif742) 
                stream_INDENT.add(INDENT54)


                NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif744) 
                stream_NEWLINE.add(NEWLINE55)


                # grammar/ShyRecognizerFrontend.g:84:28: ( statement )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((ID <= LA13_0 <= IF)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:84:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_elif746)
                        statement56 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement56.tree)



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                DEDENT57 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif750) 
                stream_DEDENT.add(DEDENT57)


                NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif752) 
                stream_NEWLINE.add(NEWLINE58)


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
                # 85:9: -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:85:13: ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                self._adaptor.addChild(root_1, stream_condition.nextTree())

                # grammar/ShyRecognizerFrontend.g:87:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:87:36: ( statement )+
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

    # $ANTLR end "statement_elif"


    class condition_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.condition_return, self).__init__()

            self.tree = None





    # $ANTLR start "condition"
    # grammar/ShyRecognizerFrontend.g:91:1: condition : ( statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ANY statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ALL statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ALL statement_call ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DO60 = None
        NEWLINE61 = None
        ANY62 = None
        DO64 = None
        NEWLINE65 = None
        ALL66 = None
        DO68 = None
        NEWLINE69 = None
        statement_call59 = None

        statement_call63 = None

        statement_call67 = None


        DO60_tree = None
        NEWLINE61_tree = None
        ANY62_tree = None
        DO64_tree = None
        NEWLINE65_tree = None
        ALL66_tree = None
        DO68_tree = None
        NEWLINE69_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_statement_call = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:92:5: ( statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ANY statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ALL statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ALL statement_call ) )
                alt17 = 3
                LA17 = self.input.LA(1)
                if LA17 == ID:
                    alt17 = 1
                elif LA17 == ANY:
                    alt17 = 2
                elif LA17 == ALL:
                    alt17 = 3
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:92:9: statement_call ( DO )? NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_in_condition844)
                    statement_call59 = self.statement_call()

                    self._state.following.pop()
                    stream_statement_call.add(statement_call59.tree)


                    # grammar/ShyRecognizerFrontend.g:92:24: ( DO )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == DO) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:92:24: DO
                        pass 
                        DO60 = self.match(self.input, DO, self.FOLLOW_DO_in_condition846) 
                        stream_DO.add(DO60)





                    NEWLINE61 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition850) 
                    stream_NEWLINE.add(NEWLINE61)


                    # AST Rewrite
                    # elements: statement_call
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
                    # 93:9: -> ^( TREE_CONDITION_ANY statement_call )
                    # grammar/ShyRecognizerFrontend.g:93:13: ^( TREE_CONDITION_ANY statement_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_statement_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:94:9: ANY statement_call ( DO )? NEWLINE
                    pass 
                    ANY62 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition879) 
                    stream_ANY.add(ANY62)


                    self._state.following.append(self.FOLLOW_statement_call_in_condition881)
                    statement_call63 = self.statement_call()

                    self._state.following.pop()
                    stream_statement_call.add(statement_call63.tree)


                    # grammar/ShyRecognizerFrontend.g:94:28: ( DO )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == DO) :
                        alt15 = 1
                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:94:28: DO
                        pass 
                        DO64 = self.match(self.input, DO, self.FOLLOW_DO_in_condition883) 
                        stream_DO.add(DO64)





                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition887) 
                    stream_NEWLINE.add(NEWLINE65)


                    # AST Rewrite
                    # elements: statement_call
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
                    # 95:9: -> ^( TREE_CONDITION_ANY statement_call )
                    # grammar/ShyRecognizerFrontend.g:95:13: ^( TREE_CONDITION_ANY statement_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_statement_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 3:
                    # grammar/ShyRecognizerFrontend.g:96:9: ALL statement_call ( DO )? NEWLINE
                    pass 
                    ALL66 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition916) 
                    stream_ALL.add(ALL66)


                    self._state.following.append(self.FOLLOW_statement_call_in_condition918)
                    statement_call67 = self.statement_call()

                    self._state.following.pop()
                    stream_statement_call.add(statement_call67.tree)


                    # grammar/ShyRecognizerFrontend.g:96:28: ( DO )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == DO) :
                        alt16 = 1
                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:96:28: DO
                        pass 
                        DO68 = self.match(self.input, DO, self.FOLLOW_DO_in_condition920) 
                        stream_DO.add(DO68)





                    NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition924) 
                    stream_NEWLINE.add(NEWLINE69)


                    # AST Rewrite
                    # elements: statement_call
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
                    # 97:9: -> ^( TREE_CONDITION_ALL statement_call )
                    # grammar/ShyRecognizerFrontend.g:97:13: ^( TREE_CONDITION_ALL statement_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ALL, "TREE_CONDITION_ALL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_statement_call.nextTree())

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


    class statement_else_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_else_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerFrontend.g:100:1: statement_else : ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE70 = None
        NEWLINE71 = None
        INDENT72 = None
        NEWLINE73 = None
        DEDENT75 = None
        NEWLINE76 = None
        statement74 = None


        ELSE70_tree = None
        NEWLINE71_tree = None
        INDENT72_tree = None
        NEWLINE73_tree = None
        DEDENT75_tree = None
        NEWLINE76_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:101:5: ( ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:101:9: ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELSE70 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else962) 
                stream_ELSE.add(ELSE70)


                NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else964) 
                stream_NEWLINE.add(NEWLINE71)


                INDENT72 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else978) 
                stream_INDENT.add(INDENT72)


                NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else980) 
                stream_NEWLINE.add(NEWLINE73)


                # grammar/ShyRecognizerFrontend.g:102:28: ( statement )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if ((ID <= LA18_0 <= IF)) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerFrontend.g:102:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_else982)
                        statement74 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement74.tree)



                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1


                DEDENT75 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else986) 
                stream_DEDENT.add(DEDENT75)


                NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else988) 
                stream_NEWLINE.add(NEWLINE76)


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
                # 103:9: -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:103:13: ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:104:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:104:36: ( statement )+
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


    class statement_call_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerFrontend.g:108:1: statement_call : ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID77 = None
        DO79 = None
        NEWLINE80 = None
        INDENT81 = None
        NEWLINE82 = None
        NEWLINE84 = None
        DEDENT85 = None
        NEWLINE86 = None
        statement_call_args78 = None

        statement_call_args83 = None


        ID77_tree = None
        DO79_tree = None
        NEWLINE80_tree = None
        INDENT81_tree = None
        NEWLINE82_tree = None
        NEWLINE84_tree = None
        DEDENT85_tree = None
        NEWLINE86_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:109:5: ( ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:109:9: ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID77 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call1062) 
                stream_ID.add(ID77)


                # grammar/ShyRecognizerFrontend.g:109:12: ( statement_call_args )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:109:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1064)
                    statement_call_args78 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args78.tree)





                # grammar/ShyRecognizerFrontend.g:109:34: ( DO | NEWLINE )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == DO) :
                    alt20 = 1
                elif (LA20_0 == NEWLINE) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:109:36: DO
                    pass 
                    DO79 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_call1070) 
                    stream_DO.add(DO79)



                elif alt20 == 2:
                    # grammar/ShyRecognizerFrontend.g:109:41: NEWLINE
                    pass 
                    NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1074) 
                    stream_NEWLINE.add(NEWLINE80)





                # grammar/ShyRecognizerFrontend.g:110:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == INDENT) :
                    alt22 = 1
                if alt22 == 1:
                    # grammar/ShyRecognizerFrontend.g:110:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT81 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call1088) 
                    stream_INDENT.add(INDENT81)


                    NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1090) 
                    stream_NEWLINE.add(NEWLINE82)


                    # grammar/ShyRecognizerFrontend.g:110:26: ( statement_call_args NEWLINE )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:110:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1094)
                            statement_call_args83 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args83.tree)


                            NEWLINE84 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1096) 
                            stream_NEWLINE.add(NEWLINE84)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    DEDENT85 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call1102) 
                    stream_DEDENT.add(DEDENT85)


                    NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1104) 
                    stream_NEWLINE.add(NEWLINE86)





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
                # 111:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:111:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:112:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:115:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg87 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:115:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:115:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:115:23: ( statement_call_arg )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerFrontend.g:115:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1162)
                        statement_call_arg87 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg87.tree)



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
    # grammar/ShyRecognizerFrontend.g:117:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID88 = None
        EXPRESSION89 = None
        num_whole90 = None

        num_fract91 = None


        ID88_tree = None
        EXPRESSION89_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:118:5: ( ID | EXPRESSION | num_whole | num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:118:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID88 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1179)
                    ID88_tree = self._adaptor.createWithPayload(ID88)
                    self._adaptor.addChild(root_0, ID88_tree)




                elif alt24 == 2:
                    # grammar/ShyRecognizerFrontend.g:119:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION89 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1189)
                    EXPRESSION89_tree = self._adaptor.createWithPayload(EXPRESSION89)
                    self._adaptor.addChild(root_0, EXPRESSION89_tree)




                elif alt24 == 3:
                    # grammar/ShyRecognizerFrontend.g:120:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1199)
                    num_whole90 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole90.tree)



                elif alt24 == 4:
                    # grammar/ShyRecognizerFrontend.g:121:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1209)
                    num_fract91 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract91.tree)



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
    # grammar/ShyRecognizerFrontend.g:124:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS92 = None
        ID93 = None
        NEWLINE94 = None
        INDENT95 = None
        NEWLINE96 = None
        DEDENT98 = None
        NEWLINE99 = None
        consts_items97 = None


        CONSTS92_tree = None
        ID93_tree = None
        NEWLINE94_tree = None
        INDENT95_tree = None
        NEWLINE96_tree = None
        DEDENT98_tree = None
        NEWLINE99_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:125:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:125:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS92 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1228) 
                stream_CONSTS.add(CONSTS92)


                ID93 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1230) 
                stream_ID.add(ID93)


                NEWLINE94 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1232) 
                stream_NEWLINE.add(NEWLINE94)


                INDENT95 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1242) 
                stream_INDENT.add(INDENT95)


                NEWLINE96 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1244) 
                stream_NEWLINE.add(NEWLINE96)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1246)
                consts_items97 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items97.tree)


                DEDENT98 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1248) 
                stream_DEDENT.add(DEDENT98)


                NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1250) 
                stream_NEWLINE.add(NEWLINE99)


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
                # 127:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:127:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:129:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item100 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:129:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:129:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:129:16: ( consts_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ID) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:129:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1282)
                        consts_item100 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item100.tree)



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
    # grammar/ShyRecognizerFrontend.g:130:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID101 = None
        NEWLINE103 = None
        ID104 = None
        NEWLINE106 = None
        ID107 = None
        EXPRESSION108 = None
        NEWLINE109 = None
        num_whole102 = None

        num_fract105 = None


        ID101_tree = None
        NEWLINE103_tree = None
        ID104_tree = None
        NEWLINE106_tree = None
        ID107_tree = None
        EXPRESSION108_tree = None
        NEWLINE109_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:131:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerFrontend.g:131:9: ID num_whole NEWLINE
                    pass 
                    ID101 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1298) 
                    stream_ID.add(ID101)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1300)
                    num_whole102 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole102.tree)


                    NEWLINE103 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1302) 
                    stream_NEWLINE.add(NEWLINE103)


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
                    # 131:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:131:33: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/ShyRecognizerFrontend.g:132:9: ID num_fract NEWLINE
                    pass 
                    ID104 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1324) 
                    stream_ID.add(ID104)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1326)
                    num_fract105 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract105.tree)


                    NEWLINE106 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1328) 
                    stream_NEWLINE.add(NEWLINE106)


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
                    # 132:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:132:33: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:133:9: ID EXPRESSION NEWLINE
                    pass 
                    ID107 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1350) 
                    stream_ID.add(ID107)


                    EXPRESSION108 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1352) 
                    stream_EXPRESSION.add(EXPRESSION108)


                    NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1354) 
                    stream_NEWLINE.add(NEWLINE109)


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
                    # 133:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:133:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:136:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES110 = None
        ID111 = None
        NEWLINE112 = None
        INDENT113 = None
        NEWLINE114 = None
        DEDENT116 = None
        NEWLINE117 = None
        types_items115 = None


        TYPES110_tree = None
        ID111_tree = None
        NEWLINE112_tree = None
        INDENT113_tree = None
        NEWLINE114_tree = None
        DEDENT116_tree = None
        NEWLINE117_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:137:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:137:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES110 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1385) 
                stream_TYPES.add(TYPES110)


                ID111 = self.match(self.input, ID, self.FOLLOW_ID_in_types1387) 
                stream_ID.add(ID111)


                NEWLINE112 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1389) 
                stream_NEWLINE.add(NEWLINE112)


                INDENT113 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1399) 
                stream_INDENT.add(INDENT113)


                NEWLINE114 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1401) 
                stream_NEWLINE.add(NEWLINE114)


                self._state.following.append(self.FOLLOW_types_items_in_types1403)
                types_items115 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items115.tree)


                DEDENT116 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1405) 
                stream_DEDENT.add(DEDENT116)


                NEWLINE117 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1407) 
                stream_NEWLINE.add(NEWLINE117)


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
                # 139:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:139:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:141:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item118 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:141:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:141:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:141:15: ( types_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == ID) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerFrontend.g:141:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1439)
                        types_item118 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item118.tree)



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
    # grammar/ShyRecognizerFrontend.g:142:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID119 = None
        vars_hint120 = None


        ID119_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:142:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:142:14: ID vars_hint
                pass 
                ID119 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1449) 
                stream_ID.add(ID119)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1451)
                vars_hint120 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint120.tree)


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
                # 142:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:142:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:144:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE122 = None
        INDENT123 = None
        NEWLINE124 = None
        NEWLINE126 = None
        DEDENT127 = None
        NEWLINE128 = None
        var_hint121 = None

        var_hint125 = None


        NEWLINE122_tree = None
        INDENT123_tree = None
        NEWLINE124_tree = None
        NEWLINE126_tree = None
        DEDENT127_tree = None
        NEWLINE128_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:145:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:145:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:145:9: ( var_hint )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == CURLY_OPEN or LA28_0 == ID) :
                    alt28 = 1
                if alt28 == 1:
                    # grammar/ShyRecognizerFrontend.g:145:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1478)
                    var_hint121 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint121.tree)





                NEWLINE122 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1482) 
                stream_NEWLINE.add(NEWLINE122)


                # grammar/ShyRecognizerFrontend.g:146:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == INDENT) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:146:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT123 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1494) 
                    stream_INDENT.add(INDENT123)


                    NEWLINE124 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1496) 
                    stream_NEWLINE.add(NEWLINE124)


                    # grammar/ShyRecognizerFrontend.g:146:26: ( var_hint NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == CURLY_OPEN or LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:146:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1500)
                            var_hint125 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint125.tree)


                            NEWLINE126 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1502) 
                            stream_NEWLINE.add(NEWLINE126)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT127 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1508) 
                    stream_DEDENT.add(DEDENT127)


                    NEWLINE128 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1510) 
                    stream_NEWLINE.add(NEWLINE128)





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
                # 147:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:147:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:149:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE133 = None
        INDENT134 = None
        NEWLINE135 = None
        NEWLINE137 = None
        DEDENT138 = None
        var129 = None

        hint130 = None

        var131 = None

        hint132 = None

        var136 = None


        NEWLINE133_tree = None
        INDENT134_tree = None
        NEWLINE135_tree = None
        NEWLINE137_tree = None
        DEDENT138_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:150:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt35 = 3
                alt35 = self.dfa35.predict(self.input)
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:150:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:150:9: ( var )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == ID) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:150:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1549)
                            var129 = self.var()

                            self._state.following.pop()
                            stream_var.add(var129.tree)



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
                    # 151:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:151:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:151:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:152:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1584)
                    hint130 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint130.tree)


                    # grammar/ShyRecognizerFrontend.g:152:14: ( var )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:152:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1586)
                            var131 = self.var()

                            self._state.following.pop()
                            stream_var.add(var131.tree)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


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
                    # 153:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:153:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:153:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 3:
                    # grammar/ShyRecognizerFrontend.g:154:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1620)
                    hint132 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint132.tree)


                    NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1622) 
                    stream_NEWLINE.add(NEWLINE133)


                    INDENT134 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1624) 
                    stream_INDENT.add(INDENT134)


                    NEWLINE135 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1626) 
                    stream_NEWLINE.add(NEWLINE135)


                    # grammar/ShyRecognizerFrontend.g:154:37: ( ( var )+ NEWLINE )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == ID) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerFrontend.g:154:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:154:39: ( var )+
                            cnt33 = 0
                            while True: #loop33
                                alt33 = 2
                                LA33_0 = self.input.LA(1)

                                if (LA33_0 == ID) :
                                    alt33 = 1


                                if alt33 == 1:
                                    # grammar/ShyRecognizerFrontend.g:154:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1630)
                                    var136 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var136.tree)



                                else:
                                    if cnt33 >= 1:
                                        break #loop33

                                    eee = EarlyExitException(33, self.input)
                                    raise eee

                                cnt33 += 1


                            NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1634) 
                            stream_NEWLINE.add(NEWLINE137)



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


                    DEDENT138 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1640) 
                    stream_DEDENT.add(DEDENT138)


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
                    # 155:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:155:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:155:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:157:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID139 = None

        ID139_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:157:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:157:7: ID
                pass 
                ID139 = self.match(self.input, ID, self.FOLLOW_ID_in_var1674) 
                stream_ID.add(ID139)


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
                # 157:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:157:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:159:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN140 = None
        ID141 = None
        CURLY_CLOSE142 = None
        CURLY_OPEN143 = None
        ID144 = None
        CURLY_CLOSE146 = None
        hint_arg145 = None


        CURLY_OPEN140_tree = None
        ID141_tree = None
        CURLY_CLOSE142_tree = None
        CURLY_OPEN143_tree = None
        ID144_tree = None
        CURLY_CLOSE146_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:160:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:160:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN140 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1699) 
                    stream_CURLY_OPEN.add(CURLY_OPEN140)


                    ID141 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1701) 
                    stream_ID.add(ID141)


                    CURLY_CLOSE142 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1703) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE142)


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
                    # 160:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:160:38: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:161:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN143 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1723) 
                    stream_CURLY_OPEN.add(CURLY_OPEN143)


                    ID144 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1725) 
                    stream_ID.add(ID144)


                    # grammar/ShyRecognizerFrontend.g:161:23: ( hint_arg )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID or LA36_0 == UNDERSCORE) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:161:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1727)
                            hint_arg145 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg145.tree)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


                    CURLY_CLOSE146 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1731) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE146)


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
                    # 161:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:161:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:161:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:163:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set147 = None

        set147_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:163:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set147 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set147))

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
    # grammar/ShyRecognizerFrontend.g:165:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS148 = None
        NUMBER149 = None

        MINUS148_tree = None
        NUMBER149_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:165:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:165:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:165:13: ( MINUS )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == MINUS) :
                    alt38 = 1
                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:165:13: MINUS
                    pass 
                    MINUS148 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1770)
                    MINUS148_tree = self._adaptor.createWithPayload(MINUS148)
                    self._adaptor.addChild(root_0, MINUS148_tree)






                NUMBER149 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1774)
                NUMBER149_tree = self._adaptor.createWithPayload(NUMBER149)
                self._adaptor.addChild(root_0, NUMBER149_tree)





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
    # grammar/ShyRecognizerFrontend.g:166:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS150 = None
        NUMBER151 = None
        DIVIDE152 = None
        NUMBER153 = None

        MINUS150_tree = None
        NUMBER151_tree = None
        DIVIDE152_tree = None
        NUMBER153_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:166:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:166:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:166:13: ( MINUS )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == MINUS) :
                    alt39 = 1
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:166:13: MINUS
                    pass 
                    MINUS150 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1782)
                    MINUS150_tree = self._adaptor.createWithPayload(MINUS150)
                    self._adaptor.addChild(root_0, MINUS150_tree)






                NUMBER151 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1786)
                NUMBER151_tree = self._adaptor.createWithPayload(NUMBER151)
                self._adaptor.addChild(root_0, NUMBER151_tree)



                DIVIDE152 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1788)
                DIVIDE152_tree = self._adaptor.createWithPayload(DIVIDE152)
                self._adaptor.addChild(root_0, DIVIDE152_tree)



                NUMBER153 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1790)
                NUMBER153_tree = self._adaptor.createWithPayload(NUMBER153)
                self._adaptor.addChild(root_0, NUMBER153_tree)





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
        u"\1\23\1\uffff\1\23\1\77\1\30\1\77\2\uffff\1\30"
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
        DFA.unpack(u"\1\4\7\uffff\1\5\53\uffff\1\5"),
        DFA.unpack(u"\1\6\4\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\53\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\4\uffff\1\7")
    ]

    # class definition for DFA #35

    class DFA35(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 23, 30, 62])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 23, 30, 62])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 23, 30, 62])
    FOLLOW_types_in_start94 = frozenset([1, 9, 23, 30, 62])
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
    FOLLOW_NEWLINE_in_proc249 = frozenset([6, 13, 26, 64])
    FOLLOW_proc_args_in_proc263 = frozenset([13, 26, 64])
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
    FOLLOW_statement_call_in_statement449 = frozenset([1])
    FOLLOW_statement_if_in_statement459 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if478 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if488 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if500 = frozenset([1])
    FOLLOW_IF_in_statement_if_head608 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_if_head610 = frozenset([21])
    FOLLOW_INDENT_in_statement_if_head624 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_if_head626 = frozenset([19, 20])
    FOLLOW_statement_in_statement_if_head628 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_if_head632 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_if_head634 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif726 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_elif728 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif742 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif744 = frozenset([19, 20])
    FOLLOW_statement_in_statement_elif746 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_elif750 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif752 = frozenset([1])
    FOLLOW_statement_call_in_condition844 = frozenset([15, 24])
    FOLLOW_DO_in_condition846 = frozenset([24])
    FOLLOW_NEWLINE_in_condition850 = frozenset([1])
    FOLLOW_ANY_in_condition879 = frozenset([19])
    FOLLOW_statement_call_in_condition881 = frozenset([15, 24])
    FOLLOW_DO_in_condition883 = frozenset([24])
    FOLLOW_NEWLINE_in_condition887 = frozenset([1])
    FOLLOW_ALL_in_condition916 = frozenset([19])
    FOLLOW_statement_call_in_condition918 = frozenset([15, 24])
    FOLLOW_DO_in_condition920 = frozenset([24])
    FOLLOW_NEWLINE_in_condition924 = frozenset([1])
    FOLLOW_ELSE_in_statement_else962 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else964 = frozenset([21])
    FOLLOW_INDENT_in_statement_else978 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else980 = frozenset([19, 20])
    FOLLOW_statement_in_statement_else982 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_else986 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else988 = frozenset([1])
    FOLLOW_ID_in_statement_call1062 = frozenset([15, 18, 19, 22, 24, 25])
    FOLLOW_statement_call_args_in_statement_call1064 = frozenset([15, 24])
    FOLLOW_DO_in_statement_call1070 = frozenset([1, 21])
    FOLLOW_NEWLINE_in_statement_call1074 = frozenset([1, 21])
    FOLLOW_INDENT_in_statement_call1088 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call1090 = frozenset([18, 19, 22, 25])
    FOLLOW_statement_call_args_in_statement_call1094 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call1096 = frozenset([13, 18, 19, 22, 25])
    FOLLOW_DEDENT_in_statement_call1102 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call1104 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args1162 = frozenset([1, 18, 19, 22, 25])
    FOLLOW_ID_in_statement_call_arg1179 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1189 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1199 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1209 = frozenset([1])
    FOLLOW_CONSTS_in_consts1228 = frozenset([19])
    FOLLOW_ID_in_consts1230 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1232 = frozenset([21])
    FOLLOW_INDENT_in_consts1242 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1244 = frozenset([19])
    FOLLOW_consts_items_in_consts1246 = frozenset([13])
    FOLLOW_DEDENT_in_consts1248 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1250 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1282 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1298 = frozenset([22, 25])
    FOLLOW_num_whole_in_consts_item1300 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1302 = frozenset([1])
    FOLLOW_ID_in_consts_item1324 = frozenset([22, 25])
    FOLLOW_num_fract_in_consts_item1326 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1328 = frozenset([1])
    FOLLOW_ID_in_consts_item1350 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1352 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1354 = frozenset([1])
    FOLLOW_TYPES_in_types1385 = frozenset([19])
    FOLLOW_ID_in_types1387 = frozenset([24])
    FOLLOW_NEWLINE_in_types1389 = frozenset([21])
    FOLLOW_INDENT_in_types1399 = frozenset([24])
    FOLLOW_NEWLINE_in_types1401 = frozenset([19])
    FOLLOW_types_items_in_types1403 = frozenset([13])
    FOLLOW_DEDENT_in_types1405 = frozenset([24])
    FOLLOW_NEWLINE_in_types1407 = frozenset([1])
    FOLLOW_types_item_in_types_items1439 = frozenset([1, 19])
    FOLLOW_ID_in_types_item1449 = frozenset([12, 19, 24])
    FOLLOW_vars_hint_in_types_item1451 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1478 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1482 = frozenset([1, 21])
    FOLLOW_INDENT_in_vars_hint1494 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1496 = frozenset([12, 19])
    FOLLOW_var_hint_in_vars_hint1500 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1502 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_vars_hint1508 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1510 = frozenset([1])
    FOLLOW_var_in_var_hint1549 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1584 = frozenset([19])
    FOLLOW_var_in_var_hint1586 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1620 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1622 = frozenset([21])
    FOLLOW_INDENT_in_var_hint1624 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1626 = frozenset([19])
    FOLLOW_var_in_var_hint1630 = frozenset([19, 24])
    FOLLOW_NEWLINE_in_var_hint1634 = frozenset([13, 19])
    FOLLOW_DEDENT_in_var_hint1640 = frozenset([1])
    FOLLOW_ID_in_var1674 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1699 = frozenset([19])
    FOLLOW_ID_in_hint1701 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint1703 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1723 = frozenset([19])
    FOLLOW_ID_in_hint1725 = frozenset([19, 63])
    FOLLOW_hint_arg_in_hint1727 = frozenset([11, 19, 63])
    FOLLOW_CURLY_CLOSE_in_hint1731 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1770 = frozenset([25])
    FOLLOW_NUMBER_in_num_whole1774 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1782 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1786 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract1788 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1790 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
