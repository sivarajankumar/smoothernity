# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-24 20:25:12

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

        self.dfa33 = self.DFA33(
            self, 33,
            eot = self.DFA33_eot,
            eof = self.DFA33_eof,
            min = self.DFA33_min,
            max = self.DFA33_max,
            accept = self.DFA33_accept,
            special = self.DFA33_special,
            transition = self.DFA33_transition
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
                    # elements: proc_vars, ID, proc_args, proc_ops
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
    # grammar/ShyRecognizerFrontend.g:73:1: statement_if_head : IF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF45 = None
        DO47 = None
        NEWLINE48 = None
        INDENT49 = None
        NEWLINE50 = None
        DEDENT52 = None
        NEWLINE53 = None
        statement_call46 = None

        statement51 = None


        IF45_tree = None
        DO47_tree = None
        NEWLINE48_tree = None
        INDENT49_tree = None
        NEWLINE50_tree = None
        DEDENT52_tree = None
        NEWLINE53_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statement_call = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:74:5: ( IF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:74:9: IF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                IF45 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head608) 
                stream_IF.add(IF45)


                self._state.following.append(self.FOLLOW_statement_call_in_statement_if_head610)
                statement_call46 = self.statement_call()

                self._state.following.pop()
                stream_statement_call.add(statement_call46.tree)


                # grammar/ShyRecognizerFrontend.g:74:27: ( DO )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == DO) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:74:27: DO
                    pass 
                    DO47 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_if_head612) 
                    stream_DO.add(DO47)





                NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head616) 
                stream_NEWLINE.add(NEWLINE48)


                INDENT49 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_if_head630) 
                stream_INDENT.add(INDENT49)


                NEWLINE50 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head632) 
                stream_NEWLINE.add(NEWLINE50)


                # grammar/ShyRecognizerFrontend.g:75:28: ( statement )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((ID <= LA13_0 <= IF)) :
                        alt13 = 1


                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:75:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_if_head634)
                        statement51 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement51.tree)



                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                DEDENT52 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_if_head638) 
                stream_DEDENT.add(DEDENT52)


                NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_if_head640) 
                stream_NEWLINE.add(NEWLINE53)


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
                # 76:9: -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:76:13: ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:77:17: ^( TREE_CONDITION_ANY statement_call )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                , root_2)

                self._adaptor.addChild(root_2, stream_statement_call.nextTree())

                self._adaptor.addChild(root_1, root_2)

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
    # grammar/ShyRecognizerFrontend.g:82:1: statement_elif : ELIF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF54 = None
        DO56 = None
        NEWLINE57 = None
        INDENT58 = None
        NEWLINE59 = None
        DEDENT61 = None
        NEWLINE62 = None
        statement_call55 = None

        statement60 = None


        ELIF54_tree = None
        DO56_tree = None
        NEWLINE57_tree = None
        INDENT58_tree = None
        NEWLINE59_tree = None
        DEDENT61_tree = None
        NEWLINE62_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statement_call = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:5: ( ELIF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:83:9: ELIF statement_call ( DO )? NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELIF54 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif738) 
                stream_ELIF.add(ELIF54)


                self._state.following.append(self.FOLLOW_statement_call_in_statement_elif740)
                statement_call55 = self.statement_call()

                self._state.following.pop()
                stream_statement_call.add(statement_call55.tree)


                # grammar/ShyRecognizerFrontend.g:83:29: ( DO )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == DO) :
                    alt14 = 1
                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:83:29: DO
                    pass 
                    DO56 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif742) 
                    stream_DO.add(DO56)





                NEWLINE57 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif746) 
                stream_NEWLINE.add(NEWLINE57)


                INDENT58 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif760) 
                stream_INDENT.add(INDENT58)


                NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif762) 
                stream_NEWLINE.add(NEWLINE59)


                # grammar/ShyRecognizerFrontend.g:84:28: ( statement )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((ID <= LA15_0 <= IF)) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:84:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_elif764)
                        statement60 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement60.tree)



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


                DEDENT61 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif768) 
                stream_DEDENT.add(DEDENT61)


                NEWLINE62 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif770) 
                stream_NEWLINE.add(NEWLINE62)


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
                # 85:9: -> ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:85:13: ^( TREE_STATEMENT_ELIF ^( TREE_CONDITION_ANY statement_call ) ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:86:17: ^( TREE_CONDITION_ANY statement_call )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                , root_2)

                self._adaptor.addChild(root_2, stream_statement_call.nextTree())

                self._adaptor.addChild(root_1, root_2)

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


    class statement_else_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_else_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_else"
    # grammar/ShyRecognizerFrontend.g:91:1: statement_else : ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE63 = None
        NEWLINE64 = None
        INDENT65 = None
        NEWLINE66 = None
        DEDENT68 = None
        NEWLINE69 = None
        statement67 = None


        ELSE63_tree = None
        NEWLINE64_tree = None
        INDENT65_tree = None
        NEWLINE66_tree = None
        DEDENT68_tree = None
        NEWLINE69_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:92:5: ( ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) ) )
                # grammar/ShyRecognizerFrontend.g:92:9: ELSE NEWLINE INDENT NEWLINE ( statement )+ DEDENT NEWLINE
                pass 
                ELSE63 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else868) 
                stream_ELSE.add(ELSE63)


                NEWLINE64 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else870) 
                stream_NEWLINE.add(NEWLINE64)


                INDENT65 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else884) 
                stream_INDENT.add(INDENT65)


                NEWLINE66 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else886) 
                stream_NEWLINE.add(NEWLINE66)


                # grammar/ShyRecognizerFrontend.g:93:28: ( statement )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if ((ID <= LA16_0 <= IF)) :
                        alt16 = 1


                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:93:28: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statement_else888)
                        statement67 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement67.tree)



                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1


                DEDENT68 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else892) 
                stream_DEDENT.add(DEDENT68)


                NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else894) 
                stream_NEWLINE.add(NEWLINE69)


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
                # 94:9: -> ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:94:13: ^( TREE_STATEMENT_ELSE ^( TREE_STATEMENTS ( statement )+ ) )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:95:17: ^( TREE_STATEMENTS ( statement )+ )
                root_2 = self._adaptor.nil()
                root_2 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_2)

                # grammar/ShyRecognizerFrontend.g:95:36: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:99:1: statement_call : ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) ;
    def statement_call(self, ):
        retval = self.statement_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID70 = None
        DO72 = None
        NEWLINE73 = None
        INDENT74 = None
        NEWLINE75 = None
        NEWLINE77 = None
        DEDENT78 = None
        NEWLINE79 = None
        statement_call_args71 = None

        statement_call_args76 = None


        ID70_tree = None
        DO72_tree = None
        NEWLINE73_tree = None
        INDENT74_tree = None
        NEWLINE75_tree = None
        NEWLINE77_tree = None
        DEDENT78_tree = None
        NEWLINE79_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:100:5: ( ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )? -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:100:9: ID ( statement_call_args )? ( DO | NEWLINE ) ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                pass 
                ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call968) 
                stream_ID.add(ID70)


                # grammar/ShyRecognizerFrontend.g:100:12: ( statement_call_args )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if ((EXPRESSION <= LA17_0 <= ID) or LA17_0 == MINUS or LA17_0 == NUMBER) :
                    alt17 = 1
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:100:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call970)
                    statement_call_args71 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args71.tree)





                # grammar/ShyRecognizerFrontend.g:100:34: ( DO | NEWLINE )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == DO) :
                    alt18 = 1
                elif (LA18_0 == NEWLINE) :
                    alt18 = 2
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:100:36: DO
                    pass 
                    DO72 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_call976) 
                    stream_DO.add(DO72)



                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:100:41: NEWLINE
                    pass 
                    NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call980) 
                    stream_NEWLINE.add(NEWLINE73)





                # grammar/ShyRecognizerFrontend.g:101:9: ( INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == INDENT) :
                    alt20 = 1
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:101:11: INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT74 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call994) 
                    stream_INDENT.add(INDENT74)


                    NEWLINE75 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call996) 
                    stream_NEWLINE.add(NEWLINE75)


                    # grammar/ShyRecognizerFrontend.g:101:26: ( statement_call_args NEWLINE )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                            alt19 = 1


                        if alt19 == 1:
                            # grammar/ShyRecognizerFrontend.g:101:28: statement_call_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call1000)
                            statement_call_args76 = self.statement_call_args()

                            self._state.following.pop()
                            stream_statement_call_args.add(statement_call_args76.tree)


                            NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1002) 
                            stream_NEWLINE.add(NEWLINE77)



                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1


                    DEDENT78 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call1008) 
                    stream_DEDENT.add(DEDENT78)


                    NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call1010) 
                    stream_NEWLINE.add(NEWLINE79)





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
                # 102:9: -> ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:102:13: ^( TREE_STATEMENT_CALL ID TREE_STATEMENT_CALL_ARGS ( statement_call_args )* )
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

                # grammar/ShyRecognizerFrontend.g:103:42: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:106:1: statement_call_args : ( statement_call_arg )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_arg80 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:106:21: ( ( statement_call_arg )+ )
                # grammar/ShyRecognizerFrontend.g:106:23: ( statement_call_arg )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:106:23: ( statement_call_arg )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerFrontend.g:106:23: statement_call_arg
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_arg_in_statement_call_args1068)
                        statement_call_arg80 = self.statement_call_arg()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, statement_call_arg80.tree)



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:108:1: statement_call_arg : ( ID | EXPRESSION | num_whole | num_fract );
    def statement_call_arg(self, ):
        retval = self.statement_call_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID81 = None
        EXPRESSION82 = None
        num_whole83 = None

        num_fract84 = None


        ID81_tree = None
        EXPRESSION82_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:109:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt22 = 4
                LA22 = self.input.LA(1)
                if LA22 == ID:
                    alt22 = 1
                elif LA22 == EXPRESSION:
                    alt22 = 2
                elif LA22 == MINUS:
                    LA22_3 = self.input.LA(2)

                    if (LA22_3 == NUMBER) :
                        LA22_4 = self.input.LA(3)

                        if (LA22_4 == DIVIDE) :
                            alt22 = 4
                        elif (LA22_4 == DO or (EXPRESSION <= LA22_4 <= ID) or LA22_4 == MINUS or (NEWLINE <= LA22_4 <= NUMBER)) :
                            alt22 = 3
                        else:
                            nvae = NoViableAltException("", 22, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 22, 3, self.input)

                        raise nvae


                elif LA22 == NUMBER:
                    LA22_4 = self.input.LA(2)

                    if (LA22_4 == DIVIDE) :
                        alt22 = 4
                    elif (LA22_4 == DO or (EXPRESSION <= LA22_4 <= ID) or LA22_4 == MINUS or (NEWLINE <= LA22_4 <= NUMBER)) :
                        alt22 = 3
                    else:
                        nvae = NoViableAltException("", 22, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # grammar/ShyRecognizerFrontend.g:109:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_arg1085)
                    ID81_tree = self._adaptor.createWithPayload(ID81)
                    self._adaptor.addChild(root_0, ID81_tree)




                elif alt22 == 2:
                    # grammar/ShyRecognizerFrontend.g:110:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION82 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_statement_call_arg1095)
                    EXPRESSION82_tree = self._adaptor.createWithPayload(EXPRESSION82)
                    self._adaptor.addChild(root_0, EXPRESSION82_tree)




                elif alt22 == 3:
                    # grammar/ShyRecognizerFrontend.g:111:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_statement_call_arg1105)
                    num_whole83 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole83.tree)



                elif alt22 == 4:
                    # grammar/ShyRecognizerFrontend.g:112:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_statement_call_arg1115)
                    num_fract84 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract84.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:115:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS85 = None
        ID86 = None
        NEWLINE87 = None
        INDENT88 = None
        NEWLINE89 = None
        DEDENT91 = None
        NEWLINE92 = None
        consts_items90 = None


        CONSTS85_tree = None
        ID86_tree = None
        NEWLINE87_tree = None
        INDENT88_tree = None
        NEWLINE89_tree = None
        DEDENT91_tree = None
        NEWLINE92_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:116:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:116:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS85 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1134) 
                stream_CONSTS.add(CONSTS85)


                ID86 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1136) 
                stream_ID.add(ID86)


                NEWLINE87 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1138) 
                stream_NEWLINE.add(NEWLINE87)


                INDENT88 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1148) 
                stream_INDENT.add(INDENT88)


                NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1150) 
                stream_NEWLINE.add(NEWLINE89)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1152)
                consts_items90 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items90.tree)


                DEDENT91 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1154) 
                stream_DEDENT.add(DEDENT91)


                NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1156) 
                stream_NEWLINE.add(NEWLINE92)


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
                # 118:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:118:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:120:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item93 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:120:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:120:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:120:16: ( consts_item )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == ID) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerFrontend.g:120:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1188)
                        consts_item93 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item93.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:121:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID94 = None
        NEWLINE96 = None
        ID97 = None
        NEWLINE99 = None
        ID100 = None
        EXPRESSION101 = None
        NEWLINE102 = None
        num_whole95 = None

        num_fract98 = None


        ID94_tree = None
        NEWLINE96_tree = None
        ID97_tree = None
        NEWLINE99_tree = None
        ID100_tree = None
        EXPRESSION101_tree = None
        NEWLINE102_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:122:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt24 = 3
                LA24_0 = self.input.LA(1)

                if (LA24_0 == ID) :
                    LA24 = self.input.LA(2)
                    if LA24 == EXPRESSION:
                        alt24 = 3
                    elif LA24 == MINUS:
                        LA24_3 = self.input.LA(3)

                        if (LA24_3 == NUMBER) :
                            LA24_4 = self.input.LA(4)

                            if (LA24_4 == DIVIDE) :
                                alt24 = 2
                            elif (LA24_4 == NEWLINE) :
                                alt24 = 1
                            else:
                                nvae = NoViableAltException("", 24, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 24, 3, self.input)

                            raise nvae


                    elif LA24 == NUMBER:
                        LA24_4 = self.input.LA(3)

                        if (LA24_4 == DIVIDE) :
                            alt24 = 2
                        elif (LA24_4 == NEWLINE) :
                            alt24 = 1
                        else:
                            nvae = NoViableAltException("", 24, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 24, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerFrontend.g:122:9: ID num_whole NEWLINE
                    pass 
                    ID94 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1204) 
                    stream_ID.add(ID94)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1206)
                    num_whole95 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole95.tree)


                    NEWLINE96 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1208) 
                    stream_NEWLINE.add(NEWLINE96)


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
                    # 122:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:122:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt24 == 2:
                    # grammar/ShyRecognizerFrontend.g:123:9: ID num_fract NEWLINE
                    pass 
                    ID97 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1230) 
                    stream_ID.add(ID97)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1232)
                    num_fract98 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract98.tree)


                    NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1234) 
                    stream_NEWLINE.add(NEWLINE99)


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
                    # 123:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:123:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt24 == 3:
                    # grammar/ShyRecognizerFrontend.g:124:9: ID EXPRESSION NEWLINE
                    pass 
                    ID100 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1256) 
                    stream_ID.add(ID100)


                    EXPRESSION101 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1258) 
                    stream_EXPRESSION.add(EXPRESSION101)


                    NEWLINE102 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1260) 
                    stream_NEWLINE.add(NEWLINE102)


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
                    # 124:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:124:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:127:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES103 = None
        ID104 = None
        NEWLINE105 = None
        INDENT106 = None
        NEWLINE107 = None
        DEDENT109 = None
        NEWLINE110 = None
        types_items108 = None


        TYPES103_tree = None
        ID104_tree = None
        NEWLINE105_tree = None
        INDENT106_tree = None
        NEWLINE107_tree = None
        DEDENT109_tree = None
        NEWLINE110_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:128:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:128:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES103 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1291) 
                stream_TYPES.add(TYPES103)


                ID104 = self.match(self.input, ID, self.FOLLOW_ID_in_types1293) 
                stream_ID.add(ID104)


                NEWLINE105 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1295) 
                stream_NEWLINE.add(NEWLINE105)


                INDENT106 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1305) 
                stream_INDENT.add(INDENT106)


                NEWLINE107 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1307) 
                stream_NEWLINE.add(NEWLINE107)


                self._state.following.append(self.FOLLOW_types_items_in_types1309)
                types_items108 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items108.tree)


                DEDENT109 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1311) 
                stream_DEDENT.add(DEDENT109)


                NEWLINE110 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1313) 
                stream_NEWLINE.add(NEWLINE110)


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
                # 130:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:130:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:132:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item111 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:132:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:132:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:132:15: ( types_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ID) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:132:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1345)
                        types_item111 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item111.tree)



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

    # $ANTLR end "types_items"


    class types_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.types_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerFrontend.g:133:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID112 = None
        vars_hint113 = None


        ID112_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:133:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:133:14: ID vars_hint
                pass 
                ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1355) 
                stream_ID.add(ID112)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1357)
                vars_hint113 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint113.tree)


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
                # 133:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:133:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:135:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE115 = None
        INDENT116 = None
        NEWLINE117 = None
        NEWLINE119 = None
        DEDENT120 = None
        NEWLINE121 = None
        var_hint114 = None

        var_hint118 = None


        NEWLINE115_tree = None
        INDENT116_tree = None
        NEWLINE117_tree = None
        NEWLINE119_tree = None
        DEDENT120_tree = None
        NEWLINE121_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:136:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:136:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:136:9: ( var_hint )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == CURLY_OPEN or LA26_0 == ID) :
                    alt26 = 1
                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:136:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1384)
                    var_hint114 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint114.tree)





                NEWLINE115 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1388) 
                stream_NEWLINE.add(NEWLINE115)


                # grammar/ShyRecognizerFrontend.g:137:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == INDENT) :
                    alt28 = 1
                if alt28 == 1:
                    # grammar/ShyRecognizerFrontend.g:137:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT116 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1400) 
                    stream_INDENT.add(INDENT116)


                    NEWLINE117 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1402) 
                    stream_NEWLINE.add(NEWLINE117)


                    # grammar/ShyRecognizerFrontend.g:137:26: ( var_hint NEWLINE )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == CURLY_OPEN or LA27_0 == ID) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:137:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1406)
                            var_hint118 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint118.tree)


                            NEWLINE119 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1408) 
                            stream_NEWLINE.add(NEWLINE119)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    DEDENT120 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1414) 
                    stream_DEDENT.add(DEDENT120)


                    NEWLINE121 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1416) 
                    stream_NEWLINE.add(NEWLINE121)





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
                # 138:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:138:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:140:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE126 = None
        INDENT127 = None
        NEWLINE128 = None
        NEWLINE130 = None
        DEDENT131 = None
        var122 = None

        hint123 = None

        var124 = None

        hint125 = None

        var129 = None


        NEWLINE126_tree = None
        INDENT127_tree = None
        NEWLINE128_tree = None
        NEWLINE130_tree = None
        DEDENT131_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:141:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt33 = 3
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:141:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:141:9: ( var )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:141:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1455)
                            var122 = self.var()

                            self._state.following.pop()
                            stream_var.add(var122.tree)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


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
                    # 142:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:142:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:142:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt33 == 2:
                    # grammar/ShyRecognizerFrontend.g:143:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1490)
                    hint123 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint123.tree)


                    # grammar/ShyRecognizerFrontend.g:143:14: ( var )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == ID) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:143:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1492)
                            var124 = self.var()

                            self._state.following.pop()
                            stream_var.add(var124.tree)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


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
                    # 144:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:144:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:144:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt33 == 3:
                    # grammar/ShyRecognizerFrontend.g:145:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1526)
                    hint125 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint125.tree)


                    NEWLINE126 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1528) 
                    stream_NEWLINE.add(NEWLINE126)


                    INDENT127 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1530) 
                    stream_INDENT.add(INDENT127)


                    NEWLINE128 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1532) 
                    stream_NEWLINE.add(NEWLINE128)


                    # grammar/ShyRecognizerFrontend.g:145:37: ( ( var )+ NEWLINE )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:145:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:145:39: ( var )+
                            cnt31 = 0
                            while True: #loop31
                                alt31 = 2
                                LA31_0 = self.input.LA(1)

                                if (LA31_0 == ID) :
                                    alt31 = 1


                                if alt31 == 1:
                                    # grammar/ShyRecognizerFrontend.g:145:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1536)
                                    var129 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var129.tree)



                                else:
                                    if cnt31 >= 1:
                                        break #loop31

                                    eee = EarlyExitException(31, self.input)
                                    raise eee

                                cnt31 += 1


                            NEWLINE130 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1540) 
                            stream_NEWLINE.add(NEWLINE130)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


                    DEDENT131 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1546) 
                    stream_DEDENT.add(DEDENT131)


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
                    # 146:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:146:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:146:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:148:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID132 = None

        ID132_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:148:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:148:7: ID
                pass 
                ID132 = self.match(self.input, ID, self.FOLLOW_ID_in_var1580) 
                stream_ID.add(ID132)


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
                # 148:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:148:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:150:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN133 = None
        ID134 = None
        CURLY_CLOSE135 = None
        CURLY_OPEN136 = None
        ID137 = None
        CURLY_CLOSE139 = None
        hint_arg138 = None


        CURLY_OPEN133_tree = None
        ID134_tree = None
        CURLY_CLOSE135_tree = None
        CURLY_OPEN136_tree = None
        ID137_tree = None
        CURLY_CLOSE139_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:151:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == CURLY_OPEN) :
                    LA35_1 = self.input.LA(2)

                    if (LA35_1 == ID) :
                        LA35_2 = self.input.LA(3)

                        if (LA35_2 == CURLY_CLOSE) :
                            alt35 = 1
                        elif (LA35_2 == ID or LA35_2 == UNDERSCORE) :
                            alt35 = 2
                        else:
                            nvae = NoViableAltException("", 35, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 35, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae


                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:151:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN133 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1605) 
                    stream_CURLY_OPEN.add(CURLY_OPEN133)


                    ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1607) 
                    stream_ID.add(ID134)


                    CURLY_CLOSE135 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1609) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE135)


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
                    # 151:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:151:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:152:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN136 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1629) 
                    stream_CURLY_OPEN.add(CURLY_OPEN136)


                    ID137 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1631) 
                    stream_ID.add(ID137)


                    # grammar/ShyRecognizerFrontend.g:152:23: ( hint_arg )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == ID or LA34_0 == UNDERSCORE) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerFrontend.g:152:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1633)
                            hint_arg138 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg138.tree)



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


                    CURLY_CLOSE139 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1637) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE139)


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
                    # 152:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:152:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:152:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:154:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set140 = None

        set140_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:154:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set140 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set140))

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
    # grammar/ShyRecognizerFrontend.g:156:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS141 = None
        NUMBER142 = None

        MINUS141_tree = None
        NUMBER142_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:156:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:156:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:156:13: ( MINUS )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == MINUS) :
                    alt36 = 1
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:156:13: MINUS
                    pass 
                    MINUS141 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1676)
                    MINUS141_tree = self._adaptor.createWithPayload(MINUS141)
                    self._adaptor.addChild(root_0, MINUS141_tree)






                NUMBER142 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1680)
                NUMBER142_tree = self._adaptor.createWithPayload(NUMBER142)
                self._adaptor.addChild(root_0, NUMBER142_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:157:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS143 = None
        NUMBER144 = None
        DIVIDE145 = None
        NUMBER146 = None

        MINUS143_tree = None
        NUMBER144_tree = None
        DIVIDE145_tree = None
        NUMBER146_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:157:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:157:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:157:13: ( MINUS )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == MINUS) :
                    alt37 = 1
                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:157:13: MINUS
                    pass 
                    MINUS143 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1688)
                    MINUS143_tree = self._adaptor.createWithPayload(MINUS143)
                    self._adaptor.addChild(root_0, MINUS143_tree)






                NUMBER144 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1692)
                NUMBER144_tree = self._adaptor.createWithPayload(NUMBER144)
                self._adaptor.addChild(root_0, NUMBER144_tree)



                DIVIDE145 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1694)
                DIVIDE145_tree = self._adaptor.createWithPayload(DIVIDE145)
                self._adaptor.addChild(root_0, DIVIDE145_tree)



                NUMBER146 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1696)
                NUMBER146_tree = self._adaptor.createWithPayload(NUMBER146)
                self._adaptor.addChild(root_0, NUMBER146_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\1\12\1\uffff\1\21\1\11\1\21\1\11\2\uffff\1\21"
        )

    DFA33_max = DFA.unpack(
        u"\1\21\1\uffff\1\21\1\74\1\26\1\74\2\uffff\1\26"
        )

    DFA33_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA33_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA33_transition = [
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

    # class definition for DFA #33

    class DFA33(DFA):
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
    FOLLOW_statement_call_in_statement_if_head610 = frozenset([13, 22])
    FOLLOW_DO_in_statement_if_head612 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_if_head616 = frozenset([19])
    FOLLOW_INDENT_in_statement_if_head630 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_if_head632 = frozenset([17, 18])
    FOLLOW_statement_in_statement_if_head634 = frozenset([11, 17, 18])
    FOLLOW_DEDENT_in_statement_if_head638 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_if_head640 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif738 = frozenset([17])
    FOLLOW_statement_call_in_statement_elif740 = frozenset([13, 22])
    FOLLOW_DO_in_statement_elif742 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_elif746 = frozenset([19])
    FOLLOW_INDENT_in_statement_elif760 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_elif762 = frozenset([17, 18])
    FOLLOW_statement_in_statement_elif764 = frozenset([11, 17, 18])
    FOLLOW_DEDENT_in_statement_elif768 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_elif770 = frozenset([1])
    FOLLOW_ELSE_in_statement_else868 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_else870 = frozenset([19])
    FOLLOW_INDENT_in_statement_else884 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_else886 = frozenset([17, 18])
    FOLLOW_statement_in_statement_else888 = frozenset([11, 17, 18])
    FOLLOW_DEDENT_in_statement_else892 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_else894 = frozenset([1])
    FOLLOW_ID_in_statement_call968 = frozenset([13, 16, 17, 20, 22, 23])
    FOLLOW_statement_call_args_in_statement_call970 = frozenset([13, 22])
    FOLLOW_DO_in_statement_call976 = frozenset([1, 19])
    FOLLOW_NEWLINE_in_statement_call980 = frozenset([1, 19])
    FOLLOW_INDENT_in_statement_call994 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_call996 = frozenset([16, 17, 20, 23])
    FOLLOW_statement_call_args_in_statement_call1000 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_call1002 = frozenset([11, 16, 17, 20, 23])
    FOLLOW_DEDENT_in_statement_call1008 = frozenset([22])
    FOLLOW_NEWLINE_in_statement_call1010 = frozenset([1])
    FOLLOW_statement_call_arg_in_statement_call_args1068 = frozenset([1, 16, 17, 20, 23])
    FOLLOW_ID_in_statement_call_arg1085 = frozenset([1])
    FOLLOW_EXPRESSION_in_statement_call_arg1095 = frozenset([1])
    FOLLOW_num_whole_in_statement_call_arg1105 = frozenset([1])
    FOLLOW_num_fract_in_statement_call_arg1115 = frozenset([1])
    FOLLOW_CONSTS_in_consts1134 = frozenset([17])
    FOLLOW_ID_in_consts1136 = frozenset([22])
    FOLLOW_NEWLINE_in_consts1138 = frozenset([19])
    FOLLOW_INDENT_in_consts1148 = frozenset([22])
    FOLLOW_NEWLINE_in_consts1150 = frozenset([17])
    FOLLOW_consts_items_in_consts1152 = frozenset([11])
    FOLLOW_DEDENT_in_consts1154 = frozenset([22])
    FOLLOW_NEWLINE_in_consts1156 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1188 = frozenset([1, 17])
    FOLLOW_ID_in_consts_item1204 = frozenset([20, 23])
    FOLLOW_num_whole_in_consts_item1206 = frozenset([22])
    FOLLOW_NEWLINE_in_consts_item1208 = frozenset([1])
    FOLLOW_ID_in_consts_item1230 = frozenset([20, 23])
    FOLLOW_num_fract_in_consts_item1232 = frozenset([22])
    FOLLOW_NEWLINE_in_consts_item1234 = frozenset([1])
    FOLLOW_ID_in_consts_item1256 = frozenset([16])
    FOLLOW_EXPRESSION_in_consts_item1258 = frozenset([22])
    FOLLOW_NEWLINE_in_consts_item1260 = frozenset([1])
    FOLLOW_TYPES_in_types1291 = frozenset([17])
    FOLLOW_ID_in_types1293 = frozenset([22])
    FOLLOW_NEWLINE_in_types1295 = frozenset([19])
    FOLLOW_INDENT_in_types1305 = frozenset([22])
    FOLLOW_NEWLINE_in_types1307 = frozenset([17])
    FOLLOW_types_items_in_types1309 = frozenset([11])
    FOLLOW_DEDENT_in_types1311 = frozenset([22])
    FOLLOW_NEWLINE_in_types1313 = frozenset([1])
    FOLLOW_types_item_in_types_items1345 = frozenset([1, 17])
    FOLLOW_ID_in_types_item1355 = frozenset([10, 17, 22])
    FOLLOW_vars_hint_in_types_item1357 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1384 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1388 = frozenset([1, 19])
    FOLLOW_INDENT_in_vars_hint1400 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1402 = frozenset([10, 17])
    FOLLOW_var_hint_in_vars_hint1406 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1408 = frozenset([10, 11, 17])
    FOLLOW_DEDENT_in_vars_hint1414 = frozenset([22])
    FOLLOW_NEWLINE_in_vars_hint1416 = frozenset([1])
    FOLLOW_var_in_var_hint1455 = frozenset([1, 17])
    FOLLOW_hint_in_var_hint1490 = frozenset([17])
    FOLLOW_var_in_var_hint1492 = frozenset([1, 17])
    FOLLOW_hint_in_var_hint1526 = frozenset([22])
    FOLLOW_NEWLINE_in_var_hint1528 = frozenset([19])
    FOLLOW_INDENT_in_var_hint1530 = frozenset([22])
    FOLLOW_NEWLINE_in_var_hint1532 = frozenset([17])
    FOLLOW_var_in_var_hint1536 = frozenset([17, 22])
    FOLLOW_NEWLINE_in_var_hint1540 = frozenset([11, 17])
    FOLLOW_DEDENT_in_var_hint1546 = frozenset([1])
    FOLLOW_ID_in_var1580 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1605 = frozenset([17])
    FOLLOW_ID_in_hint1607 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint1609 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1629 = frozenset([17])
    FOLLOW_ID_in_hint1631 = frozenset([17, 60])
    FOLLOW_hint_arg_in_hint1633 = frozenset([9, 17, 60])
    FOLLOW_CURLY_CLOSE_in_hint1637 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1676 = frozenset([23])
    FOLLOW_NUMBER_in_num_whole1680 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1688 = frozenset([23])
    FOLLOW_NUMBER_in_num_fract1692 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract1694 = frozenset([23])
    FOLLOW_NUMBER_in_num_fract1696 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
