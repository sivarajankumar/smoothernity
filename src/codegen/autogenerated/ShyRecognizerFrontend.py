# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-10 19:37:28

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
SEND=35
STATELESS=36
STRING=37
TRACE=38
TREE_ARBITRARY_TOKEN=39
TREE_ATTR=40
TREE_ATTRS_HINTS=41
TREE_ATTR_HINT=42
TREE_CONDITION_ALL=43
TREE_CONDITION_ANY=44
TREE_CONSTS=45
TREE_COPY=46
TREE_COPY_PASTE=47
TREE_EXPRESSION=48
TREE_HINT=49
TREE_HINT_NONE=50
TREE_LOCAL_VARS=51
TREE_MESSAGES=52
TREE_MESSAGES_ITEM=53
TREE_MESSAGES_ITEM_RECEIVE=54
TREE_MESSAGES_ITEM_REPLY=55
TREE_MESSAGES_ITEM_REQUEST=56
TREE_MODULE=57
TREE_MODULE_QUEUE=58
TREE_NUM_FRACT=59
TREE_NUM_WHOLE=60
TREE_PASTE=61
TREE_PASTE_REPLACE=62
TREE_PASTE_WITH=63
TREE_PROC=64
TREE_PROC_ARGS=65
TREE_RECEIVE=66
TREE_REQUEST=67
TREE_STATELESS=68
TREE_STATEMENTS=69
TREE_STATEMENT_ASSIGN=70
TREE_STATEMENT_ASSIGN_TO=71
TREE_STATEMENT_CALL=72
TREE_STATEMENT_ELIF=73
TREE_STATEMENT_ELSE=74
TREE_STATEMENT_IF=75
TREE_STATEMENT_SEND=76
TREE_STATEMENT_WHILE=77
TREE_STATEMENT_WITH=78
TREE_TRACE=79
TREE_TYPES=80
TREE_TYPES_ITEM=81
TREE_VARS=82
TYPES=83
UNDERSCORE=84
VARS=85
WHILE=86
WHITESPACE=87
WITH=88

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ALL", "ANY", "ARGS", "ARROW_LEFT", "ARROW_RIGHT", "CONSTS", "COPY", 
    "CURLY_CLOSE", "CURLY_OPEN", "DEDENT", "DIVIDE", "DO", "ELIF", "ELSE", 
    "EXPRESSION", "ID", "IF", "INDENT", "MESSAGES", "MINUS", "MODULE", "MODULE_QUEUE", 
    "NEWLINE", "NUMBER", "OPS", "PASTE", "PROC", "RECEIVE", "REPLACE", "REPLY", 
    "REQUEST", "SEND", "STATELESS", "STRING", "TRACE", "TREE_ARBITRARY_TOKEN", 
    "TREE_ATTR", "TREE_ATTRS_HINTS", "TREE_ATTR_HINT", "TREE_CONDITION_ALL", 
    "TREE_CONDITION_ANY", "TREE_CONSTS", "TREE_COPY", "TREE_COPY_PASTE", 
    "TREE_EXPRESSION", "TREE_HINT", "TREE_HINT_NONE", "TREE_LOCAL_VARS", 
    "TREE_MESSAGES", "TREE_MESSAGES_ITEM", "TREE_MESSAGES_ITEM_RECEIVE", 
    "TREE_MESSAGES_ITEM_REPLY", "TREE_MESSAGES_ITEM_REQUEST", "TREE_MODULE", 
    "TREE_MODULE_QUEUE", "TREE_NUM_FRACT", "TREE_NUM_WHOLE", "TREE_PASTE", 
    "TREE_PASTE_REPLACE", "TREE_PASTE_WITH", "TREE_PROC", "TREE_PROC_ARGS", 
    "TREE_RECEIVE", "TREE_REQUEST", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", "TREE_STATEMENT_CALL", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_SEND", 
    "TREE_STATEMENT_WHILE", "TREE_STATEMENT_WITH", "TREE_TRACE", "TREE_TYPES", 
    "TREE_TYPES_ITEM", "TREE_VARS", "TYPES", "UNDERSCORE", "VARS", "WHILE", 
    "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

        self.dfa19 = self.DFA19(
            self, 19,
            eot = self.DFA19_eot,
            eof = self.DFA19_eof,
            min = self.DFA19_min,
            max = self.DFA19_max,
            accept = self.DFA19_accept,
            special = self.DFA19_special,
            transition = self.DFA19_transition
            )

        self.dfa31 = self.DFA31(
            self, 31,
            eot = self.DFA31_eot,
            eof = self.DFA31_eof,
            min = self.DFA31_min,
            max = self.DFA31_max,
            accept = self.DFA31_accept,
            special = self.DFA31_special,
            transition = self.DFA31_transition
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

        self.dfa48 = self.DFA48(
            self, 48,
            eot = self.DFA48_eot,
            eof = self.DFA48_eof,
            min = self.DFA48_min,
            max = self.DFA48_max,
            accept = self.DFA48_accept,
            special = self.DFA48_special,
            transition = self.DFA48_transition
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

        self.dfa58 = self.DFA58(
            self, 58,
            eot = self.DFA58_eot,
            eof = self.DFA58_eof,
            min = self.DFA58_min,
            max = self.DFA58_max,
            accept = self.DFA58_accept,
            special = self.DFA58_special,
            transition = self.DFA58_transition
            )

        self.dfa63 = self.DFA63(
            self, 63,
            eot = self.DFA63_eot,
            eof = self.DFA63_eof,
            min = self.DFA63_min,
            max = self.DFA63_max,
            accept = self.DFA63_accept,
            special = self.DFA63_special,
            transition = self.DFA63_transition
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
    # grammar/ShyRecognizerFrontend.g:26:1: module : MODULE ID NEWLINE INDENT NEWLINE ( module_item )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_item )* ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE8 = None
        ID9 = None
        NEWLINE10 = None
        INDENT11 = None
        NEWLINE12 = None
        DEDENT14 = None
        NEWLINE15 = None
        module_item13 = None


        MODULE8_tree = None
        ID9_tree = None
        NEWLINE10_tree = None
        INDENT11_tree = None
        NEWLINE12_tree = None
        DEDENT14_tree = None
        NEWLINE15_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_module_item = RewriteRuleSubtreeStream(self._adaptor, "rule module_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:27:5: ( MODULE ID NEWLINE INDENT NEWLINE ( module_item )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_item )* ) )
                # grammar/ShyRecognizerFrontend.g:27:9: MODULE ID NEWLINE INDENT NEWLINE ( module_item )* DEDENT NEWLINE
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


                # grammar/ShyRecognizerFrontend.g:27:42: ( module_item )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == MODULE_QUEUE or (PROC <= LA2_0 <= RECEIVE) or LA2_0 == REQUEST) :
                        alt2 = 1


                    if alt2 == 1:
                        # grammar/ShyRecognizerFrontend.g:27:42: module_item
                        pass 
                        self._state.following.append(self.FOLLOW_module_item_in_module135)
                        module_item13 = self.module_item()

                        self._state.following.pop()
                        stream_module_item.add(module_item13.tree)



                    else:
                        break #loop2


                DEDENT14 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_module139) 
                stream_DEDENT.add(DEDENT14)


                NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module141) 
                stream_NEWLINE.add(NEWLINE15)


                # AST Rewrite
                # elements: ID, module_item
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 28:9: -> ^( TREE_MODULE ID ( module_item )* )
                # grammar/ShyRecognizerFrontend.g:28:13: ^( TREE_MODULE ID ( module_item )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MODULE, "TREE_MODULE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:28:31: ( module_item )*
                while stream_module_item.hasNext():
                    self._adaptor.addChild(root_1, stream_module_item.nextTree())


                stream_module_item.reset();

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


    class module_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.module_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "module_item"
    # grammar/ShyRecognizerFrontend.g:30:1: module_item : ( module_queue | proc | receive | request );
    def module_item(self, ):
        retval = self.module_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        module_queue16 = None

        proc17 = None

        receive18 = None

        request19 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:30:13: ( module_queue | proc | receive | request )
                alt3 = 4
                LA3 = self.input.LA(1)
                if LA3 == MODULE_QUEUE:
                    alt3 = 1
                elif LA3 == PROC:
                    alt3 = 2
                elif LA3 == RECEIVE:
                    alt3 = 3
                elif LA3 == REQUEST:
                    alt3 = 4
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # grammar/ShyRecognizerFrontend.g:30:15: module_queue
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_module_queue_in_module_item176)
                    module_queue16 = self.module_queue()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, module_queue16.tree)



                elif alt3 == 2:
                    # grammar/ShyRecognizerFrontend.g:30:30: proc
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_proc_in_module_item180)
                    proc17 = self.proc()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, proc17.tree)



                elif alt3 == 3:
                    # grammar/ShyRecognizerFrontend.g:30:37: receive
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_receive_in_module_item184)
                    receive18 = self.receive()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, receive18.tree)



                elif alt3 == 4:
                    # grammar/ShyRecognizerFrontend.g:30:47: request
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_request_in_module_item188)
                    request19 = self.request()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, request19.tree)



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "module_item"


    class module_queue_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.module_queue_return, self).__init__()

            self.tree = None





    # $ANTLR start "module_queue"
    # grammar/ShyRecognizerFrontend.g:32:1: module_queue : MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        retval = self.module_queue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE_QUEUE20 = None
        ID21 = None
        NEWLINE22 = None

        MODULE_QUEUE20_tree = None
        ID21_tree = None
        NEWLINE22_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE_QUEUE = RewriteRuleTokenStream(self._adaptor, "token MODULE_QUEUE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:33:5: ( MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerFrontend.g:33:9: MODULE_QUEUE ID NEWLINE
                pass 
                MODULE_QUEUE20 = self.match(self.input, MODULE_QUEUE, self.FOLLOW_MODULE_QUEUE_in_module_queue203) 
                stream_MODULE_QUEUE.add(MODULE_QUEUE20)


                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue205) 
                stream_ID.add(ID21)


                NEWLINE22 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module_queue207) 
                stream_NEWLINE.add(NEWLINE22)


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
                # 34:9: -> ^( TREE_MODULE_QUEUE ID )
                # grammar/ShyRecognizerFrontend.g:34:13: ^( TREE_MODULE_QUEUE ID )
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
    # grammar/ShyRecognizerFrontend.g:37:1: trace : TRACE ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_TRACE ID ( proc )* ) ;
    def trace(self, ):
        retval = self.trace_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TRACE23 = None
        ID24 = None
        NEWLINE25 = None
        INDENT26 = None
        NEWLINE27 = None
        DEDENT29 = None
        NEWLINE30 = None
        proc28 = None


        TRACE23_tree = None
        ID24_tree = None
        NEWLINE25_tree = None
        INDENT26_tree = None
        NEWLINE27_tree = None
        DEDENT29_tree = None
        NEWLINE30_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_TRACE = RewriteRuleTokenStream(self._adaptor, "token TRACE")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:38:5: ( TRACE ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_TRACE ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:38:9: TRACE ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                TRACE23 = self.match(self.input, TRACE, self.FOLLOW_TRACE_in_trace245) 
                stream_TRACE.add(TRACE23)


                ID24 = self.match(self.input, ID, self.FOLLOW_ID_in_trace247) 
                stream_ID.add(ID24)


                NEWLINE25 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_trace249) 
                stream_NEWLINE.add(NEWLINE25)


                # grammar/ShyRecognizerFrontend.g:38:26: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == INDENT) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerFrontend.g:38:28: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT26 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_trace253) 
                    stream_INDENT.add(INDENT26)


                    NEWLINE27 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_trace255) 
                    stream_NEWLINE.add(NEWLINE27)


                    # grammar/ShyRecognizerFrontend.g:38:43: ( proc )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == PROC) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammar/ShyRecognizerFrontend.g:38:43: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_trace257)
                            proc28 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc28.tree)



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    DEDENT29 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_trace261) 
                    stream_DEDENT.add(DEDENT29)


                    NEWLINE30 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_trace263) 
                    stream_NEWLINE.add(NEWLINE30)





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
                # 39:9: -> ^( TREE_TRACE ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:39:13: ^( TREE_TRACE ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TRACE, "TREE_TRACE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:39:30: ( proc )*
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
    # grammar/ShyRecognizerFrontend.g:42:1: stateless : STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS31 = None
        ID32 = None
        NEWLINE33 = None
        INDENT34 = None
        NEWLINE35 = None
        DEDENT37 = None
        NEWLINE38 = None
        proc36 = None


        STATELESS31_tree = None
        ID32_tree = None
        NEWLINE33_tree = None
        INDENT34_tree = None
        NEWLINE35_tree = None
        DEDENT37_tree = None
        NEWLINE38_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:43:5: ( STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:43:9: STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                STATELESS31 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless309) 
                stream_STATELESS.add(STATELESS31)


                ID32 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless311) 
                stream_ID.add(ID32)


                NEWLINE33 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless313) 
                stream_NEWLINE.add(NEWLINE33)


                # grammar/ShyRecognizerFrontend.g:43:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == INDENT) :
                    alt7 = 1
                if alt7 == 1:
                    # grammar/ShyRecognizerFrontend.g:43:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT34 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless317) 
                    stream_INDENT.add(INDENT34)


                    NEWLINE35 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless319) 
                    stream_NEWLINE.add(NEWLINE35)


                    # grammar/ShyRecognizerFrontend.g:43:47: ( proc )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == PROC) :
                            alt6 = 1


                        if alt6 == 1:
                            # grammar/ShyRecognizerFrontend.g:43:47: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless321)
                            proc36 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc36.tree)



                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1


                    DEDENT37 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless325) 
                    stream_DEDENT.add(DEDENT37)


                    NEWLINE38 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless327) 
                    stream_NEWLINE.add(NEWLINE38)





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
                # 44:9: -> ^( TREE_STATELESS ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:44:13: ^( TREE_STATELESS ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:44:34: ( proc )*
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
    # grammar/ShyRecognizerFrontend.g:47:1: request : ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID statement -> ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) );
    def request(self, ):
        retval = self.request_return()
        retval.start = self.input.LT(1)


        root_0 = None

        REQUEST39 = None
        ID40 = None
        NEWLINE41 = None
        REQUEST42 = None
        ID43 = None
        REQUEST45 = None
        ID46 = None
        NEWLINE47 = None
        INDENT48 = None
        NEWLINE49 = None
        DEDENT51 = None
        NEWLINE52 = None
        REQUEST53 = None
        ID54 = None
        NEWLINE55 = None
        INDENT56 = None
        NEWLINE57 = None
        DEDENT60 = None
        NEWLINE61 = None
        statement44 = None

        statements50 = None

        local_vars58 = None

        local_ops59 = None


        REQUEST39_tree = None
        ID40_tree = None
        NEWLINE41_tree = None
        REQUEST42_tree = None
        ID43_tree = None
        REQUEST45_tree = None
        ID46_tree = None
        NEWLINE47_tree = None
        INDENT48_tree = None
        NEWLINE49_tree = None
        DEDENT51_tree = None
        NEWLINE52_tree = None
        REQUEST53_tree = None
        ID54_tree = None
        NEWLINE55_tree = None
        INDENT56_tree = None
        NEWLINE57_tree = None
        DEDENT60_tree = None
        NEWLINE61_tree = None
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
                # grammar/ShyRecognizerFrontend.g:48:5: ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID statement -> ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) )
                alt10 = 4
                LA10_0 = self.input.LA(1)

                if (LA10_0 == REQUEST) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == ID) :
                        LA10_2 = self.input.LA(3)

                        if (LA10_2 == NEWLINE) :
                            LA10_3 = self.input.LA(4)

                            if (LA10_3 == INDENT) :
                                LA10_5 = self.input.LA(5)

                                if (LA10_5 == NEWLINE) :
                                    LA10_7 = self.input.LA(6)

                                    if ((EXPRESSION <= LA10_7 <= IF) or LA10_7 == MINUS or LA10_7 == NUMBER or LA10_7 == SEND or LA10_7 == STRING or LA10_7 == WHILE or LA10_7 == WITH) :
                                        alt10 = 3
                                    elif (LA10_7 == DEDENT or LA10_7 == OPS or LA10_7 == VARS) :
                                        alt10 = 4
                                    else:
                                        nvae = NoViableAltException("", 10, 7, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 10, 5, self.input)

                                    raise nvae


                            elif (LA10_3 == DEDENT or LA10_3 == MODULE_QUEUE or (PROC <= LA10_3 <= RECEIVE) or LA10_3 == REQUEST) :
                                alt10 = 1
                            else:
                                nvae = NoViableAltException("", 10, 3, self.input)

                                raise nvae


                        elif ((EXPRESSION <= LA10_2 <= IF) or LA10_2 == MINUS or LA10_2 == NUMBER or LA10_2 == SEND or LA10_2 == STRING or LA10_2 == WHILE or LA10_2 == WITH) :
                            alt10 = 2
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
                    # grammar/ShyRecognizerFrontend.g:48:9: REQUEST ID NEWLINE
                    pass 
                    REQUEST39 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request373) 
                    stream_REQUEST.add(REQUEST39)


                    ID40 = self.match(self.input, ID, self.FOLLOW_ID_in_request375) 
                    stream_ID.add(ID40)


                    NEWLINE41 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request377) 
                    stream_NEWLINE.add(NEWLINE41)


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
                    # 49:9: -> ^( TREE_REQUEST ID )
                    # grammar/ShyRecognizerFrontend.g:49:13: ^( TREE_REQUEST ID )
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
                    # grammar/ShyRecognizerFrontend.g:50:9: REQUEST ID statement
                    pass 
                    REQUEST42 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request406) 
                    stream_REQUEST.add(REQUEST42)


                    ID43 = self.match(self.input, ID, self.FOLLOW_ID_in_request408) 
                    stream_ID.add(ID43)


                    self._state.following.append(self.FOLLOW_statement_in_request410)
                    statement44 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement44.tree)


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
                    # 51:9: -> ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) )
                    # grammar/ShyRecognizerFrontend.g:51:13: ^( TREE_REQUEST ID ^( TREE_STATEMENTS statement ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:51:32: ^( TREE_STATEMENTS statement )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                    , root_2)

                    self._adaptor.addChild(root_2, stream_statement.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt10 == 3:
                    # grammar/ShyRecognizerFrontend.g:52:9: REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    REQUEST45 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request447) 
                    stream_REQUEST.add(REQUEST45)


                    ID46 = self.match(self.input, ID, self.FOLLOW_ID_in_request449) 
                    stream_ID.add(ID46)


                    NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request451) 
                    stream_NEWLINE.add(NEWLINE47)


                    INDENT48 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request453) 
                    stream_INDENT.add(INDENT48)


                    NEWLINE49 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request455) 
                    stream_NEWLINE.add(NEWLINE49)


                    self._state.following.append(self.FOLLOW_statements_in_request457)
                    statements50 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements50.tree)


                    DEDENT51 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request459) 
                    stream_DEDENT.add(DEDENT51)


                    NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request461) 
                    stream_NEWLINE.add(NEWLINE52)


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
                    # 53:9: -> ^( TREE_REQUEST ID statements )
                    # grammar/ShyRecognizerFrontend.g:53:13: ^( TREE_REQUEST ID statements )
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




                elif alt10 == 4:
                    # grammar/ShyRecognizerFrontend.g:54:9: REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    REQUEST53 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request492) 
                    stream_REQUEST.add(REQUEST53)


                    ID54 = self.match(self.input, ID, self.FOLLOW_ID_in_request494) 
                    stream_ID.add(ID54)


                    NEWLINE55 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request496) 
                    stream_NEWLINE.add(NEWLINE55)


                    INDENT56 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request498) 
                    stream_INDENT.add(INDENT56)


                    NEWLINE57 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request500) 
                    stream_NEWLINE.add(NEWLINE57)


                    # grammar/ShyRecognizerFrontend.g:55:13: ( local_vars )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == VARS) :
                        alt8 = 1
                    if alt8 == 1:
                        # grammar/ShyRecognizerFrontend.g:55:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_request514)
                        local_vars58 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars58.tree)





                    # grammar/ShyRecognizerFrontend.g:55:26: ( local_ops )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OPS) :
                        alt9 = 1
                    if alt9 == 1:
                        # grammar/ShyRecognizerFrontend.g:55:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_request518)
                        local_ops59 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops59.tree)





                    DEDENT60 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request530) 
                    stream_DEDENT.add(DEDENT60)


                    NEWLINE61 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request532) 
                    stream_NEWLINE.add(NEWLINE61)


                    # AST Rewrite
                    # elements: local_vars, local_ops, ID
                    # token labels: 
                    # rule labels: retval
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
    # grammar/ShyRecognizerFrontend.g:60:1: receive : ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID statement -> ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) );
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECEIVE62 = None
        ID63 = None
        NEWLINE64 = None
        RECEIVE65 = None
        ID66 = None
        RECEIVE68 = None
        ID69 = None
        NEWLINE70 = None
        INDENT71 = None
        NEWLINE72 = None
        DEDENT74 = None
        NEWLINE75 = None
        RECEIVE76 = None
        ID77 = None
        NEWLINE78 = None
        INDENT79 = None
        NEWLINE80 = None
        DEDENT83 = None
        NEWLINE84 = None
        statement67 = None

        statements73 = None

        local_vars81 = None

        local_ops82 = None


        RECEIVE62_tree = None
        ID63_tree = None
        NEWLINE64_tree = None
        RECEIVE65_tree = None
        ID66_tree = None
        RECEIVE68_tree = None
        ID69_tree = None
        NEWLINE70_tree = None
        INDENT71_tree = None
        NEWLINE72_tree = None
        DEDENT74_tree = None
        NEWLINE75_tree = None
        RECEIVE76_tree = None
        ID77_tree = None
        NEWLINE78_tree = None
        INDENT79_tree = None
        NEWLINE80_tree = None
        DEDENT83_tree = None
        NEWLINE84_tree = None
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
                # grammar/ShyRecognizerFrontend.g:61:5: ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID statement -> ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) )
                alt13 = 4
                LA13_0 = self.input.LA(1)

                if (LA13_0 == RECEIVE) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == ID) :
                        LA13_2 = self.input.LA(3)

                        if (LA13_2 == NEWLINE) :
                            LA13_3 = self.input.LA(4)

                            if (LA13_3 == INDENT) :
                                LA13_5 = self.input.LA(5)

                                if (LA13_5 == NEWLINE) :
                                    LA13_7 = self.input.LA(6)

                                    if ((EXPRESSION <= LA13_7 <= IF) or LA13_7 == MINUS or LA13_7 == NUMBER or LA13_7 == SEND or LA13_7 == STRING or LA13_7 == WHILE or LA13_7 == WITH) :
                                        alt13 = 3
                                    elif (LA13_7 == DEDENT or LA13_7 == OPS or LA13_7 == VARS) :
                                        alt13 = 4
                                    else:
                                        nvae = NoViableAltException("", 13, 7, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 13, 5, self.input)

                                    raise nvae


                            elif (LA13_3 == DEDENT or LA13_3 == MODULE_QUEUE or (PROC <= LA13_3 <= RECEIVE) or LA13_3 == REQUEST) :
                                alt13 = 1
                            else:
                                nvae = NoViableAltException("", 13, 3, self.input)

                                raise nvae


                        elif ((EXPRESSION <= LA13_2 <= IF) or LA13_2 == MINUS or LA13_2 == NUMBER or LA13_2 == SEND or LA13_2 == STRING or LA13_2 == WHILE or LA13_2 == WITH) :
                            alt13 = 2
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
                    RECEIVE62 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive578) 
                    stream_RECEIVE.add(RECEIVE62)


                    ID63 = self.match(self.input, ID, self.FOLLOW_ID_in_receive580) 
                    stream_ID.add(ID63)


                    NEWLINE64 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive582) 
                    stream_NEWLINE.add(NEWLINE64)


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
                    # grammar/ShyRecognizerFrontend.g:63:9: RECEIVE ID statement
                    pass 
                    RECEIVE65 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive611) 
                    stream_RECEIVE.add(RECEIVE65)


                    ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_receive613) 
                    stream_ID.add(ID66)


                    self._state.following.append(self.FOLLOW_statement_in_receive615)
                    statement67 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement67.tree)


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
                    # 64:9: -> ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) )
                    # grammar/ShyRecognizerFrontend.g:64:13: ^( TREE_RECEIVE ID ^( TREE_STATEMENTS statement ) )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:64:32: ^( TREE_STATEMENTS statement )
                    root_2 = self._adaptor.nil()
                    root_2 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                    , root_2)

                    self._adaptor.addChild(root_2, stream_statement.nextTree())

                    self._adaptor.addChild(root_1, root_2)

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 3:
                    # grammar/ShyRecognizerFrontend.g:65:9: RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    RECEIVE68 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive652) 
                    stream_RECEIVE.add(RECEIVE68)


                    ID69 = self.match(self.input, ID, self.FOLLOW_ID_in_receive654) 
                    stream_ID.add(ID69)


                    NEWLINE70 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive656) 
                    stream_NEWLINE.add(NEWLINE70)


                    INDENT71 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive658) 
                    stream_INDENT.add(INDENT71)


                    NEWLINE72 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive660) 
                    stream_NEWLINE.add(NEWLINE72)


                    self._state.following.append(self.FOLLOW_statements_in_receive662)
                    statements73 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements73.tree)


                    DEDENT74 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive664) 
                    stream_DEDENT.add(DEDENT74)


                    NEWLINE75 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive666) 
                    stream_NEWLINE.add(NEWLINE75)


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
                    # 66:9: -> ^( TREE_RECEIVE ID statements )
                    # grammar/ShyRecognizerFrontend.g:66:13: ^( TREE_RECEIVE ID statements )
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




                elif alt13 == 4:
                    # grammar/ShyRecognizerFrontend.g:67:9: RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    RECEIVE76 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive697) 
                    stream_RECEIVE.add(RECEIVE76)


                    ID77 = self.match(self.input, ID, self.FOLLOW_ID_in_receive699) 
                    stream_ID.add(ID77)


                    NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive701) 
                    stream_NEWLINE.add(NEWLINE78)


                    INDENT79 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive703) 
                    stream_INDENT.add(INDENT79)


                    NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive705) 
                    stream_NEWLINE.add(NEWLINE80)


                    # grammar/ShyRecognizerFrontend.g:68:13: ( local_vars )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == VARS) :
                        alt11 = 1
                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:68:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_receive719)
                        local_vars81 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars81.tree)





                    # grammar/ShyRecognizerFrontend.g:68:26: ( local_ops )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == OPS) :
                        alt12 = 1
                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:68:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_receive723)
                        local_ops82 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops82.tree)





                    DEDENT83 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive735) 
                    stream_DEDENT.add(DEDENT83)


                    NEWLINE84 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive737) 
                    stream_NEWLINE.add(NEWLINE84)


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
                    # 70:9: -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:70:13: ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:70:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:70:45: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:73:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC85 = None
        ID86 = None
        NEWLINE87 = None
        PROC88 = None
        ID89 = None
        NEWLINE90 = None
        INDENT91 = None
        NEWLINE92 = None
        DEDENT94 = None
        NEWLINE95 = None
        PROC96 = None
        ID97 = None
        NEWLINE98 = None
        INDENT99 = None
        NEWLINE100 = None
        DEDENT104 = None
        NEWLINE105 = None
        statements93 = None

        proc_args101 = None

        local_vars102 = None

        local_ops103 = None


        PROC85_tree = None
        ID86_tree = None
        NEWLINE87_tree = None
        PROC88_tree = None
        ID89_tree = None
        NEWLINE90_tree = None
        INDENT91_tree = None
        NEWLINE92_tree = None
        DEDENT94_tree = None
        NEWLINE95_tree = None
        PROC96_tree = None
        ID97_tree = None
        NEWLINE98_tree = None
        INDENT99_tree = None
        NEWLINE100_tree = None
        DEDENT104_tree = None
        NEWLINE105_tree = None
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
                # grammar/ShyRecognizerFrontend.g:74:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_PROC ID statements ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) )
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

                                    if ((EXPRESSION <= LA17_6 <= IF) or LA17_6 == MINUS or LA17_6 == NUMBER or LA17_6 == SEND or LA17_6 == STRING or LA17_6 == WHILE or LA17_6 == WITH) :
                                        alt17 = 2
                                    elif (LA17_6 == ARGS or LA17_6 == DEDENT or LA17_6 == OPS or LA17_6 == VARS) :
                                        alt17 = 3
                                    else:
                                        nvae = NoViableAltException("", 17, 6, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 17, 4, self.input)

                                    raise nvae


                            elif (LA17_3 == DEDENT or LA17_3 == MODULE_QUEUE or (PROC <= LA17_3 <= RECEIVE) or LA17_3 == REQUEST) :
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
                    # grammar/ShyRecognizerFrontend.g:74:9: PROC ID NEWLINE
                    pass 
                    PROC85 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc783) 
                    stream_PROC.add(PROC85)


                    ID86 = self.match(self.input, ID, self.FOLLOW_ID_in_proc785) 
                    stream_ID.add(ID86)


                    NEWLINE87 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc787) 
                    stream_NEWLINE.add(NEWLINE87)


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
                    # 75:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:75:13: ^( TREE_PROC ID )
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
                    # grammar/ShyRecognizerFrontend.g:76:9: PROC ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    PROC88 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc816) 
                    stream_PROC.add(PROC88)


                    ID89 = self.match(self.input, ID, self.FOLLOW_ID_in_proc818) 
                    stream_ID.add(ID89)


                    NEWLINE90 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc820) 
                    stream_NEWLINE.add(NEWLINE90)


                    INDENT91 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc822) 
                    stream_INDENT.add(INDENT91)


                    NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc824) 
                    stream_NEWLINE.add(NEWLINE92)


                    self._state.following.append(self.FOLLOW_statements_in_proc826)
                    statements93 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements93.tree)


                    DEDENT94 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc828) 
                    stream_DEDENT.add(DEDENT94)


                    NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc830) 
                    stream_NEWLINE.add(NEWLINE95)


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
                    # 77:9: -> ^( TREE_PROC ID statements )
                    # grammar/ShyRecognizerFrontend.g:77:13: ^( TREE_PROC ID statements )
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
                    # grammar/ShyRecognizerFrontend.g:78:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    PROC96 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc861) 
                    stream_PROC.add(PROC96)


                    ID97 = self.match(self.input, ID, self.FOLLOW_ID_in_proc863) 
                    stream_ID.add(ID97)


                    NEWLINE98 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc865) 
                    stream_NEWLINE.add(NEWLINE98)


                    INDENT99 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc867) 
                    stream_INDENT.add(INDENT99)


                    NEWLINE100 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc869) 
                    stream_NEWLINE.add(NEWLINE100)


                    # grammar/ShyRecognizerFrontend.g:79:13: ( proc_args )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == ARGS) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:79:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc883)
                        proc_args101 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args101.tree)





                    # grammar/ShyRecognizerFrontend.g:79:25: ( local_vars )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == VARS) :
                        alt15 = 1
                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:79:25: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_proc887)
                        local_vars102 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars102.tree)





                    # grammar/ShyRecognizerFrontend.g:79:38: ( local_ops )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == OPS) :
                        alt16 = 1
                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:79:38: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_proc891)
                        local_ops103 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops103.tree)





                    DEDENT104 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc903) 
                    stream_DEDENT.add(DEDENT104)


                    NEWLINE105 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc905) 
                    stream_NEWLINE.add(NEWLINE105)


                    # AST Rewrite
                    # elements: ID, local_vars, local_ops, proc_args
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 81:9: -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:81:13: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:81:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:81:41: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:81:54: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:84:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS106 = None
        attrs_hints107 = None


        ARGS106_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:85:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:85:9: ARGS attrs_hints
                pass 
                ARGS106 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args955) 
                stream_ARGS.add(ARGS106)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args957)
                attrs_hints107 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints107.tree)


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
                # 85:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:85:29: ^( TREE_PROC_ARGS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:88:1: local_vars : VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        retval = self.local_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS108 = None
        attrs_hints109 = None


        VARS108_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:89:5: ( VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:89:9: VARS attrs_hints
                pass 
                VARS108 = self.match(self.input, VARS, self.FOLLOW_VARS_in_local_vars986) 
                stream_VARS.add(VARS108)


                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars988)
                attrs_hints109 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints109.tree)


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
                # 89:26: -> ^( TREE_LOCAL_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:89:29: ^( TREE_LOCAL_VARS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:92:1: local_ops : ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements | OPS statement -> ^( TREE_STATEMENTS statement ) );
    def local_ops(self, ):
        retval = self.local_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS110 = None
        NEWLINE111 = None
        INDENT112 = None
        NEWLINE113 = None
        DEDENT115 = None
        NEWLINE116 = None
        OPS117 = None
        statements114 = None

        statement118 = None


        OPS110_tree = None
        NEWLINE111_tree = None
        INDENT112_tree = None
        NEWLINE113_tree = None
        DEDENT115_tree = None
        NEWLINE116_tree = None
        OPS117_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:93:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements | OPS statement -> ^( TREE_STATEMENTS statement ) )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == OPS) :
                    LA18_1 = self.input.LA(2)

                    if (LA18_1 == NEWLINE) :
                        alt18 = 1
                    elif ((EXPRESSION <= LA18_1 <= IF) or LA18_1 == MINUS or LA18_1 == NUMBER or LA18_1 == SEND or LA18_1 == STRING or LA18_1 == WHILE or LA18_1 == WITH) :
                        alt18 = 2
                    else:
                        nvae = NoViableAltException("", 18, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:93:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    OPS110 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops1017) 
                    stream_OPS.add(OPS110)


                    NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1019) 
                    stream_NEWLINE.add(NEWLINE111)


                    INDENT112 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_local_ops1021) 
                    stream_INDENT.add(INDENT112)


                    NEWLINE113 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1023) 
                    stream_NEWLINE.add(NEWLINE113)


                    self._state.following.append(self.FOLLOW_statements_in_local_ops1025)
                    statements114 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements114.tree)


                    DEDENT115 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_local_ops1027) 
                    stream_DEDENT.add(DEDENT115)


                    NEWLINE116 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops1029) 
                    stream_NEWLINE.add(NEWLINE116)


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
                    # 94:9: -> statements
                    self._adaptor.addChild(root_0, stream_statements.nextTree())




                    retval.tree = root_0




                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:95:9: OPS statement
                    pass 
                    OPS117 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops1051) 
                    stream_OPS.add(OPS117)


                    self._state.following.append(self.FOLLOW_statement_in_local_ops1053)
                    statement118 = self.statement()

                    self._state.following.pop()
                    stream_statement.add(statement118.tree)


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
                    # 96:9: -> ^( TREE_STATEMENTS statement )
                    # grammar/ShyRecognizerFrontend.g:96:13: ^( TREE_STATEMENTS statement )
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
    # grammar/ShyRecognizerFrontend.g:99:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_send | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE120 = None
        statement_call_single_line119 = None

        statement_call_multi_line121 = None

        statement_send122 = None

        statement_if123 = None

        statement_assign124 = None

        statement_while125 = None

        statement_with126 = None


        NEWLINE120_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:100:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_send | statement_if | statement_assign | statement_while | statement_with )
                alt19 = 7
                alt19 = self.dfa19.predict(self.input)
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:100:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement1091)
                    statement_call_single_line119 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line119.tree)


                    NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement1093) 
                    stream_NEWLINE.add(NEWLINE120)


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
                    # 101:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt19 == 2:
                    # grammar/ShyRecognizerFrontend.g:102:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement1119)
                    statement_call_multi_line121 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line121.tree)



                elif alt19 == 3:
                    # grammar/ShyRecognizerFrontend.g:103:9: statement_send
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_send_in_statement1129)
                    statement_send122 = self.statement_send()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_send122.tree)



                elif alt19 == 4:
                    # grammar/ShyRecognizerFrontend.g:104:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement1139)
                    statement_if123 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if123.tree)



                elif alt19 == 5:
                    # grammar/ShyRecognizerFrontend.g:105:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1149)
                    statement_assign124 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign124.tree)



                elif alt19 == 6:
                    # grammar/ShyRecognizerFrontend.g:106:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement1159)
                    statement_while125 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while125.tree)



                elif alt19 == 7:
                    # grammar/ShyRecognizerFrontend.g:107:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement1169)
                    statement_with126 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with126.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:110:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement127 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:111:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:111:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:111:9: ( statement )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA20_0 <= IF) or LA20_0 == MINUS or LA20_0 == NUMBER or LA20_0 == SEND or LA20_0 == STRING or LA20_0 == WHILE or LA20_0 == WITH) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerFrontend.g:111:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1188)
                        statement127 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement127.tree)



                    else:
                        if cnt20 >= 1:
                            break #loop20

                        eee = EarlyExitException(20, self.input)
                        raise eee

                    cnt20 += 1


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
                # 112:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:112:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:112:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:115:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH128 = None
        ID129 = None
        NEWLINE130 = None
        INDENT131 = None
        NEWLINE132 = None
        DEDENT134 = None
        NEWLINE135 = None
        statements133 = None


        WITH128_tree = None
        ID129_tree = None
        NEWLINE130_tree = None
        INDENT131_tree = None
        NEWLINE132_tree = None
        DEDENT134_tree = None
        NEWLINE135_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:116:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:116:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH128 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1230) 
                stream_WITH.add(WITH128)


                ID129 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1232) 
                stream_ID.add(ID129)


                NEWLINE130 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1234) 
                stream_NEWLINE.add(NEWLINE130)


                INDENT131 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1244) 
                stream_INDENT.add(INDENT131)


                NEWLINE132 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1246) 
                stream_NEWLINE.add(NEWLINE132)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1248)
                statements133 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements133.tree)


                DEDENT134 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1250) 
                stream_DEDENT.add(DEDENT134)


                NEWLINE135 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1252) 
                stream_NEWLINE.add(NEWLINE135)


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
                # 118:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:118:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:121:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID136 = None
        ARROW_LEFT137 = None
        NEWLINE139 = None
        ID140 = None
        ARROW_LEFT141 = None
        NEWLINE142 = None
        INDENT143 = None
        NEWLINE144 = None
        NEWLINE146 = None
        DEDENT147 = None
        NEWLINE148 = None
        ARROW_RIGHT150 = None
        ID151 = None
        NEWLINE152 = None
        ARROW_RIGHT154 = None
        NEWLINE155 = None
        INDENT156 = None
        NEWLINE157 = None
        ID158 = None
        NEWLINE159 = None
        DEDENT160 = None
        NEWLINE161 = None
        arbitrary_value138 = None

        arbitrary_value145 = None

        arbitrary_value149 = None

        arbitrary_value153 = None


        ID136_tree = None
        ARROW_LEFT137_tree = None
        NEWLINE139_tree = None
        ID140_tree = None
        ARROW_LEFT141_tree = None
        NEWLINE142_tree = None
        INDENT143_tree = None
        NEWLINE144_tree = None
        NEWLINE146_tree = None
        DEDENT147_tree = None
        NEWLINE148_tree = None
        ARROW_RIGHT150_tree = None
        ID151_tree = None
        NEWLINE152_tree = None
        ARROW_RIGHT154_tree = None
        NEWLINE155_tree = None
        INDENT156_tree = None
        NEWLINE157_tree = None
        ID158_tree = None
        NEWLINE159_tree = None
        DEDENT160_tree = None
        NEWLINE161_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:122:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt31 = 4
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:122:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:122:9: ( ID )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == ID) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:122:9: ID
                            pass 
                            ID136 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1292) 
                            stream_ID.add(ID136)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    ARROW_LEFT137 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1296) 
                    stream_ARROW_LEFT.add(ARROW_LEFT137)


                    # grammar/ShyRecognizerFrontend.g:122:25: ( arbitrary_value )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER or LA22_0 == STRING) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:122:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1298)
                            arbitrary_value138 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value138.tree)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    NEWLINE139 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1302) 
                    stream_NEWLINE.add(NEWLINE139)


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




                elif alt31 == 2:
                    # grammar/ShyRecognizerFrontend.g:125:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:125:9: ( ID )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == ID) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:125:9: ID
                            pass 
                            ID140 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1355) 
                            stream_ID.add(ID140)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    ARROW_LEFT141 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1359) 
                    stream_ARROW_LEFT.add(ARROW_LEFT141)


                    NEWLINE142 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1361) 
                    stream_NEWLINE.add(NEWLINE142)


                    INDENT143 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1363) 
                    stream_INDENT.add(INDENT143)


                    NEWLINE144 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1365) 
                    stream_NEWLINE.add(NEWLINE144)


                    # grammar/ShyRecognizerFrontend.g:126:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER or LA25_0 == STRING) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:126:11: ( arbitrary_value )+
                            cnt24 = 0
                            while True: #loop24
                                alt24 = 2
                                LA24_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER or LA24_0 == STRING) :
                                    alt24 = 1


                                if alt24 == 1:
                                    # grammar/ShyRecognizerFrontend.g:126:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1377)
                                    arbitrary_value145 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value145.tree)



                                else:
                                    if cnt24 >= 1:
                                        break #loop24

                                    eee = EarlyExitException(24, self.input)
                                    raise eee

                                cnt24 += 1


                            NEWLINE146 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1381) 
                            stream_NEWLINE.add(NEWLINE146)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    DEDENT147 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1387) 
                    stream_DEDENT.add(DEDENT147)


                    NEWLINE148 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1389) 
                    stream_NEWLINE.add(NEWLINE148)


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




                elif alt31 == 3:
                    # grammar/ShyRecognizerFrontend.g:129:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:129:9: ( arbitrary_value )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA26_0 <= ID) or LA26_0 == MINUS or LA26_0 == NUMBER or LA26_0 == STRING) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:129:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1442)
                            arbitrary_value149 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value149.tree)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


                    ARROW_RIGHT150 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1446) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT150)


                    # grammar/ShyRecognizerFrontend.g:129:39: ( ID )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == ID) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:129:39: ID
                            pass 
                            ID151 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1448) 
                            stream_ID.add(ID151)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    NEWLINE152 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1452) 
                    stream_NEWLINE.add(NEWLINE152)


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
                    # 130:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:130:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:130:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:131:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt31 == 4:
                    # grammar/ShyRecognizerFrontend.g:132:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:132:9: ( arbitrary_value )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA28_0 <= ID) or LA28_0 == MINUS or LA28_0 == NUMBER or LA28_0 == STRING) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:132:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1505)
                            arbitrary_value153 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value153.tree)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    ARROW_RIGHT154 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1509) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT154)


                    NEWLINE155 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1511) 
                    stream_NEWLINE.add(NEWLINE155)


                    INDENT156 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1513) 
                    stream_INDENT.add(INDENT156)


                    NEWLINE157 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1515) 
                    stream_NEWLINE.add(NEWLINE157)


                    # grammar/ShyRecognizerFrontend.g:133:9: ( ( ID )+ NEWLINE )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == ID) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:133:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:133:11: ( ID )+
                            cnt29 = 0
                            while True: #loop29
                                alt29 = 2
                                LA29_0 = self.input.LA(1)

                                if (LA29_0 == ID) :
                                    alt29 = 1


                                if alt29 == 1:
                                    # grammar/ShyRecognizerFrontend.g:133:11: ID
                                    pass 
                                    ID158 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1527) 
                                    stream_ID.add(ID158)



                                else:
                                    if cnt29 >= 1:
                                        break #loop29

                                    eee = EarlyExitException(29, self.input)
                                    raise eee

                                cnt29 += 1


                            NEWLINE159 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1531) 
                            stream_NEWLINE.add(NEWLINE159)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


                    DEDENT160 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1537) 
                    stream_DEDENT.add(DEDENT160)


                    NEWLINE161 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1539) 
                    stream_NEWLINE.add(NEWLINE161)


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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:138:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE162 = None
        NEWLINE164 = None
        DO165 = None
        NEWLINE166 = None
        INDENT167 = None
        NEWLINE168 = None
        DEDENT170 = None
        NEWLINE171 = None
        condition163 = None

        statements169 = None


        WHILE162_tree = None
        NEWLINE164_tree = None
        DO165_tree = None
        NEWLINE166_tree = None
        INDENT167_tree = None
        NEWLINE168_tree = None
        DEDENT170_tree = None
        NEWLINE171_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:139:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:139:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE162 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1601) 
                stream_WHILE.add(WHILE162)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1603)
                condition163 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition163.tree)


                # grammar/ShyRecognizerFrontend.g:139:25: ( NEWLINE )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == NEWLINE) :
                    alt32 = 1
                if alt32 == 1:
                    # grammar/ShyRecognizerFrontend.g:139:25: NEWLINE
                    pass 
                    NEWLINE164 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1605) 
                    stream_NEWLINE.add(NEWLINE164)





                DO165 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1609) 
                stream_DO.add(DO165)


                NEWLINE166 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1611) 
                stream_NEWLINE.add(NEWLINE166)


                INDENT167 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1625) 
                stream_INDENT.add(INDENT167)


                NEWLINE168 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1627) 
                stream_NEWLINE.add(NEWLINE168)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1629)
                statements169 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements169.tree)


                DEDENT170 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1631) 
                stream_DEDENT.add(DEDENT170)


                NEWLINE171 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1633) 
                stream_NEWLINE.add(NEWLINE171)


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
                # 141:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:141:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:144:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head172 = None

        statement_elif173 = None

        statement_else174 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:145:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:145:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1673)
                statement_if_head172 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head172.tree)


                # grammar/ShyRecognizerFrontend.g:146:9: ( statement_elif )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == ELIF) :
                        alt33 = 1


                    if alt33 == 1:
                        # grammar/ShyRecognizerFrontend.g:146:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1683)
                        statement_elif173 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif173.tree)



                    else:
                        break #loop33


                # grammar/ShyRecognizerFrontend.g:147:9: ( statement_else )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == ELSE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:147:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1695)
                    statement_else174 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else174.tree)





                # AST Rewrite
                # elements: statement_elif, statement_else, statement_if_head
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 148:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:148:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:150:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:151:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:155:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF175 = None
        statement_elif_body176 = None


        IF175_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:156:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:156:9: IF statement_elif_body
                pass 
                IF175 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1803) 
                stream_IF.add(IF175)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1805)
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
                # 157:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:160:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF177 = None
        statement_elif_body178 = None


        ELIF177_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:161:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:161:9: ELIF statement_elif_body
                pass 
                ELIF177 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1837) 
                stream_ELIF.add(ELIF177)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1839)
                statement_elif_body178 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body178.tree)


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
                # 162:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:165:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE180 = None
        DO181 = None
        NEWLINE182 = None
        INDENT183 = None
        NEWLINE184 = None
        DEDENT186 = None
        NEWLINE187 = None
        condition179 = None

        statements185 = None


        NEWLINE180_tree = None
        DO181_tree = None
        NEWLINE182_tree = None
        INDENT183_tree = None
        NEWLINE184_tree = None
        DEDENT186_tree = None
        NEWLINE187_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:166:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:166:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1871)
                condition179 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition179.tree)


                # grammar/ShyRecognizerFrontend.g:166:19: ( NEWLINE )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == NEWLINE) :
                    alt35 = 1
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:166:19: NEWLINE
                    pass 
                    NEWLINE180 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1873) 
                    stream_NEWLINE.add(NEWLINE180)





                DO181 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1877) 
                stream_DO.add(DO181)


                NEWLINE182 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1879) 
                stream_NEWLINE.add(NEWLINE182)


                INDENT183 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1893) 
                stream_INDENT.add(INDENT183)


                NEWLINE184 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1895) 
                stream_NEWLINE.add(NEWLINE184)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1897)
                statements185 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements185.tree)


                DEDENT186 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1899) 
                stream_DEDENT.add(DEDENT186)


                NEWLINE187 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1901) 
                stream_NEWLINE.add(NEWLINE187)


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
                # 168:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:168:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:171:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE188 = None
        NEWLINE189 = None
        INDENT190 = None
        NEWLINE191 = None
        DEDENT193 = None
        NEWLINE194 = None
        statements192 = None


        ELSE188_tree = None
        NEWLINE189_tree = None
        INDENT190_tree = None
        NEWLINE191_tree = None
        DEDENT193_tree = None
        NEWLINE194_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:172:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:172:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE188 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1941) 
                stream_ELSE.add(ELSE188)


                NEWLINE189 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1943) 
                stream_NEWLINE.add(NEWLINE189)


                INDENT190 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1957) 
                stream_INDENT.add(INDENT190)


                NEWLINE191 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1959) 
                stream_NEWLINE.add(NEWLINE191)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1961)
                statements192 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements192.tree)


                DEDENT193 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1963) 
                stream_DEDENT.add(DEDENT193)


                NEWLINE194 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1965) 
                stream_NEWLINE.add(NEWLINE194)


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
                # 174:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:174:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:177:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY196 = None
        ALL198 = None
        condition_call195 = None

        condition_calls197 = None

        condition_calls199 = None


        ANY196_tree = None
        ALL198_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:178:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt36 = 3
                LA36 = self.input.LA(1)
                if LA36 == ID:
                    alt36 = 1
                elif LA36 == ANY:
                    alt36 = 2
                elif LA36 == ALL:
                    alt36 = 3
                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:178:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition2003)
                    condition_call195 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call195.tree)


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
                    # 179:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:179:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt36 == 2:
                    # grammar/ShyRecognizerFrontend.g:180:9: ANY condition_calls
                    pass 
                    ANY196 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition2032) 
                    stream_ANY.add(ANY196)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2034)
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
                    # 181:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:181:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt36 == 3:
                    # grammar/ShyRecognizerFrontend.g:182:9: ALL condition_calls
                    pass 
                    ALL198 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition2063) 
                    stream_ALL.add(ALL198)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2065)
                    condition_calls199 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls199.tree)


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
                    # 183:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:183:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:186:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE201 = None
        INDENT202 = None
        NEWLINE203 = None
        DEDENT205 = None
        NEWLINE206 = None
        condition_call200 = None

        condition_call_line204 = None


        NEWLINE201_tree = None
        INDENT202_tree = None
        NEWLINE203_tree = None
        DEDENT205_tree = None
        NEWLINE206_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:187:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == ID) :
                    alt38 = 1
                elif (LA38_0 == NEWLINE) :
                    alt38 = 2
                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:187:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls2103)
                    condition_call200 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call200.tree)



                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:188:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE201 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2113) 
                    stream_NEWLINE.add(NEWLINE201)


                    INDENT202 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls2115) 
                    stream_INDENT.add(INDENT202)


                    NEWLINE203 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2117) 
                    stream_NEWLINE.add(NEWLINE203)


                    # grammar/ShyRecognizerFrontend.g:188:32: ( condition_call_line )+
                    cnt37 = 0
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == ID) :
                            alt37 = 1


                        if alt37 == 1:
                            # grammar/ShyRecognizerFrontend.g:188:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls2119)
                            condition_call_line204 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line204.tree)



                        else:
                            if cnt37 >= 1:
                                break #loop37

                            eee = EarlyExitException(37, self.input)
                            raise eee

                        cnt37 += 1


                    DEDENT205 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls2123) 
                    stream_DEDENT.add(DEDENT205)


                    NEWLINE206 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2125) 
                    stream_NEWLINE.add(NEWLINE206)


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
                    # 189:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:189:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:192:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line207 = None

        statement_call_multi_line208 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:193:5: ( statement_call_single_line | statement_call_multi_line )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:193:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call2159)
                    statement_call_single_line207 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line207.tree)



                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:194:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call2169)
                    statement_call_multi_line208 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line208.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:197:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE210 = None
        statement_call_single_line209 = None

        statement_call_multi_line211 = None


        NEWLINE210_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:198:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt40 = 2
                alt40 = self.dfa40.predict(self.input)
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:198:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line2188)
                    statement_call_single_line209 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line209.tree)


                    NEWLINE210 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line2190) 
                    stream_NEWLINE.add(NEWLINE210)


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
                    # 199:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt40 == 2:
                    # grammar/ShyRecognizerFrontend.g:200:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2216)
                    statement_call_multi_line211 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line211.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:203:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID212 = None
        statement_call_args213 = None


        ID212_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:204:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:204:9: ID ( statement_call_args )?
                pass 
                ID212 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2235) 
                stream_ID.add(ID212)


                # grammar/ShyRecognizerFrontend.g:204:12: ( statement_call_args )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if ((EXPRESSION <= LA41_0 <= ID) or LA41_0 == MINUS or LA41_0 == NUMBER or LA41_0 == STRING) :
                    alt41 = 1
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:204:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2237)
                    statement_call_args213 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args213.tree)





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
                # 205:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:205:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:205:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:208:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID214 = None
        NEWLINE216 = None
        INDENT217 = None
        NEWLINE218 = None
        NEWLINE220 = None
        DEDENT221 = None
        NEWLINE222 = None
        statement_call_args215 = None

        statement_call_args219 = None


        ID214_tree = None
        NEWLINE216_tree = None
        INDENT217_tree = None
        NEWLINE218_tree = None
        NEWLINE220_tree = None
        DEDENT221_tree = None
        NEWLINE222_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:209:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:209:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID214 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2281) 
                stream_ID.add(ID214)


                # grammar/ShyRecognizerFrontend.g:209:12: ( statement_call_args )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if ((EXPRESSION <= LA42_0 <= ID) or LA42_0 == MINUS or LA42_0 == NUMBER or LA42_0 == STRING) :
                    alt42 = 1
                if alt42 == 1:
                    # grammar/ShyRecognizerFrontend.g:209:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2283)
                    statement_call_args215 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args215.tree)





                NEWLINE216 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2287) 
                stream_NEWLINE.add(NEWLINE216)


                INDENT217 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2297) 
                stream_INDENT.add(INDENT217)


                NEWLINE218 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2299) 
                stream_NEWLINE.add(NEWLINE218)


                # grammar/ShyRecognizerFrontend.g:210:24: ( statement_call_args NEWLINE )+
                cnt43 = 0
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER or LA43_0 == STRING) :
                        alt43 = 1


                    if alt43 == 1:
                        # grammar/ShyRecognizerFrontend.g:210:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2303)
                        statement_call_args219 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args219.tree)


                        NEWLINE220 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2305) 
                        stream_NEWLINE.add(NEWLINE220)



                    else:
                        if cnt43 >= 1:
                            break #loop43

                        eee = EarlyExitException(43, self.input)
                        raise eee

                    cnt43 += 1


                DEDENT221 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2311) 
                stream_DEDENT.add(DEDENT221)


                NEWLINE222 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2313) 
                stream_NEWLINE.add(NEWLINE222)


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
                # 211:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:211:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:211:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:214:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value223 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:214:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:214:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:214:23: ( arbitrary_value )+
                cnt44 = 0
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA44_0 <= ID) or LA44_0 == MINUS or LA44_0 == NUMBER or LA44_0 == STRING) :
                        alt44 = 1


                    if alt44 == 1:
                        # grammar/ShyRecognizerFrontend.g:214:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2349)
                        arbitrary_value223 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value223.tree)



                    else:
                        if cnt44 >= 1:
                            break #loop44

                        eee = EarlyExitException(44, self.input)
                        raise eee

                    cnt44 += 1




                retval.stop = self.input.LT(-1)


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


    class statement_send_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_send_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_send"
    # grammar/ShyRecognizerFrontend.g:216:1: statement_send : ( SEND ID ( statement_send_args )? NEWLINE -> ^( TREE_STATEMENT_SEND ID ( statement_send_args )? ) | SEND ID ( statement_send_args )? NEWLINE INDENT NEWLINE ( statement_send_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_SEND ID ( statement_send_args )* ) );
    def statement_send(self, ):
        retval = self.statement_send_return()
        retval.start = self.input.LT(1)


        root_0 = None

        SEND224 = None
        ID225 = None
        NEWLINE227 = None
        SEND228 = None
        ID229 = None
        NEWLINE231 = None
        INDENT232 = None
        NEWLINE233 = None
        NEWLINE235 = None
        DEDENT236 = None
        NEWLINE237 = None
        statement_send_args226 = None

        statement_send_args230 = None

        statement_send_args234 = None


        SEND224_tree = None
        ID225_tree = None
        NEWLINE227_tree = None
        SEND228_tree = None
        ID229_tree = None
        NEWLINE231_tree = None
        INDENT232_tree = None
        NEWLINE233_tree = None
        NEWLINE235_tree = None
        DEDENT236_tree = None
        NEWLINE237_tree = None
        stream_SEND = RewriteRuleTokenStream(self._adaptor, "token SEND")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_send_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_send_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:217:5: ( SEND ID ( statement_send_args )? NEWLINE -> ^( TREE_STATEMENT_SEND ID ( statement_send_args )? ) | SEND ID ( statement_send_args )? NEWLINE INDENT NEWLINE ( statement_send_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_SEND ID ( statement_send_args )* ) )
                alt48 = 2
                alt48 = self.dfa48.predict(self.input)
                if alt48 == 1:
                    # grammar/ShyRecognizerFrontend.g:217:9: SEND ID ( statement_send_args )? NEWLINE
                    pass 
                    SEND224 = self.match(self.input, SEND, self.FOLLOW_SEND_in_statement_send2366) 
                    stream_SEND.add(SEND224)


                    ID225 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_send2368) 
                    stream_ID.add(ID225)


                    # grammar/ShyRecognizerFrontend.g:217:17: ( statement_send_args )?
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA45_0 <= ID) or LA45_0 == MINUS or LA45_0 == NUMBER or LA45_0 == STRING) :
                        alt45 = 1
                    if alt45 == 1:
                        # grammar/ShyRecognizerFrontend.g:217:17: statement_send_args
                        pass 
                        self._state.following.append(self.FOLLOW_statement_send_args_in_statement_send2370)
                        statement_send_args226 = self.statement_send_args()

                        self._state.following.pop()
                        stream_statement_send_args.add(statement_send_args226.tree)





                    NEWLINE227 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_send2374) 
                    stream_NEWLINE.add(NEWLINE227)


                    # AST Rewrite
                    # elements: ID, statement_send_args
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 218:9: -> ^( TREE_STATEMENT_SEND ID ( statement_send_args )? )
                    # grammar/ShyRecognizerFrontend.g:218:13: ^( TREE_STATEMENT_SEND ID ( statement_send_args )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_SEND, "TREE_STATEMENT_SEND")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:218:39: ( statement_send_args )?
                    if stream_statement_send_args.hasNext():
                        self._adaptor.addChild(root_1, stream_statement_send_args.nextTree())


                    stream_statement_send_args.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt48 == 2:
                    # grammar/ShyRecognizerFrontend.g:219:9: SEND ID ( statement_send_args )? NEWLINE INDENT NEWLINE ( statement_send_args NEWLINE )+ DEDENT NEWLINE
                    pass 
                    SEND228 = self.match(self.input, SEND, self.FOLLOW_SEND_in_statement_send2407) 
                    stream_SEND.add(SEND228)


                    ID229 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_send2409) 
                    stream_ID.add(ID229)


                    # grammar/ShyRecognizerFrontend.g:219:17: ( statement_send_args )?
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA46_0 <= ID) or LA46_0 == MINUS or LA46_0 == NUMBER or LA46_0 == STRING) :
                        alt46 = 1
                    if alt46 == 1:
                        # grammar/ShyRecognizerFrontend.g:219:17: statement_send_args
                        pass 
                        self._state.following.append(self.FOLLOW_statement_send_args_in_statement_send2411)
                        statement_send_args230 = self.statement_send_args()

                        self._state.following.pop()
                        stream_statement_send_args.add(statement_send_args230.tree)





                    NEWLINE231 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_send2415) 
                    stream_NEWLINE.add(NEWLINE231)


                    INDENT232 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_send2425) 
                    stream_INDENT.add(INDENT232)


                    NEWLINE233 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_send2427) 
                    stream_NEWLINE.add(NEWLINE233)


                    # grammar/ShyRecognizerFrontend.g:220:24: ( statement_send_args NEWLINE )+
                    cnt47 = 0
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA47_0 <= ID) or LA47_0 == MINUS or LA47_0 == NUMBER or LA47_0 == STRING) :
                            alt47 = 1


                        if alt47 == 1:
                            # grammar/ShyRecognizerFrontend.g:220:26: statement_send_args NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_statement_send_args_in_statement_send2431)
                            statement_send_args234 = self.statement_send_args()

                            self._state.following.pop()
                            stream_statement_send_args.add(statement_send_args234.tree)


                            NEWLINE235 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_send2433) 
                            stream_NEWLINE.add(NEWLINE235)



                        else:
                            if cnt47 >= 1:
                                break #loop47

                            eee = EarlyExitException(47, self.input)
                            raise eee

                        cnt47 += 1


                    DEDENT236 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_send2439) 
                    stream_DEDENT.add(DEDENT236)


                    NEWLINE237 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_send2441) 
                    stream_NEWLINE.add(NEWLINE237)


                    # AST Rewrite
                    # elements: statement_send_args, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 221:9: -> ^( TREE_STATEMENT_SEND ID ( statement_send_args )* )
                    # grammar/ShyRecognizerFrontend.g:221:13: ^( TREE_STATEMENT_SEND ID ( statement_send_args )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_SEND, "TREE_STATEMENT_SEND")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:221:39: ( statement_send_args )*
                    while stream_statement_send_args.hasNext():
                        self._adaptor.addChild(root_1, stream_statement_send_args.nextTree())


                    stream_statement_send_args.reset();

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

    # $ANTLR end "statement_send"


    class statement_send_args_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_send_args_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_send_args"
    # grammar/ShyRecognizerFrontend.g:224:1: statement_send_args : ( arbitrary_value )+ ;
    def statement_send_args(self, ):
        retval = self.statement_send_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value238 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:224:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:224:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:224:23: ( arbitrary_value )+
                cnt49 = 0
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA49_0 <= ID) or LA49_0 == MINUS or LA49_0 == NUMBER or LA49_0 == STRING) :
                        alt49 = 1


                    if alt49 == 1:
                        # grammar/ShyRecognizerFrontend.g:224:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_send_args2477)
                        arbitrary_value238 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value238.tree)



                    else:
                        if cnt49 >= 1:
                            break #loop49

                        eee = EarlyExitException(49, self.input)
                        raise eee

                    cnt49 += 1




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "statement_send_args"


    class arbitrary_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.arbitrary_value_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerFrontend.g:226:1: arbitrary_value : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID239 = None
        EXPRESSION240 = None
        STRING241 = None
        num_whole242 = None

        num_fract243 = None


        ID239_tree = None
        EXPRESSION240_tree = None
        STRING241_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:227:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
                alt50 = 5
                LA50 = self.input.LA(1)
                if LA50 == ID:
                    alt50 = 1
                elif LA50 == EXPRESSION:
                    alt50 = 2
                elif LA50 == STRING:
                    alt50 = 3
                elif LA50 == MINUS:
                    LA50_4 = self.input.LA(2)

                    if (LA50_4 == NUMBER) :
                        LA50_5 = self.input.LA(3)

                        if (LA50_5 == DIVIDE) :
                            alt50 = 5
                        elif (LA50_5 == ARROW_RIGHT or LA50_5 == DO or (EXPRESSION <= LA50_5 <= ID) or LA50_5 == MINUS or (NEWLINE <= LA50_5 <= NUMBER) or LA50_5 == STRING) :
                            alt50 = 4
                        else:
                            nvae = NoViableAltException("", 50, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 50, 4, self.input)

                        raise nvae


                elif LA50 == NUMBER:
                    LA50_5 = self.input.LA(2)

                    if (LA50_5 == DIVIDE) :
                        alt50 = 5
                    elif (LA50_5 == ARROW_RIGHT or LA50_5 == DO or (EXPRESSION <= LA50_5 <= ID) or LA50_5 == MINUS or (NEWLINE <= LA50_5 <= NUMBER) or LA50_5 == STRING) :
                        alt50 = 4
                    else:
                        nvae = NoViableAltException("", 50, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae


                if alt50 == 1:
                    # grammar/ShyRecognizerFrontend.g:227:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID239 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2494)
                    ID239_tree = self._adaptor.createWithPayload(ID239)
                    self._adaptor.addChild(root_0, ID239_tree)




                elif alt50 == 2:
                    # grammar/ShyRecognizerFrontend.g:228:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION240 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2504)
                    EXPRESSION240_tree = self._adaptor.createWithPayload(EXPRESSION240)
                    self._adaptor.addChild(root_0, EXPRESSION240_tree)




                elif alt50 == 3:
                    # grammar/ShyRecognizerFrontend.g:229:9: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING241 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2514)
                    STRING241_tree = self._adaptor.createWithPayload(STRING241)
                    self._adaptor.addChild(root_0, STRING241_tree)




                elif alt50 == 4:
                    # grammar/ShyRecognizerFrontend.g:230:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2524)
                    num_whole242 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole242.tree)



                elif alt50 == 5:
                    # grammar/ShyRecognizerFrontend.g:231:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2534)
                    num_fract243 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract243.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:234:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS244 = None
        ID245 = None
        NEWLINE246 = None
        INDENT247 = None
        NEWLINE248 = None
        DEDENT250 = None
        NEWLINE251 = None
        consts_items249 = None


        CONSTS244_tree = None
        ID245_tree = None
        NEWLINE246_tree = None
        INDENT247_tree = None
        NEWLINE248_tree = None
        DEDENT250_tree = None
        NEWLINE251_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:235:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:235:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS244 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2553) 
                stream_CONSTS.add(CONSTS244)


                ID245 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2555) 
                stream_ID.add(ID245)


                NEWLINE246 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2557) 
                stream_NEWLINE.add(NEWLINE246)


                INDENT247 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2567) 
                stream_INDENT.add(INDENT247)


                NEWLINE248 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2569) 
                stream_NEWLINE.add(NEWLINE248)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2571)
                consts_items249 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items249.tree)


                DEDENT250 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2573) 
                stream_DEDENT.add(DEDENT250)


                NEWLINE251 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2575) 
                stream_NEWLINE.add(NEWLINE251)


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
                # 237:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:237:13: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:239:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item252 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:239:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:239:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:239:16: ( consts_item )+
                cnt51 = 0
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == ID) :
                        alt51 = 1


                    if alt51 == 1:
                        # grammar/ShyRecognizerFrontend.g:239:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2608)
                        consts_item252 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item252.tree)



                    else:
                        if cnt51 >= 1:
                            break #loop51

                        eee = EarlyExitException(51, self.input)
                        raise eee

                    cnt51 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:240:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID253 = None
        NEWLINE255 = None
        ID256 = None
        NEWLINE258 = None
        ID259 = None
        EXPRESSION260 = None
        NEWLINE261 = None
        num_whole254 = None

        num_fract257 = None


        ID253_tree = None
        NEWLINE255_tree = None
        ID256_tree = None
        NEWLINE258_tree = None
        ID259_tree = None
        EXPRESSION260_tree = None
        NEWLINE261_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:241:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt52 = 3
                LA52_0 = self.input.LA(1)

                if (LA52_0 == ID) :
                    LA52 = self.input.LA(2)
                    if LA52 == EXPRESSION:
                        alt52 = 3
                    elif LA52 == MINUS:
                        LA52_3 = self.input.LA(3)

                        if (LA52_3 == NUMBER) :
                            LA52_4 = self.input.LA(4)

                            if (LA52_4 == DIVIDE) :
                                alt52 = 2
                            elif (LA52_4 == NEWLINE) :
                                alt52 = 1
                            else:
                                nvae = NoViableAltException("", 52, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 52, 3, self.input)

                            raise nvae


                    elif LA52 == NUMBER:
                        LA52_4 = self.input.LA(3)

                        if (LA52_4 == DIVIDE) :
                            alt52 = 2
                        elif (LA52_4 == NEWLINE) :
                            alt52 = 1
                        else:
                            nvae = NoViableAltException("", 52, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 52, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 52, 0, self.input)

                    raise nvae


                if alt52 == 1:
                    # grammar/ShyRecognizerFrontend.g:241:9: ID num_whole NEWLINE
                    pass 
                    ID253 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2624) 
                    stream_ID.add(ID253)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2626)
                    num_whole254 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole254.tree)


                    NEWLINE255 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2628) 
                    stream_NEWLINE.add(NEWLINE255)


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
                    # 241:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:241:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt52 == 2:
                    # grammar/ShyRecognizerFrontend.g:242:9: ID num_fract NEWLINE
                    pass 
                    ID256 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2650) 
                    stream_ID.add(ID256)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2652)
                    num_fract257 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract257.tree)


                    NEWLINE258 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2654) 
                    stream_NEWLINE.add(NEWLINE258)


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
                    # 242:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:242:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt52 == 3:
                    # grammar/ShyRecognizerFrontend.g:243:9: ID EXPRESSION NEWLINE
                    pass 
                    ID259 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2676) 
                    stream_ID.add(ID259)


                    EXPRESSION260 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2678) 
                    stream_EXPRESSION.add(EXPRESSION260)


                    NEWLINE261 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2680) 
                    stream_NEWLINE.add(NEWLINE261)


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
                    # 243:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:243:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:246:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES262 = None
        ID263 = None
        NEWLINE264 = None
        INDENT265 = None
        NEWLINE266 = None
        DEDENT268 = None
        NEWLINE269 = None
        types_item267 = None


        TYPES262_tree = None
        ID263_tree = None
        NEWLINE264_tree = None
        INDENT265_tree = None
        NEWLINE266_tree = None
        DEDENT268_tree = None
        NEWLINE269_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:247:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:247:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES262 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2711) 
                stream_TYPES.add(TYPES262)


                ID263 = self.match(self.input, ID, self.FOLLOW_ID_in_types2713) 
                stream_ID.add(ID263)


                NEWLINE264 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2715) 
                stream_NEWLINE.add(NEWLINE264)


                INDENT265 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2725) 
                stream_INDENT.add(INDENT265)


                NEWLINE266 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2727) 
                stream_NEWLINE.add(NEWLINE266)


                # grammar/ShyRecognizerFrontend.g:248:24: ( types_item )+
                cnt53 = 0
                while True: #loop53
                    alt53 = 2
                    LA53_0 = self.input.LA(1)

                    if (LA53_0 == ID) :
                        alt53 = 1


                    if alt53 == 1:
                        # grammar/ShyRecognizerFrontend.g:248:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2729)
                        types_item267 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item267.tree)



                    else:
                        if cnt53 >= 1:
                            break #loop53

                        eee = EarlyExitException(53, self.input)
                        raise eee

                    cnt53 += 1


                DEDENT268 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2733) 
                stream_DEDENT.add(DEDENT268)


                NEWLINE269 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2735) 
                stream_NEWLINE.add(NEWLINE269)


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
                # 249:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:249:13: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:249:30: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:251:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID270 = None
        attrs_hints271 = None


        ID270_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:251:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:251:14: ID attrs_hints
                pass 
                ID270 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2770) 
                stream_ID.add(ID270)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2772)
                attrs_hints271 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints271.tree)


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
                # 251:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:251:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:253:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES272 = None
        ID273 = None
        NEWLINE274 = None
        INDENT275 = None
        NEWLINE276 = None
        DEDENT278 = None
        NEWLINE279 = None
        messages_item277 = None


        MESSAGES272_tree = None
        ID273_tree = None
        NEWLINE274_tree = None
        INDENT275_tree = None
        NEWLINE276_tree = None
        DEDENT278_tree = None
        NEWLINE279_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:254:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:254:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES272 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2799) 
                stream_MESSAGES.add(MESSAGES272)


                ID273 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2801) 
                stream_ID.add(ID273)


                NEWLINE274 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2803) 
                stream_NEWLINE.add(NEWLINE274)


                INDENT275 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2813) 
                stream_INDENT.add(INDENT275)


                NEWLINE276 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2815) 
                stream_NEWLINE.add(NEWLINE276)


                # grammar/ShyRecognizerFrontend.g:255:24: ( messages_item )+
                cnt54 = 0
                while True: #loop54
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if (LA54_0 == ID) :
                        alt54 = 1


                    if alt54 == 1:
                        # grammar/ShyRecognizerFrontend.g:255:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2817)
                        messages_item277 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item277.tree)



                    else:
                        if cnt54 >= 1:
                            break #loop54

                        eee = EarlyExitException(54, self.input)
                        raise eee

                    cnt54 += 1


                DEDENT278 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2821) 
                stream_DEDENT.add(DEDENT278)


                NEWLINE279 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2823) 
                stream_NEWLINE.add(NEWLINE279)


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
                # 256:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:256:13: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:256:33: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:259:1: messages_item : ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) );
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID280 = None
        ID282 = None
        REPLY283 = None
        ID285 = None
        REQUEST286 = None
        ID288 = None
        NEWLINE289 = None
        INDENT290 = None
        NEWLINE291 = None
        REPLY292 = None
        DEDENT294 = None
        NEWLINE295 = None
        ID296 = None
        NEWLINE297 = None
        INDENT298 = None
        NEWLINE299 = None
        REQUEST300 = None
        DEDENT302 = None
        NEWLINE303 = None
        ID304 = None
        NEWLINE305 = None
        INDENT306 = None
        NEWLINE307 = None
        REQUEST308 = None
        REPLY310 = None
        DEDENT312 = None
        NEWLINE313 = None
        attrs_hints281 = None

        attrs_hints284 = None

        attrs_hints287 = None

        attrs_hints293 = None

        attrs_hints301 = None

        attrs_hints309 = None

        attrs_hints311 = None


        ID280_tree = None
        ID282_tree = None
        REPLY283_tree = None
        ID285_tree = None
        REQUEST286_tree = None
        ID288_tree = None
        NEWLINE289_tree = None
        INDENT290_tree = None
        NEWLINE291_tree = None
        REPLY292_tree = None
        DEDENT294_tree = None
        NEWLINE295_tree = None
        ID296_tree = None
        NEWLINE297_tree = None
        INDENT298_tree = None
        NEWLINE299_tree = None
        REQUEST300_tree = None
        DEDENT302_tree = None
        NEWLINE303_tree = None
        ID304_tree = None
        NEWLINE305_tree = None
        INDENT306_tree = None
        NEWLINE307_tree = None
        REQUEST308_tree = None
        REPLY310_tree = None
        DEDENT312_tree = None
        NEWLINE313_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_REPLY = RewriteRuleTokenStream(self._adaptor, "token REPLY")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:260:5: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) )
                alt55 = 6
                alt55 = self.dfa55.predict(self.input)
                if alt55 == 1:
                    # grammar/ShyRecognizerFrontend.g:260:9: ID attrs_hints
                    pass 
                    ID280 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2865) 
                    stream_ID.add(ID280)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2867)
                    attrs_hints281 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints281.tree)


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
                    # 261:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:261:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
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




                elif alt55 == 2:
                    # grammar/ShyRecognizerFrontend.g:264:9: ID REPLY attrs_hints
                    pass 
                    ID282 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2928) 
                    stream_ID.add(ID282)


                    REPLY283 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2930) 
                    stream_REPLY.add(REPLY283)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2932)
                    attrs_hints284 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints284.tree)


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
                    # 265:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:265:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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




                elif alt55 == 3:
                    # grammar/ShyRecognizerFrontend.g:268:9: ID REQUEST attrs_hints
                    pass 
                    ID285 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2993) 
                    stream_ID.add(ID285)


                    REQUEST286 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item2995) 
                    stream_REQUEST.add(REQUEST286)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2997)
                    attrs_hints287 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints287.tree)


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




                elif alt55 == 4:
                    # grammar/ShyRecognizerFrontend.g:272:9: ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID288 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3058) 
                    stream_ID.add(ID288)


                    NEWLINE289 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3060) 
                    stream_NEWLINE.add(NEWLINE289)


                    INDENT290 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3062) 
                    stream_INDENT.add(INDENT290)


                    NEWLINE291 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3064) 
                    stream_NEWLINE.add(NEWLINE291)


                    REPLY292 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item3066) 
                    stream_REPLY.add(REPLY292)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3068)
                    attrs_hints293 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints293.tree)


                    DEDENT294 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3070) 
                    stream_DEDENT.add(DEDENT294)


                    NEWLINE295 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3072) 
                    stream_NEWLINE.add(NEWLINE295)


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
                    # 273:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:273:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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




                elif alt55 == 5:
                    # grammar/ShyRecognizerFrontend.g:276:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE
                    pass 
                    ID296 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3133) 
                    stream_ID.add(ID296)


                    NEWLINE297 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3135) 
                    stream_NEWLINE.add(NEWLINE297)


                    INDENT298 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3137) 
                    stream_INDENT.add(INDENT298)


                    NEWLINE299 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3139) 
                    stream_NEWLINE.add(NEWLINE299)


                    REQUEST300 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3141) 
                    stream_REQUEST.add(REQUEST300)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3143)
                    attrs_hints301 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints301.tree)


                    DEDENT302 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3145) 
                    stream_DEDENT.add(DEDENT302)


                    NEWLINE303 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3147) 
                    stream_NEWLINE.add(NEWLINE303)


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
                    # 277:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:277:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
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




                elif alt55 == 6:
                    # grammar/ShyRecognizerFrontend.g:280:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID304 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3208) 
                    stream_ID.add(ID304)


                    NEWLINE305 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3210) 
                    stream_NEWLINE.add(NEWLINE305)


                    INDENT306 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3212) 
                    stream_INDENT.add(INDENT306)


                    NEWLINE307 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3214) 
                    stream_NEWLINE.add(NEWLINE307)


                    REQUEST308 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3228) 
                    stream_REQUEST.add(REQUEST308)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3230)
                    attrs_hints309 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints309.tree)


                    REPLY310 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item3244) 
                    stream_REPLY.add(REPLY310)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3246)
                    attrs_hints311 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints311.tree)


                    DEDENT312 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3256) 
                    stream_DEDENT.add(DEDENT312)


                    NEWLINE313 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3258) 
                    stream_NEWLINE.add(NEWLINE313)


                    # AST Rewrite
                    # elements: ID, attrs_hints, attrs_hints
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 284:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:284:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:290:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS314 = None
        ID315 = None
        attrs_hints316 = None


        VARS314_tree = None
        ID315_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:291:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:291:9: VARS ID attrs_hints
                pass 
                VARS314 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars3348) 
                stream_VARS.add(VARS314)


                ID315 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3350) 
                stream_ID.add(ID315)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3352)
                attrs_hints316 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints316.tree)


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
                # 292:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:292:13: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:295:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE318 = None
        NEWLINE319 = None
        INDENT320 = None
        NEWLINE321 = None
        NEWLINE323 = None
        DEDENT324 = None
        NEWLINE325 = None
        NEWLINE327 = None
        INDENT328 = None
        NEWLINE329 = None
        NEWLINE331 = None
        DEDENT332 = None
        NEWLINE333 = None
        attr_hint317 = None

        attr_hint322 = None

        attr_hint326 = None

        attr_hint330 = None


        NEWLINE318_tree = None
        NEWLINE319_tree = None
        INDENT320_tree = None
        NEWLINE321_tree = None
        NEWLINE323_tree = None
        DEDENT324_tree = None
        NEWLINE325_tree = None
        NEWLINE327_tree = None
        INDENT328_tree = None
        NEWLINE329_tree = None
        NEWLINE331_tree = None
        DEDENT332_tree = None
        NEWLINE333_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:296:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt58 = 3
                alt58 = self.dfa58.predict(self.input)
                if alt58 == 1:
                    # grammar/ShyRecognizerFrontend.g:296:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3392)
                    attr_hint317 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint317.tree)


                    NEWLINE318 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3394) 
                    stream_NEWLINE.add(NEWLINE318)


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
                    # 297:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt58 == 2:
                    # grammar/ShyRecognizerFrontend.g:298:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE319 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3419) 
                    stream_NEWLINE.add(NEWLINE319)


                    # grammar/ShyRecognizerFrontend.g:299:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:299:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT320 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3431) 
                    stream_INDENT.add(INDENT320)


                    NEWLINE321 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3433) 
                    stream_NEWLINE.add(NEWLINE321)


                    # grammar/ShyRecognizerFrontend.g:299:26: ( attr_hint NEWLINE )+
                    cnt56 = 0
                    while True: #loop56
                        alt56 = 2
                        LA56_0 = self.input.LA(1)

                        if (LA56_0 == CURLY_OPEN or LA56_0 == ID) :
                            alt56 = 1


                        if alt56 == 1:
                            # grammar/ShyRecognizerFrontend.g:299:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3437)
                            attr_hint322 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint322.tree)


                            NEWLINE323 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3439) 
                            stream_NEWLINE.add(NEWLINE323)



                        else:
                            if cnt56 >= 1:
                                break #loop56

                            eee = EarlyExitException(56, self.input)
                            raise eee

                        cnt56 += 1


                    DEDENT324 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3445) 
                    stream_DEDENT.add(DEDENT324)


                    NEWLINE325 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3447) 
                    stream_NEWLINE.add(NEWLINE325)





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
                    # 300:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:300:30: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt58 == 3:
                    # grammar/ShyRecognizerFrontend.g:301:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3476)
                    attr_hint326 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint326.tree)


                    NEWLINE327 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3478) 
                    stream_NEWLINE.add(NEWLINE327)


                    # grammar/ShyRecognizerFrontend.g:302:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:302:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT328 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3490) 
                    stream_INDENT.add(INDENT328)


                    NEWLINE329 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3492) 
                    stream_NEWLINE.add(NEWLINE329)


                    # grammar/ShyRecognizerFrontend.g:302:26: ( attr_hint NEWLINE )+
                    cnt57 = 0
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == CURLY_OPEN or LA57_0 == ID) :
                            alt57 = 1


                        if alt57 == 1:
                            # grammar/ShyRecognizerFrontend.g:302:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3496)
                            attr_hint330 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint330.tree)


                            NEWLINE331 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3498) 
                            stream_NEWLINE.add(NEWLINE331)



                        else:
                            if cnt57 >= 1:
                                break #loop57

                            eee = EarlyExitException(57, self.input)
                            raise eee

                        cnt57 += 1


                    DEDENT332 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3504) 
                    stream_DEDENT.add(DEDENT332)


                    NEWLINE333 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3506) 
                    stream_NEWLINE.add(NEWLINE333)





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
                    # 303:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:303:30: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:305:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID334 = None
        ID336 = None
        NEWLINE338 = None
        INDENT339 = None
        NEWLINE340 = None
        ID341 = None
        NEWLINE342 = None
        DEDENT343 = None
        hint335 = None

        hint337 = None


        ID334_tree = None
        ID336_tree = None
        NEWLINE338_tree = None
        INDENT339_tree = None
        NEWLINE340_tree = None
        ID341_tree = None
        NEWLINE342_tree = None
        DEDENT343_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:306:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt63 = 3
                alt63 = self.dfa63.predict(self.input)
                if alt63 == 1:
                    # grammar/ShyRecognizerFrontend.g:306:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:306:9: ( ID )+
                    cnt59 = 0
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == ID) :
                            alt59 = 1


                        if alt59 == 1:
                            # grammar/ShyRecognizerFrontend.g:306:9: ID
                            pass 
                            ID334 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3544) 
                            stream_ID.add(ID334)



                        else:
                            if cnt59 >= 1:
                                break #loop59

                            eee = EarlyExitException(59, self.input)
                            raise eee

                        cnt59 += 1


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
                    # 307:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:307:13: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:307:46: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:307:46: ^( TREE_ATTR ID )
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




                elif alt63 == 2:
                    # grammar/ShyRecognizerFrontend.g:308:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3586)
                    hint335 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint335.tree)


                    # grammar/ShyRecognizerFrontend.g:308:14: ( ID )+
                    cnt60 = 0
                    while True: #loop60
                        alt60 = 2
                        LA60_0 = self.input.LA(1)

                        if (LA60_0 == ID) :
                            alt60 = 1


                        if alt60 == 1:
                            # grammar/ShyRecognizerFrontend.g:308:14: ID
                            pass 
                            ID336 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3588) 
                            stream_ID.add(ID336)



                        else:
                            if cnt60 >= 1:
                                break #loop60

                            eee = EarlyExitException(60, self.input)
                            raise eee

                        cnt60 += 1


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




                elif alt63 == 3:
                    # grammar/ShyRecognizerFrontend.g:310:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3629)
                    hint337 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint337.tree)


                    NEWLINE338 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3631) 
                    stream_NEWLINE.add(NEWLINE338)


                    INDENT339 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint3633) 
                    stream_INDENT.add(INDENT339)


                    NEWLINE340 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3635) 
                    stream_NEWLINE.add(NEWLINE340)


                    # grammar/ShyRecognizerFrontend.g:310:37: ( ( ID )+ NEWLINE )+
                    cnt62 = 0
                    while True: #loop62
                        alt62 = 2
                        LA62_0 = self.input.LA(1)

                        if (LA62_0 == ID) :
                            alt62 = 1


                        if alt62 == 1:
                            # grammar/ShyRecognizerFrontend.g:310:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:310:39: ( ID )+
                            cnt61 = 0
                            while True: #loop61
                                alt61 = 2
                                LA61_0 = self.input.LA(1)

                                if (LA61_0 == ID) :
                                    alt61 = 1


                                if alt61 == 1:
                                    # grammar/ShyRecognizerFrontend.g:310:39: ID
                                    pass 
                                    ID341 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3639) 
                                    stream_ID.add(ID341)



                                else:
                                    if cnt61 >= 1:
                                        break #loop61

                                    eee = EarlyExitException(61, self.input)
                                    raise eee

                                cnt61 += 1


                            NEWLINE342 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3643) 
                            stream_NEWLINE.add(NEWLINE342)



                        else:
                            if cnt62 >= 1:
                                break #loop62

                            eee = EarlyExitException(62, self.input)
                            raise eee

                        cnt62 += 1


                    DEDENT343 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint3649) 
                    stream_DEDENT.add(DEDENT343)


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
                    # 311:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:311:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:311:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:311:36: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:314:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN344 = None
        ID345 = None
        CURLY_CLOSE346 = None
        CURLY_OPEN347 = None
        ID348 = None
        CURLY_CLOSE350 = None
        hint_arg349 = None


        CURLY_OPEN344_tree = None
        ID345_tree = None
        CURLY_CLOSE346_tree = None
        CURLY_OPEN347_tree = None
        ID348_tree = None
        CURLY_CLOSE350_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:315:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt65 = 2
                LA65_0 = self.input.LA(1)

                if (LA65_0 == CURLY_OPEN) :
                    LA65_1 = self.input.LA(2)

                    if (LA65_1 == ID) :
                        LA65_2 = self.input.LA(3)

                        if (LA65_2 == CURLY_CLOSE) :
                            alt65 = 1
                        elif (LA65_2 == ID or LA65_2 == UNDERSCORE) :
                            alt65 = 2
                        else:
                            nvae = NoViableAltException("", 65, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 65, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 65, 0, self.input)

                    raise nvae


                if alt65 == 1:
                    # grammar/ShyRecognizerFrontend.g:315:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN344 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3697) 
                    stream_CURLY_OPEN.add(CURLY_OPEN344)


                    ID345 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3699) 
                    stream_ID.add(ID345)


                    CURLY_CLOSE346 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3701) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE346)


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
                    # 315:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:315:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt65 == 2:
                    # grammar/ShyRecognizerFrontend.g:316:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN347 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3721) 
                    stream_CURLY_OPEN.add(CURLY_OPEN347)


                    ID348 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3723) 
                    stream_ID.add(ID348)


                    # grammar/ShyRecognizerFrontend.g:316:23: ( hint_arg )+
                    cnt64 = 0
                    while True: #loop64
                        alt64 = 2
                        LA64_0 = self.input.LA(1)

                        if (LA64_0 == ID or LA64_0 == UNDERSCORE) :
                            alt64 = 1


                        if alt64 == 1:
                            # grammar/ShyRecognizerFrontend.g:316:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint3725)
                            hint_arg349 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg349.tree)



                        else:
                            if cnt64 >= 1:
                                break #loop64

                            eee = EarlyExitException(64, self.input)
                            raise eee

                        cnt64 += 1


                    CURLY_CLOSE350 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3729) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE350)


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
                    # 316:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:316:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:316:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:318:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set351 = None

        set351_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:318:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set351 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set351))

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
    # grammar/ShyRecognizerFrontend.g:320:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS352 = None
        NUMBER353 = None

        MINUS352_tree = None
        NUMBER353_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:320:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:320:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:320:13: ( MINUS )?
                alt66 = 2
                LA66_0 = self.input.LA(1)

                if (LA66_0 == MINUS) :
                    alt66 = 1
                if alt66 == 1:
                    # grammar/ShyRecognizerFrontend.g:320:13: MINUS
                    pass 
                    MINUS352 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3768)
                    MINUS352_tree = self._adaptor.createWithPayload(MINUS352)
                    self._adaptor.addChild(root_0, MINUS352_tree)






                NUMBER353 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3772)
                NUMBER353_tree = self._adaptor.createWithPayload(NUMBER353)
                self._adaptor.addChild(root_0, NUMBER353_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:321:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS354 = None
        NUMBER355 = None
        DIVIDE356 = None
        NUMBER357 = None

        MINUS354_tree = None
        NUMBER355_tree = None
        DIVIDE356_tree = None
        NUMBER357_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:321:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:321:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:321:13: ( MINUS )?
                alt67 = 2
                LA67_0 = self.input.LA(1)

                if (LA67_0 == MINUS) :
                    alt67 = 1
                if alt67 == 1:
                    # grammar/ShyRecognizerFrontend.g:321:13: MINUS
                    pass 
                    MINUS354 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3780)
                    MINUS354_tree = self._adaptor.createWithPayload(MINUS354)
                    self._adaptor.addChild(root_0, MINUS354_tree)






                NUMBER355 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3784)
                NUMBER355_tree = self._adaptor.createWithPayload(NUMBER355)
                self._adaptor.addChild(root_0, NUMBER355_tree)



                DIVIDE356 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3786)
                DIVIDE356_tree = self._adaptor.createWithPayload(DIVIDE356)
                self._adaptor.addChild(root_0, DIVIDE356_tree)



                NUMBER357 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3788)
                NUMBER357_tree = self._adaptor.createWithPayload(NUMBER357)
                self._adaptor.addChild(root_0, NUMBER357_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #19

    DFA19_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA19_eof = DFA.unpack(
        u"\22\uffff"
        )

    DFA19_min = DFA.unpack(
        u"\1\22\1\7\5\uffff\1\7\2\10\1\33\1\10\1\15\1\10\1\33\2\uffff\1\10"
        )

    DFA19_max = DFA.unpack(
        u"\1\130\1\45\5\uffff\3\45\1\33\1\45\1\130\1\45\1\33\2\uffff\1\45"
        )

    DFA19_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\1\7\10\uffff\1\2\1\1\1\uffff"
        )

    DFA19_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA19_transition = [
        DFA.unpack(u"\1\4\1\1\1\3\2\uffff\1\4\3\uffff\1\4\7\uffff\1\2\1\uffff"
        u"\1\4\60\uffff\1\5\1\uffff\1\6"),
        DFA.unpack(u"\2\4\11\uffff\1\10\1\7\3\uffff\1\12\2\uffff\1\14\1"
        u"\13\11\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\4\11\uffff\1\10\1\7\3\uffff\1\12\2\uffff\1\14\1"
        u"\13\11\uffff\1\11"),
        DFA.unpack(u"\1\4\11\uffff\1\10\1\15\3\uffff\1\12\2\uffff\1\14\1"
        u"\13\11\uffff\1\11"),
        DFA.unpack(u"\1\4\11\uffff\1\10\1\15\3\uffff\1\12\2\uffff\1\14\1"
        u"\13\11\uffff\1\11"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u"\1\4\5\uffff\1\16\3\uffff\1\10\1\15\3\uffff\1\12\2"
        u"\uffff\1\14\1\13\11\uffff\1\11"),
        DFA.unpack(u"\1\20\4\uffff\3\20\1\17\1\uffff\1\20\1\uffff\1\20\1"
        u"\uffff\1\20\2\uffff\2\20\2\uffff\2\20\1\uffff\1\20\60\uffff\1\20"
        u"\1\uffff\1\20"),
        DFA.unpack(u"\1\4\11\uffff\1\10\1\15\3\uffff\1\12\2\uffff\1\14\1"
        u"\13\11\uffff\1\11"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\11\uffff\1\10\1\15\3\uffff\1\12\2\uffff\1\14\1"
        u"\13\11\uffff\1\11")
    ]

    # class definition for DFA #19

    class DFA19(DFA):
        pass


    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\17\uffff"
        )

    DFA31_min = DFA.unpack(
        u"\1\22\1\7\2\10\1\33\1\10\1\22\1\23\1\10\1\33\4\uffff\1\10"
        )

    DFA31_max = DFA.unpack(
        u"\4\45\1\33\2\45\1\32\1\45\1\33\4\uffff\1\45"
        )

    DFA31_accept = DFA.unpack(
        u"\12\uffff\1\2\1\1\1\4\1\3\1\uffff"
        )

    DFA31_special = DFA.unpack(
        u"\17\uffff"
        )


    DFA31_transition = [
        DFA.unpack(u"\1\2\1\1\3\uffff\1\4\3\uffff\1\5\11\uffff\1\3"),
        DFA.unpack(u"\1\6\1\7\11\uffff\1\2\1\1\3\uffff\1\4\3\uffff\1\5\11"
        u"\uffff\1\3"),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\11\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\11\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u"\1\7\5\uffff\1\11\3\uffff\1\2\1\10\3\uffff\1\4\3\uffff"
        u"\1\5\11\uffff\1\3"),
        DFA.unpack(u"\2\13\3\uffff\1\13\2\uffff\1\12\1\13\11\uffff\1\13"),
        DFA.unpack(u"\1\15\6\uffff\1\14"),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\11\uffff"
        u"\1\3"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\11\uffff\1\2\1\10\3\uffff\1\4\3\uffff\1\5\11\uffff"
        u"\1\3")
    ]

    # class definition for DFA #31

    class DFA31(DFA):
        pass


    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA39_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA39_min = DFA.unpack(
        u"\1\23\4\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA39_max = DFA.unpack(
        u"\1\23\4\45\1\33\1\45\1\25\1\uffff\1\33\1\uffff\1\45"
        )

    DFA39_accept = DFA.unpack(
        u"\10\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA39_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA39_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\11\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7"
        u"\1\6\11\uffff\1\4"),
        DFA.unpack(u"\1\10\5\uffff\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\10\2\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11"
        u"\uffff\1\4")
    ]

    # class definition for DFA #39

    class DFA39(DFA):
        pass


    # lookup tables for DFA #40

    DFA40_eot = DFA.unpack(
        u"\14\uffff"
        )

    DFA40_eof = DFA.unpack(
        u"\14\uffff"
        )

    DFA40_min = DFA.unpack(
        u"\1\23\4\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA40_max = DFA.unpack(
        u"\1\23\4\45\1\33\1\45\1\25\1\33\2\uffff\1\45"
        )

    DFA40_accept = DFA.unpack(
        u"\11\uffff\1\2\1\1\1\uffff"
        )

    DFA40_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA40_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11\uffff\1\4"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11\uffff\1\4"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11\uffff\1\4"),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11\uffff\1\4"),
        DFA.unpack(u"\1\6"),
        DFA.unpack(u"\1\10\3\uffff\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11"
        u"\uffff\1\4"),
        DFA.unpack(u"\1\12\5\uffff\1\12\1\uffff\1\11"),
        DFA.unpack(u"\1\13"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\2\3\uffff\1\5\2\uffff\1\7\1\6\11\uffff\1\4")
    ]

    # class definition for DFA #40

    class DFA40(DFA):
        pass


    # lookup tables for DFA #48

    DFA48_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA48_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA48_min = DFA.unpack(
        u"\1\43\1\23\4\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA48_max = DFA.unpack(
        u"\1\43\1\23\4\45\1\33\1\45\1\130\1\33\2\uffff\1\45"
        )

    DFA48_accept = DFA.unpack(
        u"\12\uffff\1\2\1\1\1\uffff"
        )

    DFA48_special = DFA.unpack(
        u"\15\uffff"
        )


    DFA48_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\2"),
        DFA.unpack(u"\1\4\1\3\3\uffff\1\6\2\uffff\1\10\1\7\11\uffff\1\5"),
        DFA.unpack(u"\1\4\1\3\3\uffff\1\6\2\uffff\1\10\1\7\11\uffff\1\5"),
        DFA.unpack(u"\1\4\1\3\3\uffff\1\6\2\uffff\1\10\1\7\11\uffff\1\5"),
        DFA.unpack(u"\1\4\1\3\3\uffff\1\6\2\uffff\1\10\1\7\11\uffff\1\5"),
        DFA.unpack(u"\1\7"),
        DFA.unpack(u"\1\11\3\uffff\1\4\1\3\3\uffff\1\6\2\uffff\1\10\1\7"
        u"\11\uffff\1\5"),
        DFA.unpack(u"\1\13\4\uffff\3\13\1\12\1\uffff\1\13\1\uffff\1\13\1"
        u"\uffff\1\13\2\uffff\2\13\2\uffff\2\13\1\uffff\1\13\60\uffff\1\13"
        u"\1\uffff\1\13"),
        DFA.unpack(u"\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\4\1\3\3\uffff\1\6\2\uffff\1\10\1\7\11\uffff\1\5")
    ]

    # class definition for DFA #48

    class DFA48(DFA):
        pass


    # lookup tables for DFA #55

    DFA55_eot = DFA.unpack(
        u"\77\uffff"
        )

    DFA55_eof = DFA.unpack(
        u"\77\uffff"
        )

    DFA55_min = DFA.unpack(
        u"\1\23\1\14\2\uffff\1\25\1\uffff\1\32\1\14\1\uffff\1\14\2\23\1\25"
        u"\1\15\1\13\1\32\1\uffff\1\32\1\uffff\1\23\1\13\2\14\1\23\1\25\5"
        u"\23\1\32\1\14\1\13\1\14\1\13\1\23\1\32\1\23\1\13\1\32\1\23\1\13"
        u"\1\23\1\15\1\23\1\25\1\23\1\15\1\23\1\25\1\23\1\15\3\32\4\23\2"
        u"\15\2\32"
        )

    DFA55_max = DFA.unpack(
        u"\1\23\1\42\2\uffff\1\25\1\uffff\1\32\1\42\1\uffff\2\32\1\23\1\25"
        u"\1\41\1\124\1\32\1\uffff\1\32\1\uffff\1\32\1\124\2\23\1\32\1\25"
        u"\2\32\1\23\1\32\1\23\1\32\1\23\1\124\1\23\1\124\1\23\2\32\1\124"
        u"\2\32\1\124\1\32\1\41\1\32\1\25\1\32\1\41\1\32\1\25\1\32\1\23\3"
        u"\32\2\23\2\32\2\23\2\32"
        )

    DFA55_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\uffff\1\1\2\uffff\1\4\7\uffff\1\5\1\uffff\1"
        u"\6\54\uffff"
        )

    DFA55_special = DFA.unpack(
        u"\77\uffff"
        )


    DFA55_transition = [
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
        DFA.unpack(u"\1\23\7\uffff\1\24\100\uffff\1\24"),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\26"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\27\6\uffff\1\30"),
        DFA.unpack(u"\1\31\7\uffff\1\24\100\uffff\1\24"),
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
        DFA.unpack(u"\1\45\7\uffff\1\46\100\uffff\1\46"),
        DFA.unpack(u"\1\35\1\47\5\uffff\1\34"),
        DFA.unpack(u"\1\50\7\uffff\1\51\100\uffff\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u"\1\53"),
        DFA.unpack(u"\1\54\6\uffff\1\55"),
        DFA.unpack(u"\1\56\7\uffff\1\46\100\uffff\1\46"),
        DFA.unpack(u"\1\57"),
        DFA.unpack(u"\1\60\6\uffff\1\61"),
        DFA.unpack(u"\1\62\7\uffff\1\51\100\uffff\1\51"),
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

    # class definition for DFA #55

    class DFA55(DFA):
        pass


    # lookup tables for DFA #58

    DFA58_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA58_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA58_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA58_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\125\1\124\2\uffff\1\32\1\124\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA58_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA58_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA58_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1\6\uffff\1\3"),
        DFA.unpack(u"\1\1\6\uffff\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\6\5\uffff\1\6\1\uffff\1\7\1\6\1\uffff"
        u"\1\6\3\uffff\1\6\4\uffff\1\6\2\uffff\1\6\1\uffff\1\6\54\uffff\1"
        u"\6\1\uffff\1\6"),
        DFA.unpack(u"\1\10\7\uffff\1\11\100\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\14\7\uffff\1\11\100\uffff\1\11"),
        DFA.unpack(u"\1\12\6\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\17\6\uffff\1\20"),
        DFA.unpack(u"\1\21\5\uffff\1\17"),
        DFA.unpack(u"\1\4")
    ]

    # class definition for DFA #58

    class DFA58(DFA):
        pass


    # lookup tables for DFA #63

    DFA63_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA63_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA63_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA63_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\124\1\32\1\124\2\uffff\1\32"
        )

    DFA63_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA63_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA63_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\7\uffff\1\5\100\uffff\1\5"),
        DFA.unpack(u"\1\6\6\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\100\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\6\uffff\1\7")
    ]

    # class definition for DFA #63

    class DFA63(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 22, 24, 36, 38, 83, 85])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 22, 24, 36, 38, 83, 85])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 22, 24, 36, 38, 83, 85])
    FOLLOW_types_in_start94 = frozenset([1, 9, 22, 24, 36, 38, 83, 85])
    FOLLOW_messages_in_start98 = frozenset([1, 9, 22, 24, 36, 38, 83, 85])
    FOLLOW_vars_in_start102 = frozenset([1, 9, 22, 24, 36, 38, 83, 85])
    FOLLOW_trace_in_start106 = frozenset([1, 9, 22, 24, 36, 38, 83, 85])
    FOLLOW_MODULE_in_module125 = frozenset([19])
    FOLLOW_ID_in_module127 = frozenset([26])
    FOLLOW_NEWLINE_in_module129 = frozenset([21])
    FOLLOW_INDENT_in_module131 = frozenset([26])
    FOLLOW_NEWLINE_in_module133 = frozenset([13, 25, 30, 31, 34])
    FOLLOW_module_item_in_module135 = frozenset([13, 25, 30, 31, 34])
    FOLLOW_DEDENT_in_module139 = frozenset([26])
    FOLLOW_NEWLINE_in_module141 = frozenset([1])
    FOLLOW_module_queue_in_module_item176 = frozenset([1])
    FOLLOW_proc_in_module_item180 = frozenset([1])
    FOLLOW_receive_in_module_item184 = frozenset([1])
    FOLLOW_request_in_module_item188 = frozenset([1])
    FOLLOW_MODULE_QUEUE_in_module_queue203 = frozenset([19])
    FOLLOW_ID_in_module_queue205 = frozenset([26])
    FOLLOW_NEWLINE_in_module_queue207 = frozenset([1])
    FOLLOW_TRACE_in_trace245 = frozenset([19])
    FOLLOW_ID_in_trace247 = frozenset([26])
    FOLLOW_NEWLINE_in_trace249 = frozenset([1, 21])
    FOLLOW_INDENT_in_trace253 = frozenset([26])
    FOLLOW_NEWLINE_in_trace255 = frozenset([30])
    FOLLOW_proc_in_trace257 = frozenset([13, 30])
    FOLLOW_DEDENT_in_trace261 = frozenset([26])
    FOLLOW_NEWLINE_in_trace263 = frozenset([1])
    FOLLOW_STATELESS_in_stateless309 = frozenset([19])
    FOLLOW_ID_in_stateless311 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless313 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless317 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless319 = frozenset([30])
    FOLLOW_proc_in_stateless321 = frozenset([13, 30])
    FOLLOW_DEDENT_in_stateless325 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless327 = frozenset([1])
    FOLLOW_REQUEST_in_request373 = frozenset([19])
    FOLLOW_ID_in_request375 = frozenset([26])
    FOLLOW_NEWLINE_in_request377 = frozenset([1])
    FOLLOW_REQUEST_in_request406 = frozenset([19])
    FOLLOW_ID_in_request408 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statement_in_request410 = frozenset([1])
    FOLLOW_REQUEST_in_request447 = frozenset([19])
    FOLLOW_ID_in_request449 = frozenset([26])
    FOLLOW_NEWLINE_in_request451 = frozenset([21])
    FOLLOW_INDENT_in_request453 = frozenset([26])
    FOLLOW_NEWLINE_in_request455 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_request457 = frozenset([13])
    FOLLOW_DEDENT_in_request459 = frozenset([26])
    FOLLOW_NEWLINE_in_request461 = frozenset([1])
    FOLLOW_REQUEST_in_request492 = frozenset([19])
    FOLLOW_ID_in_request494 = frozenset([26])
    FOLLOW_NEWLINE_in_request496 = frozenset([21])
    FOLLOW_INDENT_in_request498 = frozenset([26])
    FOLLOW_NEWLINE_in_request500 = frozenset([13, 28, 85])
    FOLLOW_local_vars_in_request514 = frozenset([13, 28])
    FOLLOW_local_ops_in_request518 = frozenset([13])
    FOLLOW_DEDENT_in_request530 = frozenset([26])
    FOLLOW_NEWLINE_in_request532 = frozenset([1])
    FOLLOW_RECEIVE_in_receive578 = frozenset([19])
    FOLLOW_ID_in_receive580 = frozenset([26])
    FOLLOW_NEWLINE_in_receive582 = frozenset([1])
    FOLLOW_RECEIVE_in_receive611 = frozenset([19])
    FOLLOW_ID_in_receive613 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statement_in_receive615 = frozenset([1])
    FOLLOW_RECEIVE_in_receive652 = frozenset([19])
    FOLLOW_ID_in_receive654 = frozenset([26])
    FOLLOW_NEWLINE_in_receive656 = frozenset([21])
    FOLLOW_INDENT_in_receive658 = frozenset([26])
    FOLLOW_NEWLINE_in_receive660 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_receive662 = frozenset([13])
    FOLLOW_DEDENT_in_receive664 = frozenset([26])
    FOLLOW_NEWLINE_in_receive666 = frozenset([1])
    FOLLOW_RECEIVE_in_receive697 = frozenset([19])
    FOLLOW_ID_in_receive699 = frozenset([26])
    FOLLOW_NEWLINE_in_receive701 = frozenset([21])
    FOLLOW_INDENT_in_receive703 = frozenset([26])
    FOLLOW_NEWLINE_in_receive705 = frozenset([13, 28, 85])
    FOLLOW_local_vars_in_receive719 = frozenset([13, 28])
    FOLLOW_local_ops_in_receive723 = frozenset([13])
    FOLLOW_DEDENT_in_receive735 = frozenset([26])
    FOLLOW_NEWLINE_in_receive737 = frozenset([1])
    FOLLOW_PROC_in_proc783 = frozenset([19])
    FOLLOW_ID_in_proc785 = frozenset([26])
    FOLLOW_NEWLINE_in_proc787 = frozenset([1])
    FOLLOW_PROC_in_proc816 = frozenset([19])
    FOLLOW_ID_in_proc818 = frozenset([26])
    FOLLOW_NEWLINE_in_proc820 = frozenset([21])
    FOLLOW_INDENT_in_proc822 = frozenset([26])
    FOLLOW_NEWLINE_in_proc824 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_proc826 = frozenset([13])
    FOLLOW_DEDENT_in_proc828 = frozenset([26])
    FOLLOW_NEWLINE_in_proc830 = frozenset([1])
    FOLLOW_PROC_in_proc861 = frozenset([19])
    FOLLOW_ID_in_proc863 = frozenset([26])
    FOLLOW_NEWLINE_in_proc865 = frozenset([21])
    FOLLOW_INDENT_in_proc867 = frozenset([26])
    FOLLOW_NEWLINE_in_proc869 = frozenset([6, 13, 28, 85])
    FOLLOW_proc_args_in_proc883 = frozenset([13, 28, 85])
    FOLLOW_local_vars_in_proc887 = frozenset([13, 28])
    FOLLOW_local_ops_in_proc891 = frozenset([13])
    FOLLOW_DEDENT_in_proc903 = frozenset([26])
    FOLLOW_NEWLINE_in_proc905 = frozenset([1])
    FOLLOW_ARGS_in_proc_args955 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args957 = frozenset([1])
    FOLLOW_VARS_in_local_vars986 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_local_vars988 = frozenset([1])
    FOLLOW_OPS_in_local_ops1017 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1019 = frozenset([21])
    FOLLOW_INDENT_in_local_ops1021 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1023 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_local_ops1025 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops1027 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1029 = frozenset([1])
    FOLLOW_OPS_in_local_ops1051 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statement_in_local_ops1053 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement1091 = frozenset([26])
    FOLLOW_NEWLINE_in_statement1093 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement1119 = frozenset([1])
    FOLLOW_statement_send_in_statement1129 = frozenset([1])
    FOLLOW_statement_if_in_statement1139 = frozenset([1])
    FOLLOW_statement_assign_in_statement1149 = frozenset([1])
    FOLLOW_statement_while_in_statement1159 = frozenset([1])
    FOLLOW_statement_with_in_statement1169 = frozenset([1])
    FOLLOW_statement_in_statements1188 = frozenset([1, 18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_WITH_in_statement_with1230 = frozenset([19])
    FOLLOW_ID_in_statement_with1232 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1234 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1244 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1246 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_statement_with1248 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1250 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1252 = frozenset([1])
    FOLLOW_ID_in_statement_assign1292 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1296 = frozenset([18, 19, 23, 27, 37])
    FOLLOW_arbitrary_value_in_statement_assign1298 = frozenset([18, 19, 23, 26, 27, 37])
    FOLLOW_NEWLINE_in_statement_assign1302 = frozenset([1])
    FOLLOW_ID_in_statement_assign1355 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1359 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1361 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1363 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1365 = frozenset([18, 19, 23, 27, 37])
    FOLLOW_arbitrary_value_in_statement_assign1377 = frozenset([18, 19, 23, 26, 27, 37])
    FOLLOW_NEWLINE_in_statement_assign1381 = frozenset([13, 18, 19, 23, 27, 37])
    FOLLOW_DEDENT_in_statement_assign1387 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1389 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1442 = frozenset([8, 18, 19, 23, 27, 37])
    FOLLOW_ARROW_RIGHT_in_statement_assign1446 = frozenset([19])
    FOLLOW_ID_in_statement_assign1448 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1452 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1505 = frozenset([8, 18, 19, 23, 27, 37])
    FOLLOW_ARROW_RIGHT_in_statement_assign1509 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1511 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1513 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1515 = frozenset([19])
    FOLLOW_ID_in_statement_assign1527 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1531 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1537 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1539 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1601 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1603 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1605 = frozenset([15])
    FOLLOW_DO_in_statement_while1609 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1611 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1625 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1627 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_statement_while1629 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1631 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1633 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1673 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1683 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1695 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1803 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1805 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1837 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1839 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1871 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1873 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1877 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1879 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1893 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1895 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_statement_elif_body1897 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1899 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1901 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1941 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1943 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1957 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1959 = frozenset([18, 19, 20, 23, 27, 35, 37, 86, 88])
    FOLLOW_statements_in_statement_else1961 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1963 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1965 = frozenset([1])
    FOLLOW_condition_call_in_condition2003 = frozenset([1])
    FOLLOW_ANY_in_condition2032 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2034 = frozenset([1])
    FOLLOW_ALL_in_condition2063 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2065 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls2103 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls2113 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls2115 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2117 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls2119 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls2123 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2125 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call2159 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call2169 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line2188 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line2190 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2216 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2235 = frozenset([1, 18, 19, 23, 27, 37])
    FOLLOW_statement_call_args_in_statement_call_single_line2237 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2281 = frozenset([18, 19, 23, 26, 27, 37])
    FOLLOW_statement_call_args_in_statement_call_multi_line2283 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2287 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2297 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2299 = frozenset([18, 19, 23, 27, 37])
    FOLLOW_statement_call_args_in_statement_call_multi_line2303 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2305 = frozenset([13, 18, 19, 23, 27, 37])
    FOLLOW_DEDENT_in_statement_call_multi_line2311 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2313 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2349 = frozenset([1, 18, 19, 23, 27, 37])
    FOLLOW_SEND_in_statement_send2366 = frozenset([19])
    FOLLOW_ID_in_statement_send2368 = frozenset([18, 19, 23, 26, 27, 37])
    FOLLOW_statement_send_args_in_statement_send2370 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_send2374 = frozenset([1])
    FOLLOW_SEND_in_statement_send2407 = frozenset([19])
    FOLLOW_ID_in_statement_send2409 = frozenset([18, 19, 23, 26, 27, 37])
    FOLLOW_statement_send_args_in_statement_send2411 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_send2415 = frozenset([21])
    FOLLOW_INDENT_in_statement_send2425 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_send2427 = frozenset([18, 19, 23, 27, 37])
    FOLLOW_statement_send_args_in_statement_send2431 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_send2433 = frozenset([13, 18, 19, 23, 27, 37])
    FOLLOW_DEDENT_in_statement_send2439 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_send2441 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_send_args2477 = frozenset([1, 18, 19, 23, 27, 37])
    FOLLOW_ID_in_arbitrary_value2494 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2504 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2514 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2524 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2534 = frozenset([1])
    FOLLOW_CONSTS_in_consts2553 = frozenset([19])
    FOLLOW_ID_in_consts2555 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2557 = frozenset([21])
    FOLLOW_INDENT_in_consts2567 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2569 = frozenset([19])
    FOLLOW_consts_items_in_consts2571 = frozenset([13])
    FOLLOW_DEDENT_in_consts2573 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2575 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2608 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2624 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2626 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2628 = frozenset([1])
    FOLLOW_ID_in_consts_item2650 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2652 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2654 = frozenset([1])
    FOLLOW_ID_in_consts_item2676 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2678 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2680 = frozenset([1])
    FOLLOW_TYPES_in_types2711 = frozenset([19])
    FOLLOW_ID_in_types2713 = frozenset([26])
    FOLLOW_NEWLINE_in_types2715 = frozenset([21])
    FOLLOW_INDENT_in_types2725 = frozenset([26])
    FOLLOW_NEWLINE_in_types2727 = frozenset([19])
    FOLLOW_types_item_in_types2729 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2733 = frozenset([26])
    FOLLOW_NEWLINE_in_types2735 = frozenset([1])
    FOLLOW_ID_in_types_item2770 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2772 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2799 = frozenset([19])
    FOLLOW_ID_in_messages2801 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2803 = frozenset([21])
    FOLLOW_INDENT_in_messages2813 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2815 = frozenset([19])
    FOLLOW_messages_item_in_messages2817 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2821 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2823 = frozenset([1])
    FOLLOW_ID_in_messages_item2865 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2867 = frozenset([1])
    FOLLOW_ID_in_messages_item2928 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2930 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2932 = frozenset([1])
    FOLLOW_ID_in_messages_item2993 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item2995 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2997 = frozenset([1])
    FOLLOW_ID_in_messages_item3058 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3060 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3062 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3064 = frozenset([33])
    FOLLOW_REPLY_in_messages_item3066 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3068 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3070 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3072 = frozenset([1])
    FOLLOW_ID_in_messages_item3133 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3135 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3137 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3139 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3141 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3143 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3145 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3147 = frozenset([1])
    FOLLOW_ID_in_messages_item3208 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3210 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3212 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3214 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3228 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3230 = frozenset([33])
    FOLLOW_REPLY_in_messages_item3244 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3246 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3256 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3258 = frozenset([1])
    FOLLOW_VARS_in_vars3348 = frozenset([19])
    FOLLOW_ID_in_vars3350 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars3352 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3392 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3394 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints3419 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3431 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3433 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3437 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3439 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3445 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3447 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3476 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3478 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3490 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3492 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3496 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3498 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3504 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3506 = frozenset([1])
    FOLLOW_ID_in_attr_hint3544 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3586 = frozenset([19])
    FOLLOW_ID_in_attr_hint3588 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3629 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3631 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint3633 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3635 = frozenset([19])
    FOLLOW_ID_in_attr_hint3639 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint3643 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint3649 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3697 = frozenset([19])
    FOLLOW_ID_in_hint3699 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint3701 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3721 = frozenset([19])
    FOLLOW_ID_in_hint3723 = frozenset([19, 84])
    FOLLOW_hint_arg_in_hint3725 = frozenset([11, 19, 84])
    FOLLOW_CURLY_CLOSE_in_hint3729 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3768 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3772 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3780 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3784 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3786 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3788 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
