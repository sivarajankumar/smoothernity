# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-27 07:53:09

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
MESSAGES=22
MINUS=23
MODULE=24
NEWLINE=25
NUMBER=26
OPS=27
PASTE=28
PROC=29
REPLACE=30
STATELESS=31
STRING=32
TREE_ARBITRARY_TOKEN=33
TREE_CONDITION_ALL=34
TREE_CONDITION_ANY=35
TREE_CONSTS=36
TREE_COPY=37
TREE_COPY_PASTE=38
TREE_EXPRESSION=39
TREE_HINT=40
TREE_HINT_NONE=41
TREE_MODULE=42
TREE_NUM_FRACT=43
TREE_NUM_WHOLE=44
TREE_PASTE=45
TREE_PASTE_REPLACE=46
TREE_PASTE_WITH=47
TREE_PROC=48
TREE_PROC_ARGS=49
TREE_PROC_VARS=50
TREE_STATELESS=51
TREE_STATEMENTS=52
TREE_STATEMENT_ASSIGN=53
TREE_STATEMENT_CALL=54
TREE_STATEMENT_ELIF=55
TREE_STATEMENT_ELSE=56
TREE_STATEMENT_IF=57
TREE_STATEMENT_WITH=58
TREE_TYPES=59
TREE_TYPES_ITEM=60
TREE_VAR=61
TREE_VARS_HINT=62
TREE_VAR_HINT=63
TYPES=64
UNDERSCORE=65
VARS=66
WHITESPACE=67
WITH=68

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "NEWLINE", 
    "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "STATELESS", "STRING", 
    "TREE_ARBITRARY_TOKEN", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WITH", "TREE_TYPES", 
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

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )

        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

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
                    # elements: proc_ops, proc_vars, ID, proc_args
                    # token labels: 
                    # rule labels: retval
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
    # grammar/ShyRecognizerFrontend.g:52:1: proc_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
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
        statements37 = None


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
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:53:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
                # grammar/ShyRecognizerFrontend.g:53:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                OPS33 = self.match(self.input, OPS, self.FOLLOW_OPS_in_proc_ops396) 
                stream_OPS.add(OPS33)


                NEWLINE34 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops398) 
                stream_NEWLINE.add(NEWLINE34)


                INDENT35 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc_ops400) 
                stream_INDENT.add(INDENT35)


                NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops402) 
                stream_NEWLINE.add(NEWLINE36)


                self._state.following.append(self.FOLLOW_statements_in_proc_ops404)
                statements37 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements37.tree)


                DEDENT38 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc_ops406) 
                stream_DEDENT.add(DEDENT38)


                NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops408) 
                stream_NEWLINE.add(NEWLINE39)


                # AST Rewrite
                # elements: statements
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 54:9: -> statements
                self._adaptor.addChild(root_0, stream_statements.nextTree())




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
    # grammar/ShyRecognizerFrontend.g:57:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE41 = None
        statement_call_single_line40 = None

        statement_call_multi_line42 = None

        statement_if43 = None

        statement_assign44 = None

        statement_with45 = None


        NEWLINE41_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:58:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_with )
                alt8 = 5
                alt8 = self.dfa8.predict(self.input)
                if alt8 == 1:
                    # grammar/ShyRecognizerFrontend.g:58:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement439)
                    statement_call_single_line40 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line40.tree)


                    NEWLINE41 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement441) 
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




                elif alt8 == 2:
                    # grammar/ShyRecognizerFrontend.g:60:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement467)
                    statement_call_multi_line42 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line42.tree)



                elif alt8 == 3:
                    # grammar/ShyRecognizerFrontend.g:61:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement477)
                    statement_if43 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if43.tree)



                elif alt8 == 4:
                    # grammar/ShyRecognizerFrontend.g:62:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement487)
                    statement_assign44 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign44.tree)



                elif alt8 == 5:
                    # grammar/ShyRecognizerFrontend.g:63:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement497)
                    statement_with45 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with45.tree)



                retval.stop = self.input.LT(-1)


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


    class statements_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statements_return, self).__init__()

            self.tree = None





    # $ANTLR start "statements"
    # grammar/ShyRecognizerFrontend.g:66:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement46 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:67:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:67:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:67:9: ( statement )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if ((ID <= LA9_0 <= IF) or LA9_0 == WITH) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerFrontend.g:67:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements516)
                        statement46 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement46.tree)



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1


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
                # 68:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:68:12: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:68:31: ( statement )+
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

    # $ANTLR end "statements"


    class statement_with_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_with_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_with"
    # grammar/ShyRecognizerFrontend.g:71:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH47 = None
        ID48 = None
        NEWLINE49 = None
        INDENT50 = None
        NEWLINE51 = None
        DEDENT53 = None
        NEWLINE54 = None
        statements52 = None


        WITH47_tree = None
        ID48_tree = None
        NEWLINE49_tree = None
        INDENT50_tree = None
        NEWLINE51_tree = None
        DEDENT53_tree = None
        NEWLINE54_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:72:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:72:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH47 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with557) 
                stream_WITH.add(WITH47)


                ID48 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with559) 
                stream_ID.add(ID48)


                NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with561) 
                stream_NEWLINE.add(NEWLINE49)


                INDENT50 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with571) 
                stream_INDENT.add(INDENT50)


                NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with573) 
                stream_NEWLINE.add(NEWLINE51)


                self._state.following.append(self.FOLLOW_statements_in_statement_with575)
                statements52 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements52.tree)


                DEDENT53 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with577) 
                stream_DEDENT.add(DEDENT53)


                NEWLINE54 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with579) 
                stream_NEWLINE.add(NEWLINE54)


                # AST Rewrite
                # elements: ID, statements
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 74:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:74:13: ^( TREE_STATEMENT_WITH ID statements )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_WITH, "TREE_STATEMENT_WITH")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_statements.nextTree())

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

    # $ANTLR end "statement_with"


    class statement_assign_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_assign_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_assign"
    # grammar/ShyRecognizerFrontend.g:77:1: statement_assign : ID ARROW_LEFT arbitrary_value NEWLINE -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID ) ;
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID55 = None
        ARROW_LEFT56 = None
        NEWLINE58 = None
        arbitrary_value57 = None


        ID55_tree = None
        ARROW_LEFT56_tree = None
        NEWLINE58_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:78:5: ( ID ARROW_LEFT arbitrary_value NEWLINE -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID ) )
                # grammar/ShyRecognizerFrontend.g:78:9: ID ARROW_LEFT arbitrary_value NEWLINE
                pass 
                ID55 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign619) 
                stream_ID.add(ID55)


                ARROW_LEFT56 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign621) 
                stream_ARROW_LEFT.add(ARROW_LEFT56)


                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign623)
                arbitrary_value57 = self.arbitrary_value()

                self._state.following.pop()
                stream_arbitrary_value.add(arbitrary_value57.tree)


                NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign625) 
                stream_NEWLINE.add(NEWLINE58)


                # AST Rewrite
                # elements: arbitrary_value, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 79:9: -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID )
                # grammar/ShyRecognizerFrontend.g:79:13: ^( TREE_STATEMENT_ASSIGN arbitrary_value ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                , root_1)

                self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())

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

    # $ANTLR end "statement_assign"


    class statement_if_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_if_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerFrontend.g:82:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head59 = None

        statement_elif60 = None

        statement_else61 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:83:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if665)
                statement_if_head59 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head59.tree)


                # grammar/ShyRecognizerFrontend.g:84:9: ( statement_elif )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ELIF) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:84:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if675)
                        statement_elif60 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif60.tree)



                    else:
                        break #loop10


                # grammar/ShyRecognizerFrontend.g:85:9: ( statement_else )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == ELSE) :
                    alt11 = 1
                if alt11 == 1:
                    # grammar/ShyRecognizerFrontend.g:85:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if687)
                    statement_else61 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else61.tree)





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
                # 86:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:86:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:88:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:89:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:93:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF62 = None
        statement_elif_body63 = None


        IF62_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:94:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:94:9: IF statement_elif_body
                pass 
                IF62 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head795) 
                stream_IF.add(IF62)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head797)
                statement_elif_body63 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body63.tree)


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
                # 95:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:98:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF64 = None
        statement_elif_body65 = None


        ELIF64_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:99:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:99:9: ELIF statement_elif_body
                pass 
                ELIF64 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif829) 
                stream_ELIF.add(ELIF64)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif831)
                statement_elif_body65 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body65.tree)


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
                # 100:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:103:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE67 = None
        DO68 = None
        NEWLINE69 = None
        INDENT70 = None
        NEWLINE71 = None
        DEDENT73 = None
        NEWLINE74 = None
        condition66 = None

        statements72 = None


        NEWLINE67_tree = None
        DO68_tree = None
        NEWLINE69_tree = None
        INDENT70_tree = None
        NEWLINE71_tree = None
        DEDENT73_tree = None
        NEWLINE74_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:104:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:104:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body863)
                condition66 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition66.tree)


                # grammar/ShyRecognizerFrontend.g:104:19: ( NEWLINE )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == NEWLINE) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:104:19: NEWLINE
                    pass 
                    NEWLINE67 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body865) 
                    stream_NEWLINE.add(NEWLINE67)





                DO68 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body869) 
                stream_DO.add(DO68)


                NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body871) 
                stream_NEWLINE.add(NEWLINE69)


                INDENT70 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body885) 
                stream_INDENT.add(INDENT70)


                NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body887) 
                stream_NEWLINE.add(NEWLINE71)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body889)
                statements72 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements72.tree)


                DEDENT73 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body891) 
                stream_DEDENT.add(DEDENT73)


                NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body893) 
                stream_NEWLINE.add(NEWLINE74)


                # AST Rewrite
                # elements: statements, condition
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 106:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:106:13: ^( TREE_STATEMENT_ELIF condition statements )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELIF, "TREE_STATEMENT_ELIF")
                , root_1)

                self._adaptor.addChild(root_1, stream_condition.nextTree())

                self._adaptor.addChild(root_1, stream_statements.nextTree())

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
    # grammar/ShyRecognizerFrontend.g:109:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE75 = None
        NEWLINE76 = None
        INDENT77 = None
        NEWLINE78 = None
        DEDENT80 = None
        NEWLINE81 = None
        statements79 = None


        ELSE75_tree = None
        NEWLINE76_tree = None
        INDENT77_tree = None
        NEWLINE78_tree = None
        DEDENT80_tree = None
        NEWLINE81_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:110:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:110:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE75 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else933) 
                stream_ELSE.add(ELSE75)


                NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else935) 
                stream_NEWLINE.add(NEWLINE76)


                INDENT77 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else949) 
                stream_INDENT.add(INDENT77)


                NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else951) 
                stream_NEWLINE.add(NEWLINE78)


                self._state.following.append(self.FOLLOW_statements_in_statement_else953)
                statements79 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements79.tree)


                DEDENT80 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else955) 
                stream_DEDENT.add(DEDENT80)


                NEWLINE81 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else957) 
                stream_NEWLINE.add(NEWLINE81)


                # AST Rewrite
                # elements: statements
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 112:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:112:13: ^( TREE_STATEMENT_ELSE statements )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_ELSE, "TREE_STATEMENT_ELSE")
                , root_1)

                self._adaptor.addChild(root_1, stream_statements.nextTree())

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
    # grammar/ShyRecognizerFrontend.g:115:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY83 = None
        ALL85 = None
        condition_call82 = None

        condition_calls84 = None

        condition_calls86 = None


        ANY83_tree = None
        ALL85_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:116:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt13 = 3
                LA13 = self.input.LA(1)
                if LA13 == ID:
                    alt13 = 1
                elif LA13 == ANY:
                    alt13 = 2
                elif LA13 == ALL:
                    alt13 = 3
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # grammar/ShyRecognizerFrontend.g:116:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition995)
                    condition_call82 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call82.tree)


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
                    # 117:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:117:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 2:
                    # grammar/ShyRecognizerFrontend.g:118:9: ANY condition_calls
                    pass 
                    ANY83 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1024) 
                    stream_ANY.add(ANY83)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1026)
                    condition_calls84 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls84.tree)


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
                    # 119:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:119:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 3:
                    # grammar/ShyRecognizerFrontend.g:120:9: ALL condition_calls
                    pass 
                    ALL85 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1055) 
                    stream_ALL.add(ALL85)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1057)
                    condition_calls86 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls86.tree)


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
                    # 121:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:121:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:124:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE88 = None
        INDENT89 = None
        NEWLINE90 = None
        DEDENT92 = None
        NEWLINE93 = None
        condition_call87 = None

        condition_call_line91 = None


        NEWLINE88_tree = None
        INDENT89_tree = None
        NEWLINE90_tree = None
        DEDENT92_tree = None
        NEWLINE93_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:125:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == ID) :
                    alt15 = 1
                elif (LA15_0 == NEWLINE) :
                    alt15 = 2
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:125:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1095)
                    condition_call87 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call87.tree)



                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:126:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1105) 
                    stream_NEWLINE.add(NEWLINE88)


                    INDENT89 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1107) 
                    stream_INDENT.add(INDENT89)


                    NEWLINE90 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1109) 
                    stream_NEWLINE.add(NEWLINE90)


                    # grammar/ShyRecognizerFrontend.g:126:32: ( condition_call_line )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == ID) :
                            alt14 = 1


                        if alt14 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1111)
                            condition_call_line91 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line91.tree)



                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                    DEDENT92 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1115) 
                    stream_DEDENT.add(DEDENT92)


                    NEWLINE93 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1117) 
                    stream_NEWLINE.add(NEWLINE93)


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
                    # 127:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:127:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:130:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line94 = None

        statement_call_multi_line95 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:131:5: ( statement_call_single_line | statement_call_multi_line )
                alt16 = 2
                alt16 = self.dfa16.predict(self.input)
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:131:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1151)
                    statement_call_single_line94 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line94.tree)



                elif alt16 == 2:
                    # grammar/ShyRecognizerFrontend.g:132:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1161)
                    statement_call_multi_line95 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line95.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:135:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE97 = None
        statement_call_single_line96 = None

        statement_call_multi_line98 = None


        NEWLINE97_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:136:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt17 = 2
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:136:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1180)
                    statement_call_single_line96 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line96.tree)


                    NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1182) 
                    stream_NEWLINE.add(NEWLINE97)


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
                    # 137:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:138:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1208)
                    statement_call_multi_line98 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line98.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:141:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID99 = None
        statement_call_args100 = None


        ID99_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:142:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:142:9: ID ( statement_call_args )?
                pass 
                ID99 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1227) 
                stream_ID.add(ID99)


                # grammar/ShyRecognizerFrontend.g:142:12: ( statement_call_args )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if ((EXPRESSION <= LA18_0 <= ID) or LA18_0 == MINUS or LA18_0 == NUMBER) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:142:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1229)
                    statement_call_args100 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args100.tree)





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
                # 143:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:143:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:143:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:146:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID101 = None
        NEWLINE103 = None
        INDENT104 = None
        NEWLINE105 = None
        NEWLINE107 = None
        DEDENT108 = None
        NEWLINE109 = None
        statement_call_args102 = None

        statement_call_args106 = None


        ID101_tree = None
        NEWLINE103_tree = None
        INDENT104_tree = None
        NEWLINE105_tree = None
        NEWLINE107_tree = None
        DEDENT108_tree = None
        NEWLINE109_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:147:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:147:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID101 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1273) 
                stream_ID.add(ID101)


                # grammar/ShyRecognizerFrontend.g:147:12: ( statement_call_args )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:147:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1275)
                    statement_call_args102 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args102.tree)





                NEWLINE103 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1279) 
                stream_NEWLINE.add(NEWLINE103)


                INDENT104 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1289) 
                stream_INDENT.add(INDENT104)


                NEWLINE105 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1291) 
                stream_NEWLINE.add(NEWLINE105)


                # grammar/ShyRecognizerFrontend.g:148:24: ( statement_call_args NEWLINE )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerFrontend.g:148:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1295)
                        statement_call_args106 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args106.tree)


                        NEWLINE107 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1297) 
                        stream_NEWLINE.add(NEWLINE107)



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1


                DEDENT108 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1303) 
                stream_DEDENT.add(DEDENT108)


                NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1305) 
                stream_NEWLINE.add(NEWLINE109)


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
                # 149:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:149:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:149:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:152:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value110 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:152:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:152:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:152:23: ( arbitrary_value )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerFrontend.g:152:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1341)
                        arbitrary_value110 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value110.tree)



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


    class arbitrary_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.arbitrary_value_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerFrontend.g:154:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID111 = None
        EXPRESSION112 = None
        num_whole113 = None

        num_fract114 = None


        ID111_tree = None
        EXPRESSION112_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:155:5: ( ID | EXPRESSION | num_whole | num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:155:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID111 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1358)
                    ID111_tree = self._adaptor.createWithPayload(ID111)
                    self._adaptor.addChild(root_0, ID111_tree)




                elif alt22 == 2:
                    # grammar/ShyRecognizerFrontend.g:156:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION112 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1368)
                    EXPRESSION112_tree = self._adaptor.createWithPayload(EXPRESSION112)
                    self._adaptor.addChild(root_0, EXPRESSION112_tree)




                elif alt22 == 3:
                    # grammar/ShyRecognizerFrontend.g:157:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1378)
                    num_whole113 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole113.tree)



                elif alt22 == 4:
                    # grammar/ShyRecognizerFrontend.g:158:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1388)
                    num_fract114 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract114.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "arbitrary_value"


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:161:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS115 = None
        ID116 = None
        NEWLINE117 = None
        INDENT118 = None
        NEWLINE119 = None
        DEDENT121 = None
        NEWLINE122 = None
        consts_items120 = None


        CONSTS115_tree = None
        ID116_tree = None
        NEWLINE117_tree = None
        INDENT118_tree = None
        NEWLINE119_tree = None
        DEDENT121_tree = None
        NEWLINE122_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:162:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:162:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS115 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1407) 
                stream_CONSTS.add(CONSTS115)


                ID116 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1409) 
                stream_ID.add(ID116)


                NEWLINE117 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1411) 
                stream_NEWLINE.add(NEWLINE117)


                INDENT118 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1421) 
                stream_INDENT.add(INDENT118)


                NEWLINE119 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1423) 
                stream_NEWLINE.add(NEWLINE119)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1425)
                consts_items120 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items120.tree)


                DEDENT121 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1427) 
                stream_DEDENT.add(DEDENT121)


                NEWLINE122 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1429) 
                stream_NEWLINE.add(NEWLINE122)


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
                # 164:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:164:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:166:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item123 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:166:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:166:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:166:16: ( consts_item )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == ID) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerFrontend.g:166:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1461)
                        consts_item123 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item123.tree)



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
    # grammar/ShyRecognizerFrontend.g:167:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID124 = None
        NEWLINE126 = None
        ID127 = None
        NEWLINE129 = None
        ID130 = None
        EXPRESSION131 = None
        NEWLINE132 = None
        num_whole125 = None

        num_fract128 = None


        ID124_tree = None
        NEWLINE126_tree = None
        ID127_tree = None
        NEWLINE129_tree = None
        ID130_tree = None
        EXPRESSION131_tree = None
        NEWLINE132_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:168:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerFrontend.g:168:9: ID num_whole NEWLINE
                    pass 
                    ID124 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1477) 
                    stream_ID.add(ID124)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1479)
                    num_whole125 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole125.tree)


                    NEWLINE126 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1481) 
                    stream_NEWLINE.add(NEWLINE126)


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
                    # 168:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:168:33: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/ShyRecognizerFrontend.g:169:9: ID num_fract NEWLINE
                    pass 
                    ID127 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1503) 
                    stream_ID.add(ID127)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1505)
                    num_fract128 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract128.tree)


                    NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1507) 
                    stream_NEWLINE.add(NEWLINE129)


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
                    # 169:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:169:33: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:170:9: ID EXPRESSION NEWLINE
                    pass 
                    ID130 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1529) 
                    stream_ID.add(ID130)


                    EXPRESSION131 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1531) 
                    stream_EXPRESSION.add(EXPRESSION131)


                    NEWLINE132 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1533) 
                    stream_NEWLINE.add(NEWLINE132)


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
                    # 170:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:170:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:173:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES133 = None
        ID134 = None
        NEWLINE135 = None
        INDENT136 = None
        NEWLINE137 = None
        DEDENT139 = None
        NEWLINE140 = None
        types_items138 = None


        TYPES133_tree = None
        ID134_tree = None
        NEWLINE135_tree = None
        INDENT136_tree = None
        NEWLINE137_tree = None
        DEDENT139_tree = None
        NEWLINE140_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:174:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES133 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1564) 
                stream_TYPES.add(TYPES133)


                ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_types1566) 
                stream_ID.add(ID134)


                NEWLINE135 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1568) 
                stream_NEWLINE.add(NEWLINE135)


                INDENT136 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1578) 
                stream_INDENT.add(INDENT136)


                NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1580) 
                stream_NEWLINE.add(NEWLINE137)


                self._state.following.append(self.FOLLOW_types_items_in_types1582)
                types_items138 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items138.tree)


                DEDENT139 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1584) 
                stream_DEDENT.add(DEDENT139)


                NEWLINE140 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1586) 
                stream_NEWLINE.add(NEWLINE140)


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
                # 176:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:176:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:178:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item141 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:178:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:178:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:178:15: ( types_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ID) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:178:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items1618)
                        types_item141 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item141.tree)



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
    # grammar/ShyRecognizerFrontend.g:179:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID142 = None
        vars_hint143 = None


        ID142_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:179:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:179:14: ID vars_hint
                pass 
                ID142 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1628) 
                stream_ID.add(ID142)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item1630)
                vars_hint143 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint143.tree)


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
                # 179:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:179:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:181:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE145 = None
        INDENT146 = None
        NEWLINE147 = None
        NEWLINE149 = None
        DEDENT150 = None
        NEWLINE151 = None
        var_hint144 = None

        var_hint148 = None


        NEWLINE145_tree = None
        INDENT146_tree = None
        NEWLINE147_tree = None
        NEWLINE149_tree = None
        DEDENT150_tree = None
        NEWLINE151_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:182:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:182:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:182:9: ( var_hint )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == CURLY_OPEN or LA26_0 == ID) :
                    alt26 = 1
                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:182:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1657)
                    var_hint144 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint144.tree)





                NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1661) 
                stream_NEWLINE.add(NEWLINE145)


                # grammar/ShyRecognizerFrontend.g:183:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == INDENT) :
                    alt28 = 1
                if alt28 == 1:
                    # grammar/ShyRecognizerFrontend.g:183:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT146 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint1673) 
                    stream_INDENT.add(INDENT146)


                    NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1675) 
                    stream_NEWLINE.add(NEWLINE147)


                    # grammar/ShyRecognizerFrontend.g:183:26: ( var_hint NEWLINE )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == CURLY_OPEN or LA27_0 == ID) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:183:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint1679)
                            var_hint148 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint148.tree)


                            NEWLINE149 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1681) 
                            stream_NEWLINE.add(NEWLINE149)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    DEDENT150 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint1687) 
                    stream_DEDENT.add(DEDENT150)


                    NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint1689) 
                    stream_NEWLINE.add(NEWLINE151)





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
                # 184:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:184:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:186:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE156 = None
        INDENT157 = None
        NEWLINE158 = None
        NEWLINE160 = None
        DEDENT161 = None
        var152 = None

        hint153 = None

        var154 = None

        hint155 = None

        var159 = None


        NEWLINE156_tree = None
        INDENT157_tree = None
        NEWLINE158_tree = None
        NEWLINE160_tree = None
        DEDENT161_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:187:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt33 = 3
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:187:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:187:9: ( var )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:187:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1728)
                            var152 = self.var()

                            self._state.following.pop()
                            stream_var.add(var152.tree)



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
                    # 188:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:188:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:188:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt33 == 2:
                    # grammar/ShyRecognizerFrontend.g:189:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1763)
                    hint153 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint153.tree)


                    # grammar/ShyRecognizerFrontend.g:189:14: ( var )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == ID) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:189:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint1765)
                            var154 = self.var()

                            self._state.following.pop()
                            stream_var.add(var154.tree)



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
                    # 190:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:190:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:190:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt33 == 3:
                    # grammar/ShyRecognizerFrontend.g:191:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint1799)
                    hint155 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint155.tree)


                    NEWLINE156 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1801) 
                    stream_NEWLINE.add(NEWLINE156)


                    INDENT157 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint1803) 
                    stream_INDENT.add(INDENT157)


                    NEWLINE158 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1805) 
                    stream_NEWLINE.add(NEWLINE158)


                    # grammar/ShyRecognizerFrontend.g:191:37: ( ( var )+ NEWLINE )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:191:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:191:39: ( var )+
                            cnt31 = 0
                            while True: #loop31
                                alt31 = 2
                                LA31_0 = self.input.LA(1)

                                if (LA31_0 == ID) :
                                    alt31 = 1


                                if alt31 == 1:
                                    # grammar/ShyRecognizerFrontend.g:191:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint1809)
                                    var159 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var159.tree)



                                else:
                                    if cnt31 >= 1:
                                        break #loop31

                                    eee = EarlyExitException(31, self.input)
                                    raise eee

                                cnt31 += 1


                            NEWLINE160 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint1813) 
                            stream_NEWLINE.add(NEWLINE160)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


                    DEDENT161 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint1819) 
                    stream_DEDENT.add(DEDENT161)


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
                    # 192:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:192:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:192:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:194:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID162 = None

        ID162_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:194:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:194:7: ID
                pass 
                ID162 = self.match(self.input, ID, self.FOLLOW_ID_in_var1853) 
                stream_ID.add(ID162)


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
                # 194:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:194:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:196:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN163 = None
        ID164 = None
        CURLY_CLOSE165 = None
        CURLY_OPEN166 = None
        ID167 = None
        CURLY_CLOSE169 = None
        hint_arg168 = None


        CURLY_OPEN163_tree = None
        ID164_tree = None
        CURLY_CLOSE165_tree = None
        CURLY_OPEN166_tree = None
        ID167_tree = None
        CURLY_CLOSE169_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:197:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:197:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN163 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1878) 
                    stream_CURLY_OPEN.add(CURLY_OPEN163)


                    ID164 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1880) 
                    stream_ID.add(ID164)


                    CURLY_CLOSE165 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1882) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE165)


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
                    # 197:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:197:38: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:198:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN166 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint1902) 
                    stream_CURLY_OPEN.add(CURLY_OPEN166)


                    ID167 = self.match(self.input, ID, self.FOLLOW_ID_in_hint1904) 
                    stream_ID.add(ID167)


                    # grammar/ShyRecognizerFrontend.g:198:23: ( hint_arg )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == ID or LA34_0 == UNDERSCORE) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerFrontend.g:198:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint1906)
                            hint_arg168 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg168.tree)



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


                    CURLY_CLOSE169 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint1910) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE169)


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
                    # 198:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:198:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:198:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:200:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set170 = None

        set170_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:200:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set170 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set170))

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
    # grammar/ShyRecognizerFrontend.g:202:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS171 = None
        NUMBER172 = None

        MINUS171_tree = None
        NUMBER172_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:202:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:202:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:202:13: ( MINUS )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == MINUS) :
                    alt36 = 1
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:202:13: MINUS
                    pass 
                    MINUS171 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole1949)
                    MINUS171_tree = self._adaptor.createWithPayload(MINUS171)
                    self._adaptor.addChild(root_0, MINUS171_tree)






                NUMBER172 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole1953)
                NUMBER172_tree = self._adaptor.createWithPayload(NUMBER172)
                self._adaptor.addChild(root_0, NUMBER172_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:203:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS173 = None
        NUMBER174 = None
        DIVIDE175 = None
        NUMBER176 = None

        MINUS173_tree = None
        NUMBER174_tree = None
        DIVIDE175_tree = None
        NUMBER176_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:203:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:203:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:203:13: ( MINUS )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == MINUS) :
                    alt37 = 1
                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:203:13: MINUS
                    pass 
                    MINUS173 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract1961)
                    MINUS173_tree = self._adaptor.createWithPayload(MINUS173)
                    self._adaptor.addChild(root_0, MINUS173_tree)






                NUMBER174 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1965)
                NUMBER174_tree = self._adaptor.createWithPayload(NUMBER174)
                self._adaptor.addChild(root_0, NUMBER174_tree)



                DIVIDE175 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract1967)
                DIVIDE175_tree = self._adaptor.createWithPayload(DIVIDE175)
                self._adaptor.addChild(root_0, DIVIDE175_tree)



                NUMBER176 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract1969)
                NUMBER176_tree = self._adaptor.createWithPayload(NUMBER176)
                self._adaptor.addChild(root_0, NUMBER176_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\1\23\1\7\3\uffff\2\22\1\32\1\16\1\15\1\32\2\uffff\1\22"
        )

    DFA8_max = DFA.unpack(
        u"\1\104\1\32\3\uffff\4\32\1\104\1\32\2\uffff\1\32"
        )

    DFA8_accept = DFA.unpack(
        u"\2\uffff\1\3\1\5\1\4\6\uffff\1\2\1\1\1\uffff"
        )

    DFA8_special = DFA.unpack(
        u"\16\uffff"
        )


    DFA8_transition = [
        DFA.unpack(u"\1\1\1\2\57\uffff\1\3"),
        DFA.unpack(u"\1\4\12\uffff\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u"\1\12\3\uffff\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u"\1\14\5\uffff\2\14\1\13\56\uffff\1\14"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\1\23\3\17\1\32\1\16\1\17\1\uffff\1\32\1\uffff\1\17"
        )

    DFA16_max = DFA.unpack(
        u"\1\23\5\32\1\25\1\uffff\1\32\1\uffff\1\32"
        )

    DFA16_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA16_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA16_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\10\1\7\2\uffff\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1"
        u"\5"),
        DFA.unpack(u"\1\7\5\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5")
    ]

    # class definition for DFA #16

    class DFA16(DFA):
        pass


    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\23\3\22\1\32\1\16\1\15\1\32\2\uffff\1\22"
        )

    DFA17_max = DFA.unpack(
        u"\1\23\5\32\1\25\1\32\2\uffff\1\32"
        )

    DFA17_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA17_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA17_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\7\3\uffff\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5"),
        DFA.unpack(u"\1\11\5\uffff\1\11\1\uffff\1\10"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\1\uffff\1\6\1\5")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA33_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\101\1\31\1\101\2\uffff\1\31"
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
        DFA.unpack(u"\1\4\7\uffff\1\5\55\uffff\1\5"),
        DFA.unpack(u"\1\6\5\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\55\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\5\uffff\1\7")
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 24, 31, 64])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 24, 31, 64])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 24, 31, 64])
    FOLLOW_types_in_start94 = frozenset([1, 9, 24, 31, 64])
    FOLLOW_MODULE_in_module113 = frozenset([19])
    FOLLOW_ID_in_module115 = frozenset([25])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([19])
    FOLLOW_ID_in_stateless148 = frozenset([25])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless154 = frozenset([25])
    FOLLOW_NEWLINE_in_stateless156 = frozenset([29])
    FOLLOW_proc_in_stateless158 = frozenset([13, 29])
    FOLLOW_DEDENT_in_stateless162 = frozenset([25])
    FOLLOW_NEWLINE_in_stateless164 = frozenset([1])
    FOLLOW_PROC_in_proc209 = frozenset([19])
    FOLLOW_ID_in_proc211 = frozenset([25])
    FOLLOW_NEWLINE_in_proc213 = frozenset([1])
    FOLLOW_PROC_in_proc241 = frozenset([19])
    FOLLOW_ID_in_proc243 = frozenset([25])
    FOLLOW_NEWLINE_in_proc245 = frozenset([21])
    FOLLOW_INDENT_in_proc247 = frozenset([25])
    FOLLOW_NEWLINE_in_proc249 = frozenset([6, 13, 27, 66])
    FOLLOW_proc_args_in_proc263 = frozenset([13, 27, 66])
    FOLLOW_proc_vars_in_proc267 = frozenset([13, 27])
    FOLLOW_proc_ops_in_proc271 = frozenset([13])
    FOLLOW_DEDENT_in_proc283 = frozenset([25])
    FOLLOW_NEWLINE_in_proc285 = frozenset([1])
    FOLLOW_ARGS_in_proc_args334 = frozenset([12, 19, 25])
    FOLLOW_vars_hint_in_proc_args336 = frozenset([1])
    FOLLOW_VARS_in_proc_vars365 = frozenset([12, 19, 25])
    FOLLOW_vars_hint_in_proc_vars367 = frozenset([1])
    FOLLOW_OPS_in_proc_ops396 = frozenset([25])
    FOLLOW_NEWLINE_in_proc_ops398 = frozenset([21])
    FOLLOW_INDENT_in_proc_ops400 = frozenset([25])
    FOLLOW_NEWLINE_in_proc_ops402 = frozenset([19, 20, 68])
    FOLLOW_statements_in_proc_ops404 = frozenset([13])
    FOLLOW_DEDENT_in_proc_ops406 = frozenset([25])
    FOLLOW_NEWLINE_in_proc_ops408 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement439 = frozenset([25])
    FOLLOW_NEWLINE_in_statement441 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement467 = frozenset([1])
    FOLLOW_statement_if_in_statement477 = frozenset([1])
    FOLLOW_statement_assign_in_statement487 = frozenset([1])
    FOLLOW_statement_with_in_statement497 = frozenset([1])
    FOLLOW_statement_in_statements516 = frozenset([1, 19, 20, 68])
    FOLLOW_WITH_in_statement_with557 = frozenset([19])
    FOLLOW_ID_in_statement_with559 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_with561 = frozenset([21])
    FOLLOW_INDENT_in_statement_with571 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_with573 = frozenset([19, 20, 68])
    FOLLOW_statements_in_statement_with575 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with577 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_with579 = frozenset([1])
    FOLLOW_ID_in_statement_assign619 = frozenset([7])
    FOLLOW_ARROW_LEFT_in_statement_assign621 = frozenset([18, 19, 23, 26])
    FOLLOW_arbitrary_value_in_statement_assign623 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_assign625 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if665 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if675 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if687 = frozenset([1])
    FOLLOW_IF_in_statement_if_head795 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head797 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif829 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif831 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body863 = frozenset([15, 25])
    FOLLOW_NEWLINE_in_statement_elif_body865 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body869 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_elif_body871 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body885 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_elif_body887 = frozenset([19, 20, 68])
    FOLLOW_statements_in_statement_elif_body889 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body891 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_elif_body893 = frozenset([1])
    FOLLOW_ELSE_in_statement_else933 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_else935 = frozenset([21])
    FOLLOW_INDENT_in_statement_else949 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_else951 = frozenset([19, 20, 68])
    FOLLOW_statements_in_statement_else953 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else955 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_else957 = frozenset([1])
    FOLLOW_condition_call_in_condition995 = frozenset([1])
    FOLLOW_ANY_in_condition1024 = frozenset([19, 25])
    FOLLOW_condition_calls_in_condition1026 = frozenset([1])
    FOLLOW_ALL_in_condition1055 = frozenset([19, 25])
    FOLLOW_condition_calls_in_condition1057 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1095 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1105 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1107 = frozenset([25])
    FOLLOW_NEWLINE_in_condition_calls1109 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1111 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1115 = frozenset([25])
    FOLLOW_NEWLINE_in_condition_calls1117 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1151 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1161 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1180 = frozenset([25])
    FOLLOW_NEWLINE_in_condition_call_line1182 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1208 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1227 = frozenset([1, 18, 19, 23, 26])
    FOLLOW_statement_call_args_in_statement_call_single_line1229 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1273 = frozenset([18, 19, 23, 25, 26])
    FOLLOW_statement_call_args_in_statement_call_multi_line1275 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1279 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1289 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1291 = frozenset([18, 19, 23, 26])
    FOLLOW_statement_call_args_in_statement_call_multi_line1295 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1297 = frozenset([13, 18, 19, 23, 26])
    FOLLOW_DEDENT_in_statement_call_multi_line1303 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1305 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args1341 = frozenset([1, 18, 19, 23, 26])
    FOLLOW_ID_in_arbitrary_value1358 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1368 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1378 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1388 = frozenset([1])
    FOLLOW_CONSTS_in_consts1407 = frozenset([19])
    FOLLOW_ID_in_consts1409 = frozenset([25])
    FOLLOW_NEWLINE_in_consts1411 = frozenset([21])
    FOLLOW_INDENT_in_consts1421 = frozenset([25])
    FOLLOW_NEWLINE_in_consts1423 = frozenset([19])
    FOLLOW_consts_items_in_consts1425 = frozenset([13])
    FOLLOW_DEDENT_in_consts1427 = frozenset([25])
    FOLLOW_NEWLINE_in_consts1429 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1461 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1477 = frozenset([23, 26])
    FOLLOW_num_whole_in_consts_item1479 = frozenset([25])
    FOLLOW_NEWLINE_in_consts_item1481 = frozenset([1])
    FOLLOW_ID_in_consts_item1503 = frozenset([23, 26])
    FOLLOW_num_fract_in_consts_item1505 = frozenset([25])
    FOLLOW_NEWLINE_in_consts_item1507 = frozenset([1])
    FOLLOW_ID_in_consts_item1529 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1531 = frozenset([25])
    FOLLOW_NEWLINE_in_consts_item1533 = frozenset([1])
    FOLLOW_TYPES_in_types1564 = frozenset([19])
    FOLLOW_ID_in_types1566 = frozenset([25])
    FOLLOW_NEWLINE_in_types1568 = frozenset([21])
    FOLLOW_INDENT_in_types1578 = frozenset([25])
    FOLLOW_NEWLINE_in_types1580 = frozenset([19])
    FOLLOW_types_items_in_types1582 = frozenset([13])
    FOLLOW_DEDENT_in_types1584 = frozenset([25])
    FOLLOW_NEWLINE_in_types1586 = frozenset([1])
    FOLLOW_types_item_in_types_items1618 = frozenset([1, 19])
    FOLLOW_ID_in_types_item1628 = frozenset([12, 19, 25])
    FOLLOW_vars_hint_in_types_item1630 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint1657 = frozenset([25])
    FOLLOW_NEWLINE_in_vars_hint1661 = frozenset([1, 21])
    FOLLOW_INDENT_in_vars_hint1673 = frozenset([25])
    FOLLOW_NEWLINE_in_vars_hint1675 = frozenset([12, 19])
    FOLLOW_var_hint_in_vars_hint1679 = frozenset([25])
    FOLLOW_NEWLINE_in_vars_hint1681 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_vars_hint1687 = frozenset([25])
    FOLLOW_NEWLINE_in_vars_hint1689 = frozenset([1])
    FOLLOW_var_in_var_hint1728 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1763 = frozenset([19])
    FOLLOW_var_in_var_hint1765 = frozenset([1, 19])
    FOLLOW_hint_in_var_hint1799 = frozenset([25])
    FOLLOW_NEWLINE_in_var_hint1801 = frozenset([21])
    FOLLOW_INDENT_in_var_hint1803 = frozenset([25])
    FOLLOW_NEWLINE_in_var_hint1805 = frozenset([19])
    FOLLOW_var_in_var_hint1809 = frozenset([19, 25])
    FOLLOW_NEWLINE_in_var_hint1813 = frozenset([13, 19])
    FOLLOW_DEDENT_in_var_hint1819 = frozenset([1])
    FOLLOW_ID_in_var1853 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1878 = frozenset([19])
    FOLLOW_ID_in_hint1880 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint1882 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint1902 = frozenset([19])
    FOLLOW_ID_in_hint1904 = frozenset([19, 65])
    FOLLOW_hint_arg_in_hint1906 = frozenset([11, 19, 65])
    FOLLOW_CURLY_CLOSE_in_hint1910 = frozenset([1])
    FOLLOW_MINUS_in_num_whole1949 = frozenset([26])
    FOLLOW_NUMBER_in_num_whole1953 = frozenset([1])
    FOLLOW_MINUS_in_num_fract1961 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract1965 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract1967 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract1969 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
