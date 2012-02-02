# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-02 20:28:47

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
                # elements: request, ID, proc, receive, module_queue
                # token labels: 
                # rule labels: retval
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
    # grammar/ShyRecognizerFrontend.g:56:1: request : ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) );
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REQUEST38 = None
        ID39 = None
        NEWLINE40 = None
        REQUEST41 = None
        ID42 = None
        NEWLINE43 = None
        INDENT44 = None
        NEWLINE45 = None
        DEDENT47 = None
        NEWLINE48 = None
        REQUEST49 = None
        ID50 = None
        NEWLINE51 = None
        INDENT52 = None
        NEWLINE53 = None
        DEDENT56 = None
        NEWLINE57 = None
        statements46 = None

        local_vars54 = None

        local_ops55 = None


        REQUEST38_tree = None
        ID39_tree = None
        NEWLINE40_tree = None
        REQUEST41_tree = None
        ID42_tree = None
        NEWLINE43_tree = None
        INDENT44_tree = None
        NEWLINE45_tree = None
        DEDENT47_tree = None
        NEWLINE48_tree = None
        REQUEST49_tree = None
        ID50_tree = None
        NEWLINE51_tree = None
        INDENT52_tree = None
        NEWLINE53_tree = None
        DEDENT56_tree = None
        NEWLINE57_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:57:5: ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) )
                alt12 = 3
                LA12_0 = self.input.LA(1)

                if (LA12_0 == REQUEST) :
                    LA12_1 = self.input.LA(2)

                    if (LA12_1 == ID) :
                        LA12_2 = self.input.LA(3)

                        if (LA12_2 == NEWLINE) :
                            LA12_3 = self.input.LA(4)

                            if (LA12_3 == INDENT) :
                                LA12_4 = self.input.LA(5)

                                if (LA12_4 == NEWLINE) :
                                    LA12_6 = self.input.LA(6)

                                    if ((EXPRESSION <= LA12_6 <= IF) or LA12_6 == MINUS or LA12_6 == NUMBER or LA12_6 == STRING or LA12_6 == WHILE or LA12_6 == WITH) :
                                        alt12 = 2
                                    elif (LA12_6 == DEDENT or LA12_6 == OPS or LA12_6 == VARS) :
                                        alt12 = 3
                                    else:
                                        nvae = NoViableAltException("", 12, 6, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 12, 4, self.input)

                                    raise nvae


                            elif (LA12_3 == DEDENT or LA12_3 == REQUEST) :
                                alt12 = 1
                            else:
                                nvae = NoViableAltException("", 12, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerFrontend.g:59:9: REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    REQUEST41 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request526) 
                    stream_REQUEST.add(REQUEST41)


                    ID42 = self.match(self.input, ID, self.FOLLOW_ID_in_request528) 
                    stream_ID.add(ID42)


                    NEWLINE43 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request530) 
                    stream_NEWLINE.add(NEWLINE43)


                    INDENT44 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request532) 
                    stream_INDENT.add(INDENT44)


                    NEWLINE45 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request534) 
                    stream_NEWLINE.add(NEWLINE45)


                    self._state.following.append(self.FOLLOW_statements_in_request536)
                    statements46 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements46.tree)


                    DEDENT47 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request538) 
                    stream_DEDENT.add(DEDENT47)


                    NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request540) 
                    stream_NEWLINE.add(NEWLINE48)


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
                    # 60:9: -> ^( TREE_REQUEST ID statements )
                    # grammar/ShyRecognizerFrontend.g:60:13: ^( TREE_REQUEST ID statements )
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




                elif alt12 == 3:
                    # grammar/ShyRecognizerFrontend.g:61:9: REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    REQUEST49 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request571) 
                    stream_REQUEST.add(REQUEST49)


                    ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_request573) 
                    stream_ID.add(ID50)


                    NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request575) 
                    stream_NEWLINE.add(NEWLINE51)


                    INDENT52 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request577) 
                    stream_INDENT.add(INDENT52)


                    NEWLINE53 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request579) 
                    stream_NEWLINE.add(NEWLINE53)


                    # grammar/ShyRecognizerFrontend.g:62:13: ( local_vars )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == VARS) :
                        alt10 = 1
                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:62:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_request593)
                        local_vars54 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars54.tree)





                    # grammar/ShyRecognizerFrontend.g:62:26: ( local_ops )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == OPS) :
                        alt11 = 1
                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:62:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_request597)
                        local_ops55 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops55.tree)





                    DEDENT56 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request609) 
                    stream_DEDENT.add(DEDENT56)


                    NEWLINE57 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request611) 
                    stream_NEWLINE.add(NEWLINE57)


                    # AST Rewrite
                    # elements: local_ops, ID, local_vars
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 64:9: -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:64:13: ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:64:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:64:45: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:67:1: receive : ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) );
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECEIVE58 = None
        ID59 = None
        NEWLINE60 = None
        RECEIVE61 = None
        ID62 = None
        NEWLINE63 = None
        INDENT64 = None
        NEWLINE65 = None
        DEDENT67 = None
        NEWLINE68 = None
        RECEIVE69 = None
        ID70 = None
        NEWLINE71 = None
        INDENT72 = None
        NEWLINE73 = None
        DEDENT76 = None
        NEWLINE77 = None
        statements66 = None

        local_vars74 = None

        local_ops75 = None


        RECEIVE58_tree = None
        ID59_tree = None
        NEWLINE60_tree = None
        RECEIVE61_tree = None
        ID62_tree = None
        NEWLINE63_tree = None
        INDENT64_tree = None
        NEWLINE65_tree = None
        DEDENT67_tree = None
        NEWLINE68_tree = None
        RECEIVE69_tree = None
        ID70_tree = None
        NEWLINE71_tree = None
        INDENT72_tree = None
        NEWLINE73_tree = None
        DEDENT76_tree = None
        NEWLINE77_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_RECEIVE = RewriteRuleTokenStream(self._adaptor, "token RECEIVE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:68:5: ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) )
                alt15 = 3
                LA15_0 = self.input.LA(1)

                if (LA15_0 == RECEIVE) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == ID) :
                        LA15_2 = self.input.LA(3)

                        if (LA15_2 == NEWLINE) :
                            LA15_3 = self.input.LA(4)

                            if (LA15_3 == INDENT) :
                                LA15_4 = self.input.LA(5)

                                if (LA15_4 == NEWLINE) :
                                    LA15_6 = self.input.LA(6)

                                    if ((EXPRESSION <= LA15_6 <= IF) or LA15_6 == MINUS or LA15_6 == NUMBER or LA15_6 == STRING or LA15_6 == WHILE or LA15_6 == WITH) :
                                        alt15 = 2
                                    elif (LA15_6 == DEDENT or LA15_6 == OPS or LA15_6 == VARS) :
                                        alt15 = 3
                                    else:
                                        nvae = NoViableAltException("", 15, 6, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 15, 4, self.input)

                                    raise nvae


                            elif (LA15_3 == DEDENT or LA15_3 == RECEIVE or LA15_3 == REQUEST) :
                                alt15 = 1
                            else:
                                nvae = NoViableAltException("", 15, 3, self.input)

                                raise nvae


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
                    # grammar/ShyRecognizerFrontend.g:68:9: RECEIVE ID NEWLINE
                    pass 
                    RECEIVE58 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive657) 
                    stream_RECEIVE.add(RECEIVE58)


                    ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_receive659) 
                    stream_ID.add(ID59)


                    NEWLINE60 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive661) 
                    stream_NEWLINE.add(NEWLINE60)


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
                    # 69:9: -> ^( TREE_RECEIVE ID )
                    # grammar/ShyRecognizerFrontend.g:69:13: ^( TREE_RECEIVE ID )
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
                    # grammar/ShyRecognizerFrontend.g:70:9: RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    RECEIVE61 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive690) 
                    stream_RECEIVE.add(RECEIVE61)


                    ID62 = self.match(self.input, ID, self.FOLLOW_ID_in_receive692) 
                    stream_ID.add(ID62)


                    NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive694) 
                    stream_NEWLINE.add(NEWLINE63)


                    INDENT64 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive696) 
                    stream_INDENT.add(INDENT64)


                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive698) 
                    stream_NEWLINE.add(NEWLINE65)


                    self._state.following.append(self.FOLLOW_statements_in_receive700)
                    statements66 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements66.tree)


                    DEDENT67 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive702) 
                    stream_DEDENT.add(DEDENT67)


                    NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive704) 
                    stream_NEWLINE.add(NEWLINE68)


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
                    # 71:9: -> ^( TREE_RECEIVE ID statements )
                    # grammar/ShyRecognizerFrontend.g:71:13: ^( TREE_RECEIVE ID statements )
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




                elif alt15 == 3:
                    # grammar/ShyRecognizerFrontend.g:72:9: RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    RECEIVE69 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive735) 
                    stream_RECEIVE.add(RECEIVE69)


                    ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_receive737) 
                    stream_ID.add(ID70)


                    NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive739) 
                    stream_NEWLINE.add(NEWLINE71)


                    INDENT72 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive741) 
                    stream_INDENT.add(INDENT72)


                    NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive743) 
                    stream_NEWLINE.add(NEWLINE73)


                    # grammar/ShyRecognizerFrontend.g:73:13: ( local_vars )?
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == VARS) :
                        alt13 = 1
                    if alt13 == 1:
                        # grammar/ShyRecognizerFrontend.g:73:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_receive757)
                        local_vars74 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars74.tree)





                    # grammar/ShyRecognizerFrontend.g:73:26: ( local_ops )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == OPS) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:73:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_receive761)
                        local_ops75 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops75.tree)





                    DEDENT76 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive773) 
                    stream_DEDENT.add(DEDENT76)


                    NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive775) 
                    stream_NEWLINE.add(NEWLINE77)


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
                    # 75:9: -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:75:13: ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:75:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:75:45: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:78:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC78 = None
        ID79 = None
        NEWLINE80 = None
        PROC81 = None
        ID82 = None
        NEWLINE83 = None
        INDENT84 = None
        NEWLINE85 = None
        DEDENT87 = None
        NEWLINE88 = None
        PROC89 = None
        ID90 = None
        NEWLINE91 = None
        INDENT92 = None
        NEWLINE93 = None
        DEDENT97 = None
        NEWLINE98 = None
        statements86 = None

        proc_args94 = None

        local_vars95 = None

        local_ops96 = None


        PROC78_tree = None
        ID79_tree = None
        NEWLINE80_tree = None
        PROC81_tree = None
        ID82_tree = None
        NEWLINE83_tree = None
        INDENT84_tree = None
        NEWLINE85_tree = None
        DEDENT87_tree = None
        NEWLINE88_tree = None
        PROC89_tree = None
        ID90_tree = None
        NEWLINE91_tree = None
        INDENT92_tree = None
        NEWLINE93_tree = None
        DEDENT97_tree = None
        NEWLINE98_tree = None
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
                # grammar/ShyRecognizerFrontend.g:79:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) )
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
                    # grammar/ShyRecognizerFrontend.g:79:9: PROC ID NEWLINE
                    pass 
                    PROC78 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc821) 
                    stream_PROC.add(PROC78)


                    ID79 = self.match(self.input, ID, self.FOLLOW_ID_in_proc823) 
                    stream_ID.add(ID79)


                    NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc825) 
                    stream_NEWLINE.add(NEWLINE80)


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
                    # 80:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:80:13: ^( TREE_PROC ID )
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
                    # grammar/ShyRecognizerFrontend.g:81:9: PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    PROC81 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc854) 
                    stream_PROC.add(PROC81)


                    ID82 = self.match(self.input, ID, self.FOLLOW_ID_in_proc856) 
                    stream_ID.add(ID82)


                    NEWLINE83 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc858) 
                    stream_NEWLINE.add(NEWLINE83)


                    INDENT84 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc860) 
                    stream_INDENT.add(INDENT84)


                    NEWLINE85 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc862) 
                    stream_NEWLINE.add(NEWLINE85)


                    self._state.following.append(self.FOLLOW_statements_in_proc864)
                    statements86 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements86.tree)


                    DEDENT87 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc866) 
                    stream_DEDENT.add(DEDENT87)


                    NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc868) 
                    stream_NEWLINE.add(NEWLINE88)


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
                    # 82:9: -> ^( TREE_PROC ID statements )
                    # grammar/ShyRecognizerFrontend.g:82:13: ^( TREE_PROC ID statements )
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
                    # grammar/ShyRecognizerFrontend.g:83:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    PROC89 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc899) 
                    stream_PROC.add(PROC89)


                    ID90 = self.match(self.input, ID, self.FOLLOW_ID_in_proc901) 
                    stream_ID.add(ID90)


                    NEWLINE91 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc903) 
                    stream_NEWLINE.add(NEWLINE91)


                    INDENT92 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc905) 
                    stream_INDENT.add(INDENT92)


                    NEWLINE93 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc907) 
                    stream_NEWLINE.add(NEWLINE93)


                    # grammar/ShyRecognizerFrontend.g:84:13: ( proc_args )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == ARGS) :
                        alt16 = 1
                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:84:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc921)
                        proc_args94 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args94.tree)





                    # grammar/ShyRecognizerFrontend.g:84:25: ( local_vars )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == VARS) :
                        alt17 = 1
                    if alt17 == 1:
                        # grammar/ShyRecognizerFrontend.g:84:25: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_proc925)
                        local_vars95 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars95.tree)





                    # grammar/ShyRecognizerFrontend.g:84:38: ( local_ops )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == OPS) :
                        alt18 = 1
                    if alt18 == 1:
                        # grammar/ShyRecognizerFrontend.g:84:38: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_proc929)
                        local_ops96 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops96.tree)





                    DEDENT97 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc941) 
                    stream_DEDENT.add(DEDENT97)


                    NEWLINE98 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc943) 
                    stream_NEWLINE.add(NEWLINE98)


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
                    # 86:9: -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:86:13: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:86:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:86:41: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:86:54: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:89:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS99 = None
        attrs_hints100 = None


        ARGS99_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:90:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:90:9: ARGS attrs_hints
                pass 
                ARGS99 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args993) 
                stream_ARGS.add(ARGS99)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args995)
                attrs_hints100 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints100.tree)


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
                # 90:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:90:29: ^( TREE_PROC_ARGS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:93:1: local_vars : VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        retval = self.local_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS101 = None
        attrs_hints102 = None


        VARS101_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:94:5: ( VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:94:9: VARS attrs_hints
                pass 
                VARS101 = self.match(self.input, VARS, self.FOLLOW_VARS_in_local_vars1024) 
                stream_VARS.add(VARS101)


                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars1026)
                attrs_hints102 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints102.tree)


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
                # 94:26: -> ^( TREE_LOCAL_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:94:29: ^( TREE_LOCAL_VARS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:97:1: local_ops : ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements | OPS statement -> ^( TREE_STATEMENTS statement ) );
    def local_ops(self, ):
        retval = self.local_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS103 = None
        NEWLINE104 = None
        INDENT105 = None
        NEWLINE106 = None
        DEDENT108 = None
        NEWLINE109 = None
        OPS110 = None
        statements107 = None

        statement111 = None


        OPS103_tree = None
        NEWLINE104_tree = None
        INDENT105_tree = None
        NEWLINE106_tree = None
        DEDENT108_tree = None
        NEWLINE109_tree = None
        OPS110_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:98:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements | OPS statement -> ^( TREE_STATEMENTS statement ) )
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
                    # grammar/ShyRecognizerFrontend.g:98:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    OPS103 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops1055) 
                    stream_OPS.add(OPS103)


                    NEWLINE104 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1057) 
                    stream_NEWLINE.add(NEWLINE104)


                    INDENT105 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_local_ops1059) 
                    stream_INDENT.add(INDENT105)


                    NEWLINE106 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1061) 
                    stream_NEWLINE.add(NEWLINE106)


                    self._state.following.append(self.FOLLOW_statements_in_local_ops1063)
                    statements107 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements107.tree)


                    DEDENT108 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_local_ops1065) 
                    stream_DEDENT.add(DEDENT108)


                    NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1067) 
                    stream_NEWLINE.add(NEWLINE109)


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
                    # 99:9: -> statements
                    self._adaptor.addChild(root_0, stream_statements.nextTree())




                    retval.tree = root_0




                elif alt20 == 2:
                    # grammar/ShyRecognizerFrontend.g:100:9: OPS statement
                    pass 
                    OPS110 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops1089) 
                    stream_OPS.add(OPS110)


                    self._state.following.append(self.FOLLOW_statement_in_local_ops1091)
                    statement111 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement111.tree)


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
                    # 101:9: -> ^( TREE_STATEMENTS statement )
                    # grammar/ShyRecognizerFrontend.g:101:13: ^( TREE_STATEMENTS statement )
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
    # grammar/ShyRecognizerFrontend.g:104:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE113 = None
        statement_call_single_line112 = None

        statement_call_multi_line114 = None

        statement_if115 = None

        statement_assign116 = None

        statement_while117 = None

        statement_with118 = None


        NEWLINE113_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:105:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt21 = 6
                alt21 = self.dfa21.predict(self.input)
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:105:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement1129)
                    statement_call_single_line112 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line112.tree)


                    NEWLINE113 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement1131) 
                    stream_NEWLINE.add(NEWLINE113)


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
                    # 106:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt21 == 2:
                    # grammar/ShyRecognizerFrontend.g:107:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement1157)
                    statement_call_multi_line114 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line114.tree)



                elif alt21 == 3:
                    # grammar/ShyRecognizerFrontend.g:108:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement1167)
                    statement_if115 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if115.tree)



                elif alt21 == 4:
                    # grammar/ShyRecognizerFrontend.g:109:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1177)
                    statement_assign116 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign116.tree)



                elif alt21 == 5:
                    # grammar/ShyRecognizerFrontend.g:110:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement1187)
                    statement_while117 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while117.tree)



                elif alt21 == 6:
                    # grammar/ShyRecognizerFrontend.g:111:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement1197)
                    statement_with118 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with118.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:114:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement119 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:115:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:115:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:115:9: ( statement )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= IF) or LA22_0 == MINUS or LA22_0 == NUMBER or LA22_0 == STRING or LA22_0 == WHILE or LA22_0 == WITH) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerFrontend.g:115:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1216)
                        statement119 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement119.tree)



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
                # 116:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:116:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:116:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:119:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH120 = None
        ID121 = None
        NEWLINE122 = None
        INDENT123 = None
        NEWLINE124 = None
        DEDENT126 = None
        NEWLINE127 = None
        statements125 = None


        WITH120_tree = None
        ID121_tree = None
        NEWLINE122_tree = None
        INDENT123_tree = None
        NEWLINE124_tree = None
        DEDENT126_tree = None
        NEWLINE127_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:120:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:120:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH120 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1258) 
                stream_WITH.add(WITH120)


                ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1260) 
                stream_ID.add(ID121)


                NEWLINE122 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1262) 
                stream_NEWLINE.add(NEWLINE122)


                INDENT123 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1272) 
                stream_INDENT.add(INDENT123)


                NEWLINE124 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1274) 
                stream_NEWLINE.add(NEWLINE124)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1276)
                statements125 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements125.tree)


                DEDENT126 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1278) 
                stream_DEDENT.add(DEDENT126)


                NEWLINE127 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1280) 
                stream_NEWLINE.add(NEWLINE127)


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
                # 122:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:122:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:125:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID128 = None
        ARROW_LEFT129 = None
        NEWLINE131 = None
        ID132 = None
        ARROW_LEFT133 = None
        NEWLINE134 = None
        INDENT135 = None
        NEWLINE136 = None
        NEWLINE138 = None
        DEDENT139 = None
        NEWLINE140 = None
        ARROW_RIGHT142 = None
        ID143 = None
        NEWLINE144 = None
        ARROW_RIGHT146 = None
        NEWLINE147 = None
        INDENT148 = None
        NEWLINE149 = None
        ID150 = None
        NEWLINE151 = None
        DEDENT152 = None
        NEWLINE153 = None
        arbitrary_value130 = None

        arbitrary_value137 = None

        arbitrary_value141 = None

        arbitrary_value145 = None


        ID128_tree = None
        ARROW_LEFT129_tree = None
        NEWLINE131_tree = None
        ID132_tree = None
        ARROW_LEFT133_tree = None
        NEWLINE134_tree = None
        INDENT135_tree = None
        NEWLINE136_tree = None
        NEWLINE138_tree = None
        DEDENT139_tree = None
        NEWLINE140_tree = None
        ARROW_RIGHT142_tree = None
        ID143_tree = None
        NEWLINE144_tree = None
        ARROW_RIGHT146_tree = None
        NEWLINE147_tree = None
        INDENT148_tree = None
        NEWLINE149_tree = None
        ID150_tree = None
        NEWLINE151_tree = None
        DEDENT152_tree = None
        NEWLINE153_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:126:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt33 = 4
                alt33 = self.dfa33.predict(self.input)
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:126:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:126:9: ( ID )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == ID) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:9: ID
                            pass 
                            ID128 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1320) 
                            stream_ID.add(ID128)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    ARROW_LEFT129 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1324) 
                    stream_ARROW_LEFT.add(ARROW_LEFT129)


                    # grammar/ShyRecognizerFrontend.g:126:25: ( arbitrary_value )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER or LA24_0 == STRING) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1326)
                            arbitrary_value130 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value130.tree)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    NEWLINE131 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1330) 
                    stream_NEWLINE.add(NEWLINE131)


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




                elif alt33 == 2:
                    # grammar/ShyRecognizerFrontend.g:129:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:129:9: ( ID )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == ID) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:129:9: ID
                            pass 
                            ID132 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1383) 
                            stream_ID.add(ID132)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    ARROW_LEFT133 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1387) 
                    stream_ARROW_LEFT.add(ARROW_LEFT133)


                    NEWLINE134 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1389) 
                    stream_NEWLINE.add(NEWLINE134)


                    INDENT135 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1391) 
                    stream_INDENT.add(INDENT135)


                    NEWLINE136 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1393) 
                    stream_NEWLINE.add(NEWLINE136)


                    # grammar/ShyRecognizerFrontend.g:130:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA27_0 <= ID) or LA27_0 == MINUS or LA27_0 == NUMBER or LA27_0 == STRING) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:130:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:130:11: ( arbitrary_value )+
                            cnt26 = 0
                            while True: #loop26
                                alt26 = 2
                                LA26_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA26_0 <= ID) or LA26_0 == MINUS or LA26_0 == NUMBER or LA26_0 == STRING) :
                                    alt26 = 1


                                if alt26 == 1:
                                    # grammar/ShyRecognizerFrontend.g:130:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1405)
                                    arbitrary_value137 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value137.tree)



                                else:
                                    if cnt26 >= 1:
                                        break #loop26

                                    eee = EarlyExitException(26, self.input)
                                    raise eee

                                cnt26 += 1


                            NEWLINE138 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1409) 
                            stream_NEWLINE.add(NEWLINE138)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    DEDENT139 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1415) 
                    stream_DEDENT.add(DEDENT139)


                    NEWLINE140 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1417) 
                    stream_NEWLINE.add(NEWLINE140)


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




                elif alt33 == 3:
                    # grammar/ShyRecognizerFrontend.g:133:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:133:9: ( arbitrary_value )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA28_0 <= ID) or LA28_0 == MINUS or LA28_0 == NUMBER or LA28_0 == STRING) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:133:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1470)
                            arbitrary_value141 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value141.tree)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    ARROW_RIGHT142 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1474) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT142)


                    # grammar/ShyRecognizerFrontend.g:133:39: ( ID )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:133:39: ID
                            pass 
                            ID143 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1476) 
                            stream_ID.add(ID143)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    NEWLINE144 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1480) 
                    stream_NEWLINE.add(NEWLINE144)


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
                    # 134:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:134:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:134:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:135:42: ( ID )+
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
                    # grammar/ShyRecognizerFrontend.g:136:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:136:9: ( arbitrary_value )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA30_0 <= ID) or LA30_0 == MINUS or LA30_0 == NUMBER or LA30_0 == STRING) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:136:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1533)
                            arbitrary_value145 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value145.tree)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


                    ARROW_RIGHT146 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1537) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT146)


                    NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1539) 
                    stream_NEWLINE.add(NEWLINE147)


                    INDENT148 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1541) 
                    stream_INDENT.add(INDENT148)


                    NEWLINE149 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1543) 
                    stream_NEWLINE.add(NEWLINE149)


                    # grammar/ShyRecognizerFrontend.g:137:9: ( ( ID )+ NEWLINE )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:137:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:137:11: ( ID )+
                            cnt31 = 0
                            while True: #loop31
                                alt31 = 2
                                LA31_0 = self.input.LA(1)

                                if (LA31_0 == ID) :
                                    alt31 = 1


                                if alt31 == 1:
                                    # grammar/ShyRecognizerFrontend.g:137:11: ID
                                    pass 
                                    ID150 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1555) 
                                    stream_ID.add(ID150)



                                else:
                                    if cnt31 >= 1:
                                        break #loop31

                                    eee = EarlyExitException(31, self.input)
                                    raise eee

                                cnt31 += 1


                            NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1559) 
                            stream_NEWLINE.add(NEWLINE151)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


                    DEDENT152 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1565) 
                    stream_DEDENT.add(DEDENT152)


                    NEWLINE153 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1567) 
                    stream_NEWLINE.add(NEWLINE153)


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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:142:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE154 = None
        NEWLINE156 = None
        DO157 = None
        NEWLINE158 = None
        INDENT159 = None
        NEWLINE160 = None
        DEDENT162 = None
        NEWLINE163 = None
        condition155 = None

        statements161 = None


        WHILE154_tree = None
        NEWLINE156_tree = None
        DO157_tree = None
        NEWLINE158_tree = None
        INDENT159_tree = None
        NEWLINE160_tree = None
        DEDENT162_tree = None
        NEWLINE163_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:143:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:143:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE154 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1629) 
                stream_WHILE.add(WHILE154)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1631)
                condition155 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition155.tree)


                # grammar/ShyRecognizerFrontend.g:143:25: ( NEWLINE )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == NEWLINE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:143:25: NEWLINE
                    pass 
                    NEWLINE156 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1633) 
                    stream_NEWLINE.add(NEWLINE156)





                DO157 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1637) 
                stream_DO.add(DO157)


                NEWLINE158 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1639) 
                stream_NEWLINE.add(NEWLINE158)


                INDENT159 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1653) 
                stream_INDENT.add(INDENT159)


                NEWLINE160 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1655) 
                stream_NEWLINE.add(NEWLINE160)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1657)
                statements161 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements161.tree)


                DEDENT162 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1659) 
                stream_DEDENT.add(DEDENT162)


                NEWLINE163 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1661) 
                stream_NEWLINE.add(NEWLINE163)


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
                # 145:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:145:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:148:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head164 = None

        statement_elif165 = None

        statement_else166 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:149:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:149:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1701)
                statement_if_head164 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head164.tree)


                # grammar/ShyRecognizerFrontend.g:150:9: ( statement_elif )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == ELIF) :
                        alt35 = 1


                    if alt35 == 1:
                        # grammar/ShyRecognizerFrontend.g:150:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1711)
                        statement_elif165 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif165.tree)



                    else:
                        break #loop35


                # grammar/ShyRecognizerFrontend.g:151:9: ( statement_else )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == ELSE) :
                    alt36 = 1
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:151:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1723)
                    statement_else166 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else166.tree)





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
                # 152:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:152:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:154:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:155:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:159:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF167 = None
        statement_elif_body168 = None


        IF167_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:160:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:160:9: IF statement_elif_body
                pass 
                IF167 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1831) 
                stream_IF.add(IF167)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1833)
                statement_elif_body168 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body168.tree)


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
                # 161:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:164:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF169 = None
        statement_elif_body170 = None


        ELIF169_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:165:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:165:9: ELIF statement_elif_body
                pass 
                ELIF169 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1865) 
                stream_ELIF.add(ELIF169)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1867)
                statement_elif_body170 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body170.tree)


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
                # 166:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:169:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE172 = None
        DO173 = None
        NEWLINE174 = None
        INDENT175 = None
        NEWLINE176 = None
        DEDENT178 = None
        NEWLINE179 = None
        condition171 = None

        statements177 = None


        NEWLINE172_tree = None
        DO173_tree = None
        NEWLINE174_tree = None
        INDENT175_tree = None
        NEWLINE176_tree = None
        DEDENT178_tree = None
        NEWLINE179_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:170:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:170:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1899)
                condition171 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition171.tree)


                # grammar/ShyRecognizerFrontend.g:170:19: ( NEWLINE )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == NEWLINE) :
                    alt37 = 1
                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:170:19: NEWLINE
                    pass 
                    NEWLINE172 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1901) 
                    stream_NEWLINE.add(NEWLINE172)





                DO173 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1905) 
                stream_DO.add(DO173)


                NEWLINE174 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1907) 
                stream_NEWLINE.add(NEWLINE174)


                INDENT175 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1921) 
                stream_INDENT.add(INDENT175)


                NEWLINE176 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1923) 
                stream_NEWLINE.add(NEWLINE176)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1925)
                statements177 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements177.tree)


                DEDENT178 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1927) 
                stream_DEDENT.add(DEDENT178)


                NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1929) 
                stream_NEWLINE.add(NEWLINE179)


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
                # 172:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:172:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:175:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE180 = None
        NEWLINE181 = None
        INDENT182 = None
        NEWLINE183 = None
        DEDENT185 = None
        NEWLINE186 = None
        statements184 = None


        ELSE180_tree = None
        NEWLINE181_tree = None
        INDENT182_tree = None
        NEWLINE183_tree = None
        DEDENT185_tree = None
        NEWLINE186_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:176:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:176:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE180 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1969) 
                stream_ELSE.add(ELSE180)


                NEWLINE181 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1971) 
                stream_NEWLINE.add(NEWLINE181)


                INDENT182 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1985) 
                stream_INDENT.add(INDENT182)


                NEWLINE183 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1987) 
                stream_NEWLINE.add(NEWLINE183)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1989)
                statements184 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements184.tree)


                DEDENT185 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1991) 
                stream_DEDENT.add(DEDENT185)


                NEWLINE186 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1993) 
                stream_NEWLINE.add(NEWLINE186)


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
                # 178:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:178:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:181:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY188 = None
        ALL190 = None
        condition_call187 = None

        condition_calls189 = None

        condition_calls191 = None


        ANY188_tree = None
        ALL190_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:182:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
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
                    # grammar/ShyRecognizerFrontend.g:182:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition2031)
                    condition_call187 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call187.tree)


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
                    # 183:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:183:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:184:9: ANY condition_calls
                    pass 
                    ANY188 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition2060) 
                    stream_ANY.add(ANY188)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2062)
                    condition_calls189 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls189.tree)


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
                    # 185:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:185:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt38 == 3:
                    # grammar/ShyRecognizerFrontend.g:186:9: ALL condition_calls
                    pass 
                    ALL190 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition2091) 
                    stream_ALL.add(ALL190)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2093)
                    condition_calls191 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls191.tree)


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
                    # 187:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:187:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:190:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE193 = None
        INDENT194 = None
        NEWLINE195 = None
        DEDENT197 = None
        NEWLINE198 = None
        condition_call192 = None

        condition_call_line196 = None


        NEWLINE193_tree = None
        INDENT194_tree = None
        NEWLINE195_tree = None
        DEDENT197_tree = None
        NEWLINE198_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:191:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
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
                    # grammar/ShyRecognizerFrontend.g:191:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls2131)
                    condition_call192 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call192.tree)



                elif alt40 == 2:
                    # grammar/ShyRecognizerFrontend.g:192:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE193 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2141) 
                    stream_NEWLINE.add(NEWLINE193)


                    INDENT194 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls2143) 
                    stream_INDENT.add(INDENT194)


                    NEWLINE195 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2145) 
                    stream_NEWLINE.add(NEWLINE195)


                    # grammar/ShyRecognizerFrontend.g:192:32: ( condition_call_line )+
                    cnt39 = 0
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == ID) :
                            alt39 = 1


                        if alt39 == 1:
                            # grammar/ShyRecognizerFrontend.g:192:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls2147)
                            condition_call_line196 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line196.tree)



                        else:
                            if cnt39 >= 1:
                                break #loop39

                            eee = EarlyExitException(39, self.input)
                            raise eee

                        cnt39 += 1


                    DEDENT197 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls2151) 
                    stream_DEDENT.add(DEDENT197)


                    NEWLINE198 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2153) 
                    stream_NEWLINE.add(NEWLINE198)


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
                    # 193:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:193:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:196:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line199 = None

        statement_call_multi_line200 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:197:5: ( statement_call_single_line | statement_call_multi_line )
                alt41 = 2
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:197:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call2187)
                    statement_call_single_line199 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line199.tree)



                elif alt41 == 2:
                    # grammar/ShyRecognizerFrontend.g:198:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call2197)
                    statement_call_multi_line200 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line200.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:201:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE202 = None
        statement_call_single_line201 = None

        statement_call_multi_line203 = None


        NEWLINE202_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:202:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt42 = 2
                alt42 = self.dfa42.predict(self.input)
                if alt42 == 1:
                    # grammar/ShyRecognizerFrontend.g:202:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line2216)
                    statement_call_single_line201 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line201.tree)


                    NEWLINE202 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line2218) 
                    stream_NEWLINE.add(NEWLINE202)


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
                    # 203:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt42 == 2:
                    # grammar/ShyRecognizerFrontend.g:204:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2244)
                    statement_call_multi_line203 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line203.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:207:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID204 = None
        statement_call_args205 = None


        ID204_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:208:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:208:9: ID ( statement_call_args )?
                pass 
                ID204 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2263) 
                stream_ID.add(ID204)


                # grammar/ShyRecognizerFrontend.g:208:12: ( statement_call_args )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER or LA43_0 == STRING) :
                    alt43 = 1
                if alt43 == 1:
                    # grammar/ShyRecognizerFrontend.g:208:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2265)
                    statement_call_args205 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args205.tree)





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
                # 209:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:209:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:209:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:212:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID206 = None
        NEWLINE208 = None
        INDENT209 = None
        NEWLINE210 = None
        NEWLINE212 = None
        DEDENT213 = None
        NEWLINE214 = None
        statement_call_args207 = None

        statement_call_args211 = None


        ID206_tree = None
        NEWLINE208_tree = None
        INDENT209_tree = None
        NEWLINE210_tree = None
        NEWLINE212_tree = None
        DEDENT213_tree = None
        NEWLINE214_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:213:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:213:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID206 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2309) 
                stream_ID.add(ID206)


                # grammar/ShyRecognizerFrontend.g:213:12: ( statement_call_args )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if ((EXPRESSION <= LA44_0 <= ID) or LA44_0 == MINUS or LA44_0 == NUMBER or LA44_0 == STRING) :
                    alt44 = 1
                if alt44 == 1:
                    # grammar/ShyRecognizerFrontend.g:213:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2311)
                    statement_call_args207 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args207.tree)





                NEWLINE208 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2315) 
                stream_NEWLINE.add(NEWLINE208)


                INDENT209 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2325) 
                stream_INDENT.add(INDENT209)


                NEWLINE210 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2327) 
                stream_NEWLINE.add(NEWLINE210)


                # grammar/ShyRecognizerFrontend.g:214:24: ( statement_call_args NEWLINE )+
                cnt45 = 0
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA45_0 <= ID) or LA45_0 == MINUS or LA45_0 == NUMBER or LA45_0 == STRING) :
                        alt45 = 1


                    if alt45 == 1:
                        # grammar/ShyRecognizerFrontend.g:214:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2331)
                        statement_call_args211 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args211.tree)


                        NEWLINE212 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2333) 
                        stream_NEWLINE.add(NEWLINE212)



                    else:
                        if cnt45 >= 1:
                            break #loop45

                        eee = EarlyExitException(45, self.input)
                        raise eee

                    cnt45 += 1


                DEDENT213 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2339) 
                stream_DEDENT.add(DEDENT213)


                NEWLINE214 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2341) 
                stream_NEWLINE.add(NEWLINE214)


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
                # 215:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:215:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:215:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:218:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value215 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:218:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:218:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:218:23: ( arbitrary_value )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA46_0 <= ID) or LA46_0 == MINUS or LA46_0 == NUMBER or LA46_0 == STRING) :
                        alt46 = 1


                    if alt46 == 1:
                        # grammar/ShyRecognizerFrontend.g:218:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2377)
                        arbitrary_value215 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value215.tree)



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
    # grammar/ShyRecognizerFrontend.g:220:1: arbitrary_value : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID216 = None
        EXPRESSION217 = None
        STRING218 = None
        num_whole219 = None

        num_fract220 = None


        ID216_tree = None
        EXPRESSION217_tree = None
        STRING218_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:221:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:221:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID216 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2394)
                    ID216_tree = self._adaptor.createWithPayload(ID216)
                    self._adaptor.addChild(root_0, ID216_tree)




                elif alt47 == 2:
                    # grammar/ShyRecognizerFrontend.g:222:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION217 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2404)
                    EXPRESSION217_tree = self._adaptor.createWithPayload(EXPRESSION217)
                    self._adaptor.addChild(root_0, EXPRESSION217_tree)




                elif alt47 == 3:
                    # grammar/ShyRecognizerFrontend.g:223:9: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING218 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2414)
                    STRING218_tree = self._adaptor.createWithPayload(STRING218)
                    self._adaptor.addChild(root_0, STRING218_tree)




                elif alt47 == 4:
                    # grammar/ShyRecognizerFrontend.g:224:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2424)
                    num_whole219 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole219.tree)



                elif alt47 == 5:
                    # grammar/ShyRecognizerFrontend.g:225:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2434)
                    num_fract220 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract220.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:228:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS221 = None
        ID222 = None
        NEWLINE223 = None
        INDENT224 = None
        NEWLINE225 = None
        DEDENT227 = None
        NEWLINE228 = None
        consts_items226 = None


        CONSTS221_tree = None
        ID222_tree = None
        NEWLINE223_tree = None
        INDENT224_tree = None
        NEWLINE225_tree = None
        DEDENT227_tree = None
        NEWLINE228_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:229:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:229:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS221 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2453) 
                stream_CONSTS.add(CONSTS221)


                ID222 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2455) 
                stream_ID.add(ID222)


                NEWLINE223 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2457) 
                stream_NEWLINE.add(NEWLINE223)


                INDENT224 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2467) 
                stream_INDENT.add(INDENT224)


                NEWLINE225 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2469) 
                stream_NEWLINE.add(NEWLINE225)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2471)
                consts_items226 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items226.tree)


                DEDENT227 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2473) 
                stream_DEDENT.add(DEDENT227)


                NEWLINE228 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2475) 
                stream_NEWLINE.add(NEWLINE228)


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
                # 231:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:231:13: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:233:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item229 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:233:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:233:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:233:16: ( consts_item )+
                cnt48 = 0
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == ID) :
                        alt48 = 1


                    if alt48 == 1:
                        # grammar/ShyRecognizerFrontend.g:233:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2508)
                        consts_item229 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item229.tree)



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
    # grammar/ShyRecognizerFrontend.g:234:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID230 = None
        NEWLINE232 = None
        ID233 = None
        NEWLINE235 = None
        ID236 = None
        EXPRESSION237 = None
        NEWLINE238 = None
        num_whole231 = None

        num_fract234 = None


        ID230_tree = None
        NEWLINE232_tree = None
        ID233_tree = None
        NEWLINE235_tree = None
        ID236_tree = None
        EXPRESSION237_tree = None
        NEWLINE238_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:235:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerFrontend.g:235:9: ID num_whole NEWLINE
                    pass 
                    ID230 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2524) 
                    stream_ID.add(ID230)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2526)
                    num_whole231 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole231.tree)


                    NEWLINE232 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2528) 
                    stream_NEWLINE.add(NEWLINE232)


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
                    # 235:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:235:33: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/ShyRecognizerFrontend.g:236:9: ID num_fract NEWLINE
                    pass 
                    ID233 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2550) 
                    stream_ID.add(ID233)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2552)
                    num_fract234 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract234.tree)


                    NEWLINE235 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2554) 
                    stream_NEWLINE.add(NEWLINE235)


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
                    # 236:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:236:33: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:237:9: ID EXPRESSION NEWLINE
                    pass 
                    ID236 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2576) 
                    stream_ID.add(ID236)


                    EXPRESSION237 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2578) 
                    stream_EXPRESSION.add(EXPRESSION237)


                    NEWLINE238 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2580) 
                    stream_NEWLINE.add(NEWLINE238)


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
                    # 237:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:237:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:240:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES239 = None
        ID240 = None
        NEWLINE241 = None
        INDENT242 = None
        NEWLINE243 = None
        DEDENT245 = None
        NEWLINE246 = None
        types_item244 = None


        TYPES239_tree = None
        ID240_tree = None
        NEWLINE241_tree = None
        INDENT242_tree = None
        NEWLINE243_tree = None
        DEDENT245_tree = None
        NEWLINE246_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:241:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:241:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES239 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2611) 
                stream_TYPES.add(TYPES239)


                ID240 = self.match(self.input, ID, self.FOLLOW_ID_in_types2613) 
                stream_ID.add(ID240)


                NEWLINE241 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2615) 
                stream_NEWLINE.add(NEWLINE241)


                INDENT242 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2625) 
                stream_INDENT.add(INDENT242)


                NEWLINE243 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2627) 
                stream_NEWLINE.add(NEWLINE243)


                # grammar/ShyRecognizerFrontend.g:242:24: ( types_item )+
                cnt50 = 0
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == ID) :
                        alt50 = 1


                    if alt50 == 1:
                        # grammar/ShyRecognizerFrontend.g:242:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2629)
                        types_item244 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item244.tree)



                    else:
                        if cnt50 >= 1:
                            break #loop50

                        eee = EarlyExitException(50, self.input)
                        raise eee

                    cnt50 += 1


                DEDENT245 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2633) 
                stream_DEDENT.add(DEDENT245)


                NEWLINE246 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2635) 
                stream_NEWLINE.add(NEWLINE246)


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
                # 243:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:243:13: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:243:30: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:245:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID247 = None
        attrs_hints248 = None


        ID247_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:245:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:245:14: ID attrs_hints
                pass 
                ID247 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2670) 
                stream_ID.add(ID247)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2672)
                attrs_hints248 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints248.tree)


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
                # 245:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:245:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:247:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES249 = None
        ID250 = None
        NEWLINE251 = None
        INDENT252 = None
        NEWLINE253 = None
        DEDENT255 = None
        NEWLINE256 = None
        messages_item254 = None


        MESSAGES249_tree = None
        ID250_tree = None
        NEWLINE251_tree = None
        INDENT252_tree = None
        NEWLINE253_tree = None
        DEDENT255_tree = None
        NEWLINE256_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:248:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:248:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES249 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2699) 
                stream_MESSAGES.add(MESSAGES249)


                ID250 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2701) 
                stream_ID.add(ID250)


                NEWLINE251 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2703) 
                stream_NEWLINE.add(NEWLINE251)


                INDENT252 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2713) 
                stream_INDENT.add(INDENT252)


                NEWLINE253 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2715) 
                stream_NEWLINE.add(NEWLINE253)


                # grammar/ShyRecognizerFrontend.g:249:24: ( messages_item )+
                cnt51 = 0
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == ID) :
                        alt51 = 1


                    if alt51 == 1:
                        # grammar/ShyRecognizerFrontend.g:249:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2717)
                        messages_item254 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item254.tree)



                    else:
                        if cnt51 >= 1:
                            break #loop51

                        eee = EarlyExitException(51, self.input)
                        raise eee

                    cnt51 += 1


                DEDENT255 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2721) 
                stream_DEDENT.add(DEDENT255)


                NEWLINE256 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2723) 
                stream_NEWLINE.add(NEWLINE256)


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
                # 250:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:250:13: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:250:33: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:253:1: messages_item : ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) );
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID257 = None
        ID259 = None
        REPLY260 = None
        ID262 = None
        REQUEST263 = None
        ID265 = None
        NEWLINE266 = None
        INDENT267 = None
        NEWLINE268 = None
        REPLY269 = None
        DEDENT271 = None
        NEWLINE272 = None
        ID273 = None
        NEWLINE274 = None
        INDENT275 = None
        NEWLINE276 = None
        REQUEST277 = None
        DEDENT279 = None
        NEWLINE280 = None
        ID281 = None
        NEWLINE282 = None
        INDENT283 = None
        NEWLINE284 = None
        REQUEST285 = None
        REPLY287 = None
        DEDENT289 = None
        NEWLINE290 = None
        attrs_hints258 = None

        attrs_hints261 = None

        attrs_hints264 = None

        attrs_hints270 = None

        attrs_hints278 = None

        attrs_hints286 = None

        attrs_hints288 = None


        ID257_tree = None
        ID259_tree = None
        REPLY260_tree = None
        ID262_tree = None
        REQUEST263_tree = None
        ID265_tree = None
        NEWLINE266_tree = None
        INDENT267_tree = None
        NEWLINE268_tree = None
        REPLY269_tree = None
        DEDENT271_tree = None
        NEWLINE272_tree = None
        ID273_tree = None
        NEWLINE274_tree = None
        INDENT275_tree = None
        NEWLINE276_tree = None
        REQUEST277_tree = None
        DEDENT279_tree = None
        NEWLINE280_tree = None
        ID281_tree = None
        NEWLINE282_tree = None
        INDENT283_tree = None
        NEWLINE284_tree = None
        REQUEST285_tree = None
        REPLY287_tree = None
        DEDENT289_tree = None
        NEWLINE290_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_REPLY = RewriteRuleTokenStream(self._adaptor, "token REPLY")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:254:5: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) )
                alt52 = 6
                alt52 = self.dfa52.predict(self.input)
                if alt52 == 1:
                    # grammar/ShyRecognizerFrontend.g:254:9: ID attrs_hints
                    pass 
                    ID257 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2765) 
                    stream_ID.add(ID257)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2767)
                    attrs_hints258 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints258.tree)


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
                    # 255:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:255:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
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
                    # grammar/ShyRecognizerFrontend.g:258:9: ID REPLY attrs_hints
                    pass 
                    ID259 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2828) 
                    stream_ID.add(ID259)


                    REPLY260 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2830) 
                    stream_REPLY.add(REPLY260)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2832)
                    attrs_hints261 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints261.tree)


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
                    # 259:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:259:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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
                    # grammar/ShyRecognizerFrontend.g:262:9: ID REQUEST attrs_hints
                    pass 
                    ID262 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2893) 
                    stream_ID.add(ID262)


                    REQUEST263 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item2895) 
                    stream_REQUEST.add(REQUEST263)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2897)
                    attrs_hints264 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints264.tree)


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
                    # 263:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:263:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
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
                    # grammar/ShyRecognizerFrontend.g:266:9: ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID265 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2958) 
                    stream_ID.add(ID265)


                    NEWLINE266 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2960) 
                    stream_NEWLINE.add(NEWLINE266)


                    INDENT267 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item2962) 
                    stream_INDENT.add(INDENT267)


                    NEWLINE268 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2964) 
                    stream_NEWLINE.add(NEWLINE268)


                    REPLY269 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2966) 
                    stream_REPLY.add(REPLY269)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2968)
                    attrs_hints270 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints270.tree)


                    DEDENT271 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item2970) 
                    stream_DEDENT.add(DEDENT271)


                    NEWLINE272 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2972) 
                    stream_NEWLINE.add(NEWLINE272)


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
                    # 267:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:267:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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
                    # grammar/ShyRecognizerFrontend.g:270:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE
                    pass 
                    ID273 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3033) 
                    stream_ID.add(ID273)


                    NEWLINE274 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3035) 
                    stream_NEWLINE.add(NEWLINE274)


                    INDENT275 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3037) 
                    stream_INDENT.add(INDENT275)


                    NEWLINE276 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3039) 
                    stream_NEWLINE.add(NEWLINE276)


                    REQUEST277 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3041) 
                    stream_REQUEST.add(REQUEST277)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3043)
                    attrs_hints278 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints278.tree)


                    DEDENT279 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3045) 
                    stream_DEDENT.add(DEDENT279)


                    NEWLINE280 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3047) 
                    stream_NEWLINE.add(NEWLINE280)


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
                    # 271:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:271:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
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
                    # grammar/ShyRecognizerFrontend.g:274:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID281 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3108) 
                    stream_ID.add(ID281)


                    NEWLINE282 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3110) 
                    stream_NEWLINE.add(NEWLINE282)


                    INDENT283 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3112) 
                    stream_INDENT.add(INDENT283)


                    NEWLINE284 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3114) 
                    stream_NEWLINE.add(NEWLINE284)


                    REQUEST285 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3128) 
                    stream_REQUEST.add(REQUEST285)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3130)
                    attrs_hints286 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints286.tree)


                    REPLY287 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item3144) 
                    stream_REPLY.add(REPLY287)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3146)
                    attrs_hints288 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints288.tree)


                    DEDENT289 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3156) 
                    stream_DEDENT.add(DEDENT289)


                    NEWLINE290 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3158) 
                    stream_NEWLINE.add(NEWLINE290)


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
                    # 278:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:278:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:284:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS291 = None
        ID292 = None
        attrs_hints293 = None


        VARS291_tree = None
        ID292_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:285:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:285:9: VARS ID attrs_hints
                pass 
                VARS291 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars3248) 
                stream_VARS.add(VARS291)


                ID292 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3250) 
                stream_ID.add(ID292)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3252)
                attrs_hints293 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints293.tree)


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
                # 286:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:286:13: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:289:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE295 = None
        NEWLINE296 = None
        INDENT297 = None
        NEWLINE298 = None
        NEWLINE300 = None
        DEDENT301 = None
        NEWLINE302 = None
        NEWLINE304 = None
        INDENT305 = None
        NEWLINE306 = None
        NEWLINE308 = None
        DEDENT309 = None
        NEWLINE310 = None
        attr_hint294 = None

        attr_hint299 = None

        attr_hint303 = None

        attr_hint307 = None


        NEWLINE295_tree = None
        NEWLINE296_tree = None
        INDENT297_tree = None
        NEWLINE298_tree = None
        NEWLINE300_tree = None
        DEDENT301_tree = None
        NEWLINE302_tree = None
        NEWLINE304_tree = None
        INDENT305_tree = None
        NEWLINE306_tree = None
        NEWLINE308_tree = None
        DEDENT309_tree = None
        NEWLINE310_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:290:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt55 = 3
                alt55 = self.dfa55.predict(self.input)
                if alt55 == 1:
                    # grammar/ShyRecognizerFrontend.g:290:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3292)
                    attr_hint294 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint294.tree)


                    NEWLINE295 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3294) 
                    stream_NEWLINE.add(NEWLINE295)


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
                    # 291:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt55 == 2:
                    # grammar/ShyRecognizerFrontend.g:292:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE296 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3319) 
                    stream_NEWLINE.add(NEWLINE296)


                    # grammar/ShyRecognizerFrontend.g:293:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:293:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT297 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3331) 
                    stream_INDENT.add(INDENT297)


                    NEWLINE298 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3333) 
                    stream_NEWLINE.add(NEWLINE298)


                    # grammar/ShyRecognizerFrontend.g:293:26: ( attr_hint NEWLINE )+
                    cnt53 = 0
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == CURLY_OPEN or LA53_0 == ID) :
                            alt53 = 1


                        if alt53 == 1:
                            # grammar/ShyRecognizerFrontend.g:293:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3337)
                            attr_hint299 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint299.tree)


                            NEWLINE300 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3339) 
                            stream_NEWLINE.add(NEWLINE300)



                        else:
                            if cnt53 >= 1:
                                break #loop53

                            eee = EarlyExitException(53, self.input)
                            raise eee

                        cnt53 += 1


                    DEDENT301 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3345) 
                    stream_DEDENT.add(DEDENT301)


                    NEWLINE302 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3347) 
                    stream_NEWLINE.add(NEWLINE302)





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
                    # 294:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:294:30: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt55 == 3:
                    # grammar/ShyRecognizerFrontend.g:295:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3376)
                    attr_hint303 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint303.tree)


                    NEWLINE304 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3378) 
                    stream_NEWLINE.add(NEWLINE304)


                    # grammar/ShyRecognizerFrontend.g:296:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:296:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT305 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3390) 
                    stream_INDENT.add(INDENT305)


                    NEWLINE306 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3392) 
                    stream_NEWLINE.add(NEWLINE306)


                    # grammar/ShyRecognizerFrontend.g:296:26: ( attr_hint NEWLINE )+
                    cnt54 = 0
                    while True: #loop54
                        alt54 = 2
                        LA54_0 = self.input.LA(1)

                        if (LA54_0 == CURLY_OPEN or LA54_0 == ID) :
                            alt54 = 1


                        if alt54 == 1:
                            # grammar/ShyRecognizerFrontend.g:296:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3396)
                            attr_hint307 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint307.tree)


                            NEWLINE308 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3398) 
                            stream_NEWLINE.add(NEWLINE308)



                        else:
                            if cnt54 >= 1:
                                break #loop54

                            eee = EarlyExitException(54, self.input)
                            raise eee

                        cnt54 += 1


                    DEDENT309 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3404) 
                    stream_DEDENT.add(DEDENT309)


                    NEWLINE310 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3406) 
                    stream_NEWLINE.add(NEWLINE310)





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
                    # 297:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:297:30: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:299:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID311 = None
        ID313 = None
        NEWLINE315 = None
        INDENT316 = None
        NEWLINE317 = None
        ID318 = None
        NEWLINE319 = None
        DEDENT320 = None
        hint312 = None

        hint314 = None


        ID311_tree = None
        ID313_tree = None
        NEWLINE315_tree = None
        INDENT316_tree = None
        NEWLINE317_tree = None
        ID318_tree = None
        NEWLINE319_tree = None
        DEDENT320_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:300:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt60 = 3
                alt60 = self.dfa60.predict(self.input)
                if alt60 == 1:
                    # grammar/ShyRecognizerFrontend.g:300:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:300:9: ( ID )+
                    cnt56 = 0
                    while True: #loop56
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == ID) :
                            alt56 = 1


                        if alt56 == 1:
                            # grammar/ShyRecognizerFrontend.g:300:9: ID
                            pass 
                            ID311 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3444) 
                            stream_ID.add(ID311)



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
                    # 301:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:301:13: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:301:46: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:301:46: ^( TREE_ATTR ID )
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
                    # grammar/ShyRecognizerFrontend.g:302:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3486)
                    hint312 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint312.tree)


                    # grammar/ShyRecognizerFrontend.g:302:14: ( ID )+
                    cnt57 = 0
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == ID) :
                            alt57 = 1


                        if alt57 == 1:
                            # grammar/ShyRecognizerFrontend.g:302:14: ID
                            pass 
                            ID313 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3488) 
                            stream_ID.add(ID313)



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
                    # 303:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:303:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:303:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:303:36: ^( TREE_ATTR ID )
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
                    # grammar/ShyRecognizerFrontend.g:304:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3529)
                    hint314 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint314.tree)


                    NEWLINE315 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3531) 
                    stream_NEWLINE.add(NEWLINE315)


                    INDENT316 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint3533) 
                    stream_INDENT.add(INDENT316)


                    NEWLINE317 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3535) 
                    stream_NEWLINE.add(NEWLINE317)


                    # grammar/ShyRecognizerFrontend.g:304:37: ( ( ID )+ NEWLINE )+
                    cnt59 = 0
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == ID) :
                            alt59 = 1


                        if alt59 == 1:
                            # grammar/ShyRecognizerFrontend.g:304:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:304:39: ( ID )+
                            cnt58 = 0
                            while True: #loop58
                                alt58 = 2
                                LA58_0 = self.input.LA(1)

                                if (LA58_0 == ID) :
                                    alt58 = 1


                                if alt58 == 1:
                                    # grammar/ShyRecognizerFrontend.g:304:39: ID
                                    pass 
                                    ID318 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3539) 
                                    stream_ID.add(ID318)



                                else:
                                    if cnt58 >= 1:
                                        break #loop58

                                    eee = EarlyExitException(58, self.input)
                                    raise eee

                                cnt58 += 1


                            NEWLINE319 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3543) 
                            stream_NEWLINE.add(NEWLINE319)



                        else:
                            if cnt59 >= 1:
                                break #loop59

                            eee = EarlyExitException(59, self.input)
                            raise eee

                        cnt59 += 1


                    DEDENT320 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint3549) 
                    stream_DEDENT.add(DEDENT320)


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
                    # 305:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:305:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:305:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:305:36: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:308:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN321 = None
        ID322 = None
        CURLY_CLOSE323 = None
        CURLY_OPEN324 = None
        ID325 = None
        CURLY_CLOSE327 = None
        hint_arg326 = None


        CURLY_OPEN321_tree = None
        ID322_tree = None
        CURLY_CLOSE323_tree = None
        CURLY_OPEN324_tree = None
        ID325_tree = None
        CURLY_CLOSE327_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:309:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:309:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN321 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3597) 
                    stream_CURLY_OPEN.add(CURLY_OPEN321)


                    ID322 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3599) 
                    stream_ID.add(ID322)


                    CURLY_CLOSE323 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3601) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE323)


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
                    # 309:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:309:38: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:310:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN324 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3621) 
                    stream_CURLY_OPEN.add(CURLY_OPEN324)


                    ID325 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3623) 
                    stream_ID.add(ID325)


                    # grammar/ShyRecognizerFrontend.g:310:23: ( hint_arg )+
                    cnt61 = 0
                    while True: #loop61
                        alt61 = 2
                        LA61_0 = self.input.LA(1)

                        if (LA61_0 == ID or LA61_0 == UNDERSCORE) :
                            alt61 = 1


                        if alt61 == 1:
                            # grammar/ShyRecognizerFrontend.g:310:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint3625)
                            hint_arg326 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg326.tree)



                        else:
                            if cnt61 >= 1:
                                break #loop61

                            eee = EarlyExitException(61, self.input)
                            raise eee

                        cnt61 += 1


                    CURLY_CLOSE327 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3629) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE327)


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
                    # 310:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:310:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:310:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:312:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set328 = None

        set328_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:312:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set328 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set328))

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
    # grammar/ShyRecognizerFrontend.g:314:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS329 = None
        NUMBER330 = None

        MINUS329_tree = None
        NUMBER330_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:314:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:314:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:314:13: ( MINUS )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == MINUS) :
                    alt63 = 1
                if alt63 == 1:
                    # grammar/ShyRecognizerFrontend.g:314:13: MINUS
                    pass 
                    MINUS329 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3668)
                    MINUS329_tree = self._adaptor.createWithPayload(MINUS329)
                    self._adaptor.addChild(root_0, MINUS329_tree)






                NUMBER330 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3672)
                NUMBER330_tree = self._adaptor.createWithPayload(NUMBER330)
                self._adaptor.addChild(root_0, NUMBER330_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:315:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS331 = None
        NUMBER332 = None
        DIVIDE333 = None
        NUMBER334 = None

        MINUS331_tree = None
        NUMBER332_tree = None
        DIVIDE333_tree = None
        NUMBER334_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:315:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:315:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:315:13: ( MINUS )?
                alt64 = 2
                LA64_0 = self.input.LA(1)

                if (LA64_0 == MINUS) :
                    alt64 = 1
                if alt64 == 1:
                    # grammar/ShyRecognizerFrontend.g:315:13: MINUS
                    pass 
                    MINUS331 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3680)
                    MINUS331_tree = self._adaptor.createWithPayload(MINUS331)
                    self._adaptor.addChild(root_0, MINUS331_tree)






                NUMBER332 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3684)
                NUMBER332_tree = self._adaptor.createWithPayload(NUMBER332)
                self._adaptor.addChild(root_0, NUMBER332_tree)



                DIVIDE333 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3686)
                DIVIDE333_tree = self._adaptor.createWithPayload(DIVIDE333)
                self._adaptor.addChild(root_0, DIVIDE333_tree)



                NUMBER334 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3688)
                NUMBER334_tree = self._adaptor.createWithPayload(NUMBER334)
                self._adaptor.addChild(root_0, NUMBER334_tree)





                retval.stop = self.input.LT(-1)


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
        DFA.unpack(u"\1\17\4\uffff\3\17\1\16\1\uffff\1\17\3\uffff\1\17\10"
        u"\uffff\1\17\57\uffff\1\17\1\uffff\1\17"),
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
    FOLLOW_ID_in_request528 = frozenset([26])
    FOLLOW_NEWLINE_in_request530 = frozenset([21])
    FOLLOW_INDENT_in_request532 = frozenset([26])
    FOLLOW_NEWLINE_in_request534 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_request536 = frozenset([13])
    FOLLOW_DEDENT_in_request538 = frozenset([26])
    FOLLOW_NEWLINE_in_request540 = frozenset([1])
    FOLLOW_REQUEST_in_request571 = frozenset([19])
    FOLLOW_ID_in_request573 = frozenset([26])
    FOLLOW_NEWLINE_in_request575 = frozenset([21])
    FOLLOW_INDENT_in_request577 = frozenset([26])
    FOLLOW_NEWLINE_in_request579 = frozenset([13, 28, 83])
    FOLLOW_local_vars_in_request593 = frozenset([13, 28])
    FOLLOW_local_ops_in_request597 = frozenset([13])
    FOLLOW_DEDENT_in_request609 = frozenset([26])
    FOLLOW_NEWLINE_in_request611 = frozenset([1])
    FOLLOW_RECEIVE_in_receive657 = frozenset([19])
    FOLLOW_ID_in_receive659 = frozenset([26])
    FOLLOW_NEWLINE_in_receive661 = frozenset([1])
    FOLLOW_RECEIVE_in_receive690 = frozenset([19])
    FOLLOW_ID_in_receive692 = frozenset([26])
    FOLLOW_NEWLINE_in_receive694 = frozenset([21])
    FOLLOW_INDENT_in_receive696 = frozenset([26])
    FOLLOW_NEWLINE_in_receive698 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_receive700 = frozenset([13])
    FOLLOW_DEDENT_in_receive702 = frozenset([26])
    FOLLOW_NEWLINE_in_receive704 = frozenset([1])
    FOLLOW_RECEIVE_in_receive735 = frozenset([19])
    FOLLOW_ID_in_receive737 = frozenset([26])
    FOLLOW_NEWLINE_in_receive739 = frozenset([21])
    FOLLOW_INDENT_in_receive741 = frozenset([26])
    FOLLOW_NEWLINE_in_receive743 = frozenset([13, 28, 83])
    FOLLOW_local_vars_in_receive757 = frozenset([13, 28])
    FOLLOW_local_ops_in_receive761 = frozenset([13])
    FOLLOW_DEDENT_in_receive773 = frozenset([26])
    FOLLOW_NEWLINE_in_receive775 = frozenset([1])
    FOLLOW_PROC_in_proc821 = frozenset([19])
    FOLLOW_ID_in_proc823 = frozenset([26])
    FOLLOW_NEWLINE_in_proc825 = frozenset([1])
    FOLLOW_PROC_in_proc854 = frozenset([19])
    FOLLOW_ID_in_proc856 = frozenset([26])
    FOLLOW_NEWLINE_in_proc858 = frozenset([21])
    FOLLOW_INDENT_in_proc860 = frozenset([26])
    FOLLOW_NEWLINE_in_proc862 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_proc864 = frozenset([13])
    FOLLOW_DEDENT_in_proc866 = frozenset([26])
    FOLLOW_NEWLINE_in_proc868 = frozenset([1])
    FOLLOW_PROC_in_proc899 = frozenset([19])
    FOLLOW_ID_in_proc901 = frozenset([26])
    FOLLOW_NEWLINE_in_proc903 = frozenset([21])
    FOLLOW_INDENT_in_proc905 = frozenset([26])
    FOLLOW_NEWLINE_in_proc907 = frozenset([6, 13, 28, 83])
    FOLLOW_proc_args_in_proc921 = frozenset([13, 28, 83])
    FOLLOW_local_vars_in_proc925 = frozenset([13, 28])
    FOLLOW_local_ops_in_proc929 = frozenset([13])
    FOLLOW_DEDENT_in_proc941 = frozenset([26])
    FOLLOW_NEWLINE_in_proc943 = frozenset([1])
    FOLLOW_ARGS_in_proc_args993 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args995 = frozenset([1])
    FOLLOW_VARS_in_local_vars1024 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_local_vars1026 = frozenset([1])
    FOLLOW_OPS_in_local_ops1055 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1057 = frozenset([21])
    FOLLOW_INDENT_in_local_ops1059 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1061 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_local_ops1063 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops1065 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1067 = frozenset([1])
    FOLLOW_OPS_in_local_ops1089 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statement_in_local_ops1091 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement1129 = frozenset([26])
    FOLLOW_NEWLINE_in_statement1131 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement1157 = frozenset([1])
    FOLLOW_statement_if_in_statement1167 = frozenset([1])
    FOLLOW_statement_assign_in_statement1177 = frozenset([1])
    FOLLOW_statement_while_in_statement1187 = frozenset([1])
    FOLLOW_statement_with_in_statement1197 = frozenset([1])
    FOLLOW_statement_in_statements1216 = frozenset([1, 18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_WITH_in_statement_with1258 = frozenset([19])
    FOLLOW_ID_in_statement_with1260 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1262 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1272 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1274 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_with1276 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1278 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1280 = frozenset([1])
    FOLLOW_ID_in_statement_assign1320 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1324 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1326 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1330 = frozenset([1])
    FOLLOW_ID_in_statement_assign1383 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1387 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1389 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1391 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1393 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1405 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1409 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_assign1415 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1417 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1470 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1474 = frozenset([19])
    FOLLOW_ID_in_statement_assign1476 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1480 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1533 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1537 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1539 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1541 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1543 = frozenset([19])
    FOLLOW_ID_in_statement_assign1555 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1559 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1565 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1567 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1629 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1631 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1633 = frozenset([15])
    FOLLOW_DO_in_statement_while1637 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1639 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1653 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1655 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_while1657 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1659 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1661 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1701 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1711 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1723 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1831 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1833 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1865 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1867 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1899 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1901 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1905 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1907 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1921 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1923 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_elif_body1925 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1927 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1929 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1969 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1971 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1985 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1987 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_else1989 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1991 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1993 = frozenset([1])
    FOLLOW_condition_call_in_condition2031 = frozenset([1])
    FOLLOW_ANY_in_condition2060 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2062 = frozenset([1])
    FOLLOW_ALL_in_condition2091 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2093 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls2131 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls2141 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls2143 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2145 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls2147 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls2151 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2153 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call2187 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call2197 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line2216 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line2218 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2244 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2263 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_single_line2265 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2309 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2311 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2315 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2325 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2327 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2331 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2333 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_call_multi_line2339 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2341 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2377 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_ID_in_arbitrary_value2394 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2404 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2414 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2424 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2434 = frozenset([1])
    FOLLOW_CONSTS_in_consts2453 = frozenset([19])
    FOLLOW_ID_in_consts2455 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2457 = frozenset([21])
    FOLLOW_INDENT_in_consts2467 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2469 = frozenset([19])
    FOLLOW_consts_items_in_consts2471 = frozenset([13])
    FOLLOW_DEDENT_in_consts2473 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2475 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2508 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2524 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2526 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2528 = frozenset([1])
    FOLLOW_ID_in_consts_item2550 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2552 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2554 = frozenset([1])
    FOLLOW_ID_in_consts_item2576 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2578 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2580 = frozenset([1])
    FOLLOW_TYPES_in_types2611 = frozenset([19])
    FOLLOW_ID_in_types2613 = frozenset([26])
    FOLLOW_NEWLINE_in_types2615 = frozenset([21])
    FOLLOW_INDENT_in_types2625 = frozenset([26])
    FOLLOW_NEWLINE_in_types2627 = frozenset([19])
    FOLLOW_types_item_in_types2629 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2633 = frozenset([26])
    FOLLOW_NEWLINE_in_types2635 = frozenset([1])
    FOLLOW_ID_in_types_item2670 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2672 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2699 = frozenset([19])
    FOLLOW_ID_in_messages2701 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2703 = frozenset([21])
    FOLLOW_INDENT_in_messages2713 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2715 = frozenset([19])
    FOLLOW_messages_item_in_messages2717 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2721 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2723 = frozenset([1])
    FOLLOW_ID_in_messages_item2765 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2767 = frozenset([1])
    FOLLOW_ID_in_messages_item2828 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2830 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2832 = frozenset([1])
    FOLLOW_ID_in_messages_item2893 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item2895 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2897 = frozenset([1])
    FOLLOW_ID_in_messages_item2958 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2960 = frozenset([21])
    FOLLOW_INDENT_in_messages_item2962 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2964 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2966 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2968 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item2970 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2972 = frozenset([1])
    FOLLOW_ID_in_messages_item3033 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3035 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3037 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3039 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3041 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3043 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3045 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3047 = frozenset([1])
    FOLLOW_ID_in_messages_item3108 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3110 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3112 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3114 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3128 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3130 = frozenset([33])
    FOLLOW_REPLY_in_messages_item3144 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3146 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3156 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3158 = frozenset([1])
    FOLLOW_VARS_in_vars3248 = frozenset([19])
    FOLLOW_ID_in_vars3250 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars3252 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3292 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3294 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints3319 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3331 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3333 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3337 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3339 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3345 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3347 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3376 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3378 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3390 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3392 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3396 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3398 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3404 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3406 = frozenset([1])
    FOLLOW_ID_in_attr_hint3444 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3486 = frozenset([19])
    FOLLOW_ID_in_attr_hint3488 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3529 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3531 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint3533 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3535 = frozenset([19])
    FOLLOW_ID_in_attr_hint3539 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint3543 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint3549 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3597 = frozenset([19])
    FOLLOW_ID_in_hint3599 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint3601 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3621 = frozenset([19])
    FOLLOW_ID_in_hint3623 = frozenset([19, 82])
    FOLLOW_hint_arg_in_hint3625 = frozenset([11, 19, 82])
    FOLLOW_CURLY_CLOSE_in_hint3629 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3668 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3672 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3680 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3684 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3686 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3688 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
