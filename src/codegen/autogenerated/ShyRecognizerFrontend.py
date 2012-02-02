# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-02 20:18:10

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

        self.dfa20 = self.DFA20(
            self, 20,
            eot = self.DFA20_eot,
            eof = self.DFA20_eof,
            min = self.DFA20_min,
            max = self.DFA20_max,
            accept = self.DFA20_accept,
            special = self.DFA20_special,
            transition = self.DFA20_transition
            )

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

        self.dfa40 = self.DFA40(
            self, 40,
            eot = self.DFA40_eot,
            eof = self.DFA40_eof,
            min = self.DFA40_min,
            max = self.DFA40_max,
            accept = self.DFA40_accept,
            special = self.DFA40_special,
            transition = self.DFA40_transition
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

        self.dfa54 = self.DFA54(
            self, 54,
            eot = self.DFA54_eot,
            eof = self.DFA54_eof,
            min = self.DFA54_min,
            max = self.DFA54_max,
            accept = self.DFA54_accept,
            special = self.DFA54_special,
            transition = self.DFA54_transition
            )

        self.dfa59 = self.DFA59(
            self, 59,
            eot = self.DFA59_eot,
            eof = self.DFA59_eof,
            min = self.DFA59_min,
            max = self.DFA59_max,
            accept = self.DFA59_accept,
            special = self.DFA59_special,
            transition = self.DFA59_transition
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
                # elements: receive, request, proc, module_queue, ID
                # token labels: 
                # rule labels: retval
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
                    # elements: local_vars, ID, local_ops
                    # token labels: 
                    # rule labels: retval
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
                    # elements: ID, local_vars, proc_args, local_ops
                    # token labels: 
                    # rule labels: retval
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
    # grammar/ShyRecognizerFrontend.g:97:1: local_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
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
        statements107 = None


        OPS103_tree = None
        NEWLINE104_tree = None
        INDENT105_tree = None
        NEWLINE106_tree = None
        DEDENT108_tree = None
        NEWLINE109_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:98:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
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





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:102:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE111 = None
        statement_call_single_line110 = None

        statement_call_multi_line112 = None

        statement_if113 = None

        statement_assign114 = None

        statement_while115 = None

        statement_with116 = None


        NEWLINE111_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:103:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt20 = 6
                alt20 = self.dfa20.predict(self.input)
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:103:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement1098)
                    statement_call_single_line110 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line110.tree)


                    NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement1100) 
                    stream_NEWLINE.add(NEWLINE111)


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
                    # 104:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt20 == 2:
                    # grammar/ShyRecognizerFrontend.g:105:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement1126)
                    statement_call_multi_line112 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line112.tree)



                elif alt20 == 3:
                    # grammar/ShyRecognizerFrontend.g:106:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement1136)
                    statement_if113 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if113.tree)



                elif alt20 == 4:
                    # grammar/ShyRecognizerFrontend.g:107:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1146)
                    statement_assign114 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign114.tree)



                elif alt20 == 5:
                    # grammar/ShyRecognizerFrontend.g:108:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement1156)
                    statement_while115 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while115.tree)



                elif alt20 == 6:
                    # grammar/ShyRecognizerFrontend.g:109:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement1166)
                    statement_with116 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with116.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:112:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement117 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:113:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:113:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:113:9: ( statement )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA21_0 <= IF) or LA21_0 == MINUS or LA21_0 == NUMBER or LA21_0 == STRING or LA21_0 == WHILE or LA21_0 == WITH) :
                        alt21 = 1


                    if alt21 == 1:
                        # grammar/ShyRecognizerFrontend.g:113:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1185)
                        statement117 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement117.tree)



                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1


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
                # 114:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:114:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:114:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:117:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH118 = None
        ID119 = None
        NEWLINE120 = None
        INDENT121 = None
        NEWLINE122 = None
        DEDENT124 = None
        NEWLINE125 = None
        statements123 = None


        WITH118_tree = None
        ID119_tree = None
        NEWLINE120_tree = None
        INDENT121_tree = None
        NEWLINE122_tree = None
        DEDENT124_tree = None
        NEWLINE125_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:118:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:118:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH118 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1227) 
                stream_WITH.add(WITH118)


                ID119 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1229) 
                stream_ID.add(ID119)


                NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1231) 
                stream_NEWLINE.add(NEWLINE120)


                INDENT121 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1241) 
                stream_INDENT.add(INDENT121)


                NEWLINE122 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1243) 
                stream_NEWLINE.add(NEWLINE122)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1245)
                statements123 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements123.tree)


                DEDENT124 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1247) 
                stream_DEDENT.add(DEDENT124)


                NEWLINE125 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1249) 
                stream_NEWLINE.add(NEWLINE125)


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
                # 120:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:120:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:123:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID126 = None
        ARROW_LEFT127 = None
        NEWLINE129 = None
        ID130 = None
        ARROW_LEFT131 = None
        NEWLINE132 = None
        INDENT133 = None
        NEWLINE134 = None
        NEWLINE136 = None
        DEDENT137 = None
        NEWLINE138 = None
        ARROW_RIGHT140 = None
        ID141 = None
        NEWLINE142 = None
        ARROW_RIGHT144 = None
        NEWLINE145 = None
        INDENT146 = None
        NEWLINE147 = None
        ID148 = None
        NEWLINE149 = None
        DEDENT150 = None
        NEWLINE151 = None
        arbitrary_value128 = None

        arbitrary_value135 = None

        arbitrary_value139 = None

        arbitrary_value143 = None


        ID126_tree = None
        ARROW_LEFT127_tree = None
        NEWLINE129_tree = None
        ID130_tree = None
        ARROW_LEFT131_tree = None
        NEWLINE132_tree = None
        INDENT133_tree = None
        NEWLINE134_tree = None
        NEWLINE136_tree = None
        DEDENT137_tree = None
        NEWLINE138_tree = None
        ARROW_RIGHT140_tree = None
        ID141_tree = None
        NEWLINE142_tree = None
        ARROW_RIGHT144_tree = None
        NEWLINE145_tree = None
        INDENT146_tree = None
        NEWLINE147_tree = None
        ID148_tree = None
        NEWLINE149_tree = None
        DEDENT150_tree = None
        NEWLINE151_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:124:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt32 = 4
                alt32 = self.dfa32.predict(self.input)
                if alt32 == 1:
                    # grammar/ShyRecognizerFrontend.g:124:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:124:9: ( ID )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == ID) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:124:9: ID
                            pass 
                            ID126 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1289) 
                            stream_ID.add(ID126)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    ARROW_LEFT127 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1293) 
                    stream_ARROW_LEFT.add(ARROW_LEFT127)


                    # grammar/ShyRecognizerFrontend.g:124:25: ( arbitrary_value )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER or LA23_0 == STRING) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:124:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1295)
                            arbitrary_value128 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value128.tree)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1299) 
                    stream_NEWLINE.add(NEWLINE129)


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
                    # 125:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:125:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:125:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:126:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt32 == 2:
                    # grammar/ShyRecognizerFrontend.g:127:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:127:9: ( ID )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if (LA24_0 == ID) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:127:9: ID
                            pass 
                            ID130 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1352) 
                            stream_ID.add(ID130)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    ARROW_LEFT131 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1356) 
                    stream_ARROW_LEFT.add(ARROW_LEFT131)


                    NEWLINE132 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1358) 
                    stream_NEWLINE.add(NEWLINE132)


                    INDENT133 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1360) 
                    stream_INDENT.add(INDENT133)


                    NEWLINE134 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1362) 
                    stream_NEWLINE.add(NEWLINE134)


                    # grammar/ShyRecognizerFrontend.g:128:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA26_0 <= ID) or LA26_0 == MINUS or LA26_0 == NUMBER or LA26_0 == STRING) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:128:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:128:11: ( arbitrary_value )+
                            cnt25 = 0
                            while True: #loop25
                                alt25 = 2
                                LA25_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER or LA25_0 == STRING) :
                                    alt25 = 1


                                if alt25 == 1:
                                    # grammar/ShyRecognizerFrontend.g:128:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1374)
                                    arbitrary_value135 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value135.tree)



                                else:
                                    if cnt25 >= 1:
                                        break #loop25

                                    eee = EarlyExitException(25, self.input)
                                    raise eee

                                cnt25 += 1


                            NEWLINE136 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1378) 
                            stream_NEWLINE.add(NEWLINE136)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


                    DEDENT137 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1384) 
                    stream_DEDENT.add(DEDENT137)


                    NEWLINE138 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1386) 
                    stream_NEWLINE.add(NEWLINE138)


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
                    # 129:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:129:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:129:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:130:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt32 == 3:
                    # grammar/ShyRecognizerFrontend.g:131:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:131:9: ( arbitrary_value )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA27_0 <= ID) or LA27_0 == MINUS or LA27_0 == NUMBER or LA27_0 == STRING) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:131:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1439)
                            arbitrary_value139 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value139.tree)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    ARROW_RIGHT140 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1443) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT140)


                    # grammar/ShyRecognizerFrontend.g:131:39: ( ID )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == ID) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:131:39: ID
                            pass 
                            ID141 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1445) 
                            stream_ID.add(ID141)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    NEWLINE142 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1449) 
                    stream_NEWLINE.add(NEWLINE142)


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
                    # 132:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:132:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:132:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:133:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt32 == 4:
                    # grammar/ShyRecognizerFrontend.g:134:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:134:9: ( arbitrary_value )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA29_0 <= ID) or LA29_0 == MINUS or LA29_0 == NUMBER or LA29_0 == STRING) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:134:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1502)
                            arbitrary_value143 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value143.tree)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    ARROW_RIGHT144 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1506) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT144)


                    NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1508) 
                    stream_NEWLINE.add(NEWLINE145)


                    INDENT146 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1510) 
                    stream_INDENT.add(INDENT146)


                    NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1512) 
                    stream_NEWLINE.add(NEWLINE147)


                    # grammar/ShyRecognizerFrontend.g:135:9: ( ( ID )+ NEWLINE )+
                    cnt31 = 0
                    while True: #loop31
                        alt31 = 2
                        LA31_0 = self.input.LA(1)

                        if (LA31_0 == ID) :
                            alt31 = 1


                        if alt31 == 1:
                            # grammar/ShyRecognizerFrontend.g:135:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:135:11: ( ID )+
                            cnt30 = 0
                            while True: #loop30
                                alt30 = 2
                                LA30_0 = self.input.LA(1)

                                if (LA30_0 == ID) :
                                    alt30 = 1


                                if alt30 == 1:
                                    # grammar/ShyRecognizerFrontend.g:135:11: ID
                                    pass 
                                    ID148 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1524) 
                                    stream_ID.add(ID148)



                                else:
                                    if cnt30 >= 1:
                                        break #loop30

                                    eee = EarlyExitException(30, self.input)
                                    raise eee

                                cnt30 += 1


                            NEWLINE149 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1528) 
                            stream_NEWLINE.add(NEWLINE149)



                        else:
                            if cnt31 >= 1:
                                break #loop31

                            eee = EarlyExitException(31, self.input)
                            raise eee

                        cnt31 += 1


                    DEDENT150 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1534) 
                    stream_DEDENT.add(DEDENT150)


                    NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1536) 
                    stream_NEWLINE.add(NEWLINE151)


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
                    # 136:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:136:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:136:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:137:42: ( ID )+
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
    # grammar/ShyRecognizerFrontend.g:140:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE152 = None
        NEWLINE154 = None
        DO155 = None
        NEWLINE156 = None
        INDENT157 = None
        NEWLINE158 = None
        DEDENT160 = None
        NEWLINE161 = None
        condition153 = None

        statements159 = None


        WHILE152_tree = None
        NEWLINE154_tree = None
        DO155_tree = None
        NEWLINE156_tree = None
        INDENT157_tree = None
        NEWLINE158_tree = None
        DEDENT160_tree = None
        NEWLINE161_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:141:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:141:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE152 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1598) 
                stream_WHILE.add(WHILE152)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1600)
                condition153 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition153.tree)


                # grammar/ShyRecognizerFrontend.g:141:25: ( NEWLINE )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == NEWLINE) :
                    alt33 = 1
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:141:25: NEWLINE
                    pass 
                    NEWLINE154 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1602) 
                    stream_NEWLINE.add(NEWLINE154)





                DO155 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1606) 
                stream_DO.add(DO155)


                NEWLINE156 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1608) 
                stream_NEWLINE.add(NEWLINE156)


                INDENT157 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1622) 
                stream_INDENT.add(INDENT157)


                NEWLINE158 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1624) 
                stream_NEWLINE.add(NEWLINE158)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1626)
                statements159 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements159.tree)


                DEDENT160 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1628) 
                stream_DEDENT.add(DEDENT160)


                NEWLINE161 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1630) 
                stream_NEWLINE.add(NEWLINE161)


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
                # 143:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:143:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:146:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head162 = None

        statement_elif163 = None

        statement_else164 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:147:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:147:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1670)
                statement_if_head162 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head162.tree)


                # grammar/ShyRecognizerFrontend.g:148:9: ( statement_elif )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == ELIF) :
                        alt34 = 1


                    if alt34 == 1:
                        # grammar/ShyRecognizerFrontend.g:148:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1680)
                        statement_elif163 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif163.tree)



                    else:
                        break #loop34


                # grammar/ShyRecognizerFrontend.g:149:9: ( statement_else )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == ELSE) :
                    alt35 = 1
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:149:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1692)
                    statement_else164 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else164.tree)





                # AST Rewrite
                # elements: statement_elif, statement_if_head, statement_else
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 150:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:150:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:152:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:153:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:157:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF165 = None
        statement_elif_body166 = None


        IF165_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:158:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:158:9: IF statement_elif_body
                pass 
                IF165 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1800) 
                stream_IF.add(IF165)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1802)
                statement_elif_body166 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body166.tree)


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
                # 159:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:162:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF167 = None
        statement_elif_body168 = None


        ELIF167_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:163:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:163:9: ELIF statement_elif_body
                pass 
                ELIF167 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1834) 
                stream_ELIF.add(ELIF167)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1836)
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
                # 164:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:167:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE170 = None
        DO171 = None
        NEWLINE172 = None
        INDENT173 = None
        NEWLINE174 = None
        DEDENT176 = None
        NEWLINE177 = None
        condition169 = None

        statements175 = None


        NEWLINE170_tree = None
        DO171_tree = None
        NEWLINE172_tree = None
        INDENT173_tree = None
        NEWLINE174_tree = None
        DEDENT176_tree = None
        NEWLINE177_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:168:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:168:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1868)
                condition169 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition169.tree)


                # grammar/ShyRecognizerFrontend.g:168:19: ( NEWLINE )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == NEWLINE) :
                    alt36 = 1
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:168:19: NEWLINE
                    pass 
                    NEWLINE170 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1870) 
                    stream_NEWLINE.add(NEWLINE170)





                DO171 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1874) 
                stream_DO.add(DO171)


                NEWLINE172 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1876) 
                stream_NEWLINE.add(NEWLINE172)


                INDENT173 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1890) 
                stream_INDENT.add(INDENT173)


                NEWLINE174 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1892) 
                stream_NEWLINE.add(NEWLINE174)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1894)
                statements175 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements175.tree)


                DEDENT176 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1896) 
                stream_DEDENT.add(DEDENT176)


                NEWLINE177 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1898) 
                stream_NEWLINE.add(NEWLINE177)


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
                # 170:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:170:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:173:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE178 = None
        NEWLINE179 = None
        INDENT180 = None
        NEWLINE181 = None
        DEDENT183 = None
        NEWLINE184 = None
        statements182 = None


        ELSE178_tree = None
        NEWLINE179_tree = None
        INDENT180_tree = None
        NEWLINE181_tree = None
        DEDENT183_tree = None
        NEWLINE184_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:174:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE178 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1938) 
                stream_ELSE.add(ELSE178)


                NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1940) 
                stream_NEWLINE.add(NEWLINE179)


                INDENT180 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1954) 
                stream_INDENT.add(INDENT180)


                NEWLINE181 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1956) 
                stream_NEWLINE.add(NEWLINE181)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1958)
                statements182 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements182.tree)


                DEDENT183 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1960) 
                stream_DEDENT.add(DEDENT183)


                NEWLINE184 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1962) 
                stream_NEWLINE.add(NEWLINE184)


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
                # 176:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:176:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:179:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY186 = None
        ALL188 = None
        condition_call185 = None

        condition_calls187 = None

        condition_calls189 = None


        ANY186_tree = None
        ALL188_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:180:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt37 = 3
                LA37 = self.input.LA(1)
                if LA37 == ID:
                    alt37 = 1
                elif LA37 == ANY:
                    alt37 = 2
                elif LA37 == ALL:
                    alt37 = 3
                else:
                    nvae = NoViableAltException("", 37, 0, self.input)

                    raise nvae


                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:180:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition2000)
                    condition_call185 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call185.tree)


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
                    # 181:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:181:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt37 == 2:
                    # grammar/ShyRecognizerFrontend.g:182:9: ANY condition_calls
                    pass 
                    ANY186 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition2029) 
                    stream_ANY.add(ANY186)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2031)
                    condition_calls187 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls187.tree)


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
                    # 183:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:183:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt37 == 3:
                    # grammar/ShyRecognizerFrontend.g:184:9: ALL condition_calls
                    pass 
                    ALL188 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition2060) 
                    stream_ALL.add(ALL188)


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
                    # 185:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:185:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:188:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE191 = None
        INDENT192 = None
        NEWLINE193 = None
        DEDENT195 = None
        NEWLINE196 = None
        condition_call190 = None

        condition_call_line194 = None


        NEWLINE191_tree = None
        INDENT192_tree = None
        NEWLINE193_tree = None
        DEDENT195_tree = None
        NEWLINE196_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:189:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == ID) :
                    alt39 = 1
                elif (LA39_0 == NEWLINE) :
                    alt39 = 2
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae


                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:189:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls2100)
                    condition_call190 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call190.tree)



                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:190:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE191 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2110) 
                    stream_NEWLINE.add(NEWLINE191)


                    INDENT192 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls2112) 
                    stream_INDENT.add(INDENT192)


                    NEWLINE193 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2114) 
                    stream_NEWLINE.add(NEWLINE193)


                    # grammar/ShyRecognizerFrontend.g:190:32: ( condition_call_line )+
                    cnt38 = 0
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == ID) :
                            alt38 = 1


                        if alt38 == 1:
                            # grammar/ShyRecognizerFrontend.g:190:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls2116)
                            condition_call_line194 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line194.tree)



                        else:
                            if cnt38 >= 1:
                                break #loop38

                            eee = EarlyExitException(38, self.input)
                            raise eee

                        cnt38 += 1


                    DEDENT195 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls2120) 
                    stream_DEDENT.add(DEDENT195)


                    NEWLINE196 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2122) 
                    stream_NEWLINE.add(NEWLINE196)


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
                    # 191:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:191:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:194:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line197 = None

        statement_call_multi_line198 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:195:5: ( statement_call_single_line | statement_call_multi_line )
                alt40 = 2
                alt40 = self.dfa40.predict(self.input)
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:195:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call2156)
                    statement_call_single_line197 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line197.tree)



                elif alt40 == 2:
                    # grammar/ShyRecognizerFrontend.g:196:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call2166)
                    statement_call_multi_line198 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line198.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:199:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE200 = None
        statement_call_single_line199 = None

        statement_call_multi_line201 = None


        NEWLINE200_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:200:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt41 = 2
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:200:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line2185)
                    statement_call_single_line199 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line199.tree)


                    NEWLINE200 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line2187) 
                    stream_NEWLINE.add(NEWLINE200)


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
                    # 201:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt41 == 2:
                    # grammar/ShyRecognizerFrontend.g:202:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2213)
                    statement_call_multi_line201 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line201.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:205:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID202 = None
        statement_call_args203 = None


        ID202_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:206:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:206:9: ID ( statement_call_args )?
                pass 
                ID202 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2232) 
                stream_ID.add(ID202)


                # grammar/ShyRecognizerFrontend.g:206:12: ( statement_call_args )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if ((EXPRESSION <= LA42_0 <= ID) or LA42_0 == MINUS or LA42_0 == NUMBER or LA42_0 == STRING) :
                    alt42 = 1
                if alt42 == 1:
                    # grammar/ShyRecognizerFrontend.g:206:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2234)
                    statement_call_args203 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args203.tree)





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
                # 207:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:207:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:207:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:210:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID204 = None
        NEWLINE206 = None
        INDENT207 = None
        NEWLINE208 = None
        NEWLINE210 = None
        DEDENT211 = None
        NEWLINE212 = None
        statement_call_args205 = None

        statement_call_args209 = None


        ID204_tree = None
        NEWLINE206_tree = None
        INDENT207_tree = None
        NEWLINE208_tree = None
        NEWLINE210_tree = None
        DEDENT211_tree = None
        NEWLINE212_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:211:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:211:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID204 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2278) 
                stream_ID.add(ID204)


                # grammar/ShyRecognizerFrontend.g:211:12: ( statement_call_args )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER or LA43_0 == STRING) :
                    alt43 = 1
                if alt43 == 1:
                    # grammar/ShyRecognizerFrontend.g:211:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2280)
                    statement_call_args205 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args205.tree)





                NEWLINE206 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2284) 
                stream_NEWLINE.add(NEWLINE206)


                INDENT207 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2294) 
                stream_INDENT.add(INDENT207)


                NEWLINE208 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2296) 
                stream_NEWLINE.add(NEWLINE208)


                # grammar/ShyRecognizerFrontend.g:212:24: ( statement_call_args NEWLINE )+
                cnt44 = 0
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA44_0 <= ID) or LA44_0 == MINUS or LA44_0 == NUMBER or LA44_0 == STRING) :
                        alt44 = 1


                    if alt44 == 1:
                        # grammar/ShyRecognizerFrontend.g:212:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2300)
                        statement_call_args209 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args209.tree)


                        NEWLINE210 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2302) 
                        stream_NEWLINE.add(NEWLINE210)



                    else:
                        if cnt44 >= 1:
                            break #loop44

                        eee = EarlyExitException(44, self.input)
                        raise eee

                    cnt44 += 1


                DEDENT211 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2308) 
                stream_DEDENT.add(DEDENT211)


                NEWLINE212 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2310) 
                stream_NEWLINE.add(NEWLINE212)


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
                # 213:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:213:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:213:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:216:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value213 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:216:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:216:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:216:23: ( arbitrary_value )+
                cnt45 = 0
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA45_0 <= ID) or LA45_0 == MINUS or LA45_0 == NUMBER or LA45_0 == STRING) :
                        alt45 = 1


                    if alt45 == 1:
                        # grammar/ShyRecognizerFrontend.g:216:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2346)
                        arbitrary_value213 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value213.tree)



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

    # $ANTLR end "statement_call_args"


    class arbitrary_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.arbitrary_value_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerFrontend.g:218:1: arbitrary_value : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID214 = None
        EXPRESSION215 = None
        STRING216 = None
        num_whole217 = None

        num_fract218 = None


        ID214_tree = None
        EXPRESSION215_tree = None
        STRING216_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:219:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
                alt46 = 5
                LA46 = self.input.LA(1)
                if LA46 == ID:
                    alt46 = 1
                elif LA46 == EXPRESSION:
                    alt46 = 2
                elif LA46 == STRING:
                    alt46 = 3
                elif LA46 == MINUS:
                    LA46_4 = self.input.LA(2)

                    if (LA46_4 == NUMBER) :
                        LA46_5 = self.input.LA(3)

                        if (LA46_5 == DIVIDE) :
                            alt46 = 5
                        elif (LA46_5 == ARROW_RIGHT or LA46_5 == DO or (EXPRESSION <= LA46_5 <= ID) or LA46_5 == MINUS or (NEWLINE <= LA46_5 <= NUMBER) or LA46_5 == STRING) :
                            alt46 = 4
                        else:
                            nvae = NoViableAltException("", 46, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 46, 4, self.input)

                        raise nvae


                elif LA46 == NUMBER:
                    LA46_5 = self.input.LA(2)

                    if (LA46_5 == DIVIDE) :
                        alt46 = 5
                    elif (LA46_5 == ARROW_RIGHT or LA46_5 == DO or (EXPRESSION <= LA46_5 <= ID) or LA46_5 == MINUS or (NEWLINE <= LA46_5 <= NUMBER) or LA46_5 == STRING) :
                        alt46 = 4
                    else:
                        nvae = NoViableAltException("", 46, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 46, 0, self.input)

                    raise nvae


                if alt46 == 1:
                    # grammar/ShyRecognizerFrontend.g:219:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID214 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2363)
                    ID214_tree = self._adaptor.createWithPayload(ID214)
                    self._adaptor.addChild(root_0, ID214_tree)




                elif alt46 == 2:
                    # grammar/ShyRecognizerFrontend.g:220:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION215 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2373)
                    EXPRESSION215_tree = self._adaptor.createWithPayload(EXPRESSION215)
                    self._adaptor.addChild(root_0, EXPRESSION215_tree)




                elif alt46 == 3:
                    # grammar/ShyRecognizerFrontend.g:221:9: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING216 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2383)
                    STRING216_tree = self._adaptor.createWithPayload(STRING216)
                    self._adaptor.addChild(root_0, STRING216_tree)




                elif alt46 == 4:
                    # grammar/ShyRecognizerFrontend.g:222:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2393)
                    num_whole217 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole217.tree)



                elif alt46 == 5:
                    # grammar/ShyRecognizerFrontend.g:223:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2403)
                    num_fract218 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract218.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:226:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS219 = None
        ID220 = None
        NEWLINE221 = None
        INDENT222 = None
        NEWLINE223 = None
        DEDENT225 = None
        NEWLINE226 = None
        consts_items224 = None


        CONSTS219_tree = None
        ID220_tree = None
        NEWLINE221_tree = None
        INDENT222_tree = None
        NEWLINE223_tree = None
        DEDENT225_tree = None
        NEWLINE226_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:227:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:227:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS219 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2422) 
                stream_CONSTS.add(CONSTS219)


                ID220 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2424) 
                stream_ID.add(ID220)


                NEWLINE221 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2426) 
                stream_NEWLINE.add(NEWLINE221)


                INDENT222 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2436) 
                stream_INDENT.add(INDENT222)


                NEWLINE223 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2438) 
                stream_NEWLINE.add(NEWLINE223)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2440)
                consts_items224 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items224.tree)


                DEDENT225 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2442) 
                stream_DEDENT.add(DEDENT225)


                NEWLINE226 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2444) 
                stream_NEWLINE.add(NEWLINE226)


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
                # 229:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:229:13: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:231:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item227 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:231:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:231:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:231:16: ( consts_item )+
                cnt47 = 0
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == ID) :
                        alt47 = 1


                    if alt47 == 1:
                        # grammar/ShyRecognizerFrontend.g:231:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2477)
                        consts_item227 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item227.tree)



                    else:
                        if cnt47 >= 1:
                            break #loop47

                        eee = EarlyExitException(47, self.input)
                        raise eee

                    cnt47 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:232:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID228 = None
        NEWLINE230 = None
        ID231 = None
        NEWLINE233 = None
        ID234 = None
        EXPRESSION235 = None
        NEWLINE236 = None
        num_whole229 = None

        num_fract232 = None


        ID228_tree = None
        NEWLINE230_tree = None
        ID231_tree = None
        NEWLINE233_tree = None
        ID234_tree = None
        EXPRESSION235_tree = None
        NEWLINE236_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:233:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt48 = 3
                LA48_0 = self.input.LA(1)

                if (LA48_0 == ID) :
                    LA48 = self.input.LA(2)
                    if LA48 == EXPRESSION:
                        alt48 = 3
                    elif LA48 == MINUS:
                        LA48_3 = self.input.LA(3)

                        if (LA48_3 == NUMBER) :
                            LA48_4 = self.input.LA(4)

                            if (LA48_4 == DIVIDE) :
                                alt48 = 2
                            elif (LA48_4 == NEWLINE) :
                                alt48 = 1
                            else:
                                nvae = NoViableAltException("", 48, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 48, 3, self.input)

                            raise nvae


                    elif LA48 == NUMBER:
                        LA48_4 = self.input.LA(3)

                        if (LA48_4 == DIVIDE) :
                            alt48 = 2
                        elif (LA48_4 == NEWLINE) :
                            alt48 = 1
                        else:
                            nvae = NoViableAltException("", 48, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 48, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 48, 0, self.input)

                    raise nvae


                if alt48 == 1:
                    # grammar/ShyRecognizerFrontend.g:233:9: ID num_whole NEWLINE
                    pass 
                    ID228 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2493) 
                    stream_ID.add(ID228)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2495)
                    num_whole229 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole229.tree)


                    NEWLINE230 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2497) 
                    stream_NEWLINE.add(NEWLINE230)


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
                    # 233:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:233:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt48 == 2:
                    # grammar/ShyRecognizerFrontend.g:234:9: ID num_fract NEWLINE
                    pass 
                    ID231 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2519) 
                    stream_ID.add(ID231)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2521)
                    num_fract232 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract232.tree)


                    NEWLINE233 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2523) 
                    stream_NEWLINE.add(NEWLINE233)


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
                    # 234:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:234:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt48 == 3:
                    # grammar/ShyRecognizerFrontend.g:235:9: ID EXPRESSION NEWLINE
                    pass 
                    ID234 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2545) 
                    stream_ID.add(ID234)


                    EXPRESSION235 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2547) 
                    stream_EXPRESSION.add(EXPRESSION235)


                    NEWLINE236 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2549) 
                    stream_NEWLINE.add(NEWLINE236)


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
                    # 235:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:235:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:238:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES237 = None
        ID238 = None
        NEWLINE239 = None
        INDENT240 = None
        NEWLINE241 = None
        DEDENT243 = None
        NEWLINE244 = None
        types_item242 = None


        TYPES237_tree = None
        ID238_tree = None
        NEWLINE239_tree = None
        INDENT240_tree = None
        NEWLINE241_tree = None
        DEDENT243_tree = None
        NEWLINE244_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:239:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:239:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES237 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2580) 
                stream_TYPES.add(TYPES237)


                ID238 = self.match(self.input, ID, self.FOLLOW_ID_in_types2582) 
                stream_ID.add(ID238)


                NEWLINE239 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2584) 
                stream_NEWLINE.add(NEWLINE239)


                INDENT240 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2594) 
                stream_INDENT.add(INDENT240)


                NEWLINE241 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2596) 
                stream_NEWLINE.add(NEWLINE241)


                # grammar/ShyRecognizerFrontend.g:240:24: ( types_item )+
                cnt49 = 0
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == ID) :
                        alt49 = 1


                    if alt49 == 1:
                        # grammar/ShyRecognizerFrontend.g:240:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2598)
                        types_item242 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item242.tree)



                    else:
                        if cnt49 >= 1:
                            break #loop49

                        eee = EarlyExitException(49, self.input)
                        raise eee

                    cnt49 += 1


                DEDENT243 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2602) 
                stream_DEDENT.add(DEDENT243)


                NEWLINE244 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2604) 
                stream_NEWLINE.add(NEWLINE244)


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
                # 241:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:241:13: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:241:30: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:243:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID245 = None
        attrs_hints246 = None


        ID245_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:243:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:243:14: ID attrs_hints
                pass 
                ID245 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2639) 
                stream_ID.add(ID245)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2641)
                attrs_hints246 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints246.tree)


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
                # 243:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:243:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:245:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES247 = None
        ID248 = None
        NEWLINE249 = None
        INDENT250 = None
        NEWLINE251 = None
        DEDENT253 = None
        NEWLINE254 = None
        messages_item252 = None


        MESSAGES247_tree = None
        ID248_tree = None
        NEWLINE249_tree = None
        INDENT250_tree = None
        NEWLINE251_tree = None
        DEDENT253_tree = None
        NEWLINE254_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:246:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:246:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES247 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2668) 
                stream_MESSAGES.add(MESSAGES247)


                ID248 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2670) 
                stream_ID.add(ID248)


                NEWLINE249 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2672) 
                stream_NEWLINE.add(NEWLINE249)


                INDENT250 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2682) 
                stream_INDENT.add(INDENT250)


                NEWLINE251 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2684) 
                stream_NEWLINE.add(NEWLINE251)


                # grammar/ShyRecognizerFrontend.g:247:24: ( messages_item )+
                cnt50 = 0
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == ID) :
                        alt50 = 1


                    if alt50 == 1:
                        # grammar/ShyRecognizerFrontend.g:247:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2686)
                        messages_item252 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item252.tree)



                    else:
                        if cnt50 >= 1:
                            break #loop50

                        eee = EarlyExitException(50, self.input)
                        raise eee

                    cnt50 += 1


                DEDENT253 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2690) 
                stream_DEDENT.add(DEDENT253)


                NEWLINE254 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2692) 
                stream_NEWLINE.add(NEWLINE254)


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
                # 248:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:248:13: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:248:33: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:251:1: messages_item : ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) );
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID255 = None
        ID257 = None
        REPLY258 = None
        ID260 = None
        NEWLINE261 = None
        INDENT262 = None
        NEWLINE263 = None
        REPLY264 = None
        DEDENT266 = None
        NEWLINE267 = None
        ID268 = None
        REQUEST269 = None
        ID271 = None
        NEWLINE272 = None
        INDENT273 = None
        NEWLINE274 = None
        REQUEST275 = None
        DEDENT277 = None
        NEWLINE278 = None
        ID279 = None
        NEWLINE280 = None
        INDENT281 = None
        NEWLINE282 = None
        REQUEST283 = None
        REPLY285 = None
        DEDENT287 = None
        NEWLINE288 = None
        attrs_hints256 = None

        attrs_hints259 = None

        attrs_hints265 = None

        attrs_hints270 = None

        attrs_hints276 = None

        attrs_hints284 = None

        attrs_hints286 = None


        ID255_tree = None
        ID257_tree = None
        REPLY258_tree = None
        ID260_tree = None
        NEWLINE261_tree = None
        INDENT262_tree = None
        NEWLINE263_tree = None
        REPLY264_tree = None
        DEDENT266_tree = None
        NEWLINE267_tree = None
        ID268_tree = None
        REQUEST269_tree = None
        ID271_tree = None
        NEWLINE272_tree = None
        INDENT273_tree = None
        NEWLINE274_tree = None
        REQUEST275_tree = None
        DEDENT277_tree = None
        NEWLINE278_tree = None
        ID279_tree = None
        NEWLINE280_tree = None
        INDENT281_tree = None
        NEWLINE282_tree = None
        REQUEST283_tree = None
        REPLY285_tree = None
        DEDENT287_tree = None
        NEWLINE288_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_REPLY = RewriteRuleTokenStream(self._adaptor, "token REPLY")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:252:5: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) )
                alt51 = 6
                alt51 = self.dfa51.predict(self.input)
                if alt51 == 1:
                    # grammar/ShyRecognizerFrontend.g:252:9: ID attrs_hints
                    pass 
                    ID255 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2734) 
                    stream_ID.add(ID255)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2736)
                    attrs_hints256 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints256.tree)


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
                    # 253:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:253:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
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




                elif alt51 == 2:
                    # grammar/ShyRecognizerFrontend.g:256:9: ID REPLY attrs_hints
                    pass 
                    ID257 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2797) 
                    stream_ID.add(ID257)


                    REPLY258 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2799) 
                    stream_REPLY.add(REPLY258)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2801)
                    attrs_hints259 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints259.tree)


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
                    # 257:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:257:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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




                elif alt51 == 3:
                    # grammar/ShyRecognizerFrontend.g:260:9: ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID260 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2862) 
                    stream_ID.add(ID260)


                    NEWLINE261 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2864) 
                    stream_NEWLINE.add(NEWLINE261)


                    INDENT262 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item2866) 
                    stream_INDENT.add(INDENT262)


                    NEWLINE263 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2868) 
                    stream_NEWLINE.add(NEWLINE263)


                    REPLY264 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2870) 
                    stream_REPLY.add(REPLY264)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2872)
                    attrs_hints265 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints265.tree)


                    DEDENT266 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item2874) 
                    stream_DEDENT.add(DEDENT266)


                    NEWLINE267 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2876) 
                    stream_NEWLINE.add(NEWLINE267)


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
                    # 261:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:261:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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




                elif alt51 == 4:
                    # grammar/ShyRecognizerFrontend.g:264:9: ID REQUEST attrs_hints
                    pass 
                    ID268 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2937) 
                    stream_ID.add(ID268)


                    REQUEST269 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item2939) 
                    stream_REQUEST.add(REQUEST269)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2941)
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
                    # 265:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:265:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
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




                elif alt51 == 5:
                    # grammar/ShyRecognizerFrontend.g:268:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE
                    pass 
                    ID271 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3002) 
                    stream_ID.add(ID271)


                    NEWLINE272 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3004) 
                    stream_NEWLINE.add(NEWLINE272)


                    INDENT273 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3006) 
                    stream_INDENT.add(INDENT273)


                    NEWLINE274 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3008) 
                    stream_NEWLINE.add(NEWLINE274)


                    REQUEST275 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3010) 
                    stream_REQUEST.add(REQUEST275)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3012)
                    attrs_hints276 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints276.tree)


                    DEDENT277 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3014) 
                    stream_DEDENT.add(DEDENT277)


                    NEWLINE278 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3016) 
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
                    # 269:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:269:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
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




                elif alt51 == 6:
                    # grammar/ShyRecognizerFrontend.g:272:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID279 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3077) 
                    stream_ID.add(ID279)


                    NEWLINE280 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3079) 
                    stream_NEWLINE.add(NEWLINE280)


                    INDENT281 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3081) 
                    stream_INDENT.add(INDENT281)


                    NEWLINE282 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3083) 
                    stream_NEWLINE.add(NEWLINE282)


                    REQUEST283 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3097) 
                    stream_REQUEST.add(REQUEST283)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3099)
                    attrs_hints284 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints284.tree)


                    REPLY285 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item3113) 
                    stream_REPLY.add(REPLY285)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3115)
                    attrs_hints286 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints286.tree)


                    DEDENT287 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3125) 
                    stream_DEDENT.add(DEDENT287)


                    NEWLINE288 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3127) 
                    stream_NEWLINE.add(NEWLINE288)


                    # AST Rewrite
                    # elements: attrs_hints, attrs_hints, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 276:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:276:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:282:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS289 = None
        ID290 = None
        attrs_hints291 = None


        VARS289_tree = None
        ID290_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:283:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:283:9: VARS ID attrs_hints
                pass 
                VARS289 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars3217) 
                stream_VARS.add(VARS289)


                ID290 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3219) 
                stream_ID.add(ID290)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3221)
                attrs_hints291 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints291.tree)


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
                # 284:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:284:13: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:287:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE293 = None
        NEWLINE294 = None
        INDENT295 = None
        NEWLINE296 = None
        NEWLINE298 = None
        DEDENT299 = None
        NEWLINE300 = None
        NEWLINE302 = None
        INDENT303 = None
        NEWLINE304 = None
        NEWLINE306 = None
        DEDENT307 = None
        NEWLINE308 = None
        attr_hint292 = None

        attr_hint297 = None

        attr_hint301 = None

        attr_hint305 = None


        NEWLINE293_tree = None
        NEWLINE294_tree = None
        INDENT295_tree = None
        NEWLINE296_tree = None
        NEWLINE298_tree = None
        DEDENT299_tree = None
        NEWLINE300_tree = None
        NEWLINE302_tree = None
        INDENT303_tree = None
        NEWLINE304_tree = None
        NEWLINE306_tree = None
        DEDENT307_tree = None
        NEWLINE308_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:288:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt54 = 3
                alt54 = self.dfa54.predict(self.input)
                if alt54 == 1:
                    # grammar/ShyRecognizerFrontend.g:288:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3261)
                    attr_hint292 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint292.tree)


                    NEWLINE293 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3263) 
                    stream_NEWLINE.add(NEWLINE293)


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
                    # 289:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt54 == 2:
                    # grammar/ShyRecognizerFrontend.g:290:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE294 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3288) 
                    stream_NEWLINE.add(NEWLINE294)


                    # grammar/ShyRecognizerFrontend.g:291:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:291:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT295 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3300) 
                    stream_INDENT.add(INDENT295)


                    NEWLINE296 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3302) 
                    stream_NEWLINE.add(NEWLINE296)


                    # grammar/ShyRecognizerFrontend.g:291:26: ( attr_hint NEWLINE )+
                    cnt52 = 0
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == CURLY_OPEN or LA52_0 == ID) :
                            alt52 = 1


                        if alt52 == 1:
                            # grammar/ShyRecognizerFrontend.g:291:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3306)
                            attr_hint297 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint297.tree)


                            NEWLINE298 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3308) 
                            stream_NEWLINE.add(NEWLINE298)



                        else:
                            if cnt52 >= 1:
                                break #loop52

                            eee = EarlyExitException(52, self.input)
                            raise eee

                        cnt52 += 1


                    DEDENT299 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3314) 
                    stream_DEDENT.add(DEDENT299)


                    NEWLINE300 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3316) 
                    stream_NEWLINE.add(NEWLINE300)





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
                    # 292:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:292:30: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt54 == 3:
                    # grammar/ShyRecognizerFrontend.g:293:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3345)
                    attr_hint301 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint301.tree)


                    NEWLINE302 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3347) 
                    stream_NEWLINE.add(NEWLINE302)


                    # grammar/ShyRecognizerFrontend.g:294:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:294:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT303 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3359) 
                    stream_INDENT.add(INDENT303)


                    NEWLINE304 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3361) 
                    stream_NEWLINE.add(NEWLINE304)


                    # grammar/ShyRecognizerFrontend.g:294:26: ( attr_hint NEWLINE )+
                    cnt53 = 0
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == CURLY_OPEN or LA53_0 == ID) :
                            alt53 = 1


                        if alt53 == 1:
                            # grammar/ShyRecognizerFrontend.g:294:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3365)
                            attr_hint305 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint305.tree)


                            NEWLINE306 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3367) 
                            stream_NEWLINE.add(NEWLINE306)



                        else:
                            if cnt53 >= 1:
                                break #loop53

                            eee = EarlyExitException(53, self.input)
                            raise eee

                        cnt53 += 1


                    DEDENT307 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3373) 
                    stream_DEDENT.add(DEDENT307)


                    NEWLINE308 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3375) 
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
                    # 295:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:295:30: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:297:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID309 = None
        ID311 = None
        NEWLINE313 = None
        INDENT314 = None
        NEWLINE315 = None
        ID316 = None
        NEWLINE317 = None
        DEDENT318 = None
        hint310 = None

        hint312 = None


        ID309_tree = None
        ID311_tree = None
        NEWLINE313_tree = None
        INDENT314_tree = None
        NEWLINE315_tree = None
        ID316_tree = None
        NEWLINE317_tree = None
        DEDENT318_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:298:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt59 = 3
                alt59 = self.dfa59.predict(self.input)
                if alt59 == 1:
                    # grammar/ShyRecognizerFrontend.g:298:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:298:9: ( ID )+
                    cnt55 = 0
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == ID) :
                            alt55 = 1


                        if alt55 == 1:
                            # grammar/ShyRecognizerFrontend.g:298:9: ID
                            pass 
                            ID309 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3413) 
                            stream_ID.add(ID309)



                        else:
                            if cnt55 >= 1:
                                break #loop55

                            eee = EarlyExitException(55, self.input)
                            raise eee

                        cnt55 += 1


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
                    # 299:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:299:13: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:299:46: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:299:46: ^( TREE_ATTR ID )
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




                elif alt59 == 2:
                    # grammar/ShyRecognizerFrontend.g:300:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3455)
                    hint310 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint310.tree)


                    # grammar/ShyRecognizerFrontend.g:300:14: ( ID )+
                    cnt56 = 0
                    while True: #loop56
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == ID) :
                            alt56 = 1


                        if alt56 == 1:
                            # grammar/ShyRecognizerFrontend.g:300:14: ID
                            pass 
                            ID311 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3457) 
                            stream_ID.add(ID311)



                        else:
                            if cnt56 >= 1:
                                break #loop56

                            eee = EarlyExitException(56, self.input)
                            raise eee

                        cnt56 += 1


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
                    # 301:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:301:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:301:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:301:36: ^( TREE_ATTR ID )
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




                elif alt59 == 3:
                    # grammar/ShyRecognizerFrontend.g:302:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3498)
                    hint312 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint312.tree)


                    NEWLINE313 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3500) 
                    stream_NEWLINE.add(NEWLINE313)


                    INDENT314 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint3502) 
                    stream_INDENT.add(INDENT314)


                    NEWLINE315 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3504) 
                    stream_NEWLINE.add(NEWLINE315)


                    # grammar/ShyRecognizerFrontend.g:302:37: ( ( ID )+ NEWLINE )+
                    cnt58 = 0
                    while True: #loop58
                        alt58 = 2
                        LA58_0 = self.input.LA(1)

                        if (LA58_0 == ID) :
                            alt58 = 1


                        if alt58 == 1:
                            # grammar/ShyRecognizerFrontend.g:302:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:302:39: ( ID )+
                            cnt57 = 0
                            while True: #loop57
                                alt57 = 2
                                LA57_0 = self.input.LA(1)

                                if (LA57_0 == ID) :
                                    alt57 = 1


                                if alt57 == 1:
                                    # grammar/ShyRecognizerFrontend.g:302:39: ID
                                    pass 
                                    ID316 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3508) 
                                    stream_ID.add(ID316)



                                else:
                                    if cnt57 >= 1:
                                        break #loop57

                                    eee = EarlyExitException(57, self.input)
                                    raise eee

                                cnt57 += 1


                            NEWLINE317 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3512) 
                            stream_NEWLINE.add(NEWLINE317)



                        else:
                            if cnt58 >= 1:
                                break #loop58

                            eee = EarlyExitException(58, self.input)
                            raise eee

                        cnt58 += 1


                    DEDENT318 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint3518) 
                    stream_DEDENT.add(DEDENT318)


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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:306:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN319 = None
        ID320 = None
        CURLY_CLOSE321 = None
        CURLY_OPEN322 = None
        ID323 = None
        CURLY_CLOSE325 = None
        hint_arg324 = None


        CURLY_OPEN319_tree = None
        ID320_tree = None
        CURLY_CLOSE321_tree = None
        CURLY_OPEN322_tree = None
        ID323_tree = None
        CURLY_CLOSE325_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:307:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == CURLY_OPEN) :
                    LA61_1 = self.input.LA(2)

                    if (LA61_1 == ID) :
                        LA61_2 = self.input.LA(3)

                        if (LA61_2 == CURLY_CLOSE) :
                            alt61 = 1
                        elif (LA61_2 == ID or LA61_2 == UNDERSCORE) :
                            alt61 = 2
                        else:
                            nvae = NoViableAltException("", 61, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 61, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 61, 0, self.input)

                    raise nvae


                if alt61 == 1:
                    # grammar/ShyRecognizerFrontend.g:307:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN319 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3566) 
                    stream_CURLY_OPEN.add(CURLY_OPEN319)


                    ID320 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3568) 
                    stream_ID.add(ID320)


                    CURLY_CLOSE321 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3570) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE321)


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
                    # 307:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:307:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt61 == 2:
                    # grammar/ShyRecognizerFrontend.g:308:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN322 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3590) 
                    stream_CURLY_OPEN.add(CURLY_OPEN322)


                    ID323 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3592) 
                    stream_ID.add(ID323)


                    # grammar/ShyRecognizerFrontend.g:308:23: ( hint_arg )+
                    cnt60 = 0
                    while True: #loop60
                        alt60 = 2
                        LA60_0 = self.input.LA(1)

                        if (LA60_0 == ID or LA60_0 == UNDERSCORE) :
                            alt60 = 1


                        if alt60 == 1:
                            # grammar/ShyRecognizerFrontend.g:308:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint3594)
                            hint_arg324 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg324.tree)



                        else:
                            if cnt60 >= 1:
                                break #loop60

                            eee = EarlyExitException(60, self.input)
                            raise eee

                        cnt60 += 1


                    CURLY_CLOSE325 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3598) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE325)


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
                    # 308:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:308:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:308:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:310:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set326 = None

        set326_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:310:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set326 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set326))

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
    # grammar/ShyRecognizerFrontend.g:312:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS327 = None
        NUMBER328 = None

        MINUS327_tree = None
        NUMBER328_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:312:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:312:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:312:13: ( MINUS )?
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == MINUS) :
                    alt62 = 1
                if alt62 == 1:
                    # grammar/ShyRecognizerFrontend.g:312:13: MINUS
                    pass 
                    MINUS327 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3637)
                    MINUS327_tree = self._adaptor.createWithPayload(MINUS327)
                    self._adaptor.addChild(root_0, MINUS327_tree)






                NUMBER328 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3641)
                NUMBER328_tree = self._adaptor.createWithPayload(NUMBER328)
                self._adaptor.addChild(root_0, NUMBER328_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:313:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS329 = None
        NUMBER330 = None
        DIVIDE331 = None
        NUMBER332 = None

        MINUS329_tree = None
        NUMBER330_tree = None
        DIVIDE331_tree = None
        NUMBER332_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:313:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:313:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:313:13: ( MINUS )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == MINUS) :
                    alt63 = 1
                if alt63 == 1:
                    # grammar/ShyRecognizerFrontend.g:313:13: MINUS
                    pass 
                    MINUS329 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3649)
                    MINUS329_tree = self._adaptor.createWithPayload(MINUS329)
                    self._adaptor.addChild(root_0, MINUS329_tree)






                NUMBER330 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3653)
                NUMBER330_tree = self._adaptor.createWithPayload(NUMBER330)
                self._adaptor.addChild(root_0, NUMBER330_tree)



                DIVIDE331 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3655)
                DIVIDE331_tree = self._adaptor.createWithPayload(DIVIDE331)
                self._adaptor.addChild(root_0, DIVIDE331_tree)



                NUMBER332 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3657)
                NUMBER332_tree = self._adaptor.createWithPayload(NUMBER332)
                self._adaptor.addChild(root_0, NUMBER332_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #20

    DFA20_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA20_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA20_min = DFA.unpack(
        u"\1\22\1\7\4\uffff\1\7\2\10\1\33\1\10\1\15\1\10\1\33\2\uffff\1\10"
        )

    DFA20_max = DFA.unpack(
        u"\1\126\1\44\4\uffff\3\44\1\33\1\44\1\126\1\44\1\33\2\uffff\1\44"
        )

    DFA20_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\10\uffff\1\2\1\1\1\uffff"
        )

    DFA20_special = DFA.unpack(
        u"\21\uffff"
        )


    DFA20_transition = [
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

    # class definition for DFA #20

    class DFA20(DFA):
        pass


    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA32_min = DFA.unpack(
        u"\1\22\1\7\2\10\1\33\1\10\1\22\1\23\1\10\1\33\4\uffff\1\10"
        )

    DFA32_max = DFA.unpack(
        u"\4\44\1\33\2\44\1\32\1\44\1\33\4\uffff\1\44"
        )

    DFA32_accept = DFA.unpack(
        u"\12\uffff\1\2\1\1\1\4\1\3\1\uffff"
        )

    DFA32_special = DFA.unpack(
        u"\17\uffff"
        )


    DFA32_transition = [
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

    # class definition for DFA #32

    class DFA32(DFA):
        pass


    # lookup tables for DFA #40

    DFA40_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA40_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA40_min = DFA.unpack(
        u"\1\23\4\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA40_max = DFA.unpack(
        u"\1\23\4\44\1\33\1\44\1\25\1\uffff\1\33\1\uffff\1\44"
        )

    DFA40_accept = DFA.unpack(
        u"\10\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA40_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA40_transition = [
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

    # class definition for DFA #40

    class DFA40(DFA):
        pass


    # lookup tables for DFA #41

    DFA41_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA41_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA41_min = DFA.unpack(
        u"\1\23\4\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA41_max = DFA.unpack(
        u"\1\23\4\44\1\33\1\44\1\25\1\33\2\uffff\1\44"
        )

    DFA41_accept = DFA.unpack(
        u"\11\uffff\1\2\1\1\1\uffff"
        )

    DFA41_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA41_transition = [
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

    # class definition for DFA #41

    class DFA41(DFA):
        pass


    # lookup tables for DFA #51

    DFA51_eot = DFA.unpack(
        u"\77\uffff"
        )

    DFA51_eof = DFA.unpack(
        u"\77\uffff"
        )

    DFA51_min = DFA.unpack(
        u"\1\23\1\14\1\uffff\1\25\2\uffff\1\32\1\14\1\uffff\1\14\2\23\1\25"
        u"\1\15\1\13\1\32\1\uffff\1\32\1\uffff\1\23\1\13\2\14\1\23\1\25\5"
        u"\23\1\32\1\14\1\13\1\14\1\13\1\23\1\32\1\23\1\13\1\32\1\23\1\13"
        u"\1\23\1\15\1\23\1\25\1\23\1\15\1\23\1\25\1\23\1\15\3\32\4\23\2"
        u"\15\2\32"
        )

    DFA51_max = DFA.unpack(
        u"\1\23\1\42\1\uffff\1\25\2\uffff\1\32\1\42\1\uffff\2\32\1\23\1\25"
        u"\1\41\1\122\1\32\1\uffff\1\32\1\uffff\1\32\1\122\2\23\1\32\1\25"
        u"\2\32\1\23\1\32\1\23\1\32\1\23\1\122\1\23\1\122\1\23\2\32\1\122"
        u"\2\32\1\122\1\32\1\41\1\32\1\25\1\32\1\41\1\32\1\25\1\32\1\23\3"
        u"\32\2\23\2\32\2\23\2\32"
        )

    DFA51_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\4\1\1\2\uffff\1\3\7\uffff\1\5\1\uffff\1"
        u"\6\54\uffff"
        )

    DFA51_special = DFA.unpack(
        u"\77\uffff"
        )


    DFA51_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\5\6\uffff\1\5\6\uffff\1\3\6\uffff\1\2\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u""),
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

    # class definition for DFA #51

    class DFA51(DFA):
        pass


    # lookup tables for DFA #54

    DFA54_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA54_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA54_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA54_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\123\1\122\2\uffff\1\32\1\122\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA54_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA54_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA54_transition = [
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

    # class definition for DFA #54

    class DFA54(DFA):
        pass


    # lookup tables for DFA #59

    DFA59_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA59_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA59_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA59_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\122\1\32\1\122\2\uffff\1\32"
        )

    DFA59_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA59_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA59_transition = [
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

    # class definition for DFA #59

    class DFA59(DFA):
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
    FOLLOW_statement_call_single_line_in_statement1098 = frozenset([26])
    FOLLOW_NEWLINE_in_statement1100 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement1126 = frozenset([1])
    FOLLOW_statement_if_in_statement1136 = frozenset([1])
    FOLLOW_statement_assign_in_statement1146 = frozenset([1])
    FOLLOW_statement_while_in_statement1156 = frozenset([1])
    FOLLOW_statement_with_in_statement1166 = frozenset([1])
    FOLLOW_statement_in_statements1185 = frozenset([1, 18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_WITH_in_statement_with1227 = frozenset([19])
    FOLLOW_ID_in_statement_with1229 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1231 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1241 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1243 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_with1245 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1247 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1249 = frozenset([1])
    FOLLOW_ID_in_statement_assign1289 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1293 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1295 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1299 = frozenset([1])
    FOLLOW_ID_in_statement_assign1352 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1356 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1358 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1360 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1362 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1374 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1378 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_assign1384 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1386 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1439 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1443 = frozenset([19])
    FOLLOW_ID_in_statement_assign1445 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1449 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1502 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1506 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1508 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1510 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1512 = frozenset([19])
    FOLLOW_ID_in_statement_assign1524 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1528 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1534 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1536 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1598 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1600 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1602 = frozenset([15])
    FOLLOW_DO_in_statement_while1606 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1608 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1622 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1624 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_while1626 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1628 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1630 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1670 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1680 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1692 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1800 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1802 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1834 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1836 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1868 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1870 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1874 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1876 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1890 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1892 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_elif_body1894 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1896 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1898 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1938 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1940 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1954 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1956 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_else1958 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1960 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1962 = frozenset([1])
    FOLLOW_condition_call_in_condition2000 = frozenset([1])
    FOLLOW_ANY_in_condition2029 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2031 = frozenset([1])
    FOLLOW_ALL_in_condition2060 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2062 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls2100 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls2110 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls2112 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2114 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls2116 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls2120 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2122 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call2156 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call2166 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line2185 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line2187 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2213 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2232 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_single_line2234 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2278 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2280 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2284 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2294 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2296 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2300 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2302 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_call_multi_line2308 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2310 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2346 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_ID_in_arbitrary_value2363 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2373 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2383 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2393 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2403 = frozenset([1])
    FOLLOW_CONSTS_in_consts2422 = frozenset([19])
    FOLLOW_ID_in_consts2424 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2426 = frozenset([21])
    FOLLOW_INDENT_in_consts2436 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2438 = frozenset([19])
    FOLLOW_consts_items_in_consts2440 = frozenset([13])
    FOLLOW_DEDENT_in_consts2442 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2444 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2477 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2493 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2495 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2497 = frozenset([1])
    FOLLOW_ID_in_consts_item2519 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2521 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2523 = frozenset([1])
    FOLLOW_ID_in_consts_item2545 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2547 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2549 = frozenset([1])
    FOLLOW_TYPES_in_types2580 = frozenset([19])
    FOLLOW_ID_in_types2582 = frozenset([26])
    FOLLOW_NEWLINE_in_types2584 = frozenset([21])
    FOLLOW_INDENT_in_types2594 = frozenset([26])
    FOLLOW_NEWLINE_in_types2596 = frozenset([19])
    FOLLOW_types_item_in_types2598 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2602 = frozenset([26])
    FOLLOW_NEWLINE_in_types2604 = frozenset([1])
    FOLLOW_ID_in_types_item2639 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2641 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2668 = frozenset([19])
    FOLLOW_ID_in_messages2670 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2672 = frozenset([21])
    FOLLOW_INDENT_in_messages2682 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2684 = frozenset([19])
    FOLLOW_messages_item_in_messages2686 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2690 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2692 = frozenset([1])
    FOLLOW_ID_in_messages_item2734 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2736 = frozenset([1])
    FOLLOW_ID_in_messages_item2797 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2799 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2801 = frozenset([1])
    FOLLOW_ID_in_messages_item2862 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2864 = frozenset([21])
    FOLLOW_INDENT_in_messages_item2866 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2868 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2870 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2872 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item2874 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2876 = frozenset([1])
    FOLLOW_ID_in_messages_item2937 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item2939 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2941 = frozenset([1])
    FOLLOW_ID_in_messages_item3002 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3004 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3006 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3008 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3010 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3012 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3014 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3016 = frozenset([1])
    FOLLOW_ID_in_messages_item3077 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3079 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3081 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3083 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3097 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3099 = frozenset([33])
    FOLLOW_REPLY_in_messages_item3113 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3115 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3125 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3127 = frozenset([1])
    FOLLOW_VARS_in_vars3217 = frozenset([19])
    FOLLOW_ID_in_vars3219 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars3221 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3261 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3263 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints3288 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3300 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3302 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3306 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3308 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3314 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3316 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3345 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3347 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3359 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3361 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3365 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3367 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3373 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3375 = frozenset([1])
    FOLLOW_ID_in_attr_hint3413 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3455 = frozenset([19])
    FOLLOW_ID_in_attr_hint3457 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3498 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3500 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint3502 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3504 = frozenset([19])
    FOLLOW_ID_in_attr_hint3508 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint3512 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint3518 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3566 = frozenset([19])
    FOLLOW_ID_in_hint3568 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint3570 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3590 = frozenset([19])
    FOLLOW_ID_in_hint3592 = frozenset([19, 82])
    FOLLOW_hint_arg_in_hint3594 = frozenset([11, 19, 82])
    FOLLOW_CURLY_CLOSE_in_hint3598 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3637 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3641 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3649 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3653 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3655 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3657 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
