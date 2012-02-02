# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-02 18:53:47

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
                # elements: ID, module_queue, request, receive, proc
                # token labels: 
                # rule labels: retval
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
    # grammar/ShyRecognizerFrontend.g:69:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) );
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
        DEDENT64 = None
        NEWLINE65 = None
        proc_args61 = None

        local_vars62 = None

        local_ops63 = None


        PROC53_tree = None
        ID54_tree = None
        NEWLINE55_tree = None
        PROC56_tree = None
        ID57_tree = None
        NEWLINE58_tree = None
        INDENT59_tree = None
        NEWLINE60_tree = None
        DEDENT64_tree = None
        NEWLINE65_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_PROC = RewriteRuleTokenStream(self._adaptor, "token PROC")
        stream_proc_args = RewriteRuleSubtreeStream(self._adaptor, "rule proc_args")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:70:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == PROC) :
                    LA17_1 = self.input.LA(2)

                    if (LA17_1 == ID) :
                        LA17_2 = self.input.LA(3)

                        if (LA17_2 == NEWLINE) :
                            LA17_3 = self.input.LA(4)

                            if (LA17_3 == INDENT) :
                                alt17 = 2
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
                    # grammar/ShyRecognizerFrontend.g:72:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE
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


                    # grammar/ShyRecognizerFrontend.g:73:13: ( proc_args )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == ARGS) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:73:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc718)
                        proc_args61 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args61.tree)





                    # grammar/ShyRecognizerFrontend.g:73:25: ( local_vars )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == VARS) :
                        alt15 = 1
                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:73:25: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_proc722)
                        local_vars62 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars62.tree)





                    # grammar/ShyRecognizerFrontend.g:73:38: ( local_ops )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == OPS) :
                        alt16 = 1
                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:73:38: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_proc726)
                        local_ops63 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops63.tree)





                    DEDENT64 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc738) 
                    stream_DEDENT.add(DEDENT64)


                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc740) 
                    stream_NEWLINE.add(NEWLINE65)


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
                    # 75:9: -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:75:13: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:75:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:75:41: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:75:54: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:78:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS66 = None
        attrs_hints67 = None


        ARGS66_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:79:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:79:9: ARGS attrs_hints
                pass 
                ARGS66 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args790) 
                stream_ARGS.add(ARGS66)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args792)
                attrs_hints67 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints67.tree)


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
                # 79:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:79:29: ^( TREE_PROC_ARGS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:82:1: local_vars : VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        retval = self.local_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS68 = None
        attrs_hints69 = None


        VARS68_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:83:5: ( VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:83:9: VARS attrs_hints
                pass 
                VARS68 = self.match(self.input, VARS, self.FOLLOW_VARS_in_local_vars821) 
                stream_VARS.add(VARS68)


                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars823)
                attrs_hints69 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints69.tree)


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
                # 83:26: -> ^( TREE_LOCAL_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:83:29: ^( TREE_LOCAL_VARS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:86:1: local_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
    def local_ops(self, ):
        retval = self.local_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS70 = None
        NEWLINE71 = None
        INDENT72 = None
        NEWLINE73 = None
        DEDENT75 = None
        NEWLINE76 = None
        statements74 = None


        OPS70_tree = None
        NEWLINE71_tree = None
        INDENT72_tree = None
        NEWLINE73_tree = None
        DEDENT75_tree = None
        NEWLINE76_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:87:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
                # grammar/ShyRecognizerFrontend.g:87:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                OPS70 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops852) 
                stream_OPS.add(OPS70)


                NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops854) 
                stream_NEWLINE.add(NEWLINE71)


                INDENT72 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_local_ops856) 
                stream_INDENT.add(INDENT72)


                NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops858) 
                stream_NEWLINE.add(NEWLINE73)


                self._state.following.append(self.FOLLOW_statements_in_local_ops860)
                statements74 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements74.tree)


                DEDENT75 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_local_ops862) 
                stream_DEDENT.add(DEDENT75)


                NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops864) 
                stream_NEWLINE.add(NEWLINE76)


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
                # 88:9: -> statements
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
    # grammar/ShyRecognizerFrontend.g:91:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE78 = None
        statement_call_single_line77 = None

        statement_call_multi_line79 = None

        statement_if80 = None

        statement_assign81 = None

        statement_while82 = None

        statement_with83 = None


        NEWLINE78_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:92:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt18 = 6
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:92:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement895)
                    statement_call_single_line77 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line77.tree)


                    NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement897) 
                    stream_NEWLINE.add(NEWLINE78)


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
                    # 93:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:94:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement923)
                    statement_call_multi_line79 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line79.tree)



                elif alt18 == 3:
                    # grammar/ShyRecognizerFrontend.g:95:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement933)
                    statement_if80 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if80.tree)



                elif alt18 == 4:
                    # grammar/ShyRecognizerFrontend.g:96:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement943)
                    statement_assign81 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign81.tree)



                elif alt18 == 5:
                    # grammar/ShyRecognizerFrontend.g:97:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement953)
                    statement_while82 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while82.tree)



                elif alt18 == 6:
                    # grammar/ShyRecognizerFrontend.g:98:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement963)
                    statement_with83 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with83.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:101:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement84 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:102:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:102:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:102:9: ( statement )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA19_0 <= IF) or LA19_0 == MINUS or LA19_0 == NUMBER or LA19_0 == WHILE or LA19_0 == WITH) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerFrontend.g:102:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements982)
                        statement84 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement84.tree)



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
                # 103:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:103:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:103:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:106:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH85 = None
        ID86 = None
        NEWLINE87 = None
        INDENT88 = None
        NEWLINE89 = None
        DEDENT91 = None
        NEWLINE92 = None
        statements90 = None


        WITH85_tree = None
        ID86_tree = None
        NEWLINE87_tree = None
        INDENT88_tree = None
        NEWLINE89_tree = None
        DEDENT91_tree = None
        NEWLINE92_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:107:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:107:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH85 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1024) 
                stream_WITH.add(WITH85)


                ID86 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1026) 
                stream_ID.add(ID86)


                NEWLINE87 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1028) 
                stream_NEWLINE.add(NEWLINE87)


                INDENT88 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1038) 
                stream_INDENT.add(INDENT88)


                NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1040) 
                stream_NEWLINE.add(NEWLINE89)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1042)
                statements90 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements90.tree)


                DEDENT91 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1044) 
                stream_DEDENT.add(DEDENT91)


                NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1046) 
                stream_NEWLINE.add(NEWLINE92)


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
                # 109:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:109:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:112:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID93 = None
        ARROW_LEFT94 = None
        NEWLINE96 = None
        ID97 = None
        ARROW_LEFT98 = None
        NEWLINE99 = None
        INDENT100 = None
        NEWLINE101 = None
        NEWLINE103 = None
        DEDENT104 = None
        NEWLINE105 = None
        ARROW_RIGHT107 = None
        ID108 = None
        NEWLINE109 = None
        ARROW_RIGHT111 = None
        NEWLINE112 = None
        INDENT113 = None
        NEWLINE114 = None
        ID115 = None
        NEWLINE116 = None
        DEDENT117 = None
        NEWLINE118 = None
        arbitrary_value95 = None

        arbitrary_value102 = None

        arbitrary_value106 = None

        arbitrary_value110 = None


        ID93_tree = None
        ARROW_LEFT94_tree = None
        NEWLINE96_tree = None
        ID97_tree = None
        ARROW_LEFT98_tree = None
        NEWLINE99_tree = None
        INDENT100_tree = None
        NEWLINE101_tree = None
        NEWLINE103_tree = None
        DEDENT104_tree = None
        NEWLINE105_tree = None
        ARROW_RIGHT107_tree = None
        ID108_tree = None
        NEWLINE109_tree = None
        ARROW_RIGHT111_tree = None
        NEWLINE112_tree = None
        INDENT113_tree = None
        NEWLINE114_tree = None
        ID115_tree = None
        NEWLINE116_tree = None
        DEDENT117_tree = None
        NEWLINE118_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:113:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt30 = 4
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:113:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:113:9: ( ID )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == ID) :
                            alt20 = 1


                        if alt20 == 1:
                            # grammar/ShyRecognizerFrontend.g:113:9: ID
                            pass 
                            ID93 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1086) 
                            stream_ID.add(ID93)



                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


                    ARROW_LEFT94 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1090) 
                    stream_ARROW_LEFT.add(ARROW_LEFT94)


                    # grammar/ShyRecognizerFrontend.g:113:25: ( arbitrary_value )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:113:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1092)
                            arbitrary_value95 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value95.tree)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    NEWLINE96 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1096) 
                    stream_NEWLINE.add(NEWLINE96)


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
                    # 114:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:114:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:114:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:115:42: ( ID )+
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
                    # grammar/ShyRecognizerFrontend.g:116:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:116:9: ( ID )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == ID) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:116:9: ID
                            pass 
                            ID97 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1149) 
                            stream_ID.add(ID97)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    ARROW_LEFT98 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1153) 
                    stream_ARROW_LEFT.add(ARROW_LEFT98)


                    NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1155) 
                    stream_NEWLINE.add(NEWLINE99)


                    INDENT100 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1157) 
                    stream_INDENT.add(INDENT100)


                    NEWLINE101 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1159) 
                    stream_NEWLINE.add(NEWLINE101)


                    # grammar/ShyRecognizerFrontend.g:117:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:117:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:117:11: ( arbitrary_value )+
                            cnt23 = 0
                            while True: #loop23
                                alt23 = 2
                                LA23_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                                    alt23 = 1


                                if alt23 == 1:
                                    # grammar/ShyRecognizerFrontend.g:117:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1171)
                                    arbitrary_value102 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value102.tree)



                                else:
                                    if cnt23 >= 1:
                                        break #loop23

                                    eee = EarlyExitException(23, self.input)
                                    raise eee

                                cnt23 += 1


                            NEWLINE103 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1175) 
                            stream_NEWLINE.add(NEWLINE103)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    DEDENT104 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1181) 
                    stream_DEDENT.add(DEDENT104)


                    NEWLINE105 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1183) 
                    stream_NEWLINE.add(NEWLINE105)


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
                    # 118:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:118:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:118:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:119:42: ( ID )+
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
                    # grammar/ShyRecognizerFrontend.g:120:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:120:9: ( arbitrary_value )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:120:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1236)
                            arbitrary_value106 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value106.tree)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    ARROW_RIGHT107 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1240) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT107)


                    # grammar/ShyRecognizerFrontend.g:120:39: ( ID )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == ID) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:120:39: ID
                            pass 
                            ID108 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1242) 
                            stream_ID.add(ID108)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


                    NEWLINE109 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1246) 
                    stream_NEWLINE.add(NEWLINE109)


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
                    # 121:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:121:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:121:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:122:42: ( ID )+
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
                    # grammar/ShyRecognizerFrontend.g:123:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:123:9: ( arbitrary_value )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA27_0 <= ID) or LA27_0 == MINUS or LA27_0 == NUMBER) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:123:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1299)
                            arbitrary_value110 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value110.tree)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    ARROW_RIGHT111 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1303) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT111)


                    NEWLINE112 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1305) 
                    stream_NEWLINE.add(NEWLINE112)


                    INDENT113 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1307) 
                    stream_INDENT.add(INDENT113)


                    NEWLINE114 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1309) 
                    stream_NEWLINE.add(NEWLINE114)


                    # grammar/ShyRecognizerFrontend.g:124:9: ( ( ID )+ NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:124:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:124:11: ( ID )+
                            cnt28 = 0
                            while True: #loop28
                                alt28 = 2
                                LA28_0 = self.input.LA(1)

                                if (LA28_0 == ID) :
                                    alt28 = 1


                                if alt28 == 1:
                                    # grammar/ShyRecognizerFrontend.g:124:11: ID
                                    pass 
                                    ID115 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1321) 
                                    stream_ID.add(ID115)



                                else:
                                    if cnt28 >= 1:
                                        break #loop28

                                    eee = EarlyExitException(28, self.input)
                                    raise eee

                                cnt28 += 1


                            NEWLINE116 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1325) 
                            stream_NEWLINE.add(NEWLINE116)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT117 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1331) 
                    stream_DEDENT.add(DEDENT117)


                    NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1333) 
                    stream_NEWLINE.add(NEWLINE118)


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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:129:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE119 = None
        NEWLINE121 = None
        DO122 = None
        NEWLINE123 = None
        INDENT124 = None
        NEWLINE125 = None
        DEDENT127 = None
        NEWLINE128 = None
        condition120 = None

        statements126 = None


        WHILE119_tree = None
        NEWLINE121_tree = None
        DO122_tree = None
        NEWLINE123_tree = None
        INDENT124_tree = None
        NEWLINE125_tree = None
        DEDENT127_tree = None
        NEWLINE128_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:130:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:130:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE119 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1395) 
                stream_WHILE.add(WHILE119)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1397)
                condition120 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition120.tree)


                # grammar/ShyRecognizerFrontend.g:130:25: ( NEWLINE )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == NEWLINE) :
                    alt31 = 1
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:130:25: NEWLINE
                    pass 
                    NEWLINE121 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1399) 
                    stream_NEWLINE.add(NEWLINE121)





                DO122 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1403) 
                stream_DO.add(DO122)


                NEWLINE123 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1405) 
                stream_NEWLINE.add(NEWLINE123)


                INDENT124 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1419) 
                stream_INDENT.add(INDENT124)


                NEWLINE125 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1421) 
                stream_NEWLINE.add(NEWLINE125)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1423)
                statements126 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements126.tree)


                DEDENT127 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1425) 
                stream_DEDENT.add(DEDENT127)


                NEWLINE128 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1427) 
                stream_NEWLINE.add(NEWLINE128)


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
                # 132:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:132:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:135:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head129 = None

        statement_elif130 = None

        statement_else131 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:136:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:136:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1467)
                statement_if_head129 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head129.tree)


                # grammar/ShyRecognizerFrontend.g:137:9: ( statement_elif )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == ELIF) :
                        alt32 = 1


                    if alt32 == 1:
                        # grammar/ShyRecognizerFrontend.g:137:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1477)
                        statement_elif130 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif130.tree)



                    else:
                        break #loop32


                # grammar/ShyRecognizerFrontend.g:138:9: ( statement_else )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == ELSE) :
                    alt33 = 1
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:138:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1489)
                    statement_else131 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else131.tree)





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
                # 139:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:139:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:141:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:142:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:146:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF132 = None
        statement_elif_body133 = None


        IF132_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:147:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:147:9: IF statement_elif_body
                pass 
                IF132 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1597) 
                stream_IF.add(IF132)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1599)
                statement_elif_body133 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body133.tree)


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
                # 148:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:151:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF134 = None
        statement_elif_body135 = None


        ELIF134_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:152:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:152:9: ELIF statement_elif_body
                pass 
                ELIF134 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1631) 
                stream_ELIF.add(ELIF134)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1633)
                statement_elif_body135 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body135.tree)


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
                # 153:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:156:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE137 = None
        DO138 = None
        NEWLINE139 = None
        INDENT140 = None
        NEWLINE141 = None
        DEDENT143 = None
        NEWLINE144 = None
        condition136 = None

        statements142 = None


        NEWLINE137_tree = None
        DO138_tree = None
        NEWLINE139_tree = None
        INDENT140_tree = None
        NEWLINE141_tree = None
        DEDENT143_tree = None
        NEWLINE144_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:157:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:157:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1665)
                condition136 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition136.tree)


                # grammar/ShyRecognizerFrontend.g:157:19: ( NEWLINE )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == NEWLINE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:157:19: NEWLINE
                    pass 
                    NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1667) 
                    stream_NEWLINE.add(NEWLINE137)





                DO138 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1671) 
                stream_DO.add(DO138)


                NEWLINE139 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1673) 
                stream_NEWLINE.add(NEWLINE139)


                INDENT140 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1687) 
                stream_INDENT.add(INDENT140)


                NEWLINE141 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1689) 
                stream_NEWLINE.add(NEWLINE141)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1691)
                statements142 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements142.tree)


                DEDENT143 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1693) 
                stream_DEDENT.add(DEDENT143)


                NEWLINE144 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1695) 
                stream_NEWLINE.add(NEWLINE144)


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
                # 159:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:159:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:162:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE145 = None
        NEWLINE146 = None
        INDENT147 = None
        NEWLINE148 = None
        DEDENT150 = None
        NEWLINE151 = None
        statements149 = None


        ELSE145_tree = None
        NEWLINE146_tree = None
        INDENT147_tree = None
        NEWLINE148_tree = None
        DEDENT150_tree = None
        NEWLINE151_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:163:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:163:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE145 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1735) 
                stream_ELSE.add(ELSE145)


                NEWLINE146 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1737) 
                stream_NEWLINE.add(NEWLINE146)


                INDENT147 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1751) 
                stream_INDENT.add(INDENT147)


                NEWLINE148 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1753) 
                stream_NEWLINE.add(NEWLINE148)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1755)
                statements149 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements149.tree)


                DEDENT150 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1757) 
                stream_DEDENT.add(DEDENT150)


                NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1759) 
                stream_NEWLINE.add(NEWLINE151)


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
                # 165:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:165:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:168:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY153 = None
        ALL155 = None
        condition_call152 = None

        condition_calls154 = None

        condition_calls156 = None


        ANY153_tree = None
        ALL155_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:169:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
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
                    # grammar/ShyRecognizerFrontend.g:169:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1797)
                    condition_call152 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call152.tree)


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
                    # 170:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:170:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:171:9: ANY condition_calls
                    pass 
                    ANY153 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1826) 
                    stream_ANY.add(ANY153)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1828)
                    condition_calls154 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls154.tree)


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
                    # 172:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:172:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 3:
                    # grammar/ShyRecognizerFrontend.g:173:9: ALL condition_calls
                    pass 
                    ALL155 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1857) 
                    stream_ALL.add(ALL155)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1859)
                    condition_calls156 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls156.tree)


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
                    # 174:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:174:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:177:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE158 = None
        INDENT159 = None
        NEWLINE160 = None
        DEDENT162 = None
        NEWLINE163 = None
        condition_call157 = None

        condition_call_line161 = None


        NEWLINE158_tree = None
        INDENT159_tree = None
        NEWLINE160_tree = None
        DEDENT162_tree = None
        NEWLINE163_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:178:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
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
                    # grammar/ShyRecognizerFrontend.g:178:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1897)
                    condition_call157 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call157.tree)



                elif alt37 == 2:
                    # grammar/ShyRecognizerFrontend.g:179:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE158 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1907) 
                    stream_NEWLINE.add(NEWLINE158)


                    INDENT159 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1909) 
                    stream_INDENT.add(INDENT159)


                    NEWLINE160 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1911) 
                    stream_NEWLINE.add(NEWLINE160)


                    # grammar/ShyRecognizerFrontend.g:179:32: ( condition_call_line )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:179:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1913)
                            condition_call_line161 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line161.tree)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


                    DEDENT162 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1917) 
                    stream_DEDENT.add(DEDENT162)


                    NEWLINE163 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1919) 
                    stream_NEWLINE.add(NEWLINE163)


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
                    # 180:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:180:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:183:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line164 = None

        statement_call_multi_line165 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:184:5: ( statement_call_single_line | statement_call_multi_line )
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:184:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1953)
                    statement_call_single_line164 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line164.tree)



                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:185:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1963)
                    statement_call_multi_line165 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line165.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:188:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE167 = None
        statement_call_single_line166 = None

        statement_call_multi_line168 = None


        NEWLINE167_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:189:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:189:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1982)
                    statement_call_single_line166 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line166.tree)


                    NEWLINE167 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1984) 
                    stream_NEWLINE.add(NEWLINE167)


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
                    # 190:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:191:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2010)
                    statement_call_multi_line168 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line168.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:194:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID169 = None
        statement_call_args170 = None


        ID169_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:195:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:195:9: ID ( statement_call_args )?
                pass 
                ID169 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2029) 
                stream_ID.add(ID169)


                # grammar/ShyRecognizerFrontend.g:195:12: ( statement_call_args )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if ((EXPRESSION <= LA40_0 <= ID) or LA40_0 == MINUS or LA40_0 == NUMBER) :
                    alt40 = 1
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:195:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2031)
                    statement_call_args170 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args170.tree)





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
                # 196:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:196:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:196:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:199:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID171 = None
        NEWLINE173 = None
        INDENT174 = None
        NEWLINE175 = None
        NEWLINE177 = None
        DEDENT178 = None
        NEWLINE179 = None
        statement_call_args172 = None

        statement_call_args176 = None


        ID171_tree = None
        NEWLINE173_tree = None
        INDENT174_tree = None
        NEWLINE175_tree = None
        NEWLINE177_tree = None
        DEDENT178_tree = None
        NEWLINE179_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:200:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:200:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID171 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2075) 
                stream_ID.add(ID171)


                # grammar/ShyRecognizerFrontend.g:200:12: ( statement_call_args )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if ((EXPRESSION <= LA41_0 <= ID) or LA41_0 == MINUS or LA41_0 == NUMBER) :
                    alt41 = 1
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:200:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2077)
                    statement_call_args172 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args172.tree)





                NEWLINE173 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2081) 
                stream_NEWLINE.add(NEWLINE173)


                INDENT174 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2091) 
                stream_INDENT.add(INDENT174)


                NEWLINE175 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2093) 
                stream_NEWLINE.add(NEWLINE175)


                # grammar/ShyRecognizerFrontend.g:201:24: ( statement_call_args NEWLINE )+
                cnt42 = 0
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA42_0 <= ID) or LA42_0 == MINUS or LA42_0 == NUMBER) :
                        alt42 = 1


                    if alt42 == 1:
                        # grammar/ShyRecognizerFrontend.g:201:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2097)
                        statement_call_args176 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args176.tree)


                        NEWLINE177 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2099) 
                        stream_NEWLINE.add(NEWLINE177)



                    else:
                        if cnt42 >= 1:
                            break #loop42

                        eee = EarlyExitException(42, self.input)
                        raise eee

                    cnt42 += 1


                DEDENT178 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2105) 
                stream_DEDENT.add(DEDENT178)


                NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2107) 
                stream_NEWLINE.add(NEWLINE179)


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
                # 202:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:202:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:202:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:205:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value180 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:205:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:205:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:205:23: ( arbitrary_value )+
                cnt43 = 0
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER) :
                        alt43 = 1


                    if alt43 == 1:
                        # grammar/ShyRecognizerFrontend.g:205:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2143)
                        arbitrary_value180 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value180.tree)



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
    # grammar/ShyRecognizerFrontend.g:207:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID181 = None
        EXPRESSION182 = None
        num_whole183 = None

        num_fract184 = None


        ID181_tree = None
        EXPRESSION182_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:208:5: ( ID | EXPRESSION | num_whole | num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:208:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID181 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2160)
                    ID181_tree = self._adaptor.createWithPayload(ID181)
                    self._adaptor.addChild(root_0, ID181_tree)




                elif alt44 == 2:
                    # grammar/ShyRecognizerFrontend.g:209:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION182 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2170)
                    EXPRESSION182_tree = self._adaptor.createWithPayload(EXPRESSION182)
                    self._adaptor.addChild(root_0, EXPRESSION182_tree)




                elif alt44 == 3:
                    # grammar/ShyRecognizerFrontend.g:210:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2180)
                    num_whole183 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole183.tree)



                elif alt44 == 4:
                    # grammar/ShyRecognizerFrontend.g:211:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2190)
                    num_fract184 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract184.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:214:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS185 = None
        ID186 = None
        NEWLINE187 = None
        INDENT188 = None
        NEWLINE189 = None
        DEDENT191 = None
        NEWLINE192 = None
        consts_items190 = None


        CONSTS185_tree = None
        ID186_tree = None
        NEWLINE187_tree = None
        INDENT188_tree = None
        NEWLINE189_tree = None
        DEDENT191_tree = None
        NEWLINE192_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:215:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:215:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS185 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2209) 
                stream_CONSTS.add(CONSTS185)


                ID186 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2211) 
                stream_ID.add(ID186)


                NEWLINE187 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2213) 
                stream_NEWLINE.add(NEWLINE187)


                INDENT188 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2223) 
                stream_INDENT.add(INDENT188)


                NEWLINE189 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2225) 
                stream_NEWLINE.add(NEWLINE189)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2227)
                consts_items190 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items190.tree)


                DEDENT191 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2229) 
                stream_DEDENT.add(DEDENT191)


                NEWLINE192 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2231) 
                stream_NEWLINE.add(NEWLINE192)


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
                # 217:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:217:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:219:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item193 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:219:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:219:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:219:16: ( consts_item )+
                cnt45 = 0
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ID) :
                        alt45 = 1


                    if alt45 == 1:
                        # grammar/ShyRecognizerFrontend.g:219:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2263)
                        consts_item193 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item193.tree)



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
    # grammar/ShyRecognizerFrontend.g:220:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID194 = None
        NEWLINE196 = None
        ID197 = None
        NEWLINE199 = None
        ID200 = None
        EXPRESSION201 = None
        NEWLINE202 = None
        num_whole195 = None

        num_fract198 = None


        ID194_tree = None
        NEWLINE196_tree = None
        ID197_tree = None
        NEWLINE199_tree = None
        ID200_tree = None
        EXPRESSION201_tree = None
        NEWLINE202_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:221:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerFrontend.g:221:9: ID num_whole NEWLINE
                    pass 
                    ID194 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2279) 
                    stream_ID.add(ID194)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2281)
                    num_whole195 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole195.tree)


                    NEWLINE196 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2283) 
                    stream_NEWLINE.add(NEWLINE196)


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
                    # 221:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:221:33: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/ShyRecognizerFrontend.g:222:9: ID num_fract NEWLINE
                    pass 
                    ID197 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2305) 
                    stream_ID.add(ID197)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2307)
                    num_fract198 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract198.tree)


                    NEWLINE199 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2309) 
                    stream_NEWLINE.add(NEWLINE199)


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
                    # 222:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:222:33: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:223:9: ID EXPRESSION NEWLINE
                    pass 
                    ID200 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2331) 
                    stream_ID.add(ID200)


                    EXPRESSION201 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2333) 
                    stream_EXPRESSION.add(EXPRESSION201)


                    NEWLINE202 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2335) 
                    stream_NEWLINE.add(NEWLINE202)


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
                    # 223:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:223:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:226:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES203 = None
        ID204 = None
        NEWLINE205 = None
        INDENT206 = None
        NEWLINE207 = None
        DEDENT209 = None
        NEWLINE210 = None
        types_item208 = None


        TYPES203_tree = None
        ID204_tree = None
        NEWLINE205_tree = None
        INDENT206_tree = None
        NEWLINE207_tree = None
        DEDENT209_tree = None
        NEWLINE210_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:227:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:227:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES203 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2366) 
                stream_TYPES.add(TYPES203)


                ID204 = self.match(self.input, ID, self.FOLLOW_ID_in_types2368) 
                stream_ID.add(ID204)


                NEWLINE205 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2370) 
                stream_NEWLINE.add(NEWLINE205)


                INDENT206 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2380) 
                stream_INDENT.add(INDENT206)


                NEWLINE207 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2382) 
                stream_NEWLINE.add(NEWLINE207)


                # grammar/ShyRecognizerFrontend.g:228:24: ( types_item )+
                cnt47 = 0
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == ID) :
                        alt47 = 1


                    if alt47 == 1:
                        # grammar/ShyRecognizerFrontend.g:228:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2384)
                        types_item208 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item208.tree)



                    else:
                        if cnt47 >= 1:
                            break #loop47

                        eee = EarlyExitException(47, self.input)
                        raise eee

                    cnt47 += 1


                DEDENT209 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2388) 
                stream_DEDENT.add(DEDENT209)


                NEWLINE210 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2390) 
                stream_NEWLINE.add(NEWLINE210)


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
                # 229:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:229:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:229:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:231:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID211 = None
        attrs_hints212 = None


        ID211_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:231:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:231:14: ID attrs_hints
                pass 
                ID211 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2424) 
                stream_ID.add(ID211)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2426)
                attrs_hints212 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints212.tree)


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
                # 231:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:231:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:233:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES213 = None
        ID214 = None
        NEWLINE215 = None
        INDENT216 = None
        NEWLINE217 = None
        DEDENT219 = None
        NEWLINE220 = None
        messages_item218 = None


        MESSAGES213_tree = None
        ID214_tree = None
        NEWLINE215_tree = None
        INDENT216_tree = None
        NEWLINE217_tree = None
        DEDENT219_tree = None
        NEWLINE220_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:234:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:234:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES213 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2453) 
                stream_MESSAGES.add(MESSAGES213)


                ID214 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2455) 
                stream_ID.add(ID214)


                NEWLINE215 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2457) 
                stream_NEWLINE.add(NEWLINE215)


                INDENT216 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2467) 
                stream_INDENT.add(INDENT216)


                NEWLINE217 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2469) 
                stream_NEWLINE.add(NEWLINE217)


                # grammar/ShyRecognizerFrontend.g:235:24: ( messages_item )+
                cnt48 = 0
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == ID) :
                        alt48 = 1


                    if alt48 == 1:
                        # grammar/ShyRecognizerFrontend.g:235:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2471)
                        messages_item218 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item218.tree)



                    else:
                        if cnt48 >= 1:
                            break #loop48

                        eee = EarlyExitException(48, self.input)
                        raise eee

                    cnt48 += 1


                DEDENT219 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2475) 
                stream_DEDENT.add(DEDENT219)


                NEWLINE220 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2477) 
                stream_NEWLINE.add(NEWLINE220)


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
                # 236:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:236:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:236:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:238:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID221 = None
        attrs_hints222 = None


        ID221_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:238:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:238:17: ID attrs_hints
                pass 
                ID221 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2511) 
                stream_ID.add(ID221)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2513)
                attrs_hints222 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints222.tree)


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
                # 238:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:238:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:240:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS223 = None
        ID224 = None
        attrs_hints225 = None


        VARS223_tree = None
        ID224_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:241:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:241:9: VARS ID attrs_hints
                pass 
                VARS223 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars2540) 
                stream_VARS.add(VARS223)


                ID224 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2542) 
                stream_ID.add(ID224)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2544)
                attrs_hints225 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints225.tree)


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
                # 242:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:242:12: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:245:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE227 = None
        NEWLINE228 = None
        INDENT229 = None
        NEWLINE230 = None
        NEWLINE232 = None
        DEDENT233 = None
        NEWLINE234 = None
        NEWLINE236 = None
        INDENT237 = None
        NEWLINE238 = None
        NEWLINE240 = None
        DEDENT241 = None
        NEWLINE242 = None
        attr_hint226 = None

        attr_hint231 = None

        attr_hint235 = None

        attr_hint239 = None


        NEWLINE227_tree = None
        NEWLINE228_tree = None
        INDENT229_tree = None
        NEWLINE230_tree = None
        NEWLINE232_tree = None
        DEDENT233_tree = None
        NEWLINE234_tree = None
        NEWLINE236_tree = None
        INDENT237_tree = None
        NEWLINE238_tree = None
        NEWLINE240_tree = None
        DEDENT241_tree = None
        NEWLINE242_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:246:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt51 = 3
                alt51 = self.dfa51.predict(self.input)
                if alt51 == 1:
                    # grammar/ShyRecognizerFrontend.g:246:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2583)
                    attr_hint226 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint226.tree)


                    NEWLINE227 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2585) 
                    stream_NEWLINE.add(NEWLINE227)


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
                    # 247:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt51 == 2:
                    # grammar/ShyRecognizerFrontend.g:248:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE228 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2609) 
                    stream_NEWLINE.add(NEWLINE228)


                    # grammar/ShyRecognizerFrontend.g:249:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:249:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT229 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2621) 
                    stream_INDENT.add(INDENT229)


                    NEWLINE230 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2623) 
                    stream_NEWLINE.add(NEWLINE230)


                    # grammar/ShyRecognizerFrontend.g:249:26: ( attr_hint NEWLINE )+
                    cnt49 = 0
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == CURLY_OPEN or LA49_0 == ID) :
                            alt49 = 1


                        if alt49 == 1:
                            # grammar/ShyRecognizerFrontend.g:249:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2627)
                            attr_hint231 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint231.tree)


                            NEWLINE232 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2629) 
                            stream_NEWLINE.add(NEWLINE232)



                        else:
                            if cnt49 >= 1:
                                break #loop49

                            eee = EarlyExitException(49, self.input)
                            raise eee

                        cnt49 += 1


                    DEDENT233 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2635) 
                    stream_DEDENT.add(DEDENT233)


                    NEWLINE234 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2637) 
                    stream_NEWLINE.add(NEWLINE234)





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
                    # 250:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:250:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt51 == 3:
                    # grammar/ShyRecognizerFrontend.g:251:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2665)
                    attr_hint235 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint235.tree)


                    NEWLINE236 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2667) 
                    stream_NEWLINE.add(NEWLINE236)


                    # grammar/ShyRecognizerFrontend.g:252:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:252:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT237 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2679) 
                    stream_INDENT.add(INDENT237)


                    NEWLINE238 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2681) 
                    stream_NEWLINE.add(NEWLINE238)


                    # grammar/ShyRecognizerFrontend.g:252:26: ( attr_hint NEWLINE )+
                    cnt50 = 0
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == CURLY_OPEN or LA50_0 == ID) :
                            alt50 = 1


                        if alt50 == 1:
                            # grammar/ShyRecognizerFrontend.g:252:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2685)
                            attr_hint239 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint239.tree)


                            NEWLINE240 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2687) 
                            stream_NEWLINE.add(NEWLINE240)



                        else:
                            if cnt50 >= 1:
                                break #loop50

                            eee = EarlyExitException(50, self.input)
                            raise eee

                        cnt50 += 1


                    DEDENT241 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2693) 
                    stream_DEDENT.add(DEDENT241)


                    NEWLINE242 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2695) 
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
                    # 253:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:253:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:255:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID243 = None
        ID245 = None
        NEWLINE247 = None
        INDENT248 = None
        NEWLINE249 = None
        ID250 = None
        NEWLINE251 = None
        DEDENT252 = None
        hint244 = None

        hint246 = None


        ID243_tree = None
        ID245_tree = None
        NEWLINE247_tree = None
        INDENT248_tree = None
        NEWLINE249_tree = None
        ID250_tree = None
        NEWLINE251_tree = None
        DEDENT252_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:256:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt56 = 3
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # grammar/ShyRecognizerFrontend.g:256:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:256:9: ( ID )+
                    cnt52 = 0
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == ID) :
                            alt52 = 1


                        if alt52 == 1:
                            # grammar/ShyRecognizerFrontend.g:256:9: ID
                            pass 
                            ID243 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2732) 
                            stream_ID.add(ID243)



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
                    # 257:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:257:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:257:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:257:45: ^( TREE_ATTR ID )
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
                    # grammar/ShyRecognizerFrontend.g:258:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2773)
                    hint244 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint244.tree)


                    # grammar/ShyRecognizerFrontend.g:258:14: ( ID )+
                    cnt53 = 0
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == ID) :
                            alt53 = 1


                        if alt53 == 1:
                            # grammar/ShyRecognizerFrontend.g:258:14: ID
                            pass 
                            ID245 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2775) 
                            stream_ID.add(ID245)



                        else:
                            if cnt53 >= 1:
                                break #loop53

                            eee = EarlyExitException(53, self.input)
                            raise eee

                        cnt53 += 1


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
                    # 259:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:259:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:259:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:259:35: ^( TREE_ATTR ID )
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
                    # grammar/ShyRecognizerFrontend.g:260:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2815)
                    hint246 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint246.tree)


                    NEWLINE247 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2817) 
                    stream_NEWLINE.add(NEWLINE247)


                    INDENT248 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2819) 
                    stream_INDENT.add(INDENT248)


                    NEWLINE249 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2821) 
                    stream_NEWLINE.add(NEWLINE249)


                    # grammar/ShyRecognizerFrontend.g:260:37: ( ( ID )+ NEWLINE )+
                    cnt55 = 0
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == ID) :
                            alt55 = 1


                        if alt55 == 1:
                            # grammar/ShyRecognizerFrontend.g:260:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:260:39: ( ID )+
                            cnt54 = 0
                            while True: #loop54
                                alt54 = 2
                                LA54_0 = self.input.LA(1)

                                if (LA54_0 == ID) :
                                    alt54 = 1


                                if alt54 == 1:
                                    # grammar/ShyRecognizerFrontend.g:260:39: ID
                                    pass 
                                    ID250 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2825) 
                                    stream_ID.add(ID250)



                                else:
                                    if cnt54 >= 1:
                                        break #loop54

                                    eee = EarlyExitException(54, self.input)
                                    raise eee

                                cnt54 += 1


                            NEWLINE251 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2829) 
                            stream_NEWLINE.add(NEWLINE251)



                        else:
                            if cnt55 >= 1:
                                break #loop55

                            eee = EarlyExitException(55, self.input)
                            raise eee

                        cnt55 += 1


                    DEDENT252 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2835) 
                    stream_DEDENT.add(DEDENT252)


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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:264:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN253 = None
        ID254 = None
        CURLY_CLOSE255 = None
        CURLY_OPEN256 = None
        ID257 = None
        CURLY_CLOSE259 = None
        hint_arg258 = None


        CURLY_OPEN253_tree = None
        ID254_tree = None
        CURLY_CLOSE255_tree = None
        CURLY_OPEN256_tree = None
        ID257_tree = None
        CURLY_CLOSE259_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:265:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:265:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN253 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2882) 
                    stream_CURLY_OPEN.add(CURLY_OPEN253)


                    ID254 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2884) 
                    stream_ID.add(ID254)


                    CURLY_CLOSE255 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2886) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE255)


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
                    # 265:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:265:38: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:266:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN256 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2906) 
                    stream_CURLY_OPEN.add(CURLY_OPEN256)


                    ID257 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2908) 
                    stream_ID.add(ID257)


                    # grammar/ShyRecognizerFrontend.g:266:23: ( hint_arg )+
                    cnt57 = 0
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == ID or LA57_0 == UNDERSCORE) :
                            alt57 = 1


                        if alt57 == 1:
                            # grammar/ShyRecognizerFrontend.g:266:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2910)
                            hint_arg258 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg258.tree)



                        else:
                            if cnt57 >= 1:
                                break #loop57

                            eee = EarlyExitException(57, self.input)
                            raise eee

                        cnt57 += 1


                    CURLY_CLOSE259 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2914) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE259)


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
                    # 266:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:266:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:266:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:268:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set260 = None

        set260_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:268:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set260 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set260))

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
    # grammar/ShyRecognizerFrontend.g:270:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS261 = None
        NUMBER262 = None

        MINUS261_tree = None
        NUMBER262_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:270:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:270:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:270:13: ( MINUS )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == MINUS) :
                    alt59 = 1
                if alt59 == 1:
                    # grammar/ShyRecognizerFrontend.g:270:13: MINUS
                    pass 
                    MINUS261 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2953)
                    MINUS261_tree = self._adaptor.createWithPayload(MINUS261)
                    self._adaptor.addChild(root_0, MINUS261_tree)






                NUMBER262 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2957)
                NUMBER262_tree = self._adaptor.createWithPayload(NUMBER262)
                self._adaptor.addChild(root_0, NUMBER262_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:271:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS263 = None
        NUMBER264 = None
        DIVIDE265 = None
        NUMBER266 = None

        MINUS263_tree = None
        NUMBER264_tree = None
        DIVIDE265_tree = None
        NUMBER266_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:271:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:271:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:271:13: ( MINUS )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == MINUS) :
                    alt60 = 1
                if alt60 == 1:
                    # grammar/ShyRecognizerFrontend.g:271:13: MINUS
                    pass 
                    MINUS263 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2965)
                    MINUS263_tree = self._adaptor.createWithPayload(MINUS263)
                    self._adaptor.addChild(root_0, MINUS263_tree)






                NUMBER264 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2969)
                NUMBER264_tree = self._adaptor.createWithPayload(NUMBER264)
                self._adaptor.addChild(root_0, NUMBER264_tree)



                DIVIDE265 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2971)
                DIVIDE265_tree = self._adaptor.createWithPayload(DIVIDE265)
                self._adaptor.addChild(root_0, DIVIDE265_tree)



                NUMBER266 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2973)
                NUMBER266_tree = self._adaptor.createWithPayload(NUMBER266)
                self._adaptor.addChild(root_0, NUMBER266_tree)





                retval.stop = self.input.LT(-1)


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
    FOLLOW_NEWLINE_in_proc704 = frozenset([6, 13, 28, 78])
    FOLLOW_proc_args_in_proc718 = frozenset([13, 28, 78])
    FOLLOW_local_vars_in_proc722 = frozenset([13, 28])
    FOLLOW_local_ops_in_proc726 = frozenset([13])
    FOLLOW_DEDENT_in_proc738 = frozenset([26])
    FOLLOW_NEWLINE_in_proc740 = frozenset([1])
    FOLLOW_ARGS_in_proc_args790 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args792 = frozenset([1])
    FOLLOW_VARS_in_local_vars821 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_local_vars823 = frozenset([1])
    FOLLOW_OPS_in_local_ops852 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops854 = frozenset([21])
    FOLLOW_INDENT_in_local_ops856 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops858 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_local_ops860 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops862 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops864 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement895 = frozenset([26])
    FOLLOW_NEWLINE_in_statement897 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement923 = frozenset([1])
    FOLLOW_statement_if_in_statement933 = frozenset([1])
    FOLLOW_statement_assign_in_statement943 = frozenset([1])
    FOLLOW_statement_while_in_statement953 = frozenset([1])
    FOLLOW_statement_with_in_statement963 = frozenset([1])
    FOLLOW_statement_in_statements982 = frozenset([1, 18, 19, 20, 23, 27, 79, 81])
    FOLLOW_WITH_in_statement_with1024 = frozenset([19])
    FOLLOW_ID_in_statement_with1026 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1028 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1038 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1040 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_with1042 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1044 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1046 = frozenset([1])
    FOLLOW_ID_in_statement_assign1086 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1090 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign1092 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign1096 = frozenset([1])
    FOLLOW_ID_in_statement_assign1149 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1153 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1155 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1157 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1159 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign1171 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign1175 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_assign1181 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1183 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1236 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1240 = frozenset([19])
    FOLLOW_ID_in_statement_assign1242 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1246 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1299 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1303 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1305 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1307 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1309 = frozenset([19])
    FOLLOW_ID_in_statement_assign1321 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1325 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1331 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1333 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1395 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1397 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1399 = frozenset([15])
    FOLLOW_DO_in_statement_while1403 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1405 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1419 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1421 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_while1423 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1425 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1427 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1467 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1477 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1489 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1597 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1599 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1631 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1633 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1665 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1667 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1671 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1673 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1687 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1689 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_elif_body1691 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1693 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1695 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1735 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1737 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1751 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1753 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_else1755 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1757 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1759 = frozenset([1])
    FOLLOW_condition_call_in_condition1797 = frozenset([1])
    FOLLOW_ANY_in_condition1826 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1828 = frozenset([1])
    FOLLOW_ALL_in_condition1857 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1859 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1897 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1907 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1909 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1911 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1913 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1917 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1919 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1953 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1963 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1982 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line1984 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2010 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2029 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line2031 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2075 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line2077 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2081 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2091 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2093 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line2097 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2099 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line2105 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2107 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2143 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value2160 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2170 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2180 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2190 = frozenset([1])
    FOLLOW_CONSTS_in_consts2209 = frozenset([19])
    FOLLOW_ID_in_consts2211 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2213 = frozenset([21])
    FOLLOW_INDENT_in_consts2223 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2225 = frozenset([19])
    FOLLOW_consts_items_in_consts2227 = frozenset([13])
    FOLLOW_DEDENT_in_consts2229 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2231 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2263 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2279 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2281 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2283 = frozenset([1])
    FOLLOW_ID_in_consts_item2305 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2307 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2309 = frozenset([1])
    FOLLOW_ID_in_consts_item2331 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2333 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2335 = frozenset([1])
    FOLLOW_TYPES_in_types2366 = frozenset([19])
    FOLLOW_ID_in_types2368 = frozenset([26])
    FOLLOW_NEWLINE_in_types2370 = frozenset([21])
    FOLLOW_INDENT_in_types2380 = frozenset([26])
    FOLLOW_NEWLINE_in_types2382 = frozenset([19])
    FOLLOW_types_item_in_types2384 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2388 = frozenset([26])
    FOLLOW_NEWLINE_in_types2390 = frozenset([1])
    FOLLOW_ID_in_types_item2424 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2426 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2453 = frozenset([19])
    FOLLOW_ID_in_messages2455 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2457 = frozenset([21])
    FOLLOW_INDENT_in_messages2467 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2469 = frozenset([19])
    FOLLOW_messages_item_in_messages2471 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2475 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2477 = frozenset([1])
    FOLLOW_ID_in_messages_item2511 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2513 = frozenset([1])
    FOLLOW_VARS_in_vars2540 = frozenset([19])
    FOLLOW_ID_in_vars2542 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars2544 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2583 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2585 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints2609 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2621 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2623 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2627 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2629 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2635 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2637 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2665 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2667 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2679 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2681 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2685 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2687 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2693 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2695 = frozenset([1])
    FOLLOW_ID_in_attr_hint2732 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2773 = frozenset([19])
    FOLLOW_ID_in_attr_hint2775 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2815 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2817 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2819 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2821 = frozenset([19])
    FOLLOW_ID_in_attr_hint2825 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2829 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2835 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2882 = frozenset([19])
    FOLLOW_ID_in_hint2884 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2886 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2906 = frozenset([19])
    FOLLOW_ID_in_hint2908 = frozenset([19, 77])
    FOLLOW_hint_arg_in_hint2910 = frozenset([11, 19, 77])
    FOLLOW_CURLY_CLOSE_in_hint2914 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2953 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2957 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2965 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2969 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2971 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2973 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
