# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-02 20:31:50

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
TRACE=37
TREE_ARBITRARY_TOKEN=38
TREE_ATTR=39
TREE_ATTRS_HINTS=40
TREE_ATTR_HINT=41
TREE_CONDITION_ALL=42
TREE_CONDITION_ANY=43
TREE_CONSTS=44
TREE_COPY=45
TREE_COPY_PASTE=46
TREE_EXPRESSION=47
TREE_HINT=48
TREE_HINT_NONE=49
TREE_LOCAL_VARS=50
TREE_MESSAGES=51
TREE_MESSAGES_ITEM=52
TREE_MESSAGES_ITEM_RECEIVE=53
TREE_MESSAGES_ITEM_REPLY=54
TREE_MESSAGES_ITEM_REQUEST=55
TREE_MODULE=56
TREE_MODULE_QUEUE=57
TREE_NUM_FRACT=58
TREE_NUM_WHOLE=59
TREE_PASTE=60
TREE_PASTE_REPLACE=61
TREE_PASTE_WITH=62
TREE_PROC=63
TREE_PROC_ARGS=64
TREE_RECEIVE=65
TREE_REQUEST=66
TREE_STATELESS=67
TREE_STATEMENTS=68
TREE_STATEMENT_ASSIGN=69
TREE_STATEMENT_ASSIGN_TO=70
TREE_STATEMENT_CALL=71
TREE_STATEMENT_ELIF=72
TREE_STATEMENT_ELSE=73
TREE_STATEMENT_IF=74
TREE_STATEMENT_WHILE=75
TREE_STATEMENT_WITH=76
TREE_TRACE=77
TREE_TYPES=78
TREE_TYPES_ITEM=79
TREE_VARS=80
TYPES=81
UNDERSCORE=82
VARS=83
WHILE=84
WHITESPACE=85
WITH=86

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "RECEIVE", "REPLACE", "REPLY", 
    "REQUEST", "STATELESS", "STRING", "TRACE", "TREE_ARBITRARY_TOKEN", "TREE_ATTR", 
    "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", "TREE_CONDITION_ALL", "TREE_CONDITION_ANY", 
    "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", "TREE_EXPRESSION", "TREE_HINT", 
    "TREE_HINT_NONE", "TREE_LOCAL_VARS", "TREE_MESSAGES", "TREE_MESSAGES_ITEM", 
    "TREE_MESSAGES_ITEM_RECEIVE", "TREE_MESSAGES_ITEM_REPLY", "TREE_MESSAGES_ITEM_REQUEST", 
    "TREE_MODULE", "TREE_MODULE_QUEUE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", 
    "TREE_PASTE", "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", 
    "TREE_PROC_ARGS", "TREE_RECEIVE", "TREE_REQUEST", "TREE_STATELESS", 
    "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", 
    "TREE_STATEMENT_CALL", "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", 
    "TREE_STATEMENT_IF", "TREE_STATEMENT_WHILE", "TREE_STATEMENT_WITH", 
    "TREE_TRACE", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", 
    "UNDERSCORE", "VARS", "WHILE", "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

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

        self.dfa41 = self.DFA41(
            self, 41,
            eot = self.DFA41_eot,
            eof = self.DFA41_eof,
            min = self.DFA41_min,
            max = self.DFA41_max,
            accept = self.DFA41_accept,
            special = self.DFA41_special,
            transition = self.DFA41_transition
            )

        self.dfa42 = self.DFA42(
            self, 42,
            eot = self.DFA42_eot,
            eof = self.DFA42_eof,
            min = self.DFA42_min,
            max = self.DFA42_max,
            accept = self.DFA42_accept,
            special = self.DFA42_special,
            transition = self.DFA42_transition
            )

        self.dfa52 = self.DFA52(
            self, 52,
            eot = self.DFA52_eot,
            eof = self.DFA52_eof,
            min = self.DFA52_min,
            max = self.DFA52_max,
            accept = self.DFA52_accept,
            special = self.DFA52_special,
            transition = self.DFA52_transition
            )

        self.dfa55 = self.DFA55(
            self, 55,
            eot = self.DFA55_eot,
            eof = self.DFA55_eof,
            min = self.DFA55_min,
            max = self.DFA55_max,
            accept = self.DFA55_accept,
            special = self.DFA55_special,
            transition = self.DFA55_transition
            )

        self.dfa60 = self.DFA60(
            self, 60,
            eot = self.DFA60_eot,
            eof = self.DFA60_eof,
            min = self.DFA60_min,
            max = self.DFA60_max,
            accept = self.DFA60_accept,
            special = self.DFA60_special,
            transition = self.DFA60_transition
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
    # grammar/ShyRecognizerFrontend.g:24:1: start : ( module | stateless | consts | types | messages | vars | trace )* ;
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

        trace7 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:24:7: ( ( module | stateless | consts | types | messages | vars | trace )* )
                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types | messages | vars | trace )*
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:24:9: ( module | stateless | consts | types | messages | vars | trace )*
                while True: #loop1
                    alt1 = 8
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
                    elif LA1 == TRACE:
                        alt1 = 7

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



                    elif alt1 == 7:
                        # grammar/ShyRecognizerFrontend.g:24:67: trace
                        pass 
                        self._state.following.append(self.FOLLOW_trace_in_start106)
                        trace7 = self.trace()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, trace7.tree)



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

        MODULE8 = None
        ID9 = None
        NEWLINE10 = None
        INDENT11 = None
        NEWLINE12 = None
        DEDENT17 = None
        NEWLINE18 = None
        module_queue13 = None

        proc14 = None

        receive15 = None

        request16 = None


        MODULE8_tree = None
        ID9_tree = None
        NEWLINE10_tree = None
        INDENT11_tree = None
        NEWLINE12_tree = None
        DEDENT17_tree = None
        NEWLINE18_tree = None
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
                MODULE8 = self.match(self.input, MODULE, self.FOLLOW_MODULE_in_module125) 
                stream_MODULE.add(MODULE8)


                ID9 = self.match(self.input, ID, self.FOLLOW_ID_in_module127) 
                stream_ID.add(ID9)


                NEWLINE10 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module129) 
                stream_NEWLINE.add(NEWLINE10)


                INDENT11 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_module131) 
                stream_INDENT.add(INDENT11)


                NEWLINE12 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module133) 
                stream_NEWLINE.add(NEWLINE12)


                # grammar/ShyRecognizerFrontend.g:28:9: ( module_queue )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == MODULE_QUEUE) :
                    alt2 = 1
                if alt2 == 1:
                    # grammar/ShyRecognizerFrontend.g:28:9: module_queue
                    pass 
                    self._state.following.append(self.FOLLOW_module_queue_in_module143)
                    module_queue13 = self.module_queue()

                    self._state.following.pop()
                    stream_module_queue.add(module_queue13.tree)





                # grammar/ShyRecognizerFrontend.g:29:9: ( proc )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == PROC) :
                        alt3 = 1


                    if alt3 == 1:
                        # grammar/ShyRecognizerFrontend.g:29:9: proc
                        pass 
                        self._state.following.append(self.FOLLOW_proc_in_module155)
                        proc14 = self.proc()

                        self._state.following.pop()
                        stream_proc.add(proc14.tree)



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
                        self._state.following.append(self.FOLLOW_receive_in_module167)
                        receive15 = self.receive()

                        self._state.following.pop()
                        stream_receive.add(receive15.tree)



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
                        self._state.following.append(self.FOLLOW_request_in_module179)
                        request16 = self.request()

                        self._state.following.pop()
                        stream_request.add(request16.tree)



                    else:
                        break #loop5


                DEDENT17 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_module191) 
                stream_DEDENT.add(DEDENT17)


                NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module193) 
                stream_NEWLINE.add(NEWLINE18)


                # AST Rewrite
                # elements: module_queue, request, ID, receive, proc
                # token labels: 
                # rule labels: retval
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

        MODULE_QUEUE19 = None
        ID20 = None
        NEWLINE21 = None

        MODULE_QUEUE19_tree = None
        ID20_tree = None
        NEWLINE21_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE_QUEUE = RewriteRuleTokenStream(self._adaptor, "token MODULE_QUEUE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:42:5: ( MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerFrontend.g:42:9: MODULE_QUEUE ID NEWLINE
                pass 
                MODULE_QUEUE19 = self.match(self.input, MODULE_QUEUE, self.FOLLOW_MODULE_QUEUE_in_module_queue323) 
                stream_MODULE_QUEUE.add(MODULE_QUEUE19)


                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue325) 
                stream_ID.add(ID20)


                NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module_queue327) 
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


    class trace_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.trace_return, self).__init__()

            self.tree = None





    # $ANTLR start "trace"
    # grammar/ShyRecognizerFrontend.g:46:1: trace : TRACE ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_TRACE ID ( proc )* ) ;
    def trace(self, ):
        retval = self.trace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TRACE22 = None
        ID23 = None
        NEWLINE24 = None
        INDENT25 = None
        NEWLINE26 = None
        DEDENT28 = None
        NEWLINE29 = None
        proc27 = None


        TRACE22_tree = None
        ID23_tree = None
        NEWLINE24_tree = None
        INDENT25_tree = None
        NEWLINE26_tree = None
        DEDENT28_tree = None
        NEWLINE29_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_TRACE = RewriteRuleTokenStream(self._adaptor, "token TRACE")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:47:5: ( TRACE ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_TRACE ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:47:9: TRACE ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                TRACE22 = self.match(self.input, TRACE, self.FOLLOW_TRACE_in_trace365) 
                stream_TRACE.add(TRACE22)


                ID23 = self.match(self.input, ID, self.FOLLOW_ID_in_trace367) 
                stream_ID.add(ID23)


                NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_trace369) 
                stream_NEWLINE.add(NEWLINE24)


                # grammar/ShyRecognizerFrontend.g:47:26: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == INDENT) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerFrontend.g:47:28: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT25 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_trace373) 
                    stream_INDENT.add(INDENT25)


                    NEWLINE26 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_trace375) 
                    stream_NEWLINE.add(NEWLINE26)


                    # grammar/ShyRecognizerFrontend.g:47:43: ( proc )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == PROC) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyRecognizerFrontend.g:47:43: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_trace377)
                            proc27 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc27.tree)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT28 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_trace381) 
                    stream_DEDENT.add(DEDENT28)


                    NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_trace383) 
                    stream_NEWLINE.add(NEWLINE29)





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
                # 48:9: -> ^( TREE_TRACE ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:48:13: ^( TREE_TRACE ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TRACE, "TREE_TRACE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:48:30: ( proc )*
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

    # $ANTLR end "trace"


    class stateless_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.stateless_return, self).__init__()

            self.tree = None





    # $ANTLR start "stateless"
    # grammar/ShyRecognizerFrontend.g:51:1: stateless : STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS30 = None
        ID31 = None
        NEWLINE32 = None
        INDENT33 = None
        NEWLINE34 = None
        DEDENT36 = None
        NEWLINE37 = None
        proc35 = None


        STATELESS30_tree = None
        ID31_tree = None
        NEWLINE32_tree = None
        INDENT33_tree = None
        NEWLINE34_tree = None
        DEDENT36_tree = None
        NEWLINE37_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:52:5: ( STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:52:9: STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                STATELESS30 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless429) 
                stream_STATELESS.add(STATELESS30)


                ID31 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless431) 
                stream_ID.add(ID31)


                NEWLINE32 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless433) 
                stream_NEWLINE.add(NEWLINE32)


                # grammar/ShyRecognizerFrontend.g:52:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == INDENT) :
                    alt9 = 1
                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:52:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT33 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless437) 
                    stream_INDENT.add(INDENT33)


                    NEWLINE34 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless439) 
                    stream_NEWLINE.add(NEWLINE34)


                    # grammar/ShyRecognizerFrontend.g:52:47: ( proc )+
                    cnt8 = 0
                    while True: #loop8
                        alt8 = 2
                        LA8_0 = self.input.LA(1)

                        if (LA8_0 == PROC) :
                            alt8 = 1


                        if alt8 == 1:
                            # grammar/ShyRecognizerFrontend.g:52:47: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless441)
                            proc35 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc35.tree)



                        else:
                            if cnt8 >= 1:
                                break #loop8

                            eee = EarlyExitException(8, self.input)
                            raise eee

                        cnt8 += 1


                    DEDENT36 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless445) 
                    stream_DEDENT.add(DEDENT36)


                    NEWLINE37 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless447) 
                    stream_NEWLINE.add(NEWLINE37)





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
                # 53:9: -> ^( TREE_STATELESS ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:53:13: ^( TREE_STATELESS ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:53:34: ( proc )*
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
    # grammar/ShyRecognizerFrontend.g:56:1: request : ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID statement -> ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) );
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REQUEST38 = None
        ID39 = None
        NEWLINE40 = None
        REQUEST41 = None
        ID42 = None
        REQUEST44 = None
        ID45 = None
        NEWLINE46 = None
        INDENT47 = None
        NEWLINE48 = None
        DEDENT50 = None
        NEWLINE51 = None
        REQUEST52 = None
        ID53 = None
        NEWLINE54 = None
        INDENT55 = None
        NEWLINE56 = None
        DEDENT59 = None
        NEWLINE60 = None
        statement43 = None

        statements49 = None

        local_vars57 = None

        local_ops58 = None


        REQUEST38_tree = None
        ID39_tree = None
        NEWLINE40_tree = None
        REQUEST41_tree = None
        ID42_tree = None
        REQUEST44_tree = None
        ID45_tree = None
        NEWLINE46_tree = None
        INDENT47_tree = None
        NEWLINE48_tree = None
        DEDENT50_tree = None
        NEWLINE51_tree = None
        REQUEST52_tree = None
        ID53_tree = None
        NEWLINE54_tree = None
        INDENT55_tree = None
        NEWLINE56_tree = None
        DEDENT59_tree = None
        NEWLINE60_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:57:5: ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID statement -> ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) )
                alt12 = 4
                LA12_0 = self.input.LA(1)

                if (LA12_0 == REQUEST) :
                    LA12_1 = self.input.LA(2)

                    if (LA12_1 == ID) :
                        LA12_2 = self.input.LA(3)

                        if (LA12_2 == NEWLINE) :
                            LA12_3 = self.input.LA(4)

                            if (LA12_3 == INDENT) :
                                LA12_5 = self.input.LA(5)

                                if (LA12_5 == NEWLINE) :
                                    LA12_7 = self.input.LA(6)

                                    if ((EXPRESSION <= LA12_7 <= IF) or LA12_7 == MINUS or LA12_7 == NUMBER or LA12_7 == STRING or LA12_7 == WHILE or LA12_7 == WITH) :
                                        alt12 = 3
                                    elif (LA12_7 == DEDENT or LA12_7 == OPS or LA12_7 == VARS) :
                                        alt12 = 4
                                    else:
                                        nvae = NoViableAltException("", 12, 7, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 12, 5, self.input)

                                    raise nvae


                            elif (LA12_3 == DEDENT or LA12_3 == REQUEST) :
                                alt12 = 1
                            else:
                                nvae = NoViableAltException("", 12, 3, self.input)

                                raise nvae


                        elif ((EXPRESSION <= LA12_2 <= IF) or LA12_2 == MINUS or LA12_2 == NUMBER or LA12_2 == STRING or LA12_2 == WHILE or LA12_2 == WITH) :
                            alt12 = 2
                        else:
                            nvae = NoViableAltException("", 12, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 12, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # grammar/ShyRecognizerFrontend.g:57:9: REQUEST ID NEWLINE
                    pass 
                    REQUEST38 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request493) 
                    stream_REQUEST.add(REQUEST38)


                    ID39 = self.match(self.input, ID, self.FOLLOW_ID_in_request495) 
                    stream_ID.add(ID39)


                    NEWLINE40 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request497) 
                    stream_NEWLINE.add(NEWLINE40)


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
                    # 58:9: -> ^( TREE_REQUEST ID )
                    # grammar/ShyRecognizerFrontend.g:58:13: ^( TREE_REQUEST ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 2:
                    # grammar/ShyRecognizerFrontend.g:59:9: REQUEST ID statement
                    pass 
                    REQUEST41 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request526) 
                    stream_REQUEST.add(REQUEST41)


                    ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_request528) 
                    stream_ID.add(ID42)


                    self._state.following.append(self.FOLLOW_statement_in_request530)
                    statement43 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement43.tree)


                    # AST Rewrite
                    # elements: statement, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 60:9: -> ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) )
                    # grammar/ShyRecognizerFrontend.g:60:13: ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:60:32: ^( TREE_STATEMENTS statement )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                    , root_2)

                    self._adaptor.addChild(root_2, stream_statement.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 3:
                    # grammar/ShyRecognizerFrontend.g:61:9: REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    REQUEST44 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request567) 
                    stream_REQUEST.add(REQUEST44)


                    ID45 = self.match(self.input, ID, self.FOLLOW_ID_in_request569) 
                    stream_ID.add(ID45)


                    NEWLINE46 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request571) 
                    stream_NEWLINE.add(NEWLINE46)


                    INDENT47 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request573) 
                    stream_INDENT.add(INDENT47)


                    NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request575) 
                    stream_NEWLINE.add(NEWLINE48)


                    self._state.following.append(self.FOLLOW_statements_in_request577)
                    statements49 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements49.tree)


                    DEDENT50 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request579) 
                    stream_DEDENT.add(DEDENT50)


                    NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request581) 
                    stream_NEWLINE.add(NEWLINE51)


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
                    # 62:9: -> ^( TREE_REQUEST ID statements )
                    # grammar/ShyRecognizerFrontend.g:62:13: ^( TREE_REQUEST ID statements )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_statements.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt12 == 4:
                    # grammar/ShyRecognizerFrontend.g:63:9: REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    REQUEST52 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request612) 
                    stream_REQUEST.add(REQUEST52)


                    ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_request614) 
                    stream_ID.add(ID53)


                    NEWLINE54 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request616) 
                    stream_NEWLINE.add(NEWLINE54)


                    INDENT55 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request618) 
                    stream_INDENT.add(INDENT55)


                    NEWLINE56 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request620) 
                    stream_NEWLINE.add(NEWLINE56)


                    # grammar/ShyRecognizerFrontend.g:64:13: ( local_vars )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == VARS) :
                        alt10 = 1
                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:64:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_request634)
                        local_vars57 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars57.tree)





                    # grammar/ShyRecognizerFrontend.g:64:26: ( local_ops )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == OPS) :
                        alt11 = 1
                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:64:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_request638)
                        local_ops58 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops58.tree)





                    DEDENT59 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request650) 
                    stream_DEDENT.add(DEDENT59)


                    NEWLINE60 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request652) 
                    stream_NEWLINE.add(NEWLINE60)


                    # AST Rewrite
                    # elements: ID, local_ops, local_vars
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 66:9: -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:66:13: ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
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

    # $ANTLR end "request"


    class receive_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.receive_return, self).__init__()

            self.tree = None





    # $ANTLR start "receive"
    # grammar/ShyRecognizerFrontend.g:69:1: receive : ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID statement -> ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) );
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECEIVE61 = None
        ID62 = None
        NEWLINE63 = None
        RECEIVE64 = None
        ID65 = None
        RECEIVE67 = None
        ID68 = None
        NEWLINE69 = None
        INDENT70 = None
        NEWLINE71 = None
        DEDENT73 = None
        NEWLINE74 = None
        RECEIVE75 = None
        ID76 = None
        NEWLINE77 = None
        INDENT78 = None
        NEWLINE79 = None
        DEDENT82 = None
        NEWLINE83 = None
        statement66 = None

        statements72 = None

        local_vars80 = None

        local_ops81 = None


        RECEIVE61_tree = None
        ID62_tree = None
        NEWLINE63_tree = None
        RECEIVE64_tree = None
        ID65_tree = None
        RECEIVE67_tree = None
        ID68_tree = None
        NEWLINE69_tree = None
        INDENT70_tree = None
        NEWLINE71_tree = None
        DEDENT73_tree = None
        NEWLINE74_tree = None
        RECEIVE75_tree = None
        ID76_tree = None
        NEWLINE77_tree = None
        INDENT78_tree = None
        NEWLINE79_tree = None
        DEDENT82_tree = None
        NEWLINE83_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_RECEIVE = RewriteRuleTokenStream(self._adaptor, "token RECEIVE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:70:5: ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID statement -> ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) )
                alt15 = 4
                LA15_0 = self.input.LA(1)

                if (LA15_0 == RECEIVE) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == ID) :
                        LA15_2 = self.input.LA(3)

                        if (LA15_2 == NEWLINE) :
                            LA15_3 = self.input.LA(4)

                            if (LA15_3 == INDENT) :
                                LA15_5 = self.input.LA(5)

                                if (LA15_5 == NEWLINE) :
                                    LA15_7 = self.input.LA(6)

                                    if ((EXPRESSION <= LA15_7 <= IF) or LA15_7 == MINUS or LA15_7 == NUMBER or LA15_7 == STRING or LA15_7 == WHILE or LA15_7 == WITH) :
                                        alt15 = 3
                                    elif (LA15_7 == DEDENT or LA15_7 == OPS or LA15_7 == VARS) :
                                        alt15 = 4
                                    else:
                                        nvae = NoViableAltException("", 15, 7, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 15, 5, self.input)

                                    raise nvae


                            elif (LA15_3 == DEDENT or LA15_3 == RECEIVE or LA15_3 == REQUEST) :
                                alt15 = 1
                            else:
                                nvae = NoViableAltException("", 15, 3, self.input)

                                raise nvae


                        elif ((EXPRESSION <= LA15_2 <= IF) or LA15_2 == MINUS or LA15_2 == NUMBER or LA15_2 == STRING or LA15_2 == WHILE or LA15_2 == WITH) :
                            alt15 = 2
                        else:
                            nvae = NoViableAltException("", 15, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 15, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:70:9: RECEIVE ID NEWLINE
                    pass 
                    RECEIVE61 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive698) 
                    stream_RECEIVE.add(RECEIVE61)


                    ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_receive700) 
                    stream_ID.add(ID62)


                    NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive702) 
                    stream_NEWLINE.add(NEWLINE63)


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
                    # 71:9: -> ^( TREE_RECEIVE ID )
                    # grammar/ShyRecognizerFrontend.g:71:13: ^( TREE_RECEIVE ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:72:9: RECEIVE ID statement
                    pass 
                    RECEIVE64 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive731) 
                    stream_RECEIVE.add(RECEIVE64)


                    ID65 = self.match(self.input, ID, self.FOLLOW_ID_in_receive733) 
                    stream_ID.add(ID65)


                    self._state.following.append(self.FOLLOW_statement_in_receive735)
                    statement66 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement66.tree)


                    # AST Rewrite
                    # elements: statement, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 73:9: -> ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) )
                    # grammar/ShyRecognizerFrontend.g:73:13: ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:73:32: ^( TREE_STATEMENTS statement )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                    , root_2)

                    self._adaptor.addChild(root_2, stream_statement.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 3:
                    # grammar/ShyRecognizerFrontend.g:74:9: RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    RECEIVE67 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive772) 
                    stream_RECEIVE.add(RECEIVE67)


                    ID68 = self.match(self.input, ID, self.FOLLOW_ID_in_receive774) 
                    stream_ID.add(ID68)


                    NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive776) 
                    stream_NEWLINE.add(NEWLINE69)


                    INDENT70 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive778) 
                    stream_INDENT.add(INDENT70)


                    NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive780) 
                    stream_NEWLINE.add(NEWLINE71)


                    self._state.following.append(self.FOLLOW_statements_in_receive782)
                    statements72 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements72.tree)


                    DEDENT73 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive784) 
                    stream_DEDENT.add(DEDENT73)


                    NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive786) 
                    stream_NEWLINE.add(NEWLINE74)


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
                    # 75:9: -> ^( TREE_RECEIVE ID statements )
                    # grammar/ShyRecognizerFrontend.g:75:13: ^( TREE_RECEIVE ID statements )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_statements.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 4:
                    # grammar/ShyRecognizerFrontend.g:76:9: RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    RECEIVE75 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive817) 
                    stream_RECEIVE.add(RECEIVE75)


                    ID76 = self.match(self.input, ID, self.FOLLOW_ID_in_receive819) 
                    stream_ID.add(ID76)


                    NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive821) 
                    stream_NEWLINE.add(NEWLINE77)


                    INDENT78 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive823) 
                    stream_INDENT.add(INDENT78)


                    NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive825) 
                    stream_NEWLINE.add(NEWLINE79)


                    # grammar/ShyRecognizerFrontend.g:77:13: ( local_vars )?
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == VARS) :
                        alt13 = 1
                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:77:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_receive839)
                        local_vars80 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars80.tree)





                    # grammar/ShyRecognizerFrontend.g:77:26: ( local_ops )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == OPS) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:77:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_receive843)
                        local_ops81 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops81.tree)





                    DEDENT82 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive855) 
                    stream_DEDENT.add(DEDENT82)


                    NEWLINE83 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive857) 
                    stream_NEWLINE.add(NEWLINE83)


                    # AST Rewrite
                    # elements: ID, local_ops, local_vars
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 79:9: -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:79:13: ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:79:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:79:45: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:82:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC84 = None
        ID85 = None
        NEWLINE86 = None
        PROC87 = None
        ID88 = None
        NEWLINE89 = None
        INDENT90 = None
        NEWLINE91 = None
        DEDENT93 = None
        NEWLINE94 = None
        PROC95 = None
        ID96 = None
        NEWLINE97 = None
        INDENT98 = None
        NEWLINE99 = None
        DEDENT103 = None
        NEWLINE104 = None
        statements92 = None

        proc_args100 = None

        local_vars101 = None

        local_ops102 = None


        PROC84_tree = None
        ID85_tree = None
        NEWLINE86_tree = None
        PROC87_tree = None
        ID88_tree = None
        NEWLINE89_tree = None
        INDENT90_tree = None
        NEWLINE91_tree = None
        DEDENT93_tree = None
        NEWLINE94_tree = None
        PROC95_tree = None
        ID96_tree = None
        NEWLINE97_tree = None
        INDENT98_tree = None
        NEWLINE99_tree = None
        DEDENT103_tree = None
        NEWLINE104_tree = None
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
                # grammar/ShyRecognizerFrontend.g:83:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) )
                alt19 = 3
                LA19_0 = self.input.LA(1)

                if (LA19_0 == PROC) :
                    LA19_1 = self.input.LA(2)

                    if (LA19_1 == ID) :
                        LA19_2 = self.input.LA(3)

                        if (LA19_2 == NEWLINE) :
                            LA19_3 = self.input.LA(4)

                            if (LA19_3 == INDENT) :
                                LA19_4 = self.input.LA(5)

                                if (LA19_4 == NEWLINE) :
                                    LA19_6 = self.input.LA(6)

                                    if ((EXPRESSION <= LA19_6 <= IF) or LA19_6 == MINUS or LA19_6 == NUMBER or LA19_6 == STRING or LA19_6 == WHILE or LA19_6 == WITH) :
                                        alt19 = 2
                                    elif (LA19_6 == ARGS or LA19_6 == DEDENT or LA19_6 == OPS or LA19_6 == VARS) :
                                        alt19 = 3
                                    else:
                                        nvae = NoViableAltException("", 19, 6, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 19, 4, self.input)

                                    raise nvae


                            elif (LA19_3 == DEDENT or (PROC <= LA19_3 <= RECEIVE) or LA19_3 == REQUEST) :
                                alt19 = 1
                            else:
                                nvae = NoViableAltException("", 19, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerFrontend.g:83:9: PROC ID NEWLINE
                    pass 
                    PROC84 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc903) 
                    stream_PROC.add(PROC84)


                    ID85 = self.match(self.input, ID, self.FOLLOW_ID_in_proc905) 
                    stream_ID.add(ID85)


                    NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc907) 
                    stream_NEWLINE.add(NEWLINE86)


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
                    # 84:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:84:13: ^( TREE_PROC ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt19 == 2:
                    # grammar/ShyRecognizerFrontend.g:85:9: PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    PROC87 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc936) 
                    stream_PROC.add(PROC87)


                    ID88 = self.match(self.input, ID, self.FOLLOW_ID_in_proc938) 
                    stream_ID.add(ID88)


                    NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc940) 
                    stream_NEWLINE.add(NEWLINE89)


                    INDENT90 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc942) 
                    stream_INDENT.add(INDENT90)


                    NEWLINE91 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc944) 
                    stream_NEWLINE.add(NEWLINE91)


                    self._state.following.append(self.FOLLOW_statements_in_proc946)
                    statements92 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements92.tree)


                    DEDENT93 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc948) 
                    stream_DEDENT.add(DEDENT93)


                    NEWLINE94 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc950) 
                    stream_NEWLINE.add(NEWLINE94)


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
                    # 86:9: -> ^( TREE_PROC ID statements )
                    # grammar/ShyRecognizerFrontend.g:86:13: ^( TREE_PROC ID statements )
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




                elif alt19 == 3:
                    # grammar/ShyRecognizerFrontend.g:87:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    PROC95 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc981) 
                    stream_PROC.add(PROC95)


                    ID96 = self.match(self.input, ID, self.FOLLOW_ID_in_proc983) 
                    stream_ID.add(ID96)


                    NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc985) 
                    stream_NEWLINE.add(NEWLINE97)


                    INDENT98 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc987) 
                    stream_INDENT.add(INDENT98)


                    NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc989) 
                    stream_NEWLINE.add(NEWLINE99)


                    # grammar/ShyRecognizerFrontend.g:88:13: ( proc_args )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ARGS) :
                        alt16 = 1
                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:88:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc1003)
                        proc_args100 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args100.tree)





                    # grammar/ShyRecognizerFrontend.g:88:25: ( local_vars )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == VARS) :
                        alt17 = 1
                    if alt17 == 1:
                        # grammar/ShyRecognizerFrontend.g:88:25: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_proc1007)
                        local_vars101 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars101.tree)





                    # grammar/ShyRecognizerFrontend.g:88:38: ( local_ops )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == OPS) :
                        alt18 = 1
                    if alt18 == 1:
                        # grammar/ShyRecognizerFrontend.g:88:38: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_proc1011)
                        local_ops102 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops102.tree)





                    DEDENT103 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc1023) 
                    stream_DEDENT.add(DEDENT103)


                    NEWLINE104 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc1025) 
                    stream_NEWLINE.add(NEWLINE104)


                    # AST Rewrite
                    # elements: local_ops, proc_args, local_vars, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 90:9: -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:90:13: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:90:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:90:41: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:90:54: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:93:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS105 = None
        attrs_hints106 = None


        ARGS105_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:94:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:94:9: ARGS attrs_hints
                pass 
                ARGS105 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args1075) 
                stream_ARGS.add(ARGS105)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args1077)
                attrs_hints106 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints106.tree)


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
                # 94:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:94:29: ^( TREE_PROC_ARGS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:97:1: local_vars : VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        retval = self.local_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS107 = None
        attrs_hints108 = None


        VARS107_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:98:5: ( VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:98:9: VARS attrs_hints
                pass 
                VARS107 = self.match(self.input, VARS, self.FOLLOW_VARS_in_local_vars1106) 
                stream_VARS.add(VARS107)


                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars1108)
                attrs_hints108 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints108.tree)


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
                # 98:26: -> ^( TREE_LOCAL_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:98:29: ^( TREE_LOCAL_VARS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:101:1: local_ops : ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements | OPS statement -> ^( TREE_STATEMENTS statement ) );
    def local_ops(self, ):
        retval = self.local_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS109 = None
        NEWLINE110 = None
        INDENT111 = None
        NEWLINE112 = None
        DEDENT114 = None
        NEWLINE115 = None
        OPS116 = None
        statements113 = None

        statement117 = None


        OPS109_tree = None
        NEWLINE110_tree = None
        INDENT111_tree = None
        NEWLINE112_tree = None
        DEDENT114_tree = None
        NEWLINE115_tree = None
        OPS116_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:102:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements | OPS statement -> ^( TREE_STATEMENTS statement ) )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == OPS) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == NEWLINE) :
                        alt20 = 1
                    elif ((EXPRESSION <= LA20_1 <= IF) or LA20_1 == MINUS or LA20_1 == NUMBER or LA20_1 == STRING or LA20_1 == WHILE or LA20_1 == WITH) :
                        alt20 = 2
                    else:
                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:102:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    OPS109 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops1137) 
                    stream_OPS.add(OPS109)


                    NEWLINE110 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1139) 
                    stream_NEWLINE.add(NEWLINE110)


                    INDENT111 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_local_ops1141) 
                    stream_INDENT.add(INDENT111)


                    NEWLINE112 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1143) 
                    stream_NEWLINE.add(NEWLINE112)


                    self._state.following.append(self.FOLLOW_statements_in_local_ops1145)
                    statements113 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements113.tree)


                    DEDENT114 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_local_ops1147) 
                    stream_DEDENT.add(DEDENT114)


                    NEWLINE115 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1149) 
                    stream_NEWLINE.add(NEWLINE115)


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
                    # 103:9: -> statements
                    self._adaptor.addChild(root_0, stream_statements.nextTree())




                    retval.tree = root_0




                elif alt20 == 2:
                    # grammar/ShyRecognizerFrontend.g:104:9: OPS statement
                    pass 
                    OPS116 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops1171) 
                    stream_OPS.add(OPS116)


                    self._state.following.append(self.FOLLOW_statement_in_local_ops1173)
                    statement117 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement117.tree)


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
                    # 105:9: -> ^( TREE_STATEMENTS statement )
                    # grammar/ShyRecognizerFrontend.g:105:13: ^( TREE_STATEMENTS statement )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_statement.nextTree())

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

    # $ANTLR end "local_ops"


    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement"
    # grammar/ShyRecognizerFrontend.g:108:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE119 = None
        statement_call_single_line118 = None

        statement_call_multi_line120 = None

        statement_if121 = None

        statement_assign122 = None

        statement_while123 = None

        statement_with124 = None


        NEWLINE119_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:109:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt21 = 6
                alt21 = self.dfa21.predict(self.input)
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:109:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement1211)
                    statement_call_single_line118 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line118.tree)


                    NEWLINE119 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement1213) 
                    stream_NEWLINE.add(NEWLINE119)


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
                    # 110:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt21 == 2:
                    # grammar/ShyRecognizerFrontend.g:111:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement1239)
                    statement_call_multi_line120 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line120.tree)



                elif alt21 == 3:
                    # grammar/ShyRecognizerFrontend.g:112:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement1249)
                    statement_if121 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if121.tree)



                elif alt21 == 4:
                    # grammar/ShyRecognizerFrontend.g:113:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1259)
                    statement_assign122 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign122.tree)



                elif alt21 == 5:
                    # grammar/ShyRecognizerFrontend.g:114:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement1269)
                    statement_while123 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while123.tree)



                elif alt21 == 6:
                    # grammar/ShyRecognizerFrontend.g:115:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement1279)
                    statement_with124 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with124.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:118:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement125 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:119:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:119:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:119:9: ( statement )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= IF) or LA22_0 == MINUS or LA22_0 == NUMBER or LA22_0 == STRING or LA22_0 == WHILE or LA22_0 == WITH) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerFrontend.g:119:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1298)
                        statement125 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement125.tree)



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1


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
                # 120:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:120:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:120:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:123:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH126 = None
        ID127 = None
        NEWLINE128 = None
        INDENT129 = None
        NEWLINE130 = None
        DEDENT132 = None
        NEWLINE133 = None
        statements131 = None


        WITH126_tree = None
        ID127_tree = None
        NEWLINE128_tree = None
        INDENT129_tree = None
        NEWLINE130_tree = None
        DEDENT132_tree = None
        NEWLINE133_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:124:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:124:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH126 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1340) 
                stream_WITH.add(WITH126)


                ID127 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1342) 
                stream_ID.add(ID127)


                NEWLINE128 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1344) 
                stream_NEWLINE.add(NEWLINE128)


                INDENT129 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1354) 
                stream_INDENT.add(INDENT129)


                NEWLINE130 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1356) 
                stream_NEWLINE.add(NEWLINE130)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1358)
                statements131 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements131.tree)


                DEDENT132 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1360) 
                stream_DEDENT.add(DEDENT132)


                NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1362) 
                stream_NEWLINE.add(NEWLINE133)


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
                # 126:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:126:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:129:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID134 = None
        ARROW_LEFT135 = None
        NEWLINE137 = None
        ID138 = None
        ARROW_LEFT139 = None
        NEWLINE140 = None
        INDENT141 = None
        NEWLINE142 = None
        NEWLINE144 = None
        DEDENT145 = None
        NEWLINE146 = None
        ARROW_RIGHT148 = None
        ID149 = None
        NEWLINE150 = None
        ARROW_RIGHT152 = None
        NEWLINE153 = None
        INDENT154 = None
        NEWLINE155 = None
        ID156 = None
        NEWLINE157 = None
        DEDENT158 = None
        NEWLINE159 = None
        arbitrary_value136 = None

        arbitrary_value143 = None

        arbitrary_value147 = None

        arbitrary_value151 = None


        ID134_tree = None
        ARROW_LEFT135_tree = None
        NEWLINE137_tree = None
        ID138_tree = None
        ARROW_LEFT139_tree = None
        NEWLINE140_tree = None
        INDENT141_tree = None
        NEWLINE142_tree = None
        NEWLINE144_tree = None
        DEDENT145_tree = None
        NEWLINE146_tree = None
        ARROW_RIGHT148_tree = None
        ID149_tree = None
        NEWLINE150_tree = None
        ARROW_RIGHT152_tree = None
        NEWLINE153_tree = None
        INDENT154_tree = None
        NEWLINE155_tree = None
        ID156_tree = None
        NEWLINE157_tree = None
        DEDENT158_tree = None
        NEWLINE159_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:130:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt33 = 4
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:130:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:130:9: ( ID )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == ID) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:130:9: ID
                            pass 
                            ID134 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1402) 
                            stream_ID.add(ID134)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    ARROW_LEFT135 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1406) 
                    stream_ARROW_LEFT.add(ARROW_LEFT135)


                    # grammar/ShyRecognizerFrontend.g:130:25: ( arbitrary_value )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER or LA24_0 == STRING) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:130:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1408)
                            arbitrary_value136 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value136.tree)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1412) 
                    stream_NEWLINE.add(NEWLINE137)


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
                    # 131:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:131:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:131:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:132:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt33 == 2:
                    # grammar/ShyRecognizerFrontend.g:133:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:133:9: ( ID )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == ID) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:133:9: ID
                            pass 
                            ID138 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1465) 
                            stream_ID.add(ID138)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    ARROW_LEFT139 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1469) 
                    stream_ARROW_LEFT.add(ARROW_LEFT139)


                    NEWLINE140 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1471) 
                    stream_NEWLINE.add(NEWLINE140)


                    INDENT141 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1473) 
                    stream_INDENT.add(INDENT141)


                    NEWLINE142 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1475) 
                    stream_NEWLINE.add(NEWLINE142)


                    # grammar/ShyRecognizerFrontend.g:134:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA27_0 <= ID) or LA27_0 == MINUS or LA27_0 == NUMBER or LA27_0 == STRING) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:134:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:134:11: ( arbitrary_value )+
                            cnt26 = 0
                            while True: #loop26
                                alt26 = 2
                                LA26_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA26_0 <= ID) or LA26_0 == MINUS or LA26_0 == NUMBER or LA26_0 == STRING) :
                                    alt26 = 1


                                if alt26 == 1:
                                    # grammar/ShyRecognizerFrontend.g:134:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1487)
                                    arbitrary_value143 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value143.tree)



                                else:
                                    if cnt26 >= 1:
                                        break #loop26

                                    eee = EarlyExitException(26, self.input)
                                    raise eee

                                cnt26 += 1


                            NEWLINE144 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1491) 
                            stream_NEWLINE.add(NEWLINE144)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    DEDENT145 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1497) 
                    stream_DEDENT.add(DEDENT145)


                    NEWLINE146 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1499) 
                    stream_NEWLINE.add(NEWLINE146)


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
                    # 135:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:135:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:135:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:136:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt33 == 3:
                    # grammar/ShyRecognizerFrontend.g:137:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:137:9: ( arbitrary_value )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA28_0 <= ID) or LA28_0 == MINUS or LA28_0 == NUMBER or LA28_0 == STRING) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:137:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1552)
                            arbitrary_value147 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value147.tree)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    ARROW_RIGHT148 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1556) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT148)


                    # grammar/ShyRecognizerFrontend.g:137:39: ( ID )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:137:39: ID
                            pass 
                            ID149 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1558) 
                            stream_ID.add(ID149)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    NEWLINE150 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1562) 
                    stream_NEWLINE.add(NEWLINE150)


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
                    # 138:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:138:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:138:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:139:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt33 == 4:
                    # grammar/ShyRecognizerFrontend.g:140:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:140:9: ( arbitrary_value )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA30_0 <= ID) or LA30_0 == MINUS or LA30_0 == NUMBER or LA30_0 == STRING) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:140:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1615)
                            arbitrary_value151 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value151.tree)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


                    ARROW_RIGHT152 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1619) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT152)


                    NEWLINE153 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1621) 
                    stream_NEWLINE.add(NEWLINE153)


                    INDENT154 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1623) 
                    stream_INDENT.add(INDENT154)


                    NEWLINE155 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1625) 
                    stream_NEWLINE.add(NEWLINE155)


                    # grammar/ShyRecognizerFrontend.g:141:9: ( ( ID )+ NEWLINE )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:141:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:141:11: ( ID )+
                            cnt31 = 0
                            while True: #loop31
                                alt31 = 2
                                LA31_0 = self.input.LA(1)

                                if (LA31_0 == ID) :
                                    alt31 = 1


                                if alt31 == 1:
                                    # grammar/ShyRecognizerFrontend.g:141:11: ID
                                    pass 
                                    ID156 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1637) 
                                    stream_ID.add(ID156)



                                else:
                                    if cnt31 >= 1:
                                        break #loop31

                                    eee = EarlyExitException(31, self.input)
                                    raise eee

                                cnt31 += 1


                            NEWLINE157 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1641) 
                            stream_NEWLINE.add(NEWLINE157)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


                    DEDENT158 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1647) 
                    stream_DEDENT.add(DEDENT158)


                    NEWLINE159 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1649) 
                    stream_NEWLINE.add(NEWLINE159)


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
                    # 142:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:142:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:142:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:143:42: ( ID )+
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
    # grammar/ShyRecognizerFrontend.g:146:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE160 = None
        NEWLINE162 = None
        DO163 = None
        NEWLINE164 = None
        INDENT165 = None
        NEWLINE166 = None
        DEDENT168 = None
        NEWLINE169 = None
        condition161 = None

        statements167 = None


        WHILE160_tree = None
        NEWLINE162_tree = None
        DO163_tree = None
        NEWLINE164_tree = None
        INDENT165_tree = None
        NEWLINE166_tree = None
        DEDENT168_tree = None
        NEWLINE169_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:147:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:147:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE160 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1711) 
                stream_WHILE.add(WHILE160)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1713)
                condition161 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition161.tree)


                # grammar/ShyRecognizerFrontend.g:147:25: ( NEWLINE )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == NEWLINE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:147:25: NEWLINE
                    pass 
                    NEWLINE162 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1715) 
                    stream_NEWLINE.add(NEWLINE162)





                DO163 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1719) 
                stream_DO.add(DO163)


                NEWLINE164 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1721) 
                stream_NEWLINE.add(NEWLINE164)


                INDENT165 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1735) 
                stream_INDENT.add(INDENT165)


                NEWLINE166 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1737) 
                stream_NEWLINE.add(NEWLINE166)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1739)
                statements167 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements167.tree)


                DEDENT168 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1741) 
                stream_DEDENT.add(DEDENT168)


                NEWLINE169 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1743) 
                stream_NEWLINE.add(NEWLINE169)


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
                # 149:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:149:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:152:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head170 = None

        statement_elif171 = None

        statement_else172 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:153:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:153:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1783)
                statement_if_head170 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head170.tree)


                # grammar/ShyRecognizerFrontend.g:154:9: ( statement_elif )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == ELIF) :
                        alt35 = 1


                    if alt35 == 1:
                        # grammar/ShyRecognizerFrontend.g:154:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1793)
                        statement_elif171 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif171.tree)



                    else:
                        break #loop35


                # grammar/ShyRecognizerFrontend.g:155:9: ( statement_else )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == ELSE) :
                    alt36 = 1
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:155:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1805)
                    statement_else172 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else172.tree)





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
                # 156:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:156:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:158:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:159:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:163:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF173 = None
        statement_elif_body174 = None


        IF173_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:164:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:164:9: IF statement_elif_body
                pass 
                IF173 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1913) 
                stream_IF.add(IF173)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1915)
                statement_elif_body174 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body174.tree)


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
                # 165:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:168:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF175 = None
        statement_elif_body176 = None


        ELIF175_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:169:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:169:9: ELIF statement_elif_body
                pass 
                ELIF175 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1947) 
                stream_ELIF.add(ELIF175)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1949)
                statement_elif_body176 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body176.tree)


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
                # 170:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:173:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE178 = None
        DO179 = None
        NEWLINE180 = None
        INDENT181 = None
        NEWLINE182 = None
        DEDENT184 = None
        NEWLINE185 = None
        condition177 = None

        statements183 = None


        NEWLINE178_tree = None
        DO179_tree = None
        NEWLINE180_tree = None
        INDENT181_tree = None
        NEWLINE182_tree = None
        DEDENT184_tree = None
        NEWLINE185_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:174:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1981)
                condition177 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition177.tree)


                # grammar/ShyRecognizerFrontend.g:174:19: ( NEWLINE )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == NEWLINE) :
                    alt37 = 1
                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:174:19: NEWLINE
                    pass 
                    NEWLINE178 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1983) 
                    stream_NEWLINE.add(NEWLINE178)





                DO179 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1987) 
                stream_DO.add(DO179)


                NEWLINE180 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1989) 
                stream_NEWLINE.add(NEWLINE180)


                INDENT181 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body2003) 
                stream_INDENT.add(INDENT181)


                NEWLINE182 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body2005) 
                stream_NEWLINE.add(NEWLINE182)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body2007)
                statements183 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements183.tree)


                DEDENT184 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body2009) 
                stream_DEDENT.add(DEDENT184)


                NEWLINE185 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body2011) 
                stream_NEWLINE.add(NEWLINE185)


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
                # 176:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:176:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:179:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE186 = None
        NEWLINE187 = None
        INDENT188 = None
        NEWLINE189 = None
        DEDENT191 = None
        NEWLINE192 = None
        statements190 = None


        ELSE186_tree = None
        NEWLINE187_tree = None
        INDENT188_tree = None
        NEWLINE189_tree = None
        DEDENT191_tree = None
        NEWLINE192_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:180:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:180:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE186 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else2051) 
                stream_ELSE.add(ELSE186)


                NEWLINE187 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else2053) 
                stream_NEWLINE.add(NEWLINE187)


                INDENT188 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else2067) 
                stream_INDENT.add(INDENT188)


                NEWLINE189 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else2069) 
                stream_NEWLINE.add(NEWLINE189)


                self._state.following.append(self.FOLLOW_statements_in_statement_else2071)
                statements190 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements190.tree)


                DEDENT191 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else2073) 
                stream_DEDENT.add(DEDENT191)


                NEWLINE192 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else2075) 
                stream_NEWLINE.add(NEWLINE192)


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
                # 182:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:182:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:185:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY194 = None
        ALL196 = None
        condition_call193 = None

        condition_calls195 = None

        condition_calls197 = None


        ANY194_tree = None
        ALL196_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:186:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt38 = 3
                LA38 = self.input.LA(1)
                if LA38 == ID:
                    alt38 = 1
                elif LA38 == ANY:
                    alt38 = 2
                elif LA38 == ALL:
                    alt38 = 3
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:186:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition2113)
                    condition_call193 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call193.tree)


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
                    # 187:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:187:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:188:9: ANY condition_calls
                    pass 
                    ANY194 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition2142) 
                    stream_ANY.add(ANY194)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2144)
                    condition_calls195 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls195.tree)


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
                    # 189:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:189:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt38 == 3:
                    # grammar/ShyRecognizerFrontend.g:190:9: ALL condition_calls
                    pass 
                    ALL196 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition2173) 
                    stream_ALL.add(ALL196)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2175)
                    condition_calls197 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls197.tree)


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
                    # 191:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:191:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:194:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE199 = None
        INDENT200 = None
        NEWLINE201 = None
        DEDENT203 = None
        NEWLINE204 = None
        condition_call198 = None

        condition_call_line202 = None


        NEWLINE199_tree = None
        INDENT200_tree = None
        NEWLINE201_tree = None
        DEDENT203_tree = None
        NEWLINE204_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:195:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == ID) :
                    alt40 = 1
                elif (LA40_0 == NEWLINE) :
                    alt40 = 2
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae


                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:195:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls2213)
                    condition_call198 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call198.tree)



                elif alt40 == 2:
                    # grammar/ShyRecognizerFrontend.g:196:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE199 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2223) 
                    stream_NEWLINE.add(NEWLINE199)


                    INDENT200 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls2225) 
                    stream_INDENT.add(INDENT200)


                    NEWLINE201 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2227) 
                    stream_NEWLINE.add(NEWLINE201)


                    # grammar/ShyRecognizerFrontend.g:196:32: ( condition_call_line )+
                    cnt39 = 0
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == ID) :
                            alt39 = 1


                        if alt39 == 1:
                            # grammar/ShyRecognizerFrontend.g:196:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls2229)
                            condition_call_line202 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line202.tree)



                        else:
                            if cnt39 >= 1:
                                break #loop39

                            eee = EarlyExitException(39, self.input)
                            raise eee

                        cnt39 += 1


                    DEDENT203 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls2233) 
                    stream_DEDENT.add(DEDENT203)


                    NEWLINE204 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2235) 
                    stream_NEWLINE.add(NEWLINE204)


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
                    # 197:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:197:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:200:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line205 = None

        statement_call_multi_line206 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:201:5: ( statement_call_single_line | statement_call_multi_line )
                alt41 = 2
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:201:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call2269)
                    statement_call_single_line205 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line205.tree)



                elif alt41 == 2:
                    # grammar/ShyRecognizerFrontend.g:202:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call2279)
                    statement_call_multi_line206 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line206.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:205:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE208 = None
        statement_call_single_line207 = None

        statement_call_multi_line209 = None


        NEWLINE208_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:206:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt42 = 2
                alt42 = self.dfa42.predict(self.input)
                if alt42 == 1:
                    # grammar/ShyRecognizerFrontend.g:206:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line2298)
                    statement_call_single_line207 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line207.tree)


                    NEWLINE208 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line2300) 
                    stream_NEWLINE.add(NEWLINE208)


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
                    # 207:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt42 == 2:
                    # grammar/ShyRecognizerFrontend.g:208:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2326)
                    statement_call_multi_line209 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line209.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:211:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID210 = None
        statement_call_args211 = None


        ID210_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:212:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:212:9: ID ( statement_call_args )?
                pass 
                ID210 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2345) 
                stream_ID.add(ID210)


                # grammar/ShyRecognizerFrontend.g:212:12: ( statement_call_args )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER or LA43_0 == STRING) :
                    alt43 = 1
                if alt43 == 1:
                    # grammar/ShyRecognizerFrontend.g:212:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2347)
                    statement_call_args211 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args211.tree)





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
                # 213:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:213:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:213:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:216:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID212 = None
        NEWLINE214 = None
        INDENT215 = None
        NEWLINE216 = None
        NEWLINE218 = None
        DEDENT219 = None
        NEWLINE220 = None
        statement_call_args213 = None

        statement_call_args217 = None


        ID212_tree = None
        NEWLINE214_tree = None
        INDENT215_tree = None
        NEWLINE216_tree = None
        NEWLINE218_tree = None
        DEDENT219_tree = None
        NEWLINE220_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:217:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:217:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID212 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2391) 
                stream_ID.add(ID212)


                # grammar/ShyRecognizerFrontend.g:217:12: ( statement_call_args )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if ((EXPRESSION <= LA44_0 <= ID) or LA44_0 == MINUS or LA44_0 == NUMBER or LA44_0 == STRING) :
                    alt44 = 1
                if alt44 == 1:
                    # grammar/ShyRecognizerFrontend.g:217:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2393)
                    statement_call_args213 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args213.tree)





                NEWLINE214 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2397) 
                stream_NEWLINE.add(NEWLINE214)


                INDENT215 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2407) 
                stream_INDENT.add(INDENT215)


                NEWLINE216 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2409) 
                stream_NEWLINE.add(NEWLINE216)


                # grammar/ShyRecognizerFrontend.g:218:24: ( statement_call_args NEWLINE )+
                cnt45 = 0
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA45_0 <= ID) or LA45_0 == MINUS or LA45_0 == NUMBER or LA45_0 == STRING) :
                        alt45 = 1


                    if alt45 == 1:
                        # grammar/ShyRecognizerFrontend.g:218:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2413)
                        statement_call_args217 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args217.tree)


                        NEWLINE218 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2415) 
                        stream_NEWLINE.add(NEWLINE218)



                    else:
                        if cnt45 >= 1:
                            break #loop45

                        eee = EarlyExitException(45, self.input)
                        raise eee

                    cnt45 += 1


                DEDENT219 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2421) 
                stream_DEDENT.add(DEDENT219)


                NEWLINE220 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2423) 
                stream_NEWLINE.add(NEWLINE220)


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
                # 219:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:219:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:219:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:222:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value221 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:222:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:222:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:222:23: ( arbitrary_value )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA46_0 <= ID) or LA46_0 == MINUS or LA46_0 == NUMBER or LA46_0 == STRING) :
                        alt46 = 1


                    if alt46 == 1:
                        # grammar/ShyRecognizerFrontend.g:222:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2459)
                        arbitrary_value221 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value221.tree)



                    else:
                        if cnt46 >= 1:
                            break #loop46

                        eee = EarlyExitException(46, self.input)
                        raise eee

                    cnt46 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:224:1: arbitrary_value : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID222 = None
        EXPRESSION223 = None
        STRING224 = None
        num_whole225 = None

        num_fract226 = None


        ID222_tree = None
        EXPRESSION223_tree = None
        STRING224_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:225:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
                alt47 = 5
                LA47 = self.input.LA(1)
                if LA47 == ID:
                    alt47 = 1
                elif LA47 == EXPRESSION:
                    alt47 = 2
                elif LA47 == STRING:
                    alt47 = 3
                elif LA47 == MINUS:
                    LA47_4 = self.input.LA(2)

                    if (LA47_4 == NUMBER) :
                        LA47_5 = self.input.LA(3)

                        if (LA47_5 == DIVIDE) :
                            alt47 = 5
                        elif (LA47_5 == ARROW_RIGHT or LA47_5 == DO or (EXPRESSION <= LA47_5 <= ID) or LA47_5 == MINUS or (NEWLINE <= LA47_5 <= NUMBER) or LA47_5 == STRING) :
                            alt47 = 4
                        else:
                            nvae = NoViableAltException("", 47, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 47, 4, self.input)

                        raise nvae


                elif LA47 == NUMBER:
                    LA47_5 = self.input.LA(2)

                    if (LA47_5 == DIVIDE) :
                        alt47 = 5
                    elif (LA47_5 == ARROW_RIGHT or LA47_5 == DO or (EXPRESSION <= LA47_5 <= ID) or LA47_5 == MINUS or (NEWLINE <= LA47_5 <= NUMBER) or LA47_5 == STRING) :
                        alt47 = 4
                    else:
                        nvae = NoViableAltException("", 47, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae


                if alt47 == 1:
                    # grammar/ShyRecognizerFrontend.g:225:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID222 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2476)
                    ID222_tree = self._adaptor.createWithPayload(ID222)
                    self._adaptor.addChild(root_0, ID222_tree)




                elif alt47 == 2:
                    # grammar/ShyRecognizerFrontend.g:226:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION223 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2486)
                    EXPRESSION223_tree = self._adaptor.createWithPayload(EXPRESSION223)
                    self._adaptor.addChild(root_0, EXPRESSION223_tree)




                elif alt47 == 3:
                    # grammar/ShyRecognizerFrontend.g:227:9: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING224 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2496)
                    STRING224_tree = self._adaptor.createWithPayload(STRING224)
                    self._adaptor.addChild(root_0, STRING224_tree)




                elif alt47 == 4:
                    # grammar/ShyRecognizerFrontend.g:228:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2506)
                    num_whole225 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole225.tree)



                elif alt47 == 5:
                    # grammar/ShyRecognizerFrontend.g:229:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2516)
                    num_fract226 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract226.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:232:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS227 = None
        ID228 = None
        NEWLINE229 = None
        INDENT230 = None
        NEWLINE231 = None
        DEDENT233 = None
        NEWLINE234 = None
        consts_items232 = None


        CONSTS227_tree = None
        ID228_tree = None
        NEWLINE229_tree = None
        INDENT230_tree = None
        NEWLINE231_tree = None
        DEDENT233_tree = None
        NEWLINE234_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:233:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:233:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS227 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2535) 
                stream_CONSTS.add(CONSTS227)


                ID228 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2537) 
                stream_ID.add(ID228)


                NEWLINE229 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2539) 
                stream_NEWLINE.add(NEWLINE229)


                INDENT230 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2549) 
                stream_INDENT.add(INDENT230)


                NEWLINE231 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2551) 
                stream_NEWLINE.add(NEWLINE231)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2553)
                consts_items232 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items232.tree)


                DEDENT233 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2555) 
                stream_DEDENT.add(DEDENT233)


                NEWLINE234 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2557) 
                stream_NEWLINE.add(NEWLINE234)


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
                # 235:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:235:13: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:237:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item235 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:237:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:237:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:237:16: ( consts_item )+
                cnt48 = 0
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == ID) :
                        alt48 = 1


                    if alt48 == 1:
                        # grammar/ShyRecognizerFrontend.g:237:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2590)
                        consts_item235 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item235.tree)



                    else:
                        if cnt48 >= 1:
                            break #loop48

                        eee = EarlyExitException(48, self.input)
                        raise eee

                    cnt48 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:238:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID236 = None
        NEWLINE238 = None
        ID239 = None
        NEWLINE241 = None
        ID242 = None
        EXPRESSION243 = None
        NEWLINE244 = None
        num_whole237 = None

        num_fract240 = None


        ID236_tree = None
        NEWLINE238_tree = None
        ID239_tree = None
        NEWLINE241_tree = None
        ID242_tree = None
        EXPRESSION243_tree = None
        NEWLINE244_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:239:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt49 = 3
                LA49_0 = self.input.LA(1)

                if (LA49_0 == ID) :
                    LA49 = self.input.LA(2)
                    if LA49 == EXPRESSION:
                        alt49 = 3
                    elif LA49 == MINUS:
                        LA49_3 = self.input.LA(3)

                        if (LA49_3 == NUMBER) :
                            LA49_4 = self.input.LA(4)

                            if (LA49_4 == DIVIDE) :
                                alt49 = 2
                            elif (LA49_4 == NEWLINE) :
                                alt49 = 1
                            else:
                                nvae = NoViableAltException("", 49, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 49, 3, self.input)

                            raise nvae


                    elif LA49 == NUMBER:
                        LA49_4 = self.input.LA(3)

                        if (LA49_4 == DIVIDE) :
                            alt49 = 2
                        elif (LA49_4 == NEWLINE) :
                            alt49 = 1
                        else:
                            nvae = NoViableAltException("", 49, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 49, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae


                if alt49 == 1:
                    # grammar/ShyRecognizerFrontend.g:239:9: ID num_whole NEWLINE
                    pass 
                    ID236 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2606) 
                    stream_ID.add(ID236)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2608)
                    num_whole237 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole237.tree)


                    NEWLINE238 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2610) 
                    stream_NEWLINE.add(NEWLINE238)


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
                    # 239:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:239:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt49 == 2:
                    # grammar/ShyRecognizerFrontend.g:240:9: ID num_fract NEWLINE
                    pass 
                    ID239 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2632) 
                    stream_ID.add(ID239)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2634)
                    num_fract240 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract240.tree)


                    NEWLINE241 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2636) 
                    stream_NEWLINE.add(NEWLINE241)


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
                    # 240:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:240:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt49 == 3:
                    # grammar/ShyRecognizerFrontend.g:241:9: ID EXPRESSION NEWLINE
                    pass 
                    ID242 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2658) 
                    stream_ID.add(ID242)


                    EXPRESSION243 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2660) 
                    stream_EXPRESSION.add(EXPRESSION243)


                    NEWLINE244 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2662) 
                    stream_NEWLINE.add(NEWLINE244)


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
                    # 241:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:241:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:244:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES245 = None
        ID246 = None
        NEWLINE247 = None
        INDENT248 = None
        NEWLINE249 = None
        DEDENT251 = None
        NEWLINE252 = None
        types_item250 = None


        TYPES245_tree = None
        ID246_tree = None
        NEWLINE247_tree = None
        INDENT248_tree = None
        NEWLINE249_tree = None
        DEDENT251_tree = None
        NEWLINE252_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:245:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:245:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES245 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2693) 
                stream_TYPES.add(TYPES245)


                ID246 = self.match(self.input, ID, self.FOLLOW_ID_in_types2695) 
                stream_ID.add(ID246)


                NEWLINE247 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2697) 
                stream_NEWLINE.add(NEWLINE247)


                INDENT248 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2707) 
                stream_INDENT.add(INDENT248)


                NEWLINE249 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2709) 
                stream_NEWLINE.add(NEWLINE249)


                # grammar/ShyRecognizerFrontend.g:246:24: ( types_item )+
                cnt50 = 0
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == ID) :
                        alt50 = 1


                    if alt50 == 1:
                        # grammar/ShyRecognizerFrontend.g:246:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2711)
                        types_item250 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item250.tree)



                    else:
                        if cnt50 >= 1:
                            break #loop50

                        eee = EarlyExitException(50, self.input)
                        raise eee

                    cnt50 += 1


                DEDENT251 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2715) 
                stream_DEDENT.add(DEDENT251)


                NEWLINE252 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2717) 
                stream_NEWLINE.add(NEWLINE252)


                # AST Rewrite
                # elements: ID, types_item
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 247:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:247:13: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:247:30: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:249:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID253 = None
        attrs_hints254 = None


        ID253_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:249:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:249:14: ID attrs_hints
                pass 
                ID253 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2752) 
                stream_ID.add(ID253)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2754)
                attrs_hints254 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints254.tree)


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
                # 249:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:249:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:251:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES255 = None
        ID256 = None
        NEWLINE257 = None
        INDENT258 = None
        NEWLINE259 = None
        DEDENT261 = None
        NEWLINE262 = None
        messages_item260 = None


        MESSAGES255_tree = None
        ID256_tree = None
        NEWLINE257_tree = None
        INDENT258_tree = None
        NEWLINE259_tree = None
        DEDENT261_tree = None
        NEWLINE262_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:252:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:252:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES255 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2781) 
                stream_MESSAGES.add(MESSAGES255)


                ID256 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2783) 
                stream_ID.add(ID256)


                NEWLINE257 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2785) 
                stream_NEWLINE.add(NEWLINE257)


                INDENT258 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2795) 
                stream_INDENT.add(INDENT258)


                NEWLINE259 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2797) 
                stream_NEWLINE.add(NEWLINE259)


                # grammar/ShyRecognizerFrontend.g:253:24: ( messages_item )+
                cnt51 = 0
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == ID) :
                        alt51 = 1


                    if alt51 == 1:
                        # grammar/ShyRecognizerFrontend.g:253:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2799)
                        messages_item260 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item260.tree)



                    else:
                        if cnt51 >= 1:
                            break #loop51

                        eee = EarlyExitException(51, self.input)
                        raise eee

                    cnt51 += 1


                DEDENT261 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2803) 
                stream_DEDENT.add(DEDENT261)


                NEWLINE262 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2805) 
                stream_NEWLINE.add(NEWLINE262)


                # AST Rewrite
                # elements: ID, messages_item
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 254:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:254:13: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:254:33: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:257:1: messages_item : ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) );
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID263 = None
        ID265 = None
        REPLY266 = None
        ID268 = None
        REQUEST269 = None
        ID271 = None
        NEWLINE272 = None
        INDENT273 = None
        NEWLINE274 = None
        REPLY275 = None
        DEDENT277 = None
        NEWLINE278 = None
        ID279 = None
        NEWLINE280 = None
        INDENT281 = None
        NEWLINE282 = None
        REQUEST283 = None
        DEDENT285 = None
        NEWLINE286 = None
        ID287 = None
        NEWLINE288 = None
        INDENT289 = None
        NEWLINE290 = None
        REQUEST291 = None
        REPLY293 = None
        DEDENT295 = None
        NEWLINE296 = None
        attrs_hints264 = None

        attrs_hints267 = None

        attrs_hints270 = None

        attrs_hints276 = None

        attrs_hints284 = None

        attrs_hints292 = None

        attrs_hints294 = None


        ID263_tree = None
        ID265_tree = None
        REPLY266_tree = None
        ID268_tree = None
        REQUEST269_tree = None
        ID271_tree = None
        NEWLINE272_tree = None
        INDENT273_tree = None
        NEWLINE274_tree = None
        REPLY275_tree = None
        DEDENT277_tree = None
        NEWLINE278_tree = None
        ID279_tree = None
        NEWLINE280_tree = None
        INDENT281_tree = None
        NEWLINE282_tree = None
        REQUEST283_tree = None
        DEDENT285_tree = None
        NEWLINE286_tree = None
        ID287_tree = None
        NEWLINE288_tree = None
        INDENT289_tree = None
        NEWLINE290_tree = None
        REQUEST291_tree = None
        REPLY293_tree = None
        DEDENT295_tree = None
        NEWLINE296_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_REPLY = RewriteRuleTokenStream(self._adaptor, "token REPLY")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:258:5: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) )
                alt52 = 6
                alt52 = self.dfa52.predict(self.input)
                if alt52 == 1:
                    # grammar/ShyRecognizerFrontend.g:258:9: ID attrs_hints
                    pass 
                    ID263 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2847) 
                    stream_ID.add(ID263)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2849)
                    attrs_hints264 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints264.tree)


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
                    # 259:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:259:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM, "TREE_MESSAGES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM_RECEIVE, "TREE_MESSAGES_ITEM_RECEIVE")
                    )

                    self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt52 == 2:
                    # grammar/ShyRecognizerFrontend.g:262:9: ID REPLY attrs_hints
                    pass 
                    ID265 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2910) 
                    stream_ID.add(ID265)


                    REPLY266 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2912) 
                    stream_REPLY.add(REPLY266)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2914)
                    attrs_hints267 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints267.tree)


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
                    # 263:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:263:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM, "TREE_MESSAGES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM_REPLY, "TREE_MESSAGES_ITEM_REPLY")
                    )

                    self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt52 == 3:
                    # grammar/ShyRecognizerFrontend.g:266:9: ID REQUEST attrs_hints
                    pass 
                    ID268 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2975) 
                    stream_ID.add(ID268)


                    REQUEST269 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item2977) 
                    stream_REQUEST.add(REQUEST269)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2979)
                    attrs_hints270 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints270.tree)


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
                    # 267:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:267:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM, "TREE_MESSAGES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM_REQUEST, "TREE_MESSAGES_ITEM_REQUEST")
                    )

                    self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt52 == 4:
                    # grammar/ShyRecognizerFrontend.g:270:9: ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID271 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3040) 
                    stream_ID.add(ID271)


                    NEWLINE272 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3042) 
                    stream_NEWLINE.add(NEWLINE272)


                    INDENT273 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3044) 
                    stream_INDENT.add(INDENT273)


                    NEWLINE274 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3046) 
                    stream_NEWLINE.add(NEWLINE274)


                    REPLY275 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item3048) 
                    stream_REPLY.add(REPLY275)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3050)
                    attrs_hints276 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints276.tree)


                    DEDENT277 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3052) 
                    stream_DEDENT.add(DEDENT277)


                    NEWLINE278 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3054) 
                    stream_NEWLINE.add(NEWLINE278)


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
                    # 271:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:271:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM, "TREE_MESSAGES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM_REPLY, "TREE_MESSAGES_ITEM_REPLY")
                    )

                    self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt52 == 5:
                    # grammar/ShyRecognizerFrontend.g:274:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE
                    pass 
                    ID279 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3115) 
                    stream_ID.add(ID279)


                    NEWLINE280 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3117) 
                    stream_NEWLINE.add(NEWLINE280)


                    INDENT281 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3119) 
                    stream_INDENT.add(INDENT281)


                    NEWLINE282 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3121) 
                    stream_NEWLINE.add(NEWLINE282)


                    REQUEST283 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3123) 
                    stream_REQUEST.add(REQUEST283)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3125)
                    attrs_hints284 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints284.tree)


                    DEDENT285 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3127) 
                    stream_DEDENT.add(DEDENT285)


                    NEWLINE286 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3129) 
                    stream_NEWLINE.add(NEWLINE286)


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
                    # 275:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:275:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM, "TREE_MESSAGES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM_REQUEST, "TREE_MESSAGES_ITEM_REQUEST")
                    )

                    self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt52 == 6:
                    # grammar/ShyRecognizerFrontend.g:278:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID287 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3190) 
                    stream_ID.add(ID287)


                    NEWLINE288 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3192) 
                    stream_NEWLINE.add(NEWLINE288)


                    INDENT289 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3194) 
                    stream_INDENT.add(INDENT289)


                    NEWLINE290 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3196) 
                    stream_NEWLINE.add(NEWLINE290)


                    REQUEST291 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3210) 
                    stream_REQUEST.add(REQUEST291)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3212)
                    attrs_hints292 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints292.tree)


                    REPLY293 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item3226) 
                    stream_REPLY.add(REPLY293)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3228)
                    attrs_hints294 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints294.tree)


                    DEDENT295 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3238) 
                    stream_DEDENT.add(DEDENT295)


                    NEWLINE296 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3240) 
                    stream_NEWLINE.add(NEWLINE296)


                    # AST Rewrite
                    # elements: attrs_hints, ID, attrs_hints
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 282:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:282:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM, "TREE_MESSAGES_ITEM")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM_REQUEST, "TREE_MESSAGES_ITEM_REQUEST")
                    )

                    self._adaptor.addChild(root_1, stream_attrs_hints.nextTree())

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_MESSAGES_ITEM_REPLY, "TREE_MESSAGES_ITEM_REPLY")
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
    # grammar/ShyRecognizerFrontend.g:288:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS297 = None
        ID298 = None
        attrs_hints299 = None


        VARS297_tree = None
        ID298_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:289:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:289:9: VARS ID attrs_hints
                pass 
                VARS297 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars3330) 
                stream_VARS.add(VARS297)


                ID298 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3332) 
                stream_ID.add(ID298)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3334)
                attrs_hints299 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints299.tree)


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
                # 290:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:290:13: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:293:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE301 = None
        NEWLINE302 = None
        INDENT303 = None
        NEWLINE304 = None
        NEWLINE306 = None
        DEDENT307 = None
        NEWLINE308 = None
        NEWLINE310 = None
        INDENT311 = None
        NEWLINE312 = None
        NEWLINE314 = None
        DEDENT315 = None
        NEWLINE316 = None
        attr_hint300 = None

        attr_hint305 = None

        attr_hint309 = None

        attr_hint313 = None


        NEWLINE301_tree = None
        NEWLINE302_tree = None
        INDENT303_tree = None
        NEWLINE304_tree = None
        NEWLINE306_tree = None
        DEDENT307_tree = None
        NEWLINE308_tree = None
        NEWLINE310_tree = None
        INDENT311_tree = None
        NEWLINE312_tree = None
        NEWLINE314_tree = None
        DEDENT315_tree = None
        NEWLINE316_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:294:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt55 = 3
                alt55 = self.dfa55.predict(self.input)
                if alt55 == 1:
                    # grammar/ShyRecognizerFrontend.g:294:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3374)
                    attr_hint300 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint300.tree)


                    NEWLINE301 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3376) 
                    stream_NEWLINE.add(NEWLINE301)


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
                    # 295:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt55 == 2:
                    # grammar/ShyRecognizerFrontend.g:296:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE302 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3401) 
                    stream_NEWLINE.add(NEWLINE302)


                    # grammar/ShyRecognizerFrontend.g:297:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:297:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT303 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3413) 
                    stream_INDENT.add(INDENT303)


                    NEWLINE304 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3415) 
                    stream_NEWLINE.add(NEWLINE304)


                    # grammar/ShyRecognizerFrontend.g:297:26: ( attr_hint NEWLINE )+
                    cnt53 = 0
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == CURLY_OPEN or LA53_0 == ID) :
                            alt53 = 1


                        if alt53 == 1:
                            # grammar/ShyRecognizerFrontend.g:297:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3419)
                            attr_hint305 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint305.tree)


                            NEWLINE306 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3421) 
                            stream_NEWLINE.add(NEWLINE306)



                        else:
                            if cnt53 >= 1:
                                break #loop53

                            eee = EarlyExitException(53, self.input)
                            raise eee

                        cnt53 += 1


                    DEDENT307 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3427) 
                    stream_DEDENT.add(DEDENT307)


                    NEWLINE308 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3429) 
                    stream_NEWLINE.add(NEWLINE308)





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
                    # 298:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:298:30: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt55 == 3:
                    # grammar/ShyRecognizerFrontend.g:299:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3458)
                    attr_hint309 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint309.tree)


                    NEWLINE310 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3460) 
                    stream_NEWLINE.add(NEWLINE310)


                    # grammar/ShyRecognizerFrontend.g:300:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:300:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT311 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3472) 
                    stream_INDENT.add(INDENT311)


                    NEWLINE312 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3474) 
                    stream_NEWLINE.add(NEWLINE312)


                    # grammar/ShyRecognizerFrontend.g:300:26: ( attr_hint NEWLINE )+
                    cnt54 = 0
                    while True: #loop54
                        alt54 = 2
                        LA54_0 = self.input.LA(1)

                        if (LA54_0 == CURLY_OPEN or LA54_0 == ID) :
                            alt54 = 1


                        if alt54 == 1:
                            # grammar/ShyRecognizerFrontend.g:300:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3478)
                            attr_hint313 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint313.tree)


                            NEWLINE314 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3480) 
                            stream_NEWLINE.add(NEWLINE314)



                        else:
                            if cnt54 >= 1:
                                break #loop54

                            eee = EarlyExitException(54, self.input)
                            raise eee

                        cnt54 += 1


                    DEDENT315 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3486) 
                    stream_DEDENT.add(DEDENT315)


                    NEWLINE316 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3488) 
                    stream_NEWLINE.add(NEWLINE316)





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
                    # 301:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:301:30: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:303:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID317 = None
        ID319 = None
        NEWLINE321 = None
        INDENT322 = None
        NEWLINE323 = None
        ID324 = None
        NEWLINE325 = None
        DEDENT326 = None
        hint318 = None

        hint320 = None


        ID317_tree = None
        ID319_tree = None
        NEWLINE321_tree = None
        INDENT322_tree = None
        NEWLINE323_tree = None
        ID324_tree = None
        NEWLINE325_tree = None
        DEDENT326_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:304:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt60 = 3
                alt60 = self.dfa60.predict(self.input)
                if alt60 == 1:
                    # grammar/ShyRecognizerFrontend.g:304:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:304:9: ( ID )+
                    cnt56 = 0
                    while True: #loop56
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == ID) :
                            alt56 = 1


                        if alt56 == 1:
                            # grammar/ShyRecognizerFrontend.g:304:9: ID
                            pass 
                            ID317 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3526) 
                            stream_ID.add(ID317)



                        else:
                            if cnt56 >= 1:
                                break #loop56

                            eee = EarlyExitException(56, self.input)
                            raise eee

                        cnt56 += 1


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
                    # 305:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:305:13: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:305:46: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:305:46: ^( TREE_ATTR ID )
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




                elif alt60 == 2:
                    # grammar/ShyRecognizerFrontend.g:306:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3568)
                    hint318 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint318.tree)


                    # grammar/ShyRecognizerFrontend.g:306:14: ( ID )+
                    cnt57 = 0
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == ID) :
                            alt57 = 1


                        if alt57 == 1:
                            # grammar/ShyRecognizerFrontend.g:306:14: ID
                            pass 
                            ID319 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3570) 
                            stream_ID.add(ID319)



                        else:
                            if cnt57 >= 1:
                                break #loop57

                            eee = EarlyExitException(57, self.input)
                            raise eee

                        cnt57 += 1


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
                    # 307:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:307:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:307:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:307:36: ^( TREE_ATTR ID )
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




                elif alt60 == 3:
                    # grammar/ShyRecognizerFrontend.g:308:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3611)
                    hint320 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint320.tree)


                    NEWLINE321 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3613) 
                    stream_NEWLINE.add(NEWLINE321)


                    INDENT322 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint3615) 
                    stream_INDENT.add(INDENT322)


                    NEWLINE323 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3617) 
                    stream_NEWLINE.add(NEWLINE323)


                    # grammar/ShyRecognizerFrontend.g:308:37: ( ( ID )+ NEWLINE )+
                    cnt59 = 0
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == ID) :
                            alt59 = 1


                        if alt59 == 1:
                            # grammar/ShyRecognizerFrontend.g:308:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:308:39: ( ID )+
                            cnt58 = 0
                            while True: #loop58
                                alt58 = 2
                                LA58_0 = self.input.LA(1)

                                if (LA58_0 == ID) :
                                    alt58 = 1


                                if alt58 == 1:
                                    # grammar/ShyRecognizerFrontend.g:308:39: ID
                                    pass 
                                    ID324 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3621) 
                                    stream_ID.add(ID324)



                                else:
                                    if cnt58 >= 1:
                                        break #loop58

                                    eee = EarlyExitException(58, self.input)
                                    raise eee

                                cnt58 += 1


                            NEWLINE325 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3625) 
                            stream_NEWLINE.add(NEWLINE325)



                        else:
                            if cnt59 >= 1:
                                break #loop59

                            eee = EarlyExitException(59, self.input)
                            raise eee

                        cnt59 += 1


                    DEDENT326 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint3631) 
                    stream_DEDENT.add(DEDENT326)


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
                    # 309:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:309:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:309:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:309:36: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:312:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN327 = None
        ID328 = None
        CURLY_CLOSE329 = None
        CURLY_OPEN330 = None
        ID331 = None
        CURLY_CLOSE333 = None
        hint_arg332 = None


        CURLY_OPEN327_tree = None
        ID328_tree = None
        CURLY_CLOSE329_tree = None
        CURLY_OPEN330_tree = None
        ID331_tree = None
        CURLY_CLOSE333_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:313:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == CURLY_OPEN) :
                    LA62_1 = self.input.LA(2)

                    if (LA62_1 == ID) :
                        LA62_2 = self.input.LA(3)

                        if (LA62_2 == CURLY_CLOSE) :
                            alt62 = 1
                        elif (LA62_2 == ID or LA62_2 == UNDERSCORE) :
                            alt62 = 2
                        else:
                            nvae = NoViableAltException("", 62, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 62, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 62, 0, self.input)

                    raise nvae


                if alt62 == 1:
                    # grammar/ShyRecognizerFrontend.g:313:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN327 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3679) 
                    stream_CURLY_OPEN.add(CURLY_OPEN327)


                    ID328 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3681) 
                    stream_ID.add(ID328)


                    CURLY_CLOSE329 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3683) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE329)


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
                    # 313:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:313:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt62 == 2:
                    # grammar/ShyRecognizerFrontend.g:314:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN330 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3703) 
                    stream_CURLY_OPEN.add(CURLY_OPEN330)


                    ID331 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3705) 
                    stream_ID.add(ID331)


                    # grammar/ShyRecognizerFrontend.g:314:23: ( hint_arg )+
                    cnt61 = 0
                    while True: #loop61
                        alt61 = 2
                        LA61_0 = self.input.LA(1)

                        if (LA61_0 == ID or LA61_0 == UNDERSCORE) :
                            alt61 = 1


                        if alt61 == 1:
                            # grammar/ShyRecognizerFrontend.g:314:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint3707)
                            hint_arg332 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg332.tree)



                        else:
                            if cnt61 >= 1:
                                break #loop61

                            eee = EarlyExitException(61, self.input)
                            raise eee

                        cnt61 += 1


                    CURLY_CLOSE333 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3711) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE333)


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
                    # 314:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:314:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:314:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:316:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set334 = None

        set334_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:316:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set334 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set334))

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
    # grammar/ShyRecognizerFrontend.g:318:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS335 = None
        NUMBER336 = None

        MINUS335_tree = None
        NUMBER336_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:318:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:318:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:318:13: ( MINUS )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == MINUS) :
                    alt63 = 1
                if alt63 == 1:
                    # grammar/ShyRecognizerFrontend.g:318:13: MINUS
                    pass 
                    MINUS335 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3750)
                    MINUS335_tree = self._adaptor.createWithPayload(MINUS335)
                    self._adaptor.addChild(root_0, MINUS335_tree)






                NUMBER336 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3754)
                NUMBER336_tree = self._adaptor.createWithPayload(NUMBER336)
                self._adaptor.addChild(root_0, NUMBER336_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:319:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS337 = None
        NUMBER338 = None
        DIVIDE339 = None
        NUMBER340 = None

        MINUS337_tree = None
        NUMBER338_tree = None
        DIVIDE339_tree = None
        NUMBER340_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:319:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:319:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:319:13: ( MINUS )?
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if (LA64_0 == MINUS) :
                    alt64 = 1
                if alt64 == 1:
                    # grammar/ShyRecognizerFrontend.g:319:13: MINUS
                    pass 
                    MINUS337 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3762)
                    MINUS337_tree = self._adaptor.createWithPayload(MINUS337)
                    self._adaptor.addChild(root_0, MINUS337_tree)






                NUMBER338 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3766)
                NUMBER338_tree = self._adaptor.createWithPayload(NUMBER338)
                self._adaptor.addChild(root_0, NUMBER338_tree)



                DIVIDE339 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3768)
                DIVIDE339_tree = self._adaptor.createWithPayload(DIVIDE339)
                self._adaptor.addChild(root_0, DIVIDE339_tree)



                NUMBER340 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3770)
                NUMBER340_tree = self._adaptor.createWithPayload(NUMBER340)
                self._adaptor.addChild(root_0, NUMBER340_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\1\22\1\7\4\uffff\1\7\2\10\1\33\1\10\1\15\1\10\1\33\2\uffff\1\10"
        )

    DFA21_max = DFA.unpack(
        u"\1\126\1\44\4\uffff\3\44\1\33\1\44\1\126\1\44\1\33\2\uffff\1\44"
        )

    DFA21_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\10\uffff\1\2\1\1\1\uffff"
        )

    DFA21_special = DFA.unpack(
        u"\21\uffff"
        )


    DFA21_transition = [
        DFA.unpack(u"\1\3\1\1\1\2\2\uffff\1\3\3\uffff\1\3\10\uffff\1\3\57"
        u"\uffff\1\4\1\uffff\1\5"),
        DFA.unpack(u"\2\3\11\uffff\1\7\1\6\3\uffff\1\11\2\uffff\1\13\1\12"
        u"\10\uffff\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\3\11\uffff\1\7\1\6\3\uffff\1\11\2\uffff\1\13\1\12"
        u"\10\uffff\1\10"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\14\3\uffff\1\11\2\uffff\1\13\1"
        u"\12\10\uffff\1\10"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\14\3\uffff\1\11\2\uffff\1\13\1"
        u"\12\10\uffff\1\10"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\1\3\5\uffff\1\15\3\uffff\1\7\1\14\3\uffff\1\11\2\uffff"
        u"\1\13\1\12\10\uffff\1\10"),
        DFA.unpack(u"\1\17\4\uffff\3\17\1\16\1\uffff\1\17\3\uffff\1\17\3"
        u"\uffff\1\17\2\uffff\1\17\1\uffff\1\17\57\uffff\1\17\1\uffff\1\17"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\14\3\uffff\1\11\2\uffff\1\13\1"
        u"\12\10\uffff\1\10"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\14\3\uffff\1\11\2\uffff\1\13\1"
        u"\12\10\uffff\1\10")
    ]

    # class definition for DFA #21

    class DFA21(DFA):
        pass


    # lookup tables for DFA #33

    DFA33_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA33_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA33_min = DFA.unpack(
        u"\1\22\1\7\2\10\1\33\1\10\1\22\1\23\1\10\1\33\4\uffff\1\10"
        )

    DFA33_max = DFA.unpack(
        u"\4\44\1\33\2\44\1\32\1\44\1\33\4\uffff\1\44"
        )

    DFA33_accept = DFA.unpack(
        u"\12\uffff\1\2\1\1\1\4\1\3\1\uffff"
        )

    DFA33_special = DFA.unpack(
        u"\17\uffff"
        )


    DFA33_transition = [
        DFA.unpack(u"\1\2\1\1\3\uffff\1\4\3\uffff\1\5\10\uffff\1\3"),
        DFA.unpack(u"\1\6\1\7\11\uffff\1\2\1\1\3\uffff\1\4\3\uffff\1\5\10"
        u"\uffff\1\3"),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\10\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\10\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\7\5\uffff\1\11\3\uffff\1\2\1\10\3\uffff\1\4\3\uffff"
        u"\1\5\10\uffff\1\3"),
        DFA.unpack(u"\2\13\3\uffff\1\13\2\uffff\1\12\1\13\10\uffff\1\13"),
        DFA.unpack(u"\1\15\6\uffff\1\14"),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\10\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\10\uffff"
        u"\1\3")
    ]

    # class definition for DFA #33

    class DFA33(DFA):
        pass


    # lookup tables for DFA #41

    DFA41_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA41_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA41_min = DFA.unpack(
        u"\1\23\4\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA41_max = DFA.unpack(
        u"\1\23\4\44\1\33\1\44\1\25\1\uffff\1\33\1\uffff\1\44"
        )

    DFA41_accept = DFA.unpack(
        u"\10\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA41_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA41_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\11\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7"
        u"\1\6\10\uffff\1\4"),
        DFA.unpack(u"\1\10\5\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10"
        u"\uffff\1\4")
    ]

    # class definition for DFA #41

    class DFA41(DFA):
        pass


    # lookup tables for DFA #42

    DFA42_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA42_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA42_min = DFA.unpack(
        u"\1\23\4\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA42_max = DFA.unpack(
        u"\1\23\4\44\1\33\1\44\1\25\1\33\2\uffff\1\44"
        )

    DFA42_accept = DFA.unpack(
        u"\11\uffff\1\2\1\1\1\uffff"
        )

    DFA42_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA42_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10\uffff\1\4"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10\uffff\1\4"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10\uffff\1\4"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10\uffff\1\4"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\10\3\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\12\5\uffff\1\12\1\uffff\1\11"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\10\uffff\1\4")
    ]

    # class definition for DFA #42

    class DFA42(DFA):
        pass


    # lookup tables for DFA #52

    DFA52_eot = DFA.unpack(
        u"\77\uffff"
        )

    DFA52_eof = DFA.unpack(
        u"\77\uffff"
        )

    DFA52_min = DFA.unpack(
        u"\1\23\1\14\2\uffff\1\25\1\uffff\1\32\1\14\1\uffff\1\14\2\23\1\25"
        u"\1\15\1\13\1\32\1\uffff\1\32\1\uffff\1\23\1\13\2\14\1\23\1\25\5"
        u"\23\1\32\1\14\1\13\1\14\1\13\1\23\1\32\1\23\1\13\1\32\1\23\1\13"
        u"\1\23\1\15\1\23\1\25\1\23\1\15\1\23\1\25\1\23\1\15\3\32\4\23\2"
        u"\15\2\32"
        )

    DFA52_max = DFA.unpack(
        u"\1\23\1\42\2\uffff\1\25\1\uffff\1\32\1\42\1\uffff\2\32\1\23\1\25"
        u"\1\41\1\122\1\32\1\uffff\1\32\1\uffff\1\32\1\122\2\23\1\32\1\25"
        u"\2\32\1\23\1\32\1\23\1\32\1\23\1\122\1\23\1\122\1\23\2\32\1\122"
        u"\2\32\1\122\1\32\1\41\1\32\1\25\1\32\1\41\1\32\1\25\1\32\1\23\3"
        u"\32\2\23\2\32\2\23\2\32"
        )

    DFA52_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\uffff\1\1\2\uffff\1\4\7\uffff\1\5\1\uffff\1"
        u"\6\54\uffff"
        )

    DFA52_special = DFA.unpack(
        u"\77\uffff"
        )


    DFA52_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\5\6\uffff\1\5\6\uffff\1\4\6\uffff\1\2\1\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\5\6\uffff\1\5\15\uffff\1\10\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13\6\uffff\1\12\6\uffff\1\14"),
        DFA.unpack(u"\1\12\6\uffff\1\15"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\20\7\uffff\1\21\13\uffff\1\22"),
        DFA.unpack(u"\1\23\7\uffff\1\24\76\uffff\1\24"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\27\6\uffff\1\30"),
        DFA.unpack(u"\1\31\7\uffff\1\24\76\uffff\1\24"),
        DFA.unpack(u"\1\33\6\uffff\1\32"),
        DFA.unpack(u"\1\35\6\uffff\1\34"),
        DFA.unpack(u"\1\27\6\uffff\1\15"),
        DFA.unpack(u"\1\36"),
        DFA.unpack(u"\1\27\6\uffff\1\30"),
        DFA.unpack(u"\1\32\6\uffff\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\34\6\uffff\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\33\1\44\5\uffff\1\32"),
        DFA.unpack(u"\1\45\7\uffff\1\46\76\uffff\1\46"),
        DFA.unpack(u"\1\35\1\47\5\uffff\1\34"),
        DFA.unpack(u"\1\50\7\uffff\1\51\76\uffff\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54\6\uffff\1\55"),
        DFA.unpack(u"\1\56\7\uffff\1\46\76\uffff\1\46"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60\6\uffff\1\61"),
        DFA.unpack(u"\1\62\7\uffff\1\51\76\uffff\1\51"),
        DFA.unpack(u"\1\52\6\uffff\1\63"),
        DFA.unpack(u"\1\20\23\uffff\1\22"),
        DFA.unpack(u"\1\54\6\uffff\1\37"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\54\6\uffff\1\55"),
        DFA.unpack(u"\1\20\23\uffff\1\22"),
        DFA.unpack(u"\1\60\6\uffff\1\41"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\60\6\uffff\1\61"),
        DFA.unpack(u"\1\66\5\uffff\1\52"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\71\6\uffff\1\73"),
        DFA.unpack(u"\1\72\6\uffff\1\74"),
        DFA.unpack(u"\1\75\5\uffff\1\71"),
        DFA.unpack(u"\1\76\5\uffff\1\72"),
        DFA.unpack(u"\1\37"),
        DFA.unpack(u"\1\41")
    ]

    # class definition for DFA #52

    class DFA52(DFA):
        pass


    # lookup tables for DFA #55

    DFA55_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA55_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA55_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA55_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\123\1\122\2\uffff\1\32\1\122\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA55_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA55_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA55_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1\6\uffff\1\3"),
        DFA.unpack(u"\1\1\6\uffff\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\6\5\uffff\1\6\1\uffff\1\7\1\6\1\uffff"
        u"\1\6\3\uffff\1\6\4\uffff\1\6\1\uffff\1\6\1\uffff\1\6\53\uffff\1"
        u"\6\1\uffff\1\6"),
        DFA.unpack(u"\1\10\7\uffff\1\11\76\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\14\7\uffff\1\11\76\uffff\1\11"),
        DFA.unpack(u"\1\12\6\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\17\6\uffff\1\20"),
        DFA.unpack(u"\1\21\5\uffff\1\17"),
        DFA.unpack(u"\1\4")
    ]

    # class definition for DFA #55

    class DFA55(DFA):
        pass


    # lookup tables for DFA #60

    DFA60_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA60_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA60_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA60_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\122\1\32\1\122\2\uffff\1\32"
        )

    DFA60_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA60_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA60_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\7\uffff\1\5\76\uffff\1\5"),
        DFA.unpack(u"\1\6\6\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\76\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\6\uffff\1\7")
    ]

    # class definition for DFA #60

    class DFA60(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 22, 24, 35, 37, 81, 83])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 22, 24, 35, 37, 81, 83])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 22, 24, 35, 37, 81, 83])
    FOLLOW_types_in_start94 = frozenset([1, 9, 22, 24, 35, 37, 81, 83])
    FOLLOW_messages_in_start98 = frozenset([1, 9, 22, 24, 35, 37, 81, 83])
    FOLLOW_vars_in_start102 = frozenset([1, 9, 22, 24, 35, 37, 81, 83])
    FOLLOW_trace_in_start106 = frozenset([1, 9, 22, 24, 35, 37, 81, 83])
    FOLLOW_MODULE_in_module125 = frozenset([19])
    FOLLOW_ID_in_module127 = frozenset([26])
    FOLLOW_NEWLINE_in_module129 = frozenset([21])
    FOLLOW_INDENT_in_module131 = frozenset([26])
    FOLLOW_NEWLINE_in_module133 = frozenset([13, 25, 30, 31, 34])
    FOLLOW_module_queue_in_module143 = frozenset([13, 30, 31, 34])
    FOLLOW_proc_in_module155 = frozenset([13, 30, 31, 34])
    FOLLOW_receive_in_module167 = frozenset([13, 31, 34])
    FOLLOW_request_in_module179 = frozenset([13, 34])
    FOLLOW_DEDENT_in_module191 = frozenset([26])
    FOLLOW_NEWLINE_in_module193 = frozenset([1])
    FOLLOW_MODULE_QUEUE_in_module_queue323 = frozenset([19])
    FOLLOW_ID_in_module_queue325 = frozenset([26])
    FOLLOW_NEWLINE_in_module_queue327 = frozenset([1])
    FOLLOW_TRACE_in_trace365 = frozenset([19])
    FOLLOW_ID_in_trace367 = frozenset([26])
    FOLLOW_NEWLINE_in_trace369 = frozenset([1, 21])
    FOLLOW_INDENT_in_trace373 = frozenset([26])
    FOLLOW_NEWLINE_in_trace375 = frozenset([30])
    FOLLOW_proc_in_trace377 = frozenset([13, 30])
    FOLLOW_DEDENT_in_trace381 = frozenset([26])
    FOLLOW_NEWLINE_in_trace383 = frozenset([1])
    FOLLOW_STATELESS_in_stateless429 = frozenset([19])
    FOLLOW_ID_in_stateless431 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless433 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless437 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless439 = frozenset([30])
    FOLLOW_proc_in_stateless441 = frozenset([13, 30])
    FOLLOW_DEDENT_in_stateless445 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless447 = frozenset([1])
    FOLLOW_REQUEST_in_request493 = frozenset([19])
    FOLLOW_ID_in_request495 = frozenset([26])
    FOLLOW_NEWLINE_in_request497 = frozenset([1])
    FOLLOW_REQUEST_in_request526 = frozenset([19])
    FOLLOW_ID_in_request528 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statement_in_request530 = frozenset([1])
    FOLLOW_REQUEST_in_request567 = frozenset([19])
    FOLLOW_ID_in_request569 = frozenset([26])
    FOLLOW_NEWLINE_in_request571 = frozenset([21])
    FOLLOW_INDENT_in_request573 = frozenset([26])
    FOLLOW_NEWLINE_in_request575 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_request577 = frozenset([13])
    FOLLOW_DEDENT_in_request579 = frozenset([26])
    FOLLOW_NEWLINE_in_request581 = frozenset([1])
    FOLLOW_REQUEST_in_request612 = frozenset([19])
    FOLLOW_ID_in_request614 = frozenset([26])
    FOLLOW_NEWLINE_in_request616 = frozenset([21])
    FOLLOW_INDENT_in_request618 = frozenset([26])
    FOLLOW_NEWLINE_in_request620 = frozenset([13, 28, 83])
    FOLLOW_local_vars_in_request634 = frozenset([13, 28])
    FOLLOW_local_ops_in_request638 = frozenset([13])
    FOLLOW_DEDENT_in_request650 = frozenset([26])
    FOLLOW_NEWLINE_in_request652 = frozenset([1])
    FOLLOW_RECEIVE_in_receive698 = frozenset([19])
    FOLLOW_ID_in_receive700 = frozenset([26])
    FOLLOW_NEWLINE_in_receive702 = frozenset([1])
    FOLLOW_RECEIVE_in_receive731 = frozenset([19])
    FOLLOW_ID_in_receive733 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statement_in_receive735 = frozenset([1])
    FOLLOW_RECEIVE_in_receive772 = frozenset([19])
    FOLLOW_ID_in_receive774 = frozenset([26])
    FOLLOW_NEWLINE_in_receive776 = frozenset([21])
    FOLLOW_INDENT_in_receive778 = frozenset([26])
    FOLLOW_NEWLINE_in_receive780 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_receive782 = frozenset([13])
    FOLLOW_DEDENT_in_receive784 = frozenset([26])
    FOLLOW_NEWLINE_in_receive786 = frozenset([1])
    FOLLOW_RECEIVE_in_receive817 = frozenset([19])
    FOLLOW_ID_in_receive819 = frozenset([26])
    FOLLOW_NEWLINE_in_receive821 = frozenset([21])
    FOLLOW_INDENT_in_receive823 = frozenset([26])
    FOLLOW_NEWLINE_in_receive825 = frozenset([13, 28, 83])
    FOLLOW_local_vars_in_receive839 = frozenset([13, 28])
    FOLLOW_local_ops_in_receive843 = frozenset([13])
    FOLLOW_DEDENT_in_receive855 = frozenset([26])
    FOLLOW_NEWLINE_in_receive857 = frozenset([1])
    FOLLOW_PROC_in_proc903 = frozenset([19])
    FOLLOW_ID_in_proc905 = frozenset([26])
    FOLLOW_NEWLINE_in_proc907 = frozenset([1])
    FOLLOW_PROC_in_proc936 = frozenset([19])
    FOLLOW_ID_in_proc938 = frozenset([26])
    FOLLOW_NEWLINE_in_proc940 = frozenset([21])
    FOLLOW_INDENT_in_proc942 = frozenset([26])
    FOLLOW_NEWLINE_in_proc944 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_proc946 = frozenset([13])
    FOLLOW_DEDENT_in_proc948 = frozenset([26])
    FOLLOW_NEWLINE_in_proc950 = frozenset([1])
    FOLLOW_PROC_in_proc981 = frozenset([19])
    FOLLOW_ID_in_proc983 = frozenset([26])
    FOLLOW_NEWLINE_in_proc985 = frozenset([21])
    FOLLOW_INDENT_in_proc987 = frozenset([26])
    FOLLOW_NEWLINE_in_proc989 = frozenset([6, 13, 28, 83])
    FOLLOW_proc_args_in_proc1003 = frozenset([13, 28, 83])
    FOLLOW_local_vars_in_proc1007 = frozenset([13, 28])
    FOLLOW_local_ops_in_proc1011 = frozenset([13])
    FOLLOW_DEDENT_in_proc1023 = frozenset([26])
    FOLLOW_NEWLINE_in_proc1025 = frozenset([1])
    FOLLOW_ARGS_in_proc_args1075 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args1077 = frozenset([1])
    FOLLOW_VARS_in_local_vars1106 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_local_vars1108 = frozenset([1])
    FOLLOW_OPS_in_local_ops1137 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1139 = frozenset([21])
    FOLLOW_INDENT_in_local_ops1141 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1143 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_local_ops1145 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops1147 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1149 = frozenset([1])
    FOLLOW_OPS_in_local_ops1171 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statement_in_local_ops1173 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement1211 = frozenset([26])
    FOLLOW_NEWLINE_in_statement1213 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement1239 = frozenset([1])
    FOLLOW_statement_if_in_statement1249 = frozenset([1])
    FOLLOW_statement_assign_in_statement1259 = frozenset([1])
    FOLLOW_statement_while_in_statement1269 = frozenset([1])
    FOLLOW_statement_with_in_statement1279 = frozenset([1])
    FOLLOW_statement_in_statements1298 = frozenset([1, 18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_WITH_in_statement_with1340 = frozenset([19])
    FOLLOW_ID_in_statement_with1342 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1344 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1354 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1356 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_with1358 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1360 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1362 = frozenset([1])
    FOLLOW_ID_in_statement_assign1402 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1406 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1408 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1412 = frozenset([1])
    FOLLOW_ID_in_statement_assign1465 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1469 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1471 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1473 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1475 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1487 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1491 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_assign1497 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1499 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1552 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1556 = frozenset([19])
    FOLLOW_ID_in_statement_assign1558 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1562 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1615 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1619 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1621 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1623 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1625 = frozenset([19])
    FOLLOW_ID_in_statement_assign1637 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1641 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1647 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1649 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1711 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1713 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1715 = frozenset([15])
    FOLLOW_DO_in_statement_while1719 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1721 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1735 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1737 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_while1739 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1741 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1743 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1783 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1793 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1805 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1913 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1915 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1947 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1949 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1981 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1983 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1987 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1989 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body2003 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body2005 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_elif_body2007 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body2009 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body2011 = frozenset([1])
    FOLLOW_ELSE_in_statement_else2051 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else2053 = frozenset([21])
    FOLLOW_INDENT_in_statement_else2067 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else2069 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_else2071 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else2073 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else2075 = frozenset([1])
    FOLLOW_condition_call_in_condition2113 = frozenset([1])
    FOLLOW_ANY_in_condition2142 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2144 = frozenset([1])
    FOLLOW_ALL_in_condition2173 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2175 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls2213 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls2223 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls2225 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2227 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls2229 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls2233 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2235 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call2269 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call2279 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line2298 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line2300 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2326 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2345 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_single_line2347 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2391 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2393 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2397 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2407 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2409 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2413 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2415 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_call_multi_line2421 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2423 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2459 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_ID_in_arbitrary_value2476 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2486 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2496 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2506 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2516 = frozenset([1])
    FOLLOW_CONSTS_in_consts2535 = frozenset([19])
    FOLLOW_ID_in_consts2537 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2539 = frozenset([21])
    FOLLOW_INDENT_in_consts2549 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2551 = frozenset([19])
    FOLLOW_consts_items_in_consts2553 = frozenset([13])
    FOLLOW_DEDENT_in_consts2555 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2557 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2590 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2606 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2608 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2610 = frozenset([1])
    FOLLOW_ID_in_consts_item2632 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2634 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2636 = frozenset([1])
    FOLLOW_ID_in_consts_item2658 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2660 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2662 = frozenset([1])
    FOLLOW_TYPES_in_types2693 = frozenset([19])
    FOLLOW_ID_in_types2695 = frozenset([26])
    FOLLOW_NEWLINE_in_types2697 = frozenset([21])
    FOLLOW_INDENT_in_types2707 = frozenset([26])
    FOLLOW_NEWLINE_in_types2709 = frozenset([19])
    FOLLOW_types_item_in_types2711 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2715 = frozenset([26])
    FOLLOW_NEWLINE_in_types2717 = frozenset([1])
    FOLLOW_ID_in_types_item2752 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2754 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2781 = frozenset([19])
    FOLLOW_ID_in_messages2783 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2785 = frozenset([21])
    FOLLOW_INDENT_in_messages2795 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2797 = frozenset([19])
    FOLLOW_messages_item_in_messages2799 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2803 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2805 = frozenset([1])
    FOLLOW_ID_in_messages_item2847 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2849 = frozenset([1])
    FOLLOW_ID_in_messages_item2910 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2912 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2914 = frozenset([1])
    FOLLOW_ID_in_messages_item2975 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item2977 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2979 = frozenset([1])
    FOLLOW_ID_in_messages_item3040 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3042 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3044 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3046 = frozenset([33])
    FOLLOW_REPLY_in_messages_item3048 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3050 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3052 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3054 = frozenset([1])
    FOLLOW_ID_in_messages_item3115 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3117 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3119 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3121 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3123 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3125 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3127 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3129 = frozenset([1])
    FOLLOW_ID_in_messages_item3190 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3192 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3194 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3196 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3210 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3212 = frozenset([33])
    FOLLOW_REPLY_in_messages_item3226 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3228 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3238 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3240 = frozenset([1])
    FOLLOW_VARS_in_vars3330 = frozenset([19])
    FOLLOW_ID_in_vars3332 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars3334 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3374 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3376 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints3401 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3413 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3415 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3419 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3421 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3427 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3429 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3458 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3460 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3472 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3474 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3478 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3480 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3486 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3488 = frozenset([1])
    FOLLOW_ID_in_attr_hint3526 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3568 = frozenset([19])
    FOLLOW_ID_in_attr_hint3570 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3611 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3613 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint3615 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3617 = frozenset([19])
    FOLLOW_ID_in_attr_hint3621 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint3625 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint3631 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3679 = frozenset([19])
    FOLLOW_ID_in_hint3681 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint3683 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3703 = frozenset([19])
    FOLLOW_ID_in_hint3705 = frozenset([19, 82])
    FOLLOW_hint_arg_in_hint3707 = frozenset([11, 19, 82])
    FOLLOW_CURLY_CLOSE_in_hint3711 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3750 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3754 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3762 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3766 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3768 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3770 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
