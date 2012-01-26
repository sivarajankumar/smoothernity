# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-26 19:08:32

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

        self.dfa20 = self.DFA20(
            self, 20,
            eot = self.DFA20_eot,
            eof = self.DFA20_eof,
            min = self.DFA20_min,
            max = self.DFA20_max,
            accept = self.DFA20_accept,
            special = self.DFA20_special,
            transition = self.DFA20_transition
            )

        self.dfa21 = self.DFA21(
            self, 21,
            eot = self.DFA21_eot,
            eof = self.DFA21_eof,
            min = self.DFA21_min,
            max = self.DFA21_max,
            accept = self.DFA21_accept,
            special = self.DFA21_special,
            transition = self.DFA21_transition
            )

        self.dfa37 = self.DFA37(
            self, 37,
            eot = self.DFA37_eot,
            eof = self.DFA37_eof,
            min = self.DFA37_min,
            max = self.DFA37_max,
            accept = self.DFA37_accept,
            special = self.DFA37_special,
            transition = self.DFA37_transition
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
                    # elements: ID, proc_ops, proc_args, proc_vars
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
    # grammar/ShyRecognizerFrontend.g:75:1: statement_if_head : IF condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF47 = None
        NEWLINE49 = None
        DO50 = None
        NEWLINE51 = None
        INDENT52 = None
        NEWLINE53 = None
        DEDENT55 = None
        NEWLINE56 = None
        condition48 = None

        statement54 = None


        IF47_tree = None
        NEWLINE49_tree = None
        DO50_tree = None
        NEWLINE51_tree = None
        INDENT52_tree = None
        NEWLINE53_tree = None
        DEDENT55_tree = None
        NEWLINE56_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:76:5: ( IF condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:76:9: IF condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                IF47 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head636) 
                stream_IF.add(IF47)


                self._state.following.append(self.FOLLOW_condition_in_statement_if_head638)
                condition48 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition48.tree)


                # grammar/ShyRecognizerFrontend.g:76:22: ( NEWLINE )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == NEWLINE) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:76:22: NEWLINE
                    pass 
                    NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head640) 
                    stream_NEWLINE.add(NEWLINE49)





                DO50 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_if_head644) 
                stream_DO.add(DO50)


                NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head646) 
                stream_NEWLINE.add(NEWLINE51)


                INDENT52 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_if_head660) 
                stream_INDENT.add(INDENT52)


                NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head662) 
                stream_NEWLINE.add(NEWLINE53)


                # grammar/ShyRecognizerFrontend.g:77:28: ( statement )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((ID <= LA13_0 <= IF)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:77:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_if_head664)
                        statement54 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement54.tree)



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                DEDENT55 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_if_head668) 
                stream_DEDENT.add(DEDENT55)


                NEWLINE56 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head670) 
                stream_NEWLINE.add(NEWLINE56)


                # AST Rewrite
                # elements: condition, statement
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
                # 78:9: -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:78:13: ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                self._adaptor.addChild(root_1, stream_condition.nextTree())

                # grammar/ShyRecognizerFrontend.g:80:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:80:36: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:84:1: statement_elif : ELIF condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF57 = None
        NEWLINE59 = None
        DO60 = None
        NEWLINE61 = None
        INDENT62 = None
        NEWLINE63 = None
        DEDENT65 = None
        NEWLINE66 = None
        condition58 = None

        statement64 = None


        ELIF57_tree = None
        NEWLINE59_tree = None
        DO60_tree = None
        NEWLINE61_tree = None
        INDENT62_tree = None
        NEWLINE63_tree = None
        DEDENT65_tree = None
        NEWLINE66_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:85:5: ( ELIF condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:85:9: ELIF condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELIF57 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif762) 
                stream_ELIF.add(ELIF57)


                self._state.following.append(self.FOLLOW_condition_in_statement_elif764)
                condition58 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition58.tree)


                # grammar/ShyRecognizerFrontend.g:85:24: ( NEWLINE )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == NEWLINE) :
                    alt14 = 1
                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:85:24: NEWLINE
                    pass 
                    NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif766) 
                    stream_NEWLINE.add(NEWLINE59)





                DO60 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif770) 
                stream_DO.add(DO60)


                NEWLINE61 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif772) 
                stream_NEWLINE.add(NEWLINE61)


                INDENT62 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif786) 
                stream_INDENT.add(INDENT62)


                NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif788) 
                stream_NEWLINE.add(NEWLINE63)


                # grammar/ShyRecognizerFrontend.g:86:28: ( statement )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((ID <= LA15_0 <= IF)) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:86:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_elif790)
                        statement64 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement64.tree)



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                DEDENT65 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif794) 
                stream_DEDENT.add(DEDENT65)


                NEWLINE66 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif796) 
                stream_NEWLINE.add(NEWLINE66)


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
                # 87:9: -> ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:87:13: ^( TREE_STATEMENT_ELIF condition ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                self._adaptor.addChild(root_1, stream_condition.nextTree())

                # grammar/ShyRecognizerFrontend.g:89:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:89:36: ( statement )+
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


    class statement_else_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_else_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerFrontend.g:93:1: statement_else : ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE67 = None
        NEWLINE68 = None
        INDENT69 = None
        NEWLINE70 = None
        DEDENT72 = None
        NEWLINE73 = None
        statement71 = None


        ELSE67_tree = None
        NEWLINE68_tree = None
        INDENT69_tree = None
        NEWLINE70_tree = None
        DEDENT72_tree = None
        NEWLINE73_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:94:5: ( ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:94:9: ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELSE67 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else888) 
                stream_ELSE.add(ELSE67)


                NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else890) 
                stream_NEWLINE.add(NEWLINE68)


                INDENT69 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else904) 
                stream_INDENT.add(INDENT69)


                NEWLINE70 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else906) 
                stream_NEWLINE.add(NEWLINE70)


                # grammar/ShyRecognizerFrontend.g:95:28: ( statement )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((ID <= LA16_0 <= IF)) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:95:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_else908)
                        statement71 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement71.tree)



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1


                DEDENT72 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else912) 
                stream_DEDENT.add(DEDENT72)


                NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else914) 
                stream_NEWLINE.add(NEWLINE73)


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
                # 96:9: -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:96:13: ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:97:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:97:36: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:101:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY75 = None
        ALL77 = None
        condition_call74 = None

        condition_calls76 = None

        condition_calls78 = None


        ANY75_tree = None
        ALL77_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:102:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
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
                    # grammar/ShyRecognizerFrontend.g:102:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition988)
                    condition_call74 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call74.tree)


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
                    # 103:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:103:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:104:9: ANY condition_calls
                    pass 
                    ANY75 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1017) 
                    stream_ANY.add(ANY75)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1019)
                    condition_calls76 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls76.tree)


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
                    # 105:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:105:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 3:
                    # grammar/ShyRecognizerFrontend.g:106:9: ALL condition_calls
                    pass 
                    ALL77 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1048) 
                    stream_ALL.add(ALL77)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1050)
                    condition_calls78 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls78.tree)


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
                    # 107:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:107:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:110:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE80 = None
        INDENT81 = None
        NEWLINE82 = None
        DEDENT84 = None
        NEWLINE85 = None
        condition_call79 = None

        condition_call_line83 = None


        NEWLINE80_tree = None
        INDENT81_tree = None
        NEWLINE82_tree = None
        DEDENT84_tree = None
        NEWLINE85_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:111:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == ID) :
                    alt19 = 1
                elif (LA19_0 == NEWLINE) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:111:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1088)
                    condition_call79 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call79.tree)



                elif alt19 == 2:
                    # grammar/ShyRecognizerFrontend.g:112:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1098) 
                    stream_NEWLINE.add(NEWLINE80)


                    INDENT81 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1100) 
                    stream_INDENT.add(INDENT81)


                    NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1102) 
                    stream_NEWLINE.add(NEWLINE82)


                    # grammar/ShyRecognizerFrontend.g:112:32: ( condition_call_line )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == ID) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerFrontend.g:112:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1104)
                            condition_call_line83 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line83.tree)



                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


                    DEDENT84 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1108) 
                    stream_DEDENT.add(DEDENT84)


                    NEWLINE85 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1110) 
                    stream_NEWLINE.add(NEWLINE85)


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
                    # 113:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:113:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:116:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line86 = None

        statement_call_multi_line87 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:117:5: ( statement_call_single_line | statement_call_multi_line )
                alt20 = 2
                alt20 = self.dfa20.predict(self.input)
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:117:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1144)
                    statement_call_single_line86 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line86.tree)



                elif alt20 == 2:
                    # grammar/ShyRecognizerFrontend.g:118:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1154)
                    statement_call_multi_line87 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line87.tree)



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
    # grammar/ShyRecognizerFrontend.g:121:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE89 = None
        statement_call_single_line88 = None

        statement_call_multi_line90 = None


        NEWLINE89_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:122:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt21 = 2
                alt21 = self.dfa21.predict(self.input)
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:122:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1173)
                    statement_call_single_line88 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line88.tree)


                    NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1175) 
                    stream_NEWLINE.add(NEWLINE89)


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
                    # 123:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt21 == 2:
                    # grammar/ShyRecognizerFrontend.g:124:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1201)
                    statement_call_multi_line90 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line90.tree)



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
    # grammar/ShyRecognizerFrontend.g:127:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID91 = None
        statement_call_args92 = None


        ID91_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:128:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:128:9: ID ( statement_call_args )?
                pass 
                ID91 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1220) 
                stream_ID.add(ID91)


                # grammar/ShyRecognizerFrontend.g:128:12: ( statement_call_args )?
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER) :
                    alt22 = 1
                if alt22 == 1:
                    # grammar/ShyRecognizerFrontend.g:128:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1222)
                    statement_call_args92 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args92.tree)





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
                # 129:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:129:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )? )
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

                # grammar/ShyRecognizerFrontend.g:130:42: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:133:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID93 = None
        NEWLINE95 = None
        INDENT96 = None
        NEWLINE97 = None
        NEWLINE99 = None
        DEDENT100 = None
        NEWLINE101 = None
        statement_call_args94 = None

        statement_call_args98 = None


        ID93_tree = None
        NEWLINE95_tree = None
        INDENT96_tree = None
        NEWLINE97_tree = None
        NEWLINE99_tree = None
        DEDENT100_tree = None
        NEWLINE101_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:134:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:134:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID93 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1284) 
                stream_ID.add(ID93)


                # grammar/ShyRecognizerFrontend.g:134:12: ( statement_call_args )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                    alt23 = 1
                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:134:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1286)
                    statement_call_args94 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args94.tree)





                NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1290) 
                stream_NEWLINE.add(NEWLINE95)


                INDENT96 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1300) 
                stream_INDENT.add(INDENT96)


                NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1302) 
                stream_NEWLINE.add(NEWLINE97)


                # grammar/ShyRecognizerFrontend.g:135:24: ( statement_call_args NEWLINE )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerFrontend.g:135:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1306)
                        statement_call_args98 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args98.tree)


                        NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1308) 
                        stream_NEWLINE.add(NEWLINE99)



                    else:
                        if cnt24 >= 1:
                            break #loop24

                        eee = EarlyExitException(24, self.input)
                        raise eee

                    cnt24 += 1


                DEDENT100 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1314) 
                stream_DEDENT.add(DEDENT100)


                NEWLINE101 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1316) 
                stream_NEWLINE.add(NEWLINE101)


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
                # 136:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:136:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:137:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:140:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg102 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:140:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:140:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:140:23: ( statement_call_arg )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:140:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1370)
                        statement_call_arg102 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg102.tree)



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

    # $ANTLR end "statement_call_args"


    class statement_call_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_arg_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerFrontend.g:142:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID103 = None
        EXPRESSION104 = None
        num_whole105 = None

        num_fract106 = None


        ID103_tree = None
        EXPRESSION104_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:143:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt26 = 4
                LA26 = self.input.LA(1)
                if LA26 == ID:
                    alt26 = 1
                elif LA26 == EXPRESSION:
                    alt26 = 2
                elif LA26 == MINUS:
                    LA26_3 = self.input.LA(2)

                    if (LA26_3 == NUMBER) :
                        LA26_4 = self.input.LA(3)

                        if (LA26_4 == DIVIDE) :
                            alt26 = 4
                        elif (LA26_4 == DO or (EXPRESSION <= LA26_4 <= ID) or LA26_4 == MINUS or (NEWLINE <= LA26_4 <= NUMBER)) :
                            alt26 = 3
                        else:
                            nvae = NoViableAltException("", 26, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 26, 3, self.input)

                        raise nvae


                elif LA26 == NUMBER:
                    LA26_4 = self.input.LA(2)

                    if (LA26_4 == DIVIDE) :
                        alt26 = 4
                    elif (LA26_4 == DO or (EXPRESSION <= LA26_4 <= ID) or LA26_4 == MINUS or (NEWLINE <= LA26_4 <= NUMBER)) :
                        alt26 = 3
                    else:
                        nvae = NoViableAltException("", 26, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:143:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID103 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1387)
                    ID103_tree = self._adaptor.createWithPayload(ID103)
                    self._adaptor.addChild(root_0, ID103_tree)




                elif alt26 == 2:
                    # grammar/ShyRecognizerFrontend.g:144:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION104 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1397)
                    EXPRESSION104_tree = self._adaptor.createWithPayload(EXPRESSION104)
                    self._adaptor.addChild(root_0, EXPRESSION104_tree)




                elif alt26 == 3:
                    # grammar/ShyRecognizerFrontend.g:145:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1407)
                    num_whole105 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole105.tree)



                elif alt26 == 4:
                    # grammar/ShyRecognizerFrontend.g:146:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1417)
                    num_fract106 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract106.tree)



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
    # grammar/ShyRecognizerFrontend.g:149:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS107 = None
        ID108 = None
        NEWLINE109 = None
        INDENT110 = None
        NEWLINE111 = None
        DEDENT113 = None
        NEWLINE114 = None
        consts_items112 = None


        CONSTS107_tree = None
        ID108_tree = None
        NEWLINE109_tree = None
        INDENT110_tree = None
        NEWLINE111_tree = None
        DEDENT113_tree = None
        NEWLINE114_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:150:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:150:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS107 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1436) 
                stream_CONSTS.add(CONSTS107)


                ID108 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1438) 
                stream_ID.add(ID108)


                NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1440) 
                stream_NEWLINE.add(NEWLINE109)


                INDENT110 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1450) 
                stream_INDENT.add(INDENT110)


                NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1452) 
                stream_NEWLINE.add(NEWLINE111)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1454)
                consts_items112 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items112.tree)


                DEDENT113 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1456) 
                stream_DEDENT.add(DEDENT113)


                NEWLINE114 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1458) 
                stream_NEWLINE.add(NEWLINE114)


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
                # 152:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:152:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:154:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item115 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:154:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:154:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:154:16: ( consts_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == ID) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerFrontend.g:154:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1490)
                        consts_item115 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item115.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:155:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID116 = None
        NEWLINE118 = None
        ID119 = None
        NEWLINE121 = None
        ID122 = None
        EXPRESSION123 = None
        NEWLINE124 = None
        num_whole117 = None

        num_fract120 = None


        ID116_tree = None
        NEWLINE118_tree = None
        ID119_tree = None
        NEWLINE121_tree = None
        ID122_tree = None
        EXPRESSION123_tree = None
        NEWLINE124_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:156:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt28 = 3
                LA28_0 = self.input.LA(1)

                if (LA28_0 == ID) :
                    LA28 = self.input.LA(2)
                    if LA28 == EXPRESSION:
                        alt28 = 3
                    elif LA28 == MINUS:
                        LA28_3 = self.input.LA(3)

                        if (LA28_3 == NUMBER) :
                            LA28_4 = self.input.LA(4)

                            if (LA28_4 == DIVIDE) :
                                alt28 = 2
                            elif (LA28_4 == NEWLINE) :
                                alt28 = 1
                            else:
                                nvae = NoViableAltException("", 28, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 28, 3, self.input)

                            raise nvae


                    elif LA28 == NUMBER:
                        LA28_4 = self.input.LA(3)

                        if (LA28_4 == DIVIDE) :
                            alt28 = 2
                        elif (LA28_4 == NEWLINE) :
                            alt28 = 1
                        else:
                            nvae = NoViableAltException("", 28, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 28, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 28, 0, self.input)

                    raise nvae


                if alt28 == 1:
                    # grammar/ShyRecognizerFrontend.g:156:9: ID num_whole NEWLINE
                    pass 
                    ID116 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1506) 
                    stream_ID.add(ID116)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1508)
                    num_whole117 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole117.tree)


                    NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1510) 
                    stream_NEWLINE.add(NEWLINE118)


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
                    # 156:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:156:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt28 == 2:
                    # grammar/ShyRecognizerFrontend.g:157:9: ID num_fract NEWLINE
                    pass 
                    ID119 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1532) 
                    stream_ID.add(ID119)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1534)
                    num_fract120 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract120.tree)


                    NEWLINE121 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1536) 
                    stream_NEWLINE.add(NEWLINE121)


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
                    # 157:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:157:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt28 == 3:
                    # grammar/ShyRecognizerFrontend.g:158:9: ID EXPRESSION NEWLINE
                    pass 
                    ID122 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1558) 
                    stream_ID.add(ID122)


                    EXPRESSION123 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1560) 
                    stream_EXPRESSION.add(EXPRESSION123)


                    NEWLINE124 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1562) 
                    stream_NEWLINE.add(NEWLINE124)


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
                    # 158:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:158:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:161:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES125 = None
        ID126 = None
        NEWLINE127 = None
        INDENT128 = None
        NEWLINE129 = None
        DEDENT131 = None
        NEWLINE132 = None
        types_items130 = None


        TYPES125_tree = None
        ID126_tree = None
        NEWLINE127_tree = None
        INDENT128_tree = None
        NEWLINE129_tree = None
        DEDENT131_tree = None
        NEWLINE132_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:162:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:162:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES125 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1593) 
                stream_TYPES.add(TYPES125)


                ID126 = self.match(self.input, ID, self.FOLLOW_ID_in_types1595) 
                stream_ID.add(ID126)


                NEWLINE127 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1597) 
                stream_NEWLINE.add(NEWLINE127)


                INDENT128 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1607) 
                stream_INDENT.add(INDENT128)


                NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1609) 
                stream_NEWLINE.add(NEWLINE129)


                self._state.following.append(self.FOLLOW_types_items_in_types1611)
                types_items130 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items130.tree)


                DEDENT131 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1613) 
                stream_DEDENT.add(DEDENT131)


                NEWLINE132 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1615) 
                stream_NEWLINE.add(NEWLINE132)


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
                # 164:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:164:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:166:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item133 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:166:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:166:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:166:15: ( types_item )+
                cnt29 = 0
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == ID) :
                        alt29 = 1


                    if alt29 == 1:
                        # grammar/ShyRecognizerFrontend.g:166:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1647)
                        types_item133 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item133.tree)



                    else:
                        if cnt29 >= 1:
                            break #loop29

                        eee = EarlyExitException(29, self.input)
                        raise eee

                    cnt29 += 1




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
    # grammar/ShyRecognizerFrontend.g:167:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID134 = None
        vars_hint135 = None


        ID134_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:167:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:167:14: ID vars_hint
                pass 
                ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1657) 
                stream_ID.add(ID134)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1659)
                vars_hint135 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint135.tree)


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
                # 167:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:167:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:169:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE137 = None
        INDENT138 = None
        NEWLINE139 = None
        NEWLINE141 = None
        DEDENT142 = None
        NEWLINE143 = None
        var_hint136 = None

        var_hint140 = None


        NEWLINE137_tree = None
        INDENT138_tree = None
        NEWLINE139_tree = None
        NEWLINE141_tree = None
        DEDENT142_tree = None
        NEWLINE143_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:170:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:170:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:170:9: ( var_hint )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == CURLY_OPEN or LA30_0 == ID) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:170:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1686)
                    var_hint136 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint136.tree)





                NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1690) 
                stream_NEWLINE.add(NEWLINE137)


                # grammar/ShyRecognizerFrontend.g:171:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == INDENT) :
                    alt32 = 1
                if alt32 == 1:
                    # grammar/ShyRecognizerFrontend.g:171:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT138 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1702) 
                    stream_INDENT.add(INDENT138)


                    NEWLINE139 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1704) 
                    stream_NEWLINE.add(NEWLINE139)


                    # grammar/ShyRecognizerFrontend.g:171:26: ( var_hint NEWLINE )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == CURLY_OPEN or LA31_0 == ID) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:171:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1708)
                            var_hint140 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint140.tree)


                            NEWLINE141 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1710) 
                            stream_NEWLINE.add(NEWLINE141)



                        else:
                            if cnt31 >= 1:
                                break #loop31

                            eee = EarlyExitException(31, self.input)
                            raise eee

                        cnt31 += 1


                    DEDENT142 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1716) 
                    stream_DEDENT.add(DEDENT142)


                    NEWLINE143 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1718) 
                    stream_NEWLINE.add(NEWLINE143)





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
                # 172:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:172:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:174:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE148 = None
        INDENT149 = None
        NEWLINE150 = None
        NEWLINE152 = None
        DEDENT153 = None
        var144 = None

        hint145 = None

        var146 = None

        hint147 = None

        var151 = None


        NEWLINE148_tree = None
        INDENT149_tree = None
        NEWLINE150_tree = None
        NEWLINE152_tree = None
        DEDENT153_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:175:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt37 = 3
                alt37 = self.dfa37.predict(self.input)
                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:175:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:175:9: ( var )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == ID) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerFrontend.g:175:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1757)
                            var144 = self.var()

                            self._state.following.pop()
                            stream_var.add(var144.tree)



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


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
                    # 176:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:176:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:176:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt37 == 2:
                    # grammar/ShyRecognizerFrontend.g:177:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1792)
                    hint145 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint145.tree)


                    # grammar/ShyRecognizerFrontend.g:177:14: ( var )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == ID) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerFrontend.g:177:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1794)
                            var146 = self.var()

                            self._state.following.pop()
                            stream_var.add(var146.tree)



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


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
                    # 178:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:178:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:178:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt37 == 3:
                    # grammar/ShyRecognizerFrontend.g:179:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1828)
                    hint147 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint147.tree)


                    NEWLINE148 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1830) 
                    stream_NEWLINE.add(NEWLINE148)


                    INDENT149 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1832) 
                    stream_INDENT.add(INDENT149)


                    NEWLINE150 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1834) 
                    stream_NEWLINE.add(NEWLINE150)


                    # grammar/ShyRecognizerFrontend.g:179:37: ( ( var )+ NEWLINE )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:179:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:179:39: ( var )+
                            cnt35 = 0
                            while True: #loop35
                                alt35 = 2
                                LA35_0 = self.input.LA(1)

                                if (LA35_0 == ID) :
                                    alt35 = 1


                                if alt35 == 1:
                                    # grammar/ShyRecognizerFrontend.g:179:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1838)
                                    var151 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var151.tree)



                                else:
                                    if cnt35 >= 1:
                                        break #loop35

                                    eee = EarlyExitException(35, self.input)
                                    raise eee

                                cnt35 += 1


                            NEWLINE152 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1842) 
                            stream_NEWLINE.add(NEWLINE152)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


                    DEDENT153 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1848) 
                    stream_DEDENT.add(DEDENT153)


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
                    # 180:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:180:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:180:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:182:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID154 = None

        ID154_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:182:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:182:7: ID
                pass 
                ID154 = self.match(self.input, ID, self.FOLLOW_ID_in_var1882) 
                stream_ID.add(ID154)


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
                # 182:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:182:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:184:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN155 = None
        ID156 = None
        CURLY_CLOSE157 = None
        CURLY_OPEN158 = None
        ID159 = None
        CURLY_CLOSE161 = None
        hint_arg160 = None


        CURLY_OPEN155_tree = None
        ID156_tree = None
        CURLY_CLOSE157_tree = None
        CURLY_OPEN158_tree = None
        ID159_tree = None
        CURLY_CLOSE161_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:185:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == CURLY_OPEN) :
                    LA39_1 = self.input.LA(2)

                    if (LA39_1 == ID) :
                        LA39_2 = self.input.LA(3)

                        if (LA39_2 == CURLY_CLOSE) :
                            alt39 = 1
                        elif (LA39_2 == ID or LA39_2 == UNDERSCORE) :
                            alt39 = 2
                        else:
                            nvae = NoViableAltException("", 39, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 39, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae


                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:185:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN155 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1907) 
                    stream_CURLY_OPEN.add(CURLY_OPEN155)


                    ID156 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1909) 
                    stream_ID.add(ID156)


                    CURLY_CLOSE157 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1911) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE157)


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
                    # 185:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:185:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:186:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN158 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1931) 
                    stream_CURLY_OPEN.add(CURLY_OPEN158)


                    ID159 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1933) 
                    stream_ID.add(ID159)


                    # grammar/ShyRecognizerFrontend.g:186:23: ( hint_arg )+
                    cnt38 = 0
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == ID or LA38_0 == UNDERSCORE) :
                            alt38 = 1


                        if alt38 == 1:
                            # grammar/ShyRecognizerFrontend.g:186:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1935)
                            hint_arg160 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg160.tree)



                        else:
                            if cnt38 >= 1:
                                break #loop38

                            eee = EarlyExitException(38, self.input)
                            raise eee

                        cnt38 += 1


                    CURLY_CLOSE161 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1939) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE161)


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
                    # 186:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:186:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:186:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:188:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set162 = None

        set162_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:188:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set162 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set162))

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
    # grammar/ShyRecognizerFrontend.g:190:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS163 = None
        NUMBER164 = None

        MINUS163_tree = None
        NUMBER164_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:190:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:190:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:190:13: ( MINUS )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == MINUS) :
                    alt40 = 1
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:190:13: MINUS
                    pass 
                    MINUS163 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1978)
                    MINUS163_tree = self._adaptor.createWithPayload(MINUS163)
                    self._adaptor.addChild(root_0, MINUS163_tree)






                NUMBER164 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1982)
                NUMBER164_tree = self._adaptor.createWithPayload(NUMBER164)
                self._adaptor.addChild(root_0, NUMBER164_tree)





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
    # grammar/ShyRecognizerFrontend.g:191:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS165 = None
        NUMBER166 = None
        DIVIDE167 = None
        NUMBER168 = None

        MINUS165_tree = None
        NUMBER166_tree = None
        DIVIDE167_tree = None
        NUMBER168_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:191:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:191:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:191:13: ( MINUS )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == MINUS) :
                    alt41 = 1
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:191:13: MINUS
                    pass 
                    MINUS165 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1990)
                    MINUS165_tree = self._adaptor.createWithPayload(MINUS165)
                    self._adaptor.addChild(root_0, MINUS165_tree)






                NUMBER166 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1994)
                NUMBER166_tree = self._adaptor.createWithPayload(NUMBER166)
                self._adaptor.addChild(root_0, NUMBER166_tree)



                DIVIDE167 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1996)
                DIVIDE167_tree = self._adaptor.createWithPayload(DIVIDE167)
                self._adaptor.addChild(root_0, DIVIDE167_tree)



                NUMBER168 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1998)
                NUMBER168_tree = self._adaptor.createWithPayload(NUMBER168)
                self._adaptor.addChild(root_0, NUMBER168_tree)





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


    # lookup tables for DFA #20

    DFA20_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA20_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA20_min = DFA.unpack(
        u"\1\23\3\17\1\31\1\16\1\17\1\uffff\1\31\1\uffff\1\17"
        )

    DFA20_max = DFA.unpack(
        u"\1\23\5\31\1\25\1\uffff\1\31\1\uffff\1\31"
        )

    DFA20_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA20_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA20_transition = [
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

    # class definition for DFA #20

    class DFA20(DFA):
        pass


    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\1\23\3\22\1\31\1\16\1\15\1\31\2\uffff\1\22"
        )

    DFA21_max = DFA.unpack(
        u"\1\23\5\31\1\25\1\31\2\uffff\1\31"
        )

    DFA21_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA21_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA21_transition = [
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

    # class definition for DFA #21

    class DFA21(DFA):
        pass


    # lookup tables for DFA #37

    DFA37_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA37_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA37_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA37_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\77\1\30\1\77\2\uffff\1\30"
        )

    DFA37_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA37_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA37_transition = [
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

    # class definition for DFA #37

    class DFA37(DFA):
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
    FOLLOW_statement_call_single_line_in_statement449 = frozenset([24])
    FOLLOW_NEWLINE_in_statement451 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement477 = frozenset([1])
    FOLLOW_statement_if_in_statement487 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if506 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if516 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if528 = frozenset([1])
    FOLLOW_IF_in_statement_if_head636 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_if_head638 = frozenset([15, 24])
    FOLLOW_NEWLINE_in_statement_if_head640 = frozenset([15])
    FOLLOW_DO_in_statement_if_head644 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_if_head646 = frozenset([21])
    FOLLOW_INDENT_in_statement_if_head660 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_if_head662 = frozenset([19, 20])
    FOLLOW_statement_in_statement_if_head664 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_if_head668 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_if_head670 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif762 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_elif764 = frozenset([15, 24])
    FOLLOW_NEWLINE_in_statement_elif766 = frozenset([15])
    FOLLOW_DO_in_statement_elif770 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif772 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif786 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif788 = frozenset([19, 20])
    FOLLOW_statement_in_statement_elif790 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_elif794 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_elif796 = frozenset([1])
    FOLLOW_ELSE_in_statement_else888 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else890 = frozenset([21])
    FOLLOW_INDENT_in_statement_else904 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else906 = frozenset([19, 20])
    FOLLOW_statement_in_statement_else908 = frozenset([13, 19, 20])
    FOLLOW_DEDENT_in_statement_else912 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_else914 = frozenset([1])
    FOLLOW_condition_call_in_condition988 = frozenset([1])
    FOLLOW_ANY_in_condition1017 = frozenset([19, 24])
    FOLLOW_condition_calls_in_condition1019 = frozenset([1])
    FOLLOW_ALL_in_condition1048 = frozenset([19, 24])
    FOLLOW_condition_calls_in_condition1050 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1088 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1098 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1100 = frozenset([24])
    FOLLOW_NEWLINE_in_condition_calls1102 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1104 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1108 = frozenset([24])
    FOLLOW_NEWLINE_in_condition_calls1110 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1144 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1154 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1173 = frozenset([24])
    FOLLOW_NEWLINE_in_condition_call_line1175 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1201 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1220 = frozenset([1, 18, 19, 22, 25])
    FOLLOW_statement_call_args_in_statement_call_single_line1222 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1284 = frozenset([18, 19, 22, 24, 25])
    FOLLOW_statement_call_args_in_statement_call_multi_line1286 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1290 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1300 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1302 = frozenset([18, 19, 22, 25])
    FOLLOW_statement_call_args_in_statement_call_multi_line1306 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1308 = frozenset([13, 18, 19, 22, 25])
    FOLLOW_DEDENT_in_statement_call_multi_line1314 = frozenset([24])
    FOLLOW_NEWLINE_in_statement_call_multi_line1316 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args1370 = frozenset([1, 18, 19, 22, 25])
    FOLLOW_ID_in_statement_call_arg1387 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1397 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1407 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1417 = frozenset([1])
    FOLLOW_CONSTS_in_consts1436 = frozenset([19])
    FOLLOW_ID_in_consts1438 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1440 = frozenset([21])
    FOLLOW_INDENT_in_consts1450 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1452 = frozenset([19])
    FOLLOW_consts_items_in_consts1454 = frozenset([13])
    FOLLOW_DEDENT_in_consts1456 = frozenset([24])
    FOLLOW_NEWLINE_in_consts1458 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1490 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1506 = frozenset([22, 25])
    FOLLOW_num_whole_in_consts_item1508 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1510 = frozenset([1])
    FOLLOW_ID_in_consts_item1532 = frozenset([22, 25])
    FOLLOW_num_fract_in_consts_item1534 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1536 = frozenset([1])
    FOLLOW_ID_in_consts_item1558 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1560 = frozenset([24])
    FOLLOW_NEWLINE_in_consts_item1562 = frozenset([1])
    FOLLOW_TYPES_in_types1593 = frozenset([19])
    FOLLOW_ID_in_types1595 = frozenset([24])
    FOLLOW_NEWLINE_in_types1597 = frozenset([21])
    FOLLOW_INDENT_in_types1607 = frozenset([24])
    FOLLOW_NEWLINE_in_types1609 = frozenset([19])
    FOLLOW_types_items_in_types1611 = frozenset([13])
    FOLLOW_DEDENT_in_types1613 = frozenset([24])
    FOLLOW_NEWLINE_in_types1615 = frozenset([1])
    FOLLOW_types_item_in_types_items1647 = frozenset([1, 19])
    FOLLOW_ID_in_types_item1657 = frozenset([12, 19, 24])
    FOLLOW_vars_hint_in_types_item1659 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1686 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1690 = frozenset([1, 21])
    FOLLOW_INDENT_in_vars_hint1702 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1704 = frozenset([12, 19])
    FOLLOW_var_hint_in_vars_hint1708 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1710 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_vars_hint1716 = frozenset([24])
    FOLLOW_NEWLINE_in_vars_hint1718 = frozenset([1])
    FOLLOW_var_in_var_hint1757 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1792 = frozenset([19])
    FOLLOW_var_in_var_hint1794 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1828 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1830 = frozenset([21])
    FOLLOW_INDENT_in_var_hint1832 = frozenset([24])
    FOLLOW_NEWLINE_in_var_hint1834 = frozenset([19])
    FOLLOW_var_in_var_hint1838 = frozenset([19, 24])
    FOLLOW_NEWLINE_in_var_hint1842 = frozenset([13, 19])
    FOLLOW_DEDENT_in_var_hint1848 = frozenset([1])
    FOLLOW_ID_in_var1882 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1907 = frozenset([19])
    FOLLOW_ID_in_hint1909 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint1911 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1931 = frozenset([19])
    FOLLOW_ID_in_hint1933 = frozenset([19, 63])
    FOLLOW_hint_arg_in_hint1935 = frozenset([11, 19, 63])
    FOLLOW_CURLY_CLOSE_in_hint1939 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1978 = frozenset([25])
    FOLLOW_NUMBER_in_num_whole1982 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1990 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1994 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract1996 = frozenset([25])
    FOLLOW_NUMBER_in_num_fract1998 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
