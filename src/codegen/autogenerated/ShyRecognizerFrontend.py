# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-31 18:58:03

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
REPLY=31
REQUEST=32
STATELESS=33
STRING=34
TREE_ARBITRARY_TOKEN=35
TREE_ATTR=36
TREE_ATTRS_HINTS=37
TREE_ATTR_HINT=38
TREE_CONDITION_ALL=39
TREE_CONDITION_ANY=40
TREE_CONSTS=41
TREE_COPY=42
TREE_COPY_PASTE=43
TREE_EXPRESSION=44
TREE_HINT=45
TREE_HINT_NONE=46
TREE_MESSAGES=47
TREE_MESSAGES_ITEM=48
TREE_MODULE=49
TREE_NUM_FRACT=50
TREE_NUM_WHOLE=51
TREE_PASTE=52
TREE_PASTE_REPLACE=53
TREE_PASTE_WITH=54
TREE_PROC=55
TREE_PROC_ARGS=56
TREE_PROC_VARS=57
TREE_STATELESS=58
TREE_STATEMENTS=59
TREE_STATEMENT_ASSIGN=60
TREE_STATEMENT_CALL=61
TREE_STATEMENT_ELIF=62
TREE_STATEMENT_ELSE=63
TREE_STATEMENT_IF=64
TREE_STATEMENT_WITH=65
TREE_TYPES=66
TREE_TYPES_ITEM=67
TYPES=68
UNDERSCORE=69
VARS=70
WHITESPACE=71
WITH=72

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "NEWLINE", 
    "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "REPLY", "REQUEST", "STATELESS", 
    "STRING", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", 
    "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", 
    "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", 
    "TREE_MESSAGES", "TREE_MESSAGES_ITEM", "TREE_MODULE", "TREE_NUM_FRACT", 
    "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", 
    "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", 
    "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WITH", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TYPES", "UNDERSCORE", "VARS", "WHITESPACE", "WITH"
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

        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
            )

        self.dfa34 = self.DFA34(
            self, 34,
            eot = self.DFA34_eot,
            eof = self.DFA34_eof,
            min = self.DFA34_min,
            max = self.DFA34_max,
            accept = self.DFA34_accept,
            special = self.DFA34_special,
            transition = self.DFA34_transition
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
    # grammar/ShyRecognizerFrontend.g:24:1: start : ( module | stateless | consts | types | messages )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        module1 = None

        stateless2 = None

        consts3 = None

        types4 = None

        messages5 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:24:7: ( ( module | stateless | consts | types | messages )* )
                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types | messages )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types | messages )*
                while True: #loop1
                    alt1 = 6
                    LA1 = self.input.LA(1)
                    if LA1 == MODULE:
                        alt1 = 1
                    elif LA1 == STATELESS:
                        alt1 = 2
                    elif LA1 == CONSTS:
                        alt1 = 3
                    elif LA1 == TYPES:
                        alt1 = 4
                    elif LA1 == MESSAGES:
                        alt1 = 5

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



                    elif alt1 == 5:
                        # grammar/ShyRecognizerFrontend.g:24:49: messages
                        pass 
                        self._state.following.append(self.FOLLOW_messages_in_start98)
                        messages5 = self.messages()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, messages5.tree)



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

        MODULE6 = None
        ID7 = None
        NEWLINE8 = None

        MODULE6_tree = None
        ID7_tree = None
        NEWLINE8_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:27:5: ( MODULE ID NEWLINE -> ^( TREE_MODULE ID ) )
                # grammar/ShyRecognizerFrontend.g:27:9: MODULE ID NEWLINE
                pass 
                MODULE6 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module117) 
                stream_MODULE.add(MODULE6)


                ID7 = self.match(self.input, ID, self.FOLLOW_ID_in_module119) 
                stream_ID.add(ID7)


                NEWLINE8 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module121) 
                stream_NEWLINE.add(NEWLINE8)


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

        STATELESS9 = None
        ID10 = None
        NEWLINE11 = None
        INDENT12 = None
        NEWLINE13 = None
        DEDENT15 = None
        NEWLINE16 = None
        proc14 = None


        STATELESS9_tree = None
        ID10_tree = None
        NEWLINE11_tree = None
        INDENT12_tree = None
        NEWLINE13_tree = None
        DEDENT15_tree = None
        NEWLINE16_tree = None
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
                STATELESS9 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless150) 
                stream_STATELESS.add(STATELESS9)


                ID10 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless152) 
                stream_ID.add(ID10)


                NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless154) 
                stream_NEWLINE.add(NEWLINE11)


                # grammar/ShyRecognizerFrontend.g:31:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == INDENT) :
                    alt3 = 1
                if alt3 == 1:
                    # grammar/ShyRecognizerFrontend.g:31:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT12 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless158) 
                    stream_INDENT.add(INDENT12)


                    NEWLINE13 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless160) 
                    stream_NEWLINE.add(NEWLINE13)


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
                            self._state.following.append(self.FOLLOW_proc_in_stateless162)
                            proc14 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc14.tree)



                        else:
                            if cnt2 >= 1:
                                break #loop2

                            eee = EarlyExitException(2, self.input)
                            raise eee

                        cnt2 += 1


                    DEDENT15 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless166) 
                    stream_DEDENT.add(DEDENT15)


                    NEWLINE16 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless168) 
                    stream_NEWLINE.add(NEWLINE16)





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
    # grammar/ShyRecognizerFrontend.g:35:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC17 = None
        ID18 = None
        NEWLINE19 = None
        PROC20 = None
        ID21 = None
        NEWLINE22 = None
        INDENT23 = None
        NEWLINE24 = None
        DEDENT28 = None
        NEWLINE29 = None
        proc_args25 = None

        proc_attrs26 = None

        proc_ops27 = None


        PROC17_tree = None
        ID18_tree = None
        NEWLINE19_tree = None
        PROC20_tree = None
        ID21_tree = None
        NEWLINE22_tree = None
        INDENT23_tree = None
        NEWLINE24_tree = None
        DEDENT28_tree = None
        NEWLINE29_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_proc_ops = RewriteRuleSubtreeStream(self._adaptor, "rule proc_ops")
        stream_proc_args = RewriteRuleSubtreeStream(self._adaptor, "rule proc_args")
        stream_proc_attrs = RewriteRuleSubtreeStream(self._adaptor, "rule proc_attrs")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:36:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? ) )
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
                    PROC17 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc213) 
                    stream_PROC.add(PROC17)


                    ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_proc215) 
                    stream_ID.add(ID18)


                    NEWLINE19 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc217) 
                    stream_NEWLINE.add(NEWLINE19)


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
                    # grammar/ShyRecognizerFrontend.g:38:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE
                    pass 
                    PROC20 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc245) 
                    stream_PROC.add(PROC20)


                    ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_proc247) 
                    stream_ID.add(ID21)


                    NEWLINE22 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc249) 
                    stream_NEWLINE.add(NEWLINE22)


                    INDENT23 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc251) 
                    stream_INDENT.add(INDENT23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc253) 
                    stream_NEWLINE.add(NEWLINE24)


                    # grammar/ShyRecognizerFrontend.g:39:13: ( proc_args )?
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == ARGS) :
                        alt4 = 1
                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:39:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc267)
                        proc_args25 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args25.tree)





                    # grammar/ShyRecognizerFrontend.g:39:25: ( proc_attrs )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == VARS) :
                        alt5 = 1
                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:39:25: proc_attrs
                        pass 
                        self._state.following.append(self.FOLLOW_proc_attrs_in_proc271)
                        proc_attrs26 = self.proc_attrs()

                        self._state.following.pop()
                        stream_proc_attrs.add(proc_attrs26.tree)





                    # grammar/ShyRecognizerFrontend.g:39:38: ( proc_ops )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == OPS) :
                        alt6 = 1
                    if alt6 == 1:
                        # grammar/ShyRecognizerFrontend.g:39:38: proc_ops
                        pass 
                        self._state.following.append(self.FOLLOW_proc_ops_in_proc275)
                        proc_ops27 = self.proc_ops()

                        self._state.following.pop()
                        stream_proc_ops.add(proc_ops27.tree)





                    DEDENT28 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc287) 
                    stream_DEDENT.add(DEDENT28)


                    NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc289) 
                    stream_NEWLINE.add(NEWLINE29)


                    # AST Rewrite
                    # elements: ID, proc_ops, proc_attrs, proc_args
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 41:9: -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? )
                    # grammar/ShyRecognizerFrontend.g:41:12: ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? )
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

                    # grammar/ShyRecognizerFrontend.g:41:40: ( proc_attrs )?
                    if stream_proc_attrs.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_attrs.nextTree())


                    stream_proc_attrs.reset();

                    # grammar/ShyRecognizerFrontend.g:41:53: ( proc_ops )?
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
    # grammar/ShyRecognizerFrontend.g:44:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS30 = None
        attrs_hints31 = None


        ARGS30_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:45:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:45:9: ARGS attrs_hints
                pass 
                ARGS30 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args338) 
                stream_ARGS.add(ARGS30)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args340)
                attrs_hints31 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints31.tree)


                # AST Rewrite
                # elements: attrs_hints
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 45:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:45:29: ^( TREE_PROC_ARGS attrs_hints )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC_ARGS, "TREE_PROC_ARGS")
                , root_1)

                self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

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


    class proc_attrs_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_attrs_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc_attrs"
    # grammar/ShyRecognizerFrontend.g:48:1: proc_attrs : VARS attrs_hints -> ^( TREE_PROC_VARS attrs_hints ) ;
    def proc_attrs(self, ):
        retval = self.proc_attrs_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS32 = None
        attrs_hints33 = None


        VARS32_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:49:5: ( VARS attrs_hints -> ^( TREE_PROC_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:49:9: VARS attrs_hints
                pass 
                VARS32 = self.match(self.input, VARS, self.FOLLOW_VARS_in_proc_attrs369) 
                stream_VARS.add(VARS32)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_attrs371)
                attrs_hints33 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints33.tree)


                # AST Rewrite
                # elements: attrs_hints
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 49:26: -> ^( TREE_PROC_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:49:29: ^( TREE_PROC_VARS attrs_hints )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_PROC_VARS, "TREE_PROC_VARS")
                , root_1)

                self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

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

    # $ANTLR end "proc_attrs"


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

        OPS34 = None
        NEWLINE35 = None
        INDENT36 = None
        NEWLINE37 = None
        DEDENT39 = None
        NEWLINE40 = None
        statements38 = None


        OPS34_tree = None
        NEWLINE35_tree = None
        INDENT36_tree = None
        NEWLINE37_tree = None
        DEDENT39_tree = None
        NEWLINE40_tree = None
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
                OPS34 = self.match(self.input, OPS, self.FOLLOW_OPS_in_proc_ops400) 
                stream_OPS.add(OPS34)


                NEWLINE35 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops402) 
                stream_NEWLINE.add(NEWLINE35)


                INDENT36 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc_ops404) 
                stream_INDENT.add(INDENT36)


                NEWLINE37 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops406) 
                stream_NEWLINE.add(NEWLINE37)


                self._state.following.append(self.FOLLOW_statements_in_proc_ops408)
                statements38 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements38.tree)


                DEDENT39 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc_ops410) 
                stream_DEDENT.add(DEDENT39)


                NEWLINE40 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops412) 
                stream_NEWLINE.add(NEWLINE40)


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

        NEWLINE42 = None
        statement_call_single_line41 = None

        statement_call_multi_line43 = None

        statement_if44 = None

        statement_assign45 = None

        statement_with46 = None


        NEWLINE42_tree = None
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
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement443)
                    statement_call_single_line41 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line41.tree)


                    NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement445) 
                    stream_NEWLINE.add(NEWLINE42)


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


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement471)
                    statement_call_multi_line43 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line43.tree)



                elif alt8 == 3:
                    # grammar/ShyRecognizerFrontend.g:61:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement481)
                    statement_if44 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if44.tree)



                elif alt8 == 4:
                    # grammar/ShyRecognizerFrontend.g:62:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement491)
                    statement_assign45 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign45.tree)



                elif alt8 == 5:
                    # grammar/ShyRecognizerFrontend.g:63:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement501)
                    statement_with46 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with46.tree)



                retval.stop = self.input.LT(-1)


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

        statement47 = None


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
                        self._state.following.append(self.FOLLOW_statement_in_statements520)
                        statement47 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement47.tree)



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

        WITH48 = None
        ID49 = None
        NEWLINE50 = None
        INDENT51 = None
        NEWLINE52 = None
        DEDENT54 = None
        NEWLINE55 = None
        statements53 = None


        WITH48_tree = None
        ID49_tree = None
        NEWLINE50_tree = None
        INDENT51_tree = None
        NEWLINE52_tree = None
        DEDENT54_tree = None
        NEWLINE55_tree = None
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
                WITH48 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with561) 
                stream_WITH.add(WITH48)


                ID49 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with563) 
                stream_ID.add(ID49)


                NEWLINE50 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with565) 
                stream_NEWLINE.add(NEWLINE50)


                INDENT51 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with575) 
                stream_INDENT.add(INDENT51)


                NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with577) 
                stream_NEWLINE.add(NEWLINE52)


                self._state.following.append(self.FOLLOW_statements_in_statement_with579)
                statements53 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements53.tree)


                DEDENT54 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with581) 
                stream_DEDENT.add(DEDENT54)


                NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with583) 
                stream_NEWLINE.add(NEWLINE55)


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

        ID56 = None
        ARROW_LEFT57 = None
        NEWLINE59 = None
        arbitrary_value58 = None


        ID56_tree = None
        ARROW_LEFT57_tree = None
        NEWLINE59_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:78:5: ( ID ARROW_LEFT arbitrary_value NEWLINE -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID ) )
                # grammar/ShyRecognizerFrontend.g:78:9: ID ARROW_LEFT arbitrary_value NEWLINE
                pass 
                ID56 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign623) 
                stream_ID.add(ID56)


                ARROW_LEFT57 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign625) 
                stream_ARROW_LEFT.add(ARROW_LEFT57)


                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign627)
                arbitrary_value58 = self.arbitrary_value()

                self._state.following.pop()
                stream_arbitrary_value.add(arbitrary_value58.tree)


                NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign629) 
                stream_NEWLINE.add(NEWLINE59)


                # AST Rewrite
                # elements: ID, arbitrary_value
                # token labels: 
                # rule labels: retval
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

        statement_if_head60 = None

        statement_elif61 = None

        statement_else62 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:83:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if669)
                statement_if_head60 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head60.tree)


                # grammar/ShyRecognizerFrontend.g:84:9: ( statement_elif )*
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ELIF) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:84:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if679)
                        statement_elif61 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif61.tree)



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
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if691)
                    statement_else62 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else62.tree)





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

        IF63 = None
        statement_elif_body64 = None


        IF63_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:94:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:94:9: IF statement_elif_body
                pass 
                IF63 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head799) 
                stream_IF.add(IF63)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head801)
                statement_elif_body64 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body64.tree)


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

        ELIF65 = None
        statement_elif_body66 = None


        ELIF65_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:99:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:99:9: ELIF statement_elif_body
                pass 
                ELIF65 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif833) 
                stream_ELIF.add(ELIF65)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif835)
                statement_elif_body66 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body66.tree)


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

        NEWLINE68 = None
        DO69 = None
        NEWLINE70 = None
        INDENT71 = None
        NEWLINE72 = None
        DEDENT74 = None
        NEWLINE75 = None
        condition67 = None

        statements73 = None


        NEWLINE68_tree = None
        DO69_tree = None
        NEWLINE70_tree = None
        INDENT71_tree = None
        NEWLINE72_tree = None
        DEDENT74_tree = None
        NEWLINE75_tree = None
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
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body867)
                condition67 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition67.tree)


                # grammar/ShyRecognizerFrontend.g:104:19: ( NEWLINE )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == NEWLINE) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:104:19: NEWLINE
                    pass 
                    NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body869) 
                    stream_NEWLINE.add(NEWLINE68)





                DO69 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body873) 
                stream_DO.add(DO69)


                NEWLINE70 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body875) 
                stream_NEWLINE.add(NEWLINE70)


                INDENT71 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body889) 
                stream_INDENT.add(INDENT71)


                NEWLINE72 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body891) 
                stream_NEWLINE.add(NEWLINE72)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body893)
                statements73 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements73.tree)


                DEDENT74 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body895) 
                stream_DEDENT.add(DEDENT74)


                NEWLINE75 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body897) 
                stream_NEWLINE.add(NEWLINE75)


                # AST Rewrite
                # elements: condition, statements
                # token labels: 
                # rule labels: retval
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

        ELSE76 = None
        NEWLINE77 = None
        INDENT78 = None
        NEWLINE79 = None
        DEDENT81 = None
        NEWLINE82 = None
        statements80 = None


        ELSE76_tree = None
        NEWLINE77_tree = None
        INDENT78_tree = None
        NEWLINE79_tree = None
        DEDENT81_tree = None
        NEWLINE82_tree = None
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
                ELSE76 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else937) 
                stream_ELSE.add(ELSE76)


                NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else939) 
                stream_NEWLINE.add(NEWLINE77)


                INDENT78 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else953) 
                stream_INDENT.add(INDENT78)


                NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else955) 
                stream_NEWLINE.add(NEWLINE79)


                self._state.following.append(self.FOLLOW_statements_in_statement_else957)
                statements80 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements80.tree)


                DEDENT81 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else959) 
                stream_DEDENT.add(DEDENT81)


                NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else961) 
                stream_NEWLINE.add(NEWLINE82)


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

        ANY84 = None
        ALL86 = None
        condition_call83 = None

        condition_calls85 = None

        condition_calls87 = None


        ANY84_tree = None
        ALL86_tree = None
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
                    self._state.following.append(self.FOLLOW_condition_call_in_condition999)
                    condition_call83 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call83.tree)


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
                    ANY84 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1028) 
                    stream_ANY.add(ANY84)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1030)
                    condition_calls85 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls85.tree)


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
                    ALL86 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1059) 
                    stream_ALL.add(ALL86)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1061)
                    condition_calls87 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls87.tree)


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

        NEWLINE89 = None
        INDENT90 = None
        NEWLINE91 = None
        DEDENT93 = None
        NEWLINE94 = None
        condition_call88 = None

        condition_call_line92 = None


        NEWLINE89_tree = None
        INDENT90_tree = None
        NEWLINE91_tree = None
        DEDENT93_tree = None
        NEWLINE94_tree = None
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


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1099)
                    condition_call88 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call88.tree)



                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:126:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1109) 
                    stream_NEWLINE.add(NEWLINE89)


                    INDENT90 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1111) 
                    stream_INDENT.add(INDENT90)


                    NEWLINE91 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1113) 
                    stream_NEWLINE.add(NEWLINE91)


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
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1115)
                            condition_call_line92 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line92.tree)



                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                    DEDENT93 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1119) 
                    stream_DEDENT.add(DEDENT93)


                    NEWLINE94 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1121) 
                    stream_NEWLINE.add(NEWLINE94)


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

        statement_call_single_line95 = None

        statement_call_multi_line96 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:131:5: ( statement_call_single_line | statement_call_multi_line )
                alt16 = 2
                alt16 = self.dfa16.predict(self.input)
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:131:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1155)
                    statement_call_single_line95 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line95.tree)



                elif alt16 == 2:
                    # grammar/ShyRecognizerFrontend.g:132:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1165)
                    statement_call_multi_line96 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line96.tree)



                retval.stop = self.input.LT(-1)


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

        NEWLINE98 = None
        statement_call_single_line97 = None

        statement_call_multi_line99 = None


        NEWLINE98_tree = None
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
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1184)
                    statement_call_single_line97 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line97.tree)


                    NEWLINE98 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1186) 
                    stream_NEWLINE.add(NEWLINE98)


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


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1212)
                    statement_call_multi_line99 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line99.tree)



                retval.stop = self.input.LT(-1)


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

        ID100 = None
        statement_call_args101 = None


        ID100_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:142:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:142:9: ID ( statement_call_args )?
                pass 
                ID100 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1231) 
                stream_ID.add(ID100)


                # grammar/ShyRecognizerFrontend.g:142:12: ( statement_call_args )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if ((EXPRESSION <= LA18_0 <= ID) or LA18_0 == MINUS or LA18_0 == NUMBER) :
                    alt18 = 1
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:142:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1233)
                    statement_call_args101 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args101.tree)





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

        ID102 = None
        NEWLINE104 = None
        INDENT105 = None
        NEWLINE106 = None
        NEWLINE108 = None
        DEDENT109 = None
        NEWLINE110 = None
        statement_call_args103 = None

        statement_call_args107 = None


        ID102_tree = None
        NEWLINE104_tree = None
        INDENT105_tree = None
        NEWLINE106_tree = None
        NEWLINE108_tree = None
        DEDENT109_tree = None
        NEWLINE110_tree = None
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
                ID102 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1277) 
                stream_ID.add(ID102)


                # grammar/ShyRecognizerFrontend.g:147:12: ( statement_call_args )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:147:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1279)
                    statement_call_args103 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args103.tree)





                NEWLINE104 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1283) 
                stream_NEWLINE.add(NEWLINE104)


                INDENT105 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1293) 
                stream_INDENT.add(INDENT105)


                NEWLINE106 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1295) 
                stream_NEWLINE.add(NEWLINE106)


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
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1299)
                        statement_call_args107 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args107.tree)


                        NEWLINE108 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1301) 
                        stream_NEWLINE.add(NEWLINE108)



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1


                DEDENT109 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1307) 
                stream_DEDENT.add(DEDENT109)


                NEWLINE110 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1309) 
                stream_NEWLINE.add(NEWLINE110)


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

        arbitrary_value111 = None



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
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1345)
                        arbitrary_value111 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value111.tree)



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

        ID112 = None
        EXPRESSION113 = None
        num_whole114 = None

        num_fract115 = None


        ID112_tree = None
        EXPRESSION113_tree = None

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


                    ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1362)
                    ID112_tree = self._adaptor.createWithPayload(ID112)
                    self._adaptor.addChild(root_0, ID112_tree)




                elif alt22 == 2:
                    # grammar/ShyRecognizerFrontend.g:156:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION113 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1372)
                    EXPRESSION113_tree = self._adaptor.createWithPayload(EXPRESSION113)
                    self._adaptor.addChild(root_0, EXPRESSION113_tree)




                elif alt22 == 3:
                    # grammar/ShyRecognizerFrontend.g:157:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1382)
                    num_whole114 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole114.tree)



                elif alt22 == 4:
                    # grammar/ShyRecognizerFrontend.g:158:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1392)
                    num_fract115 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract115.tree)



                retval.stop = self.input.LT(-1)


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

        CONSTS116 = None
        ID117 = None
        NEWLINE118 = None
        INDENT119 = None
        NEWLINE120 = None
        DEDENT122 = None
        NEWLINE123 = None
        consts_items121 = None


        CONSTS116_tree = None
        ID117_tree = None
        NEWLINE118_tree = None
        INDENT119_tree = None
        NEWLINE120_tree = None
        DEDENT122_tree = None
        NEWLINE123_tree = None
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
                CONSTS116 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1411) 
                stream_CONSTS.add(CONSTS116)


                ID117 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1413) 
                stream_ID.add(ID117)


                NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1415) 
                stream_NEWLINE.add(NEWLINE118)


                INDENT119 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1425) 
                stream_INDENT.add(INDENT119)


                NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1427) 
                stream_NEWLINE.add(NEWLINE120)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1429)
                consts_items121 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items121.tree)


                DEDENT122 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1431) 
                stream_DEDENT.add(DEDENT122)


                NEWLINE123 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1433) 
                stream_NEWLINE.add(NEWLINE123)


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

        consts_item124 = None



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
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1465)
                        consts_item124 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item124.tree)



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

        ID125 = None
        NEWLINE127 = None
        ID128 = None
        NEWLINE130 = None
        ID131 = None
        EXPRESSION132 = None
        NEWLINE133 = None
        num_whole126 = None

        num_fract129 = None


        ID125_tree = None
        NEWLINE127_tree = None
        ID128_tree = None
        NEWLINE130_tree = None
        ID131_tree = None
        EXPRESSION132_tree = None
        NEWLINE133_tree = None
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
                    ID125 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1481) 
                    stream_ID.add(ID125)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1483)
                    num_whole126 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole126.tree)


                    NEWLINE127 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1485) 
                    stream_NEWLINE.add(NEWLINE127)


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
                    ID128 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1507) 
                    stream_ID.add(ID128)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1509)
                    num_fract129 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract129.tree)


                    NEWLINE130 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1511) 
                    stream_NEWLINE.add(NEWLINE130)


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
                    ID131 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1533) 
                    stream_ID.add(ID131)


                    EXPRESSION132 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1535) 
                    stream_EXPRESSION.add(EXPRESSION132)


                    NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1537) 
                    stream_NEWLINE.add(NEWLINE133)


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
    # grammar/ShyRecognizerFrontend.g:173:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES134 = None
        ID135 = None
        NEWLINE136 = None
        INDENT137 = None
        NEWLINE138 = None
        DEDENT140 = None
        NEWLINE141 = None
        types_item139 = None


        TYPES134_tree = None
        ID135_tree = None
        NEWLINE136_tree = None
        INDENT137_tree = None
        NEWLINE138_tree = None
        DEDENT140_tree = None
        NEWLINE141_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:174:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES134 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1568) 
                stream_TYPES.add(TYPES134)


                ID135 = self.match(self.input, ID, self.FOLLOW_ID_in_types1570) 
                stream_ID.add(ID135)


                NEWLINE136 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1572) 
                stream_NEWLINE.add(NEWLINE136)


                INDENT137 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1582) 
                stream_INDENT.add(INDENT137)


                NEWLINE138 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1584) 
                stream_NEWLINE.add(NEWLINE138)


                # grammar/ShyRecognizerFrontend.g:175:24: ( types_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ID) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:175:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types1586)
                        types_item139 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item139.tree)



                    else:
                        if cnt25 >= 1:
                            break #loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1


                DEDENT140 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1590) 
                stream_DEDENT.add(DEDENT140)


                NEWLINE141 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1592) 
                stream_NEWLINE.add(NEWLINE141)


                # AST Rewrite
                # elements: types_item, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 176:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:176:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:176:29: ( types_item )+
                if not (stream_types_item.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_types_item.hasNext():
                    self._adaptor.addChild(root_1, stream_types_item.nextTree())


                stream_types_item.reset()

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


    class types_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.types_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "types_item"
    # grammar/ShyRecognizerFrontend.g:178:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID142 = None
        attrs_hints143 = None


        ID142_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:178:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:178:14: ID attrs_hints
                pass 
                ID142 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1626) 
                stream_ID.add(ID142)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item1628)
                attrs_hints143 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints143.tree)


                # AST Rewrite
                # elements: attrs_hints, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 178:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:178:32: ^( TREE_TYPES_ITEM ID attrs_hints )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES_ITEM, "TREE_TYPES_ITEM")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

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


    class messages_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.messages_return, self).__init__()

            self.tree = None





    # $ANTLR start "messages"
    # grammar/ShyRecognizerFrontend.g:180:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES144 = None
        ID145 = None
        NEWLINE146 = None
        INDENT147 = None
        NEWLINE148 = None
        DEDENT150 = None
        NEWLINE151 = None
        messages_item149 = None


        MESSAGES144_tree = None
        ID145_tree = None
        NEWLINE146_tree = None
        INDENT147_tree = None
        NEWLINE148_tree = None
        DEDENT150_tree = None
        NEWLINE151_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:181:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:181:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES144 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages1655) 
                stream_MESSAGES.add(MESSAGES144)


                ID145 = self.match(self.input, ID, self.FOLLOW_ID_in_messages1657) 
                stream_ID.add(ID145)


                NEWLINE146 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1659) 
                stream_NEWLINE.add(NEWLINE146)


                INDENT147 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages1669) 
                stream_INDENT.add(INDENT147)


                NEWLINE148 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1671) 
                stream_NEWLINE.add(NEWLINE148)


                # grammar/ShyRecognizerFrontend.g:182:24: ( messages_item )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ID) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerFrontend.g:182:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages1673)
                        messages_item149 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item149.tree)



                    else:
                        if cnt26 >= 1:
                            break #loop26

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1


                DEDENT150 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages1677) 
                stream_DEDENT.add(DEDENT150)


                NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1679) 
                stream_NEWLINE.add(NEWLINE151)


                # AST Rewrite
                # elements: messages_item, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 183:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:183:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:183:32: ( messages_item )+
                if not (stream_messages_item.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_messages_item.hasNext():
                    self._adaptor.addChild(root_1, stream_messages_item.nextTree())


                stream_messages_item.reset()

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

    # $ANTLR end "messages"


    class messages_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.messages_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "messages_item"
    # grammar/ShyRecognizerFrontend.g:185:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID152 = None
        attrs_hints153 = None


        ID152_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:185:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:185:17: ID attrs_hints
                pass 
                ID152 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item1713) 
                stream_ID.add(ID152)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item1715)
                attrs_hints153 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints153.tree)


                # AST Rewrite
                # elements: ID, attrs_hints
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 185:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:185:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES_ITEM, "TREE_MESSAGES_ITEM")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

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

    # $ANTLR end "messages_item"


    class attrs_hints_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.attrs_hints_return, self).__init__()

            self.tree = None





    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerFrontend.g:187:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE155 = None
        NEWLINE156 = None
        INDENT157 = None
        NEWLINE158 = None
        NEWLINE160 = None
        DEDENT161 = None
        NEWLINE162 = None
        NEWLINE164 = None
        INDENT165 = None
        NEWLINE166 = None
        NEWLINE168 = None
        DEDENT169 = None
        NEWLINE170 = None
        attr_hint154 = None

        attr_hint159 = None

        attr_hint163 = None

        attr_hint167 = None


        NEWLINE155_tree = None
        NEWLINE156_tree = None
        INDENT157_tree = None
        NEWLINE158_tree = None
        NEWLINE160_tree = None
        DEDENT161_tree = None
        NEWLINE162_tree = None
        NEWLINE164_tree = None
        INDENT165_tree = None
        NEWLINE166_tree = None
        NEWLINE168_tree = None
        DEDENT169_tree = None
        NEWLINE170_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:188:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt29 = 3
                alt29 = self.dfa29.predict(self.input)
                if alt29 == 1:
                    # grammar/ShyRecognizerFrontend.g:188:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1742)
                    attr_hint154 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint154.tree)


                    NEWLINE155 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1744) 
                    stream_NEWLINE.add(NEWLINE155)


                    # AST Rewrite
                    # elements: attr_hint
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 189:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt29 == 2:
                    # grammar/ShyRecognizerFrontend.g:190:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE156 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1768) 
                    stream_NEWLINE.add(NEWLINE156)


                    # grammar/ShyRecognizerFrontend.g:191:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:191:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT157 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints1780) 
                    stream_INDENT.add(INDENT157)


                    NEWLINE158 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1782) 
                    stream_NEWLINE.add(NEWLINE158)


                    # grammar/ShyRecognizerFrontend.g:191:26: ( attr_hint NEWLINE )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == CURLY_OPEN or LA27_0 == ID) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:191:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1786)
                            attr_hint159 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint159.tree)


                            NEWLINE160 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1788) 
                            stream_NEWLINE.add(NEWLINE160)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    DEDENT161 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints1794) 
                    stream_DEDENT.add(DEDENT161)


                    NEWLINE162 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1796) 
                    stream_NEWLINE.add(NEWLINE162)





                    # AST Rewrite
                    # elements: attr_hint
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 192:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:192:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt29 == 3:
                    # grammar/ShyRecognizerFrontend.g:193:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1824)
                    attr_hint163 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint163.tree)


                    NEWLINE164 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1826) 
                    stream_NEWLINE.add(NEWLINE164)


                    # grammar/ShyRecognizerFrontend.g:194:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:194:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT165 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints1838) 
                    stream_INDENT.add(INDENT165)


                    NEWLINE166 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1840) 
                    stream_NEWLINE.add(NEWLINE166)


                    # grammar/ShyRecognizerFrontend.g:194:26: ( attr_hint NEWLINE )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == CURLY_OPEN or LA28_0 == ID) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:194:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1844)
                            attr_hint167 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint167.tree)


                            NEWLINE168 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1846) 
                            stream_NEWLINE.add(NEWLINE168)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    DEDENT169 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints1852) 
                    stream_DEDENT.add(DEDENT169)


                    NEWLINE170 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1854) 
                    stream_NEWLINE.add(NEWLINE170)





                    # AST Rewrite
                    # elements: attr_hint
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 195:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:195:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




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

    # $ANTLR end "attrs_hints"


    class attr_hint_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.attr_hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "attr_hint"
    # grammar/ShyRecognizerFrontend.g:197:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID171 = None
        ID173 = None
        NEWLINE175 = None
        INDENT176 = None
        NEWLINE177 = None
        ID178 = None
        NEWLINE179 = None
        DEDENT180 = None
        hint172 = None

        hint174 = None


        ID171_tree = None
        ID173_tree = None
        NEWLINE175_tree = None
        INDENT176_tree = None
        NEWLINE177_tree = None
        ID178_tree = None
        NEWLINE179_tree = None
        DEDENT180_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:198:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt34 = 3
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:198:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:198:9: ( ID )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == ID) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:198:9: ID
                            pass 
                            ID171 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint1891) 
                            stream_ID.add(ID171)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


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
                    # 199:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:199:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:199:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:199:45: ^( TREE_ATTR ID )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_ATTR, "TREE_ATTR")
                        , root_2)

                        self._adaptor.addChild(root_2, 
                        stream_ID.nextNode()
                        )

                        self._adaptor.addChild(root_1, root_2)


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt34 == 2:
                    # grammar/ShyRecognizerFrontend.g:200:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint1932)
                    hint172 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint172.tree)


                    # grammar/ShyRecognizerFrontend.g:200:14: ( ID )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == ID) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:200:14: ID
                            pass 
                            ID173 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint1934) 
                            stream_ID.add(ID173)



                        else:
                            if cnt31 >= 1:
                                break #loop31

                            eee = EarlyExitException(31, self.input)
                            raise eee

                        cnt31 += 1


                    # AST Rewrite
                    # elements: ID, hint
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 201:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:201:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:201:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:201:35: ^( TREE_ATTR ID )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_ATTR, "TREE_ATTR")
                        , root_2)

                        self._adaptor.addChild(root_2, 
                        stream_ID.nextNode()
                        )

                        self._adaptor.addChild(root_1, root_2)


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt34 == 3:
                    # grammar/ShyRecognizerFrontend.g:202:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint1974)
                    hint174 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint174.tree)


                    NEWLINE175 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint1976) 
                    stream_NEWLINE.add(NEWLINE175)


                    INDENT176 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint1978) 
                    stream_INDENT.add(INDENT176)


                    NEWLINE177 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint1980) 
                    stream_NEWLINE.add(NEWLINE177)


                    # grammar/ShyRecognizerFrontend.g:202:37: ( ( ID )+ NEWLINE )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == ID) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerFrontend.g:202:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:202:39: ( ID )+
                            cnt32 = 0
                            while True: #loop32
                                alt32 = 2
                                LA32_0 = self.input.LA(1)

                                if (LA32_0 == ID) :
                                    alt32 = 1


                                if alt32 == 1:
                                    # grammar/ShyRecognizerFrontend.g:202:39: ID
                                    pass 
                                    ID178 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint1984) 
                                    stream_ID.add(ID178)



                                else:
                                    if cnt32 >= 1:
                                        break #loop32

                                    eee = EarlyExitException(32, self.input)
                                    raise eee

                                cnt32 += 1


                            NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint1988) 
                            stream_NEWLINE.add(NEWLINE179)



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


                    DEDENT180 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint1994) 
                    stream_DEDENT.add(DEDENT180)


                    # AST Rewrite
                    # elements: ID, hint
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 203:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:203:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:203:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:203:35: ^( TREE_ATTR ID )
                        root_2 = self._adaptor.nil()
                        root_2 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(TREE_ATTR, "TREE_ATTR")
                        , root_2)

                        self._adaptor.addChild(root_2, 
                        stream_ID.nextNode()
                        )

                        self._adaptor.addChild(root_1, root_2)


                    stream_ID.reset()

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

    # $ANTLR end "attr_hint"


    class hint_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.hint_return, self).__init__()

            self.tree = None





    # $ANTLR start "hint"
    # grammar/ShyRecognizerFrontend.g:206:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN181 = None
        ID182 = None
        CURLY_CLOSE183 = None
        CURLY_OPEN184 = None
        ID185 = None
        CURLY_CLOSE187 = None
        hint_arg186 = None


        CURLY_OPEN181_tree = None
        ID182_tree = None
        CURLY_CLOSE183_tree = None
        CURLY_OPEN184_tree = None
        ID185_tree = None
        CURLY_CLOSE187_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:207:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == CURLY_OPEN) :
                    LA36_1 = self.input.LA(2)

                    if (LA36_1 == ID) :
                        LA36_2 = self.input.LA(3)

                        if (LA36_2 == CURLY_CLOSE) :
                            alt36 = 1
                        elif (LA36_2 == ID or LA36_2 == UNDERSCORE) :
                            alt36 = 2
                        else:
                            nvae = NoViableAltException("", 36, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 36, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:207:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN181 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2041) 
                    stream_CURLY_OPEN.add(CURLY_OPEN181)


                    ID182 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2043) 
                    stream_ID.add(ID182)


                    CURLY_CLOSE183 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2045) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE183)


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
                    # 207:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:207:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt36 == 2:
                    # grammar/ShyRecognizerFrontend.g:208:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN184 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2065) 
                    stream_CURLY_OPEN.add(CURLY_OPEN184)


                    ID185 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2067) 
                    stream_ID.add(ID185)


                    # grammar/ShyRecognizerFrontend.g:208:23: ( hint_arg )+
                    cnt35 = 0
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == ID or LA35_0 == UNDERSCORE) :
                            alt35 = 1


                        if alt35 == 1:
                            # grammar/ShyRecognizerFrontend.g:208:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2069)
                            hint_arg186 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg186.tree)



                        else:
                            if cnt35 >= 1:
                                break #loop35

                            eee = EarlyExitException(35, self.input)
                            raise eee

                        cnt35 += 1


                    CURLY_CLOSE187 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2073) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE187)


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
                    # 208:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:208:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:208:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:210:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set188 = None

        set188_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:210:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set188 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set188))

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
    # grammar/ShyRecognizerFrontend.g:212:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS189 = None
        NUMBER190 = None

        MINUS189_tree = None
        NUMBER190_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:212:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:212:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:212:13: ( MINUS )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == MINUS) :
                    alt37 = 1
                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:212:13: MINUS
                    pass 
                    MINUS189 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2112)
                    MINUS189_tree = self._adaptor.createWithPayload(MINUS189)
                    self._adaptor.addChild(root_0, MINUS189_tree)






                NUMBER190 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2116)
                NUMBER190_tree = self._adaptor.createWithPayload(NUMBER190)
                self._adaptor.addChild(root_0, NUMBER190_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:213:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS191 = None
        NUMBER192 = None
        DIVIDE193 = None
        NUMBER194 = None

        MINUS191_tree = None
        NUMBER192_tree = None
        DIVIDE193_tree = None
        NUMBER194_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:213:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:213:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:213:13: ( MINUS )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == MINUS) :
                    alt38 = 1
                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:213:13: MINUS
                    pass 
                    MINUS191 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2124)
                    MINUS191_tree = self._adaptor.createWithPayload(MINUS191)
                    self._adaptor.addChild(root_0, MINUS191_tree)






                NUMBER192 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2128)
                NUMBER192_tree = self._adaptor.createWithPayload(NUMBER192)
                self._adaptor.addChild(root_0, NUMBER192_tree)



                DIVIDE193 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2130)
                DIVIDE193_tree = self._adaptor.createWithPayload(DIVIDE193)
                self._adaptor.addChild(root_0, DIVIDE193_tree)



                NUMBER194 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2132)
                NUMBER194_tree = self._adaptor.createWithPayload(NUMBER194)
                self._adaptor.addChild(root_0, NUMBER194_tree)





                retval.stop = self.input.LT(-1)


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
        u"\1\110\1\32\3\uffff\4\32\1\110\1\32\2\uffff\1\32"
        )

    DFA8_accept = DFA.unpack(
        u"\2\uffff\1\3\1\5\1\4\6\uffff\1\2\1\1\1\uffff"
        )

    DFA8_special = DFA.unpack(
        u"\16\uffff"
        )


    DFA8_transition = [
        DFA.unpack(u"\1\1\1\2\63\uffff\1\3"),
        DFA.unpack(u"\1\4\12\uffff\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u"\1\12\3\uffff\1\6\1\5\3\uffff\1\7\1\uffff\1\11\1\10"),
        DFA.unpack(u"\1\14\5\uffff\2\14\1\13\62\uffff\1\14"),
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


    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA29_eof = DFA.unpack(
        u"\22\uffff"
        )

    DFA29_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\15\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\31\2\23\1\15\1\31"
        )

    DFA29_max = DFA.unpack(
        u"\2\31\1\23\1\uffff\1\106\1\105\2\uffff\1\31\1\105\1\31\1\25\2\31"
        u"\1\23\1\31\1\23\1\31"
        )

    DFA29_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA29_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA29_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1\5\uffff\1\3"),
        DFA.unpack(u"\1\1\5\uffff\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\5\uffff\1\6\1\uffff\1\7\5\uffff\1\6\52\uffff\1"
        u"\6"),
        DFA.unpack(u"\1\10\7\uffff\1\11\61\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\5\uffff\1\13"),
        DFA.unpack(u"\1\14\7\uffff\1\11\61\uffff\1\11"),
        DFA.unpack(u"\1\12\5\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\12\5\uffff\1\13"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\17\5\uffff\1\20"),
        DFA.unpack(u"\1\21\5\uffff\1\17"),
        DFA.unpack(u"\1\4")
    ]

    # class definition for DFA #29

    class DFA29(DFA):
        pass


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA34_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\105\1\31\1\105\2\uffff\1\31"
        )

    DFA34_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA34_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA34_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\7\uffff\1\5\61\uffff\1\5"),
        DFA.unpack(u"\1\6\5\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\61\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\5\uffff\1\7")
    ]

    # class definition for DFA #34

    class DFA34(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 22, 24, 33, 68])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 22, 24, 33, 68])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 22, 24, 33, 68])
    FOLLOW_types_in_start94 = frozenset([1, 9, 22, 24, 33, 68])
    FOLLOW_messages_in_start98 = frozenset([1, 9, 22, 24, 33, 68])
    FOLLOW_MODULE_in_module117 = frozenset([19])
    FOLLOW_ID_in_module119 = frozenset([25])
    FOLLOW_NEWLINE_in_module121 = frozenset([1])
    FOLLOW_STATELESS_in_stateless150 = frozenset([19])
    FOLLOW_ID_in_stateless152 = frozenset([25])
    FOLLOW_NEWLINE_in_stateless154 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless158 = frozenset([25])
    FOLLOW_NEWLINE_in_stateless160 = frozenset([29])
    FOLLOW_proc_in_stateless162 = frozenset([13, 29])
    FOLLOW_DEDENT_in_stateless166 = frozenset([25])
    FOLLOW_NEWLINE_in_stateless168 = frozenset([1])
    FOLLOW_PROC_in_proc213 = frozenset([19])
    FOLLOW_ID_in_proc215 = frozenset([25])
    FOLLOW_NEWLINE_in_proc217 = frozenset([1])
    FOLLOW_PROC_in_proc245 = frozenset([19])
    FOLLOW_ID_in_proc247 = frozenset([25])
    FOLLOW_NEWLINE_in_proc249 = frozenset([21])
    FOLLOW_INDENT_in_proc251 = frozenset([25])
    FOLLOW_NEWLINE_in_proc253 = frozenset([6, 13, 27, 70])
    FOLLOW_proc_args_in_proc267 = frozenset([13, 27, 70])
    FOLLOW_proc_attrs_in_proc271 = frozenset([13, 27])
    FOLLOW_proc_ops_in_proc275 = frozenset([13])
    FOLLOW_DEDENT_in_proc287 = frozenset([25])
    FOLLOW_NEWLINE_in_proc289 = frozenset([1])
    FOLLOW_ARGS_in_proc_args338 = frozenset([12, 19, 25])
    FOLLOW_attrs_hints_in_proc_args340 = frozenset([1])
    FOLLOW_VARS_in_proc_attrs369 = frozenset([12, 19, 25])
    FOLLOW_attrs_hints_in_proc_attrs371 = frozenset([1])
    FOLLOW_OPS_in_proc_ops400 = frozenset([25])
    FOLLOW_NEWLINE_in_proc_ops402 = frozenset([21])
    FOLLOW_INDENT_in_proc_ops404 = frozenset([25])
    FOLLOW_NEWLINE_in_proc_ops406 = frozenset([19, 20, 72])
    FOLLOW_statements_in_proc_ops408 = frozenset([13])
    FOLLOW_DEDENT_in_proc_ops410 = frozenset([25])
    FOLLOW_NEWLINE_in_proc_ops412 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement443 = frozenset([25])
    FOLLOW_NEWLINE_in_statement445 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement471 = frozenset([1])
    FOLLOW_statement_if_in_statement481 = frozenset([1])
    FOLLOW_statement_assign_in_statement491 = frozenset([1])
    FOLLOW_statement_with_in_statement501 = frozenset([1])
    FOLLOW_statement_in_statements520 = frozenset([1, 19, 20, 72])
    FOLLOW_WITH_in_statement_with561 = frozenset([19])
    FOLLOW_ID_in_statement_with563 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_with565 = frozenset([21])
    FOLLOW_INDENT_in_statement_with575 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_with577 = frozenset([19, 20, 72])
    FOLLOW_statements_in_statement_with579 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with581 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_with583 = frozenset([1])
    FOLLOW_ID_in_statement_assign623 = frozenset([7])
    FOLLOW_ARROW_LEFT_in_statement_assign625 = frozenset([18, 19, 23, 26])
    FOLLOW_arbitrary_value_in_statement_assign627 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_assign629 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if669 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if679 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if691 = frozenset([1])
    FOLLOW_IF_in_statement_if_head799 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head801 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif833 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif835 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body867 = frozenset([15, 25])
    FOLLOW_NEWLINE_in_statement_elif_body869 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body873 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_elif_body875 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body889 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_elif_body891 = frozenset([19, 20, 72])
    FOLLOW_statements_in_statement_elif_body893 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body895 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_elif_body897 = frozenset([1])
    FOLLOW_ELSE_in_statement_else937 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_else939 = frozenset([21])
    FOLLOW_INDENT_in_statement_else953 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_else955 = frozenset([19, 20, 72])
    FOLLOW_statements_in_statement_else957 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else959 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_else961 = frozenset([1])
    FOLLOW_condition_call_in_condition999 = frozenset([1])
    FOLLOW_ANY_in_condition1028 = frozenset([19, 25])
    FOLLOW_condition_calls_in_condition1030 = frozenset([1])
    FOLLOW_ALL_in_condition1059 = frozenset([19, 25])
    FOLLOW_condition_calls_in_condition1061 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1099 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1109 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1111 = frozenset([25])
    FOLLOW_NEWLINE_in_condition_calls1113 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1115 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1119 = frozenset([25])
    FOLLOW_NEWLINE_in_condition_calls1121 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1155 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1165 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1184 = frozenset([25])
    FOLLOW_NEWLINE_in_condition_call_line1186 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1212 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1231 = frozenset([1, 18, 19, 23, 26])
    FOLLOW_statement_call_args_in_statement_call_single_line1233 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1277 = frozenset([18, 19, 23, 25, 26])
    FOLLOW_statement_call_args_in_statement_call_multi_line1279 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1283 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1293 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1295 = frozenset([18, 19, 23, 26])
    FOLLOW_statement_call_args_in_statement_call_multi_line1299 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1301 = frozenset([13, 18, 19, 23, 26])
    FOLLOW_DEDENT_in_statement_call_multi_line1307 = frozenset([25])
    FOLLOW_NEWLINE_in_statement_call_multi_line1309 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args1345 = frozenset([1, 18, 19, 23, 26])
    FOLLOW_ID_in_arbitrary_value1362 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1372 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1382 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1392 = frozenset([1])
    FOLLOW_CONSTS_in_consts1411 = frozenset([19])
    FOLLOW_ID_in_consts1413 = frozenset([25])
    FOLLOW_NEWLINE_in_consts1415 = frozenset([21])
    FOLLOW_INDENT_in_consts1425 = frozenset([25])
    FOLLOW_NEWLINE_in_consts1427 = frozenset([19])
    FOLLOW_consts_items_in_consts1429 = frozenset([13])
    FOLLOW_DEDENT_in_consts1431 = frozenset([25])
    FOLLOW_NEWLINE_in_consts1433 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1465 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1481 = frozenset([23, 26])
    FOLLOW_num_whole_in_consts_item1483 = frozenset([25])
    FOLLOW_NEWLINE_in_consts_item1485 = frozenset([1])
    FOLLOW_ID_in_consts_item1507 = frozenset([23, 26])
    FOLLOW_num_fract_in_consts_item1509 = frozenset([25])
    FOLLOW_NEWLINE_in_consts_item1511 = frozenset([1])
    FOLLOW_ID_in_consts_item1533 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1535 = frozenset([25])
    FOLLOW_NEWLINE_in_consts_item1537 = frozenset([1])
    FOLLOW_TYPES_in_types1568 = frozenset([19])
    FOLLOW_ID_in_types1570 = frozenset([25])
    FOLLOW_NEWLINE_in_types1572 = frozenset([21])
    FOLLOW_INDENT_in_types1582 = frozenset([25])
    FOLLOW_NEWLINE_in_types1584 = frozenset([19])
    FOLLOW_types_item_in_types1586 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types1590 = frozenset([25])
    FOLLOW_NEWLINE_in_types1592 = frozenset([1])
    FOLLOW_ID_in_types_item1626 = frozenset([12, 19, 25])
    FOLLOW_attrs_hints_in_types_item1628 = frozenset([1])
    FOLLOW_MESSAGES_in_messages1655 = frozenset([19])
    FOLLOW_ID_in_messages1657 = frozenset([25])
    FOLLOW_NEWLINE_in_messages1659 = frozenset([21])
    FOLLOW_INDENT_in_messages1669 = frozenset([25])
    FOLLOW_NEWLINE_in_messages1671 = frozenset([19])
    FOLLOW_messages_item_in_messages1673 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages1677 = frozenset([25])
    FOLLOW_NEWLINE_in_messages1679 = frozenset([1])
    FOLLOW_ID_in_messages_item1713 = frozenset([12, 19, 25])
    FOLLOW_attrs_hints_in_messages_item1715 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints1742 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1744 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints1768 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints1780 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1782 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints1786 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1788 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints1794 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1796 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints1824 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1826 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints1838 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1840 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints1844 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1846 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints1852 = frozenset([25])
    FOLLOW_NEWLINE_in_attrs_hints1854 = frozenset([1])
    FOLLOW_ID_in_attr_hint1891 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint1932 = frozenset([19])
    FOLLOW_ID_in_attr_hint1934 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint1974 = frozenset([25])
    FOLLOW_NEWLINE_in_attr_hint1976 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint1978 = frozenset([25])
    FOLLOW_NEWLINE_in_attr_hint1980 = frozenset([19])
    FOLLOW_ID_in_attr_hint1984 = frozenset([19, 25])
    FOLLOW_NEWLINE_in_attr_hint1988 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint1994 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2041 = frozenset([19])
    FOLLOW_ID_in_hint2043 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2045 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2065 = frozenset([19])
    FOLLOW_ID_in_hint2067 = frozenset([19, 69])
    FOLLOW_hint_arg_in_hint2069 = frozenset([11, 19, 69])
    FOLLOW_CURLY_CLOSE_in_hint2073 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2112 = frozenset([26])
    FOLLOW_NUMBER_in_num_whole2116 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2124 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2128 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2130 = frozenset([26])
    FOLLOW_NUMBER_in_num_fract2132 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
