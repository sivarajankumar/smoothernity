# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-23 19:01:47

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
PASTE=20
PROC=21
REPLACE=22
STATELESS=23
STRING=24
TREE_ARBITRARY_TOKEN=25
TREE_CONSTS=26
TREE_COPY=27
TREE_COPY_PASTE=28
TREE_EXPRESSION=29
TREE_HINT=30
TREE_HINT_NONE=31
TREE_MODULE=32
TREE_NUM_FRACT=33
TREE_NUM_WHOLE=34
TREE_PASTE=35
TREE_PASTE_REPLACE=36
TREE_PASTE_WITH=37
TREE_PROC=38
TREE_PROC_ARGS=39
TREE_PROC_VARS=40
TREE_STATELESS=41
TREE_TYPES=42
TREE_TYPES_ITEM=43
TREE_VAR=44
TREE_VARS_HINT=45
TREE_VAR_HINT=46
TYPES=47
UNDERSCORE=48
VARS=49
WHITESPACE=50
WITH=51

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", "CURLY_CLOSE", 
    "CURLY_OPEN", "DEDENT", "DIVIDE", "EXPRESSION", "ID", "INDENT", "MINUS", 
    "MODULE", "NEWLINE", "NUMBER", "PASTE", "PROC", "REPLACE", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_TYPES", 
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
    # grammar/ShyRecognizerFrontend.g:30:1: stateless : ( STATELESS ID NEWLINE -> ^( TREE_STATELESS ID ) | STATELESS ID NEWLINE INDENT NEWLINE ( proc )+ DEDENT NEWLINE -> ^( TREE_STATELESS ID ( proc )+ ) );
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS8 = None
        ID9 = None
        NEWLINE10 = None
        STATELESS11 = None
        ID12 = None
        NEWLINE13 = None
        INDENT14 = None
        NEWLINE15 = None
        DEDENT17 = None
        NEWLINE18 = None
        proc16 = None


        STATELESS8_tree = None
        ID9_tree = None
        NEWLINE10_tree = None
        STATELESS11_tree = None
        ID12_tree = None
        NEWLINE13_tree = None
        INDENT14_tree = None
        NEWLINE15_tree = None
        DEDENT17_tree = None
        NEWLINE18_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:31:5: ( STATELESS ID NEWLINE -> ^( TREE_STATELESS ID ) | STATELESS ID NEWLINE INDENT NEWLINE ( proc )+ DEDENT NEWLINE -> ^( TREE_STATELESS ID ( proc )+ ) )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == STATELESS) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 == ID) :
                        LA3_2 = self.input.LA(3)

                        if (LA3_2 == NEWLINE) :
                            LA3_3 = self.input.LA(4)

                            if (LA3_3 == INDENT) :
                                alt3 = 2
                            elif (LA3_3 == EOF or LA3_3 == CONSTS or LA3_3 == MODULE or LA3_3 == STATELESS or LA3_3 == TYPES) :
                                alt3 = 1
                            else:
                                nvae = NoViableAltException("", 3, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 3, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyRecognizerFrontend.g:31:9: STATELESS ID NEWLINE
                    pass 
                    STATELESS8 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless146) 
                    stream_STATELESS.add(STATELESS8)


                    ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless148) 
                    stream_ID.add(ID9)


                    NEWLINE10 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless150) 
                    stream_NEWLINE.add(NEWLINE10)


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
                    # 32:9: -> ^( TREE_STATELESS ID )
                    # grammar/ShyRecognizerFrontend.g:32:12: ^( TREE_STATELESS ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt3 == 2:
                    # grammar/ShyRecognizerFrontend.g:33:9: STATELESS ID NEWLINE INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    STATELESS11 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless178) 
                    stream_STATELESS.add(STATELESS11)


                    ID12 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless180) 
                    stream_ID.add(ID12)


                    NEWLINE13 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless182) 
                    stream_NEWLINE.add(NEWLINE13)


                    INDENT14 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless184) 
                    stream_INDENT.add(INDENT14)


                    NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless186) 
                    stream_NEWLINE.add(NEWLINE15)


                    # grammar/ShyRecognizerFrontend.g:33:45: ( proc )+
                    cnt2 = 0
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == PROC) :
                            alt2 = 1


                        if alt2 == 1:
                            # grammar/ShyRecognizerFrontend.g:33:45: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless188)
                            proc16 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc16.tree)



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    DEDENT17 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless192) 
                    stream_DEDENT.add(DEDENT17)


                    NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless194) 
                    stream_NEWLINE.add(NEWLINE18)


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
                    # 34:9: -> ^( TREE_STATELESS ID ( proc )+ )
                    # grammar/ShyRecognizerFrontend.g:34:12: ^( TREE_STATELESS ID ( proc )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:34:33: ( proc )+
                    if not (stream_proc.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_proc.hasNext():
                        self._adaptor.addChild(root_1, stream_proc.nextTree())


                    stream_proc.reset()

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
    # grammar/ShyRecognizerFrontend.g:37:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC19 = None
        ID20 = None
        NEWLINE21 = None
        PROC22 = None
        ID23 = None
        NEWLINE24 = None
        INDENT25 = None
        NEWLINE26 = None
        DEDENT29 = None
        NEWLINE30 = None
        proc_args27 = None

        proc_vars28 = None


        PROC19_tree = None
        ID20_tree = None
        NEWLINE21_tree = None
        PROC22_tree = None
        ID23_tree = None
        NEWLINE24_tree = None
        INDENT25_tree = None
        NEWLINE26_tree = None
        DEDENT29_tree = None
        NEWLINE30_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_proc_vars = RewriteRuleSubtreeStream(self._adaptor, "rule proc_vars")
        stream_proc_args = RewriteRuleSubtreeStream(self._adaptor, "rule proc_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:38:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? ) )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == PROC) :
                    LA6_1 = self.input.LA(2)

                    if (LA6_1 == ID) :
                        LA6_2 = self.input.LA(3)

                        if (LA6_2 == NEWLINE) :
                            LA6_3 = self.input.LA(4)

                            if (LA6_3 == INDENT) :
                                alt6 = 2
                            elif (LA6_3 == DEDENT or LA6_3 == PROC) :
                                alt6 = 1
                            else:
                                nvae = NoViableAltException("", 6, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 6, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 6, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # grammar/ShyRecognizerFrontend.g:38:9: PROC ID NEWLINE
                    pass 
                    PROC19 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc235) 
                    stream_PROC.add(PROC19)


                    ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_proc237) 
                    stream_ID.add(ID20)


                    NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc239) 
                    stream_NEWLINE.add(NEWLINE21)


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
                    # 39:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:39:12: ^( TREE_PROC ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt6 == 2:
                    # grammar/ShyRecognizerFrontend.g:40:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_vars )? DEDENT NEWLINE
                    pass 
                    PROC22 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc267) 
                    stream_PROC.add(PROC22)


                    ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_proc269) 
                    stream_ID.add(ID23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc271) 
                    stream_NEWLINE.add(NEWLINE24)


                    INDENT25 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc273) 
                    stream_INDENT.add(INDENT25)


                    NEWLINE26 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc275) 
                    stream_NEWLINE.add(NEWLINE26)


                    # grammar/ShyRecognizerFrontend.g:41:13: ( proc_args )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ARGS) :
                        alt4 = 1
                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:41:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc289)
                        proc_args27 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args27.tree)





                    # grammar/ShyRecognizerFrontend.g:41:25: ( proc_vars )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == VARS) :
                        alt5 = 1
                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:41:25: proc_vars
                        pass 
                        self._state.following.append(self.FOLLOW_proc_vars_in_proc293)
                        proc_vars28 = self.proc_vars()

                        self._state.following.pop()
                        stream_proc_vars.add(proc_vars28.tree)





                    DEDENT29 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc305) 
                    stream_DEDENT.add(DEDENT29)


                    NEWLINE30 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc307) 
                    stream_NEWLINE.add(NEWLINE30)


                    # AST Rewrite
                    # elements: proc_vars, ID, proc_args
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 43:9: -> ^( TREE_PROC ID ( proc_args )? ( proc_vars )? )
                    # grammar/ShyRecognizerFrontend.g:43:12: ^( TREE_PROC ID ( proc_args )? ( proc_vars )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:43:28: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:43:40: ( proc_vars )?
                    if stream_proc_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_vars.nextTree())


                    stream_proc_vars.reset();

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
    # grammar/ShyRecognizerFrontend.g:46:1: proc_args : ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS31 = None
        vars_hint32 = None


        ARGS31_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:47:5: ( ARGS vars_hint -> ^( TREE_PROC_ARGS vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:47:9: ARGS vars_hint
                pass 
                ARGS31 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args352) 
                stream_ARGS.add(ARGS31)


                self._state.following.append(self.FOLLOW_vars_hint_in_proc_args354)
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
                # 47:24: -> ^( TREE_PROC_ARGS vars_hint )
                # grammar/ShyRecognizerFrontend.g:47:27: ^( TREE_PROC_ARGS vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:50:1: proc_vars : VARS vars_hint -> ^( TREE_PROC_VARS vars_hint ) ;
    def proc_vars(self, ):
        retval = self.proc_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS33 = None
        vars_hint34 = None


        VARS33_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:51:5: ( VARS vars_hint -> ^( TREE_PROC_VARS vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:51:9: VARS vars_hint
                pass 
                VARS33 = self.match(self.input, VARS, self.FOLLOW_VARS_in_proc_vars383) 
                stream_VARS.add(VARS33)


                self._state.following.append(self.FOLLOW_vars_hint_in_proc_vars385)
                vars_hint34 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint34.tree)


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
                # 51:24: -> ^( TREE_PROC_VARS vars_hint )
                # grammar/ShyRecognizerFrontend.g:51:27: ^( TREE_PROC_VARS vars_hint )
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


    class consts_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts"
    # grammar/ShyRecognizerFrontend.g:54:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS35 = None
        ID36 = None
        NEWLINE37 = None
        INDENT38 = None
        NEWLINE39 = None
        DEDENT41 = None
        NEWLINE42 = None
        consts_items40 = None


        CONSTS35_tree = None
        ID36_tree = None
        NEWLINE37_tree = None
        INDENT38_tree = None
        NEWLINE39_tree = None
        DEDENT41_tree = None
        NEWLINE42_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:55:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:55:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS35 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts414) 
                stream_CONSTS.add(CONSTS35)


                ID36 = self.match(self.input, ID, self.FOLLOW_ID_in_consts416) 
                stream_ID.add(ID36)


                NEWLINE37 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts418) 
                stream_NEWLINE.add(NEWLINE37)


                INDENT38 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts428) 
                stream_INDENT.add(INDENT38)


                NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts430) 
                stream_NEWLINE.add(NEWLINE39)


                self._state.following.append(self.FOLLOW_consts_items_in_consts432)
                consts_items40 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items40.tree)


                DEDENT41 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts434) 
                stream_DEDENT.add(DEDENT41)


                NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts436) 
                stream_NEWLINE.add(NEWLINE42)


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
                # 57:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:57:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:59:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item43 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:59:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:59:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:59:16: ( consts_item )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == ID) :
                        alt7 = 1


                    if alt7 == 1:
                        # grammar/ShyRecognizerFrontend.g:59:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items468)
                        consts_item43 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item43.tree)



                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:60:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID44 = None
        NEWLINE46 = None
        ID47 = None
        NEWLINE49 = None
        ID50 = None
        EXPRESSION51 = None
        NEWLINE52 = None
        num_whole45 = None

        num_fract48 = None


        ID44_tree = None
        NEWLINE46_tree = None
        ID47_tree = None
        NEWLINE49_tree = None
        ID50_tree = None
        EXPRESSION51_tree = None
        NEWLINE52_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:61:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt8 = 3
                LA8_0 = self.input.LA(1)

                if (LA8_0 == ID) :
                    LA8 = self.input.LA(2)
                    if LA8 == EXPRESSION:
                        alt8 = 3
                    elif LA8 == MINUS:
                        LA8_3 = self.input.LA(3)

                        if (LA8_3 == NUMBER) :
                            LA8_4 = self.input.LA(4)

                            if (LA8_4 == DIVIDE) :
                                alt8 = 2
                            elif (LA8_4 == NEWLINE) :
                                alt8 = 1
                            else:
                                nvae = NoViableAltException("", 8, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 8, 3, self.input)

                            raise nvae


                    elif LA8 == NUMBER:
                        LA8_4 = self.input.LA(3)

                        if (LA8_4 == DIVIDE) :
                            alt8 = 2
                        elif (LA8_4 == NEWLINE) :
                            alt8 = 1
                        else:
                            nvae = NoViableAltException("", 8, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 8, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # grammar/ShyRecognizerFrontend.g:61:9: ID num_whole NEWLINE
                    pass 
                    ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item484) 
                    stream_ID.add(ID44)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item486)
                    num_whole45 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole45.tree)


                    NEWLINE46 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item488) 
                    stream_NEWLINE.add(NEWLINE46)


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
                    # 61:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:61:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt8 == 2:
                    # grammar/ShyRecognizerFrontend.g:62:9: ID num_fract NEWLINE
                    pass 
                    ID47 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item510) 
                    stream_ID.add(ID47)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item512)
                    num_fract48 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract48.tree)


                    NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item514) 
                    stream_NEWLINE.add(NEWLINE49)


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
                    # 62:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:62:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt8 == 3:
                    # grammar/ShyRecognizerFrontend.g:63:9: ID EXPRESSION NEWLINE
                    pass 
                    ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item536) 
                    stream_ID.add(ID50)


                    EXPRESSION51 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item538) 
                    stream_EXPRESSION.add(EXPRESSION51)


                    NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item540) 
                    stream_NEWLINE.add(NEWLINE52)


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
                    # 63:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:63:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:66:1: types : TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES53 = None
        ID54 = None
        NEWLINE55 = None
        INDENT56 = None
        NEWLINE57 = None
        DEDENT59 = None
        NEWLINE60 = None
        types_items58 = None


        TYPES53_tree = None
        ID54_tree = None
        NEWLINE55_tree = None
        INDENT56_tree = None
        NEWLINE57_tree = None
        DEDENT59_tree = None
        NEWLINE60_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_items = RewriteRuleSubtreeStream(self._adaptor, "rule types_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:67:5: ( TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE -> ^( TREE_TYPES ID types_items ) )
                # grammar/ShyRecognizerFrontend.g:67:9: TYPES ID NEWLINE INDENT NEWLINE types_items DEDENT NEWLINE
                pass 
                TYPES53 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types571) 
                stream_TYPES.add(TYPES53)


                ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_types573) 
                stream_ID.add(ID54)


                NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types575) 
                stream_NEWLINE.add(NEWLINE55)


                INDENT56 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types585) 
                stream_INDENT.add(INDENT56)


                NEWLINE57 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types587) 
                stream_NEWLINE.add(NEWLINE57)


                self._state.following.append(self.FOLLOW_types_items_in_types589)
                types_items58 = self.types_items()

                self._state.following.pop()
                stream_types_items.add(types_items58.tree)


                DEDENT59 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types591) 
                stream_DEDENT.add(DEDENT59)


                NEWLINE60 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types593) 
                stream_NEWLINE.add(NEWLINE60)


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
                # 69:9: -> ^( TREE_TYPES ID types_items )
                # grammar/ShyRecognizerFrontend.g:69:12: ^( TREE_TYPES ID types_items )
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
    # grammar/ShyRecognizerFrontend.g:71:1: types_items : ( types_item )+ ;
    def types_items(self, ):
        retval = self.types_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        types_item61 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:71:13: ( ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:71:15: ( types_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:71:15: ( types_item )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == ID) :
                        alt9 = 1


                    if alt9 == 1:
                        # grammar/ShyRecognizerFrontend.g:71:15: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types_items625)
                        types_item61 = self.types_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, types_item61.tree)



                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:72:1: types_item : ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID62 = None
        vars_hint63 = None


        ID62_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_vars_hint = RewriteRuleSubtreeStream(self._adaptor, "rule vars_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:72:12: ( ID vars_hint -> ^( TREE_TYPES_ITEM ID vars_hint ) )
                # grammar/ShyRecognizerFrontend.g:72:14: ID vars_hint
                pass 
                ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item635) 
                stream_ID.add(ID62)


                self._state.following.append(self.FOLLOW_vars_hint_in_types_item637)
                vars_hint63 = self.vars_hint()

                self._state.following.pop()
                stream_vars_hint.add(vars_hint63.tree)


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
                # 72:27: -> ^( TREE_TYPES_ITEM ID vars_hint )
                # grammar/ShyRecognizerFrontend.g:72:30: ^( TREE_TYPES_ITEM ID vars_hint )
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
    # grammar/ShyRecognizerFrontend.g:74:1: vars_hint : ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* ;
    def vars_hint(self, ):
        retval = self.vars_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE65 = None
        INDENT66 = None
        NEWLINE67 = None
        NEWLINE69 = None
        DEDENT70 = None
        NEWLINE71 = None
        var_hint64 = None

        var_hint68 = None


        NEWLINE65_tree = None
        INDENT66_tree = None
        NEWLINE67_tree = None
        NEWLINE69_tree = None
        DEDENT70_tree = None
        NEWLINE71_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var_hint = RewriteRuleSubtreeStream(self._adaptor, "rule var_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:75:5: ( ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )? -> TREE_VARS_HINT ( var_hint )* )
                # grammar/ShyRecognizerFrontend.g:75:9: ( var_hint )? NEWLINE ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                pass 
                # grammar/ShyRecognizerFrontend.g:75:9: ( var_hint )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == CURLY_OPEN or LA10_0 == ID) :
                    alt10 = 1
                if alt10 == 1:
                    # grammar/ShyRecognizerFrontend.g:75:9: var_hint
                    pass 
                    self._state.following.append(self.FOLLOW_var_hint_in_vars_hint664)
                    var_hint64 = self.var_hint()

                    self._state.following.pop()
                    stream_var_hint.add(var_hint64.tree)





                NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint668) 
                stream_NEWLINE.add(NEWLINE65)


                # grammar/ShyRecognizerFrontend.g:76:9: ( INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == INDENT) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:76:11: INDENT NEWLINE ( var_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT66 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_vars_hint680) 
                    stream_INDENT.add(INDENT66)


                    NEWLINE67 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint682) 
                    stream_NEWLINE.add(NEWLINE67)


                    # grammar/ShyRecognizerFrontend.g:76:26: ( var_hint NEWLINE )+
                    cnt11 = 0
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == CURLY_OPEN or LA11_0 == ID) :
                            alt11 = 1


                        if alt11 == 1:
                            # grammar/ShyRecognizerFrontend.g:76:28: var_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_var_hint_in_vars_hint686)
                            var_hint68 = self.var_hint()

                            self._state.following.pop()
                            stream_var_hint.add(var_hint68.tree)


                            NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint688) 
                            stream_NEWLINE.add(NEWLINE69)



                        else:
                            if cnt11 >= 1:
                                break #loop11

                            eee = EarlyExitException(11, self.input)
                            raise eee

                        cnt11 += 1


                    DEDENT70 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_vars_hint694) 
                    stream_DEDENT.add(DEDENT70)


                    NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_vars_hint696) 
                    stream_NEWLINE.add(NEWLINE71)





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
                # 77:9: -> TREE_VARS_HINT ( var_hint )*
                self._adaptor.addChild(root_0, 
                self._adaptor.createFromType(TREE_VARS_HINT, "TREE_VARS_HINT")
                )

                # grammar/ShyRecognizerFrontend.g:77:27: ( var_hint )*
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
    # grammar/ShyRecognizerFrontend.g:79:1: var_hint : ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) );
    def var_hint(self, ):
        retval = self.var_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE76 = None
        INDENT77 = None
        NEWLINE78 = None
        NEWLINE80 = None
        DEDENT81 = None
        var72 = None

        hint73 = None

        var74 = None

        hint75 = None

        var79 = None


        NEWLINE76_tree = None
        INDENT77_tree = None
        NEWLINE78_tree = None
        NEWLINE80_tree = None
        DEDENT81_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_var = RewriteRuleSubtreeStream(self._adaptor, "rule var")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:80:5: ( ( var )+ -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ ) | hint ( var )+ -> ^( TREE_VAR_HINT hint ( var )+ ) | hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT -> ^( TREE_VAR_HINT hint ( var )+ ) )
                alt17 = 3
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:80:9: ( var )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:80:9: ( var )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == ID) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyRecognizerFrontend.g:80:9: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint735)
                            var72 = self.var()

                            self._state.following.pop()
                            stream_var.add(var72.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


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
                    # 81:9: -> ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:81:12: ^( TREE_VAR_HINT TREE_HINT_NONE ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:81:44: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:82:9: hint ( var )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint770)
                    hint73 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint73.tree)


                    # grammar/ShyRecognizerFrontend.g:82:14: ( var )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == ID) :
                            alt14 = 1


                        if alt14 == 1:
                            # grammar/ShyRecognizerFrontend.g:82:14: var
                            pass 
                            self._state.following.append(self.FOLLOW_var_in_var_hint772)
                            var74 = self.var()

                            self._state.following.pop()
                            stream_var.add(var74.tree)



                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


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
                    # 83:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:83:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:83:34: ( var )+
                    if not (stream_var.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_var.hasNext():
                        self._adaptor.addChild(root_1, stream_var.nextTree())


                    stream_var.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 3:
                    # grammar/ShyRecognizerFrontend.g:84:9: hint NEWLINE INDENT NEWLINE ( ( var )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_var_hint806)
                    hint75 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint75.tree)


                    NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint808) 
                    stream_NEWLINE.add(NEWLINE76)


                    INDENT77 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_var_hint810) 
                    stream_INDENT.add(INDENT77)


                    NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint812) 
                    stream_NEWLINE.add(NEWLINE78)


                    # grammar/ShyRecognizerFrontend.g:84:37: ( ( var )+ NEWLINE )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == ID) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:84:39: ( var )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:84:39: ( var )+
                            cnt15 = 0
                            while True: #loop15
                                alt15 = 2
                                LA15_0 = self.input.LA(1)

                                if (LA15_0 == ID) :
                                    alt15 = 1


                                if alt15 == 1:
                                    # grammar/ShyRecognizerFrontend.g:84:39: var
                                    pass 
                                    self._state.following.append(self.FOLLOW_var_in_var_hint816)
                                    var79 = self.var()

                                    self._state.following.pop()
                                    stream_var.add(var79.tree)



                                else:
                                    if cnt15 >= 1:
                                        break #loop15

                                    eee = EarlyExitException(15, self.input)
                                    raise eee

                                cnt15 += 1


                            NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_var_hint820) 
                            stream_NEWLINE.add(NEWLINE80)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    DEDENT81 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_var_hint826) 
                    stream_DEDENT.add(DEDENT81)


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
                    # 85:9: -> ^( TREE_VAR_HINT hint ( var )+ )
                    # grammar/ShyRecognizerFrontend.g:85:12: ^( TREE_VAR_HINT hint ( var )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_VAR_HINT, "TREE_VAR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:85:34: ( var )+
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
    # grammar/ShyRecognizerFrontend.g:87:1: var : ID -> ^( TREE_VAR ID ) ;
    def var(self, ):
        retval = self.var_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID82 = None

        ID82_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:87:5: ( ID -> ^( TREE_VAR ID ) )
                # grammar/ShyRecognizerFrontend.g:87:7: ID
                pass 
                ID82 = self.match(self.input, ID, self.FOLLOW_ID_in_var860) 
                stream_ID.add(ID82)


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
                # 87:10: -> ^( TREE_VAR ID )
                # grammar/ShyRecognizerFrontend.g:87:13: ^( TREE_VAR ID )
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
    # grammar/ShyRecognizerFrontend.g:89:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN83 = None
        ID84 = None
        CURLY_CLOSE85 = None
        CURLY_OPEN86 = None
        ID87 = None
        CURLY_CLOSE89 = None
        hint_arg88 = None


        CURLY_OPEN83_tree = None
        ID84_tree = None
        CURLY_CLOSE85_tree = None
        CURLY_OPEN86_tree = None
        ID87_tree = None
        CURLY_CLOSE89_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:90:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == CURLY_OPEN) :
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == ID) :
                        LA19_2 = self.input.LA(3)

                        if (LA19_2 == CURLY_CLOSE) :
                            alt19 = 1
                        elif (LA19_2 == ID or LA19_2 == UNDERSCORE) :
                            alt19 = 2
                        else:
                            nvae = NoViableAltException("", 19, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 19, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:90:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN83 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint885) 
                    stream_CURLY_OPEN.add(CURLY_OPEN83)


                    ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_hint887) 
                    stream_ID.add(ID84)


                    CURLY_CLOSE85 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint889) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE85)


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
                    # 90:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:90:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt19 == 2:
                    # grammar/ShyRecognizerFrontend.g:91:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN86 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint909) 
                    stream_CURLY_OPEN.add(CURLY_OPEN86)


                    ID87 = self.match(self.input, ID, self.FOLLOW_ID_in_hint911) 
                    stream_ID.add(ID87)


                    # grammar/ShyRecognizerFrontend.g:91:23: ( hint_arg )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == ID or LA18_0 == UNDERSCORE) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerFrontend.g:91:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint913)
                            hint_arg88 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg88.tree)



                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


                    CURLY_CLOSE89 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint917) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE89)


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
                    # 91:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:91:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:91:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:93:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set90 = None

        set90_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:93:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set90 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set90))

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
    # grammar/ShyRecognizerFrontend.g:95:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS91 = None
        NUMBER92 = None

        MINUS91_tree = None
        NUMBER92_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:95:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:95:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:95:13: ( MINUS )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == MINUS) :
                    alt20 = 1
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:95:13: MINUS
                    pass 
                    MINUS91 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole956)
                    MINUS91_tree = self._adaptor.createWithPayload(MINUS91)
                    self._adaptor.addChild(root_0, MINUS91_tree)






                NUMBER92 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole960)
                NUMBER92_tree = self._adaptor.createWithPayload(NUMBER92)
                self._adaptor.addChild(root_0, NUMBER92_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:96:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS93 = None
        NUMBER94 = None
        DIVIDE95 = None
        NUMBER96 = None

        MINUS93_tree = None
        NUMBER94_tree = None
        DIVIDE95_tree = None
        NUMBER96_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:96:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:96:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:96:13: ( MINUS )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == MINUS) :
                    alt21 = 1
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:96:13: MINUS
                    pass 
                    MINUS93 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract968)
                    MINUS93_tree = self._adaptor.createWithPayload(MINUS93)
                    self._adaptor.addChild(root_0, MINUS93_tree)






                NUMBER94 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract972)
                NUMBER94_tree = self._adaptor.createWithPayload(NUMBER94)
                self._adaptor.addChild(root_0, NUMBER94_tree)



                DIVIDE95 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract974)
                DIVIDE95_tree = self._adaptor.createWithPayload(DIVIDE95)
                self._adaptor.addChild(root_0, DIVIDE95_tree)



                NUMBER96 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract976)
                NUMBER96_tree = self._adaptor.createWithPayload(NUMBER96)
                self._adaptor.addChild(root_0, NUMBER96_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\12\1\uffff\1\16\1\11\1\16\1\11\2\uffff\1\16"
        )

    DFA17_max = DFA.unpack(
        u"\1\16\1\uffff\1\16\1\60\1\22\1\60\2\uffff\1\22"
        )

    DFA17_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA17_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA17_transition = [
        DFA.unpack(u"\1\2\3\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\4\uffff\1\5\41\uffff\1\5"),
        DFA.unpack(u"\1\6\3\uffff\1\7"),
        DFA.unpack(u"\1\10\4\uffff\1\5\41\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\7")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 7, 17, 23, 47])
    FOLLOW_stateless_in_start86 = frozenset([1, 7, 17, 23, 47])
    FOLLOW_consts_in_start90 = frozenset([1, 7, 17, 23, 47])
    FOLLOW_types_in_start94 = frozenset([1, 7, 17, 23, 47])
    FOLLOW_MODULE_in_module113 = frozenset([14])
    FOLLOW_ID_in_module115 = frozenset([18])
    FOLLOW_NEWLINE_in_module117 = frozenset([1])
    FOLLOW_STATELESS_in_stateless146 = frozenset([14])
    FOLLOW_ID_in_stateless148 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless150 = frozenset([1])
    FOLLOW_STATELESS_in_stateless178 = frozenset([14])
    FOLLOW_ID_in_stateless180 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless182 = frozenset([15])
    FOLLOW_INDENT_in_stateless184 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless186 = frozenset([21])
    FOLLOW_proc_in_stateless188 = frozenset([11, 21])
    FOLLOW_DEDENT_in_stateless192 = frozenset([18])
    FOLLOW_NEWLINE_in_stateless194 = frozenset([1])
    FOLLOW_PROC_in_proc235 = frozenset([14])
    FOLLOW_ID_in_proc237 = frozenset([18])
    FOLLOW_NEWLINE_in_proc239 = frozenset([1])
    FOLLOW_PROC_in_proc267 = frozenset([14])
    FOLLOW_ID_in_proc269 = frozenset([18])
    FOLLOW_NEWLINE_in_proc271 = frozenset([15])
    FOLLOW_INDENT_in_proc273 = frozenset([18])
    FOLLOW_NEWLINE_in_proc275 = frozenset([4, 11, 49])
    FOLLOW_proc_args_in_proc289 = frozenset([11, 49])
    FOLLOW_proc_vars_in_proc293 = frozenset([11])
    FOLLOW_DEDENT_in_proc305 = frozenset([18])
    FOLLOW_NEWLINE_in_proc307 = frozenset([1])
    FOLLOW_ARGS_in_proc_args352 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_proc_args354 = frozenset([1])
    FOLLOW_VARS_in_proc_vars383 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_proc_vars385 = frozenset([1])
    FOLLOW_CONSTS_in_consts414 = frozenset([14])
    FOLLOW_ID_in_consts416 = frozenset([18])
    FOLLOW_NEWLINE_in_consts418 = frozenset([15])
    FOLLOW_INDENT_in_consts428 = frozenset([18])
    FOLLOW_NEWLINE_in_consts430 = frozenset([14])
    FOLLOW_consts_items_in_consts432 = frozenset([11])
    FOLLOW_DEDENT_in_consts434 = frozenset([18])
    FOLLOW_NEWLINE_in_consts436 = frozenset([1])
    FOLLOW_consts_item_in_consts_items468 = frozenset([1, 14])
    FOLLOW_ID_in_consts_item484 = frozenset([16, 19])
    FOLLOW_num_whole_in_consts_item486 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item488 = frozenset([1])
    FOLLOW_ID_in_consts_item510 = frozenset([16, 19])
    FOLLOW_num_fract_in_consts_item512 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item514 = frozenset([1])
    FOLLOW_ID_in_consts_item536 = frozenset([13])
    FOLLOW_EXPRESSION_in_consts_item538 = frozenset([18])
    FOLLOW_NEWLINE_in_consts_item540 = frozenset([1])
    FOLLOW_TYPES_in_types571 = frozenset([14])
    FOLLOW_ID_in_types573 = frozenset([18])
    FOLLOW_NEWLINE_in_types575 = frozenset([15])
    FOLLOW_INDENT_in_types585 = frozenset([18])
    FOLLOW_NEWLINE_in_types587 = frozenset([14])
    FOLLOW_types_items_in_types589 = frozenset([11])
    FOLLOW_DEDENT_in_types591 = frozenset([18])
    FOLLOW_NEWLINE_in_types593 = frozenset([1])
    FOLLOW_types_item_in_types_items625 = frozenset([1, 14])
    FOLLOW_ID_in_types_item635 = frozenset([10, 14, 18])
    FOLLOW_vars_hint_in_types_item637 = frozenset([1])
    FOLLOW_var_hint_in_vars_hint664 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint668 = frozenset([1, 15])
    FOLLOW_INDENT_in_vars_hint680 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint682 = frozenset([10, 14])
    FOLLOW_var_hint_in_vars_hint686 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint688 = frozenset([10, 11, 14])
    FOLLOW_DEDENT_in_vars_hint694 = frozenset([18])
    FOLLOW_NEWLINE_in_vars_hint696 = frozenset([1])
    FOLLOW_var_in_var_hint735 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint770 = frozenset([14])
    FOLLOW_var_in_var_hint772 = frozenset([1, 14])
    FOLLOW_hint_in_var_hint806 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint808 = frozenset([15])
    FOLLOW_INDENT_in_var_hint810 = frozenset([18])
    FOLLOW_NEWLINE_in_var_hint812 = frozenset([14])
    FOLLOW_var_in_var_hint816 = frozenset([14, 18])
    FOLLOW_NEWLINE_in_var_hint820 = frozenset([11, 14])
    FOLLOW_DEDENT_in_var_hint826 = frozenset([1])
    FOLLOW_ID_in_var860 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint885 = frozenset([14])
    FOLLOW_ID_in_hint887 = frozenset([9])
    FOLLOW_CURLY_CLOSE_in_hint889 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint909 = frozenset([14])
    FOLLOW_ID_in_hint911 = frozenset([14, 48])
    FOLLOW_hint_arg_in_hint913 = frozenset([9, 14, 48])
    FOLLOW_CURLY_CLOSE_in_hint917 = frozenset([1])
    FOLLOW_MINUS_in_num_whole956 = frozenset([19])
    FOLLOW_NUMBER_in_num_whole960 = frozenset([1])
    FOLLOW_MINUS_in_num_fract968 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract972 = frozenset([12])
    FOLLOW_DIVIDE_in_num_fract974 = frozenset([19])
    FOLLOW_NUMBER_in_num_fract976 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
