# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-03 22:28:15

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

        self.dfa50 = self.DFA50(
            self, 50,
            eot = self.DFA50_eot,
            eof = self.DFA50_eof,
            min = self.DFA50_min,
            max = self.DFA50_max,
            accept = self.DFA50_accept,
            special = self.DFA50_special,
            transition = self.DFA50_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
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

                                    if ((EXPRESSION <= LA10_7 <= IF) or LA10_7 == MINUS or LA10_7 == NUMBER or LA10_7 == STRING or LA10_7 == WHILE or LA10_7 == WITH) :
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


                        elif ((EXPRESSION <= LA10_2 <= IF) or LA10_2 == MINUS or LA10_2 == NUMBER or LA10_2 == STRING or LA10_2 == WHILE or LA10_2 == WITH) :
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
                    # elements: ID, statement
                    # token labels: 
                    # rule labels: retval
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

                                    if ((EXPRESSION <= LA13_7 <= IF) or LA13_7 == MINUS or LA13_7 == NUMBER or LA13_7 == STRING or LA13_7 == WHILE or LA13_7 == WITH) :
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


                        elif ((EXPRESSION <= LA13_2 <= IF) or LA13_2 == MINUS or LA13_2 == NUMBER or LA13_2 == STRING or LA13_2 == WHILE or LA13_2 == WITH) :
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
                    # elements: ID, statement
                    # token labels: 
                    # rule labels: retval
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

                                    if ((EXPRESSION <= LA17_6 <= IF) or LA17_6 == MINUS or LA17_6 == NUMBER or LA17_6 == STRING or LA17_6 == WHILE or LA17_6 == WITH) :
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
                    # elements: local_vars, ID, proc_args, local_ops
                    # token labels: 
                    # rule labels: retval
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
                    elif ((EXPRESSION <= LA18_1 <= IF) or LA18_1 == MINUS or LA18_1 == NUMBER or LA18_1 == STRING or LA18_1 == WHILE or LA18_1 == WITH) :
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
    # grammar/ShyRecognizerFrontend.g:99:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE120 = None
        statement_call_single_line119 = None

        statement_call_multi_line121 = None

        statement_if122 = None

        statement_assign123 = None

        statement_while124 = None

        statement_with125 = None


        NEWLINE120_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:100:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt19 = 6
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
                    # grammar/ShyRecognizerFrontend.g:103:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement1129)
                    statement_if122 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if122.tree)



                elif alt19 == 4:
                    # grammar/ShyRecognizerFrontend.g:104:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1139)
                    statement_assign123 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign123.tree)



                elif alt19 == 5:
                    # grammar/ShyRecognizerFrontend.g:105:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement1149)
                    statement_while124 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while124.tree)



                elif alt19 == 6:
                    # grammar/ShyRecognizerFrontend.g:106:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement1159)
                    statement_with125 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with125.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:109:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement126 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:110:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:110:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:110:9: ( statement )+
                cnt20 = 0
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA20_0 <= IF) or LA20_0 == MINUS or LA20_0 == NUMBER or LA20_0 == STRING or LA20_0 == WHILE or LA20_0 == WITH) :
                        alt20 = 1


                    if alt20 == 1:
                        # grammar/ShyRecognizerFrontend.g:110:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1178)
                        statement126 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement126.tree)



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
                # 111:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:111:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:111:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:114:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH127 = None
        ID128 = None
        NEWLINE129 = None
        INDENT130 = None
        NEWLINE131 = None
        DEDENT133 = None
        NEWLINE134 = None
        statements132 = None


        WITH127_tree = None
        ID128_tree = None
        NEWLINE129_tree = None
        INDENT130_tree = None
        NEWLINE131_tree = None
        DEDENT133_tree = None
        NEWLINE134_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:115:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:115:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH127 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1220) 
                stream_WITH.add(WITH127)


                ID128 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1222) 
                stream_ID.add(ID128)


                NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1224) 
                stream_NEWLINE.add(NEWLINE129)


                INDENT130 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1234) 
                stream_INDENT.add(INDENT130)


                NEWLINE131 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1236) 
                stream_NEWLINE.add(NEWLINE131)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1238)
                statements132 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements132.tree)


                DEDENT133 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1240) 
                stream_DEDENT.add(DEDENT133)


                NEWLINE134 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1242) 
                stream_NEWLINE.add(NEWLINE134)


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
                # 117:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:117:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:120:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID135 = None
        ARROW_LEFT136 = None
        NEWLINE138 = None
        ID139 = None
        ARROW_LEFT140 = None
        NEWLINE141 = None
        INDENT142 = None
        NEWLINE143 = None
        NEWLINE145 = None
        DEDENT146 = None
        NEWLINE147 = None
        ARROW_RIGHT149 = None
        ID150 = None
        NEWLINE151 = None
        ARROW_RIGHT153 = None
        NEWLINE154 = None
        INDENT155 = None
        NEWLINE156 = None
        ID157 = None
        NEWLINE158 = None
        DEDENT159 = None
        NEWLINE160 = None
        arbitrary_value137 = None

        arbitrary_value144 = None

        arbitrary_value148 = None

        arbitrary_value152 = None


        ID135_tree = None
        ARROW_LEFT136_tree = None
        NEWLINE138_tree = None
        ID139_tree = None
        ARROW_LEFT140_tree = None
        NEWLINE141_tree = None
        INDENT142_tree = None
        NEWLINE143_tree = None
        NEWLINE145_tree = None
        DEDENT146_tree = None
        NEWLINE147_tree = None
        ARROW_RIGHT149_tree = None
        ID150_tree = None
        NEWLINE151_tree = None
        ARROW_RIGHT153_tree = None
        NEWLINE154_tree = None
        INDENT155_tree = None
        NEWLINE156_tree = None
        ID157_tree = None
        NEWLINE158_tree = None
        DEDENT159_tree = None
        NEWLINE160_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:121:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt31 = 4
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:121:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:121:9: ( ID )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == ID) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:121:9: ID
                            pass 
                            ID135 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1282) 
                            stream_ID.add(ID135)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    ARROW_LEFT136 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1286) 
                    stream_ARROW_LEFT.add(ARROW_LEFT136)


                    # grammar/ShyRecognizerFrontend.g:121:25: ( arbitrary_value )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER or LA22_0 == STRING) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:121:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1288)
                            arbitrary_value137 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value137.tree)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    NEWLINE138 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1292) 
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
                    # 122:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:122:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:122:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:123:42: ( ID )+
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
                    # grammar/ShyRecognizerFrontend.g:124:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:124:9: ( ID )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if (LA23_0 == ID) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:124:9: ID
                            pass 
                            ID139 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1345) 
                            stream_ID.add(ID139)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    ARROW_LEFT140 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1349) 
                    stream_ARROW_LEFT.add(ARROW_LEFT140)


                    NEWLINE141 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1351) 
                    stream_NEWLINE.add(NEWLINE141)


                    INDENT142 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1353) 
                    stream_INDENT.add(INDENT142)


                    NEWLINE143 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1355) 
                    stream_NEWLINE.add(NEWLINE143)


                    # grammar/ShyRecognizerFrontend.g:125:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER or LA25_0 == STRING) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:125:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:125:11: ( arbitrary_value )+
                            cnt24 = 0
                            while True: #loop24
                                alt24 = 2
                                LA24_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER or LA24_0 == STRING) :
                                    alt24 = 1


                                if alt24 == 1:
                                    # grammar/ShyRecognizerFrontend.g:125:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1367)
                                    arbitrary_value144 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value144.tree)



                                else:
                                    if cnt24 >= 1:
                                        break #loop24

                                    eee = EarlyExitException(24, self.input)
                                    raise eee

                                cnt24 += 1


                            NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1371) 
                            stream_NEWLINE.add(NEWLINE145)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    DEDENT146 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1377) 
                    stream_DEDENT.add(DEDENT146)


                    NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1379) 
                    stream_NEWLINE.add(NEWLINE147)


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
                    # 126:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:126:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:126:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:127:42: ( ID )+
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
                    # grammar/ShyRecognizerFrontend.g:128:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:128:9: ( arbitrary_value )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA26_0 <= ID) or LA26_0 == MINUS or LA26_0 == NUMBER or LA26_0 == STRING) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:128:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1432)
                            arbitrary_value148 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value148.tree)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


                    ARROW_RIGHT149 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1436) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT149)


                    # grammar/ShyRecognizerFrontend.g:128:39: ( ID )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == ID) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:128:39: ID
                            pass 
                            ID150 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1438) 
                            stream_ID.add(ID150)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1442) 
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




                elif alt31 == 4:
                    # grammar/ShyRecognizerFrontend.g:131:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:131:9: ( arbitrary_value )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA28_0 <= ID) or LA28_0 == MINUS or LA28_0 == NUMBER or LA28_0 == STRING) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:131:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1495)
                            arbitrary_value152 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value152.tree)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    ARROW_RIGHT153 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1499) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT153)


                    NEWLINE154 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1501) 
                    stream_NEWLINE.add(NEWLINE154)


                    INDENT155 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1503) 
                    stream_INDENT.add(INDENT155)


                    NEWLINE156 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1505) 
                    stream_NEWLINE.add(NEWLINE156)


                    # grammar/ShyRecognizerFrontend.g:132:9: ( ( ID )+ NEWLINE )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == ID) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:132:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:132:11: ( ID )+
                            cnt29 = 0
                            while True: #loop29
                                alt29 = 2
                                LA29_0 = self.input.LA(1)

                                if (LA29_0 == ID) :
                                    alt29 = 1


                                if alt29 == 1:
                                    # grammar/ShyRecognizerFrontend.g:132:11: ID
                                    pass 
                                    ID157 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1517) 
                                    stream_ID.add(ID157)



                                else:
                                    if cnt29 >= 1:
                                        break #loop29

                                    eee = EarlyExitException(29, self.input)
                                    raise eee

                                cnt29 += 1


                            NEWLINE158 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1521) 
                            stream_NEWLINE.add(NEWLINE158)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


                    DEDENT159 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1527) 
                    stream_DEDENT.add(DEDENT159)


                    NEWLINE160 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1529) 
                    stream_NEWLINE.add(NEWLINE160)


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
                    # 133:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:133:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:133:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:134:42: ( ID )+
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
    # grammar/ShyRecognizerFrontend.g:137:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE161 = None
        NEWLINE163 = None
        DO164 = None
        NEWLINE165 = None
        INDENT166 = None
        NEWLINE167 = None
        DEDENT169 = None
        NEWLINE170 = None
        condition162 = None

        statements168 = None


        WHILE161_tree = None
        NEWLINE163_tree = None
        DO164_tree = None
        NEWLINE165_tree = None
        INDENT166_tree = None
        NEWLINE167_tree = None
        DEDENT169_tree = None
        NEWLINE170_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:138:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:138:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE161 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1591) 
                stream_WHILE.add(WHILE161)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1593)
                condition162 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition162.tree)


                # grammar/ShyRecognizerFrontend.g:138:25: ( NEWLINE )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == NEWLINE) :
                    alt32 = 1
                if alt32 == 1:
                    # grammar/ShyRecognizerFrontend.g:138:25: NEWLINE
                    pass 
                    NEWLINE163 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1595) 
                    stream_NEWLINE.add(NEWLINE163)





                DO164 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1599) 
                stream_DO.add(DO164)


                NEWLINE165 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1601) 
                stream_NEWLINE.add(NEWLINE165)


                INDENT166 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1615) 
                stream_INDENT.add(INDENT166)


                NEWLINE167 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1617) 
                stream_NEWLINE.add(NEWLINE167)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1619)
                statements168 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements168.tree)


                DEDENT169 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1621) 
                stream_DEDENT.add(DEDENT169)


                NEWLINE170 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1623) 
                stream_NEWLINE.add(NEWLINE170)


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
                # 140:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:140:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:143:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head171 = None

        statement_elif172 = None

        statement_else173 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:144:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:144:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1663)
                statement_if_head171 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head171.tree)


                # grammar/ShyRecognizerFrontend.g:145:9: ( statement_elif )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == ELIF) :
                        alt33 = 1


                    if alt33 == 1:
                        # grammar/ShyRecognizerFrontend.g:145:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1673)
                        statement_elif172 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif172.tree)



                    else:
                        break #loop33


                # grammar/ShyRecognizerFrontend.g:146:9: ( statement_else )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == ELSE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:146:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1685)
                    statement_else173 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else173.tree)





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
                # 147:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:147:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:149:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:150:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:154:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF174 = None
        statement_elif_body175 = None


        IF174_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:155:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:155:9: IF statement_elif_body
                pass 
                IF174 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1793) 
                stream_IF.add(IF174)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1795)
                statement_elif_body175 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body175.tree)


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
                # 156:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:159:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF176 = None
        statement_elif_body177 = None


        ELIF176_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:160:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:160:9: ELIF statement_elif_body
                pass 
                ELIF176 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1827) 
                stream_ELIF.add(ELIF176)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1829)
                statement_elif_body177 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body177.tree)


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

    # $ANTLR end "statement_elif"


    class statement_elif_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_elif_body_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_elif_body"
    # grammar/ShyRecognizerFrontend.g:164:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE179 = None
        DO180 = None
        NEWLINE181 = None
        INDENT182 = None
        NEWLINE183 = None
        DEDENT185 = None
        NEWLINE186 = None
        condition178 = None

        statements184 = None


        NEWLINE179_tree = None
        DO180_tree = None
        NEWLINE181_tree = None
        INDENT182_tree = None
        NEWLINE183_tree = None
        DEDENT185_tree = None
        NEWLINE186_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:165:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:165:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1861)
                condition178 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition178.tree)


                # grammar/ShyRecognizerFrontend.g:165:19: ( NEWLINE )?
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == NEWLINE) :
                    alt35 = 1
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:165:19: NEWLINE
                    pass 
                    NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1863) 
                    stream_NEWLINE.add(NEWLINE179)





                DO180 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1867) 
                stream_DO.add(DO180)


                NEWLINE181 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1869) 
                stream_NEWLINE.add(NEWLINE181)


                INDENT182 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1883) 
                stream_INDENT.add(INDENT182)


                NEWLINE183 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1885) 
                stream_NEWLINE.add(NEWLINE183)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1887)
                statements184 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements184.tree)


                DEDENT185 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1889) 
                stream_DEDENT.add(DEDENT185)


                NEWLINE186 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1891) 
                stream_NEWLINE.add(NEWLINE186)


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
                # 167:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:167:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:170:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE187 = None
        NEWLINE188 = None
        INDENT189 = None
        NEWLINE190 = None
        DEDENT192 = None
        NEWLINE193 = None
        statements191 = None


        ELSE187_tree = None
        NEWLINE188_tree = None
        INDENT189_tree = None
        NEWLINE190_tree = None
        DEDENT192_tree = None
        NEWLINE193_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:171:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:171:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE187 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1931) 
                stream_ELSE.add(ELSE187)


                NEWLINE188 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1933) 
                stream_NEWLINE.add(NEWLINE188)


                INDENT189 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1947) 
                stream_INDENT.add(INDENT189)


                NEWLINE190 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1949) 
                stream_NEWLINE.add(NEWLINE190)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1951)
                statements191 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements191.tree)


                DEDENT192 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1953) 
                stream_DEDENT.add(DEDENT192)


                NEWLINE193 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1955) 
                stream_NEWLINE.add(NEWLINE193)


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
                # 173:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:173:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:176:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY195 = None
        ALL197 = None
        condition_call194 = None

        condition_calls196 = None

        condition_calls198 = None


        ANY195_tree = None
        ALL197_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:177:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
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
                    # grammar/ShyRecognizerFrontend.g:177:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1993)
                    condition_call194 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call194.tree)


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
                    # 178:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:178:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt36 == 2:
                    # grammar/ShyRecognizerFrontend.g:179:9: ANY condition_calls
                    pass 
                    ANY195 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition2022) 
                    stream_ANY.add(ANY195)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2024)
                    condition_calls196 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls196.tree)


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
                    # 180:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:180:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt36 == 3:
                    # grammar/ShyRecognizerFrontend.g:181:9: ALL condition_calls
                    pass 
                    ALL197 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition2053) 
                    stream_ALL.add(ALL197)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition2055)
                    condition_calls198 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls198.tree)


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
                    # 182:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:182:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:185:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE200 = None
        INDENT201 = None
        NEWLINE202 = None
        DEDENT204 = None
        NEWLINE205 = None
        condition_call199 = None

        condition_call_line203 = None


        NEWLINE200_tree = None
        INDENT201_tree = None
        NEWLINE202_tree = None
        DEDENT204_tree = None
        NEWLINE205_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:186:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
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
                    # grammar/ShyRecognizerFrontend.g:186:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls2093)
                    condition_call199 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call199.tree)



                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:187:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE200 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2103) 
                    stream_NEWLINE.add(NEWLINE200)


                    INDENT201 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls2105) 
                    stream_INDENT.add(INDENT201)


                    NEWLINE202 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2107) 
                    stream_NEWLINE.add(NEWLINE202)


                    # grammar/ShyRecognizerFrontend.g:187:32: ( condition_call_line )+
                    cnt37 = 0
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == ID) :
                            alt37 = 1


                        if alt37 == 1:
                            # grammar/ShyRecognizerFrontend.g:187:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls2109)
                            condition_call_line203 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line203.tree)



                        else:
                            if cnt37 >= 1:
                                break #loop37

                            eee = EarlyExitException(37, self.input)
                            raise eee

                        cnt37 += 1


                    DEDENT204 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls2113) 
                    stream_DEDENT.add(DEDENT204)


                    NEWLINE205 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2115) 
                    stream_NEWLINE.add(NEWLINE205)


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
                    # 188:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:188:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:191:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line206 = None

        statement_call_multi_line207 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:192:5: ( statement_call_single_line | statement_call_multi_line )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:192:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call2149)
                    statement_call_single_line206 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line206.tree)



                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:193:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call2159)
                    statement_call_multi_line207 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line207.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:196:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE209 = None
        statement_call_single_line208 = None

        statement_call_multi_line210 = None


        NEWLINE209_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:197:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt40 = 2
                alt40 = self.dfa40.predict(self.input)
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:197:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line2178)
                    statement_call_single_line208 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line208.tree)


                    NEWLINE209 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line2180) 
                    stream_NEWLINE.add(NEWLINE209)


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
                    # 198:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt40 == 2:
                    # grammar/ShyRecognizerFrontend.g:199:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2206)
                    statement_call_multi_line210 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line210.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:202:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID211 = None
        statement_call_args212 = None


        ID211_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:203:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:203:9: ID ( statement_call_args )?
                pass 
                ID211 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2225) 
                stream_ID.add(ID211)


                # grammar/ShyRecognizerFrontend.g:203:12: ( statement_call_args )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if ((EXPRESSION <= LA41_0 <= ID) or LA41_0 == MINUS or LA41_0 == NUMBER or LA41_0 == STRING) :
                    alt41 = 1
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:203:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2227)
                    statement_call_args212 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args212.tree)





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
                # 204:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:204:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:204:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:207:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID213 = None
        NEWLINE215 = None
        INDENT216 = None
        NEWLINE217 = None
        NEWLINE219 = None
        DEDENT220 = None
        NEWLINE221 = None
        statement_call_args214 = None

        statement_call_args218 = None


        ID213_tree = None
        NEWLINE215_tree = None
        INDENT216_tree = None
        NEWLINE217_tree = None
        NEWLINE219_tree = None
        DEDENT220_tree = None
        NEWLINE221_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:208:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:208:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID213 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2271) 
                stream_ID.add(ID213)


                # grammar/ShyRecognizerFrontend.g:208:12: ( statement_call_args )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if ((EXPRESSION <= LA42_0 <= ID) or LA42_0 == MINUS or LA42_0 == NUMBER or LA42_0 == STRING) :
                    alt42 = 1
                if alt42 == 1:
                    # grammar/ShyRecognizerFrontend.g:208:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2273)
                    statement_call_args214 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args214.tree)





                NEWLINE215 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2277) 
                stream_NEWLINE.add(NEWLINE215)


                INDENT216 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2287) 
                stream_INDENT.add(INDENT216)


                NEWLINE217 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2289) 
                stream_NEWLINE.add(NEWLINE217)


                # grammar/ShyRecognizerFrontend.g:209:24: ( statement_call_args NEWLINE )+
                cnt43 = 0
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER or LA43_0 == STRING) :
                        alt43 = 1


                    if alt43 == 1:
                        # grammar/ShyRecognizerFrontend.g:209:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2293)
                        statement_call_args218 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args218.tree)


                        NEWLINE219 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2295) 
                        stream_NEWLINE.add(NEWLINE219)



                    else:
                        if cnt43 >= 1:
                            break #loop43

                        eee = EarlyExitException(43, self.input)
                        raise eee

                    cnt43 += 1


                DEDENT220 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2301) 
                stream_DEDENT.add(DEDENT220)


                NEWLINE221 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2303) 
                stream_NEWLINE.add(NEWLINE221)


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
                # 210:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:210:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:210:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:213:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value222 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:213:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:213:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:213:23: ( arbitrary_value )+
                cnt44 = 0
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA44_0 <= ID) or LA44_0 == MINUS or LA44_0 == NUMBER or LA44_0 == STRING) :
                        alt44 = 1


                    if alt44 == 1:
                        # grammar/ShyRecognizerFrontend.g:213:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2339)
                        arbitrary_value222 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value222.tree)



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


    class arbitrary_value_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.arbitrary_value_return, self).__init__()

            self.tree = None





    # $ANTLR start "arbitrary_value"
    # grammar/ShyRecognizerFrontend.g:215:1: arbitrary_value : ( ID | EXPRESSION | STRING | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID223 = None
        EXPRESSION224 = None
        STRING225 = None
        num_whole226 = None

        num_fract227 = None


        ID223_tree = None
        EXPRESSION224_tree = None
        STRING225_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:216:5: ( ID | EXPRESSION | STRING | num_whole | num_fract )
                alt45 = 5
                LA45 = self.input.LA(1)
                if LA45 == ID:
                    alt45 = 1
                elif LA45 == EXPRESSION:
                    alt45 = 2
                elif LA45 == STRING:
                    alt45 = 3
                elif LA45 == MINUS:
                    LA45_4 = self.input.LA(2)

                    if (LA45_4 == NUMBER) :
                        LA45_5 = self.input.LA(3)

                        if (LA45_5 == DIVIDE) :
                            alt45 = 5
                        elif (LA45_5 == ARROW_RIGHT or LA45_5 == DO or (EXPRESSION <= LA45_5 <= ID) or LA45_5 == MINUS or (NEWLINE <= LA45_5 <= NUMBER) or LA45_5 == STRING) :
                            alt45 = 4
                        else:
                            nvae = NoViableAltException("", 45, 5, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 45, 4, self.input)

                        raise nvae


                elif LA45 == NUMBER:
                    LA45_5 = self.input.LA(2)

                    if (LA45_5 == DIVIDE) :
                        alt45 = 5
                    elif (LA45_5 == ARROW_RIGHT or LA45_5 == DO or (EXPRESSION <= LA45_5 <= ID) or LA45_5 == MINUS or (NEWLINE <= LA45_5 <= NUMBER) or LA45_5 == STRING) :
                        alt45 = 4
                    else:
                        nvae = NoViableAltException("", 45, 5, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 45, 0, self.input)

                    raise nvae


                if alt45 == 1:
                    # grammar/ShyRecognizerFrontend.g:216:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID223 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2356)
                    ID223_tree = self._adaptor.createWithPayload(ID223)
                    self._adaptor.addChild(root_0, ID223_tree)




                elif alt45 == 2:
                    # grammar/ShyRecognizerFrontend.g:217:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION224 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2366)
                    EXPRESSION224_tree = self._adaptor.createWithPayload(EXPRESSION224)
                    self._adaptor.addChild(root_0, EXPRESSION224_tree)




                elif alt45 == 3:
                    # grammar/ShyRecognizerFrontend.g:218:9: STRING
                    pass 
                    root_0 = self._adaptor.nil()


                    STRING225 = self.match(self.input, STRING, self.FOLLOW_STRING_in_arbitrary_value2376)
                    STRING225_tree = self._adaptor.createWithPayload(STRING225)
                    self._adaptor.addChild(root_0, STRING225_tree)




                elif alt45 == 4:
                    # grammar/ShyRecognizerFrontend.g:219:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2386)
                    num_whole226 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole226.tree)



                elif alt45 == 5:
                    # grammar/ShyRecognizerFrontend.g:220:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2396)
                    num_fract227 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract227.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:223:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS228 = None
        ID229 = None
        NEWLINE230 = None
        INDENT231 = None
        NEWLINE232 = None
        DEDENT234 = None
        NEWLINE235 = None
        consts_items233 = None


        CONSTS228_tree = None
        ID229_tree = None
        NEWLINE230_tree = None
        INDENT231_tree = None
        NEWLINE232_tree = None
        DEDENT234_tree = None
        NEWLINE235_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:224:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:224:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS228 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2415) 
                stream_CONSTS.add(CONSTS228)


                ID229 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2417) 
                stream_ID.add(ID229)


                NEWLINE230 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2419) 
                stream_NEWLINE.add(NEWLINE230)


                INDENT231 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2429) 
                stream_INDENT.add(INDENT231)


                NEWLINE232 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2431) 
                stream_NEWLINE.add(NEWLINE232)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2433)
                consts_items233 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items233.tree)


                DEDENT234 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2435) 
                stream_DEDENT.add(DEDENT234)


                NEWLINE235 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2437) 
                stream_NEWLINE.add(NEWLINE235)


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
                # 226:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:226:13: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:228:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item236 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:228:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:228:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:228:16: ( consts_item )+
                cnt46 = 0
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == ID) :
                        alt46 = 1


                    if alt46 == 1:
                        # grammar/ShyRecognizerFrontend.g:228:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2470)
                        consts_item236 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item236.tree)



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

    # $ANTLR end "consts_items"


    class consts_item_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.consts_item_return, self).__init__()

            self.tree = None





    # $ANTLR start "consts_item"
    # grammar/ShyRecognizerFrontend.g:229:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID237 = None
        NEWLINE239 = None
        ID240 = None
        NEWLINE242 = None
        ID243 = None
        EXPRESSION244 = None
        NEWLINE245 = None
        num_whole238 = None

        num_fract241 = None


        ID237_tree = None
        NEWLINE239_tree = None
        ID240_tree = None
        NEWLINE242_tree = None
        ID243_tree = None
        EXPRESSION244_tree = None
        NEWLINE245_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:230:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt47 = 3
                LA47_0 = self.input.LA(1)

                if (LA47_0 == ID) :
                    LA47 = self.input.LA(2)
                    if LA47 == EXPRESSION:
                        alt47 = 3
                    elif LA47 == MINUS:
                        LA47_3 = self.input.LA(3)

                        if (LA47_3 == NUMBER) :
                            LA47_4 = self.input.LA(4)

                            if (LA47_4 == DIVIDE) :
                                alt47 = 2
                            elif (LA47_4 == NEWLINE) :
                                alt47 = 1
                            else:
                                nvae = NoViableAltException("", 47, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 47, 3, self.input)

                            raise nvae


                    elif LA47 == NUMBER:
                        LA47_4 = self.input.LA(3)

                        if (LA47_4 == DIVIDE) :
                            alt47 = 2
                        elif (LA47_4 == NEWLINE) :
                            alt47 = 1
                        else:
                            nvae = NoViableAltException("", 47, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 47, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 47, 0, self.input)

                    raise nvae


                if alt47 == 1:
                    # grammar/ShyRecognizerFrontend.g:230:9: ID num_whole NEWLINE
                    pass 
                    ID237 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2486) 
                    stream_ID.add(ID237)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2488)
                    num_whole238 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole238.tree)


                    NEWLINE239 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2490) 
                    stream_NEWLINE.add(NEWLINE239)


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
                    # 230:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:230:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt47 == 2:
                    # grammar/ShyRecognizerFrontend.g:231:9: ID num_fract NEWLINE
                    pass 
                    ID240 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2512) 
                    stream_ID.add(ID240)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2514)
                    num_fract241 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract241.tree)


                    NEWLINE242 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2516) 
                    stream_NEWLINE.add(NEWLINE242)


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
                    # 231:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:231:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt47 == 3:
                    # grammar/ShyRecognizerFrontend.g:232:9: ID EXPRESSION NEWLINE
                    pass 
                    ID243 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2538) 
                    stream_ID.add(ID243)


                    EXPRESSION244 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2540) 
                    stream_EXPRESSION.add(EXPRESSION244)


                    NEWLINE245 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2542) 
                    stream_NEWLINE.add(NEWLINE245)


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
                    # 232:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:232:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:235:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES246 = None
        ID247 = None
        NEWLINE248 = None
        INDENT249 = None
        NEWLINE250 = None
        DEDENT252 = None
        NEWLINE253 = None
        types_item251 = None


        TYPES246_tree = None
        ID247_tree = None
        NEWLINE248_tree = None
        INDENT249_tree = None
        NEWLINE250_tree = None
        DEDENT252_tree = None
        NEWLINE253_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:236:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:236:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES246 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2573) 
                stream_TYPES.add(TYPES246)


                ID247 = self.match(self.input, ID, self.FOLLOW_ID_in_types2575) 
                stream_ID.add(ID247)


                NEWLINE248 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2577) 
                stream_NEWLINE.add(NEWLINE248)


                INDENT249 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2587) 
                stream_INDENT.add(INDENT249)


                NEWLINE250 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2589) 
                stream_NEWLINE.add(NEWLINE250)


                # grammar/ShyRecognizerFrontend.g:237:24: ( types_item )+
                cnt48 = 0
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == ID) :
                        alt48 = 1


                    if alt48 == 1:
                        # grammar/ShyRecognizerFrontend.g:237:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2591)
                        types_item251 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item251.tree)



                    else:
                        if cnt48 >= 1:
                            break #loop48

                        eee = EarlyExitException(48, self.input)
                        raise eee

                    cnt48 += 1


                DEDENT252 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2595) 
                stream_DEDENT.add(DEDENT252)


                NEWLINE253 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2597) 
                stream_NEWLINE.add(NEWLINE253)


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
                # 238:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:238:13: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:238:30: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:240:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID254 = None
        attrs_hints255 = None


        ID254_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:240:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:240:14: ID attrs_hints
                pass 
                ID254 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2632) 
                stream_ID.add(ID254)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2634)
                attrs_hints255 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints255.tree)


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
                # 240:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:240:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:242:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES256 = None
        ID257 = None
        NEWLINE258 = None
        INDENT259 = None
        NEWLINE260 = None
        DEDENT262 = None
        NEWLINE263 = None
        messages_item261 = None


        MESSAGES256_tree = None
        ID257_tree = None
        NEWLINE258_tree = None
        INDENT259_tree = None
        NEWLINE260_tree = None
        DEDENT262_tree = None
        NEWLINE263_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:243:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:243:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES256 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2661) 
                stream_MESSAGES.add(MESSAGES256)


                ID257 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2663) 
                stream_ID.add(ID257)


                NEWLINE258 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2665) 
                stream_NEWLINE.add(NEWLINE258)


                INDENT259 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2675) 
                stream_INDENT.add(INDENT259)


                NEWLINE260 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2677) 
                stream_NEWLINE.add(NEWLINE260)


                # grammar/ShyRecognizerFrontend.g:244:24: ( messages_item )+
                cnt49 = 0
                while True: #loop49
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == ID) :
                        alt49 = 1


                    if alt49 == 1:
                        # grammar/ShyRecognizerFrontend.g:244:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2679)
                        messages_item261 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item261.tree)



                    else:
                        if cnt49 >= 1:
                            break #loop49

                        eee = EarlyExitException(49, self.input)
                        raise eee

                    cnt49 += 1


                DEDENT262 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2683) 
                stream_DEDENT.add(DEDENT262)


                NEWLINE263 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2685) 
                stream_NEWLINE.add(NEWLINE263)


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
                # 245:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:245:13: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:245:33: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:248:1: messages_item : ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) );
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID264 = None
        ID266 = None
        REPLY267 = None
        ID269 = None
        REQUEST270 = None
        ID272 = None
        NEWLINE273 = None
        INDENT274 = None
        NEWLINE275 = None
        REPLY276 = None
        DEDENT278 = None
        NEWLINE279 = None
        ID280 = None
        NEWLINE281 = None
        INDENT282 = None
        NEWLINE283 = None
        REQUEST284 = None
        DEDENT286 = None
        NEWLINE287 = None
        ID288 = None
        NEWLINE289 = None
        INDENT290 = None
        NEWLINE291 = None
        REQUEST292 = None
        REPLY294 = None
        DEDENT296 = None
        NEWLINE297 = None
        attrs_hints265 = None

        attrs_hints268 = None

        attrs_hints271 = None

        attrs_hints277 = None

        attrs_hints285 = None

        attrs_hints293 = None

        attrs_hints295 = None


        ID264_tree = None
        ID266_tree = None
        REPLY267_tree = None
        ID269_tree = None
        REQUEST270_tree = None
        ID272_tree = None
        NEWLINE273_tree = None
        INDENT274_tree = None
        NEWLINE275_tree = None
        REPLY276_tree = None
        DEDENT278_tree = None
        NEWLINE279_tree = None
        ID280_tree = None
        NEWLINE281_tree = None
        INDENT282_tree = None
        NEWLINE283_tree = None
        REQUEST284_tree = None
        DEDENT286_tree = None
        NEWLINE287_tree = None
        ID288_tree = None
        NEWLINE289_tree = None
        INDENT290_tree = None
        NEWLINE291_tree = None
        REQUEST292_tree = None
        REPLY294_tree = None
        DEDENT296_tree = None
        NEWLINE297_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_REQUEST = RewriteRuleTokenStream(self._adaptor, "token REQUEST")
        stream_REPLY = RewriteRuleTokenStream(self._adaptor, "token REPLY")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:249:5: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints ) | ID REPLY attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID REQUEST attrs_hints -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints ) | ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints ) )
                alt50 = 6
                alt50 = self.dfa50.predict(self.input)
                if alt50 == 1:
                    # grammar/ShyRecognizerFrontend.g:249:9: ID attrs_hints
                    pass 
                    ID264 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2727) 
                    stream_ID.add(ID264)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2729)
                    attrs_hints265 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints265.tree)


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
                    # 250:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:250:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_RECEIVE attrs_hints )
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




                elif alt50 == 2:
                    # grammar/ShyRecognizerFrontend.g:253:9: ID REPLY attrs_hints
                    pass 
                    ID266 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2790) 
                    stream_ID.add(ID266)


                    REPLY267 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2792) 
                    stream_REPLY.add(REPLY267)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2794)
                    attrs_hints268 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints268.tree)


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
                    # 254:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:254:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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




                elif alt50 == 3:
                    # grammar/ShyRecognizerFrontend.g:257:9: ID REQUEST attrs_hints
                    pass 
                    ID269 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2855) 
                    stream_ID.add(ID269)


                    REQUEST270 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item2857) 
                    stream_REQUEST.add(REQUEST270)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2859)
                    attrs_hints271 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints271.tree)


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
                    # 258:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:258:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
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




                elif alt50 == 4:
                    # grammar/ShyRecognizerFrontend.g:261:9: ID NEWLINE INDENT NEWLINE REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID272 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2920) 
                    stream_ID.add(ID272)


                    NEWLINE273 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2922) 
                    stream_NEWLINE.add(NEWLINE273)


                    INDENT274 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item2924) 
                    stream_INDENT.add(INDENT274)


                    NEWLINE275 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2926) 
                    stream_NEWLINE.add(NEWLINE275)


                    REPLY276 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item2928) 
                    stream_REPLY.add(REPLY276)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2930)
                    attrs_hints277 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints277.tree)


                    DEDENT278 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item2932) 
                    stream_DEDENT.add(DEDENT278)


                    NEWLINE279 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2934) 
                    stream_NEWLINE.add(NEWLINE279)


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
                    # 262:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:262:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REPLY attrs_hints )
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




                elif alt50 == 5:
                    # grammar/ShyRecognizerFrontend.g:265:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints DEDENT NEWLINE
                    pass 
                    ID280 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2995) 
                    stream_ID.add(ID280)


                    NEWLINE281 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item2997) 
                    stream_NEWLINE.add(NEWLINE281)


                    INDENT282 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item2999) 
                    stream_INDENT.add(INDENT282)


                    NEWLINE283 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3001) 
                    stream_NEWLINE.add(NEWLINE283)


                    REQUEST284 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3003) 
                    stream_REQUEST.add(REQUEST284)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3005)
                    attrs_hints285 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints285.tree)


                    DEDENT286 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3007) 
                    stream_DEDENT.add(DEDENT286)


                    NEWLINE287 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3009) 
                    stream_NEWLINE.add(NEWLINE287)


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
                    # 266:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:266:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints )
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




                elif alt50 == 6:
                    # grammar/ShyRecognizerFrontend.g:269:9: ID NEWLINE INDENT NEWLINE REQUEST attrs_hints REPLY attrs_hints DEDENT NEWLINE
                    pass 
                    ID288 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item3070) 
                    stream_ID.add(ID288)


                    NEWLINE289 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3072) 
                    stream_NEWLINE.add(NEWLINE289)


                    INDENT290 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages_item3074) 
                    stream_INDENT.add(INDENT290)


                    NEWLINE291 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3076) 
                    stream_NEWLINE.add(NEWLINE291)


                    REQUEST292 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_messages_item3090) 
                    stream_REQUEST.add(REQUEST292)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3092)
                    attrs_hints293 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints293.tree)


                    REPLY294 = self.match(self.input, REPLY, self.FOLLOW_REPLY_in_messages_item3106) 
                    stream_REPLY.add(REPLY294)


                    self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item3108)
                    attrs_hints295 = self.attrs_hints()

                    self._state.following.pop()
                    stream_attrs_hints.add(attrs_hints295.tree)


                    DEDENT296 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages_item3118) 
                    stream_DEDENT.add(DEDENT296)


                    NEWLINE297 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages_item3120) 
                    stream_NEWLINE.add(NEWLINE297)


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
                    # 273:9: -> ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
                    # grammar/ShyRecognizerFrontend.g:273:13: ^( TREE_MESSAGES_ITEM ID TREE_MESSAGES_ITEM_REQUEST attrs_hints TREE_MESSAGES_ITEM_REPLY attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:279:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS298 = None
        ID299 = None
        attrs_hints300 = None


        VARS298_tree = None
        ID299_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:280:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:280:9: VARS ID attrs_hints
                pass 
                VARS298 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars3210) 
                stream_VARS.add(VARS298)


                ID299 = self.match(self.input, ID, self.FOLLOW_ID_in_vars3212) 
                stream_ID.add(ID299)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars3214)
                attrs_hints300 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints300.tree)


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
                # 281:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:281:13: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:284:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE302 = None
        NEWLINE303 = None
        INDENT304 = None
        NEWLINE305 = None
        NEWLINE307 = None
        DEDENT308 = None
        NEWLINE309 = None
        NEWLINE311 = None
        INDENT312 = None
        NEWLINE313 = None
        NEWLINE315 = None
        DEDENT316 = None
        NEWLINE317 = None
        attr_hint301 = None

        attr_hint306 = None

        attr_hint310 = None

        attr_hint314 = None


        NEWLINE302_tree = None
        NEWLINE303_tree = None
        INDENT304_tree = None
        NEWLINE305_tree = None
        NEWLINE307_tree = None
        DEDENT308_tree = None
        NEWLINE309_tree = None
        NEWLINE311_tree = None
        INDENT312_tree = None
        NEWLINE313_tree = None
        NEWLINE315_tree = None
        DEDENT316_tree = None
        NEWLINE317_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:285:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt53 = 3
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # grammar/ShyRecognizerFrontend.g:285:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3254)
                    attr_hint301 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint301.tree)


                    NEWLINE302 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3256) 
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
                    # 286:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt53 == 2:
                    # grammar/ShyRecognizerFrontend.g:287:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE303 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3281) 
                    stream_NEWLINE.add(NEWLINE303)


                    # grammar/ShyRecognizerFrontend.g:288:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:288:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT304 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3293) 
                    stream_INDENT.add(INDENT304)


                    NEWLINE305 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3295) 
                    stream_NEWLINE.add(NEWLINE305)


                    # grammar/ShyRecognizerFrontend.g:288:26: ( attr_hint NEWLINE )+
                    cnt51 = 0
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == CURLY_OPEN or LA51_0 == ID) :
                            alt51 = 1


                        if alt51 == 1:
                            # grammar/ShyRecognizerFrontend.g:288:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3299)
                            attr_hint306 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint306.tree)


                            NEWLINE307 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3301) 
                            stream_NEWLINE.add(NEWLINE307)



                        else:
                            if cnt51 >= 1:
                                break #loop51

                            eee = EarlyExitException(51, self.input)
                            raise eee

                        cnt51 += 1


                    DEDENT308 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3307) 
                    stream_DEDENT.add(DEDENT308)


                    NEWLINE309 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3309) 
                    stream_NEWLINE.add(NEWLINE309)





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
                    # 289:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:289:30: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt53 == 3:
                    # grammar/ShyRecognizerFrontend.g:290:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3338)
                    attr_hint310 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint310.tree)


                    NEWLINE311 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3340) 
                    stream_NEWLINE.add(NEWLINE311)


                    # grammar/ShyRecognizerFrontend.g:291:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:291:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT312 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints3352) 
                    stream_INDENT.add(INDENT312)


                    NEWLINE313 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3354) 
                    stream_NEWLINE.add(NEWLINE313)


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
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints3358)
                            attr_hint314 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint314.tree)


                            NEWLINE315 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3360) 
                            stream_NEWLINE.add(NEWLINE315)



                        else:
                            if cnt52 >= 1:
                                break #loop52

                            eee = EarlyExitException(52, self.input)
                            raise eee

                        cnt52 += 1


                    DEDENT316 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints3366) 
                    stream_DEDENT.add(DEDENT316)


                    NEWLINE317 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints3368) 
                    stream_NEWLINE.add(NEWLINE317)





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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:294:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID318 = None
        ID320 = None
        NEWLINE322 = None
        INDENT323 = None
        NEWLINE324 = None
        ID325 = None
        NEWLINE326 = None
        DEDENT327 = None
        hint319 = None

        hint321 = None


        ID318_tree = None
        ID320_tree = None
        NEWLINE322_tree = None
        INDENT323_tree = None
        NEWLINE324_tree = None
        ID325_tree = None
        NEWLINE326_tree = None
        DEDENT327_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:295:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt58 = 3
                alt58 = self.dfa58.predict(self.input)
                if alt58 == 1:
                    # grammar/ShyRecognizerFrontend.g:295:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:295:9: ( ID )+
                    cnt54 = 0
                    while True: #loop54
                        alt54 = 2
                        LA54_0 = self.input.LA(1)

                        if (LA54_0 == ID) :
                            alt54 = 1


                        if alt54 == 1:
                            # grammar/ShyRecognizerFrontend.g:295:9: ID
                            pass 
                            ID318 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3406) 
                            stream_ID.add(ID318)



                        else:
                            if cnt54 >= 1:
                                break #loop54

                            eee = EarlyExitException(54, self.input)
                            raise eee

                        cnt54 += 1


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
                    # 296:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:296:13: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:296:46: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:296:46: ^( TREE_ATTR ID )
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




                elif alt58 == 2:
                    # grammar/ShyRecognizerFrontend.g:297:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3448)
                    hint319 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint319.tree)


                    # grammar/ShyRecognizerFrontend.g:297:14: ( ID )+
                    cnt55 = 0
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == ID) :
                            alt55 = 1


                        if alt55 == 1:
                            # grammar/ShyRecognizerFrontend.g:297:14: ID
                            pass 
                            ID320 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3450) 
                            stream_ID.add(ID320)



                        else:
                            if cnt55 >= 1:
                                break #loop55

                            eee = EarlyExitException(55, self.input)
                            raise eee

                        cnt55 += 1


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
                    # 298:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:298:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:298:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:298:36: ^( TREE_ATTR ID )
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




                elif alt58 == 3:
                    # grammar/ShyRecognizerFrontend.g:299:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint3491)
                    hint321 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint321.tree)


                    NEWLINE322 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3493) 
                    stream_NEWLINE.add(NEWLINE322)


                    INDENT323 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint3495) 
                    stream_INDENT.add(INDENT323)


                    NEWLINE324 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3497) 
                    stream_NEWLINE.add(NEWLINE324)


                    # grammar/ShyRecognizerFrontend.g:299:37: ( ( ID )+ NEWLINE )+
                    cnt57 = 0
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == ID) :
                            alt57 = 1


                        if alt57 == 1:
                            # grammar/ShyRecognizerFrontend.g:299:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:299:39: ( ID )+
                            cnt56 = 0
                            while True: #loop56
                                alt56 = 2
                                LA56_0 = self.input.LA(1)

                                if (LA56_0 == ID) :
                                    alt56 = 1


                                if alt56 == 1:
                                    # grammar/ShyRecognizerFrontend.g:299:39: ID
                                    pass 
                                    ID325 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint3501) 
                                    stream_ID.add(ID325)



                                else:
                                    if cnt56 >= 1:
                                        break #loop56

                                    eee = EarlyExitException(56, self.input)
                                    raise eee

                                cnt56 += 1


                            NEWLINE326 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint3505) 
                            stream_NEWLINE.add(NEWLINE326)



                        else:
                            if cnt57 >= 1:
                                break #loop57

                            eee = EarlyExitException(57, self.input)
                            raise eee

                        cnt57 += 1


                    DEDENT327 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint3511) 
                    stream_DEDENT.add(DEDENT327)


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
                    # 300:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:300:13: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:300:36: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:300:36: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:303:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN328 = None
        ID329 = None
        CURLY_CLOSE330 = None
        CURLY_OPEN331 = None
        ID332 = None
        CURLY_CLOSE334 = None
        hint_arg333 = None


        CURLY_OPEN328_tree = None
        ID329_tree = None
        CURLY_CLOSE330_tree = None
        CURLY_OPEN331_tree = None
        ID332_tree = None
        CURLY_CLOSE334_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:304:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == CURLY_OPEN) :
                    LA60_1 = self.input.LA(2)

                    if (LA60_1 == ID) :
                        LA60_2 = self.input.LA(3)

                        if (LA60_2 == CURLY_CLOSE) :
                            alt60 = 1
                        elif (LA60_2 == ID or LA60_2 == UNDERSCORE) :
                            alt60 = 2
                        else:
                            nvae = NoViableAltException("", 60, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 60, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 60, 0, self.input)

                    raise nvae


                if alt60 == 1:
                    # grammar/ShyRecognizerFrontend.g:304:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN328 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3559) 
                    stream_CURLY_OPEN.add(CURLY_OPEN328)


                    ID329 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3561) 
                    stream_ID.add(ID329)


                    CURLY_CLOSE330 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3563) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE330)


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
                    # 304:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:304:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt60 == 2:
                    # grammar/ShyRecognizerFrontend.g:305:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN331 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3583) 
                    stream_CURLY_OPEN.add(CURLY_OPEN331)


                    ID332 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3585) 
                    stream_ID.add(ID332)


                    # grammar/ShyRecognizerFrontend.g:305:23: ( hint_arg )+
                    cnt59 = 0
                    while True: #loop59
                        alt59 = 2
                        LA59_0 = self.input.LA(1)

                        if (LA59_0 == ID or LA59_0 == UNDERSCORE) :
                            alt59 = 1


                        if alt59 == 1:
                            # grammar/ShyRecognizerFrontend.g:305:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint3587)
                            hint_arg333 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg333.tree)



                        else:
                            if cnt59 >= 1:
                                break #loop59

                            eee = EarlyExitException(59, self.input)
                            raise eee

                        cnt59 += 1


                    CURLY_CLOSE334 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3591) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE334)


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
                    # 305:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:305:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:305:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:307:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set335 = None

        set335_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:307:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set335 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set335))

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
    # grammar/ShyRecognizerFrontend.g:309:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS336 = None
        NUMBER337 = None

        MINUS336_tree = None
        NUMBER337_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:309:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:309:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:309:13: ( MINUS )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == MINUS) :
                    alt61 = 1
                if alt61 == 1:
                    # grammar/ShyRecognizerFrontend.g:309:13: MINUS
                    pass 
                    MINUS336 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3630)
                    MINUS336_tree = self._adaptor.createWithPayload(MINUS336)
                    self._adaptor.addChild(root_0, MINUS336_tree)






                NUMBER337 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3634)
                NUMBER337_tree = self._adaptor.createWithPayload(NUMBER337)
                self._adaptor.addChild(root_0, NUMBER337_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:310:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS338 = None
        NUMBER339 = None
        DIVIDE340 = None
        NUMBER341 = None

        MINUS338_tree = None
        NUMBER339_tree = None
        DIVIDE340_tree = None
        NUMBER341_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:310:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:310:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:310:13: ( MINUS )?
                alt62 = 2
                LA62_0 = self.input.LA(1)

                if (LA62_0 == MINUS) :
                    alt62 = 1
                if alt62 == 1:
                    # grammar/ShyRecognizerFrontend.g:310:13: MINUS
                    pass 
                    MINUS338 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3642)
                    MINUS338_tree = self._adaptor.createWithPayload(MINUS338)
                    self._adaptor.addChild(root_0, MINUS338_tree)






                NUMBER339 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3646)
                NUMBER339_tree = self._adaptor.createWithPayload(NUMBER339)
                self._adaptor.addChild(root_0, NUMBER339_tree)



                DIVIDE340 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3648)
                DIVIDE340_tree = self._adaptor.createWithPayload(DIVIDE340)
                self._adaptor.addChild(root_0, DIVIDE340_tree)



                NUMBER341 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3650)
                NUMBER341_tree = self._adaptor.createWithPayload(NUMBER341)
                self._adaptor.addChild(root_0, NUMBER341_tree)





                retval.stop = self.input.LT(-1)


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
        u"\21\uffff"
        )

    DFA19_eof = DFA.unpack(
        u"\21\uffff"
        )

    DFA19_min = DFA.unpack(
        u"\1\22\1\7\4\uffff\1\7\2\10\1\33\1\10\1\15\1\10\1\33\2\uffff\1\10"
        )

    DFA19_max = DFA.unpack(
        u"\1\126\1\44\4\uffff\3\44\1\33\1\44\1\126\1\44\1\33\2\uffff\1\44"
        )

    DFA19_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\10\uffff\1\2\1\1\1\uffff"
        )

    DFA19_special = DFA.unpack(
        u"\21\uffff"
        )


    DFA19_transition = [
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
        DFA.unpack(u"\1\17\4\uffff\3\17\1\16\1\uffff\1\17\1\uffff\1\17\1"
        u"\uffff\1\17\2\uffff\2\17\2\uffff\1\17\1\uffff\1\17\57\uffff\1\17"
        u"\1\uffff\1\17"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\14\3\uffff\1\11\2\uffff\1\13\1"
        u"\12\10\uffff\1\10"),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\14\3\uffff\1\11\2\uffff\1\13\1"
        u"\12\10\uffff\1\10")
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
        u"\4\44\1\33\2\44\1\32\1\44\1\33\4\uffff\1\44"
        )

    DFA31_accept = DFA.unpack(
        u"\12\uffff\1\2\1\1\1\4\1\3\1\uffff"
        )

    DFA31_special = DFA.unpack(
        u"\17\uffff"
        )


    DFA31_transition = [
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
        u"\1\23\4\44\1\33\1\44\1\25\1\uffff\1\33\1\uffff\1\44"
        )

    DFA39_accept = DFA.unpack(
        u"\10\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA39_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA39_transition = [
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
        u"\1\23\4\44\1\33\1\44\1\25\1\33\2\uffff\1\44"
        )

    DFA40_accept = DFA.unpack(
        u"\11\uffff\1\2\1\1\1\uffff"
        )

    DFA40_special = DFA.unpack(
        u"\14\uffff"
        )


    DFA40_transition = [
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

    # class definition for DFA #40

    class DFA40(DFA):
        pass


    # lookup tables for DFA #50

    DFA50_eot = DFA.unpack(
        u"\77\uffff"
        )

    DFA50_eof = DFA.unpack(
        u"\77\uffff"
        )

    DFA50_min = DFA.unpack(
        u"\1\23\1\14\2\uffff\1\25\1\uffff\1\32\1\14\1\uffff\1\14\2\23\1\25"
        u"\1\15\1\13\1\32\1\uffff\1\32\1\uffff\1\23\1\13\2\14\1\23\1\25\5"
        u"\23\1\32\1\14\1\13\1\14\1\13\1\23\1\32\1\23\1\13\1\32\1\23\1\13"
        u"\1\23\1\15\1\23\1\25\1\23\1\15\1\23\1\25\1\23\1\15\3\32\4\23\2"
        u"\15\2\32"
        )

    DFA50_max = DFA.unpack(
        u"\1\23\1\42\2\uffff\1\25\1\uffff\1\32\1\42\1\uffff\2\32\1\23\1\25"
        u"\1\41\1\122\1\32\1\uffff\1\32\1\uffff\1\32\1\122\2\23\1\32\1\25"
        u"\2\32\1\23\1\32\1\23\1\32\1\23\1\122\1\23\1\122\1\23\2\32\1\122"
        u"\2\32\1\122\1\32\1\41\1\32\1\25\1\32\1\41\1\32\1\25\1\32\1\23\3"
        u"\32\2\23\2\32\2\23\2\32"
        )

    DFA50_accept = DFA.unpack(
        u"\2\uffff\1\2\1\3\1\uffff\1\1\2\uffff\1\4\7\uffff\1\5\1\uffff\1"
        u"\6\54\uffff"
        )

    DFA50_special = DFA.unpack(
        u"\77\uffff"
        )


    DFA50_transition = [
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

    # class definition for DFA #50

    class DFA50(DFA):
        pass


    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA53_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA53_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA53_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\123\1\122\2\uffff\1\32\1\122\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA53_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA53_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA53_transition = [
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

    # class definition for DFA #53

    class DFA53(DFA):
        pass


    # lookup tables for DFA #58

    DFA58_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA58_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA58_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA58_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\122\1\32\1\122\2\uffff\1\32"
        )

    DFA58_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA58_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA58_transition = [
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

    # class definition for DFA #58

    class DFA58(DFA):
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
    FOLLOW_ID_in_request408 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statement_in_request410 = frozenset([1])
    FOLLOW_REQUEST_in_request447 = frozenset([19])
    FOLLOW_ID_in_request449 = frozenset([26])
    FOLLOW_NEWLINE_in_request451 = frozenset([21])
    FOLLOW_INDENT_in_request453 = frozenset([26])
    FOLLOW_NEWLINE_in_request455 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_request457 = frozenset([13])
    FOLLOW_DEDENT_in_request459 = frozenset([26])
    FOLLOW_NEWLINE_in_request461 = frozenset([1])
    FOLLOW_REQUEST_in_request492 = frozenset([19])
    FOLLOW_ID_in_request494 = frozenset([26])
    FOLLOW_NEWLINE_in_request496 = frozenset([21])
    FOLLOW_INDENT_in_request498 = frozenset([26])
    FOLLOW_NEWLINE_in_request500 = frozenset([13, 28, 83])
    FOLLOW_local_vars_in_request514 = frozenset([13, 28])
    FOLLOW_local_ops_in_request518 = frozenset([13])
    FOLLOW_DEDENT_in_request530 = frozenset([26])
    FOLLOW_NEWLINE_in_request532 = frozenset([1])
    FOLLOW_RECEIVE_in_receive578 = frozenset([19])
    FOLLOW_ID_in_receive580 = frozenset([26])
    FOLLOW_NEWLINE_in_receive582 = frozenset([1])
    FOLLOW_RECEIVE_in_receive611 = frozenset([19])
    FOLLOW_ID_in_receive613 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statement_in_receive615 = frozenset([1])
    FOLLOW_RECEIVE_in_receive652 = frozenset([19])
    FOLLOW_ID_in_receive654 = frozenset([26])
    FOLLOW_NEWLINE_in_receive656 = frozenset([21])
    FOLLOW_INDENT_in_receive658 = frozenset([26])
    FOLLOW_NEWLINE_in_receive660 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_receive662 = frozenset([13])
    FOLLOW_DEDENT_in_receive664 = frozenset([26])
    FOLLOW_NEWLINE_in_receive666 = frozenset([1])
    FOLLOW_RECEIVE_in_receive697 = frozenset([19])
    FOLLOW_ID_in_receive699 = frozenset([26])
    FOLLOW_NEWLINE_in_receive701 = frozenset([21])
    FOLLOW_INDENT_in_receive703 = frozenset([26])
    FOLLOW_NEWLINE_in_receive705 = frozenset([13, 28, 83])
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
    FOLLOW_NEWLINE_in_proc824 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_proc826 = frozenset([13])
    FOLLOW_DEDENT_in_proc828 = frozenset([26])
    FOLLOW_NEWLINE_in_proc830 = frozenset([1])
    FOLLOW_PROC_in_proc861 = frozenset([19])
    FOLLOW_ID_in_proc863 = frozenset([26])
    FOLLOW_NEWLINE_in_proc865 = frozenset([21])
    FOLLOW_INDENT_in_proc867 = frozenset([26])
    FOLLOW_NEWLINE_in_proc869 = frozenset([6, 13, 28, 83])
    FOLLOW_proc_args_in_proc883 = frozenset([13, 28, 83])
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
    FOLLOW_NEWLINE_in_local_ops1023 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_local_ops1025 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops1027 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops1029 = frozenset([1])
    FOLLOW_OPS_in_local_ops1051 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statement_in_local_ops1053 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement1091 = frozenset([26])
    FOLLOW_NEWLINE_in_statement1093 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement1119 = frozenset([1])
    FOLLOW_statement_if_in_statement1129 = frozenset([1])
    FOLLOW_statement_assign_in_statement1139 = frozenset([1])
    FOLLOW_statement_while_in_statement1149 = frozenset([1])
    FOLLOW_statement_with_in_statement1159 = frozenset([1])
    FOLLOW_statement_in_statements1178 = frozenset([1, 18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_WITH_in_statement_with1220 = frozenset([19])
    FOLLOW_ID_in_statement_with1222 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1224 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1234 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1236 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_with1238 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1240 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1242 = frozenset([1])
    FOLLOW_ID_in_statement_assign1282 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1286 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1288 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1292 = frozenset([1])
    FOLLOW_ID_in_statement_assign1345 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1349 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1351 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1353 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1355 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_arbitrary_value_in_statement_assign1367 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_NEWLINE_in_statement_assign1371 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_assign1377 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1379 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1432 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1436 = frozenset([19])
    FOLLOW_ID_in_statement_assign1438 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1442 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1495 = frozenset([8, 18, 19, 23, 27, 36])
    FOLLOW_ARROW_RIGHT_in_statement_assign1499 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1501 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1503 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1505 = frozenset([19])
    FOLLOW_ID_in_statement_assign1517 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1521 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1527 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1529 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1591 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1593 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1595 = frozenset([15])
    FOLLOW_DO_in_statement_while1599 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1601 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1615 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1617 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_while1619 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1621 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1623 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1663 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1673 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1685 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1793 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1795 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1827 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1829 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1861 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1863 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1867 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1869 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1883 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1885 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_elif_body1887 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1889 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1891 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1931 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1933 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1947 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1949 = frozenset([18, 19, 20, 23, 27, 36, 84, 86])
    FOLLOW_statements_in_statement_else1951 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1953 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1955 = frozenset([1])
    FOLLOW_condition_call_in_condition1993 = frozenset([1])
    FOLLOW_ANY_in_condition2022 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2024 = frozenset([1])
    FOLLOW_ALL_in_condition2053 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition2055 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls2093 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls2103 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls2105 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2107 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls2109 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls2113 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2115 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call2149 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call2159 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line2178 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line2180 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2206 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2225 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_single_line2227 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2271 = frozenset([18, 19, 23, 26, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2273 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2277 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2287 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2289 = frozenset([18, 19, 23, 27, 36])
    FOLLOW_statement_call_args_in_statement_call_multi_line2293 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2295 = frozenset([13, 18, 19, 23, 27, 36])
    FOLLOW_DEDENT_in_statement_call_multi_line2301 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2303 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2339 = frozenset([1, 18, 19, 23, 27, 36])
    FOLLOW_ID_in_arbitrary_value2356 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2366 = frozenset([1])
    FOLLOW_STRING_in_arbitrary_value2376 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2386 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2396 = frozenset([1])
    FOLLOW_CONSTS_in_consts2415 = frozenset([19])
    FOLLOW_ID_in_consts2417 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2419 = frozenset([21])
    FOLLOW_INDENT_in_consts2429 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2431 = frozenset([19])
    FOLLOW_consts_items_in_consts2433 = frozenset([13])
    FOLLOW_DEDENT_in_consts2435 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2437 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2470 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2486 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2488 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2490 = frozenset([1])
    FOLLOW_ID_in_consts_item2512 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2514 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2516 = frozenset([1])
    FOLLOW_ID_in_consts_item2538 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2540 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2542 = frozenset([1])
    FOLLOW_TYPES_in_types2573 = frozenset([19])
    FOLLOW_ID_in_types2575 = frozenset([26])
    FOLLOW_NEWLINE_in_types2577 = frozenset([21])
    FOLLOW_INDENT_in_types2587 = frozenset([26])
    FOLLOW_NEWLINE_in_types2589 = frozenset([19])
    FOLLOW_types_item_in_types2591 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2595 = frozenset([26])
    FOLLOW_NEWLINE_in_types2597 = frozenset([1])
    FOLLOW_ID_in_types_item2632 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2634 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2661 = frozenset([19])
    FOLLOW_ID_in_messages2663 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2665 = frozenset([21])
    FOLLOW_INDENT_in_messages2675 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2677 = frozenset([19])
    FOLLOW_messages_item_in_messages2679 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2683 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2685 = frozenset([1])
    FOLLOW_ID_in_messages_item2727 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2729 = frozenset([1])
    FOLLOW_ID_in_messages_item2790 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2792 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2794 = frozenset([1])
    FOLLOW_ID_in_messages_item2855 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item2857 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2859 = frozenset([1])
    FOLLOW_ID_in_messages_item2920 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2922 = frozenset([21])
    FOLLOW_INDENT_in_messages_item2924 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2926 = frozenset([33])
    FOLLOW_REPLY_in_messages_item2928 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2930 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item2932 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2934 = frozenset([1])
    FOLLOW_ID_in_messages_item2995 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item2997 = frozenset([21])
    FOLLOW_INDENT_in_messages_item2999 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3001 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3003 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3005 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3007 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3009 = frozenset([1])
    FOLLOW_ID_in_messages_item3070 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3072 = frozenset([21])
    FOLLOW_INDENT_in_messages_item3074 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3076 = frozenset([34])
    FOLLOW_REQUEST_in_messages_item3090 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3092 = frozenset([33])
    FOLLOW_REPLY_in_messages_item3106 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item3108 = frozenset([13])
    FOLLOW_DEDENT_in_messages_item3118 = frozenset([26])
    FOLLOW_NEWLINE_in_messages_item3120 = frozenset([1])
    FOLLOW_VARS_in_vars3210 = frozenset([19])
    FOLLOW_ID_in_vars3212 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars3214 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3254 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3256 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints3281 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3293 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3295 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3299 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3301 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3307 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3309 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints3338 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3340 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints3352 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3354 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints3358 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3360 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints3366 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints3368 = frozenset([1])
    FOLLOW_ID_in_attr_hint3406 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3448 = frozenset([19])
    FOLLOW_ID_in_attr_hint3450 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint3491 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3493 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint3495 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint3497 = frozenset([19])
    FOLLOW_ID_in_attr_hint3501 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint3505 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint3511 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3559 = frozenset([19])
    FOLLOW_ID_in_hint3561 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint3563 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3583 = frozenset([19])
    FOLLOW_ID_in_hint3585 = frozenset([19, 82])
    FOLLOW_hint_arg_in_hint3587 = frozenset([11, 19, 82])
    FOLLOW_CURLY_CLOSE_in_hint3591 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3630 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3634 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3642 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3646 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3648 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3650 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
