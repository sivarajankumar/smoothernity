# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-24 20:19:19

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
ELSE=14
EXPRESSION=15
ID=16
IF=17
INDENT=18
MINUS=19
MODULE=20
NEWLINE=21
NUMBER=22
OPS=23
PASTE=24
PROC=25
REPLACE=26
STATELESS=27
STRING=28
TREE_ARBITRARY_TOKEN=29
TREE_CONDITION_ANY=30
TREE_CONSTS=31
TREE_COPY=32
TREE_COPY_PASTE=33
TREE_EXPRESSION=34
TREE_HINT=35
TREE_HINT_NONE=36
TREE_MODULE=37
TREE_NUM_FRACT=38
TREE_NUM_WHOLE=39
TREE_PASTE=40
TREE_PASTE_REPLACE=41
TREE_PASTE_WITH=42
TREE_PROC=43
TREE_PROC_ARGS=44
TREE_PROC_VARS=45
TREE_STATELESS=46
TREE_STATEMENTS=47
TREE_STATEMENT_CALL=48
TREE_STATEMENT_CALL_ARGS=49
TREE_STATEMENT_ELIF=50
TREE_STATEMENT_ELSE=51
TREE_STATEMENT_IF=52
TREE_TYPES=53
TREE_TYPES_ITEM=54
TREE_VAR=55
TREE_VARS_HINT=56
TREE_VAR_HINT=57
TYPES=58
UNDERSCORE=59
VARS=60
WHITESPACE=61
WITH=62

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELSE", "EXPRESSION", "ID", 
    "IF", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", "OPS", "PASTE", 
    "PROC", "REPLACE", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_CALL_ARGS", "TREE_STATEMENT_ELIF", 
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

        self.dfa30 = self.DFA30(
            self, 30,
            eot = self.DFA30_eot,
            eof = self.DFA30_eof,
            min = self.DFA30_min,
            max = self.DFA30_max,
            accept = self.DFA30_accept,
            special = self.DFA30_special,
            transition = self.DFA30_transition
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
                    # elements: proc_ops, proc_args, ID, proc_vars
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
    # grammar/ShyRecognizerFrontend.g:62:1: statement_if : statement_if_head ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head42 = None

        statement_else43 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:63:5: ( statement_if_head ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:63:9: statement_if_head ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if478)
                statement_if_head42 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head42.tree)


                # grammar/ShyRecognizerFrontend.g:64:9: ( statement_else )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == ELSE) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerFrontend.g:64:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if488)
                    statement_else43 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else43.tree)





                # AST Rewrite
                # elements: statement_else, statement_if_head
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
                # 65:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:65:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:67:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:71:1: statement_if_head : IF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF44 = None
        DO46 = None
        NEWLINE47 = None
        INDENT48 = None
        NEWLINE49 = None
        DEDENT51 = None
        NEWLINE52 = None
        statement_call45 = None

        statement50 = None


        IF44_tree = None
        DO46_tree = None
        NEWLINE47_tree = None
        INDENT48_tree = None
        NEWLINE49_tree = None
        DEDENT51_tree = None
        NEWLINE52_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statement_call = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:72:5: ( IF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:72:9: IF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                IF44 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head576) 
                stream_IF.add(IF44)


                self._state.following.append(self.FOLLOW_statement_call_in_statement_if_head578)
                statement_call45 = self.statement_call()

                self._state.following.pop()
                stream_statement_call.add(statement_call45.tree)


                # grammar/ShyRecognizerFrontend.g:72:27: ( DO )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == DO) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerFrontend.g:72:27: DO
                    pass 
                    DO46 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_if_head580) 
                    stream_DO.add(DO46)





                NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head584) 
                stream_NEWLINE.add(NEWLINE47)


                INDENT48 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_if_head598) 
                stream_INDENT.add(INDENT48)


                NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head600) 
                stream_NEWLINE.add(NEWLINE49)


                # grammar/ShyRecognizerFrontend.g:73:28: ( statement )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((ID <= LA12_0 <= IF)) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:73:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_if_head602)
                        statement50 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement50.tree)



                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1


                DEDENT51 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_if_head606) 
                stream_DEDENT.add(DEDENT51)


                NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head608) 
                stream_NEWLINE.add(NEWLINE52)


                # AST Rewrite
                # elements: statement_call, statement
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
                # 74:9: -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:74:13: ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:75:17: ^( TREE_CONDITION_ANY statement_call )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                , root_2)

                self._adaptor.addChild(root_2, stream_statement_call.nextTree())

                self._adaptor.addChild(root_1, root_2)

                # grammar/ShyRecognizerFrontend.g:76:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:76:36: ( statement )+
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


    class statement_else_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_else_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerFrontend.g:80:1: statement_else : ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE53 = None
        NEWLINE54 = None
        INDENT55 = None
        NEWLINE56 = None
        DEDENT58 = None
        NEWLINE59 = None
        statement57 = None


        ELSE53_tree = None
        NEWLINE54_tree = None
        INDENT55_tree = None
        NEWLINE56_tree = None
        DEDENT58_tree = None
        NEWLINE59_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:81:5: ( ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:81:9: ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELSE53 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else706) 
                stream_ELSE.add(ELSE53)


                NEWLINE54 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else708) 
                stream_NEWLINE.add(NEWLINE54)


                INDENT55 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else722) 
                stream_INDENT.add(INDENT55)


                NEWLINE56 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else724) 
                stream_NEWLINE.add(NEWLINE56)


                # grammar/ShyRecognizerFrontend.g:82:28: ( statement )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((ID <= LA13_0 <= IF)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:82:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_else726)
                        statement57 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement57.tree)



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                DEDENT58 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else730) 
                stream_DEDENT.add(DEDENT58)


                NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else732) 
                stream_NEWLINE.add(NEWLINE59)


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
                # 83:9: -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:83:13: ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:84:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:84:36: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:88:1: statement_call : ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID60 = None
        DO62 = None
        NEWLINE63 = None
        INDENT64 = None
        NEWLINE65 = None
        NEWLINE67 = None
        DEDENT68 = None
        NEWLINE69 = None
        statement_call_args61 = None

        statement_call_args66 = None


        ID60_tree = None
        DO62_tree = None
        NEWLINE63_tree = None
        INDENT64_tree = None
        NEWLINE65_tree = None
        NEWLINE67_tree = None
        DEDENT68_tree = None
        NEWLINE69_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:89:5: ( ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:89:9: ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call806) 
                stream_ID.add(ID60)


                # grammar/ShyRecognizerFrontend.g:89:12: ( statement_call_args )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((EXPRESSION <= LA14_0 <= ID) or LA14_0 == MINUS or LA14_0 == NUMBER) :
                    alt14 = 1
                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:89:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call808)
                    statement_call_args61 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args61.tree)





                # grammar/ShyRecognizerFrontend.g:89:34: ( DO | NEWLINE )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == DO) :
                    alt15 = 1
                elif (LA15_0 == NEWLINE) :
                    alt15 = 2
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:89:36: DO
                    pass 
                    DO62 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_call814) 
                    stream_DO.add(DO62)



                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:89:41: NEWLINE
                    pass 
                    NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call818) 
                    stream_NEWLINE.add(NEWLINE63)





                # grammar/ShyRecognizerFrontend.g:90:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == INDENT) :
                    alt17 = 1
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:90:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT64 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call832) 
                    stream_INDENT.add(INDENT64)


                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call834) 
                    stream_NEWLINE.add(NEWLINE65)


                    # grammar/ShyRecognizerFrontend.g:90:26: ( statement_call_args NEWLINE )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA16_0 <= ID) or LA16_0 == MINUS or LA16_0 == NUMBER) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:90:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call838)
                            statement_call_args66 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args66.tree)


                            NEWLINE67 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call840) 
                            stream_NEWLINE.add(NEWLINE67)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    DEDENT68 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call846) 
                    stream_DEDENT.add(DEDENT68)


                    NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call848) 
                    stream_NEWLINE.add(NEWLINE69)





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
                # 91:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:91:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:92:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:95:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg70 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:95:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:95:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:95:23: ( statement_call_arg )+
                cnt18 = 0
                while True: #loop18
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA18_0 <= ID) or LA18_0 == MINUS or LA18_0 == NUMBER) :
                        alt18 = 1


                    if alt18 == 1:
                        # grammar/ShyRecognizerFrontend.g:95:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args906)
                        statement_call_arg70 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg70.tree)



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

    # $ANTLR end "statement_call_args"


    class statement_call_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_arg_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerFrontend.g:97:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID71 = None
        EXPRESSION72 = None
        num_whole73 = None

        num_fract74 = None


        ID71_tree = None
        EXPRESSION72_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:98:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt19 = 4
                LA19 = self.input.LA(1)
                if LA19 == ID:
                    alt19 = 1
                elif LA19 == EXPRESSION:
                    alt19 = 2
                elif LA19 == MINUS:
                    LA19_3 = self.input.LA(2)

                    if (LA19_3 == NUMBER) :
                        LA19_4 = self.input.LA(3)

                        if (LA19_4 == DIVIDE) :
                            alt19 = 4
                        elif (LA19_4 == DO or (EXPRESSION <= LA19_4 <= ID) or LA19_4 == MINUS or (NEWLINE <= LA19_4 <= NUMBER)) :
                            alt19 = 3
                        else:
                            nvae = NoViableAltException("", 19, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 19, 3, self.input)

                        raise nvae


                elif LA19 == NUMBER:
                    LA19_4 = self.input.LA(2)

                    if (LA19_4 == DIVIDE) :
                        alt19 = 4
                    elif (LA19_4 == DO or (EXPRESSION <= LA19_4 <= ID) or LA19_4 == MINUS or (NEWLINE <= LA19_4 <= NUMBER)) :
                        alt19 = 3
                    else:
                        nvae = NoViableAltException("", 19, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:98:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID71 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg923)
                    ID71_tree = self._adaptor.createWithPayload(ID71)
                    self._adaptor.addChild(root_0, ID71_tree)




                elif alt19 == 2:
                    # grammar/ShyRecognizerFrontend.g:99:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION72 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg933)
                    EXPRESSION72_tree = self._adaptor.createWithPayload(EXPRESSION72)
                    self._adaptor.addChild(root_0, EXPRESSION72_tree)




                elif alt19 == 3:
                    # grammar/ShyRecognizerFrontend.g:100:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg943)
                    num_whole73 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole73.tree)



                elif alt19 == 4:
                    # grammar/ShyRecognizerFrontend.g:101:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg953)
                    num_fract74 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract74.tree)



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
    # grammar/ShyRecognizerFrontend.g:104:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS75 = None
        ID76 = None
        NEWLINE77 = None
        INDENT78 = None
        NEWLINE79 = None
        DEDENT81 = None
        NEWLINE82 = None
        consts_items80 = None


        CONSTS75_tree = None
        ID76_tree = None
        NEWLINE77_tree = None
        INDENT78_tree = None
        NEWLINE79_tree = None
        DEDENT81_tree = None
        NEWLINE82_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:105:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:105:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS75 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts972) 
                stream_CONSTS.add(CONSTS75)


                ID76 = self.match(self.input, ID, self.FOLLOW_ID_in_consts974) 
                stream_ID.add(ID76)


                NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts976) 
                stream_NEWLINE.add(NEWLINE77)


                INDENT78 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts986) 
                stream_INDENT.add(INDENT78)


                NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts988) 
                stream_NEWLINE.add(NEWLINE79)


                self._state.following.append(self.FOLLOW_consts_items_in_consts990)
                consts_items80 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items80.tree)


                DEDENT81 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts992) 
                stream_DEDENT.add(DEDENT81)


                NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts994) 
                stream_NEWLINE.add(NEWLINE82)


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
                # 107:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:107:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:109:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item83 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:109:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:109:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:109:16: ( consts_item )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == ID) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerFrontend.g:109:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1026)
                        consts_item83 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item83.tree)



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1




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
    # grammar/ShyRecognizerFrontend.g:110:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID84 = None
        NEWLINE86 = None
        ID87 = None
        NEWLINE89 = None
        ID90 = None
        EXPRESSION91 = None
        NEWLINE92 = None
        num_whole85 = None

        num_fract88 = None


        ID84_tree = None
        NEWLINE86_tree = None
        ID87_tree = None
        NEWLINE89_tree = None
        ID90_tree = None
        EXPRESSION91_tree = None
        NEWLINE92_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:111:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt21 = 3
                LA21_0 = self.input.LA(1)

                if (LA21_0 == ID) :
                    LA21 = self.input.LA(2)
                    if LA21 == EXPRESSION:
                        alt21 = 3
                    elif LA21 == MINUS:
                        LA21_3 = self.input.LA(3)

                        if (LA21_3 == NUMBER) :
                            LA21_4 = self.input.LA(4)

                            if (LA21_4 == DIVIDE) :
                                alt21 = 2
                            elif (LA21_4 == NEWLINE) :
                                alt21 = 1
                            else:
                                nvae = NoViableAltException("", 21, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 21, 3, self.input)

                            raise nvae


                    elif LA21 == NUMBER:
                        LA21_4 = self.input.LA(3)

                        if (LA21_4 == DIVIDE) :
                            alt21 = 2
                        elif (LA21_4 == NEWLINE) :
                            alt21 = 1
                        else:
                            nvae = NoViableAltException("", 21, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 21, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae


                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:111:9: ID num_whole NEWLINE
                    pass 
                    ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1042) 
                    stream_ID.add(ID84)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1044)
                    num_whole85 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole85.tree)


                    NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1046) 
                    stream_NEWLINE.add(NEWLINE86)


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
                    # 111:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:111:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt21 == 2:
                    # grammar/ShyRecognizerFrontend.g:112:9: ID num_fract NEWLINE
                    pass 
                    ID87 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1068) 
                    stream_ID.add(ID87)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1070)
                    num_fract88 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract88.tree)


                    NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1072) 
                    stream_NEWLINE.add(NEWLINE89)


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
                    # 112:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:112:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt21 == 3:
                    # grammar/ShyRecognizerFrontend.g:113:9: ID EXPRESSION NEWLINE
                    pass 
                    ID90 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1094) 
                    stream_ID.add(ID90)


                    EXPRESSION91 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1096) 
                    stream_EXPRESSION.add(EXPRESSION91)


                    NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1098) 
                    stream_NEWLINE.add(NEWLINE92)


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
                    # 113:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:113:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:116:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES93 = None
        ID94 = None
        NEWLINE95 = None
        INDENT96 = None
        NEWLINE97 = None
        DEDENT99 = None
        NEWLINE100 = None
        types_items98 = None


        TYPES93_tree = None
        ID94_tree = None
        NEWLINE95_tree = None
        INDENT96_tree = None
        NEWLINE97_tree = None
        DEDENT99_tree = None
        NEWLINE100_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:117:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:117:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES93 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1129) 
                stream_TYPES.add(TYPES93)


                ID94 = self.match(self.input, ID, self.FOLLOW_ID_in_types1131) 
                stream_ID.add(ID94)


                NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1133) 
                stream_NEWLINE.add(NEWLINE95)


                INDENT96 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1143) 
                stream_INDENT.add(INDENT96)


                NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1145) 
                stream_NEWLINE.add(NEWLINE97)


                self._state.following.append(self.FOLLOW_types_items_in_types1147)
                types_items98 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items98.tree)


                DEDENT99 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1149) 
                stream_DEDENT.add(DEDENT99)


                NEWLINE100 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1151) 
                stream_NEWLINE.add(NEWLINE100)


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
                # 119:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:119:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:121:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item101 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:121:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:121:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:121:15: ( types_item )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == ID) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerFrontend.g:121:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1183)
                        types_item101 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item101.tree)



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1




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
    # grammar/ShyRecognizerFrontend.g:122:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID102 = None
        vars_hint103 = None


        ID102_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:122:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:122:14: ID vars_hint
                pass 
                ID102 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1193) 
                stream_ID.add(ID102)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1195)
                vars_hint103 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint103.tree)


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
                # 122:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:122:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:124:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE105 = None
        INDENT106 = None
        NEWLINE107 = None
        NEWLINE109 = None
        DEDENT110 = None
        NEWLINE111 = None
        var_hint104 = None

        var_hint108 = None


        NEWLINE105_tree = None
        INDENT106_tree = None
        NEWLINE107_tree = None
        NEWLINE109_tree = None
        DEDENT110_tree = None
        NEWLINE111_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:125:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:125:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:125:9: ( var_hint )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == CURLY_OPEN or LA23_0 == ID) :
                    alt23 = 1
                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:125:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1222)
                    var_hint104 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint104.tree)





                NEWLINE105 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1226) 
                stream_NEWLINE.add(NEWLINE105)


                # grammar/ShyRecognizerFrontend.g:126:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == INDENT) :
                    alt25 = 1
                if alt25 == 1:
                    # grammar/ShyRecognizerFrontend.g:126:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT106 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1238) 
                    stream_INDENT.add(INDENT106)


                    NEWLINE107 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1240) 
                    stream_NEWLINE.add(NEWLINE107)


                    # grammar/ShyRecognizerFrontend.g:126:26: ( var_hint NEWLINE )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == CURLY_OPEN or LA24_0 == ID) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1244)
                            var_hint108 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint108.tree)


                            NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1246) 
                            stream_NEWLINE.add(NEWLINE109)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    DEDENT110 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1252) 
                    stream_DEDENT.add(DEDENT110)


                    NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1254) 
                    stream_NEWLINE.add(NEWLINE111)





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
                # 127:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:127:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:129:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE116 = None
        INDENT117 = None
        NEWLINE118 = None
        NEWLINE120 = None
        DEDENT121 = None
        var112 = None

        hint113 = None

        var114 = None

        hint115 = None

        var119 = None


        NEWLINE116_tree = None
        INDENT117_tree = None
        NEWLINE118_tree = None
        NEWLINE120_tree = None
        DEDENT121_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:130:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt30 = 3
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:130:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:130:9: ( var )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == ID) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:130:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1293)
                            var112 = self.var()

                            self._state.following.pop()
                            stream_var.add(var112.tree)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


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
                    # 131:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:131:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:131:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt30 == 2:
                    # grammar/ShyRecognizerFrontend.g:132:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1328)
                    hint113 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint113.tree)


                    # grammar/ShyRecognizerFrontend.g:132:14: ( var )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == ID) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:132:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1330)
                            var114 = self.var()

                            self._state.following.pop()
                            stream_var.add(var114.tree)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


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
                    # 133:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:133:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:133:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt30 == 3:
                    # grammar/ShyRecognizerFrontend.g:134:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1364)
                    hint115 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint115.tree)


                    NEWLINE116 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1366) 
                    stream_NEWLINE.add(NEWLINE116)


                    INDENT117 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1368) 
                    stream_INDENT.add(INDENT117)


                    NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1370) 
                    stream_NEWLINE.add(NEWLINE118)


                    # grammar/ShyRecognizerFrontend.g:134:37: ( ( var )+ NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:134:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:134:39: ( var )+
                            cnt28 = 0
                            while True: #loop28
                                alt28 = 2
                                LA28_0 = self.input.LA(1)

                                if (LA28_0 == ID) :
                                    alt28 = 1


                                if alt28 == 1:
                                    # grammar/ShyRecognizerFrontend.g:134:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1374)
                                    var119 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var119.tree)



                                else:
                                    if cnt28 >= 1:
                                        break #loop28

                                    eee = EarlyExitException(28, self.input)
                                    raise eee

                                cnt28 += 1


                            NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1378) 
                            stream_NEWLINE.add(NEWLINE120)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT121 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1384) 
                    stream_DEDENT.add(DEDENT121)


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
                    # 135:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:135:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:135:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:137:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID122 = None

        ID122_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:137:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:137:7: ID
                pass 
                ID122 = self.match(self.input, ID, self.FOLLOW_ID_in_var1418) 
                stream_ID.add(ID122)


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
                # 137:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:137:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:139:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN123 = None
        ID124 = None
        CURLY_CLOSE125 = None
        CURLY_OPEN126 = None
        ID127 = None
        CURLY_CLOSE129 = None
        hint_arg128 = None


        CURLY_OPEN123_tree = None
        ID124_tree = None
        CURLY_CLOSE125_tree = None
        CURLY_OPEN126_tree = None
        ID127_tree = None
        CURLY_CLOSE129_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:140:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == CURLY_OPEN) :
                    LA32_1 = self.input.LA(2)

                    if (LA32_1 == ID) :
                        LA32_2 = self.input.LA(3)

                        if (LA32_2 == CURLY_CLOSE) :
                            alt32 = 1
                        elif (LA32_2 == ID or LA32_2 == UNDERSCORE) :
                            alt32 = 2
                        else:
                            nvae = NoViableAltException("", 32, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 32, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 32, 0, self.input)

                    raise nvae


                if alt32 == 1:
                    # grammar/ShyRecognizerFrontend.g:140:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN123 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1443) 
                    stream_CURLY_OPEN.add(CURLY_OPEN123)


                    ID124 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1445) 
                    stream_ID.add(ID124)


                    CURLY_CLOSE125 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1447) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE125)


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
                    # 140:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:140:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt32 == 2:
                    # grammar/ShyRecognizerFrontend.g:141:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN126 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1467) 
                    stream_CURLY_OPEN.add(CURLY_OPEN126)


                    ID127 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1469) 
                    stream_ID.add(ID127)


                    # grammar/ShyRecognizerFrontend.g:141:23: ( hint_arg )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == ID or LA31_0 == UNDERSCORE) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:141:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1471)
                            hint_arg128 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg128.tree)



                        else:
                            if cnt31 >= 1:
                                break #loop31

                            eee = EarlyExitException(31, self.input)
                            raise eee

                        cnt31 += 1


                    CURLY_CLOSE129 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1475) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE129)


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
                    # 141:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:141:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:141:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:143:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set130 = None

        set130_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:143:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set130 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set130))

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
    # grammar/ShyRecognizerFrontend.g:145:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS131 = None
        NUMBER132 = None

        MINUS131_tree = None
        NUMBER132_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:145:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:145:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:145:13: ( MINUS )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == MINUS) :
                    alt33 = 1
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:145:13: MINUS
                    pass 
                    MINUS131 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1514)
                    MINUS131_tree = self._adaptor.createWithPayload(MINUS131)
                    self._adaptor.addChild(root_0, MINUS131_tree)






                NUMBER132 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1518)
                NUMBER132_tree = self._adaptor.createWithPayload(NUMBER132)
                self._adaptor.addChild(root_0, NUMBER132_tree)





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
    # grammar/ShyRecognizerFrontend.g:146:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS133 = None
        NUMBER134 = None
        DIVIDE135 = None
        NUMBER136 = None

        MINUS133_tree = None
        NUMBER134_tree = None
        DIVIDE135_tree = None
        NUMBER136_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:146:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:146:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:146:13: ( MINUS )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == MINUS) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:146:13: MINUS
                    pass 
                    MINUS133 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1526)
                    MINUS133_tree = self._adaptor.createWithPayload(MINUS133)
                    self._adaptor.addChild(root_0, MINUS133_tree)






                NUMBER134 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1530)
                NUMBER134_tree = self._adaptor.createWithPayload(NUMBER134)
                self._adaptor.addChild(root_0, NUMBER134_tree)



                DIVIDE135 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1532)
                DIVIDE135_tree = self._adaptor.createWithPayload(DIVIDE135)
                self._adaptor.addChild(root_0, DIVIDE135_tree)



                NUMBER136 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1534)
                NUMBER136_tree = self._adaptor.createWithPayload(NUMBER136)
                self._adaptor.addChild(root_0, NUMBER136_tree)





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



    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\1\12\1\uffff\1\20\1\11\1\20\1\11\2\uffff\1\20"
        )

    DFA30_max = DFA.unpack(
        u"\1\20\1\uffff\1\20\1\73\1\25\1\73\2\uffff\1\25"
        )

    DFA30_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA30_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA30_transition = [
        DFA.unpack(u"\1\2\5\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\6\uffff\1\5\52\uffff\1\5"),
        DFA.unpack(u"\1\6\4\uffff\1\7"),
        DFA.unpack(u"\1\10\6\uffff\1\5\52\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\4\uffff\1\7")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 7, 20, 27, 58])
    FOLLOW_stateless_in_start86 = frozenset([1, 7, 20, 27, 58])
    FOLLOW_consts_in_start90 = frozenset([1, 7, 20, 27, 58])
    FOLLOW_types_in_start94 = frozenset([1, 7, 20, 27, 58])
    FOLLOW_MODULE_in_module113 = frozenset([16])
    FOLLOW_ID_in_module115 = frozenset([21])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([16])
    FOLLOW_ID_in_stateless148 = frozenset([21])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1, 18])
    FOLLOW_INDENT_in_stateless154 = frozenset([21])
    FOLLOW_NEWLINE_in_stateless156 = frozenset([25])
    FOLLOW_proc_in_stateless158 = frozenset([11, 25])
    FOLLOW_DEDENT_in_stateless162 = frozenset([21])
    FOLLOW_NEWLINE_in_stateless164 = frozenset([1])
    FOLLOW_PROC_in_proc209 = frozenset([16])
    FOLLOW_ID_in_proc211 = frozenset([21])
    FOLLOW_NEWLINE_in_proc213 = frozenset([1])
    FOLLOW_PROC_in_proc241 = frozenset([16])
    FOLLOW_ID_in_proc243 = frozenset([21])
    FOLLOW_NEWLINE_in_proc245 = frozenset([18])
    FOLLOW_INDENT_in_proc247 = frozenset([21])
    FOLLOW_NEWLINE_in_proc249 = frozenset([4, 11, 23, 60])
    FOLLOW_proc_args_in_proc263 = frozenset([11, 23, 60])
    FOLLOW_proc_vars_in_proc267 = frozenset([11, 23])
    FOLLOW_proc_ops_in_proc271 = frozenset([11])
    FOLLOW_DEDENT_in_proc283 = frozenset([21])
    FOLLOW_NEWLINE_in_proc285 = frozenset([1])
    FOLLOW_ARGS_in_proc_args334 = frozenset([10, 16, 21])
    FOLLOW_vars_hint_in_proc_args336 = frozenset([1])
    FOLLOW_VARS_in_proc_vars365 = frozenset([10, 16, 21])
    FOLLOW_vars_hint_in_proc_vars367 = frozenset([1])
    FOLLOW_OPS_in_proc_ops396 = frozenset([21])
    FOLLOW_NEWLINE_in_proc_ops398 = frozenset([18])
    FOLLOW_INDENT_in_proc_ops400 = frozenset([21])
    FOLLOW_NEWLINE_in_proc_ops402 = frozenset([16, 17])
    FOLLOW_statement_in_proc_ops404 = frozenset([11, 16, 17])
    FOLLOW_DEDENT_in_proc_ops408 = frozenset([21])
    FOLLOW_NEWLINE_in_proc_ops410 = frozenset([1])
    FOLLOW_statement_call_in_statement449 = frozenset([1])
    FOLLOW_statement_if_in_statement459 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if478 = frozenset([1, 14])
    FOLLOW_statement_else_in_statement_if488 = frozenset([1])
    FOLLOW_IF_in_statement_if_head576 = frozenset([16])
    FOLLOW_statement_call_in_statement_if_head578 = frozenset([13, 21])
    FOLLOW_DO_in_statement_if_head580 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_if_head584 = frozenset([18])
    FOLLOW_INDENT_in_statement_if_head598 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_if_head600 = frozenset([16, 17])
    FOLLOW_statement_in_statement_if_head602 = frozenset([11, 16, 17])
    FOLLOW_DEDENT_in_statement_if_head606 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_if_head608 = frozenset([1])
    FOLLOW_ELSE_in_statement_else706 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_else708 = frozenset([18])
    FOLLOW_INDENT_in_statement_else722 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_else724 = frozenset([16, 17])
    FOLLOW_statement_in_statement_else726 = frozenset([11, 16, 17])
    FOLLOW_DEDENT_in_statement_else730 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_else732 = frozenset([1])
    FOLLOW_ID_in_statement_call806 = frozenset([13, 15, 16, 19, 21, 22])
    FOLLOW_statement_call_args_in_statement_call808 = frozenset([13, 21])
    FOLLOW_DO_in_statement_call814 = frozenset([1, 18])
    FOLLOW_NEWLINE_in_statement_call818 = frozenset([1, 18])
    FOLLOW_INDENT_in_statement_call832 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_call834 = frozenset([15, 16, 19, 22])
    FOLLOW_statement_call_args_in_statement_call838 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_call840 = frozenset([11, 15, 16, 19, 22])
    FOLLOW_DEDENT_in_statement_call846 = frozenset([21])
    FOLLOW_NEWLINE_in_statement_call848 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args906 = frozenset([1, 15, 16, 19, 22])
    FOLLOW_ID_in_statement_call_arg923 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg933 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg943 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg953 = frozenset([1])
    FOLLOW_CONSTS_in_consts972 = frozenset([16])
    FOLLOW_ID_in_consts974 = frozenset([21])
    FOLLOW_NEWLINE_in_consts976 = frozenset([18])
    FOLLOW_INDENT_in_consts986 = frozenset([21])
    FOLLOW_NEWLINE_in_consts988 = frozenset([16])
    FOLLOW_consts_items_in_consts990 = frozenset([11])
    FOLLOW_DEDENT_in_consts992 = frozenset([21])
    FOLLOW_NEWLINE_in_consts994 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1026 = frozenset([1, 16])
    FOLLOW_ID_in_consts_item1042 = frozenset([19, 22])
    FOLLOW_num_whole_in_consts_item1044 = frozenset([21])
    FOLLOW_NEWLINE_in_consts_item1046 = frozenset([1])
    FOLLOW_ID_in_consts_item1068 = frozenset([19, 22])
    FOLLOW_num_fract_in_consts_item1070 = frozenset([21])
    FOLLOW_NEWLINE_in_consts_item1072 = frozenset([1])
    FOLLOW_ID_in_consts_item1094 = frozenset([15])
    FOLLOW_EXPRESSION_in_consts_item1096 = frozenset([21])
    FOLLOW_NEWLINE_in_consts_item1098 = frozenset([1])
    FOLLOW_TYPES_in_types1129 = frozenset([16])
    FOLLOW_ID_in_types1131 = frozenset([21])
    FOLLOW_NEWLINE_in_types1133 = frozenset([18])
    FOLLOW_INDENT_in_types1143 = frozenset([21])
    FOLLOW_NEWLINE_in_types1145 = frozenset([16])
    FOLLOW_types_items_in_types1147 = frozenset([11])
    FOLLOW_DEDENT_in_types1149 = frozenset([21])
    FOLLOW_NEWLINE_in_types1151 = frozenset([1])
    FOLLOW_types_item_in_types_items1183 = frozenset([1, 16])
    FOLLOW_ID_in_types_item1193 = frozenset([10, 16, 21])
    FOLLOW_vars_hint_in_types_item1195 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1222 = frozenset([21])
    FOLLOW_NEWLINE_in_vars_hint1226 = frozenset([1, 18])
    FOLLOW_INDENT_in_vars_hint1238 = frozenset([21])
    FOLLOW_NEWLINE_in_vars_hint1240 = frozenset([10, 16])
    FOLLOW_var_hint_in_vars_hint1244 = frozenset([21])
    FOLLOW_NEWLINE_in_vars_hint1246 = frozenset([10, 11, 16])
    FOLLOW_DEDENT_in_vars_hint1252 = frozenset([21])
    FOLLOW_NEWLINE_in_vars_hint1254 = frozenset([1])
    FOLLOW_var_in_var_hint1293 = frozenset([1, 16])
    FOLLOW_hint_in_var_hint1328 = frozenset([16])
    FOLLOW_var_in_var_hint1330 = frozenset([1, 16])
    FOLLOW_hint_in_var_hint1364 = frozenset([21])
    FOLLOW_NEWLINE_in_var_hint1366 = frozenset([18])
    FOLLOW_INDENT_in_var_hint1368 = frozenset([21])
    FOLLOW_NEWLINE_in_var_hint1370 = frozenset([16])
    FOLLOW_var_in_var_hint1374 = frozenset([16, 21])
    FOLLOW_NEWLINE_in_var_hint1378 = frozenset([11, 16])
    FOLLOW_DEDENT_in_var_hint1384 = frozenset([1])
    FOLLOW_ID_in_var1418 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1443 = frozenset([16])
    FOLLOW_ID_in_hint1445 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint1447 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1467 = frozenset([16])
    FOLLOW_ID_in_hint1469 = frozenset([16, 59])
    FOLLOW_hint_arg_in_hint1471 = frozenset([9, 16, 59])
    FOLLOW_CURLY_CLOSE_in_hint1475 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1514 = frozenset([22])
    FOLLOW_NUMBER_in_num_whole1518 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1526 = frozenset([22])
    FOLLOW_NUMBER_in_num_fract1530 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1532 = frozenset([22])
    FOLLOW_NUMBER_in_num_fract1534 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
