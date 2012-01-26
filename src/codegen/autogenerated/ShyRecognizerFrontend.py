# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-26 18:32:10

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

        self.dfa36 = self.DFA36(
            self, 36,
            eot = self.DFA36_eot,
            eof = self.DFA36_eof,
            min = self.DFA36_min,
            max = self.DFA36_max,
            accept = self.DFA36_accept,
            special = self.DFA36_special,
            transition = self.DFA36_transition
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
                    # elements: proc_args, ID, proc_vars, proc_ops
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
                # elements: statement_else, statement_if_head, statement_elif
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
    # grammar/ShyRecognizerFrontend.g:91:1: condition : ( statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ANY statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ANY NEWLINE INDENT NEWLINE ( statement_call )+ DEDENT NEWLINE DO NEWLINE -> ^( TREE_CONDITION_ANY ( statement_call )+ ) | ALL statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ALL statement_call ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DO60 = None
        NEWLINE61 = None
        ANY62 = None
        DO64 = None
        NEWLINE65 = None
        ANY66 = None
        NEWLINE67 = None
        INDENT68 = None
        NEWLINE69 = None
        DEDENT71 = None
        NEWLINE72 = None
        DO73 = None
        NEWLINE74 = None
        ALL75 = None
        DO77 = None
        NEWLINE78 = None
        statement_call59 = None

        statement_call63 = None

        statement_call70 = None

        statement_call76 = None


        DO60_tree = None
        NEWLINE61_tree = None
        ANY62_tree = None
        DO64_tree = None
        NEWLINE65_tree = None
        ANY66_tree = None
        NEWLINE67_tree = None
        INDENT68_tree = None
        NEWLINE69_tree = None
        DEDENT71_tree = None
        NEWLINE72_tree = None
        DO73_tree = None
        NEWLINE74_tree = None
        ALL75_tree = None
        DO77_tree = None
        NEWLINE78_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:92:5: ( statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ANY statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) | ANY NEWLINE INDENT NEWLINE ( statement_call )+ DEDENT NEWLINE DO NEWLINE -> ^( TREE_CONDITION_ANY ( statement_call )+ ) | ALL statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ALL statement_call ) )
                alt18 = 4
                LA18 = self.input.LA(1)
                if LA18 == ID:
                    alt18 = 1
                elif LA18 == ANY:
                    LA18_2 = self.input.LA(2)

                    if (LA18_2 == NEWLINE) :
                        alt18 = 3
                    elif (LA18_2 == ID) :
                        alt18 = 2
                    else:
                        nvae = NoViableAltException("", 18, 2, self.input)

                        raise nvae


                elif LA18 == ALL:
                    alt18 = 4
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
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




                elif alt18 == 2:
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




                elif alt18 == 3:
                    # grammar/ShyRecognizerFrontend.g:96:9: ANY NEWLINE INDENT NEWLINE ( statement_call )+ DEDENT NEWLINE DO NEWLINE
                    pass 
                    ANY66 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition916) 
                    stream_ANY.add(ANY66)


                    NEWLINE67 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition918) 
                    stream_NEWLINE.add(NEWLINE67)


                    INDENT68 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition928) 
                    stream_INDENT.add(INDENT68)


                    NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition930) 
                    stream_NEWLINE.add(NEWLINE69)


                    # grammar/ShyRecognizerFrontend.g:97:24: ( statement_call )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == ID) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:97:24: statement_call
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_in_condition932)
                            statement_call70 = self.statement_call()

                            self._state.following.pop()
                            stream_statement_call.add(statement_call70.tree)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    DEDENT71 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition936) 
                    stream_DEDENT.add(DEDENT71)


                    NEWLINE72 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition938) 
                    stream_NEWLINE.add(NEWLINE72)


                    DO73 = self.match(self.input, DO, self.FOLLOW_DO_in_condition940) 
                    stream_DO.add(DO73)


                    NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition942) 
                    stream_NEWLINE.add(NEWLINE74)


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
                    # 98:9: -> ^( TREE_CONDITION_ANY ( statement_call )+ )
                    # grammar/ShyRecognizerFrontend.g:98:13: ^( TREE_CONDITION_ANY ( statement_call )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:98:35: ( statement_call )+
                    if not (stream_statement_call.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_statement_call.hasNext():
                        self._adaptor.addChild(root_1, stream_statement_call.nextTree())


                    stream_statement_call.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt18 == 4:
                    # grammar/ShyRecognizerFrontend.g:99:9: ALL statement_call ( DO )? NEWLINE
                    pass 
                    ALL75 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition973) 
                    stream_ALL.add(ALL75)


                    self._state.following.append(self.FOLLOW_statement_call_in_condition975)
                    statement_call76 = self.statement_call()

                    self._state.following.pop()
                    stream_statement_call.add(statement_call76.tree)


                    # grammar/ShyRecognizerFrontend.g:99:28: ( DO )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == DO) :
                        alt17 = 1
                    if alt17 == 1:
                        # grammar/ShyRecognizerFrontend.g:99:28: DO
                        pass 
                        DO77 = self.match(self.input, DO, self.FOLLOW_DO_in_condition977) 
                        stream_DO.add(DO77)





                    NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition981) 
                    stream_NEWLINE.add(NEWLINE78)


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
                    # 100:9: -> ^( TREE_CONDITION_ALL statement_call )
                    # grammar/ShyRecognizerFrontend.g:100:13: ^( TREE_CONDITION_ALL statement_call )
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
    # grammar/ShyRecognizerFrontend.g:103:1: statement_else : ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE79 = None
        NEWLINE80 = None
        INDENT81 = None
        NEWLINE82 = None
        DEDENT84 = None
        NEWLINE85 = None
        statement83 = None


        ELSE79_tree = None
        NEWLINE80_tree = None
        INDENT81_tree = None
        NEWLINE82_tree = None
        DEDENT84_tree = None
        NEWLINE85_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:104:5: ( ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:104:9: ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELSE79 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1019) 
                stream_ELSE.add(ELSE79)


                NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1021) 
                stream_NEWLINE.add(NEWLINE80)


                INDENT81 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1035) 
                stream_INDENT.add(INDENT81)


                NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1037) 
                stream_NEWLINE.add(NEWLINE82)


                # grammar/ShyRecognizerFrontend.g:105:28: ( statement )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if ((ID <= LA19_0 <= IF)) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerFrontend.g:105:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_else1039)
                        statement83 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement83.tree)



                    else:
                        if cnt19 >= 1:
                            break #loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1


                DEDENT84 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1043) 
                stream_DEDENT.add(DEDENT84)


                NEWLINE85 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1045) 
                stream_NEWLINE.add(NEWLINE85)


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
                # 106:9: -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:106:13: ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:107:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:107:36: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:111:1: statement_call : ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID86 = None
        DO88 = None
        NEWLINE89 = None
        INDENT90 = None
        NEWLINE91 = None
        NEWLINE93 = None
        DEDENT94 = None
        NEWLINE95 = None
        statement_call_args87 = None

        statement_call_args92 = None


        ID86_tree = None
        DO88_tree = None
        NEWLINE89_tree = None
        INDENT90_tree = None
        NEWLINE91_tree = None
        NEWLINE93_tree = None
        DEDENT94_tree = None
        NEWLINE95_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:112:5: ( ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:112:9: ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID86 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call1119) 
                stream_ID.add(ID86)


                # grammar/ShyRecognizerFrontend.g:112:12: ( statement_call_args )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER) :
                    alt20 = 1
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:112:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1121)
                    statement_call_args87 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args87.tree)





                # grammar/ShyRecognizerFrontend.g:112:34: ( DO | NEWLINE )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == DO) :
                    alt21 = 1
                elif (LA21_0 == NEWLINE) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae


                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:112:36: DO
                    pass 
                    DO88 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_call1127) 
                    stream_DO.add(DO88)



                elif alt21 == 2:
                    # grammar/ShyRecognizerFrontend.g:112:41: NEWLINE
                    pass 
                    NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1131) 
                    stream_NEWLINE.add(NEWLINE89)





                # grammar/ShyRecognizerFrontend.g:113:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == INDENT) :
                    alt23 = 1
                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:113:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT90 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call1145) 
                    stream_INDENT.add(INDENT90)


                    NEWLINE91 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1147) 
                    stream_NEWLINE.add(NEWLINE91)


                    # grammar/ShyRecognizerFrontend.g:113:26: ( statement_call_args NEWLINE )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:113:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1151)
                            statement_call_args92 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args92.tree)


                            NEWLINE93 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1153) 
                            stream_NEWLINE.add(NEWLINE93)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    DEDENT94 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call1159) 
                    stream_DEDENT.add(DEDENT94)


                    NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1161) 
                    stream_NEWLINE.add(NEWLINE95)





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
                # 114:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:114:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:115:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:118:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg96 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:118:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:118:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:118:23: ( statement_call_arg )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerFrontend.g:118:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1219)
                        statement_call_arg96 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg96.tree)



                    else:
                        if cnt24 >= 1:
                            break #loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1




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
    # grammar/ShyRecognizerFrontend.g:120:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID97 = None
        EXPRESSION98 = None
        num_whole99 = None

        num_fract100 = None


        ID97_tree = None
        EXPRESSION98_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:121:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt25 = 4
                LA25 = self.input.LA(1)
                if LA25 == ID:
                    alt25 = 1
                elif LA25 == EXPRESSION:
                    alt25 = 2
                elif LA25 == MINUS:
                    LA25_3 = self.input.LA(2)

                    if (LA25_3 == NUMBER) :
                        LA25_4 = self.input.LA(3)

                        if (LA25_4 == DIVIDE) :
                            alt25 = 4
                        elif (LA25_4 == DO or (EXPRESSION <= LA25_4 <= ID) or LA25_4 == MINUS or (NEWLINE <= LA25_4 <= NUMBER)) :
                            alt25 = 3
                        else:
                            nvae = NoViableAltException("", 25, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 25, 3, self.input)

                        raise nvae


                elif LA25 == NUMBER:
                    LA25_4 = self.input.LA(2)

                    if (LA25_4 == DIVIDE) :
                        alt25 = 4
                    elif (LA25_4 == DO or (EXPRESSION <= LA25_4 <= ID) or LA25_4 == MINUS or (NEWLINE <= LA25_4 <= NUMBER)) :
                        alt25 = 3
                    else:
                        nvae = NoViableAltException("", 25, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # grammar/ShyRecognizerFrontend.g:121:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID97 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1236)
                    ID97_tree = self._adaptor.createWithPayload(ID97)
                    self._adaptor.addChild(root_0, ID97_tree)




                elif alt25 == 2:
                    # grammar/ShyRecognizerFrontend.g:122:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION98 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1246)
                    EXPRESSION98_tree = self._adaptor.createWithPayload(EXPRESSION98)
                    self._adaptor.addChild(root_0, EXPRESSION98_tree)




                elif alt25 == 3:
                    # grammar/ShyRecognizerFrontend.g:123:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1256)
                    num_whole99 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole99.tree)



                elif alt25 == 4:
                    # grammar/ShyRecognizerFrontend.g:124:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1266)
                    num_fract100 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract100.tree)



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
    # grammar/ShyRecognizerFrontend.g:127:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS101 = None
        ID102 = None
        NEWLINE103 = None
        INDENT104 = None
        NEWLINE105 = None
        DEDENT107 = None
        NEWLINE108 = None
        consts_items106 = None


        CONSTS101_tree = None
        ID102_tree = None
        NEWLINE103_tree = None
        INDENT104_tree = None
        NEWLINE105_tree = None
        DEDENT107_tree = None
        NEWLINE108_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:128:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:128:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS101 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1285) 
                stream_CONSTS.add(CONSTS101)


                ID102 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1287) 
                stream_ID.add(ID102)


                NEWLINE103 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1289) 
                stream_NEWLINE.add(NEWLINE103)


                INDENT104 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1299) 
                stream_INDENT.add(INDENT104)


                NEWLINE105 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1301) 
                stream_NEWLINE.add(NEWLINE105)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1303)
                consts_items106 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items106.tree)


                DEDENT107 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1305) 
                stream_DEDENT.add(DEDENT107)


                NEWLINE108 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1307) 
                stream_NEWLINE.add(NEWLINE108)


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
                # 130:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:130:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:132:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item109 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:132:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:132:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:132:16: ( consts_item )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ID) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerFrontend.g:132:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1339)
                        consts_item109 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item109.tree)



                    else:
                        if cnt26 >= 1:
                            break #loop26

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1




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
    # grammar/ShyRecognizerFrontend.g:133:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID110 = None
        NEWLINE112 = None
        ID113 = None
        NEWLINE115 = None
        ID116 = None
        EXPRESSION117 = None
        NEWLINE118 = None
        num_whole111 = None

        num_fract114 = None


        ID110_tree = None
        NEWLINE112_tree = None
        ID113_tree = None
        NEWLINE115_tree = None
        ID116_tree = None
        EXPRESSION117_tree = None
        NEWLINE118_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:134:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt27 = 3
                LA27_0 = self.input.LA(1)

                if (LA27_0 == ID) :
                    LA27 = self.input.LA(2)
                    if LA27 == EXPRESSION:
                        alt27 = 3
                    elif LA27 == MINUS:
                        LA27_3 = self.input.LA(3)

                        if (LA27_3 == NUMBER) :
                            LA27_4 = self.input.LA(4)

                            if (LA27_4 == DIVIDE) :
                                alt27 = 2
                            elif (LA27_4 == NEWLINE) :
                                alt27 = 1
                            else:
                                nvae = NoViableAltException("", 27, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 27, 3, self.input)

                            raise nvae


                    elif LA27 == NUMBER:
                        LA27_4 = self.input.LA(3)

                        if (LA27_4 == DIVIDE) :
                            alt27 = 2
                        elif (LA27_4 == NEWLINE) :
                            alt27 = 1
                        else:
                            nvae = NoViableAltException("", 27, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 27, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammar/ShyRecognizerFrontend.g:134:9: ID num_whole NEWLINE
                    pass 
                    ID110 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1355) 
                    stream_ID.add(ID110)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1357)
                    num_whole111 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole111.tree)


                    NEWLINE112 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1359) 
                    stream_NEWLINE.add(NEWLINE112)


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
                    # 134:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:134:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt27 == 2:
                    # grammar/ShyRecognizerFrontend.g:135:9: ID num_fract NEWLINE
                    pass 
                    ID113 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1381) 
                    stream_ID.add(ID113)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1383)
                    num_fract114 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract114.tree)


                    NEWLINE115 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1385) 
                    stream_NEWLINE.add(NEWLINE115)


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
                    # 135:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:135:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt27 == 3:
                    # grammar/ShyRecognizerFrontend.g:136:9: ID EXPRESSION NEWLINE
                    pass 
                    ID116 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1407) 
                    stream_ID.add(ID116)


                    EXPRESSION117 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1409) 
                    stream_EXPRESSION.add(EXPRESSION117)


                    NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1411) 
                    stream_NEWLINE.add(NEWLINE118)


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
                    # 136:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:136:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:139:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES119 = None
        ID120 = None
        NEWLINE121 = None
        INDENT122 = None
        NEWLINE123 = None
        DEDENT125 = None
        NEWLINE126 = None
        types_items124 = None


        TYPES119_tree = None
        ID120_tree = None
        NEWLINE121_tree = None
        INDENT122_tree = None
        NEWLINE123_tree = None
        DEDENT125_tree = None
        NEWLINE126_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:140:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:140:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES119 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1442) 
                stream_TYPES.add(TYPES119)


                ID120 = self.match(self.input, ID, self.FOLLOW_ID_in_types1444) 
                stream_ID.add(ID120)


                NEWLINE121 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1446) 
                stream_NEWLINE.add(NEWLINE121)


                INDENT122 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1456) 
                stream_INDENT.add(INDENT122)


                NEWLINE123 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1458) 
                stream_NEWLINE.add(NEWLINE123)


                self._state.following.append(self.FOLLOW_types_items_in_types1460)
                types_items124 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items124.tree)


                DEDENT125 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1462) 
                stream_DEDENT.add(DEDENT125)


                NEWLINE126 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1464) 
                stream_NEWLINE.add(NEWLINE126)


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
                # 142:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:142:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:144:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item127 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:144:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:144:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:144:15: ( types_item )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == ID) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerFrontend.g:144:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1496)
                        types_item127 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item127.tree)



                    else:
                        if cnt28 >= 1:
                            break #loop28

                        eee = EarlyExitException(28, self.input)
                        raise eee

                    cnt28 += 1




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
    # grammar/ShyRecognizerFrontend.g:145:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID128 = None
        vars_hint129 = None


        ID128_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:145:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:145:14: ID vars_hint
                pass 
                ID128 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1506) 
                stream_ID.add(ID128)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1508)
                vars_hint129 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint129.tree)


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
                # 145:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:145:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:147:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE131 = None
        INDENT132 = None
        NEWLINE133 = None
        NEWLINE135 = None
        DEDENT136 = None
        NEWLINE137 = None
        var_hint130 = None

        var_hint134 = None


        NEWLINE131_tree = None
        INDENT132_tree = None
        NEWLINE133_tree = None
        NEWLINE135_tree = None
        DEDENT136_tree = None
        NEWLINE137_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:148:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:148:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:148:9: ( var_hint )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == CURLY_OPEN or LA29_0 == ID) :
                    alt29 = 1
                if alt29 == 1:
                    # grammar/ShyRecognizerFrontend.g:148:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1535)
                    var_hint130 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint130.tree)





                NEWLINE131 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1539) 
                stream_NEWLINE.add(NEWLINE131)


                # grammar/ShyRecognizerFrontend.g:149:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == INDENT) :
                    alt31 = 1
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:149:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT132 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1551) 
                    stream_INDENT.add(INDENT132)


                    NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1553) 
                    stream_NEWLINE.add(NEWLINE133)


                    # grammar/ShyRecognizerFrontend.g:149:26: ( var_hint NEWLINE )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == CURLY_OPEN or LA30_0 == ID) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:149:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1557)
                            var_hint134 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint134.tree)


                            NEWLINE135 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1559) 
                            stream_NEWLINE.add(NEWLINE135)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


                    DEDENT136 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1565) 
                    stream_DEDENT.add(DEDENT136)


                    NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1567) 
                    stream_NEWLINE.add(NEWLINE137)





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
                # 150:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:150:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:152:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE142 = None
        INDENT143 = None
        NEWLINE144 = None
        NEWLINE146 = None
        DEDENT147 = None
        var138 = None

        hint139 = None

        var140 = None

        hint141 = None

        var145 = None


        NEWLINE142_tree = None
        INDENT143_tree = None
        NEWLINE144_tree = None
        NEWLINE146_tree = None
        DEDENT147_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:153:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt36 = 3
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:153:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:153:9: ( var )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:153:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1606)
                            var138 = self.var()

                            self._state.following.pop()
                            stream_var.add(var138.tree)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


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
                    # 154:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:154:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:154:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt36 == 2:
                    # grammar/ShyRecognizerFrontend.g:155:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1641)
                    hint139 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint139.tree)


                    # grammar/ShyRecognizerFrontend.g:155:14: ( var )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == ID) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerFrontend.g:155:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1643)
                            var140 = self.var()

                            self._state.following.pop()
                            stream_var.add(var140.tree)



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


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
                    # 156:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:156:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:156:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt36 == 3:
                    # grammar/ShyRecognizerFrontend.g:157:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1677)
                    hint141 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint141.tree)


                    NEWLINE142 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1679) 
                    stream_NEWLINE.add(NEWLINE142)


                    INDENT143 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1681) 
                    stream_INDENT.add(INDENT143)


                    NEWLINE144 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1683) 
                    stream_NEWLINE.add(NEWLINE144)


                    # grammar/ShyRecognizerFrontend.g:157:37: ( ( var )+ NEWLINE )+
                    cnt35 = 0
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == ID) :
                            alt35 = 1


                        if alt35 == 1:
                            # grammar/ShyRecognizerFrontend.g:157:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:157:39: ( var )+
                            cnt34 = 0
                            while True: #loop34
                                alt34 = 2
                                LA34_0 = self.input.LA(1)

                                if (LA34_0 == ID) :
                                    alt34 = 1


                                if alt34 == 1:
                                    # grammar/ShyRecognizerFrontend.g:157:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1687)
                                    var145 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var145.tree)



                                else:
                                    if cnt34 >= 1:
                                        break #loop34

                                    eee = EarlyExitException(34, self.input)
                                    raise eee

                                cnt34 += 1


                            NEWLINE146 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1691) 
                            stream_NEWLINE.add(NEWLINE146)



                        else:
                            if cnt35 >= 1:
                                break #loop35

                            eee = EarlyExitException(35, self.input)
                            raise eee

                        cnt35 += 1


                    DEDENT147 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1697) 
                    stream_DEDENT.add(DEDENT147)


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
                    # 158:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:158:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:158:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:160:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID148 = None

        ID148_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:160:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:160:7: ID
                pass 
                ID148 = self.match(self.input, ID, self.FOLLOW_ID_in_var1731) 
                stream_ID.add(ID148)


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
                # 160:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:160:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:162:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN149 = None
        ID150 = None
        CURLY_CLOSE151 = None
        CURLY_OPEN152 = None
        ID153 = None
        CURLY_CLOSE155 = None
        hint_arg154 = None


        CURLY_OPEN149_tree = None
        ID150_tree = None
        CURLY_CLOSE151_tree = None
        CURLY_OPEN152_tree = None
        ID153_tree = None
        CURLY_CLOSE155_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:163:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == CURLY_OPEN) :
                    LA38_1 = self.input.LA(2)

                    if (LA38_1 == ID) :
                        LA38_2 = self.input.LA(3)

                        if (LA38_2 == CURLY_CLOSE) :
                            alt38 = 1
                        elif (LA38_2 == ID or LA38_2 == UNDERSCORE) :
                            alt38 = 2
                        else:
                            nvae = NoViableAltException("", 38, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 38, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:163:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN149 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1756) 
                    stream_CURLY_OPEN.add(CURLY_OPEN149)


                    ID150 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1758) 
                    stream_ID.add(ID150)


                    CURLY_CLOSE151 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1760) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE151)


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
                    # 163:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:163:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:164:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN152 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1780) 
                    stream_CURLY_OPEN.add(CURLY_OPEN152)


                    ID153 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1782) 
                    stream_ID.add(ID153)


                    # grammar/ShyRecognizerFrontend.g:164:23: ( hint_arg )+
                    cnt37 = 0
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == ID or LA37_0 == UNDERSCORE) :
                            alt37 = 1


                        if alt37 == 1:
                            # grammar/ShyRecognizerFrontend.g:164:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1784)
                            hint_arg154 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg154.tree)



                        else:
                            if cnt37 >= 1:
                                break #loop37

                            eee = EarlyExitException(37, self.input)
                            raise eee

                        cnt37 += 1


                    CURLY_CLOSE155 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1788) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE155)


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
                    # 164:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:164:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:164:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:166:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set156 = None

        set156_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:166:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set156 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set156))

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
    # grammar/ShyRecognizerFrontend.g:168:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS157 = None
        NUMBER158 = None

        MINUS157_tree = None
        NUMBER158_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:168:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:168:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:168:13: ( MINUS )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == MINUS) :
                    alt39 = 1
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:168:13: MINUS
                    pass 
                    MINUS157 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1827)
                    MINUS157_tree = self._adaptor.createWithPayload(MINUS157)
                    self._adaptor.addChild(root_0, MINUS157_tree)






                NUMBER158 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1831)
                NUMBER158_tree = self._adaptor.createWithPayload(NUMBER158)
                self._adaptor.addChild(root_0, NUMBER158_tree)





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
    # grammar/ShyRecognizerFrontend.g:169:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS159 = None
        NUMBER160 = None
        DIVIDE161 = None
        NUMBER162 = None

        MINUS159_tree = None
        NUMBER160_tree = None
        DIVIDE161_tree = None
        NUMBER162_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:169:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:169:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:169:13: ( MINUS )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == MINUS) :
                    alt40 = 1
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:169:13: MINUS
                    pass 
                    MINUS159 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1839)
                    MINUS159_tree = self._adaptor.createWithPayload(MINUS159)
                    self._adaptor.addChild(root_0, MINUS159_tree)






                NUMBER160 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1843)
                NUMBER160_tree = self._adaptor.createWithPayload(NUMBER160)
                self._adaptor.addChild(root_0, NUMBER160_tree)



                DIVIDE161 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1845)
                DIVIDE161_tree = self._adaptor.createWithPayload(DIVIDE161)
                self._adaptor.addChild(root_0, DIVIDE161_tree)



                NUMBER162 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1847)
                NUMBER162_tree = self._adaptor.createWithPayload(NUMBER162)
                self._adaptor.addChild(root_0, NUMBER162_tree)





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



    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA36_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA36_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\77\1\30\1\77\2\uffff\1\30"
        )

    DFA36_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA36_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA36_transition = [
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

    # class definition for DFA #36

    class DFA36(DFA):
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
    FOLLOW_ANY_in_condition916 = frozenset([24])
    FOLLOW_NEWLINE_in_condition918 = frozenset([21])
    FOLLOW_INDENT_in_condition928 = frozenset([24])
    FOLLOW_NEWLINE_in_condition930 = frozenset([19])
    FOLLOW_statement_call_in_condition932 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition936 = frozenset([24])
    FOLLOW_NEWLINE_in_condition938 = frozenset([15])
    FOLLOW_DO_in_condition940 = frozenset([24])
    FOLLOW_NEWLINE_in_condition942 = frozenset([1])
    FOLLOW_ALL_in_condition973 = frozenset([19])
    FOLLOW_statement_call_in_condition975 = frozenset([15, 24])
    FOLLOW_DO_in_condition977 = frozenset([24])
    FOLLOW_NEWLINE_in_condition981 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1019 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else1021 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1035 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else1037 = frozenset([19, 20])
    FOLLOW_statement_in_statement_else1039 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_else1043 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else1045 = frozenset([1])
    FOLLOW_ID_in_statement_call1119 = frozenset([15, 18, 19, 22, 24, 25])
    FOLLOW_statement_call_args_in_statement_call1121 = frozenset([15, 24])
    FOLLOW_DO_in_statement_call1127 = frozenset([1, 21])
    FOLLOW_NEWLINE_in_statement_call1131 = frozenset([1, 21])
    FOLLOW_INDENT_in_statement_call1145 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call1147 = frozenset([18, 19, 22, 25])
    FOLLOW_statement_call_args_in_statement_call1151 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call1153 = frozenset([13, 18, 19, 22, 25])
    FOLLOW_DEDENT_in_statement_call1159 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call1161 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args1219 = frozenset([1, 18, 19, 22, 25])
    FOLLOW_ID_in_statement_call_arg1236 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1246 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1256 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1266 = frozenset([1])
    FOLLOW_CONSTS_in_consts1285 = frozenset([19])
    FOLLOW_ID_in_consts1287 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1289 = frozenset([21])
    FOLLOW_INDENT_in_consts1299 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1301 = frozenset([19])
    FOLLOW_consts_items_in_consts1303 = frozenset([13])
    FOLLOW_DEDENT_in_consts1305 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1307 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1339 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1355 = frozenset([22, 25])
    FOLLOW_num_whole_in_consts_item1357 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1359 = frozenset([1])
    FOLLOW_ID_in_consts_item1381 = frozenset([22, 25])
    FOLLOW_num_fract_in_consts_item1383 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1385 = frozenset([1])
    FOLLOW_ID_in_consts_item1407 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1409 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1411 = frozenset([1])
    FOLLOW_TYPES_in_types1442 = frozenset([19])
    FOLLOW_ID_in_types1444 = frozenset([24])
    FOLLOW_NEWLINE_in_types1446 = frozenset([21])
    FOLLOW_INDENT_in_types1456 = frozenset([24])
    FOLLOW_NEWLINE_in_types1458 = frozenset([19])
    FOLLOW_types_items_in_types1460 = frozenset([13])
    FOLLOW_DEDENT_in_types1462 = frozenset([24])
    FOLLOW_NEWLINE_in_types1464 = frozenset([1])
    FOLLOW_types_item_in_types_items1496 = frozenset([1, 19])
    FOLLOW_ID_in_types_item1506 = frozenset([12, 19, 24])
    FOLLOW_vars_hint_in_types_item1508 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1535 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1539 = frozenset([1, 21])
    FOLLOW_INDENT_in_vars_hint1551 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1553 = frozenset([12, 19])
    FOLLOW_var_hint_in_vars_hint1557 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1559 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_vars_hint1565 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1567 = frozenset([1])
    FOLLOW_var_in_var_hint1606 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1641 = frozenset([19])
    FOLLOW_var_in_var_hint1643 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1677 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1679 = frozenset([21])
    FOLLOW_INDENT_in_var_hint1681 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1683 = frozenset([19])
    FOLLOW_var_in_var_hint1687 = frozenset([19, 24])
    FOLLOW_NEWLINE_in_var_hint1691 = frozenset([13, 19])
    FOLLOW_DEDENT_in_var_hint1697 = frozenset([1])
    FOLLOW_ID_in_var1731 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1756 = frozenset([19])
    FOLLOW_ID_in_hint1758 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint1760 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1780 = frozenset([19])
    FOLLOW_ID_in_hint1782 = frozenset([19, 63])
    FOLLOW_hint_arg_in_hint1784 = frozenset([11, 19, 63])
    FOLLOW_CURLY_CLOSE_in_hint1788 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1827 = frozenset([25])
    FOLLOW_NUMBER_in_num_whole1831 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1839 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1843 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract1845 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1847 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
