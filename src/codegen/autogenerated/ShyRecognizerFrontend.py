# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-02 18:58:02

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
RECEIVE=31
REPLACE=32
REPLY=33
REQUEST=34
STATELESS=35
STRING=36
TREE_ARBITRARY_TOKEN=37
TREE_ATTR=38
TREE_ATTRS_HINTS=39
TREE_ATTR_HINT=40
TREE_CONDITION_ALL=41
TREE_CONDITION_ANY=42
TREE_CONSTS=43
TREE_COPY=44
TREE_COPY_PASTE=45
TREE_EXPRESSION=46
TREE_HINT=47
TREE_HINT_NONE=48
TREE_LOCAL_VARS=49
TREE_MESSAGES=50
TREE_MESSAGES_ITEM=51
TREE_MODULE=52
TREE_MODULE_QUEUE=53
TREE_NUM_FRACT=54
TREE_NUM_WHOLE=55
TREE_PASTE=56
TREE_PASTE_REPLACE=57
TREE_PASTE_WITH=58
TREE_PROC=59
TREE_PROC_ARGS=60
TREE_RECEIVE=61
TREE_REQUEST=62
TREE_STATELESS=63
TREE_STATEMENTS=64
TREE_STATEMENT_ASSIGN=65
TREE_STATEMENT_ASSIGN_TO=66
TREE_STATEMENT_CALL=67
TREE_STATEMENT_ELIF=68
TREE_STATEMENT_ELSE=69
TREE_STATEMENT_IF=70
TREE_STATEMENT_WHILE=71
TREE_STATEMENT_WITH=72
TREE_TYPES=73
TREE_TYPES_ITEM=74
TREE_VARS=75
TYPES=76
UNDERSCORE=77
VARS=78
WHILE=79
WHITESPACE=80
WITH=81

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "RECEIVE", "REPLACE", "REPLY", 
    "REQUEST", "STATELESS", "STRING", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", 
    "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_LOCAL_VARS", "TREE_MESSAGES", "TREE_MESSAGES_ITEM", 
    "TREE_MODULE", "TREE_MODULE_QUEUE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_RECEIVE", "TREE_REQUEST", "TREE_STATELESS", 
    "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", 
    "TREE_STATEMENT_IF", "TREE_STATEMENT_WHILE", "TREE_STATEMENT_WITH", 
    "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", "UNDERSCORE", 
    "VARS", "WHILE", "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

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

        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
            )

        self.dfa39 = self.DFA39(
            self, 39,
            eot = self.DFA39_eot,
            eof = self.DFA39_eof,
            min = self.DFA39_min,
            max = self.DFA39_max,
            accept = self.DFA39_accept,
            special = self.DFA39_special,
            transition = self.DFA39_transition
            )

        self.dfa51 = self.DFA51(
            self, 51,
            eot = self.DFA51_eot,
            eof = self.DFA51_eof,
            min = self.DFA51_min,
            max = self.DFA51_max,
            accept = self.DFA51_accept,
            special = self.DFA51_special,
            transition = self.DFA51_transition
            )

        self.dfa56 = self.DFA56(
            self, 56,
            eot = self.DFA56_eot,
            eof = self.DFA56_eof,
            min = self.DFA56_min,
            max = self.DFA56_max,
            accept = self.DFA56_accept,
            special = self.DFA56_special,
            transition = self.DFA56_transition
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
    # grammar/ShyRecognizerFrontend.g:26:1: module : MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* ( receive )* ( request )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* ( request )* ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE7 = None
        ID8 = None
        NEWLINE9 = None
        INDENT10 = None
        NEWLINE11 = None
        DEDENT16 = None
        NEWLINE17 = None
        module_queue12 = None

        proc13 = None

        receive14 = None

        request15 = None


        MODULE7_tree = None
        ID8_tree = None
        NEWLINE9_tree = None
        INDENT10_tree = None
        NEWLINE11_tree = None
        DEDENT16_tree = None
        NEWLINE17_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_request = RewriteRuleSubtreeStream(self._adaptor, "rule request")
        stream_module_queue = RewriteRuleSubtreeStream(self._adaptor, "rule module_queue")
        stream_receive = RewriteRuleSubtreeStream(self._adaptor, "rule receive")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:27:5: ( MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* ( receive )* ( request )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* ( request )* ) )
                # grammar/ShyRecognizerFrontend.g:27:9: MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* ( receive )* ( request )* DEDENT NEWLINE
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





                # grammar/ShyRecognizerFrontend.g:29:9: ( proc )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == PROC) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyRecognizerFrontend.g:29:9: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_module151)
                        proc13 = self.proc()

                        self._state.following.pop()
                        stream_proc.add(proc13.tree)



                    else:
                        break #loop3


                # grammar/ShyRecognizerFrontend.g:30:9: ( receive )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == RECEIVE) :
                        alt4 = 1


                    if alt4 == 1:
                        # grammar/ShyRecognizerFrontend.g:30:9: receive
                        pass 
                        self._state.following.append(self.FOLLOW_receive_in_module163)
                        receive14 = self.receive()

                        self._state.following.pop()
                        stream_receive.add(receive14.tree)



                    else:
                        break #loop4


                # grammar/ShyRecognizerFrontend.g:31:9: ( request )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == REQUEST) :
                        alt5 = 1


                    if alt5 == 1:
                        # grammar/ShyRecognizerFrontend.g:31:9: request
                        pass 
                        self._state.following.append(self.FOLLOW_request_in_module175)
                        request15 = self.request()

                        self._state.following.pop()
                        stream_request.add(request15.tree)



                    else:
                        break #loop5


                DEDENT16 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_module187) 
                stream_DEDENT.add(DEDENT16)


                NEWLINE17 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module189) 
                stream_NEWLINE.add(NEWLINE17)


                # AST Rewrite
                # elements: proc, module_queue, receive, request, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 33:9: -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* ( request )* )
                # grammar/ShyRecognizerFrontend.g:33:13: ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* ( request )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MODULE, "TREE_MODULE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:34:17: ( module_queue )?
                if stream_module_queue.hasNext():
                    self._adaptor.addChild(root_1, stream_module_queue.nextTree())


                stream_module_queue.reset();

                # grammar/ShyRecognizerFrontend.g:35:17: ( proc )*
                while stream_proc.hasNext():
                    self._adaptor.addChild(root_1, stream_proc.nextTree())


                stream_proc.reset();

                # grammar/ShyRecognizerFrontend.g:36:17: ( receive )*
                while stream_receive.hasNext():
                    self._adaptor.addChild(root_1, stream_receive.nextTree())


                stream_receive.reset();

                # grammar/ShyRecognizerFrontend.g:37:17: ( request )*
                while stream_request.hasNext():
                    self._adaptor.addChild(root_1, stream_request.nextTree())


                stream_request.reset();

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
    # grammar/ShyRecognizerFrontend.g:41:1: module_queue : MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        retval = self.module_queue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE_QUEUE18 = None
        ID19 = None
        NEWLINE20 = None

        MODULE_QUEUE18_tree = None
        ID19_tree = None
        NEWLINE20_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE_QUEUE = RewriteRuleTokenStream(self._adaptor, "token MODULE_QUEUE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:42:5: ( MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerFrontend.g:42:9: MODULE_QUEUE ID NEWLINE
                pass 
                MODULE_QUEUE18 = self.match(self.input, MODULE_QUEUE, self.FOLLOW_MODULE_QUEUE_in_module_queue319) 
                stream_MODULE_QUEUE.add(MODULE_QUEUE18)


                ID19 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue321) 
                stream_ID.add(ID19)


                NEWLINE20 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module_queue323) 
                stream_NEWLINE.add(NEWLINE20)


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
                # 43:9: -> ^( TREE_MODULE_QUEUE ID )
                # grammar/ShyRecognizerFrontend.g:43:13: ^( TREE_MODULE_QUEUE ID )
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
    # grammar/ShyRecognizerFrontend.g:46:1: stateless : STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS21 = None
        ID22 = None
        NEWLINE23 = None
        INDENT24 = None
        NEWLINE25 = None
        DEDENT27 = None
        NEWLINE28 = None
        proc26 = None


        STATELESS21_tree = None
        ID22_tree = None
        NEWLINE23_tree = None
        INDENT24_tree = None
        NEWLINE25_tree = None
        DEDENT27_tree = None
        NEWLINE28_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:47:5: ( STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:47:9: STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                STATELESS21 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless361) 
                stream_STATELESS.add(STATELESS21)


                ID22 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless363) 
                stream_ID.add(ID22)


                NEWLINE23 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless365) 
                stream_NEWLINE.add(NEWLINE23)


                # grammar/ShyRecognizerFrontend.g:47:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == INDENT) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerFrontend.g:47:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT24 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless369) 
                    stream_INDENT.add(INDENT24)


                    NEWLINE25 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless371) 
                    stream_NEWLINE.add(NEWLINE25)


                    # grammar/ShyRecognizerFrontend.g:47:47: ( proc )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == PROC) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyRecognizerFrontend.g:47:47: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless373)
                            proc26 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc26.tree)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT27 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless377) 
                    stream_DEDENT.add(DEDENT27)


                    NEWLINE28 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless379) 
                    stream_NEWLINE.add(NEWLINE28)





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
                # 48:9: -> ^( TREE_STATELESS ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:48:13: ^( TREE_STATELESS ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:48:34: ( proc )*
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


    class request_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.request_return, self).__init__()

            self.tree = None





    # $ANTLR start "request"
    # grammar/ShyRecognizerFrontend.g:51:1: request : ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) );
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REQUEST29 = None
        ID30 = None
        NEWLINE31 = None
        REQUEST32 = None
        ID33 = None
        NEWLINE34 = None
        INDENT35 = None
        NEWLINE36 = None
        DEDENT39 = None
        NEWLINE40 = None
        local_vars37 = None

        local_ops38 = None


        REQUEST29_tree = None
        ID30_tree = None
        NEWLINE31_tree = None
        REQUEST32_tree = None
        ID33_tree = None
        NEWLINE34_tree = None
        INDENT35_tree = None
        NEWLINE36_tree = None
        DEDENT39_tree = None
        NEWLINE40_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:52:5: ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) )
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == REQUEST) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == ID) :
                        LA10_2 = self.input.LA(3)

                        if (LA10_2 == NEWLINE) :
                            LA10_3 = self.input.LA(4)

                            if (LA10_3 == INDENT) :
                                alt10 = 2
                            elif (LA10_3 == DEDENT or LA10_3 == REQUEST) :
                                alt10 = 1
                            else:
                                nvae = NoViableAltException("", 10, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 10, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 10, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 10, 0, self.input)

                    raise nvae


                if alt10 == 1:
                    # grammar/ShyRecognizerFrontend.g:52:9: REQUEST ID NEWLINE
                    pass 
                    REQUEST29 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request425) 
                    stream_REQUEST.add(REQUEST29)


                    ID30 = self.match(self.input, ID, self.FOLLOW_ID_in_request427) 
                    stream_ID.add(ID30)


                    NEWLINE31 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request429) 
                    stream_NEWLINE.add(NEWLINE31)


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
                    # 53:9: -> ^( TREE_REQUEST ID )
                    # grammar/ShyRecognizerFrontend.g:53:13: ^( TREE_REQUEST ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt10 == 2:
                    # grammar/ShyRecognizerFrontend.g:54:9: REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    REQUEST32 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request458) 
                    stream_REQUEST.add(REQUEST32)


                    ID33 = self.match(self.input, ID, self.FOLLOW_ID_in_request460) 
                    stream_ID.add(ID33)


                    NEWLINE34 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request462) 
                    stream_NEWLINE.add(NEWLINE34)


                    INDENT35 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request464) 
                    stream_INDENT.add(INDENT35)


                    NEWLINE36 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request466) 
                    stream_NEWLINE.add(NEWLINE36)


                    # grammar/ShyRecognizerFrontend.g:55:13: ( local_vars )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == VARS) :
                        alt8 = 1
                    if alt8 == 1:
                        # grammar/ShyRecognizerFrontend.g:55:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_request480)
                        local_vars37 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars37.tree)





                    # grammar/ShyRecognizerFrontend.g:55:26: ( local_ops )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OPS) :
                        alt9 = 1
                    if alt9 == 1:
                        # grammar/ShyRecognizerFrontend.g:55:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_request484)
                        local_ops38 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops38.tree)





                    DEDENT39 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request496) 
                    stream_DEDENT.add(DEDENT39)


                    NEWLINE40 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request498) 
                    stream_NEWLINE.add(NEWLINE40)


                    # AST Rewrite
                    # elements: ID, local_vars, local_ops
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 57:9: -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:57:13: ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:57:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:57:45: ( local_ops )?
                    if stream_local_ops.hasNext():
                        self._adaptor.addChild(root_1, stream_local_ops.nextTree())


                    stream_local_ops.reset();

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

    # $ANTLR end "request"


    class receive_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.receive_return, self).__init__()

            self.tree = None





    # $ANTLR start "receive"
    # grammar/ShyRecognizerFrontend.g:60:1: receive : ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) );
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECEIVE41 = None
        ID42 = None
        NEWLINE43 = None
        RECEIVE44 = None
        ID45 = None
        NEWLINE46 = None
        INDENT47 = None
        NEWLINE48 = None
        DEDENT51 = None
        NEWLINE52 = None
        local_vars49 = None

        local_ops50 = None


        RECEIVE41_tree = None
        ID42_tree = None
        NEWLINE43_tree = None
        RECEIVE44_tree = None
        ID45_tree = None
        NEWLINE46_tree = None
        INDENT47_tree = None
        NEWLINE48_tree = None
        DEDENT51_tree = None
        NEWLINE52_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_RECEIVE = RewriteRuleTokenStream(self._adaptor, "token RECEIVE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:61:5: ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == RECEIVE) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == ID) :
                        LA13_2 = self.input.LA(3)

                        if (LA13_2 == NEWLINE) :
                            LA13_3 = self.input.LA(4)

                            if (LA13_3 == INDENT) :
                                alt13 = 2
                            elif (LA13_3 == DEDENT or LA13_3 == RECEIVE or LA13_3 == REQUEST) :
                                alt13 = 1
                            else:
                                nvae = NoViableAltException("", 13, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 13, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 13, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae


                if alt13 == 1:
                    # grammar/ShyRecognizerFrontend.g:61:9: RECEIVE ID NEWLINE
                    pass 
                    RECEIVE41 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive544) 
                    stream_RECEIVE.add(RECEIVE41)


                    ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_receive546) 
                    stream_ID.add(ID42)


                    NEWLINE43 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive548) 
                    stream_NEWLINE.add(NEWLINE43)


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
                    # 62:9: -> ^( TREE_RECEIVE ID )
                    # grammar/ShyRecognizerFrontend.g:62:13: ^( TREE_RECEIVE ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 2:
                    # grammar/ShyRecognizerFrontend.g:63:9: RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    RECEIVE44 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive577) 
                    stream_RECEIVE.add(RECEIVE44)


                    ID45 = self.match(self.input, ID, self.FOLLOW_ID_in_receive579) 
                    stream_ID.add(ID45)


                    NEWLINE46 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive581) 
                    stream_NEWLINE.add(NEWLINE46)


                    INDENT47 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive583) 
                    stream_INDENT.add(INDENT47)


                    NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive585) 
                    stream_NEWLINE.add(NEWLINE48)


                    # grammar/ShyRecognizerFrontend.g:64:13: ( local_vars )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == VARS) :
                        alt11 = 1
                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:64:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_receive599)
                        local_vars49 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars49.tree)





                    # grammar/ShyRecognizerFrontend.g:64:26: ( local_ops )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == OPS) :
                        alt12 = 1
                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:64:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_receive603)
                        local_ops50 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops50.tree)





                    DEDENT51 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive615) 
                    stream_DEDENT.add(DEDENT51)


                    NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive617) 
                    stream_NEWLINE.add(NEWLINE52)


                    # AST Rewrite
                    # elements: local_ops, local_vars, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 66:9: -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:66:13: ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:66:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:66:45: ( local_ops )?
                    if stream_local_ops.hasNext():
                        self._adaptor.addChild(root_1, stream_local_ops.nextTree())


                    stream_local_ops.reset();

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

    # $ANTLR end "receive"


    class proc_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc"
    # grammar/ShyRecognizerFrontend.g:69:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC53 = None
        ID54 = None
        NEWLINE55 = None
        PROC56 = None
        ID57 = None
        NEWLINE58 = None
        INDENT59 = None
        NEWLINE60 = None
        DEDENT62 = None
        NEWLINE63 = None
        PROC64 = None
        ID65 = None
        NEWLINE66 = None
        INDENT67 = None
        NEWLINE68 = None
        DEDENT72 = None
        NEWLINE73 = None
        statements61 = None

        proc_args69 = None

        local_vars70 = None

        local_ops71 = None


        PROC53_tree = None
        ID54_tree = None
        NEWLINE55_tree = None
        PROC56_tree = None
        ID57_tree = None
        NEWLINE58_tree = None
        INDENT59_tree = None
        NEWLINE60_tree = None
        DEDENT62_tree = None
        NEWLINE63_tree = None
        PROC64_tree = None
        ID65_tree = None
        NEWLINE66_tree = None
        INDENT67_tree = None
        NEWLINE68_tree = None
        DEDENT72_tree = None
        NEWLINE73_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_proc_args = RewriteRuleSubtreeStream(self._adaptor, "rule proc_args")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:70:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) )
                alt17 = 3
                LA17_0 = self.input.LA(1)

                if (LA17_0 == PROC) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == ID) :
                        LA17_2 = self.input.LA(3)

                        if (LA17_2 == NEWLINE) :
                            LA17_3 = self.input.LA(4)

                            if (LA17_3 == INDENT) :
                                LA17_4 = self.input.LA(5)

                                if (LA17_4 == NEWLINE) :
                                    LA17_6 = self.input.LA(6)

                                    if ((EXPRESSION <= LA17_6 <= IF) or LA17_6 == MINUS or LA17_6 == NUMBER or LA17_6 == WHILE or LA17_6 == WITH) :
                                        alt17 = 2
                                    elif (LA17_6 == ARGS or LA17_6 == DEDENT or LA17_6 == OPS or LA17_6 == VARS) :
                                        alt17 = 3
                                    else:
                                        nvae = NoViableAltException("", 17, 6, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 17, 4, self.input)

                                    raise nvae


                            elif (LA17_3 == DEDENT or (PROC <= LA17_3 <= RECEIVE) or LA17_3 == REQUEST) :
                                alt17 = 1
                            else:
                                nvae = NoViableAltException("", 17, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 17, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 17, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:70:9: PROC ID NEWLINE
                    pass 
                    PROC53 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc663) 
                    stream_PROC.add(PROC53)


                    ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_proc665) 
                    stream_ID.add(ID54)


                    NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc667) 
                    stream_NEWLINE.add(NEWLINE55)


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
                    # 71:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:71:13: ^( TREE_PROC ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:72:9: PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    PROC56 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc696) 
                    stream_PROC.add(PROC56)


                    ID57 = self.match(self.input, ID, self.FOLLOW_ID_in_proc698) 
                    stream_ID.add(ID57)


                    NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc700) 
                    stream_NEWLINE.add(NEWLINE58)


                    INDENT59 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc702) 
                    stream_INDENT.add(INDENT59)


                    NEWLINE60 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc704) 
                    stream_NEWLINE.add(NEWLINE60)


                    self._state.following.append(self.FOLLOW_statements_in_proc706)
                    statements61 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements61.tree)


                    DEDENT62 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc708) 
                    stream_DEDENT.add(DEDENT62)


                    NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc710) 
                    stream_NEWLINE.add(NEWLINE63)


                    # AST Rewrite
                    # elements: statements, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 73:9: -> ^( TREE_PROC ID statements )
                    # grammar/ShyRecognizerFrontend.g:73:13: ^( TREE_PROC ID statements )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_statements.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt17 == 3:
                    # grammar/ShyRecognizerFrontend.g:74:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    PROC64 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc741) 
                    stream_PROC.add(PROC64)


                    ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_proc743) 
                    stream_ID.add(ID65)


                    NEWLINE66 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc745) 
                    stream_NEWLINE.add(NEWLINE66)


                    INDENT67 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc747) 
                    stream_INDENT.add(INDENT67)


                    NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc749) 
                    stream_NEWLINE.add(NEWLINE68)


                    # grammar/ShyRecognizerFrontend.g:75:13: ( proc_args )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == ARGS) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:75:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc763)
                        proc_args69 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args69.tree)





                    # grammar/ShyRecognizerFrontend.g:75:25: ( local_vars )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == VARS) :
                        alt15 = 1
                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:75:25: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_proc767)
                        local_vars70 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars70.tree)





                    # grammar/ShyRecognizerFrontend.g:75:38: ( local_ops )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == OPS) :
                        alt16 = 1
                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:75:38: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_proc771)
                        local_ops71 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops71.tree)





                    DEDENT72 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc783) 
                    stream_DEDENT.add(DEDENT72)


                    NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc785) 
                    stream_NEWLINE.add(NEWLINE73)


                    # AST Rewrite
                    # elements: local_vars, proc_args, ID, local_ops
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 77:9: -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:77:13: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:77:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:77:41: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:77:54: ( local_ops )?
                    if stream_local_ops.hasNext():
                        self._adaptor.addChild(root_1, stream_local_ops.nextTree())


                    stream_local_ops.reset();

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
    # grammar/ShyRecognizerFrontend.g:80:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS74 = None
        attrs_hints75 = None


        ARGS74_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:81:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:81:9: ARGS attrs_hints
                pass 
                ARGS74 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args835) 
                stream_ARGS.add(ARGS74)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args837)
                attrs_hints75 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints75.tree)


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
                # 81:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:81:29: ^( TREE_PROC_ARGS attrs_hints )
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


    class local_vars_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.local_vars_return, self).__init__()

            self.tree = None





    # $ANTLR start "local_vars"
    # grammar/ShyRecognizerFrontend.g:84:1: local_vars : VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        retval = self.local_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS76 = None
        attrs_hints77 = None


        VARS76_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:85:5: ( VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:85:9: VARS attrs_hints
                pass 
                VARS76 = self.match(self.input, VARS, self.FOLLOW_VARS_in_local_vars866) 
                stream_VARS.add(VARS76)


                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars868)
                attrs_hints77 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints77.tree)


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
                # 85:26: -> ^( TREE_LOCAL_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:85:29: ^( TREE_LOCAL_VARS attrs_hints )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_LOCAL_VARS, "TREE_LOCAL_VARS")
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

    # $ANTLR end "local_vars"


    class local_ops_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.local_ops_return, self).__init__()

            self.tree = None





    # $ANTLR start "local_ops"
    # grammar/ShyRecognizerFrontend.g:88:1: local_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
    def local_ops(self, ):
        retval = self.local_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS78 = None
        NEWLINE79 = None
        INDENT80 = None
        NEWLINE81 = None
        DEDENT83 = None
        NEWLINE84 = None
        statements82 = None


        OPS78_tree = None
        NEWLINE79_tree = None
        INDENT80_tree = None
        NEWLINE81_tree = None
        DEDENT83_tree = None
        NEWLINE84_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:89:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
                # grammar/ShyRecognizerFrontend.g:89:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                OPS78 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops897) 
                stream_OPS.add(OPS78)


                NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops899) 
                stream_NEWLINE.add(NEWLINE79)


                INDENT80 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_local_ops901) 
                stream_INDENT.add(INDENT80)


                NEWLINE81 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops903) 
                stream_NEWLINE.add(NEWLINE81)


                self._state.following.append(self.FOLLOW_statements_in_local_ops905)
                statements82 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements82.tree)


                DEDENT83 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_local_ops907) 
                stream_DEDENT.add(DEDENT83)


                NEWLINE84 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops909) 
                stream_NEWLINE.add(NEWLINE84)


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
                # 90:9: -> statements
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

    # $ANTLR end "local_ops"


    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement"
    # grammar/ShyRecognizerFrontend.g:93:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE86 = None
        statement_call_single_line85 = None

        statement_call_multi_line87 = None

        statement_if88 = None

        statement_assign89 = None

        statement_while90 = None

        statement_with91 = None


        NEWLINE86_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:94:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt18 = 6
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:94:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement940)
                    statement_call_single_line85 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line85.tree)


                    NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement942) 
                    stream_NEWLINE.add(NEWLINE86)


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
                    # 95:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:96:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement968)
                    statement_call_multi_line87 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line87.tree)



                elif alt18 == 3:
                    # grammar/ShyRecognizerFrontend.g:97:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement978)
                    statement_if88 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if88.tree)



                elif alt18 == 4:
                    # grammar/ShyRecognizerFrontend.g:98:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement988)
                    statement_assign89 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign89.tree)



                elif alt18 == 5:
                    # grammar/ShyRecognizerFrontend.g:99:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement998)
                    statement_while90 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while90.tree)



                elif alt18 == 6:
                    # grammar/ShyRecognizerFrontend.g:100:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement1008)
                    statement_with91 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with91.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:103:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement92 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:104:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:104:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:104:9: ( statement )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA19_0 <= IF) or LA19_0 == MINUS or LA19_0 == NUMBER or LA19_0 == WHILE or LA19_0 == WITH) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerFrontend.g:104:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1027)
                        statement92 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement92.tree)



                    else:
                        if cnt19 >= 1:
                            break #loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1


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
                # 105:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:105:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:105:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:108:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH93 = None
        ID94 = None
        NEWLINE95 = None
        INDENT96 = None
        NEWLINE97 = None
        DEDENT99 = None
        NEWLINE100 = None
        statements98 = None


        WITH93_tree = None
        ID94_tree = None
        NEWLINE95_tree = None
        INDENT96_tree = None
        NEWLINE97_tree = None
        DEDENT99_tree = None
        NEWLINE100_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:109:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:109:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH93 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1069) 
                stream_WITH.add(WITH93)


                ID94 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1071) 
                stream_ID.add(ID94)


                NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1073) 
                stream_NEWLINE.add(NEWLINE95)


                INDENT96 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1083) 
                stream_INDENT.add(INDENT96)


                NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1085) 
                stream_NEWLINE.add(NEWLINE97)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1087)
                statements98 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements98.tree)


                DEDENT99 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1089) 
                stream_DEDENT.add(DEDENT99)


                NEWLINE100 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1091) 
                stream_NEWLINE.add(NEWLINE100)


                # AST Rewrite
                # elements: statements, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 111:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:111:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:114:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID101 = None
        ARROW_LEFT102 = None
        NEWLINE104 = None
        ID105 = None
        ARROW_LEFT106 = None
        NEWLINE107 = None
        INDENT108 = None
        NEWLINE109 = None
        NEWLINE111 = None
        DEDENT112 = None
        NEWLINE113 = None
        ARROW_RIGHT115 = None
        ID116 = None
        NEWLINE117 = None
        ARROW_RIGHT119 = None
        NEWLINE120 = None
        INDENT121 = None
        NEWLINE122 = None
        ID123 = None
        NEWLINE124 = None
        DEDENT125 = None
        NEWLINE126 = None
        arbitrary_value103 = None

        arbitrary_value110 = None

        arbitrary_value114 = None

        arbitrary_value118 = None


        ID101_tree = None
        ARROW_LEFT102_tree = None
        NEWLINE104_tree = None
        ID105_tree = None
        ARROW_LEFT106_tree = None
        NEWLINE107_tree = None
        INDENT108_tree = None
        NEWLINE109_tree = None
        NEWLINE111_tree = None
        DEDENT112_tree = None
        NEWLINE113_tree = None
        ARROW_RIGHT115_tree = None
        ID116_tree = None
        NEWLINE117_tree = None
        ARROW_RIGHT119_tree = None
        NEWLINE120_tree = None
        INDENT121_tree = None
        NEWLINE122_tree = None
        ID123_tree = None
        NEWLINE124_tree = None
        DEDENT125_tree = None
        NEWLINE126_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:115:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt30 = 4
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:115:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:115:9: ( ID )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == ID) :
                            alt20 = 1


                        if alt20 == 1:
                            # grammar/ShyRecognizerFrontend.g:115:9: ID
                            pass 
                            ID101 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1131) 
                            stream_ID.add(ID101)



                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


                    ARROW_LEFT102 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1135) 
                    stream_ARROW_LEFT.add(ARROW_LEFT102)


                    # grammar/ShyRecognizerFrontend.g:115:25: ( arbitrary_value )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:115:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1137)
                            arbitrary_value103 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value103.tree)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    NEWLINE104 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1141) 
                    stream_NEWLINE.add(NEWLINE104)


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
                    # 116:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:116:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:116:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:117:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt30 == 2:
                    # grammar/ShyRecognizerFrontend.g:118:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:118:9: ( ID )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == ID) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:118:9: ID
                            pass 
                            ID105 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1194) 
                            stream_ID.add(ID105)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    ARROW_LEFT106 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1198) 
                    stream_ARROW_LEFT.add(ARROW_LEFT106)


                    NEWLINE107 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1200) 
                    stream_NEWLINE.add(NEWLINE107)


                    INDENT108 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1202) 
                    stream_INDENT.add(INDENT108)


                    NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1204) 
                    stream_NEWLINE.add(NEWLINE109)


                    # grammar/ShyRecognizerFrontend.g:119:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:119:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:119:11: ( arbitrary_value )+
                            cnt23 = 0
                            while True: #loop23
                                alt23 = 2
                                LA23_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                                    alt23 = 1


                                if alt23 == 1:
                                    # grammar/ShyRecognizerFrontend.g:119:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1216)
                                    arbitrary_value110 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value110.tree)



                                else:
                                    if cnt23 >= 1:
                                        break #loop23

                                    eee = EarlyExitException(23, self.input)
                                    raise eee

                                cnt23 += 1


                            NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1220) 
                            stream_NEWLINE.add(NEWLINE111)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    DEDENT112 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1226) 
                    stream_DEDENT.add(DEDENT112)


                    NEWLINE113 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1228) 
                    stream_NEWLINE.add(NEWLINE113)


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
                    # 120:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:120:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:120:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:121:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt30 == 3:
                    # grammar/ShyRecognizerFrontend.g:122:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:122:9: ( arbitrary_value )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:122:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1281)
                            arbitrary_value114 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value114.tree)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    ARROW_RIGHT115 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1285) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT115)


                    # grammar/ShyRecognizerFrontend.g:122:39: ( ID )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == ID) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:122:39: ID
                            pass 
                            ID116 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1287) 
                            stream_ID.add(ID116)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


                    NEWLINE117 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1291) 
                    stream_NEWLINE.add(NEWLINE117)


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
                    # 123:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:123:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:123:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:124:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt30 == 4:
                    # grammar/ShyRecognizerFrontend.g:125:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:125:9: ( arbitrary_value )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA27_0 <= ID) or LA27_0 == MINUS or LA27_0 == NUMBER) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:125:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1344)
                            arbitrary_value118 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value118.tree)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    ARROW_RIGHT119 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1348) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT119)


                    NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1350) 
                    stream_NEWLINE.add(NEWLINE120)


                    INDENT121 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1352) 
                    stream_INDENT.add(INDENT121)


                    NEWLINE122 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1354) 
                    stream_NEWLINE.add(NEWLINE122)


                    # grammar/ShyRecognizerFrontend.g:126:9: ( ( ID )+ NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:126:11: ( ID )+
                            cnt28 = 0
                            while True: #loop28
                                alt28 = 2
                                LA28_0 = self.input.LA(1)

                                if (LA28_0 == ID) :
                                    alt28 = 1


                                if alt28 == 1:
                                    # grammar/ShyRecognizerFrontend.g:126:11: ID
                                    pass 
                                    ID123 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1366) 
                                    stream_ID.add(ID123)



                                else:
                                    if cnt28 >= 1:
                                        break #loop28

                                    eee = EarlyExitException(28, self.input)
                                    raise eee

                                cnt28 += 1


                            NEWLINE124 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1370) 
                            stream_NEWLINE.add(NEWLINE124)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT125 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1376) 
                    stream_DEDENT.add(DEDENT125)


                    NEWLINE126 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1378) 
                    stream_NEWLINE.add(NEWLINE126)


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
                    # 127:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:127:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:127:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:128:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


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

    # $ANTLR end "statement_assign"


    class statement_while_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_while_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_while"
    # grammar/ShyRecognizerFrontend.g:131:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE127 = None
        NEWLINE129 = None
        DO130 = None
        NEWLINE131 = None
        INDENT132 = None
        NEWLINE133 = None
        DEDENT135 = None
        NEWLINE136 = None
        condition128 = None

        statements134 = None


        WHILE127_tree = None
        NEWLINE129_tree = None
        DO130_tree = None
        NEWLINE131_tree = None
        INDENT132_tree = None
        NEWLINE133_tree = None
        DEDENT135_tree = None
        NEWLINE136_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:132:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:132:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE127 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1440) 
                stream_WHILE.add(WHILE127)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1442)
                condition128 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition128.tree)


                # grammar/ShyRecognizerFrontend.g:132:25: ( NEWLINE )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == NEWLINE) :
                    alt31 = 1
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:132:25: NEWLINE
                    pass 
                    NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1444) 
                    stream_NEWLINE.add(NEWLINE129)





                DO130 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1448) 
                stream_DO.add(DO130)


                NEWLINE131 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1450) 
                stream_NEWLINE.add(NEWLINE131)


                INDENT132 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1464) 
                stream_INDENT.add(INDENT132)


                NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1466) 
                stream_NEWLINE.add(NEWLINE133)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1468)
                statements134 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements134.tree)


                DEDENT135 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1470) 
                stream_DEDENT.add(DEDENT135)


                NEWLINE136 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1472) 
                stream_NEWLINE.add(NEWLINE136)


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
                # 134:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:134:13: ^( TREE_STATEMENT_WHILE condition statements )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_WHILE, "TREE_STATEMENT_WHILE")
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

    # $ANTLR end "statement_while"


    class statement_if_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_if_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_if"
    # grammar/ShyRecognizerFrontend.g:137:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head137 = None

        statement_elif138 = None

        statement_else139 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:138:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:138:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1512)
                statement_if_head137 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head137.tree)


                # grammar/ShyRecognizerFrontend.g:139:9: ( statement_elif )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == ELIF) :
                        alt32 = 1


                    if alt32 == 1:
                        # grammar/ShyRecognizerFrontend.g:139:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1522)
                        statement_elif138 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif138.tree)



                    else:
                        break #loop32


                # grammar/ShyRecognizerFrontend.g:140:9: ( statement_else )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == ELSE) :
                    alt33 = 1
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:140:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1534)
                    statement_else139 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else139.tree)





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
                # 141:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:141:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:143:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:144:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:148:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF140 = None
        statement_elif_body141 = None


        IF140_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:149:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:149:9: IF statement_elif_body
                pass 
                IF140 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1642) 
                stream_IF.add(IF140)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1644)
                statement_elif_body141 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body141.tree)


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
                # 150:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:153:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF142 = None
        statement_elif_body143 = None


        ELIF142_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:154:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:154:9: ELIF statement_elif_body
                pass 
                ELIF142 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1676) 
                stream_ELIF.add(ELIF142)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1678)
                statement_elif_body143 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body143.tree)


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
                # 155:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:158:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE145 = None
        DO146 = None
        NEWLINE147 = None
        INDENT148 = None
        NEWLINE149 = None
        DEDENT151 = None
        NEWLINE152 = None
        condition144 = None

        statements150 = None


        NEWLINE145_tree = None
        DO146_tree = None
        NEWLINE147_tree = None
        INDENT148_tree = None
        NEWLINE149_tree = None
        DEDENT151_tree = None
        NEWLINE152_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:159:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:159:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1710)
                condition144 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition144.tree)


                # grammar/ShyRecognizerFrontend.g:159:19: ( NEWLINE )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == NEWLINE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:159:19: NEWLINE
                    pass 
                    NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1712) 
                    stream_NEWLINE.add(NEWLINE145)





                DO146 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1716) 
                stream_DO.add(DO146)


                NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1718) 
                stream_NEWLINE.add(NEWLINE147)


                INDENT148 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1732) 
                stream_INDENT.add(INDENT148)


                NEWLINE149 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1734) 
                stream_NEWLINE.add(NEWLINE149)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1736)
                statements150 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements150.tree)


                DEDENT151 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1738) 
                stream_DEDENT.add(DEDENT151)


                NEWLINE152 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1740) 
                stream_NEWLINE.add(NEWLINE152)


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
                # 161:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:161:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:164:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE153 = None
        NEWLINE154 = None
        INDENT155 = None
        NEWLINE156 = None
        DEDENT158 = None
        NEWLINE159 = None
        statements157 = None


        ELSE153_tree = None
        NEWLINE154_tree = None
        INDENT155_tree = None
        NEWLINE156_tree = None
        DEDENT158_tree = None
        NEWLINE159_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:165:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:165:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE153 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1780) 
                stream_ELSE.add(ELSE153)


                NEWLINE154 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1782) 
                stream_NEWLINE.add(NEWLINE154)


                INDENT155 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1796) 
                stream_INDENT.add(INDENT155)


                NEWLINE156 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1798) 
                stream_NEWLINE.add(NEWLINE156)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1800)
                statements157 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements157.tree)


                DEDENT158 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1802) 
                stream_DEDENT.add(DEDENT158)


                NEWLINE159 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1804) 
                stream_NEWLINE.add(NEWLINE159)


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
                # 167:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:167:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:170:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY161 = None
        ALL163 = None
        condition_call160 = None

        condition_calls162 = None

        condition_calls164 = None


        ANY161_tree = None
        ALL163_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:171:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt35 = 3
                LA35 = self.input.LA(1)
                if LA35 == ID:
                    alt35 = 1
                elif LA35 == ANY:
                    alt35 = 2
                elif LA35 == ALL:
                    alt35 = 3
                else:
                    nvae = NoViableAltException("", 35, 0, self.input)

                    raise nvae


                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:171:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1842)
                    condition_call160 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call160.tree)


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
                    # 172:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:172:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:173:9: ANY condition_calls
                    pass 
                    ANY161 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1871) 
                    stream_ANY.add(ANY161)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1873)
                    condition_calls162 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls162.tree)


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
                    # 174:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:174:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 3:
                    # grammar/ShyRecognizerFrontend.g:175:9: ALL condition_calls
                    pass 
                    ALL163 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1902) 
                    stream_ALL.add(ALL163)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1904)
                    condition_calls164 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls164.tree)


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
                    # 176:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:176:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:179:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE166 = None
        INDENT167 = None
        NEWLINE168 = None
        DEDENT170 = None
        NEWLINE171 = None
        condition_call165 = None

        condition_call_line169 = None


        NEWLINE166_tree = None
        INDENT167_tree = None
        NEWLINE168_tree = None
        DEDENT170_tree = None
        NEWLINE171_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:180:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == ID) :
                    alt37 = 1
                elif (LA37_0 == NEWLINE) :
                    alt37 = 2
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:180:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1942)
                    condition_call165 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call165.tree)



                elif alt37 == 2:
                    # grammar/ShyRecognizerFrontend.g:181:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE166 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1952) 
                    stream_NEWLINE.add(NEWLINE166)


                    INDENT167 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1954) 
                    stream_INDENT.add(INDENT167)


                    NEWLINE168 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1956) 
                    stream_NEWLINE.add(NEWLINE168)


                    # grammar/ShyRecognizerFrontend.g:181:32: ( condition_call_line )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:181:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1958)
                            condition_call_line169 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line169.tree)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


                    DEDENT170 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1962) 
                    stream_DEDENT.add(DEDENT170)


                    NEWLINE171 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1964) 
                    stream_NEWLINE.add(NEWLINE171)


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
                    # 182:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:182:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:185:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line172 = None

        statement_call_multi_line173 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:186:5: ( statement_call_single_line | statement_call_multi_line )
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:186:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1998)
                    statement_call_single_line172 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line172.tree)



                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:187:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call2008)
                    statement_call_multi_line173 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line173.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:190:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE175 = None
        statement_call_single_line174 = None

        statement_call_multi_line176 = None


        NEWLINE175_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:191:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:191:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line2027)
                    statement_call_single_line174 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line174.tree)


                    NEWLINE175 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line2029) 
                    stream_NEWLINE.add(NEWLINE175)


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
                    # 192:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:193:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2055)
                    statement_call_multi_line176 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line176.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:196:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID177 = None
        statement_call_args178 = None


        ID177_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:197:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:197:9: ID ( statement_call_args )?
                pass 
                ID177 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2074) 
                stream_ID.add(ID177)


                # grammar/ShyRecognizerFrontend.g:197:12: ( statement_call_args )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if ((EXPRESSION <= LA40_0 <= ID) or LA40_0 == MINUS or LA40_0 == NUMBER) :
                    alt40 = 1
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:197:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2076)
                    statement_call_args178 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args178.tree)





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
                # 198:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:198:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:198:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:201:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID179 = None
        NEWLINE181 = None
        INDENT182 = None
        NEWLINE183 = None
        NEWLINE185 = None
        DEDENT186 = None
        NEWLINE187 = None
        statement_call_args180 = None

        statement_call_args184 = None


        ID179_tree = None
        NEWLINE181_tree = None
        INDENT182_tree = None
        NEWLINE183_tree = None
        NEWLINE185_tree = None
        DEDENT186_tree = None
        NEWLINE187_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:202:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:202:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID179 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2120) 
                stream_ID.add(ID179)


                # grammar/ShyRecognizerFrontend.g:202:12: ( statement_call_args )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if ((EXPRESSION <= LA41_0 <= ID) or LA41_0 == MINUS or LA41_0 == NUMBER) :
                    alt41 = 1
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:202:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2122)
                    statement_call_args180 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args180.tree)





                NEWLINE181 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2126) 
                stream_NEWLINE.add(NEWLINE181)


                INDENT182 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2136) 
                stream_INDENT.add(INDENT182)


                NEWLINE183 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2138) 
                stream_NEWLINE.add(NEWLINE183)


                # grammar/ShyRecognizerFrontend.g:203:24: ( statement_call_args NEWLINE )+
                cnt42 = 0
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA42_0 <= ID) or LA42_0 == MINUS or LA42_0 == NUMBER) :
                        alt42 = 1


                    if alt42 == 1:
                        # grammar/ShyRecognizerFrontend.g:203:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2142)
                        statement_call_args184 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args184.tree)


                        NEWLINE185 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2144) 
                        stream_NEWLINE.add(NEWLINE185)



                    else:
                        if cnt42 >= 1:
                            break #loop42

                        eee = EarlyExitException(42, self.input)
                        raise eee

                    cnt42 += 1


                DEDENT186 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2150) 
                stream_DEDENT.add(DEDENT186)


                NEWLINE187 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2152) 
                stream_NEWLINE.add(NEWLINE187)


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
                # 204:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:204:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:204:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:207:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value188 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:207:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:207:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:207:23: ( arbitrary_value )+
                cnt43 = 0
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER) :
                        alt43 = 1


                    if alt43 == 1:
                        # grammar/ShyRecognizerFrontend.g:207:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2188)
                        arbitrary_value188 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value188.tree)



                    else:
                        if cnt43 >= 1:
                            break #loop43

                        eee = EarlyExitException(43, self.input)
                        raise eee

                    cnt43 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:209:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID189 = None
        EXPRESSION190 = None
        num_whole191 = None

        num_fract192 = None


        ID189_tree = None
        EXPRESSION190_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:210:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt44 = 4
                LA44 = self.input.LA(1)
                if LA44 == ID:
                    alt44 = 1
                elif LA44 == EXPRESSION:
                    alt44 = 2
                elif LA44 == MINUS:
                    LA44_3 = self.input.LA(2)

                    if (LA44_3 == NUMBER) :
                        LA44_4 = self.input.LA(3)

                        if (LA44_4 == DIVIDE) :
                            alt44 = 4
                        elif (LA44_4 == ARROW_RIGHT or LA44_4 == DO or (EXPRESSION <= LA44_4 <= ID) or LA44_4 == MINUS or (NEWLINE <= LA44_4 <= NUMBER)) :
                            alt44 = 3
                        else:
                            nvae = NoViableAltException("", 44, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 44, 3, self.input)

                        raise nvae


                elif LA44 == NUMBER:
                    LA44_4 = self.input.LA(2)

                    if (LA44_4 == DIVIDE) :
                        alt44 = 4
                    elif (LA44_4 == ARROW_RIGHT or LA44_4 == DO or (EXPRESSION <= LA44_4 <= ID) or LA44_4 == MINUS or (NEWLINE <= LA44_4 <= NUMBER)) :
                        alt44 = 3
                    else:
                        nvae = NoViableAltException("", 44, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae


                if alt44 == 1:
                    # grammar/ShyRecognizerFrontend.g:210:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID189 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2205)
                    ID189_tree = self._adaptor.createWithPayload(ID189)
                    self._adaptor.addChild(root_0, ID189_tree)




                elif alt44 == 2:
                    # grammar/ShyRecognizerFrontend.g:211:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION190 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2215)
                    EXPRESSION190_tree = self._adaptor.createWithPayload(EXPRESSION190)
                    self._adaptor.addChild(root_0, EXPRESSION190_tree)




                elif alt44 == 3:
                    # grammar/ShyRecognizerFrontend.g:212:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2225)
                    num_whole191 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole191.tree)



                elif alt44 == 4:
                    # grammar/ShyRecognizerFrontend.g:213:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2235)
                    num_fract192 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract192.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:216:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS193 = None
        ID194 = None
        NEWLINE195 = None
        INDENT196 = None
        NEWLINE197 = None
        DEDENT199 = None
        NEWLINE200 = None
        consts_items198 = None


        CONSTS193_tree = None
        ID194_tree = None
        NEWLINE195_tree = None
        INDENT196_tree = None
        NEWLINE197_tree = None
        DEDENT199_tree = None
        NEWLINE200_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:217:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:217:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS193 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2254) 
                stream_CONSTS.add(CONSTS193)


                ID194 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2256) 
                stream_ID.add(ID194)


                NEWLINE195 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2258) 
                stream_NEWLINE.add(NEWLINE195)


                INDENT196 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2268) 
                stream_INDENT.add(INDENT196)


                NEWLINE197 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2270) 
                stream_NEWLINE.add(NEWLINE197)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2272)
                consts_items198 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items198.tree)


                DEDENT199 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2274) 
                stream_DEDENT.add(DEDENT199)


                NEWLINE200 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2276) 
                stream_NEWLINE.add(NEWLINE200)


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
                # 219:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:219:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:221:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item201 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:221:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:221:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:221:16: ( consts_item )+
                cnt45 = 0
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ID) :
                        alt45 = 1


                    if alt45 == 1:
                        # grammar/ShyRecognizerFrontend.g:221:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2308)
                        consts_item201 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item201.tree)



                    else:
                        if cnt45 >= 1:
                            break #loop45

                        eee = EarlyExitException(45, self.input)
                        raise eee

                    cnt45 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:222:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID202 = None
        NEWLINE204 = None
        ID205 = None
        NEWLINE207 = None
        ID208 = None
        EXPRESSION209 = None
        NEWLINE210 = None
        num_whole203 = None

        num_fract206 = None


        ID202_tree = None
        NEWLINE204_tree = None
        ID205_tree = None
        NEWLINE207_tree = None
        ID208_tree = None
        EXPRESSION209_tree = None
        NEWLINE210_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:223:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt46 = 3
                LA46_0 = self.input.LA(1)

                if (LA46_0 == ID) :
                    LA46 = self.input.LA(2)
                    if LA46 == EXPRESSION:
                        alt46 = 3
                    elif LA46 == MINUS:
                        LA46_3 = self.input.LA(3)

                        if (LA46_3 == NUMBER) :
                            LA46_4 = self.input.LA(4)

                            if (LA46_4 == DIVIDE) :
                                alt46 = 2
                            elif (LA46_4 == NEWLINE) :
                                alt46 = 1
                            else:
                                nvae = NoViableAltException("", 46, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 46, 3, self.input)

                            raise nvae


                    elif LA46 == NUMBER:
                        LA46_4 = self.input.LA(3)

                        if (LA46_4 == DIVIDE) :
                            alt46 = 2
                        elif (LA46_4 == NEWLINE) :
                            alt46 = 1
                        else:
                            nvae = NoViableAltException("", 46, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 46, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae


                if alt46 == 1:
                    # grammar/ShyRecognizerFrontend.g:223:9: ID num_whole NEWLINE
                    pass 
                    ID202 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2324) 
                    stream_ID.add(ID202)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2326)
                    num_whole203 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole203.tree)


                    NEWLINE204 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2328) 
                    stream_NEWLINE.add(NEWLINE204)


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
                    # 223:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:223:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt46 == 2:
                    # grammar/ShyRecognizerFrontend.g:224:9: ID num_fract NEWLINE
                    pass 
                    ID205 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2350) 
                    stream_ID.add(ID205)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2352)
                    num_fract206 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract206.tree)


                    NEWLINE207 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2354) 
                    stream_NEWLINE.add(NEWLINE207)


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
                    # 224:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:224:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt46 == 3:
                    # grammar/ShyRecognizerFrontend.g:225:9: ID EXPRESSION NEWLINE
                    pass 
                    ID208 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2376) 
                    stream_ID.add(ID208)


                    EXPRESSION209 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2378) 
                    stream_EXPRESSION.add(EXPRESSION209)


                    NEWLINE210 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2380) 
                    stream_NEWLINE.add(NEWLINE210)


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
                    # 225:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:225:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:228:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES211 = None
        ID212 = None
        NEWLINE213 = None
        INDENT214 = None
        NEWLINE215 = None
        DEDENT217 = None
        NEWLINE218 = None
        types_item216 = None


        TYPES211_tree = None
        ID212_tree = None
        NEWLINE213_tree = None
        INDENT214_tree = None
        NEWLINE215_tree = None
        DEDENT217_tree = None
        NEWLINE218_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:229:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:229:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES211 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2411) 
                stream_TYPES.add(TYPES211)


                ID212 = self.match(self.input, ID, self.FOLLOW_ID_in_types2413) 
                stream_ID.add(ID212)


                NEWLINE213 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2415) 
                stream_NEWLINE.add(NEWLINE213)


                INDENT214 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2425) 
                stream_INDENT.add(INDENT214)


                NEWLINE215 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2427) 
                stream_NEWLINE.add(NEWLINE215)


                # grammar/ShyRecognizerFrontend.g:230:24: ( types_item )+
                cnt47 = 0
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == ID) :
                        alt47 = 1


                    if alt47 == 1:
                        # grammar/ShyRecognizerFrontend.g:230:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2429)
                        types_item216 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item216.tree)



                    else:
                        if cnt47 >= 1:
                            break #loop47

                        eee = EarlyExitException(47, self.input)
                        raise eee

                    cnt47 += 1


                DEDENT217 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2433) 
                stream_DEDENT.add(DEDENT217)


                NEWLINE218 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2435) 
                stream_NEWLINE.add(NEWLINE218)


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
                # 231:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:231:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:231:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:233:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID219 = None
        attrs_hints220 = None


        ID219_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:233:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:233:14: ID attrs_hints
                pass 
                ID219 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2469) 
                stream_ID.add(ID219)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2471)
                attrs_hints220 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints220.tree)


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
                # 233:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:233:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:235:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES221 = None
        ID222 = None
        NEWLINE223 = None
        INDENT224 = None
        NEWLINE225 = None
        DEDENT227 = None
        NEWLINE228 = None
        messages_item226 = None


        MESSAGES221_tree = None
        ID222_tree = None
        NEWLINE223_tree = None
        INDENT224_tree = None
        NEWLINE225_tree = None
        DEDENT227_tree = None
        NEWLINE228_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:236:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:236:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES221 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2498) 
                stream_MESSAGES.add(MESSAGES221)


                ID222 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2500) 
                stream_ID.add(ID222)


                NEWLINE223 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2502) 
                stream_NEWLINE.add(NEWLINE223)


                INDENT224 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2512) 
                stream_INDENT.add(INDENT224)


                NEWLINE225 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2514) 
                stream_NEWLINE.add(NEWLINE225)


                # grammar/ShyRecognizerFrontend.g:237:24: ( messages_item )+
                cnt48 = 0
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == ID) :
                        alt48 = 1


                    if alt48 == 1:
                        # grammar/ShyRecognizerFrontend.g:237:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2516)
                        messages_item226 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item226.tree)



                    else:
                        if cnt48 >= 1:
                            break #loop48

                        eee = EarlyExitException(48, self.input)
                        raise eee

                    cnt48 += 1


                DEDENT227 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2520) 
                stream_DEDENT.add(DEDENT227)


                NEWLINE228 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2522) 
                stream_NEWLINE.add(NEWLINE228)


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
                # 238:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:238:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:238:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:240:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID229 = None
        attrs_hints230 = None


        ID229_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:240:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:240:17: ID attrs_hints
                pass 
                ID229 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2556) 
                stream_ID.add(ID229)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2558)
                attrs_hints230 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints230.tree)


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
                # 240:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:240:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:242:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS231 = None
        ID232 = None
        attrs_hints233 = None


        VARS231_tree = None
        ID232_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:243:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:243:9: VARS ID attrs_hints
                pass 
                VARS231 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars2585) 
                stream_VARS.add(VARS231)


                ID232 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2587) 
                stream_ID.add(ID232)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2589)
                attrs_hints233 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints233.tree)


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
                # 244:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:244:12: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:247:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE235 = None
        NEWLINE236 = None
        INDENT237 = None
        NEWLINE238 = None
        NEWLINE240 = None
        DEDENT241 = None
        NEWLINE242 = None
        NEWLINE244 = None
        INDENT245 = None
        NEWLINE246 = None
        NEWLINE248 = None
        DEDENT249 = None
        NEWLINE250 = None
        attr_hint234 = None

        attr_hint239 = None

        attr_hint243 = None

        attr_hint247 = None


        NEWLINE235_tree = None
        NEWLINE236_tree = None
        INDENT237_tree = None
        NEWLINE238_tree = None
        NEWLINE240_tree = None
        DEDENT241_tree = None
        NEWLINE242_tree = None
        NEWLINE244_tree = None
        INDENT245_tree = None
        NEWLINE246_tree = None
        NEWLINE248_tree = None
        DEDENT249_tree = None
        NEWLINE250_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:248:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt51 = 3
                alt51 = self.dfa51.predict(self.input)
                if alt51 == 1:
                    # grammar/ShyRecognizerFrontend.g:248:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2628)
                    attr_hint234 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint234.tree)


                    NEWLINE235 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2630) 
                    stream_NEWLINE.add(NEWLINE235)


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
                    # 249:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt51 == 2:
                    # grammar/ShyRecognizerFrontend.g:250:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE236 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2654) 
                    stream_NEWLINE.add(NEWLINE236)


                    # grammar/ShyRecognizerFrontend.g:251:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:251:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT237 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2666) 
                    stream_INDENT.add(INDENT237)


                    NEWLINE238 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2668) 
                    stream_NEWLINE.add(NEWLINE238)


                    # grammar/ShyRecognizerFrontend.g:251:26: ( attr_hint NEWLINE )+
                    cnt49 = 0
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == CURLY_OPEN or LA49_0 == ID) :
                            alt49 = 1


                        if alt49 == 1:
                            # grammar/ShyRecognizerFrontend.g:251:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2672)
                            attr_hint239 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint239.tree)


                            NEWLINE240 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2674) 
                            stream_NEWLINE.add(NEWLINE240)



                        else:
                            if cnt49 >= 1:
                                break #loop49

                            eee = EarlyExitException(49, self.input)
                            raise eee

                        cnt49 += 1


                    DEDENT241 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2680) 
                    stream_DEDENT.add(DEDENT241)


                    NEWLINE242 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2682) 
                    stream_NEWLINE.add(NEWLINE242)





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
                    # 252:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:252:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt51 == 3:
                    # grammar/ShyRecognizerFrontend.g:253:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2710)
                    attr_hint243 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint243.tree)


                    NEWLINE244 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2712) 
                    stream_NEWLINE.add(NEWLINE244)


                    # grammar/ShyRecognizerFrontend.g:254:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:254:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT245 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2724) 
                    stream_INDENT.add(INDENT245)


                    NEWLINE246 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2726) 
                    stream_NEWLINE.add(NEWLINE246)


                    # grammar/ShyRecognizerFrontend.g:254:26: ( attr_hint NEWLINE )+
                    cnt50 = 0
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == CURLY_OPEN or LA50_0 == ID) :
                            alt50 = 1


                        if alt50 == 1:
                            # grammar/ShyRecognizerFrontend.g:254:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2730)
                            attr_hint247 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint247.tree)


                            NEWLINE248 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2732) 
                            stream_NEWLINE.add(NEWLINE248)



                        else:
                            if cnt50 >= 1:
                                break #loop50

                            eee = EarlyExitException(50, self.input)
                            raise eee

                        cnt50 += 1


                    DEDENT249 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2738) 
                    stream_DEDENT.add(DEDENT249)


                    NEWLINE250 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2740) 
                    stream_NEWLINE.add(NEWLINE250)





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
                    # 255:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:255:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:257:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID251 = None
        ID253 = None
        NEWLINE255 = None
        INDENT256 = None
        NEWLINE257 = None
        ID258 = None
        NEWLINE259 = None
        DEDENT260 = None
        hint252 = None

        hint254 = None


        ID251_tree = None
        ID253_tree = None
        NEWLINE255_tree = None
        INDENT256_tree = None
        NEWLINE257_tree = None
        ID258_tree = None
        NEWLINE259_tree = None
        DEDENT260_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:258:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt56 = 3
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # grammar/ShyRecognizerFrontend.g:258:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:258:9: ( ID )+
                    cnt52 = 0
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == ID) :
                            alt52 = 1


                        if alt52 == 1:
                            # grammar/ShyRecognizerFrontend.g:258:9: ID
                            pass 
                            ID251 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2777) 
                            stream_ID.add(ID251)



                        else:
                            if cnt52 >= 1:
                                break #loop52

                            eee = EarlyExitException(52, self.input)
                            raise eee

                        cnt52 += 1


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
                    # 259:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:259:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:259:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:259:45: ^( TREE_ATTR ID )
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




                elif alt56 == 2:
                    # grammar/ShyRecognizerFrontend.g:260:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2818)
                    hint252 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint252.tree)


                    # grammar/ShyRecognizerFrontend.g:260:14: ( ID )+
                    cnt53 = 0
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == ID) :
                            alt53 = 1


                        if alt53 == 1:
                            # grammar/ShyRecognizerFrontend.g:260:14: ID
                            pass 
                            ID253 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2820) 
                            stream_ID.add(ID253)



                        else:
                            if cnt53 >= 1:
                                break #loop53

                            eee = EarlyExitException(53, self.input)
                            raise eee

                        cnt53 += 1


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
                    # 261:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:261:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:261:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:261:35: ^( TREE_ATTR ID )
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




                elif alt56 == 3:
                    # grammar/ShyRecognizerFrontend.g:262:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2860)
                    hint254 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint254.tree)


                    NEWLINE255 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2862) 
                    stream_NEWLINE.add(NEWLINE255)


                    INDENT256 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2864) 
                    stream_INDENT.add(INDENT256)


                    NEWLINE257 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2866) 
                    stream_NEWLINE.add(NEWLINE257)


                    # grammar/ShyRecognizerFrontend.g:262:37: ( ( ID )+ NEWLINE )+
                    cnt55 = 0
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == ID) :
                            alt55 = 1


                        if alt55 == 1:
                            # grammar/ShyRecognizerFrontend.g:262:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:262:39: ( ID )+
                            cnt54 = 0
                            while True: #loop54
                                alt54 = 2
                                LA54_0 = self.input.LA(1)

                                if (LA54_0 == ID) :
                                    alt54 = 1


                                if alt54 == 1:
                                    # grammar/ShyRecognizerFrontend.g:262:39: ID
                                    pass 
                                    ID258 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2870) 
                                    stream_ID.add(ID258)



                                else:
                                    if cnt54 >= 1:
                                        break #loop54

                                    eee = EarlyExitException(54, self.input)
                                    raise eee

                                cnt54 += 1


                            NEWLINE259 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2874) 
                            stream_NEWLINE.add(NEWLINE259)



                        else:
                            if cnt55 >= 1:
                                break #loop55

                            eee = EarlyExitException(55, self.input)
                            raise eee

                        cnt55 += 1


                    DEDENT260 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2880) 
                    stream_DEDENT.add(DEDENT260)


                    # AST Rewrite
                    # elements: hint, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 263:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:263:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:263:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:263:35: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:266:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN261 = None
        ID262 = None
        CURLY_CLOSE263 = None
        CURLY_OPEN264 = None
        ID265 = None
        CURLY_CLOSE267 = None
        hint_arg266 = None


        CURLY_OPEN261_tree = None
        ID262_tree = None
        CURLY_CLOSE263_tree = None
        CURLY_OPEN264_tree = None
        ID265_tree = None
        CURLY_CLOSE267_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:267:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt58 = 2
                LA58_0 = self.input.LA(1)

                if (LA58_0 == CURLY_OPEN) :
                    LA58_1 = self.input.LA(2)

                    if (LA58_1 == ID) :
                        LA58_2 = self.input.LA(3)

                        if (LA58_2 == CURLY_CLOSE) :
                            alt58 = 1
                        elif (LA58_2 == ID or LA58_2 == UNDERSCORE) :
                            alt58 = 2
                        else:
                            nvae = NoViableAltException("", 58, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 58, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 58, 0, self.input)

                    raise nvae


                if alt58 == 1:
                    # grammar/ShyRecognizerFrontend.g:267:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN261 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2927) 
                    stream_CURLY_OPEN.add(CURLY_OPEN261)


                    ID262 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2929) 
                    stream_ID.add(ID262)


                    CURLY_CLOSE263 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2931) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE263)


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
                    # 267:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:267:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt58 == 2:
                    # grammar/ShyRecognizerFrontend.g:268:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN264 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2951) 
                    stream_CURLY_OPEN.add(CURLY_OPEN264)


                    ID265 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2953) 
                    stream_ID.add(ID265)


                    # grammar/ShyRecognizerFrontend.g:268:23: ( hint_arg )+
                    cnt57 = 0
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == ID or LA57_0 == UNDERSCORE) :
                            alt57 = 1


                        if alt57 == 1:
                            # grammar/ShyRecognizerFrontend.g:268:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2955)
                            hint_arg266 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg266.tree)



                        else:
                            if cnt57 >= 1:
                                break #loop57

                            eee = EarlyExitException(57, self.input)
                            raise eee

                        cnt57 += 1


                    CURLY_CLOSE267 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2959) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE267)


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
                    # 268:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:268:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:268:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:270:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set268 = None

        set268_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:270:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set268 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set268))

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
    # grammar/ShyRecognizerFrontend.g:272:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS269 = None
        NUMBER270 = None

        MINUS269_tree = None
        NUMBER270_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:272:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:272:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:272:13: ( MINUS )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == MINUS) :
                    alt59 = 1
                if alt59 == 1:
                    # grammar/ShyRecognizerFrontend.g:272:13: MINUS
                    pass 
                    MINUS269 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2998)
                    MINUS269_tree = self._adaptor.createWithPayload(MINUS269)
                    self._adaptor.addChild(root_0, MINUS269_tree)






                NUMBER270 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3002)
                NUMBER270_tree = self._adaptor.createWithPayload(NUMBER270)
                self._adaptor.addChild(root_0, NUMBER270_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:273:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS271 = None
        NUMBER272 = None
        DIVIDE273 = None
        NUMBER274 = None

        MINUS271_tree = None
        NUMBER272_tree = None
        DIVIDE273_tree = None
        NUMBER274_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:273:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:273:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:273:13: ( MINUS )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == MINUS) :
                    alt60 = 1
                if alt60 == 1:
                    # grammar/ShyRecognizerFrontend.g:273:13: MINUS
                    pass 
                    MINUS271 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3010)
                    MINUS271_tree = self._adaptor.createWithPayload(MINUS271)
                    self._adaptor.addChild(root_0, MINUS271_tree)






                NUMBER272 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3014)
                NUMBER272_tree = self._adaptor.createWithPayload(NUMBER272)
                self._adaptor.addChild(root_0, NUMBER272_tree)



                DIVIDE273 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3016)
                DIVIDE273_tree = self._adaptor.createWithPayload(DIVIDE273)
                self._adaptor.addChild(root_0, DIVIDE273_tree)



                NUMBER274 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3018)
                NUMBER274_tree = self._adaptor.createWithPayload(NUMBER274)
                self._adaptor.addChild(root_0, NUMBER274_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\22\1\7\4\uffff\1\7\1\10\1\33\1\10\1\15\1\10\1\33\2\uffff\1\10"
        )

    DFA18_max = DFA.unpack(
        u"\1\121\1\33\4\uffff\4\33\1\121\2\33\2\uffff\1\33"
        )

    DFA18_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\7\uffff\1\2\1\1\1\uffff"
        )

    DFA18_special = DFA.unpack(
        u"\20\uffff"
        )


    DFA18_transition = [
        DFA.unpack(u"\1\3\1\1\1\2\2\uffff\1\3\3\uffff\1\3\63\uffff\1\4\1"
        u"\uffff\1\5"),
        DFA.unpack(u"\2\3\11\uffff\1\7\1\6\3\uffff\1\10\2\uffff\1\12\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\3\11\uffff\1\7\1\6\3\uffff\1\10\2\uffff\1\12\1\11"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\13\3\uffff\1\10\2\uffff\1\12\1"
        u"\11"),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\3\5\uffff\1\14\3\uffff\1\7\1\13\3\uffff\1\10\2\uffff"
        u"\1\12\1\11"),
        DFA.unpack(u"\1\16\4\uffff\3\16\1\15\1\uffff\1\16\3\uffff\1\16\63"
        u"\uffff\1\16\1\uffff\1\16"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\13\3\uffff\1\10\2\uffff\1\12\1"
        u"\11"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\13\3\uffff\1\10\2\uffff\1\12\1"
        u"\11")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\1\22\1\7\1\10\1\33\1\10\1\22\1\23\1\10\1\33\4\uffff\1\10"
        )

    DFA30_max = DFA.unpack(
        u"\6\33\1\32\2\33\4\uffff\1\33"
        )

    DFA30_accept = DFA.unpack(
        u"\11\uffff\1\2\1\1\1\4\1\3\1\uffff"
        )

    DFA30_special = DFA.unpack(
        u"\16\uffff"
        )


    DFA30_transition = [
        DFA.unpack(u"\1\2\1\1\3\uffff\1\3\3\uffff\1\4"),
        DFA.unpack(u"\1\5\1\6\11\uffff\1\2\1\1\3\uffff\1\3\3\uffff\1\4"),
        DFA.unpack(u"\1\6\11\uffff\1\2\1\7\3\uffff\1\3\3\uffff\1\4"),
        DFA.unpack(u"\1\4"),
        DFA.unpack(u"\1\6\5\uffff\1\10\3\uffff\1\2\1\7\3\uffff\1\3\3\uffff"
        u"\1\4"),
        DFA.unpack(u"\2\12\3\uffff\1\12\2\uffff\1\11\1\12"),
        DFA.unpack(u"\1\14\6\uffff\1\13"),
        DFA.unpack(u"\1\6\11\uffff\1\2\1\7\3\uffff\1\3\3\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\11\uffff\1\2\1\7\3\uffff\1\3\3\uffff\1\4")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\1\23\3\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA38_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\uffff\1\33\1\uffff\1\33"
        )

    DFA38_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA38_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA38_transition = [
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

    # class definition for DFA #38

    class DFA38(DFA):
        pass


    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA39_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA39_min = DFA.unpack(
        u"\1\23\3\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA39_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\33\2\uffff\1\33"
        )

    DFA39_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA39_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA39_transition = [
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

    # class definition for DFA #39

    class DFA39(DFA):
        pass


    # lookup tables for DFA #51

    DFA51_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA51_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA51_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA51_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\116\1\115\2\uffff\1\32\1\115\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA51_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA51_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA51_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1\6\uffff\1\3"),
        DFA.unpack(u"\1\1\6\uffff\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\6\5\uffff\1\6\1\uffff\1\7\1\6\1\uffff"
        u"\1\6\3\uffff\1\6\6\uffff\1\6\50\uffff\1\6\1\uffff\1\6"),
        DFA.unpack(u"\1\10\7\uffff\1\11\71\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\14\7\uffff\1\11\71\uffff\1\11"),
        DFA.unpack(u"\1\12\6\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\17\6\uffff\1\20"),
        DFA.unpack(u"\1\21\5\uffff\1\17"),
        DFA.unpack(u"\1\4")
    ]

    # class definition for DFA #51

    class DFA51(DFA):
        pass


    # lookup tables for DFA #56

    DFA56_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA56_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA56_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA56_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\115\1\32\1\115\2\uffff\1\32"
        )

    DFA56_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA56_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA56_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\7\uffff\1\5\71\uffff\1\5"),
        DFA.unpack(u"\1\6\6\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\71\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\6\uffff\1\7")
    ]

    # class definition for DFA #56

    class DFA56(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 22, 24, 35, 76, 78])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 22, 24, 35, 76, 78])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 22, 24, 35, 76, 78])
    FOLLOW_types_in_start94 = frozenset([1, 9, 22, 24, 35, 76, 78])
    FOLLOW_messages_in_start98 = frozenset([1, 9, 22, 24, 35, 76, 78])
    FOLLOW_vars_in_start102 = frozenset([1, 9, 22, 24, 35, 76, 78])
    FOLLOW_MODULE_in_module121 = frozenset([19])
    FOLLOW_ID_in_module123 = frozenset([26])
    FOLLOW_NEWLINE_in_module125 = frozenset([21])
    FOLLOW_INDENT_in_module127 = frozenset([26])
    FOLLOW_NEWLINE_in_module129 = frozenset([13, 25, 30, 31, 34])
    FOLLOW_module_queue_in_module139 = frozenset([13, 30, 31, 34])
    FOLLOW_proc_in_module151 = frozenset([13, 30, 31, 34])
    FOLLOW_receive_in_module163 = frozenset([13, 31, 34])
    FOLLOW_request_in_module175 = frozenset([13, 34])
    FOLLOW_DEDENT_in_module187 = frozenset([26])
    FOLLOW_NEWLINE_in_module189 = frozenset([1])
    FOLLOW_MODULE_QUEUE_in_module_queue319 = frozenset([19])
    FOLLOW_ID_in_module_queue321 = frozenset([26])
    FOLLOW_NEWLINE_in_module_queue323 = frozenset([1])
    FOLLOW_STATELESS_in_stateless361 = frozenset([19])
    FOLLOW_ID_in_stateless363 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless365 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless369 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless371 = frozenset([30])
    FOLLOW_proc_in_stateless373 = frozenset([13, 30])
    FOLLOW_DEDENT_in_stateless377 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless379 = frozenset([1])
    FOLLOW_REQUEST_in_request425 = frozenset([19])
    FOLLOW_ID_in_request427 = frozenset([26])
    FOLLOW_NEWLINE_in_request429 = frozenset([1])
    FOLLOW_REQUEST_in_request458 = frozenset([19])
    FOLLOW_ID_in_request460 = frozenset([26])
    FOLLOW_NEWLINE_in_request462 = frozenset([21])
    FOLLOW_INDENT_in_request464 = frozenset([26])
    FOLLOW_NEWLINE_in_request466 = frozenset([13, 28, 78])
    FOLLOW_local_vars_in_request480 = frozenset([13, 28])
    FOLLOW_local_ops_in_request484 = frozenset([13])
    FOLLOW_DEDENT_in_request496 = frozenset([26])
    FOLLOW_NEWLINE_in_request498 = frozenset([1])
    FOLLOW_RECEIVE_in_receive544 = frozenset([19])
    FOLLOW_ID_in_receive546 = frozenset([26])
    FOLLOW_NEWLINE_in_receive548 = frozenset([1])
    FOLLOW_RECEIVE_in_receive577 = frozenset([19])
    FOLLOW_ID_in_receive579 = frozenset([26])
    FOLLOW_NEWLINE_in_receive581 = frozenset([21])
    FOLLOW_INDENT_in_receive583 = frozenset([26])
    FOLLOW_NEWLINE_in_receive585 = frozenset([13, 28, 78])
    FOLLOW_local_vars_in_receive599 = frozenset([13, 28])
    FOLLOW_local_ops_in_receive603 = frozenset([13])
    FOLLOW_DEDENT_in_receive615 = frozenset([26])
    FOLLOW_NEWLINE_in_receive617 = frozenset([1])
    FOLLOW_PROC_in_proc663 = frozenset([19])
    FOLLOW_ID_in_proc665 = frozenset([26])
    FOLLOW_NEWLINE_in_proc667 = frozenset([1])
    FOLLOW_PROC_in_proc696 = frozenset([19])
    FOLLOW_ID_in_proc698 = frozenset([26])
    FOLLOW_NEWLINE_in_proc700 = frozenset([21])
    FOLLOW_INDENT_in_proc702 = frozenset([26])
    FOLLOW_NEWLINE_in_proc704 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_proc706 = frozenset([13])
    FOLLOW_DEDENT_in_proc708 = frozenset([26])
    FOLLOW_NEWLINE_in_proc710 = frozenset([1])
    FOLLOW_PROC_in_proc741 = frozenset([19])
    FOLLOW_ID_in_proc743 = frozenset([26])
    FOLLOW_NEWLINE_in_proc745 = frozenset([21])
    FOLLOW_INDENT_in_proc747 = frozenset([26])
    FOLLOW_NEWLINE_in_proc749 = frozenset([6, 13, 28, 78])
    FOLLOW_proc_args_in_proc763 = frozenset([13, 28, 78])
    FOLLOW_local_vars_in_proc767 = frozenset([13, 28])
    FOLLOW_local_ops_in_proc771 = frozenset([13])
    FOLLOW_DEDENT_in_proc783 = frozenset([26])
    FOLLOW_NEWLINE_in_proc785 = frozenset([1])
    FOLLOW_ARGS_in_proc_args835 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args837 = frozenset([1])
    FOLLOW_VARS_in_local_vars866 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_local_vars868 = frozenset([1])
    FOLLOW_OPS_in_local_ops897 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops899 = frozenset([21])
    FOLLOW_INDENT_in_local_ops901 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops903 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_local_ops905 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops907 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops909 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement940 = frozenset([26])
    FOLLOW_NEWLINE_in_statement942 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement968 = frozenset([1])
    FOLLOW_statement_if_in_statement978 = frozenset([1])
    FOLLOW_statement_assign_in_statement988 = frozenset([1])
    FOLLOW_statement_while_in_statement998 = frozenset([1])
    FOLLOW_statement_with_in_statement1008 = frozenset([1])
    FOLLOW_statement_in_statements1027 = frozenset([1, 18, 19, 20, 23, 27, 79, 81])
    FOLLOW_WITH_in_statement_with1069 = frozenset([19])
    FOLLOW_ID_in_statement_with1071 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1073 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1083 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1085 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_with1087 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1089 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1091 = frozenset([1])
    FOLLOW_ID_in_statement_assign1131 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1135 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign1137 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign1141 = frozenset([1])
    FOLLOW_ID_in_statement_assign1194 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1198 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1200 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1202 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1204 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign1216 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign1220 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_assign1226 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1228 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1281 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1285 = frozenset([19])
    FOLLOW_ID_in_statement_assign1287 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1291 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1344 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1348 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1350 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1352 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1354 = frozenset([19])
    FOLLOW_ID_in_statement_assign1366 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1370 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1376 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1378 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1440 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1442 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1444 = frozenset([15])
    FOLLOW_DO_in_statement_while1448 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1450 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1464 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1466 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_while1468 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1470 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1472 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1512 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1522 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1534 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1642 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1644 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1676 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1678 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1710 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1712 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1716 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1718 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1732 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1734 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_elif_body1736 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1738 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1740 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1780 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1782 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1796 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1798 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_else1800 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1802 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1804 = frozenset([1])
    FOLLOW_condition_call_in_condition1842 = frozenset([1])
    FOLLOW_ANY_in_condition1871 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1873 = frozenset([1])
    FOLLOW_ALL_in_condition1902 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1904 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1942 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1952 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1954 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1956 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1958 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1962 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1964 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1998 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call2008 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line2027 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line2029 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2055 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2074 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line2076 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2120 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line2122 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2126 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2136 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2138 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line2142 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2144 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line2150 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2152 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2188 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value2205 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2215 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2225 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2235 = frozenset([1])
    FOLLOW_CONSTS_in_consts2254 = frozenset([19])
    FOLLOW_ID_in_consts2256 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2258 = frozenset([21])
    FOLLOW_INDENT_in_consts2268 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2270 = frozenset([19])
    FOLLOW_consts_items_in_consts2272 = frozenset([13])
    FOLLOW_DEDENT_in_consts2274 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2276 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2308 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2324 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2326 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2328 = frozenset([1])
    FOLLOW_ID_in_consts_item2350 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2352 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2354 = frozenset([1])
    FOLLOW_ID_in_consts_item2376 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2378 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2380 = frozenset([1])
    FOLLOW_TYPES_in_types2411 = frozenset([19])
    FOLLOW_ID_in_types2413 = frozenset([26])
    FOLLOW_NEWLINE_in_types2415 = frozenset([21])
    FOLLOW_INDENT_in_types2425 = frozenset([26])
    FOLLOW_NEWLINE_in_types2427 = frozenset([19])
    FOLLOW_types_item_in_types2429 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2433 = frozenset([26])
    FOLLOW_NEWLINE_in_types2435 = frozenset([1])
    FOLLOW_ID_in_types_item2469 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2471 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2498 = frozenset([19])
    FOLLOW_ID_in_messages2500 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2502 = frozenset([21])
    FOLLOW_INDENT_in_messages2512 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2514 = frozenset([19])
    FOLLOW_messages_item_in_messages2516 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2520 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2522 = frozenset([1])
    FOLLOW_ID_in_messages_item2556 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2558 = frozenset([1])
    FOLLOW_VARS_in_vars2585 = frozenset([19])
    FOLLOW_ID_in_vars2587 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars2589 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2628 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2630 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints2654 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2666 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2668 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2672 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2674 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2680 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2682 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2710 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2712 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2724 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2726 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2730 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2732 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2738 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2740 = frozenset([1])
    FOLLOW_ID_in_attr_hint2777 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2818 = frozenset([19])
    FOLLOW_ID_in_attr_hint2820 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2860 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2862 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2864 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2866 = frozenset([19])
    FOLLOW_ID_in_attr_hint2870 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2874 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2880 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2927 = frozenset([19])
    FOLLOW_ID_in_hint2929 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2931 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2951 = frozenset([19])
    FOLLOW_ID_in_hint2953 = frozenset([19, 77])
    FOLLOW_hint_arg_in_hint2955 = frozenset([11, 19, 77])
    FOLLOW_CURLY_CLOSE_in_hint2959 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2998 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3002 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3010 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3014 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3016 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3018 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
