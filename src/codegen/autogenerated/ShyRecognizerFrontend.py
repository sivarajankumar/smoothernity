# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-24 15:10:57

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
DO=13
EXPRESSION=14
ID=15
IF=16
INDENT=17
MINUS=18
MODULE=19
NEWLINE=20
NUMBER=21
OPS=22
PASTE=23
PROC=24
REPLACE=25
STATELESS=26
STRING=27
TREE_ARBITRARY_TOKEN=28
TREE_CONDITION_ANY=29
TREE_CONSTS=30
TREE_COPY=31
TREE_COPY_PASTE=32
TREE_EXPRESSION=33
TREE_HINT=34
TREE_HINT_NONE=35
TREE_MODULE=36
TREE_NUM_FRACT=37
TREE_NUM_WHOLE=38
TREE_PASTE=39
TREE_PASTE_REPLACE=40
TREE_PASTE_WITH=41
TREE_PROC=42
TREE_PROC_ARGS=43
TREE_PROC_VARS=44
TREE_STATELESS=45
TREE_STATEMENTS=46
TREE_STATEMENT_CALL=47
TREE_STATEMENT_CALL_ARGS=48
TREE_STATEMENT_ELIF=49
TREE_STATEMENT_IF=50
TREE_TYPES=51
TREE_TYPES_ITEM=52
TREE_VAR=53
TREE_VARS_HINT=54
TREE_VAR_HINT=55
TYPES=56
UNDERSCORE=57
VARS=58
WHITESPACE=59
WITH=60

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "EXPRESSION", "ID", "IF", "INDENT", 
    "MINUS", "MODULE", "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", 
    "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_IF", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VAR", "TREE_VARS_HINT", 
    "TREE_VAR_HINT", "TYPES", "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

        self.dfa26 = self.DFA26(
            self, 26,
            eot = self.DFA26_eot,
            eof = self.DFA26_eof,
            min = self.DFA26_min,
            max = self.DFA26_max,
            accept = self.DFA26_accept,
            special = self.DFA26_special,
            transition = self.DFA26_transition
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
                    # elements: ID, proc_vars, proc_ops, proc_args
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
    # grammar/ShyRecognizerFrontend.g:62:1: statement_if : IF statement_call DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_IF ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF42 = None
        DO44 = None
        NEWLINE45 = None
        INDENT46 = None
        NEWLINE47 = None
        DEDENT49 = None
        NEWLINE50 = None
        statement_call43 = None

        statement48 = None


        IF42_tree = None
        DO44_tree = None
        NEWLINE45_tree = None
        INDENT46_tree = None
        NEWLINE47_tree = None
        DEDENT49_tree = None
        NEWLINE50_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statement_call = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:63:5: ( IF statement_call DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_IF ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) ) )
                # grammar/ShyRecognizerFrontend.g:63:9: IF statement_call DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                IF42 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if478) 
                stream_IF.add(IF42)


                self._state.following.append(self.FOLLOW_statement_call_in_statement_if480)
                statement_call43 = self.statement_call()

                self._state.following.pop()
                stream_statement_call.add(statement_call43.tree)


                DO44 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_if482) 
                stream_DO.add(DO44)


                NEWLINE45 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if484) 
                stream_NEWLINE.add(NEWLINE45)


                INDENT46 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_if498) 
                stream_INDENT.add(INDENT46)


                NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if500) 
                stream_NEWLINE.add(NEWLINE47)


                # grammar/ShyRecognizerFrontend.g:64:28: ( statement )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if ((ID <= LA10_0 <= IF)) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:64:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_if502)
                        statement48 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement48.tree)



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1


                DEDENT49 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_if506) 
                stream_DEDENT.add(DEDENT49)


                NEWLINE50 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if508) 
                stream_NEWLINE.add(NEWLINE50)


                # AST Rewrite
                # elements: statement, statement_call
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
                # 65:9: -> ^( TREE_STATEMENT_IF ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:65:13: ^( TREE_STATEMENT_IF ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:66:17: ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:67:21: ^( TREE_CONDITION_ANY statement_call )
                root_3 = self._adaptor.nil()
                root_3 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                , root_3)

                self._adaptor.addChild(root_3, stream_statement_call.nextTree())

                self._adaptor.addChild(root_2, root_3)

                # grammar/ShyRecognizerFrontend.g:68:21: ^( TREE_STATEMENTS ( statement )+ )
                root_3 = self._adaptor.nil()
                root_3 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_3)

                # grammar/ShyRecognizerFrontend.g:68:40: ( statement )+
                if not (stream_statement.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_statement.hasNext():
                    self._adaptor.addChild(root_3, stream_statement.nextTree())


                stream_statement.reset()

                self._adaptor.addChild(root_2, root_3)

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

    # $ANTLR end "statement_if"


    class statement_call_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call"
    # grammar/ShyRecognizerFrontend.g:73:1: statement_call : ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID51 = None
        NEWLINE53 = None
        INDENT54 = None
        NEWLINE55 = None
        NEWLINE57 = None
        DEDENT58 = None
        NEWLINE59 = None
        statement_call_args52 = None

        statement_call_args56 = None


        ID51_tree = None
        NEWLINE53_tree = None
        INDENT54_tree = None
        NEWLINE55_tree = None
        NEWLINE57_tree = None
        DEDENT58_tree = None
        NEWLINE59_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:74:5: ( ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:74:9: ID ( statement_call_args )? NEWLINE ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID51 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call652) 
                stream_ID.add(ID51)


                # grammar/ShyRecognizerFrontend.g:74:12: ( statement_call_args )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((EXPRESSION <= LA11_0 <= ID) or LA11_0 == MINUS or LA11_0 == NUMBER) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerFrontend.g:74:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call654)
                    statement_call_args52 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args52.tree)





                NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call658) 
                stream_NEWLINE.add(NEWLINE53)


                # grammar/ShyRecognizerFrontend.g:75:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == INDENT) :
                    alt13 = 1
                if alt13 == 1:
                    # grammar/ShyRecognizerFrontend.g:75:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT54 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call671) 
                    stream_INDENT.add(INDENT54)


                    NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call673) 
                    stream_NEWLINE.add(NEWLINE55)


                    # grammar/ShyRecognizerFrontend.g:75:26: ( statement_call_args NEWLINE )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA12_0 <= ID) or LA12_0 == MINUS or LA12_0 == NUMBER) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyRecognizerFrontend.g:75:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call677)
                            statement_call_args56 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args56.tree)


                            NEWLINE57 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call679) 
                            stream_NEWLINE.add(NEWLINE57)



                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    DEDENT58 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call685) 
                    stream_DEDENT.add(DEDENT58)


                    NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call687) 
                    stream_NEWLINE.add(NEWLINE59)





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
                # 76:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:76:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:77:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:80:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg60 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:80:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:80:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:80:23: ( statement_call_arg )+
                cnt14 = 0
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA14_0 <= ID) or LA14_0 == MINUS or LA14_0 == NUMBER) :
                        alt14 = 1


                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:80:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args745)
                        statement_call_arg60 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg60.tree)



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

    # $ANTLR end "statement_call_args"


    class statement_call_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_arg_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerFrontend.g:82:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID61 = None
        EXPRESSION62 = None
        num_whole63 = None

        num_fract64 = None


        ID61_tree = None
        EXPRESSION62_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt15 = 4
                LA15 = self.input.LA(1)
                if LA15 == ID:
                    alt15 = 1
                elif LA15 == EXPRESSION:
                    alt15 = 2
                elif LA15 == MINUS:
                    LA15_3 = self.input.LA(2)

                    if (LA15_3 == NUMBER) :
                        LA15_4 = self.input.LA(3)

                        if (LA15_4 == DIVIDE) :
                            alt15 = 4
                        elif ((EXPRESSION <= LA15_4 <= ID) or LA15_4 == MINUS or (NEWLINE <= LA15_4 <= NUMBER)) :
                            alt15 = 3
                        else:
                            nvae = NoViableAltException("", 15, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 15, 3, self.input)

                        raise nvae


                elif LA15 == NUMBER:
                    LA15_4 = self.input.LA(2)

                    if (LA15_4 == DIVIDE) :
                        alt15 = 4
                    elif ((EXPRESSION <= LA15_4 <= ID) or LA15_4 == MINUS or (NEWLINE <= LA15_4 <= NUMBER)) :
                        alt15 = 3
                    else:
                        nvae = NoViableAltException("", 15, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:83:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg762)
                    ID61_tree = self._adaptor.createWithPayload(ID61)
                    self._adaptor.addChild(root_0, ID61_tree)




                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:84:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION62 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg772)
                    EXPRESSION62_tree = self._adaptor.createWithPayload(EXPRESSION62)
                    self._adaptor.addChild(root_0, EXPRESSION62_tree)




                elif alt15 == 3:
                    # grammar/ShyRecognizerFrontend.g:85:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg782)
                    num_whole63 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole63.tree)



                elif alt15 == 4:
                    # grammar/ShyRecognizerFrontend.g:86:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg792)
                    num_fract64 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract64.tree)



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
    # grammar/ShyRecognizerFrontend.g:89:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS65 = None
        ID66 = None
        NEWLINE67 = None
        INDENT68 = None
        NEWLINE69 = None
        DEDENT71 = None
        NEWLINE72 = None
        consts_items70 = None


        CONSTS65_tree = None
        ID66_tree = None
        NEWLINE67_tree = None
        INDENT68_tree = None
        NEWLINE69_tree = None
        DEDENT71_tree = None
        NEWLINE72_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:90:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:90:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS65 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts811) 
                stream_CONSTS.add(CONSTS65)


                ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_consts813) 
                stream_ID.add(ID66)


                NEWLINE67 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts815) 
                stream_NEWLINE.add(NEWLINE67)


                INDENT68 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts825) 
                stream_INDENT.add(INDENT68)


                NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts827) 
                stream_NEWLINE.add(NEWLINE69)


                self._state.following.append(self.FOLLOW_consts_items_in_consts829)
                consts_items70 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items70.tree)


                DEDENT71 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts831) 
                stream_DEDENT.add(DEDENT71)


                NEWLINE72 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts833) 
                stream_NEWLINE.add(NEWLINE72)


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
                # 92:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:92:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:94:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item73 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:94:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:94:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:94:16: ( consts_item )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ID) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:94:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items865)
                        consts_item73 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item73.tree)



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1




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
    # grammar/ShyRecognizerFrontend.g:95:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID74 = None
        NEWLINE76 = None
        ID77 = None
        NEWLINE79 = None
        ID80 = None
        EXPRESSION81 = None
        NEWLINE82 = None
        num_whole75 = None

        num_fract78 = None


        ID74_tree = None
        NEWLINE76_tree = None
        ID77_tree = None
        NEWLINE79_tree = None
        ID80_tree = None
        EXPRESSION81_tree = None
        NEWLINE82_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:96:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt17 = 3
                LA17_0 = self.input.LA(1)

                if (LA17_0 == ID) :
                    LA17 = self.input.LA(2)
                    if LA17 == EXPRESSION:
                        alt17 = 3
                    elif LA17 == MINUS:
                        LA17_3 = self.input.LA(3)

                        if (LA17_3 == NUMBER) :
                            LA17_4 = self.input.LA(4)

                            if (LA17_4 == DIVIDE) :
                                alt17 = 2
                            elif (LA17_4 == NEWLINE) :
                                alt17 = 1
                            else:
                                nvae = NoViableAltException("", 17, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 17, 3, self.input)

                            raise nvae


                    elif LA17 == NUMBER:
                        LA17_4 = self.input.LA(3)

                        if (LA17_4 == DIVIDE) :
                            alt17 = 2
                        elif (LA17_4 == NEWLINE) :
                            alt17 = 1
                        else:
                            nvae = NoViableAltException("", 17, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 17, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:96:9: ID num_whole NEWLINE
                    pass 
                    ID74 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item881) 
                    stream_ID.add(ID74)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item883)
                    num_whole75 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole75.tree)


                    NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item885) 
                    stream_NEWLINE.add(NEWLINE76)


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
                    # 96:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:96:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:97:9: ID num_fract NEWLINE
                    pass 
                    ID77 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item907) 
                    stream_ID.add(ID77)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item909)
                    num_fract78 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract78.tree)


                    NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item911) 
                    stream_NEWLINE.add(NEWLINE79)


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
                    # 97:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:97:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt17 == 3:
                    # grammar/ShyRecognizerFrontend.g:98:9: ID EXPRESSION NEWLINE
                    pass 
                    ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item933) 
                    stream_ID.add(ID80)


                    EXPRESSION81 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item935) 
                    stream_EXPRESSION.add(EXPRESSION81)


                    NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item937) 
                    stream_NEWLINE.add(NEWLINE82)


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
                    # 98:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:98:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:101:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES83 = None
        ID84 = None
        NEWLINE85 = None
        INDENT86 = None
        NEWLINE87 = None
        DEDENT89 = None
        NEWLINE90 = None
        types_items88 = None


        TYPES83_tree = None
        ID84_tree = None
        NEWLINE85_tree = None
        INDENT86_tree = None
        NEWLINE87_tree = None
        DEDENT89_tree = None
        NEWLINE90_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:102:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:102:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES83 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types968) 
                stream_TYPES.add(TYPES83)


                ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_types970) 
                stream_ID.add(ID84)


                NEWLINE85 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types972) 
                stream_NEWLINE.add(NEWLINE85)


                INDENT86 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types982) 
                stream_INDENT.add(INDENT86)


                NEWLINE87 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types984) 
                stream_NEWLINE.add(NEWLINE87)


                self._state.following.append(self.FOLLOW_types_items_in_types986)
                types_items88 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items88.tree)


                DEDENT89 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types988) 
                stream_DEDENT.add(DEDENT89)


                NEWLINE90 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types990) 
                stream_NEWLINE.add(NEWLINE90)


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
                # 104:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:104:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:106:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item91 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:106:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:106:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:106:15: ( types_item )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == ID) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerFrontend.g:106:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1022)
                        types_item91 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item91.tree)



                    else:
                        if cnt18 >= 1:
                            break #loop18

                        eee = EarlyExitException(18, self.input)
                        raise eee

                    cnt18 += 1




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
    # grammar/ShyRecognizerFrontend.g:107:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID92 = None
        vars_hint93 = None


        ID92_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:107:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:107:14: ID vars_hint
                pass 
                ID92 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1032) 
                stream_ID.add(ID92)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1034)
                vars_hint93 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint93.tree)


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
                # 107:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:107:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:109:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE95 = None
        INDENT96 = None
        NEWLINE97 = None
        NEWLINE99 = None
        DEDENT100 = None
        NEWLINE101 = None
        var_hint94 = None

        var_hint98 = None


        NEWLINE95_tree = None
        INDENT96_tree = None
        NEWLINE97_tree = None
        NEWLINE99_tree = None
        DEDENT100_tree = None
        NEWLINE101_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:110:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:110:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:110:9: ( var_hint )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == CURLY_OPEN or LA19_0 == ID) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:110:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1061)
                    var_hint94 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint94.tree)





                NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1065) 
                stream_NEWLINE.add(NEWLINE95)


                # grammar/ShyRecognizerFrontend.g:111:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == INDENT) :
                    alt21 = 1
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:111:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT96 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1077) 
                    stream_INDENT.add(INDENT96)


                    NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1079) 
                    stream_NEWLINE.add(NEWLINE97)


                    # grammar/ShyRecognizerFrontend.g:111:26: ( var_hint NEWLINE )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == CURLY_OPEN or LA20_0 == ID) :
                            alt20 = 1


                        if alt20 == 1:
                            # grammar/ShyRecognizerFrontend.g:111:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1083)
                            var_hint98 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint98.tree)


                            NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1085) 
                            stream_NEWLINE.add(NEWLINE99)



                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


                    DEDENT100 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1091) 
                    stream_DEDENT.add(DEDENT100)


                    NEWLINE101 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1093) 
                    stream_NEWLINE.add(NEWLINE101)





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
                # 112:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:112:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:114:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE106 = None
        INDENT107 = None
        NEWLINE108 = None
        NEWLINE110 = None
        DEDENT111 = None
        var102 = None

        hint103 = None

        var104 = None

        hint105 = None

        var109 = None


        NEWLINE106_tree = None
        INDENT107_tree = None
        NEWLINE108_tree = None
        NEWLINE110_tree = None
        DEDENT111_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:115:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt26 = 3
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:115:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:115:9: ( var )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == ID) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:115:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1132)
                            var102 = self.var()

                            self._state.following.pop()
                            stream_var.add(var102.tree)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


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
                    # 116:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:116:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:116:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt26 == 2:
                    # grammar/ShyRecognizerFrontend.g:117:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1167)
                    hint103 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint103.tree)


                    # grammar/ShyRecognizerFrontend.g:117:14: ( var )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == ID) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:117:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1169)
                            var104 = self.var()

                            self._state.following.pop()
                            stream_var.add(var104.tree)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


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
                    # 118:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:118:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:118:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt26 == 3:
                    # grammar/ShyRecognizerFrontend.g:119:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1203)
                    hint105 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint105.tree)


                    NEWLINE106 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1205) 
                    stream_NEWLINE.add(NEWLINE106)


                    INDENT107 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1207) 
                    stream_INDENT.add(INDENT107)


                    NEWLINE108 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1209) 
                    stream_NEWLINE.add(NEWLINE108)


                    # grammar/ShyRecognizerFrontend.g:119:37: ( ( var )+ NEWLINE )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == ID) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:119:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:119:39: ( var )+
                            cnt24 = 0
                            while True: #loop24
                                alt24 = 2
                                LA24_0 = self.input.LA(1)

                                if (LA24_0 == ID) :
                                    alt24 = 1


                                if alt24 == 1:
                                    # grammar/ShyRecognizerFrontend.g:119:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1213)
                                    var109 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var109.tree)



                                else:
                                    if cnt24 >= 1:
                                        break #loop24

                                    eee = EarlyExitException(24, self.input)
                                    raise eee

                                cnt24 += 1


                            NEWLINE110 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1217) 
                            stream_NEWLINE.add(NEWLINE110)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    DEDENT111 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1223) 
                    stream_DEDENT.add(DEDENT111)


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
                    # 120:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:120:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:120:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:122:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID112 = None

        ID112_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:122:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:122:7: ID
                pass 
                ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_var1257) 
                stream_ID.add(ID112)


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
                # 122:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:122:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:124:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN113 = None
        ID114 = None
        CURLY_CLOSE115 = None
        CURLY_OPEN116 = None
        ID117 = None
        CURLY_CLOSE119 = None
        hint_arg118 = None


        CURLY_OPEN113_tree = None
        ID114_tree = None
        CURLY_CLOSE115_tree = None
        CURLY_OPEN116_tree = None
        ID117_tree = None
        CURLY_CLOSE119_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:125:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == CURLY_OPEN) :
                    LA28_1 = self.input.LA(2)

                    if (LA28_1 == ID) :
                        LA28_2 = self.input.LA(3)

                        if (LA28_2 == CURLY_CLOSE) :
                            alt28 = 1
                        elif (LA28_2 == ID or LA28_2 == UNDERSCORE) :
                            alt28 = 2
                        else:
                            nvae = NoViableAltException("", 28, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 28, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # grammar/ShyRecognizerFrontend.g:125:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN113 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1282) 
                    stream_CURLY_OPEN.add(CURLY_OPEN113)


                    ID114 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1284) 
                    stream_ID.add(ID114)


                    CURLY_CLOSE115 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1286) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE115)


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
                    # 125:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:125:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt28 == 2:
                    # grammar/ShyRecognizerFrontend.g:126:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN116 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1306) 
                    stream_CURLY_OPEN.add(CURLY_OPEN116)


                    ID117 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1308) 
                    stream_ID.add(ID117)


                    # grammar/ShyRecognizerFrontend.g:126:23: ( hint_arg )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == ID or LA27_0 == UNDERSCORE) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1310)
                            hint_arg118 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg118.tree)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    CURLY_CLOSE119 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1314) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE119)


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
                    # 126:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:126:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:126:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:128:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set120 = None

        set120_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:128:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set120 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set120))

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
    # grammar/ShyRecognizerFrontend.g:130:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS121 = None
        NUMBER122 = None

        MINUS121_tree = None
        NUMBER122_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:130:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:130:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:130:13: ( MINUS )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == MINUS) :
                    alt29 = 1
                if alt29 == 1:
                    # grammar/ShyRecognizerFrontend.g:130:13: MINUS
                    pass 
                    MINUS121 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1353)
                    MINUS121_tree = self._adaptor.createWithPayload(MINUS121)
                    self._adaptor.addChild(root_0, MINUS121_tree)






                NUMBER122 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1357)
                NUMBER122_tree = self._adaptor.createWithPayload(NUMBER122)
                self._adaptor.addChild(root_0, NUMBER122_tree)





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
    # grammar/ShyRecognizerFrontend.g:131:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS123 = None
        NUMBER124 = None
        DIVIDE125 = None
        NUMBER126 = None

        MINUS123_tree = None
        NUMBER124_tree = None
        DIVIDE125_tree = None
        NUMBER126_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:131:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:131:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:131:13: ( MINUS )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == MINUS) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:131:13: MINUS
                    pass 
                    MINUS123 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1365)
                    MINUS123_tree = self._adaptor.createWithPayload(MINUS123)
                    self._adaptor.addChild(root_0, MINUS123_tree)






                NUMBER124 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1369)
                NUMBER124_tree = self._adaptor.createWithPayload(NUMBER124)
                self._adaptor.addChild(root_0, NUMBER124_tree)



                DIVIDE125 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1371)
                DIVIDE125_tree = self._adaptor.createWithPayload(DIVIDE125)
                self._adaptor.addChild(root_0, DIVIDE125_tree)



                NUMBER126 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1373)
                NUMBER126_tree = self._adaptor.createWithPayload(NUMBER126)
                self._adaptor.addChild(root_0, NUMBER126_tree)





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



    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\12\1\uffff\1\17\1\11\1\17\1\11\2\uffff\1\17"
        )

    DFA26_max = DFA.unpack(
        u"\1\17\1\uffff\1\17\1\71\1\24\1\71\2\uffff\1\24"
        )

    DFA26_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA26_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA26_transition = [
        DFA.unpack(u"\1\2\4\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\5\uffff\1\5\51\uffff\1\5"),
        DFA.unpack(u"\1\6\4\uffff\1\7"),
        DFA.unpack(u"\1\10\5\uffff\1\5\51\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\4\uffff\1\7")
    ]

    # class definition for DFA #26

    class DFA26(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 7, 19, 26, 56])
    FOLLOW_stateless_in_start86 = frozenset([1, 7, 19, 26, 56])
    FOLLOW_consts_in_start90 = frozenset([1, 7, 19, 26, 56])
    FOLLOW_types_in_start94 = frozenset([1, 7, 19, 26, 56])
    FOLLOW_MODULE_in_module113 = frozenset([15])
    FOLLOW_ID_in_module115 = frozenset([20])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([15])
    FOLLOW_ID_in_stateless148 = frozenset([20])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1, 17])
    FOLLOW_INDENT_in_stateless154 = frozenset([20])
    FOLLOW_NEWLINE_in_stateless156 = frozenset([24])
    FOLLOW_proc_in_stateless158 = frozenset([11, 24])
    FOLLOW_DEDENT_in_stateless162 = frozenset([20])
    FOLLOW_NEWLINE_in_stateless164 = frozenset([1])
    FOLLOW_PROC_in_proc209 = frozenset([15])
    FOLLOW_ID_in_proc211 = frozenset([20])
    FOLLOW_NEWLINE_in_proc213 = frozenset([1])
    FOLLOW_PROC_in_proc241 = frozenset([15])
    FOLLOW_ID_in_proc243 = frozenset([20])
    FOLLOW_NEWLINE_in_proc245 = frozenset([17])
    FOLLOW_INDENT_in_proc247 = frozenset([20])
    FOLLOW_NEWLINE_in_proc249 = frozenset([4, 11, 22, 58])
    FOLLOW_proc_args_in_proc263 = frozenset([11, 22, 58])
    FOLLOW_proc_vars_in_proc267 = frozenset([11, 22])
    FOLLOW_proc_ops_in_proc271 = frozenset([11])
    FOLLOW_DEDENT_in_proc283 = frozenset([20])
    FOLLOW_NEWLINE_in_proc285 = frozenset([1])
    FOLLOW_ARGS_in_proc_args334 = frozenset([10, 15, 20])
    FOLLOW_vars_hint_in_proc_args336 = frozenset([1])
    FOLLOW_VARS_in_proc_vars365 = frozenset([10, 15, 20])
    FOLLOW_vars_hint_in_proc_vars367 = frozenset([1])
    FOLLOW_OPS_in_proc_ops396 = frozenset([20])
    FOLLOW_NEWLINE_in_proc_ops398 = frozenset([17])
    FOLLOW_INDENT_in_proc_ops400 = frozenset([20])
    FOLLOW_NEWLINE_in_proc_ops402 = frozenset([15, 16])
    FOLLOW_statement_in_proc_ops404 = frozenset([11, 15, 16])
    FOLLOW_DEDENT_in_proc_ops408 = frozenset([20])
    FOLLOW_NEWLINE_in_proc_ops410 = frozenset([1])
    FOLLOW_statement_call_in_statement449 = frozenset([1])
    FOLLOW_statement_if_in_statement459 = frozenset([1])
    FOLLOW_IF_in_statement_if478 = frozenset([15])
    FOLLOW_statement_call_in_statement_if480 = frozenset([13])
    FOLLOW_DO_in_statement_if482 = frozenset([20])
    FOLLOW_NEWLINE_in_statement_if484 = frozenset([17])
    FOLLOW_INDENT_in_statement_if498 = frozenset([20])
    FOLLOW_NEWLINE_in_statement_if500 = frozenset([15, 16])
    FOLLOW_statement_in_statement_if502 = frozenset([11, 15, 16])
    FOLLOW_DEDENT_in_statement_if506 = frozenset([20])
    FOLLOW_NEWLINE_in_statement_if508 = frozenset([1])
    FOLLOW_ID_in_statement_call652 = frozenset([14, 15, 18, 20, 21])
    FOLLOW_statement_call_args_in_statement_call654 = frozenset([20])
    FOLLOW_NEWLINE_in_statement_call658 = frozenset([1, 17])
    FOLLOW_INDENT_in_statement_call671 = frozenset([20])
    FOLLOW_NEWLINE_in_statement_call673 = frozenset([14, 15, 18, 21])
    FOLLOW_statement_call_args_in_statement_call677 = frozenset([20])
    FOLLOW_NEWLINE_in_statement_call679 = frozenset([11, 14, 15, 18, 21])
    FOLLOW_DEDENT_in_statement_call685 = frozenset([20])
    FOLLOW_NEWLINE_in_statement_call687 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args745 = frozenset([1, 14, 15, 18, 21])
    FOLLOW_ID_in_statement_call_arg762 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg772 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg782 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg792 = frozenset([1])
    FOLLOW_CONSTS_in_consts811 = frozenset([15])
    FOLLOW_ID_in_consts813 = frozenset([20])
    FOLLOW_NEWLINE_in_consts815 = frozenset([17])
    FOLLOW_INDENT_in_consts825 = frozenset([20])
    FOLLOW_NEWLINE_in_consts827 = frozenset([15])
    FOLLOW_consts_items_in_consts829 = frozenset([11])
    FOLLOW_DEDENT_in_consts831 = frozenset([20])
    FOLLOW_NEWLINE_in_consts833 = frozenset([1])
    FOLLOW_consts_item_in_consts_items865 = frozenset([1, 15])
    FOLLOW_ID_in_consts_item881 = frozenset([18, 21])
    FOLLOW_num_whole_in_consts_item883 = frozenset([20])
    FOLLOW_NEWLINE_in_consts_item885 = frozenset([1])
    FOLLOW_ID_in_consts_item907 = frozenset([18, 21])
    FOLLOW_num_fract_in_consts_item909 = frozenset([20])
    FOLLOW_NEWLINE_in_consts_item911 = frozenset([1])
    FOLLOW_ID_in_consts_item933 = frozenset([14])
    FOLLOW_EXPRESSION_in_consts_item935 = frozenset([20])
    FOLLOW_NEWLINE_in_consts_item937 = frozenset([1])
    FOLLOW_TYPES_in_types968 = frozenset([15])
    FOLLOW_ID_in_types970 = frozenset([20])
    FOLLOW_NEWLINE_in_types972 = frozenset([17])
    FOLLOW_INDENT_in_types982 = frozenset([20])
    FOLLOW_NEWLINE_in_types984 = frozenset([15])
    FOLLOW_types_items_in_types986 = frozenset([11])
    FOLLOW_DEDENT_in_types988 = frozenset([20])
    FOLLOW_NEWLINE_in_types990 = frozenset([1])
    FOLLOW_types_item_in_types_items1022 = frozenset([1, 15])
    FOLLOW_ID_in_types_item1032 = frozenset([10, 15, 20])
    FOLLOW_vars_hint_in_types_item1034 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1061 = frozenset([20])
    FOLLOW_NEWLINE_in_vars_hint1065 = frozenset([1, 17])
    FOLLOW_INDENT_in_vars_hint1077 = frozenset([20])
    FOLLOW_NEWLINE_in_vars_hint1079 = frozenset([10, 15])
    FOLLOW_var_hint_in_vars_hint1083 = frozenset([20])
    FOLLOW_NEWLINE_in_vars_hint1085 = frozenset([10, 11, 15])
    FOLLOW_DEDENT_in_vars_hint1091 = frozenset([20])
    FOLLOW_NEWLINE_in_vars_hint1093 = frozenset([1])
    FOLLOW_var_in_var_hint1132 = frozenset([1, 15])
    FOLLOW_hint_in_var_hint1167 = frozenset([15])
    FOLLOW_var_in_var_hint1169 = frozenset([1, 15])
    FOLLOW_hint_in_var_hint1203 = frozenset([20])
    FOLLOW_NEWLINE_in_var_hint1205 = frozenset([17])
    FOLLOW_INDENT_in_var_hint1207 = frozenset([20])
    FOLLOW_NEWLINE_in_var_hint1209 = frozenset([15])
    FOLLOW_var_in_var_hint1213 = frozenset([15, 20])
    FOLLOW_NEWLINE_in_var_hint1217 = frozenset([11, 15])
    FOLLOW_DEDENT_in_var_hint1223 = frozenset([1])
    FOLLOW_ID_in_var1257 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1282 = frozenset([15])
    FOLLOW_ID_in_hint1284 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint1286 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1306 = frozenset([15])
    FOLLOW_ID_in_hint1308 = frozenset([15, 57])
    FOLLOW_hint_arg_in_hint1310 = frozenset([9, 15, 57])
    FOLLOW_CURLY_CLOSE_in_hint1314 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1353 = frozenset([21])
    FOLLOW_NUMBER_in_num_whole1357 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1365 = frozenset([21])
    FOLLOW_NUMBER_in_num_fract1369 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1371 = frozenset([21])
    FOLLOW_NUMBER_in_num_fract1373 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
