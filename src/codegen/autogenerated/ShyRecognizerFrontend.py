# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-24 20:32:47

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
ELIF=14
ELSE=15
EXPRESSION=16
ID=17
IF=18
INDENT=19
MINUS=20
MODULE=21
NEWLINE=22
NUMBER=23
OPS=24
PASTE=25
PROC=26
REPLACE=27
STATELESS=28
STRING=29
TREE_ARBITRARY_TOKEN=30
TREE_CONDITION_ANY=31
TREE_CONSTS=32
TREE_COPY=33
TREE_COPY_PASTE=34
TREE_EXPRESSION=35
TREE_HINT=36
TREE_HINT_NONE=37
TREE_MODULE=38
TREE_NUM_FRACT=39
TREE_NUM_WHOLE=40
TREE_PASTE=41
TREE_PASTE_REPLACE=42
TREE_PASTE_WITH=43
TREE_PROC=44
TREE_PROC_ARGS=45
TREE_PROC_VARS=46
TREE_STATELESS=47
TREE_STATEMENTS=48
TREE_STATEMENT_CALL=49
TREE_STATEMENT_CALL_ARGS=50
TREE_STATEMENT_ELIF=51
TREE_STATEMENT_ELSE=52
TREE_STATEMENT_IF=53
TREE_TYPES=54
TREE_TYPES_ITEM=55
TREE_VAR=56
TREE_VARS_HINT=57
TREE_VAR_HINT=58
TYPES=59
UNDERSCORE=60
VARS=61
WHITESPACE=62
WITH=63

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", "EXPRESSION", 
    "ID", "IF", "INDENT", "MINUS", "MODULE", "NEWLINE", "NUMBER", "OPS", 
    "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", 
    "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
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

        self.dfa32 = self.DFA32(
            self, 32,
            eot = self.DFA32_eot,
            eof = self.DFA32_eof,
            min = self.DFA32_min,
            max = self.DFA32_max,
            accept = self.DFA32_accept,
            special = self.DFA32_special,
            transition = self.DFA32_transition
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
                # elements: statement_if_head, statement_else, statement_elif
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
    # grammar/ShyRecognizerFrontend.g:91:1: condition : statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) ;
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DO60 = None
        NEWLINE61 = None
        statement_call59 = None


        DO60_tree = None
        NEWLINE61_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:92:5: ( statement_call ( DO )? NEWLINE -> ^( TREE_CONDITION_ANY statement_call ) )
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





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:96:1: statement_else : ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE62 = None
        NEWLINE63 = None
        INDENT64 = None
        NEWLINE65 = None
        DEDENT67 = None
        NEWLINE68 = None
        statement66 = None


        ELSE62_tree = None
        NEWLINE63_tree = None
        INDENT64_tree = None
        NEWLINE65_tree = None
        DEDENT67_tree = None
        NEWLINE68_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:97:5: ( ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:97:9: ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELSE62 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else888) 
                stream_ELSE.add(ELSE62)


                NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else890) 
                stream_NEWLINE.add(NEWLINE63)


                INDENT64 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else904) 
                stream_INDENT.add(INDENT64)


                NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else906) 
                stream_NEWLINE.add(NEWLINE65)


                # grammar/ShyRecognizerFrontend.g:98:28: ( statement )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((ID <= LA15_0 <= IF)) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:98:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_else908)
                        statement66 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement66.tree)



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                DEDENT67 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else912) 
                stream_DEDENT.add(DEDENT67)


                NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else914) 
                stream_NEWLINE.add(NEWLINE68)


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
                # 99:9: -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:99:13: ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:100:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:100:36: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:104:1: statement_call : ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID69 = None
        DO71 = None
        NEWLINE72 = None
        INDENT73 = None
        NEWLINE74 = None
        NEWLINE76 = None
        DEDENT77 = None
        NEWLINE78 = None
        statement_call_args70 = None

        statement_call_args75 = None


        ID69_tree = None
        DO71_tree = None
        NEWLINE72_tree = None
        INDENT73_tree = None
        NEWLINE74_tree = None
        NEWLINE76_tree = None
        DEDENT77_tree = None
        NEWLINE78_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:105:5: ( ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:105:9: ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call988) 
                stream_ID.add(ID69)


                # grammar/ShyRecognizerFrontend.g:105:12: ( statement_call_args )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((EXPRESSION <= LA16_0 <= ID) or LA16_0 == MINUS or LA16_0 == NUMBER) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:105:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call990)
                    statement_call_args70 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args70.tree)





                # grammar/ShyRecognizerFrontend.g:105:34: ( DO | NEWLINE )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == DO) :
                    alt17 = 1
                elif (LA17_0 == NEWLINE) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:105:36: DO
                    pass 
                    DO71 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_call996) 
                    stream_DO.add(DO71)



                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:105:41: NEWLINE
                    pass 
                    NEWLINE72 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1000) 
                    stream_NEWLINE.add(NEWLINE72)





                # grammar/ShyRecognizerFrontend.g:106:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == INDENT) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:106:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT73 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call1014) 
                    stream_INDENT.add(INDENT73)


                    NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1016) 
                    stream_NEWLINE.add(NEWLINE74)


                    # grammar/ShyRecognizerFrontend.g:106:26: ( statement_call_args NEWLINE )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA18_0 <= ID) or LA18_0 == MINUS or LA18_0 == NUMBER) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerFrontend.g:106:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1020)
                            statement_call_args75 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args75.tree)


                            NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1022) 
                            stream_NEWLINE.add(NEWLINE76)



                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


                    DEDENT77 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call1028) 
                    stream_DEDENT.add(DEDENT77)


                    NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1030) 
                    stream_NEWLINE.add(NEWLINE78)





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
                # 107:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:107:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:108:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:111:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg79 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:111:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:111:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:111:23: ( statement_call_arg )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerFrontend.g:111:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1088)
                        statement_call_arg79 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg79.tree)



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

    # $ANTLR end "statement_call_args"


    class statement_call_arg_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_call_arg_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_call_arg"
    # grammar/ShyRecognizerFrontend.g:113:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID80 = None
        EXPRESSION81 = None
        num_whole82 = None

        num_fract83 = None


        ID80_tree = None
        EXPRESSION81_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:114:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt21 = 4
                LA21 = self.input.LA(1)
                if LA21 == ID:
                    alt21 = 1
                elif LA21 == EXPRESSION:
                    alt21 = 2
                elif LA21 == MINUS:
                    LA21_3 = self.input.LA(2)

                    if (LA21_3 == NUMBER) :
                        LA21_4 = self.input.LA(3)

                        if (LA21_4 == DIVIDE) :
                            alt21 = 4
                        elif (LA21_4 == DO or (EXPRESSION <= LA21_4 <= ID) or LA21_4 == MINUS or (NEWLINE <= LA21_4 <= NUMBER)) :
                            alt21 = 3
                        else:
                            nvae = NoViableAltException("", 21, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 21, 3, self.input)

                        raise nvae


                elif LA21 == NUMBER:
                    LA21_4 = self.input.LA(2)

                    if (LA21_4 == DIVIDE) :
                        alt21 = 4
                    elif (LA21_4 == DO or (EXPRESSION <= LA21_4 <= ID) or LA21_4 == MINUS or (NEWLINE <= LA21_4 <= NUMBER)) :
                        alt21 = 3
                    else:
                        nvae = NoViableAltException("", 21, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae


                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:114:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1105)
                    ID80_tree = self._adaptor.createWithPayload(ID80)
                    self._adaptor.addChild(root_0, ID80_tree)




                elif alt21 == 2:
                    # grammar/ShyRecognizerFrontend.g:115:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION81 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1115)
                    EXPRESSION81_tree = self._adaptor.createWithPayload(EXPRESSION81)
                    self._adaptor.addChild(root_0, EXPRESSION81_tree)




                elif alt21 == 3:
                    # grammar/ShyRecognizerFrontend.g:116:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1125)
                    num_whole82 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole82.tree)



                elif alt21 == 4:
                    # grammar/ShyRecognizerFrontend.g:117:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1135)
                    num_fract83 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract83.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:120:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS84 = None
        ID85 = None
        NEWLINE86 = None
        INDENT87 = None
        NEWLINE88 = None
        DEDENT90 = None
        NEWLINE91 = None
        consts_items89 = None


        CONSTS84_tree = None
        ID85_tree = None
        NEWLINE86_tree = None
        INDENT87_tree = None
        NEWLINE88_tree = None
        DEDENT90_tree = None
        NEWLINE91_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:121:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:121:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS84 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1154) 
                stream_CONSTS.add(CONSTS84)


                ID85 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1156) 
                stream_ID.add(ID85)


                NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1158) 
                stream_NEWLINE.add(NEWLINE86)


                INDENT87 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1168) 
                stream_INDENT.add(INDENT87)


                NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1170) 
                stream_NEWLINE.add(NEWLINE88)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1172)
                consts_items89 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items89.tree)


                DEDENT90 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1174) 
                stream_DEDENT.add(DEDENT90)


                NEWLINE91 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1176) 
                stream_NEWLINE.add(NEWLINE91)


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
                # 123:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:123:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:125:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item92 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:125:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:125:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:125:16: ( consts_item )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == ID) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerFrontend.g:125:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1208)
                        consts_item92 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item92.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:126:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID93 = None
        NEWLINE95 = None
        ID96 = None
        NEWLINE98 = None
        ID99 = None
        EXPRESSION100 = None
        NEWLINE101 = None
        num_whole94 = None

        num_fract97 = None


        ID93_tree = None
        NEWLINE95_tree = None
        ID96_tree = None
        NEWLINE98_tree = None
        ID99_tree = None
        EXPRESSION100_tree = None
        NEWLINE101_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:127:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt23 = 3
                LA23_0 = self.input.LA(1)

                if (LA23_0 == ID) :
                    LA23 = self.input.LA(2)
                    if LA23 == EXPRESSION:
                        alt23 = 3
                    elif LA23 == MINUS:
                        LA23_3 = self.input.LA(3)

                        if (LA23_3 == NUMBER) :
                            LA23_4 = self.input.LA(4)

                            if (LA23_4 == DIVIDE) :
                                alt23 = 2
                            elif (LA23_4 == NEWLINE) :
                                alt23 = 1
                            else:
                                nvae = NoViableAltException("", 23, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 23, 3, self.input)

                            raise nvae


                    elif LA23 == NUMBER:
                        LA23_4 = self.input.LA(3)

                        if (LA23_4 == DIVIDE) :
                            alt23 = 2
                        elif (LA23_4 == NEWLINE) :
                            alt23 = 1
                        else:
                            nvae = NoViableAltException("", 23, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 23, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:127:9: ID num_whole NEWLINE
                    pass 
                    ID93 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1224) 
                    stream_ID.add(ID93)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1226)
                    num_whole94 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole94.tree)


                    NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1228) 
                    stream_NEWLINE.add(NEWLINE95)


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
                    # 127:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:127:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt23 == 2:
                    # grammar/ShyRecognizerFrontend.g:128:9: ID num_fract NEWLINE
                    pass 
                    ID96 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1250) 
                    stream_ID.add(ID96)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1252)
                    num_fract97 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract97.tree)


                    NEWLINE98 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1254) 
                    stream_NEWLINE.add(NEWLINE98)


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
                    # 128:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:128:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt23 == 3:
                    # grammar/ShyRecognizerFrontend.g:129:9: ID EXPRESSION NEWLINE
                    pass 
                    ID99 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1276) 
                    stream_ID.add(ID99)


                    EXPRESSION100 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1278) 
                    stream_EXPRESSION.add(EXPRESSION100)


                    NEWLINE101 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1280) 
                    stream_NEWLINE.add(NEWLINE101)


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
                    # 129:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:129:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:132:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES102 = None
        ID103 = None
        NEWLINE104 = None
        INDENT105 = None
        NEWLINE106 = None
        DEDENT108 = None
        NEWLINE109 = None
        types_items107 = None


        TYPES102_tree = None
        ID103_tree = None
        NEWLINE104_tree = None
        INDENT105_tree = None
        NEWLINE106_tree = None
        DEDENT108_tree = None
        NEWLINE109_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:133:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:133:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES102 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1311) 
                stream_TYPES.add(TYPES102)


                ID103 = self.match(self.input, ID, self.FOLLOW_ID_in_types1313) 
                stream_ID.add(ID103)


                NEWLINE104 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1315) 
                stream_NEWLINE.add(NEWLINE104)


                INDENT105 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1325) 
                stream_INDENT.add(INDENT105)


                NEWLINE106 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1327) 
                stream_NEWLINE.add(NEWLINE106)


                self._state.following.append(self.FOLLOW_types_items_in_types1329)
                types_items107 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items107.tree)


                DEDENT108 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1331) 
                stream_DEDENT.add(DEDENT108)


                NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1333) 
                stream_NEWLINE.add(NEWLINE109)


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
                # 135:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:135:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:137:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item110 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:137:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:137:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:137:15: ( types_item )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ID) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerFrontend.g:137:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1365)
                        types_item110 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item110.tree)



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

    # $ANTLR end "types_items"


    class types_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.types_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerFrontend.g:138:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID111 = None
        vars_hint112 = None


        ID111_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:138:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:138:14: ID vars_hint
                pass 
                ID111 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1375) 
                stream_ID.add(ID111)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1377)
                vars_hint112 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint112.tree)


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
                # 138:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:138:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:140:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE114 = None
        INDENT115 = None
        NEWLINE116 = None
        NEWLINE118 = None
        DEDENT119 = None
        NEWLINE120 = None
        var_hint113 = None

        var_hint117 = None


        NEWLINE114_tree = None
        INDENT115_tree = None
        NEWLINE116_tree = None
        NEWLINE118_tree = None
        DEDENT119_tree = None
        NEWLINE120_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:141:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:141:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:141:9: ( var_hint )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == CURLY_OPEN or LA25_0 == ID) :
                    alt25 = 1
                if alt25 == 1:
                    # grammar/ShyRecognizerFrontend.g:141:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1404)
                    var_hint113 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint113.tree)





                NEWLINE114 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1408) 
                stream_NEWLINE.add(NEWLINE114)


                # grammar/ShyRecognizerFrontend.g:142:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == INDENT) :
                    alt27 = 1
                if alt27 == 1:
                    # grammar/ShyRecognizerFrontend.g:142:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT115 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1420) 
                    stream_INDENT.add(INDENT115)


                    NEWLINE116 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1422) 
                    stream_NEWLINE.add(NEWLINE116)


                    # grammar/ShyRecognizerFrontend.g:142:26: ( var_hint NEWLINE )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == CURLY_OPEN or LA26_0 == ID) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:142:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1426)
                            var_hint117 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint117.tree)


                            NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1428) 
                            stream_NEWLINE.add(NEWLINE118)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


                    DEDENT119 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1434) 
                    stream_DEDENT.add(DEDENT119)


                    NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1436) 
                    stream_NEWLINE.add(NEWLINE120)





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
                # 143:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:143:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:145:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE125 = None
        INDENT126 = None
        NEWLINE127 = None
        NEWLINE129 = None
        DEDENT130 = None
        var121 = None

        hint122 = None

        var123 = None

        hint124 = None

        var128 = None


        NEWLINE125_tree = None
        INDENT126_tree = None
        NEWLINE127_tree = None
        NEWLINE129_tree = None
        DEDENT130_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:146:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt32 = 3
                alt32 = self.dfa32.predict(self.input)
                if alt32 == 1:
                    # grammar/ShyRecognizerFrontend.g:146:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:146:9: ( var )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == ID) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:146:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1475)
                            var121 = self.var()

                            self._state.following.pop()
                            stream_var.add(var121.tree)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


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
                    # 147:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:147:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:147:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt32 == 2:
                    # grammar/ShyRecognizerFrontend.g:148:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1510)
                    hint122 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint122.tree)


                    # grammar/ShyRecognizerFrontend.g:148:14: ( var )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:148:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1512)
                            var123 = self.var()

                            self._state.following.pop()
                            stream_var.add(var123.tree)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


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
                    # 149:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:149:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:149:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt32 == 3:
                    # grammar/ShyRecognizerFrontend.g:150:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1546)
                    hint124 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint124.tree)


                    NEWLINE125 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1548) 
                    stream_NEWLINE.add(NEWLINE125)


                    INDENT126 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1550) 
                    stream_INDENT.add(INDENT126)


                    NEWLINE127 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1552) 
                    stream_NEWLINE.add(NEWLINE127)


                    # grammar/ShyRecognizerFrontend.g:150:37: ( ( var )+ NEWLINE )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == ID) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:150:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:150:39: ( var )+
                            cnt30 = 0
                            while True: #loop30
                                alt30 = 2
                                LA30_0 = self.input.LA(1)

                                if (LA30_0 == ID) :
                                    alt30 = 1


                                if alt30 == 1:
                                    # grammar/ShyRecognizerFrontend.g:150:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1556)
                                    var128 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var128.tree)



                                else:
                                    if cnt30 >= 1:
                                        break #loop30

                                    eee = EarlyExitException(30, self.input)
                                    raise eee

                                cnt30 += 1


                            NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1560) 
                            stream_NEWLINE.add(NEWLINE129)



                        else:
                            if cnt31 >= 1:
                                break #loop31

                            eee = EarlyExitException(31, self.input)
                            raise eee

                        cnt31 += 1


                    DEDENT130 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1566) 
                    stream_DEDENT.add(DEDENT130)


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
                    # 151:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:151:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:151:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:153:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID131 = None

        ID131_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:153:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:153:7: ID
                pass 
                ID131 = self.match(self.input, ID, self.FOLLOW_ID_in_var1600) 
                stream_ID.add(ID131)


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
                # 153:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:153:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:155:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN132 = None
        ID133 = None
        CURLY_CLOSE134 = None
        CURLY_OPEN135 = None
        ID136 = None
        CURLY_CLOSE138 = None
        hint_arg137 = None


        CURLY_OPEN132_tree = None
        ID133_tree = None
        CURLY_CLOSE134_tree = None
        CURLY_OPEN135_tree = None
        ID136_tree = None
        CURLY_CLOSE138_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:156:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == CURLY_OPEN) :
                    LA34_1 = self.input.LA(2)

                    if (LA34_1 == ID) :
                        LA34_2 = self.input.LA(3)

                        if (LA34_2 == CURLY_CLOSE) :
                            alt34 = 1
                        elif (LA34_2 == ID or LA34_2 == UNDERSCORE) :
                            alt34 = 2
                        else:
                            nvae = NoViableAltException("", 34, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 34, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae


                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:156:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN132 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1625) 
                    stream_CURLY_OPEN.add(CURLY_OPEN132)


                    ID133 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1627) 
                    stream_ID.add(ID133)


                    CURLY_CLOSE134 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1629) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE134)


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
                    # 156:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:156:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt34 == 2:
                    # grammar/ShyRecognizerFrontend.g:157:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN135 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1649) 
                    stream_CURLY_OPEN.add(CURLY_OPEN135)


                    ID136 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1651) 
                    stream_ID.add(ID136)


                    # grammar/ShyRecognizerFrontend.g:157:23: ( hint_arg )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == ID or LA33_0 == UNDERSCORE) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerFrontend.g:157:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1653)
                            hint_arg137 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg137.tree)



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


                    CURLY_CLOSE138 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1657) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE138)


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
                    # 157:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:157:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:157:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:159:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set139 = None

        set139_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:159:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set139 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set139))

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
    # grammar/ShyRecognizerFrontend.g:161:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS140 = None
        NUMBER141 = None

        MINUS140_tree = None
        NUMBER141_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:161:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:161:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:161:13: ( MINUS )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == MINUS) :
                    alt35 = 1
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:161:13: MINUS
                    pass 
                    MINUS140 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1696)
                    MINUS140_tree = self._adaptor.createWithPayload(MINUS140)
                    self._adaptor.addChild(root_0, MINUS140_tree)






                NUMBER141 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1700)
                NUMBER141_tree = self._adaptor.createWithPayload(NUMBER141)
                self._adaptor.addChild(root_0, NUMBER141_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:162:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS142 = None
        NUMBER143 = None
        DIVIDE144 = None
        NUMBER145 = None

        MINUS142_tree = None
        NUMBER143_tree = None
        DIVIDE144_tree = None
        NUMBER145_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:162:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:162:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:162:13: ( MINUS )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == MINUS) :
                    alt36 = 1
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:162:13: MINUS
                    pass 
                    MINUS142 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1708)
                    MINUS142_tree = self._adaptor.createWithPayload(MINUS142)
                    self._adaptor.addChild(root_0, MINUS142_tree)






                NUMBER143 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1712)
                NUMBER143_tree = self._adaptor.createWithPayload(NUMBER143)
                self._adaptor.addChild(root_0, NUMBER143_tree)



                DIVIDE144 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1714)
                DIVIDE144_tree = self._adaptor.createWithPayload(DIVIDE144)
                self._adaptor.addChild(root_0, DIVIDE144_tree)



                NUMBER145 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1716)
                NUMBER145_tree = self._adaptor.createWithPayload(NUMBER145)
                self._adaptor.addChild(root_0, NUMBER145_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA32_min = DFA.unpack(
        u"\1\12\1\uffff\1\21\1\11\1\21\1\11\2\uffff\1\21"
        )

    DFA32_max = DFA.unpack(
        u"\1\21\1\uffff\1\21\1\74\1\26\1\74\2\uffff\1\26"
        )

    DFA32_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA32_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA32_transition = [
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

    # class definition for DFA #32

    class DFA32(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 7, 21, 28, 59])
    FOLLOW_stateless_in_start86 = frozenset([1, 7, 21, 28, 59])
    FOLLOW_consts_in_start90 = frozenset([1, 7, 21, 28, 59])
    FOLLOW_types_in_start94 = frozenset([1, 7, 21, 28, 59])
    FOLLOW_MODULE_in_module113 = frozenset([17])
    FOLLOW_ID_in_module115 = frozenset([22])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([17])
    FOLLOW_ID_in_stateless148 = frozenset([22])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1, 19])
    FOLLOW_INDENT_in_stateless154 = frozenset([22])
    FOLLOW_NEWLINE_in_stateless156 = frozenset([26])
    FOLLOW_proc_in_stateless158 = frozenset([11, 26])
    FOLLOW_DEDENT_in_stateless162 = frozenset([22])
    FOLLOW_NEWLINE_in_stateless164 = frozenset([1])
    FOLLOW_PROC_in_proc209 = frozenset([17])
    FOLLOW_ID_in_proc211 = frozenset([22])
    FOLLOW_NEWLINE_in_proc213 = frozenset([1])
    FOLLOW_PROC_in_proc241 = frozenset([17])
    FOLLOW_ID_in_proc243 = frozenset([22])
    FOLLOW_NEWLINE_in_proc245 = frozenset([19])
    FOLLOW_INDENT_in_proc247 = frozenset([22])
    FOLLOW_NEWLINE_in_proc249 = frozenset([4, 11, 24, 61])
    FOLLOW_proc_args_in_proc263 = frozenset([11, 24, 61])
    FOLLOW_proc_vars_in_proc267 = frozenset([11, 24])
    FOLLOW_proc_ops_in_proc271 = frozenset([11])
    FOLLOW_DEDENT_in_proc283 = frozenset([22])
    FOLLOW_NEWLINE_in_proc285 = frozenset([1])
    FOLLOW_ARGS_in_proc_args334 = frozenset([10, 17, 22])
    FOLLOW_vars_hint_in_proc_args336 = frozenset([1])
    FOLLOW_VARS_in_proc_vars365 = frozenset([10, 17, 22])
    FOLLOW_vars_hint_in_proc_vars367 = frozenset([1])
    FOLLOW_OPS_in_proc_ops396 = frozenset([22])
    FOLLOW_NEWLINE_in_proc_ops398 = frozenset([19])
    FOLLOW_INDENT_in_proc_ops400 = frozenset([22])
    FOLLOW_NEWLINE_in_proc_ops402 = frozenset([17, 18])
    FOLLOW_statement_in_proc_ops404 = frozenset([11, 17, 18])
    FOLLOW_DEDENT_in_proc_ops408 = frozenset([22])
    FOLLOW_NEWLINE_in_proc_ops410 = frozenset([1])
    FOLLOW_statement_call_in_statement449 = frozenset([1])
    FOLLOW_statement_if_in_statement459 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if478 = frozenset([1, 14, 15])
    FOLLOW_statement_elif_in_statement_if488 = frozenset([1, 14, 15])
    FOLLOW_statement_else_in_statement_if500 = frozenset([1])
    FOLLOW_IF_in_statement_if_head608 = frozenset([17])
    FOLLOW_condition_in_statement_if_head610 = frozenset([19])
    FOLLOW_INDENT_in_statement_if_head624 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_if_head626 = frozenset([17, 18])
    FOLLOW_statement_in_statement_if_head628 = frozenset([11, 17, 18])
    FOLLOW_DEDENT_in_statement_if_head632 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_if_head634 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif726 = frozenset([17])
    FOLLOW_condition_in_statement_elif728 = frozenset([19])
    FOLLOW_INDENT_in_statement_elif742 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_elif744 = frozenset([17, 18])
    FOLLOW_statement_in_statement_elif746 = frozenset([11, 17, 18])
    FOLLOW_DEDENT_in_statement_elif750 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_elif752 = frozenset([1])
    FOLLOW_statement_call_in_condition844 = frozenset([13, 22])
    FOLLOW_DO_in_condition846 = frozenset([22])
    FOLLOW_NEWLINE_in_condition850 = frozenset([1])
    FOLLOW_ELSE_in_statement_else888 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_else890 = frozenset([19])
    FOLLOW_INDENT_in_statement_else904 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_else906 = frozenset([17, 18])
    FOLLOW_statement_in_statement_else908 = frozenset([11, 17, 18])
    FOLLOW_DEDENT_in_statement_else912 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_else914 = frozenset([1])
    FOLLOW_ID_in_statement_call988 = frozenset([13, 16, 17, 20, 22, 23])
    FOLLOW_statement_call_args_in_statement_call990 = frozenset([13, 22])
    FOLLOW_DO_in_statement_call996 = frozenset([1, 19])
    FOLLOW_NEWLINE_in_statement_call1000 = frozenset([1, 19])
    FOLLOW_INDENT_in_statement_call1014 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_call1016 = frozenset([16, 17, 20, 23])
    FOLLOW_statement_call_args_in_statement_call1020 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_call1022 = frozenset([11, 16, 17, 20, 23])
    FOLLOW_DEDENT_in_statement_call1028 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_call1030 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args1088 = frozenset([1, 16, 17, 20, 23])
    FOLLOW_ID_in_statement_call_arg1105 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1115 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1125 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1135 = frozenset([1])
    FOLLOW_CONSTS_in_consts1154 = frozenset([17])
    FOLLOW_ID_in_consts1156 = frozenset([22])
    FOLLOW_NEWLINE_in_consts1158 = frozenset([19])
    FOLLOW_INDENT_in_consts1168 = frozenset([22])
    FOLLOW_NEWLINE_in_consts1170 = frozenset([17])
    FOLLOW_consts_items_in_consts1172 = frozenset([11])
    FOLLOW_DEDENT_in_consts1174 = frozenset([22])
    FOLLOW_NEWLINE_in_consts1176 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1208 = frozenset([1, 17])
    FOLLOW_ID_in_consts_item1224 = frozenset([20, 23])
    FOLLOW_num_whole_in_consts_item1226 = frozenset([22])
    FOLLOW_NEWLINE_in_consts_item1228 = frozenset([1])
    FOLLOW_ID_in_consts_item1250 = frozenset([20, 23])
    FOLLOW_num_fract_in_consts_item1252 = frozenset([22])
    FOLLOW_NEWLINE_in_consts_item1254 = frozenset([1])
    FOLLOW_ID_in_consts_item1276 = frozenset([16])
    FOLLOW_EXPRESSION_in_consts_item1278 = frozenset([22])
    FOLLOW_NEWLINE_in_consts_item1280 = frozenset([1])
    FOLLOW_TYPES_in_types1311 = frozenset([17])
    FOLLOW_ID_in_types1313 = frozenset([22])
    FOLLOW_NEWLINE_in_types1315 = frozenset([19])
    FOLLOW_INDENT_in_types1325 = frozenset([22])
    FOLLOW_NEWLINE_in_types1327 = frozenset([17])
    FOLLOW_types_items_in_types1329 = frozenset([11])
    FOLLOW_DEDENT_in_types1331 = frozenset([22])
    FOLLOW_NEWLINE_in_types1333 = frozenset([1])
    FOLLOW_types_item_in_types_items1365 = frozenset([1, 17])
    FOLLOW_ID_in_types_item1375 = frozenset([10, 17, 22])
    FOLLOW_vars_hint_in_types_item1377 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1404 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1408 = frozenset([1, 19])
    FOLLOW_INDENT_in_vars_hint1420 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1422 = frozenset([10, 17])
    FOLLOW_var_hint_in_vars_hint1426 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1428 = frozenset([10, 11, 17])
    FOLLOW_DEDENT_in_vars_hint1434 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1436 = frozenset([1])
    FOLLOW_var_in_var_hint1475 = frozenset([1, 17])
    FOLLOW_hint_in_var_hint1510 = frozenset([17])
    FOLLOW_var_in_var_hint1512 = frozenset([1, 17])
    FOLLOW_hint_in_var_hint1546 = frozenset([22])
    FOLLOW_NEWLINE_in_var_hint1548 = frozenset([19])
    FOLLOW_INDENT_in_var_hint1550 = frozenset([22])
    FOLLOW_NEWLINE_in_var_hint1552 = frozenset([17])
    FOLLOW_var_in_var_hint1556 = frozenset([17, 22])
    FOLLOW_NEWLINE_in_var_hint1560 = frozenset([11, 17])
    FOLLOW_DEDENT_in_var_hint1566 = frozenset([1])
    FOLLOW_ID_in_var1600 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1625 = frozenset([17])
    FOLLOW_ID_in_hint1627 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint1629 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1649 = frozenset([17])
    FOLLOW_ID_in_hint1651 = frozenset([17, 60])
    FOLLOW_hint_arg_in_hint1653 = frozenset([9, 17, 60])
    FOLLOW_CURLY_CLOSE_in_hint1657 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1696 = frozenset([23])
    FOLLOW_NUMBER_in_num_whole1700 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1708 = frozenset([23])
    FOLLOW_NUMBER_in_num_fract1712 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1714 = frozenset([23])
    FOLLOW_NUMBER_in_num_fract1716 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
