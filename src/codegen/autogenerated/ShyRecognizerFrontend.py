# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-31 19:47:30

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
MODULE_QUEUE=25
NEWLINE=26
NUMBER=27
OPS=28
PASTE=29
PROC=30
REPLACE=31
REPLY=32
REQUEST=33
STATELESS=34
STRING=35
TREE_ARBITRARY_TOKEN=36
TREE_ATTR=37
TREE_ATTRS_HINTS=38
TREE_ATTR_HINT=39
TREE_CONDITION_ALL=40
TREE_CONDITION_ANY=41
TREE_CONSTS=42
TREE_COPY=43
TREE_COPY_PASTE=44
TREE_EXPRESSION=45
TREE_HINT=46
TREE_HINT_NONE=47
TREE_MESSAGES=48
TREE_MESSAGES_ITEM=49
TREE_MODULE=50
TREE_MODULE_QUEUE=51
TREE_NUM_FRACT=52
TREE_NUM_WHOLE=53
TREE_PASTE=54
TREE_PASTE_REPLACE=55
TREE_PASTE_WITH=56
TREE_PROC=57
TREE_PROC_ARGS=58
TREE_PROC_VARS=59
TREE_STATELESS=60
TREE_STATEMENTS=61
TREE_STATEMENT_ASSIGN=62
TREE_STATEMENT_CALL=63
TREE_STATEMENT_ELIF=64
TREE_STATEMENT_ELSE=65
TREE_STATEMENT_IF=66
TREE_STATEMENT_WITH=67
TREE_TYPES=68
TREE_TYPES_ITEM=69
TREE_VARS=70
TYPES=71
UNDERSCORE=72
VARS=73
WHITESPACE=74
WITH=75

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "REPLACE", "REPLY", "REQUEST", 
    "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", "TREE_ATTRS_HINTS", 
    "TREE_ATTR_HINT", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", "TREE_CONSTS", 
    "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", 
    "TREE_MESSAGES", "TREE_MESSAGES_ITEM", "TREE_MODULE", "TREE_MODULE_QUEUE", 
    "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_PASTE", "TREE_PASTE_REPLACE", 
    "TREE_PASTE_WITH", "TREE_PROC", "TREE_PROC_ARGS", "TREE_PROC_VARS", 
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_CALL", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WITH", 
    "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", "UNDERSCORE", 
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

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )

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
    # grammar/ShyRecognizerFrontend.g:24:1: start : ( module | stateless | consts | types | messages | vars )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        module1 = None

        stateless2 = None

        consts3 = None

        types4 = None

        messages5 = None

        vars6 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:24:7: ( ( module | stateless | consts | types | messages | vars )* )
                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types | messages | vars )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types | messages | vars )*
                while True: #loop1
                    alt1 = 7
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
                    elif LA1 == VARS:
                        alt1 = 6

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



                    elif alt1 == 6:
                        # grammar/ShyRecognizerFrontend.g:24:60: vars
                        pass 
                        self._state.following.append(self.FOLLOW_vars_in_start102)
                        vars6 = self.vars()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, vars6.tree)



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
    # grammar/ShyRecognizerFrontend.g:26:1: module : MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE7 = None
        ID8 = None
        NEWLINE9 = None
        INDENT10 = None
        NEWLINE11 = None
        DEDENT13 = None
        NEWLINE14 = None
        module_queue12 = None


        MODULE7_tree = None
        ID8_tree = None
        NEWLINE9_tree = None
        INDENT10_tree = None
        NEWLINE11_tree = None
        DEDENT13_tree = None
        NEWLINE14_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_module_queue = RewriteRuleSubtreeStream(self._adaptor, "rule module_queue")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:27:5: ( MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ) )
                # grammar/ShyRecognizerFrontend.g:27:9: MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? DEDENT NEWLINE
                pass 
                MODULE7 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module121) 
                stream_MODULE.add(MODULE7)


                ID8 = self.match(self.input, ID, self.FOLLOW_ID_in_module123) 
                stream_ID.add(ID8)


                NEWLINE9 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module125) 
                stream_NEWLINE.add(NEWLINE9)


                INDENT10 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_module127) 
                stream_INDENT.add(INDENT10)


                NEWLINE11 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module129) 
                stream_NEWLINE.add(NEWLINE11)


                # grammar/ShyRecognizerFrontend.g:28:9: ( module_queue )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == MODULE_QUEUE) :
                    alt2 = 1
                if alt2 == 1:
                    # grammar/ShyRecognizerFrontend.g:28:9: module_queue
                    pass 
                    self._state.following.append(self.FOLLOW_module_queue_in_module139)
                    module_queue12 = self.module_queue()

                    self._state.following.pop()
                    stream_module_queue.add(module_queue12.tree)





                DEDENT13 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_module151) 
                stream_DEDENT.add(DEDENT13)


                NEWLINE14 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module153) 
                stream_NEWLINE.add(NEWLINE14)


                # AST Rewrite
                # elements: module_queue, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 30:9: -> ^( TREE_MODULE ID ( module_queue )? )
                # grammar/ShyRecognizerFrontend.g:30:13: ^( TREE_MODULE ID ( module_queue )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MODULE, "TREE_MODULE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:30:31: ( module_queue )?
                if stream_module_queue.hasNext():
                    self._adaptor.addChild(root_1, stream_module_queue.nextTree())


                stream_module_queue.reset();

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


    class module_queue_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.module_queue_return, self).__init__()

            self.tree = None





    # $ANTLR start "module_queue"
    # grammar/ShyRecognizerFrontend.g:33:1: module_queue : MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        retval = self.module_queue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE_QUEUE15 = None
        ID16 = None
        NEWLINE17 = None

        MODULE_QUEUE15_tree = None
        ID16_tree = None
        NEWLINE17_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE_QUEUE = RewriteRuleTokenStream(self._adaptor, "token MODULE_QUEUE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:34:5: ( MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerFrontend.g:34:9: MODULE_QUEUE ID NEWLINE
                pass 
                MODULE_QUEUE15 = self.match(self.input, MODULE_QUEUE, self.FOLLOW_MODULE_QUEUE_in_module_queue195) 
                stream_MODULE_QUEUE.add(MODULE_QUEUE15)


                ID16 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue197) 
                stream_ID.add(ID16)


                NEWLINE17 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module_queue199) 
                stream_NEWLINE.add(NEWLINE17)


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
                # 35:9: -> ^( TREE_MODULE_QUEUE ID )
                # grammar/ShyRecognizerFrontend.g:35:13: ^( TREE_MODULE_QUEUE ID )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MODULE_QUEUE, "TREE_MODULE_QUEUE")
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

    # $ANTLR end "module_queue"


    class stateless_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.stateless_return, self).__init__()

            self.tree = None





    # $ANTLR start "stateless"
    # grammar/ShyRecognizerFrontend.g:38:1: stateless : STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS18 = None
        ID19 = None
        NEWLINE20 = None
        INDENT21 = None
        NEWLINE22 = None
        DEDENT24 = None
        NEWLINE25 = None
        proc23 = None


        STATELESS18_tree = None
        ID19_tree = None
        NEWLINE20_tree = None
        INDENT21_tree = None
        NEWLINE22_tree = None
        DEDENT24_tree = None
        NEWLINE25_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:39:5: ( STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:39:9: STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                STATELESS18 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless237) 
                stream_STATELESS.add(STATELESS18)


                ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless239) 
                stream_ID.add(ID19)


                NEWLINE20 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless241) 
                stream_NEWLINE.add(NEWLINE20)


                # grammar/ShyRecognizerFrontend.g:39:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == INDENT) :
                    alt4 = 1
                if alt4 == 1:
                    # grammar/ShyRecognizerFrontend.g:39:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT21 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless245) 
                    stream_INDENT.add(INDENT21)


                    NEWLINE22 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless247) 
                    stream_NEWLINE.add(NEWLINE22)


                    # grammar/ShyRecognizerFrontend.g:39:47: ( proc )+
                    cnt3 = 0
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == PROC) :
                            alt3 = 1


                        if alt3 == 1:
                            # grammar/ShyRecognizerFrontend.g:39:47: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless249)
                            proc23 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc23.tree)



                        else:
                            if cnt3 >= 1:
                                break #loop3

                            eee = EarlyExitException(3, self.input)
                            raise eee

                        cnt3 += 1


                    DEDENT24 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless253) 
                    stream_DEDENT.add(DEDENT24)


                    NEWLINE25 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless255) 
                    stream_NEWLINE.add(NEWLINE25)





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
                # 40:9: -> ^( TREE_STATELESS ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:40:13: ^( TREE_STATELESS ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:40:34: ( proc )*
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
    # grammar/ShyRecognizerFrontend.g:43:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC26 = None
        ID27 = None
        NEWLINE28 = None
        PROC29 = None
        ID30 = None
        NEWLINE31 = None
        INDENT32 = None
        NEWLINE33 = None
        DEDENT37 = None
        NEWLINE38 = None
        proc_args34 = None

        proc_attrs35 = None

        proc_ops36 = None


        PROC26_tree = None
        ID27_tree = None
        NEWLINE28_tree = None
        PROC29_tree = None
        ID30_tree = None
        NEWLINE31_tree = None
        INDENT32_tree = None
        NEWLINE33_tree = None
        DEDENT37_tree = None
        NEWLINE38_tree = None
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
                # grammar/ShyRecognizerFrontend.g:44:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? ) )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == PROC) :
                    LA8_1 = self.input.LA(2)

                    if (LA8_1 == ID) :
                        LA8_2 = self.input.LA(3)

                        if (LA8_2 == NEWLINE) :
                            LA8_3 = self.input.LA(4)

                            if (LA8_3 == INDENT) :
                                alt8 = 2
                            elif (LA8_3 == DEDENT or LA8_3 == PROC) :
                                alt8 = 1
                            else:
                                nvae = NoViableAltException("", 8, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 8, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 8, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # grammar/ShyRecognizerFrontend.g:44:9: PROC ID NEWLINE
                    pass 
                    PROC26 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc301) 
                    stream_PROC.add(PROC26)


                    ID27 = self.match(self.input, ID, self.FOLLOW_ID_in_proc303) 
                    stream_ID.add(ID27)


                    NEWLINE28 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc305) 
                    stream_NEWLINE.add(NEWLINE28)


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
                    # 45:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:45:13: ^( TREE_PROC ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt8 == 2:
                    # grammar/ShyRecognizerFrontend.g:46:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE
                    pass 
                    PROC29 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc334) 
                    stream_PROC.add(PROC29)


                    ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_proc336) 
                    stream_ID.add(ID30)


                    NEWLINE31 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc338) 
                    stream_NEWLINE.add(NEWLINE31)


                    INDENT32 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc340) 
                    stream_INDENT.add(INDENT32)


                    NEWLINE33 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc342) 
                    stream_NEWLINE.add(NEWLINE33)


                    # grammar/ShyRecognizerFrontend.g:47:13: ( proc_args )?
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == ARGS) :
                        alt5 = 1
                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:47:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc356)
                        proc_args34 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args34.tree)





                    # grammar/ShyRecognizerFrontend.g:47:25: ( proc_attrs )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == VARS) :
                        alt6 = 1
                    if alt6 == 1:
                        # grammar/ShyRecognizerFrontend.g:47:25: proc_attrs
                        pass 
                        self._state.following.append(self.FOLLOW_proc_attrs_in_proc360)
                        proc_attrs35 = self.proc_attrs()

                        self._state.following.pop()
                        stream_proc_attrs.add(proc_attrs35.tree)





                    # grammar/ShyRecognizerFrontend.g:47:38: ( proc_ops )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == OPS) :
                        alt7 = 1
                    if alt7 == 1:
                        # grammar/ShyRecognizerFrontend.g:47:38: proc_ops
                        pass 
                        self._state.following.append(self.FOLLOW_proc_ops_in_proc364)
                        proc_ops36 = self.proc_ops()

                        self._state.following.pop()
                        stream_proc_ops.add(proc_ops36.tree)





                    DEDENT37 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc376) 
                    stream_DEDENT.add(DEDENT37)


                    NEWLINE38 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc378) 
                    stream_NEWLINE.add(NEWLINE38)


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
                    # 49:9: -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? )
                    # grammar/ShyRecognizerFrontend.g:49:13: ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:49:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:49:41: ( proc_attrs )?
                    if stream_proc_attrs.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_attrs.nextTree())


                    stream_proc_attrs.reset();

                    # grammar/ShyRecognizerFrontend.g:49:54: ( proc_ops )?
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
    # grammar/ShyRecognizerFrontend.g:52:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS39 = None
        attrs_hints40 = None


        ARGS39_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:53:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:53:9: ARGS attrs_hints
                pass 
                ARGS39 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args428) 
                stream_ARGS.add(ARGS39)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args430)
                attrs_hints40 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints40.tree)


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
                # 53:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:53:29: ^( TREE_PROC_ARGS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:56:1: proc_attrs : VARS attrs_hints -> ^( TREE_PROC_VARS attrs_hints ) ;
    def proc_attrs(self, ):
        retval = self.proc_attrs_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS41 = None
        attrs_hints42 = None


        VARS41_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:57:5: ( VARS attrs_hints -> ^( TREE_PROC_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:57:9: VARS attrs_hints
                pass 
                VARS41 = self.match(self.input, VARS, self.FOLLOW_VARS_in_proc_attrs459) 
                stream_VARS.add(VARS41)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_attrs461)
                attrs_hints42 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints42.tree)


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
                # 57:26: -> ^( TREE_PROC_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:57:29: ^( TREE_PROC_VARS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:60:1: proc_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
    def proc_ops(self, ):
        retval = self.proc_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS43 = None
        NEWLINE44 = None
        INDENT45 = None
        NEWLINE46 = None
        DEDENT48 = None
        NEWLINE49 = None
        statements47 = None


        OPS43_tree = None
        NEWLINE44_tree = None
        INDENT45_tree = None
        NEWLINE46_tree = None
        DEDENT48_tree = None
        NEWLINE49_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:61:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
                # grammar/ShyRecognizerFrontend.g:61:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                OPS43 = self.match(self.input, OPS, self.FOLLOW_OPS_in_proc_ops490) 
                stream_OPS.add(OPS43)


                NEWLINE44 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops492) 
                stream_NEWLINE.add(NEWLINE44)


                INDENT45 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc_ops494) 
                stream_INDENT.add(INDENT45)


                NEWLINE46 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops496) 
                stream_NEWLINE.add(NEWLINE46)


                self._state.following.append(self.FOLLOW_statements_in_proc_ops498)
                statements47 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements47.tree)


                DEDENT48 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc_ops500) 
                stream_DEDENT.add(DEDENT48)


                NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops502) 
                stream_NEWLINE.add(NEWLINE49)


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
                # 62:9: -> statements
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
    # grammar/ShyRecognizerFrontend.g:65:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE51 = None
        statement_call_single_line50 = None

        statement_call_multi_line52 = None

        statement_if53 = None

        statement_assign54 = None

        statement_with55 = None


        NEWLINE51_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:66:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_with )
                alt9 = 5
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:66:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement533)
                    statement_call_single_line50 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line50.tree)


                    NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement535) 
                    stream_NEWLINE.add(NEWLINE51)


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
                    # 67:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt9 == 2:
                    # grammar/ShyRecognizerFrontend.g:68:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement561)
                    statement_call_multi_line52 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line52.tree)



                elif alt9 == 3:
                    # grammar/ShyRecognizerFrontend.g:69:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement571)
                    statement_if53 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if53.tree)



                elif alt9 == 4:
                    # grammar/ShyRecognizerFrontend.g:70:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement581)
                    statement_assign54 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign54.tree)



                elif alt9 == 5:
                    # grammar/ShyRecognizerFrontend.g:71:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement591)
                    statement_with55 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with55.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:74:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement56 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:75:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:75:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:75:9: ( statement )+
                cnt10 = 0
                while True: #loop10
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if ((ID <= LA10_0 <= IF) or LA10_0 == WITH) :
                        alt10 = 1


                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:75:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements610)
                        statement56 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement56.tree)



                    else:
                        if cnt10 >= 1:
                            break #loop10

                        eee = EarlyExitException(10, self.input)
                        raise eee

                    cnt10 += 1


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
                # 76:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:76:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:76:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:79:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH57 = None
        ID58 = None
        NEWLINE59 = None
        INDENT60 = None
        NEWLINE61 = None
        DEDENT63 = None
        NEWLINE64 = None
        statements62 = None


        WITH57_tree = None
        ID58_tree = None
        NEWLINE59_tree = None
        INDENT60_tree = None
        NEWLINE61_tree = None
        DEDENT63_tree = None
        NEWLINE64_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:80:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:80:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH57 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with652) 
                stream_WITH.add(WITH57)


                ID58 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with654) 
                stream_ID.add(ID58)


                NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with656) 
                stream_NEWLINE.add(NEWLINE59)


                INDENT60 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with666) 
                stream_INDENT.add(INDENT60)


                NEWLINE61 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with668) 
                stream_NEWLINE.add(NEWLINE61)


                self._state.following.append(self.FOLLOW_statements_in_statement_with670)
                statements62 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements62.tree)


                DEDENT63 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with672) 
                stream_DEDENT.add(DEDENT63)


                NEWLINE64 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with674) 
                stream_NEWLINE.add(NEWLINE64)


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
                # 82:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:82:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:85:1: statement_assign : ID ARROW_LEFT arbitrary_value NEWLINE -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID ) ;
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID65 = None
        ARROW_LEFT66 = None
        NEWLINE68 = None
        arbitrary_value67 = None


        ID65_tree = None
        ARROW_LEFT66_tree = None
        NEWLINE68_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:86:5: ( ID ARROW_LEFT arbitrary_value NEWLINE -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID ) )
                # grammar/ShyRecognizerFrontend.g:86:9: ID ARROW_LEFT arbitrary_value NEWLINE
                pass 
                ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign714) 
                stream_ID.add(ID65)


                ARROW_LEFT66 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign716) 
                stream_ARROW_LEFT.add(ARROW_LEFT66)


                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign718)
                arbitrary_value67 = self.arbitrary_value()

                self._state.following.pop()
                stream_arbitrary_value.add(arbitrary_value67.tree)


                NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign720) 
                stream_NEWLINE.add(NEWLINE68)


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
                # 87:9: -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID )
                # grammar/ShyRecognizerFrontend.g:87:13: ^( TREE_STATEMENT_ASSIGN arbitrary_value ID )
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
    # grammar/ShyRecognizerFrontend.g:90:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head69 = None

        statement_elif70 = None

        statement_else71 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:91:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:91:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if760)
                statement_if_head69 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head69.tree)


                # grammar/ShyRecognizerFrontend.g:92:9: ( statement_elif )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == ELIF) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:92:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if770)
                        statement_elif70 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif70.tree)



                    else:
                        break #loop11


                # grammar/ShyRecognizerFrontend.g:93:9: ( statement_else )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == ELSE) :
                    alt12 = 1
                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:93:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if782)
                    statement_else71 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else71.tree)





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
                # 94:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:94:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:96:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:97:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:101:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF72 = None
        statement_elif_body73 = None


        IF72_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:102:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:102:9: IF statement_elif_body
                pass 
                IF72 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head890) 
                stream_IF.add(IF72)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head892)
                statement_elif_body73 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body73.tree)


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
                # 103:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:106:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF74 = None
        statement_elif_body75 = None


        ELIF74_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:107:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:107:9: ELIF statement_elif_body
                pass 
                ELIF74 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif924) 
                stream_ELIF.add(ELIF74)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif926)
                statement_elif_body75 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body75.tree)


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
                # 108:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:111:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE77 = None
        DO78 = None
        NEWLINE79 = None
        INDENT80 = None
        NEWLINE81 = None
        DEDENT83 = None
        NEWLINE84 = None
        condition76 = None

        statements82 = None


        NEWLINE77_tree = None
        DO78_tree = None
        NEWLINE79_tree = None
        INDENT80_tree = None
        NEWLINE81_tree = None
        DEDENT83_tree = None
        NEWLINE84_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:112:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:112:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body958)
                condition76 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition76.tree)


                # grammar/ShyRecognizerFrontend.g:112:19: ( NEWLINE )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == NEWLINE) :
                    alt13 = 1
                if alt13 == 1:
                    # grammar/ShyRecognizerFrontend.g:112:19: NEWLINE
                    pass 
                    NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body960) 
                    stream_NEWLINE.add(NEWLINE77)





                DO78 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body964) 
                stream_DO.add(DO78)


                NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body966) 
                stream_NEWLINE.add(NEWLINE79)


                INDENT80 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body980) 
                stream_INDENT.add(INDENT80)


                NEWLINE81 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body982) 
                stream_NEWLINE.add(NEWLINE81)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body984)
                statements82 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements82.tree)


                DEDENT83 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body986) 
                stream_DEDENT.add(DEDENT83)


                NEWLINE84 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body988) 
                stream_NEWLINE.add(NEWLINE84)


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
                # 114:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:114:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:117:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE85 = None
        NEWLINE86 = None
        INDENT87 = None
        NEWLINE88 = None
        DEDENT90 = None
        NEWLINE91 = None
        statements89 = None


        ELSE85_tree = None
        NEWLINE86_tree = None
        INDENT87_tree = None
        NEWLINE88_tree = None
        DEDENT90_tree = None
        NEWLINE91_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:118:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:118:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE85 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1028) 
                stream_ELSE.add(ELSE85)


                NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1030) 
                stream_NEWLINE.add(NEWLINE86)


                INDENT87 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1044) 
                stream_INDENT.add(INDENT87)


                NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1046) 
                stream_NEWLINE.add(NEWLINE88)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1048)
                statements89 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements89.tree)


                DEDENT90 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1050) 
                stream_DEDENT.add(DEDENT90)


                NEWLINE91 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1052) 
                stream_NEWLINE.add(NEWLINE91)


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
                # 120:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:120:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:123:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY93 = None
        ALL95 = None
        condition_call92 = None

        condition_calls94 = None

        condition_calls96 = None


        ANY93_tree = None
        ALL95_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:124:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt14 = 3
                LA14 = self.input.LA(1)
                if LA14 == ID:
                    alt14 = 1
                elif LA14 == ANY:
                    alt14 = 2
                elif LA14 == ALL:
                    alt14 = 3
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:124:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1090)
                    condition_call92 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call92.tree)


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
                    # 125:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:125:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt14 == 2:
                    # grammar/ShyRecognizerFrontend.g:126:9: ANY condition_calls
                    pass 
                    ANY93 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1119) 
                    stream_ANY.add(ANY93)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1121)
                    condition_calls94 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls94.tree)


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
                    # 127:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:127:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt14 == 3:
                    # grammar/ShyRecognizerFrontend.g:128:9: ALL condition_calls
                    pass 
                    ALL95 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1150) 
                    stream_ALL.add(ALL95)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1152)
                    condition_calls96 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls96.tree)


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
                    # 129:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:129:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:132:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE98 = None
        INDENT99 = None
        NEWLINE100 = None
        DEDENT102 = None
        NEWLINE103 = None
        condition_call97 = None

        condition_call_line101 = None


        NEWLINE98_tree = None
        INDENT99_tree = None
        NEWLINE100_tree = None
        DEDENT102_tree = None
        NEWLINE103_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:133:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == ID) :
                    alt16 = 1
                elif (LA16_0 == NEWLINE) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:133:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1190)
                    condition_call97 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call97.tree)



                elif alt16 == 2:
                    # grammar/ShyRecognizerFrontend.g:134:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE98 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1200) 
                    stream_NEWLINE.add(NEWLINE98)


                    INDENT99 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1202) 
                    stream_INDENT.add(INDENT99)


                    NEWLINE100 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1204) 
                    stream_NEWLINE.add(NEWLINE100)


                    # grammar/ShyRecognizerFrontend.g:134:32: ( condition_call_line )+
                    cnt15 = 0
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == ID) :
                            alt15 = 1


                        if alt15 == 1:
                            # grammar/ShyRecognizerFrontend.g:134:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1206)
                            condition_call_line101 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line101.tree)



                        else:
                            if cnt15 >= 1:
                                break #loop15

                            eee = EarlyExitException(15, self.input)
                            raise eee

                        cnt15 += 1


                    DEDENT102 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1210) 
                    stream_DEDENT.add(DEDENT102)


                    NEWLINE103 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1212) 
                    stream_NEWLINE.add(NEWLINE103)


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
                    # 135:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:135:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:138:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line104 = None

        statement_call_multi_line105 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:139:5: ( statement_call_single_line | statement_call_multi_line )
                alt17 = 2
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:139:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1246)
                    statement_call_single_line104 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line104.tree)



                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:140:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1256)
                    statement_call_multi_line105 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line105.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:143:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE107 = None
        statement_call_single_line106 = None

        statement_call_multi_line108 = None


        NEWLINE107_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:144:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt18 = 2
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:144:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1275)
                    statement_call_single_line106 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line106.tree)


                    NEWLINE107 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1277) 
                    stream_NEWLINE.add(NEWLINE107)


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
                    # 145:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:146:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1303)
                    statement_call_multi_line108 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line108.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:149:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID109 = None
        statement_call_args110 = None


        ID109_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:150:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:150:9: ID ( statement_call_args )?
                pass 
                ID109 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1322) 
                stream_ID.add(ID109)


                # grammar/ShyRecognizerFrontend.g:150:12: ( statement_call_args )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                    alt19 = 1
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:150:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1324)
                    statement_call_args110 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args110.tree)





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
                # 151:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:151:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:151:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:154:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID111 = None
        NEWLINE113 = None
        INDENT114 = None
        NEWLINE115 = None
        NEWLINE117 = None
        DEDENT118 = None
        NEWLINE119 = None
        statement_call_args112 = None

        statement_call_args116 = None


        ID111_tree = None
        NEWLINE113_tree = None
        INDENT114_tree = None
        NEWLINE115_tree = None
        NEWLINE117_tree = None
        DEDENT118_tree = None
        NEWLINE119_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:155:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:155:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID111 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1368) 
                stream_ID.add(ID111)


                # grammar/ShyRecognizerFrontend.g:155:12: ( statement_call_args )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER) :
                    alt20 = 1
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:155:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1370)
                    statement_call_args112 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args112.tree)





                NEWLINE113 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1374) 
                stream_NEWLINE.add(NEWLINE113)


                INDENT114 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1384) 
                stream_INDENT.add(INDENT114)


                NEWLINE115 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1386) 
                stream_NEWLINE.add(NEWLINE115)


                # grammar/ShyRecognizerFrontend.g:156:24: ( statement_call_args NEWLINE )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerFrontend.g:156:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1390)
                        statement_call_args116 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args116.tree)


                        NEWLINE117 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1392) 
                        stream_NEWLINE.add(NEWLINE117)



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1


                DEDENT118 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1398) 
                stream_DEDENT.add(DEDENT118)


                NEWLINE119 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1400) 
                stream_NEWLINE.add(NEWLINE119)


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
                # 157:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:157:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:157:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:160:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value120 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:160:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:160:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:160:23: ( arbitrary_value )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerFrontend.g:160:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1436)
                        arbitrary_value120 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value120.tree)



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

    # $ANTLR end "statement_call_args"


    class arbitrary_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.arbitrary_value_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerFrontend.g:162:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID121 = None
        EXPRESSION122 = None
        num_whole123 = None

        num_fract124 = None


        ID121_tree = None
        EXPRESSION122_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:163:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt23 = 4
                LA23 = self.input.LA(1)
                if LA23 == ID:
                    alt23 = 1
                elif LA23 == EXPRESSION:
                    alt23 = 2
                elif LA23 == MINUS:
                    LA23_3 = self.input.LA(2)

                    if (LA23_3 == NUMBER) :
                        LA23_4 = self.input.LA(3)

                        if (LA23_4 == DIVIDE) :
                            alt23 = 4
                        elif (LA23_4 == DO or (EXPRESSION <= LA23_4 <= ID) or LA23_4 == MINUS or (NEWLINE <= LA23_4 <= NUMBER)) :
                            alt23 = 3
                        else:
                            nvae = NoViableAltException("", 23, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 23, 3, self.input)

                        raise nvae


                elif LA23 == NUMBER:
                    LA23_4 = self.input.LA(2)

                    if (LA23_4 == DIVIDE) :
                        alt23 = 4
                    elif (LA23_4 == DO or (EXPRESSION <= LA23_4 <= ID) or LA23_4 == MINUS or (NEWLINE <= LA23_4 <= NUMBER)) :
                        alt23 = 3
                    else:
                        nvae = NoViableAltException("", 23, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae


                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:163:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1453)
                    ID121_tree = self._adaptor.createWithPayload(ID121)
                    self._adaptor.addChild(root_0, ID121_tree)




                elif alt23 == 2:
                    # grammar/ShyRecognizerFrontend.g:164:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION122 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1463)
                    EXPRESSION122_tree = self._adaptor.createWithPayload(EXPRESSION122)
                    self._adaptor.addChild(root_0, EXPRESSION122_tree)




                elif alt23 == 3:
                    # grammar/ShyRecognizerFrontend.g:165:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1473)
                    num_whole123 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole123.tree)



                elif alt23 == 4:
                    # grammar/ShyRecognizerFrontend.g:166:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1483)
                    num_fract124 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract124.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:169:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS125 = None
        ID126 = None
        NEWLINE127 = None
        INDENT128 = None
        NEWLINE129 = None
        DEDENT131 = None
        NEWLINE132 = None
        consts_items130 = None


        CONSTS125_tree = None
        ID126_tree = None
        NEWLINE127_tree = None
        INDENT128_tree = None
        NEWLINE129_tree = None
        DEDENT131_tree = None
        NEWLINE132_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:170:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:170:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS125 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1502) 
                stream_CONSTS.add(CONSTS125)


                ID126 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1504) 
                stream_ID.add(ID126)


                NEWLINE127 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1506) 
                stream_NEWLINE.add(NEWLINE127)


                INDENT128 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1516) 
                stream_INDENT.add(INDENT128)


                NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1518) 
                stream_NEWLINE.add(NEWLINE129)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1520)
                consts_items130 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items130.tree)


                DEDENT131 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1522) 
                stream_DEDENT.add(DEDENT131)


                NEWLINE132 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1524) 
                stream_NEWLINE.add(NEWLINE132)


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
                # 172:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:172:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:174:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item133 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:174:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:174:16: ( consts_item )+
                cnt24 = 0
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ID) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerFrontend.g:174:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1556)
                        consts_item133 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item133.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:175:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID134 = None
        NEWLINE136 = None
        ID137 = None
        NEWLINE139 = None
        ID140 = None
        EXPRESSION141 = None
        NEWLINE142 = None
        num_whole135 = None

        num_fract138 = None


        ID134_tree = None
        NEWLINE136_tree = None
        ID137_tree = None
        NEWLINE139_tree = None
        ID140_tree = None
        EXPRESSION141_tree = None
        NEWLINE142_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:176:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt25 = 3
                LA25_0 = self.input.LA(1)

                if (LA25_0 == ID) :
                    LA25 = self.input.LA(2)
                    if LA25 == EXPRESSION:
                        alt25 = 3
                    elif LA25 == MINUS:
                        LA25_3 = self.input.LA(3)

                        if (LA25_3 == NUMBER) :
                            LA25_4 = self.input.LA(4)

                            if (LA25_4 == DIVIDE) :
                                alt25 = 2
                            elif (LA25_4 == NEWLINE) :
                                alt25 = 1
                            else:
                                nvae = NoViableAltException("", 25, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 25, 3, self.input)

                            raise nvae


                    elif LA25 == NUMBER:
                        LA25_4 = self.input.LA(3)

                        if (LA25_4 == DIVIDE) :
                            alt25 = 2
                        elif (LA25_4 == NEWLINE) :
                            alt25 = 1
                        else:
                            nvae = NoViableAltException("", 25, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # grammar/ShyRecognizerFrontend.g:176:9: ID num_whole NEWLINE
                    pass 
                    ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1572) 
                    stream_ID.add(ID134)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1574)
                    num_whole135 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole135.tree)


                    NEWLINE136 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1576) 
                    stream_NEWLINE.add(NEWLINE136)


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
                    # 176:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:176:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt25 == 2:
                    # grammar/ShyRecognizerFrontend.g:177:9: ID num_fract NEWLINE
                    pass 
                    ID137 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1598) 
                    stream_ID.add(ID137)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1600)
                    num_fract138 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract138.tree)


                    NEWLINE139 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1602) 
                    stream_NEWLINE.add(NEWLINE139)


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
                    # 177:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:177:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt25 == 3:
                    # grammar/ShyRecognizerFrontend.g:178:9: ID EXPRESSION NEWLINE
                    pass 
                    ID140 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1624) 
                    stream_ID.add(ID140)


                    EXPRESSION141 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1626) 
                    stream_EXPRESSION.add(EXPRESSION141)


                    NEWLINE142 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1628) 
                    stream_NEWLINE.add(NEWLINE142)


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
                    # 178:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:178:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:181:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES143 = None
        ID144 = None
        NEWLINE145 = None
        INDENT146 = None
        NEWLINE147 = None
        DEDENT149 = None
        NEWLINE150 = None
        types_item148 = None


        TYPES143_tree = None
        ID144_tree = None
        NEWLINE145_tree = None
        INDENT146_tree = None
        NEWLINE147_tree = None
        DEDENT149_tree = None
        NEWLINE150_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:182:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:182:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES143 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1659) 
                stream_TYPES.add(TYPES143)


                ID144 = self.match(self.input, ID, self.FOLLOW_ID_in_types1661) 
                stream_ID.add(ID144)


                NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1663) 
                stream_NEWLINE.add(NEWLINE145)


                INDENT146 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1673) 
                stream_INDENT.add(INDENT146)


                NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1675) 
                stream_NEWLINE.add(NEWLINE147)


                # grammar/ShyRecognizerFrontend.g:183:24: ( types_item )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == ID) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerFrontend.g:183:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types1677)
                        types_item148 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item148.tree)



                    else:
                        if cnt26 >= 1:
                            break #loop26

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1


                DEDENT149 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1681) 
                stream_DEDENT.add(DEDENT149)


                NEWLINE150 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1683) 
                stream_NEWLINE.add(NEWLINE150)


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
                # 184:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:184:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:184:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:186:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID151 = None
        attrs_hints152 = None


        ID151_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:186:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:186:14: ID attrs_hints
                pass 
                ID151 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1717) 
                stream_ID.add(ID151)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item1719)
                attrs_hints152 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints152.tree)


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
                # 186:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:186:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:188:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES153 = None
        ID154 = None
        NEWLINE155 = None
        INDENT156 = None
        NEWLINE157 = None
        DEDENT159 = None
        NEWLINE160 = None
        messages_item158 = None


        MESSAGES153_tree = None
        ID154_tree = None
        NEWLINE155_tree = None
        INDENT156_tree = None
        NEWLINE157_tree = None
        DEDENT159_tree = None
        NEWLINE160_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:189:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:189:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES153 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages1746) 
                stream_MESSAGES.add(MESSAGES153)


                ID154 = self.match(self.input, ID, self.FOLLOW_ID_in_messages1748) 
                stream_ID.add(ID154)


                NEWLINE155 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1750) 
                stream_NEWLINE.add(NEWLINE155)


                INDENT156 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages1760) 
                stream_INDENT.add(INDENT156)


                NEWLINE157 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1762) 
                stream_NEWLINE.add(NEWLINE157)


                # grammar/ShyRecognizerFrontend.g:190:24: ( messages_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == ID) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerFrontend.g:190:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages1764)
                        messages_item158 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item158.tree)



                    else:
                        if cnt27 >= 1:
                            break #loop27

                        eee = EarlyExitException(27, self.input)
                        raise eee

                    cnt27 += 1


                DEDENT159 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages1768) 
                stream_DEDENT.add(DEDENT159)


                NEWLINE160 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1770) 
                stream_NEWLINE.add(NEWLINE160)


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
                # 191:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:191:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:191:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:193:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID161 = None
        attrs_hints162 = None


        ID161_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:193:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:193:17: ID attrs_hints
                pass 
                ID161 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item1804) 
                stream_ID.add(ID161)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item1806)
                attrs_hints162 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints162.tree)


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
                # 193:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:193:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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


    class vars_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.vars_return, self).__init__()

            self.tree = None





    # $ANTLR start "vars"
    # grammar/ShyRecognizerFrontend.g:195:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS163 = None
        ID164 = None
        attrs_hints165 = None


        VARS163_tree = None
        ID164_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:196:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:196:9: VARS ID attrs_hints
                pass 
                VARS163 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars1833) 
                stream_VARS.add(VARS163)


                ID164 = self.match(self.input, ID, self.FOLLOW_ID_in_vars1835) 
                stream_ID.add(ID164)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars1837)
                attrs_hints165 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints165.tree)


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
                # 197:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:197:12: ^( TREE_VARS ID attrs_hints )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_VARS, "TREE_VARS")
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

    # $ANTLR end "vars"


    class attrs_hints_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.attrs_hints_return, self).__init__()

            self.tree = None





    # $ANTLR start "attrs_hints"
    # grammar/ShyRecognizerFrontend.g:200:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE167 = None
        NEWLINE168 = None
        INDENT169 = None
        NEWLINE170 = None
        NEWLINE172 = None
        DEDENT173 = None
        NEWLINE174 = None
        NEWLINE176 = None
        INDENT177 = None
        NEWLINE178 = None
        NEWLINE180 = None
        DEDENT181 = None
        NEWLINE182 = None
        attr_hint166 = None

        attr_hint171 = None

        attr_hint175 = None

        attr_hint179 = None


        NEWLINE167_tree = None
        NEWLINE168_tree = None
        INDENT169_tree = None
        NEWLINE170_tree = None
        NEWLINE172_tree = None
        DEDENT173_tree = None
        NEWLINE174_tree = None
        NEWLINE176_tree = None
        INDENT177_tree = None
        NEWLINE178_tree = None
        NEWLINE180_tree = None
        DEDENT181_tree = None
        NEWLINE182_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:201:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt30 = 3
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:201:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1876)
                    attr_hint166 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint166.tree)


                    NEWLINE167 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1878) 
                    stream_NEWLINE.add(NEWLINE167)


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
                    # 202:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt30 == 2:
                    # grammar/ShyRecognizerFrontend.g:203:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE168 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1902) 
                    stream_NEWLINE.add(NEWLINE168)


                    # grammar/ShyRecognizerFrontend.g:204:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:204:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT169 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints1914) 
                    stream_INDENT.add(INDENT169)


                    NEWLINE170 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1916) 
                    stream_NEWLINE.add(NEWLINE170)


                    # grammar/ShyRecognizerFrontend.g:204:26: ( attr_hint NEWLINE )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == CURLY_OPEN or LA28_0 == ID) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:204:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1920)
                            attr_hint171 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint171.tree)


                            NEWLINE172 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1922) 
                            stream_NEWLINE.add(NEWLINE172)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    DEDENT173 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints1928) 
                    stream_DEDENT.add(DEDENT173)


                    NEWLINE174 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1930) 
                    stream_NEWLINE.add(NEWLINE174)





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
                    # 205:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:205:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt30 == 3:
                    # grammar/ShyRecognizerFrontend.g:206:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1958)
                    attr_hint175 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint175.tree)


                    NEWLINE176 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1960) 
                    stream_NEWLINE.add(NEWLINE176)


                    # grammar/ShyRecognizerFrontend.g:207:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:207:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT177 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints1972) 
                    stream_INDENT.add(INDENT177)


                    NEWLINE178 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1974) 
                    stream_NEWLINE.add(NEWLINE178)


                    # grammar/ShyRecognizerFrontend.g:207:26: ( attr_hint NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == CURLY_OPEN or LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:207:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1978)
                            attr_hint179 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint179.tree)


                            NEWLINE180 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1980) 
                            stream_NEWLINE.add(NEWLINE180)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT181 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints1986) 
                    stream_DEDENT.add(DEDENT181)


                    NEWLINE182 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1988) 
                    stream_NEWLINE.add(NEWLINE182)





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
                    # 208:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:208:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:210:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID183 = None
        ID185 = None
        NEWLINE187 = None
        INDENT188 = None
        NEWLINE189 = None
        ID190 = None
        NEWLINE191 = None
        DEDENT192 = None
        hint184 = None

        hint186 = None


        ID183_tree = None
        ID185_tree = None
        NEWLINE187_tree = None
        INDENT188_tree = None
        NEWLINE189_tree = None
        ID190_tree = None
        NEWLINE191_tree = None
        DEDENT192_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:211:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt35 = 3
                alt35 = self.dfa35.predict(self.input)
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:211:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:211:9: ( ID )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == ID) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:211:9: ID
                            pass 
                            ID183 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2025) 
                            stream_ID.add(ID183)



                        else:
                            if cnt31 >= 1:
                                break #loop31

                            eee = EarlyExitException(31, self.input)
                            raise eee

                        cnt31 += 1


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
                    # 212:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:212:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:212:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:212:45: ^( TREE_ATTR ID )
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




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:213:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2066)
                    hint184 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint184.tree)


                    # grammar/ShyRecognizerFrontend.g:213:14: ( ID )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:213:14: ID
                            pass 
                            ID185 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2068) 
                            stream_ID.add(ID185)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


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
                    # 214:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:214:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:214:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:214:35: ^( TREE_ATTR ID )
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




                elif alt35 == 3:
                    # grammar/ShyRecognizerFrontend.g:215:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2108)
                    hint186 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint186.tree)


                    NEWLINE187 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2110) 
                    stream_NEWLINE.add(NEWLINE187)


                    INDENT188 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2112) 
                    stream_INDENT.add(INDENT188)


                    NEWLINE189 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2114) 
                    stream_NEWLINE.add(NEWLINE189)


                    # grammar/ShyRecognizerFrontend.g:215:37: ( ( ID )+ NEWLINE )+
                    cnt34 = 0
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 == ID) :
                            alt34 = 1


                        if alt34 == 1:
                            # grammar/ShyRecognizerFrontend.g:215:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:215:39: ( ID )+
                            cnt33 = 0
                            while True: #loop33
                                alt33 = 2
                                LA33_0 = self.input.LA(1)

                                if (LA33_0 == ID) :
                                    alt33 = 1


                                if alt33 == 1:
                                    # grammar/ShyRecognizerFrontend.g:215:39: ID
                                    pass 
                                    ID190 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2118) 
                                    stream_ID.add(ID190)



                                else:
                                    if cnt33 >= 1:
                                        break #loop33

                                    eee = EarlyExitException(33, self.input)
                                    raise eee

                                cnt33 += 1


                            NEWLINE191 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2122) 
                            stream_NEWLINE.add(NEWLINE191)



                        else:
                            if cnt34 >= 1:
                                break #loop34

                            eee = EarlyExitException(34, self.input)
                            raise eee

                        cnt34 += 1


                    DEDENT192 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2128) 
                    stream_DEDENT.add(DEDENT192)


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
                    # 216:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:216:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:216:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:216:35: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:219:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN193 = None
        ID194 = None
        CURLY_CLOSE195 = None
        CURLY_OPEN196 = None
        ID197 = None
        CURLY_CLOSE199 = None
        hint_arg198 = None


        CURLY_OPEN193_tree = None
        ID194_tree = None
        CURLY_CLOSE195_tree = None
        CURLY_OPEN196_tree = None
        ID197_tree = None
        CURLY_CLOSE199_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:220:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:220:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN193 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2175) 
                    stream_CURLY_OPEN.add(CURLY_OPEN193)


                    ID194 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2177) 
                    stream_ID.add(ID194)


                    CURLY_CLOSE195 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2179) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE195)


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
                    # 220:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:220:38: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:221:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN196 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2199) 
                    stream_CURLY_OPEN.add(CURLY_OPEN196)


                    ID197 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2201) 
                    stream_ID.add(ID197)


                    # grammar/ShyRecognizerFrontend.g:221:23: ( hint_arg )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID or LA36_0 == UNDERSCORE) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:221:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2203)
                            hint_arg198 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg198.tree)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


                    CURLY_CLOSE199 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2207) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE199)


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
                    # 221:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:221:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:221:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:223:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set200 = None

        set200_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:223:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set200 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set200))

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
    # grammar/ShyRecognizerFrontend.g:225:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS201 = None
        NUMBER202 = None

        MINUS201_tree = None
        NUMBER202_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:225:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:225:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:225:13: ( MINUS )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == MINUS) :
                    alt38 = 1
                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:225:13: MINUS
                    pass 
                    MINUS201 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2246)
                    MINUS201_tree = self._adaptor.createWithPayload(MINUS201)
                    self._adaptor.addChild(root_0, MINUS201_tree)






                NUMBER202 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2250)
                NUMBER202_tree = self._adaptor.createWithPayload(NUMBER202)
                self._adaptor.addChild(root_0, NUMBER202_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:226:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS203 = None
        NUMBER204 = None
        DIVIDE205 = None
        NUMBER206 = None

        MINUS203_tree = None
        NUMBER204_tree = None
        DIVIDE205_tree = None
        NUMBER206_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:226:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:226:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:226:13: ( MINUS )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == MINUS) :
                    alt39 = 1
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:226:13: MINUS
                    pass 
                    MINUS203 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2258)
                    MINUS203_tree = self._adaptor.createWithPayload(MINUS203)
                    self._adaptor.addChild(root_0, MINUS203_tree)






                NUMBER204 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2262)
                NUMBER204_tree = self._adaptor.createWithPayload(NUMBER204)
                self._adaptor.addChild(root_0, NUMBER204_tree)



                DIVIDE205 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2264)
                DIVIDE205_tree = self._adaptor.createWithPayload(DIVIDE205)
                self._adaptor.addChild(root_0, DIVIDE205_tree)



                NUMBER206 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2266)
                NUMBER206_tree = self._adaptor.createWithPayload(NUMBER206)
                self._adaptor.addChild(root_0, NUMBER206_tree)





                retval.stop = self.input.LT(-1)


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
        u"\16\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\23\1\7\3\uffff\2\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA9_max = DFA.unpack(
        u"\1\113\1\33\3\uffff\4\33\1\113\1\33\2\uffff\1\33"
        )

    DFA9_accept = DFA.unpack(
        u"\2\uffff\1\3\1\5\1\4\6\uffff\1\2\1\1\1\uffff"
        )

    DFA9_special = DFA.unpack(
        u"\16\uffff"
        )


    DFA9_transition = [
        DFA.unpack(u"\1\1\1\2\66\uffff\1\3"),
        DFA.unpack(u"\1\4\12\uffff\1\6\1\5\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u"\1\12\3\uffff\1\6\1\5\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u"\1\14\5\uffff\2\14\1\13\65\uffff\1\14"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\5\3\uffff\1\7\2\uffff\1\11\1\10")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\23\3\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA17_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\uffff\1\33\1\uffff\1\33"
        )

    DFA17_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA17_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA17_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5"),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\10\1\7\2\uffff\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1"
        u"\5"),
        DFA.unpack(u"\1\7\5\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\2\uffff\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\23\3\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA18_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\33\2\uffff\1\33"
        )

    DFA18_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA18_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA18_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\7\3\uffff\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5"),
        DFA.unpack(u"\1\11\5\uffff\1\11\1\uffff\1\10"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\4\2\uffff\1\6\1\5")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA30_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\111\1\110\2\uffff\1\32\1\110\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA30_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA30_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA30_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1\6\uffff\1\3"),
        DFA.unpack(u"\1\1\6\uffff\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\6\5\uffff\1\6\1\uffff\1\7\1\6\1\uffff"
        u"\1\6\3\uffff\1\6\5\uffff\1\6\44\uffff\1\6\1\uffff\1\6"),
        DFA.unpack(u"\1\10\7\uffff\1\11\64\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\14\7\uffff\1\11\64\uffff\1\11"),
        DFA.unpack(u"\1\12\6\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\17\6\uffff\1\20"),
        DFA.unpack(u"\1\21\5\uffff\1\17"),
        DFA.unpack(u"\1\4")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


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
        u"\1\23\1\uffff\1\23\1\110\1\32\1\110\2\uffff\1\32"
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
        DFA.unpack(u"\1\4\7\uffff\1\5\64\uffff\1\5"),
        DFA.unpack(u"\1\6\6\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\64\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\6\uffff\1\7")
    ]

    # class definition for DFA #35

    class DFA35(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 22, 24, 34, 71, 73])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 22, 24, 34, 71, 73])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 22, 24, 34, 71, 73])
    FOLLOW_types_in_start94 = frozenset([1, 9, 22, 24, 34, 71, 73])
    FOLLOW_messages_in_start98 = frozenset([1, 9, 22, 24, 34, 71, 73])
    FOLLOW_vars_in_start102 = frozenset([1, 9, 22, 24, 34, 71, 73])
    FOLLOW_MODULE_in_module121 = frozenset([19])
    FOLLOW_ID_in_module123 = frozenset([26])
    FOLLOW_NEWLINE_in_module125 = frozenset([21])
    FOLLOW_INDENT_in_module127 = frozenset([26])
    FOLLOW_NEWLINE_in_module129 = frozenset([13, 25])
    FOLLOW_module_queue_in_module139 = frozenset([13])
    FOLLOW_DEDENT_in_module151 = frozenset([26])
    FOLLOW_NEWLINE_in_module153 = frozenset([1])
    FOLLOW_MODULE_QUEUE_in_module_queue195 = frozenset([19])
    FOLLOW_ID_in_module_queue197 = frozenset([26])
    FOLLOW_NEWLINE_in_module_queue199 = frozenset([1])
    FOLLOW_STATELESS_in_stateless237 = frozenset([19])
    FOLLOW_ID_in_stateless239 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless241 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless245 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless247 = frozenset([30])
    FOLLOW_proc_in_stateless249 = frozenset([13, 30])
    FOLLOW_DEDENT_in_stateless253 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless255 = frozenset([1])
    FOLLOW_PROC_in_proc301 = frozenset([19])
    FOLLOW_ID_in_proc303 = frozenset([26])
    FOLLOW_NEWLINE_in_proc305 = frozenset([1])
    FOLLOW_PROC_in_proc334 = frozenset([19])
    FOLLOW_ID_in_proc336 = frozenset([26])
    FOLLOW_NEWLINE_in_proc338 = frozenset([21])
    FOLLOW_INDENT_in_proc340 = frozenset([26])
    FOLLOW_NEWLINE_in_proc342 = frozenset([6, 13, 28, 73])
    FOLLOW_proc_args_in_proc356 = frozenset([13, 28, 73])
    FOLLOW_proc_attrs_in_proc360 = frozenset([13, 28])
    FOLLOW_proc_ops_in_proc364 = frozenset([13])
    FOLLOW_DEDENT_in_proc376 = frozenset([26])
    FOLLOW_NEWLINE_in_proc378 = frozenset([1])
    FOLLOW_ARGS_in_proc_args428 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args430 = frozenset([1])
    FOLLOW_VARS_in_proc_attrs459 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_attrs461 = frozenset([1])
    FOLLOW_OPS_in_proc_ops490 = frozenset([26])
    FOLLOW_NEWLINE_in_proc_ops492 = frozenset([21])
    FOLLOW_INDENT_in_proc_ops494 = frozenset([26])
    FOLLOW_NEWLINE_in_proc_ops496 = frozenset([19, 20, 75])
    FOLLOW_statements_in_proc_ops498 = frozenset([13])
    FOLLOW_DEDENT_in_proc_ops500 = frozenset([26])
    FOLLOW_NEWLINE_in_proc_ops502 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement533 = frozenset([26])
    FOLLOW_NEWLINE_in_statement535 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement561 = frozenset([1])
    FOLLOW_statement_if_in_statement571 = frozenset([1])
    FOLLOW_statement_assign_in_statement581 = frozenset([1])
    FOLLOW_statement_with_in_statement591 = frozenset([1])
    FOLLOW_statement_in_statements610 = frozenset([1, 19, 20, 75])
    FOLLOW_WITH_in_statement_with652 = frozenset([19])
    FOLLOW_ID_in_statement_with654 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with656 = frozenset([21])
    FOLLOW_INDENT_in_statement_with666 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with668 = frozenset([19, 20, 75])
    FOLLOW_statements_in_statement_with670 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with672 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with674 = frozenset([1])
    FOLLOW_ID_in_statement_assign714 = frozenset([7])
    FOLLOW_ARROW_LEFT_in_statement_assign716 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign718 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign720 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if760 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if770 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if782 = frozenset([1])
    FOLLOW_IF_in_statement_if_head890 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head892 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif924 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif926 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body958 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body960 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body964 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body966 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body980 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body982 = frozenset([19, 20, 75])
    FOLLOW_statements_in_statement_elif_body984 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body986 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body988 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1028 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1030 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1044 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1046 = frozenset([19, 20, 75])
    FOLLOW_statements_in_statement_else1048 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1050 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1052 = frozenset([1])
    FOLLOW_condition_call_in_condition1090 = frozenset([1])
    FOLLOW_ANY_in_condition1119 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1121 = frozenset([1])
    FOLLOW_ALL_in_condition1150 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1152 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1190 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1200 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1202 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1204 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1206 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1210 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1212 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1246 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1256 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1275 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line1277 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1303 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1322 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line1324 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1368 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1370 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1374 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1384 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1386 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1390 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1392 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line1398 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1400 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args1436 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value1453 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1463 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1473 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1483 = frozenset([1])
    FOLLOW_CONSTS_in_consts1502 = frozenset([19])
    FOLLOW_ID_in_consts1504 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1506 = frozenset([21])
    FOLLOW_INDENT_in_consts1516 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1518 = frozenset([19])
    FOLLOW_consts_items_in_consts1520 = frozenset([13])
    FOLLOW_DEDENT_in_consts1522 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1524 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1556 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1572 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item1574 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1576 = frozenset([1])
    FOLLOW_ID_in_consts_item1598 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item1600 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1602 = frozenset([1])
    FOLLOW_ID_in_consts_item1624 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1626 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1628 = frozenset([1])
    FOLLOW_TYPES_in_types1659 = frozenset([19])
    FOLLOW_ID_in_types1661 = frozenset([26])
    FOLLOW_NEWLINE_in_types1663 = frozenset([21])
    FOLLOW_INDENT_in_types1673 = frozenset([26])
    FOLLOW_NEWLINE_in_types1675 = frozenset([19])
    FOLLOW_types_item_in_types1677 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types1681 = frozenset([26])
    FOLLOW_NEWLINE_in_types1683 = frozenset([1])
    FOLLOW_ID_in_types_item1717 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item1719 = frozenset([1])
    FOLLOW_MESSAGES_in_messages1746 = frozenset([19])
    FOLLOW_ID_in_messages1748 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1750 = frozenset([21])
    FOLLOW_INDENT_in_messages1760 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1762 = frozenset([19])
    FOLLOW_messages_item_in_messages1764 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages1768 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1770 = frozenset([1])
    FOLLOW_ID_in_messages_item1804 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item1806 = frozenset([1])
    FOLLOW_VARS_in_vars1833 = frozenset([19])
    FOLLOW_ID_in_vars1835 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars1837 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints1876 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1878 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints1902 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints1914 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1916 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints1920 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1922 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints1928 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1930 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints1958 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1960 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints1972 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1974 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints1978 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1980 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints1986 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1988 = frozenset([1])
    FOLLOW_ID_in_attr_hint2025 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2066 = frozenset([19])
    FOLLOW_ID_in_attr_hint2068 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2108 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2110 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2112 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2114 = frozenset([19])
    FOLLOW_ID_in_attr_hint2118 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2122 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2128 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2175 = frozenset([19])
    FOLLOW_ID_in_hint2177 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2179 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2199 = frozenset([19])
    FOLLOW_ID_in_hint2201 = frozenset([19, 72])
    FOLLOW_hint_arg_in_hint2203 = frozenset([11, 19, 72])
    FOLLOW_CURLY_CLOSE_in_hint2207 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2246 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2250 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2258 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2262 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2264 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2266 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
