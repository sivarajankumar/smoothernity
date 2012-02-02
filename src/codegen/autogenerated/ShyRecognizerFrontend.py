# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-02 18:59:46

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
                # elements: receive, request, module_queue, proc, ID
                # token labels: 
                # rule labels: retval
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
    # grammar/ShyRecognizerFrontend.g:51:1: request : ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) );
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
        DEDENT38 = None
        NEWLINE39 = None
        REQUEST40 = None
        ID41 = None
        NEWLINE42 = None
        INDENT43 = None
        NEWLINE44 = None
        DEDENT47 = None
        NEWLINE48 = None
        statements37 = None

        local_vars45 = None

        local_ops46 = None


        REQUEST29_tree = None
        ID30_tree = None
        NEWLINE31_tree = None
        REQUEST32_tree = None
        ID33_tree = None
        NEWLINE34_tree = None
        INDENT35_tree = None
        NEWLINE36_tree = None
        DEDENT38_tree = None
        NEWLINE39_tree = None
        REQUEST40_tree = None
        ID41_tree = None
        NEWLINE42_tree = None
        INDENT43_tree = None
        NEWLINE44_tree = None
        DEDENT47_tree = None
        NEWLINE48_tree = None
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
                # grammar/ShyRecognizerFrontend.g:52:5: ( REQUEST ID NEWLINE -> ^( TREE_REQUEST ID ) | REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_REQUEST ID statements ) | REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? ) )
                alt10 = 3
                LA10_0 = self.input.LA(1)

                if (LA10_0 == REQUEST) :
                    LA10_1 = self.input.LA(2)

                    if (LA10_1 == ID) :
                        LA10_2 = self.input.LA(3)

                        if (LA10_2 == NEWLINE) :
                            LA10_3 = self.input.LA(4)

                            if (LA10_3 == INDENT) :
                                LA10_4 = self.input.LA(5)

                                if (LA10_4 == NEWLINE) :
                                    LA10_6 = self.input.LA(6)

                                    if ((EXPRESSION <= LA10_6 <= IF) or LA10_6 == MINUS or LA10_6 == NUMBER or LA10_6 == WHILE or LA10_6 == WITH) :
                                        alt10 = 2
                                    elif (LA10_6 == DEDENT or LA10_6 == OPS or LA10_6 == VARS) :
                                        alt10 = 3
                                    else:
                                        nvae = NoViableAltException("", 10, 6, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 10, 4, self.input)

                                    raise nvae


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
                    # grammar/ShyRecognizerFrontend.g:54:9: REQUEST ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
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


                    self._state.following.append(self.FOLLOW_statements_in_request468)
                    statements37 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements37.tree)


                    DEDENT38 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request470) 
                    stream_DEDENT.add(DEDENT38)


                    NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request472) 
                    stream_NEWLINE.add(NEWLINE39)


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
                    # 55:9: -> ^( TREE_REQUEST ID statements )
                    # grammar/ShyRecognizerFrontend.g:55:13: ^( TREE_REQUEST ID statements )
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




                elif alt10 == 3:
                    # grammar/ShyRecognizerFrontend.g:56:9: REQUEST ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    REQUEST40 = self.match(self.input, REQUEST, self.FOLLOW_REQUEST_in_request503) 
                    stream_REQUEST.add(REQUEST40)


                    ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_request505) 
                    stream_ID.add(ID41)


                    NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request507) 
                    stream_NEWLINE.add(NEWLINE42)


                    INDENT43 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_request509) 
                    stream_INDENT.add(INDENT43)


                    NEWLINE44 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request511) 
                    stream_NEWLINE.add(NEWLINE44)


                    # grammar/ShyRecognizerFrontend.g:57:13: ( local_vars )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == VARS) :
                        alt8 = 1
                    if alt8 == 1:
                        # grammar/ShyRecognizerFrontend.g:57:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_request525)
                        local_vars45 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars45.tree)





                    # grammar/ShyRecognizerFrontend.g:57:26: ( local_ops )?
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == OPS) :
                        alt9 = 1
                    if alt9 == 1:
                        # grammar/ShyRecognizerFrontend.g:57:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_request529)
                        local_ops46 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops46.tree)





                    DEDENT47 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_request541) 
                    stream_DEDENT.add(DEDENT47)


                    NEWLINE48 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_request543) 
                    stream_NEWLINE.add(NEWLINE48)


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
                    # 59:9: -> ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:59:13: ^( TREE_REQUEST ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_REQUEST, "TREE_REQUEST")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:59:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:59:45: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:62:1: receive : ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) );
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECEIVE49 = None
        ID50 = None
        NEWLINE51 = None
        RECEIVE52 = None
        ID53 = None
        NEWLINE54 = None
        INDENT55 = None
        NEWLINE56 = None
        DEDENT58 = None
        NEWLINE59 = None
        RECEIVE60 = None
        ID61 = None
        NEWLINE62 = None
        INDENT63 = None
        NEWLINE64 = None
        DEDENT67 = None
        NEWLINE68 = None
        statements57 = None

        local_vars65 = None

        local_ops66 = None


        RECEIVE49_tree = None
        ID50_tree = None
        NEWLINE51_tree = None
        RECEIVE52_tree = None
        ID53_tree = None
        NEWLINE54_tree = None
        INDENT55_tree = None
        NEWLINE56_tree = None
        DEDENT58_tree = None
        NEWLINE59_tree = None
        RECEIVE60_tree = None
        ID61_tree = None
        NEWLINE62_tree = None
        INDENT63_tree = None
        NEWLINE64_tree = None
        DEDENT67_tree = None
        NEWLINE68_tree = None
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
                # grammar/ShyRecognizerFrontend.g:63:5: ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_RECEIVE ID statements ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) )
                alt13 = 3
                LA13_0 = self.input.LA(1)

                if (LA13_0 == RECEIVE) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == ID) :
                        LA13_2 = self.input.LA(3)

                        if (LA13_2 == NEWLINE) :
                            LA13_3 = self.input.LA(4)

                            if (LA13_3 == INDENT) :
                                LA13_4 = self.input.LA(5)

                                if (LA13_4 == NEWLINE) :
                                    LA13_6 = self.input.LA(6)

                                    if ((EXPRESSION <= LA13_6 <= IF) or LA13_6 == MINUS or LA13_6 == NUMBER or LA13_6 == WHILE or LA13_6 == WITH) :
                                        alt13 = 2
                                    elif (LA13_6 == DEDENT or LA13_6 == OPS or LA13_6 == VARS) :
                                        alt13 = 3
                                    else:
                                        nvae = NoViableAltException("", 13, 6, self.input)

                                        raise nvae


                                else:
                                    nvae = NoViableAltException("", 13, 4, self.input)

                                    raise nvae


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
                    # grammar/ShyRecognizerFrontend.g:63:9: RECEIVE ID NEWLINE
                    pass 
                    RECEIVE49 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive589) 
                    stream_RECEIVE.add(RECEIVE49)


                    ID50 = self.match(self.input, ID, self.FOLLOW_ID_in_receive591) 
                    stream_ID.add(ID50)


                    NEWLINE51 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive593) 
                    stream_NEWLINE.add(NEWLINE51)


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
                    # 64:9: -> ^( TREE_RECEIVE ID )
                    # grammar/ShyRecognizerFrontend.g:64:13: ^( TREE_RECEIVE ID )
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
                    # grammar/ShyRecognizerFrontend.g:65:9: RECEIVE ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                    pass 
                    RECEIVE52 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive622) 
                    stream_RECEIVE.add(RECEIVE52)


                    ID53 = self.match(self.input, ID, self.FOLLOW_ID_in_receive624) 
                    stream_ID.add(ID53)


                    NEWLINE54 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive626) 
                    stream_NEWLINE.add(NEWLINE54)


                    INDENT55 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive628) 
                    stream_INDENT.add(INDENT55)


                    NEWLINE56 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive630) 
                    stream_NEWLINE.add(NEWLINE56)


                    self._state.following.append(self.FOLLOW_statements_in_receive632)
                    statements57 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements57.tree)


                    DEDENT58 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive634) 
                    stream_DEDENT.add(DEDENT58)


                    NEWLINE59 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive636) 
                    stream_NEWLINE.add(NEWLINE59)


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




                elif alt13 == 3:
                    # grammar/ShyRecognizerFrontend.g:67:9: RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    RECEIVE60 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive667) 
                    stream_RECEIVE.add(RECEIVE60)


                    ID61 = self.match(self.input, ID, self.FOLLOW_ID_in_receive669) 
                    stream_ID.add(ID61)


                    NEWLINE62 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive671) 
                    stream_NEWLINE.add(NEWLINE62)


                    INDENT63 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive673) 
                    stream_INDENT.add(INDENT63)


                    NEWLINE64 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive675) 
                    stream_NEWLINE.add(NEWLINE64)


                    # grammar/ShyRecognizerFrontend.g:68:13: ( local_vars )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == VARS) :
                        alt11 = 1
                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:68:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_receive689)
                        local_vars65 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars65.tree)





                    # grammar/ShyRecognizerFrontend.g:68:26: ( local_ops )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == OPS) :
                        alt12 = 1
                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:68:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_receive693)
                        local_ops66 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops66.tree)





                    DEDENT67 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive705) 
                    stream_DEDENT.add(DEDENT67)


                    NEWLINE68 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive707) 
                    stream_NEWLINE.add(NEWLINE68)


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

        PROC69 = None
        ID70 = None
        NEWLINE71 = None
        PROC72 = None
        ID73 = None
        NEWLINE74 = None
        INDENT75 = None
        NEWLINE76 = None
        DEDENT78 = None
        NEWLINE79 = None
        PROC80 = None
        ID81 = None
        NEWLINE82 = None
        INDENT83 = None
        NEWLINE84 = None
        DEDENT88 = None
        NEWLINE89 = None
        statements77 = None

        proc_args85 = None

        local_vars86 = None

        local_ops87 = None


        PROC69_tree = None
        ID70_tree = None
        NEWLINE71_tree = None
        PROC72_tree = None
        ID73_tree = None
        NEWLINE74_tree = None
        INDENT75_tree = None
        NEWLINE76_tree = None
        DEDENT78_tree = None
        NEWLINE79_tree = None
        PROC80_tree = None
        ID81_tree = None
        NEWLINE82_tree = None
        INDENT83_tree = None
        NEWLINE84_tree = None
        DEDENT88_tree = None
        NEWLINE89_tree = None
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
                    # grammar/ShyRecognizerFrontend.g:74:9: PROC ID NEWLINE
                    pass 
                    PROC69 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc753) 
                    stream_PROC.add(PROC69)


                    ID70 = self.match(self.input, ID, self.FOLLOW_ID_in_proc755) 
                    stream_ID.add(ID70)


                    NEWLINE71 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc757) 
                    stream_NEWLINE.add(NEWLINE71)


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
                    PROC72 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc786) 
                    stream_PROC.add(PROC72)


                    ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_proc788) 
                    stream_ID.add(ID73)


                    NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc790) 
                    stream_NEWLINE.add(NEWLINE74)


                    INDENT75 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc792) 
                    stream_INDENT.add(INDENT75)


                    NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc794) 
                    stream_NEWLINE.add(NEWLINE76)


                    self._state.following.append(self.FOLLOW_statements_in_proc796)
                    statements77 = self.statements()

                    self._state.following.pop()
                    stream_statements.add(statements77.tree)


                    DEDENT78 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc798) 
                    stream_DEDENT.add(DEDENT78)


                    NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc800) 
                    stream_NEWLINE.add(NEWLINE79)


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
                    PROC80 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc831) 
                    stream_PROC.add(PROC80)


                    ID81 = self.match(self.input, ID, self.FOLLOW_ID_in_proc833) 
                    stream_ID.add(ID81)


                    NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc835) 
                    stream_NEWLINE.add(NEWLINE82)


                    INDENT83 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc837) 
                    stream_INDENT.add(INDENT83)


                    NEWLINE84 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc839) 
                    stream_NEWLINE.add(NEWLINE84)


                    # grammar/ShyRecognizerFrontend.g:79:13: ( proc_args )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == ARGS) :
                        alt14 = 1
                    if alt14 == 1:
                        # grammar/ShyRecognizerFrontend.g:79:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc853)
                        proc_args85 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args85.tree)





                    # grammar/ShyRecognizerFrontend.g:79:25: ( local_vars )?
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == VARS) :
                        alt15 = 1
                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:79:25: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_proc857)
                        local_vars86 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars86.tree)





                    # grammar/ShyRecognizerFrontend.g:79:38: ( local_ops )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == OPS) :
                        alt16 = 1
                    if alt16 == 1:
                        # grammar/ShyRecognizerFrontend.g:79:38: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_proc861)
                        local_ops87 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops87.tree)





                    DEDENT88 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc873) 
                    stream_DEDENT.add(DEDENT88)


                    NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc875) 
                    stream_NEWLINE.add(NEWLINE89)


                    # AST Rewrite
                    # elements: local_ops, ID, proc_args, local_vars
                    # token labels: 
                    # rule labels: retval
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

        ARGS90 = None
        attrs_hints91 = None


        ARGS90_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:85:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:85:9: ARGS attrs_hints
                pass 
                ARGS90 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args925) 
                stream_ARGS.add(ARGS90)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args927)
                attrs_hints91 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints91.tree)


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

        VARS92 = None
        attrs_hints93 = None


        VARS92_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:89:5: ( VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:89:9: VARS attrs_hints
                pass 
                VARS92 = self.match(self.input, VARS, self.FOLLOW_VARS_in_local_vars956) 
                stream_VARS.add(VARS92)


                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars958)
                attrs_hints93 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints93.tree)


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
    # grammar/ShyRecognizerFrontend.g:92:1: local_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
    def local_ops(self, ):
        retval = self.local_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS94 = None
        NEWLINE95 = None
        INDENT96 = None
        NEWLINE97 = None
        DEDENT99 = None
        NEWLINE100 = None
        statements98 = None


        OPS94_tree = None
        NEWLINE95_tree = None
        INDENT96_tree = None
        NEWLINE97_tree = None
        DEDENT99_tree = None
        NEWLINE100_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:93:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
                # grammar/ShyRecognizerFrontend.g:93:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                OPS94 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops987) 
                stream_OPS.add(OPS94)


                NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops989) 
                stream_NEWLINE.add(NEWLINE95)


                INDENT96 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_local_ops991) 
                stream_INDENT.add(INDENT96)


                NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops993) 
                stream_NEWLINE.add(NEWLINE97)


                self._state.following.append(self.FOLLOW_statements_in_local_ops995)
                statements98 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements98.tree)


                DEDENT99 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_local_ops997) 
                stream_DEDENT.add(DEDENT99)


                NEWLINE100 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops999) 
                stream_NEWLINE.add(NEWLINE100)


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





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:97:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE102 = None
        statement_call_single_line101 = None

        statement_call_multi_line103 = None

        statement_if104 = None

        statement_assign105 = None

        statement_while106 = None

        statement_with107 = None


        NEWLINE102_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:98:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt18 = 6
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:98:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement1030)
                    statement_call_single_line101 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line101.tree)


                    NEWLINE102 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement1032) 
                    stream_NEWLINE.add(NEWLINE102)


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
                    # 99:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:100:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement1058)
                    statement_call_multi_line103 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line103.tree)



                elif alt18 == 3:
                    # grammar/ShyRecognizerFrontend.g:101:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement1068)
                    statement_if104 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if104.tree)



                elif alt18 == 4:
                    # grammar/ShyRecognizerFrontend.g:102:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement1078)
                    statement_assign105 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign105.tree)



                elif alt18 == 5:
                    # grammar/ShyRecognizerFrontend.g:103:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement1088)
                    statement_while106 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while106.tree)



                elif alt18 == 6:
                    # grammar/ShyRecognizerFrontend.g:104:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement1098)
                    statement_with107 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with107.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:107:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement108 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:108:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:108:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:108:9: ( statement )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA19_0 <= IF) or LA19_0 == MINUS or LA19_0 == NUMBER or LA19_0 == WHILE or LA19_0 == WITH) :
                        alt19 = 1


                    if alt19 == 1:
                        # grammar/ShyRecognizerFrontend.g:108:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements1117)
                        statement108 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement108.tree)



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
                # 109:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:109:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:109:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:112:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH109 = None
        ID110 = None
        NEWLINE111 = None
        INDENT112 = None
        NEWLINE113 = None
        DEDENT115 = None
        NEWLINE116 = None
        statements114 = None


        WITH109_tree = None
        ID110_tree = None
        NEWLINE111_tree = None
        INDENT112_tree = None
        NEWLINE113_tree = None
        DEDENT115_tree = None
        NEWLINE116_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:113:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:113:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH109 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with1159) 
                stream_WITH.add(WITH109)


                ID110 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with1161) 
                stream_ID.add(ID110)


                NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1163) 
                stream_NEWLINE.add(NEWLINE111)


                INDENT112 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with1173) 
                stream_INDENT.add(INDENT112)


                NEWLINE113 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1175) 
                stream_NEWLINE.add(NEWLINE113)


                self._state.following.append(self.FOLLOW_statements_in_statement_with1177)
                statements114 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements114.tree)


                DEDENT115 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with1179) 
                stream_DEDENT.add(DEDENT115)


                NEWLINE116 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with1181) 
                stream_NEWLINE.add(NEWLINE116)


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
                # 115:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:115:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:118:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID117 = None
        ARROW_LEFT118 = None
        NEWLINE120 = None
        ID121 = None
        ARROW_LEFT122 = None
        NEWLINE123 = None
        INDENT124 = None
        NEWLINE125 = None
        NEWLINE127 = None
        DEDENT128 = None
        NEWLINE129 = None
        ARROW_RIGHT131 = None
        ID132 = None
        NEWLINE133 = None
        ARROW_RIGHT135 = None
        NEWLINE136 = None
        INDENT137 = None
        NEWLINE138 = None
        ID139 = None
        NEWLINE140 = None
        DEDENT141 = None
        NEWLINE142 = None
        arbitrary_value119 = None

        arbitrary_value126 = None

        arbitrary_value130 = None

        arbitrary_value134 = None


        ID117_tree = None
        ARROW_LEFT118_tree = None
        NEWLINE120_tree = None
        ID121_tree = None
        ARROW_LEFT122_tree = None
        NEWLINE123_tree = None
        INDENT124_tree = None
        NEWLINE125_tree = None
        NEWLINE127_tree = None
        DEDENT128_tree = None
        NEWLINE129_tree = None
        ARROW_RIGHT131_tree = None
        ID132_tree = None
        NEWLINE133_tree = None
        ARROW_RIGHT135_tree = None
        NEWLINE136_tree = None
        INDENT137_tree = None
        NEWLINE138_tree = None
        ID139_tree = None
        NEWLINE140_tree = None
        DEDENT141_tree = None
        NEWLINE142_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:119:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt30 = 4
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:119:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:119:9: ( ID )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == ID) :
                            alt20 = 1


                        if alt20 == 1:
                            # grammar/ShyRecognizerFrontend.g:119:9: ID
                            pass 
                            ID117 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1221) 
                            stream_ID.add(ID117)



                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


                    ARROW_LEFT118 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1225) 
                    stream_ARROW_LEFT.add(ARROW_LEFT118)


                    # grammar/ShyRecognizerFrontend.g:119:25: ( arbitrary_value )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:119:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1227)
                            arbitrary_value119 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value119.tree)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1231) 
                    stream_NEWLINE.add(NEWLINE120)


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




                elif alt30 == 2:
                    # grammar/ShyRecognizerFrontend.g:122:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:122:9: ( ID )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == ID) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:122:9: ID
                            pass 
                            ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1284) 
                            stream_ID.add(ID121)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    ARROW_LEFT122 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1288) 
                    stream_ARROW_LEFT.add(ARROW_LEFT122)


                    NEWLINE123 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1290) 
                    stream_NEWLINE.add(NEWLINE123)


                    INDENT124 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1292) 
                    stream_INDENT.add(INDENT124)


                    NEWLINE125 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1294) 
                    stream_NEWLINE.add(NEWLINE125)


                    # grammar/ShyRecognizerFrontend.g:123:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt24 = 0
                    while True: #loop24
                        alt24 = 2
                        LA24_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER) :
                            alt24 = 1


                        if alt24 == 1:
                            # grammar/ShyRecognizerFrontend.g:123:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:123:11: ( arbitrary_value )+
                            cnt23 = 0
                            while True: #loop23
                                alt23 = 2
                                LA23_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                                    alt23 = 1


                                if alt23 == 1:
                                    # grammar/ShyRecognizerFrontend.g:123:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1306)
                                    arbitrary_value126 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value126.tree)



                                else:
                                    if cnt23 >= 1:
                                        break #loop23

                                    eee = EarlyExitException(23, self.input)
                                    raise eee

                                cnt23 += 1


                            NEWLINE127 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1310) 
                            stream_NEWLINE.add(NEWLINE127)



                        else:
                            if cnt24 >= 1:
                                break #loop24

                            eee = EarlyExitException(24, self.input)
                            raise eee

                        cnt24 += 1


                    DEDENT128 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1316) 
                    stream_DEDENT.add(DEDENT128)


                    NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1318) 
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
                    # 124:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:124:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:124:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:125:42: ( ID )+
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
                    # grammar/ShyRecognizerFrontend.g:126:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:126:9: ( arbitrary_value )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1371)
                            arbitrary_value130 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value130.tree)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    ARROW_RIGHT131 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1375) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT131)


                    # grammar/ShyRecognizerFrontend.g:126:39: ( ID )+
                    cnt26 = 0
                    while True: #loop26
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == ID) :
                            alt26 = 1


                        if alt26 == 1:
                            # grammar/ShyRecognizerFrontend.g:126:39: ID
                            pass 
                            ID132 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1377) 
                            stream_ID.add(ID132)



                        else:
                            if cnt26 >= 1:
                                break #loop26

                            eee = EarlyExitException(26, self.input)
                            raise eee

                        cnt26 += 1


                    NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1381) 
                    stream_NEWLINE.add(NEWLINE133)


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




                elif alt30 == 4:
                    # grammar/ShyRecognizerFrontend.g:129:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:129:9: ( arbitrary_value )+
                    cnt27 = 0
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA27_0 <= ID) or LA27_0 == MINUS or LA27_0 == NUMBER) :
                            alt27 = 1


                        if alt27 == 1:
                            # grammar/ShyRecognizerFrontend.g:129:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1434)
                            arbitrary_value134 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value134.tree)



                        else:
                            if cnt27 >= 1:
                                break #loop27

                            eee = EarlyExitException(27, self.input)
                            raise eee

                        cnt27 += 1


                    ARROW_RIGHT135 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1438) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT135)


                    NEWLINE136 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1440) 
                    stream_NEWLINE.add(NEWLINE136)


                    INDENT137 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1442) 
                    stream_INDENT.add(INDENT137)


                    NEWLINE138 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1444) 
                    stream_NEWLINE.add(NEWLINE138)


                    # grammar/ShyRecognizerFrontend.g:130:9: ( ( ID )+ NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:130:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:130:11: ( ID )+
                            cnt28 = 0
                            while True: #loop28
                                alt28 = 2
                                LA28_0 = self.input.LA(1)

                                if (LA28_0 == ID) :
                                    alt28 = 1


                                if alt28 == 1:
                                    # grammar/ShyRecognizerFrontend.g:130:11: ID
                                    pass 
                                    ID139 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1456) 
                                    stream_ID.add(ID139)



                                else:
                                    if cnt28 >= 1:
                                        break #loop28

                                    eee = EarlyExitException(28, self.input)
                                    raise eee

                                cnt28 += 1


                            NEWLINE140 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1460) 
                            stream_NEWLINE.add(NEWLINE140)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT141 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1466) 
                    stream_DEDENT.add(DEDENT141)


                    NEWLINE142 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1468) 
                    stream_NEWLINE.add(NEWLINE142)


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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:135:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE143 = None
        NEWLINE145 = None
        DO146 = None
        NEWLINE147 = None
        INDENT148 = None
        NEWLINE149 = None
        DEDENT151 = None
        NEWLINE152 = None
        condition144 = None

        statements150 = None


        WHILE143_tree = None
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
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:136:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:136:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE143 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1530) 
                stream_WHILE.add(WHILE143)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1532)
                condition144 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition144.tree)


                # grammar/ShyRecognizerFrontend.g:136:25: ( NEWLINE )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == NEWLINE) :
                    alt31 = 1
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:136:25: NEWLINE
                    pass 
                    NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1534) 
                    stream_NEWLINE.add(NEWLINE145)





                DO146 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1538) 
                stream_DO.add(DO146)


                NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1540) 
                stream_NEWLINE.add(NEWLINE147)


                INDENT148 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1554) 
                stream_INDENT.add(INDENT148)


                NEWLINE149 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1556) 
                stream_NEWLINE.add(NEWLINE149)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1558)
                statements150 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements150.tree)


                DEDENT151 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1560) 
                stream_DEDENT.add(DEDENT151)


                NEWLINE152 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1562) 
                stream_NEWLINE.add(NEWLINE152)


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
                # 138:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:138:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:141:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head153 = None

        statement_elif154 = None

        statement_else155 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:142:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:142:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1602)
                statement_if_head153 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head153.tree)


                # grammar/ShyRecognizerFrontend.g:143:9: ( statement_elif )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == ELIF) :
                        alt32 = 1


                    if alt32 == 1:
                        # grammar/ShyRecognizerFrontend.g:143:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1612)
                        statement_elif154 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif154.tree)



                    else:
                        break #loop32


                # grammar/ShyRecognizerFrontend.g:144:9: ( statement_else )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == ELSE) :
                    alt33 = 1
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:144:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1624)
                    statement_else155 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else155.tree)





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
                # 145:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:145:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:147:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:148:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:152:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF156 = None
        statement_elif_body157 = None


        IF156_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:153:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:153:9: IF statement_elif_body
                pass 
                IF156 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1732) 
                stream_IF.add(IF156)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1734)
                statement_elif_body157 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body157.tree)


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
                # 154:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:157:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF158 = None
        statement_elif_body159 = None


        ELIF158_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:158:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:158:9: ELIF statement_elif_body
                pass 
                ELIF158 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1766) 
                stream_ELIF.add(ELIF158)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1768)
                statement_elif_body159 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body159.tree)


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

    # $ANTLR end "statement_elif"


    class statement_elif_body_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.statement_elif_body_return, self).__init__()

            self.tree = None





    # $ANTLR start "statement_elif_body"
    # grammar/ShyRecognizerFrontend.g:162:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE161 = None
        DO162 = None
        NEWLINE163 = None
        INDENT164 = None
        NEWLINE165 = None
        DEDENT167 = None
        NEWLINE168 = None
        condition160 = None

        statements166 = None


        NEWLINE161_tree = None
        DO162_tree = None
        NEWLINE163_tree = None
        INDENT164_tree = None
        NEWLINE165_tree = None
        DEDENT167_tree = None
        NEWLINE168_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:163:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:163:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1800)
                condition160 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition160.tree)


                # grammar/ShyRecognizerFrontend.g:163:19: ( NEWLINE )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == NEWLINE) :
                    alt34 = 1
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:163:19: NEWLINE
                    pass 
                    NEWLINE161 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1802) 
                    stream_NEWLINE.add(NEWLINE161)





                DO162 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1806) 
                stream_DO.add(DO162)


                NEWLINE163 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1808) 
                stream_NEWLINE.add(NEWLINE163)


                INDENT164 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1822) 
                stream_INDENT.add(INDENT164)


                NEWLINE165 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1824) 
                stream_NEWLINE.add(NEWLINE165)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1826)
                statements166 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements166.tree)


                DEDENT167 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1828) 
                stream_DEDENT.add(DEDENT167)


                NEWLINE168 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1830) 
                stream_NEWLINE.add(NEWLINE168)


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
                # 165:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:165:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:168:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE169 = None
        NEWLINE170 = None
        INDENT171 = None
        NEWLINE172 = None
        DEDENT174 = None
        NEWLINE175 = None
        statements173 = None


        ELSE169_tree = None
        NEWLINE170_tree = None
        INDENT171_tree = None
        NEWLINE172_tree = None
        DEDENT174_tree = None
        NEWLINE175_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:169:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:169:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE169 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1870) 
                stream_ELSE.add(ELSE169)


                NEWLINE170 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1872) 
                stream_NEWLINE.add(NEWLINE170)


                INDENT171 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1886) 
                stream_INDENT.add(INDENT171)


                NEWLINE172 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1888) 
                stream_NEWLINE.add(NEWLINE172)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1890)
                statements173 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements173.tree)


                DEDENT174 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1892) 
                stream_DEDENT.add(DEDENT174)


                NEWLINE175 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1894) 
                stream_NEWLINE.add(NEWLINE175)


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
                # 171:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:171:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:174:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY177 = None
        ALL179 = None
        condition_call176 = None

        condition_calls178 = None

        condition_calls180 = None


        ANY177_tree = None
        ALL179_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:175:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
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
                    # grammar/ShyRecognizerFrontend.g:175:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1932)
                    condition_call176 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call176.tree)


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
                    # 176:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:176:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:177:9: ANY condition_calls
                    pass 
                    ANY177 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1961) 
                    stream_ANY.add(ANY177)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1963)
                    condition_calls178 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls178.tree)


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
                    # 178:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:178:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt35 == 3:
                    # grammar/ShyRecognizerFrontend.g:179:9: ALL condition_calls
                    pass 
                    ALL179 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1992) 
                    stream_ALL.add(ALL179)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1994)
                    condition_calls180 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls180.tree)


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
                    # 180:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:180:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:183:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE182 = None
        INDENT183 = None
        NEWLINE184 = None
        DEDENT186 = None
        NEWLINE187 = None
        condition_call181 = None

        condition_call_line185 = None


        NEWLINE182_tree = None
        INDENT183_tree = None
        NEWLINE184_tree = None
        DEDENT186_tree = None
        NEWLINE187_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:184:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
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
                    # grammar/ShyRecognizerFrontend.g:184:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls2032)
                    condition_call181 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call181.tree)



                elif alt37 == 2:
                    # grammar/ShyRecognizerFrontend.g:185:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE182 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2042) 
                    stream_NEWLINE.add(NEWLINE182)


                    INDENT183 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls2044) 
                    stream_INDENT.add(INDENT183)


                    NEWLINE184 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2046) 
                    stream_NEWLINE.add(NEWLINE184)


                    # grammar/ShyRecognizerFrontend.g:185:32: ( condition_call_line )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:185:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls2048)
                            condition_call_line185 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line185.tree)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


                    DEDENT186 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls2052) 
                    stream_DEDENT.add(DEDENT186)


                    NEWLINE187 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls2054) 
                    stream_NEWLINE.add(NEWLINE187)


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
                    # 186:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:186:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:189:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line188 = None

        statement_call_multi_line189 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:190:5: ( statement_call_single_line | statement_call_multi_line )
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:190:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call2088)
                    statement_call_single_line188 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line188.tree)



                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:191:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call2098)
                    statement_call_multi_line189 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line189.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:194:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE191 = None
        statement_call_single_line190 = None

        statement_call_multi_line192 = None


        NEWLINE191_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:195:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:195:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line2117)
                    statement_call_single_line190 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line190.tree)


                    NEWLINE191 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line2119) 
                    stream_NEWLINE.add(NEWLINE191)


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
                    # 196:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:197:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line2145)
                    statement_call_multi_line192 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line192.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:200:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID193 = None
        statement_call_args194 = None


        ID193_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:201:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:201:9: ID ( statement_call_args )?
                pass 
                ID193 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line2164) 
                stream_ID.add(ID193)


                # grammar/ShyRecognizerFrontend.g:201:12: ( statement_call_args )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if ((EXPRESSION <= LA40_0 <= ID) or LA40_0 == MINUS or LA40_0 == NUMBER) :
                    alt40 = 1
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:201:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line2166)
                    statement_call_args194 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args194.tree)





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
                # 202:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:202:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:202:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:205:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID195 = None
        NEWLINE197 = None
        INDENT198 = None
        NEWLINE199 = None
        NEWLINE201 = None
        DEDENT202 = None
        NEWLINE203 = None
        statement_call_args196 = None

        statement_call_args200 = None


        ID195_tree = None
        NEWLINE197_tree = None
        INDENT198_tree = None
        NEWLINE199_tree = None
        NEWLINE201_tree = None
        DEDENT202_tree = None
        NEWLINE203_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:206:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:206:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID195 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line2210) 
                stream_ID.add(ID195)


                # grammar/ShyRecognizerFrontend.g:206:12: ( statement_call_args )?
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if ((EXPRESSION <= LA41_0 <= ID) or LA41_0 == MINUS or LA41_0 == NUMBER) :
                    alt41 = 1
                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:206:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2212)
                    statement_call_args196 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args196.tree)





                NEWLINE197 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2216) 
                stream_NEWLINE.add(NEWLINE197)


                INDENT198 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line2226) 
                stream_INDENT.add(INDENT198)


                NEWLINE199 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2228) 
                stream_NEWLINE.add(NEWLINE199)


                # grammar/ShyRecognizerFrontend.g:207:24: ( statement_call_args NEWLINE )+
                cnt42 = 0
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA42_0 <= ID) or LA42_0 == MINUS or LA42_0 == NUMBER) :
                        alt42 = 1


                    if alt42 == 1:
                        # grammar/ShyRecognizerFrontend.g:207:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line2232)
                        statement_call_args200 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args200.tree)


                        NEWLINE201 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2234) 
                        stream_NEWLINE.add(NEWLINE201)



                    else:
                        if cnt42 >= 1:
                            break #loop42

                        eee = EarlyExitException(42, self.input)
                        raise eee

                    cnt42 += 1


                DEDENT202 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line2240) 
                stream_DEDENT.add(DEDENT202)


                NEWLINE203 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line2242) 
                stream_NEWLINE.add(NEWLINE203)


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
                # 208:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:208:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:208:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:211:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value204 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:211:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:211:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:211:23: ( arbitrary_value )+
                cnt43 = 0
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA43_0 <= ID) or LA43_0 == MINUS or LA43_0 == NUMBER) :
                        alt43 = 1


                    if alt43 == 1:
                        # grammar/ShyRecognizerFrontend.g:211:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args2278)
                        arbitrary_value204 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value204.tree)



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
    # grammar/ShyRecognizerFrontend.g:213:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID205 = None
        EXPRESSION206 = None
        num_whole207 = None

        num_fract208 = None


        ID205_tree = None
        EXPRESSION206_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:214:5: ( ID | EXPRESSION | num_whole | num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:214:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID205 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2295)
                    ID205_tree = self._adaptor.createWithPayload(ID205)
                    self._adaptor.addChild(root_0, ID205_tree)




                elif alt44 == 2:
                    # grammar/ShyRecognizerFrontend.g:215:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION206 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2305)
                    EXPRESSION206_tree = self._adaptor.createWithPayload(EXPRESSION206)
                    self._adaptor.addChild(root_0, EXPRESSION206_tree)




                elif alt44 == 3:
                    # grammar/ShyRecognizerFrontend.g:216:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2315)
                    num_whole207 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole207.tree)



                elif alt44 == 4:
                    # grammar/ShyRecognizerFrontend.g:217:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2325)
                    num_fract208 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract208.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:220:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS209 = None
        ID210 = None
        NEWLINE211 = None
        INDENT212 = None
        NEWLINE213 = None
        DEDENT215 = None
        NEWLINE216 = None
        consts_items214 = None


        CONSTS209_tree = None
        ID210_tree = None
        NEWLINE211_tree = None
        INDENT212_tree = None
        NEWLINE213_tree = None
        DEDENT215_tree = None
        NEWLINE216_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:221:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:221:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS209 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2344) 
                stream_CONSTS.add(CONSTS209)


                ID210 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2346) 
                stream_ID.add(ID210)


                NEWLINE211 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2348) 
                stream_NEWLINE.add(NEWLINE211)


                INDENT212 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2358) 
                stream_INDENT.add(INDENT212)


                NEWLINE213 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2360) 
                stream_NEWLINE.add(NEWLINE213)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2362)
                consts_items214 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items214.tree)


                DEDENT215 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2364) 
                stream_DEDENT.add(DEDENT215)


                NEWLINE216 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2366) 
                stream_NEWLINE.add(NEWLINE216)


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
                # 223:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:223:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:225:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item217 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:225:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:225:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:225:16: ( consts_item )+
                cnt45 = 0
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ID) :
                        alt45 = 1


                    if alt45 == 1:
                        # grammar/ShyRecognizerFrontend.g:225:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2398)
                        consts_item217 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item217.tree)



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
    # grammar/ShyRecognizerFrontend.g:226:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID218 = None
        NEWLINE220 = None
        ID221 = None
        NEWLINE223 = None
        ID224 = None
        EXPRESSION225 = None
        NEWLINE226 = None
        num_whole219 = None

        num_fract222 = None


        ID218_tree = None
        NEWLINE220_tree = None
        ID221_tree = None
        NEWLINE223_tree = None
        ID224_tree = None
        EXPRESSION225_tree = None
        NEWLINE226_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:227:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
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
                    # grammar/ShyRecognizerFrontend.g:227:9: ID num_whole NEWLINE
                    pass 
                    ID218 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2414) 
                    stream_ID.add(ID218)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2416)
                    num_whole219 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole219.tree)


                    NEWLINE220 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2418) 
                    stream_NEWLINE.add(NEWLINE220)


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
                    # 227:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:227:33: ^( TREE_NUM_WHOLE ID num_whole )
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
                    # grammar/ShyRecognizerFrontend.g:228:9: ID num_fract NEWLINE
                    pass 
                    ID221 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2440) 
                    stream_ID.add(ID221)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2442)
                    num_fract222 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract222.tree)


                    NEWLINE223 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2444) 
                    stream_NEWLINE.add(NEWLINE223)


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
                    # 228:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:228:33: ^( TREE_NUM_FRACT ID num_fract )
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
                    # grammar/ShyRecognizerFrontend.g:229:9: ID EXPRESSION NEWLINE
                    pass 
                    ID224 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2466) 
                    stream_ID.add(ID224)


                    EXPRESSION225 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2468) 
                    stream_EXPRESSION.add(EXPRESSION225)


                    NEWLINE226 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2470) 
                    stream_NEWLINE.add(NEWLINE226)


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
                    # 229:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:229:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:232:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES227 = None
        ID228 = None
        NEWLINE229 = None
        INDENT230 = None
        NEWLINE231 = None
        DEDENT233 = None
        NEWLINE234 = None
        types_item232 = None


        TYPES227_tree = None
        ID228_tree = None
        NEWLINE229_tree = None
        INDENT230_tree = None
        NEWLINE231_tree = None
        DEDENT233_tree = None
        NEWLINE234_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:233:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:233:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES227 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2501) 
                stream_TYPES.add(TYPES227)


                ID228 = self.match(self.input, ID, self.FOLLOW_ID_in_types2503) 
                stream_ID.add(ID228)


                NEWLINE229 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2505) 
                stream_NEWLINE.add(NEWLINE229)


                INDENT230 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2515) 
                stream_INDENT.add(INDENT230)


                NEWLINE231 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2517) 
                stream_NEWLINE.add(NEWLINE231)


                # grammar/ShyRecognizerFrontend.g:234:24: ( types_item )+
                cnt47 = 0
                while True: #loop47
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == ID) :
                        alt47 = 1


                    if alt47 == 1:
                        # grammar/ShyRecognizerFrontend.g:234:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2519)
                        types_item232 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item232.tree)



                    else:
                        if cnt47 >= 1:
                            break #loop47

                        eee = EarlyExitException(47, self.input)
                        raise eee

                    cnt47 += 1


                DEDENT233 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2523) 
                stream_DEDENT.add(DEDENT233)


                NEWLINE234 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2525) 
                stream_NEWLINE.add(NEWLINE234)


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
                # 235:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:235:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:235:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:237:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID235 = None
        attrs_hints236 = None


        ID235_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:237:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:237:14: ID attrs_hints
                pass 
                ID235 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2559) 
                stream_ID.add(ID235)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2561)
                attrs_hints236 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints236.tree)


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
                # 237:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:237:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:239:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES237 = None
        ID238 = None
        NEWLINE239 = None
        INDENT240 = None
        NEWLINE241 = None
        DEDENT243 = None
        NEWLINE244 = None
        messages_item242 = None


        MESSAGES237_tree = None
        ID238_tree = None
        NEWLINE239_tree = None
        INDENT240_tree = None
        NEWLINE241_tree = None
        DEDENT243_tree = None
        NEWLINE244_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:240:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:240:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES237 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2588) 
                stream_MESSAGES.add(MESSAGES237)


                ID238 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2590) 
                stream_ID.add(ID238)


                NEWLINE239 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2592) 
                stream_NEWLINE.add(NEWLINE239)


                INDENT240 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2602) 
                stream_INDENT.add(INDENT240)


                NEWLINE241 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2604) 
                stream_NEWLINE.add(NEWLINE241)


                # grammar/ShyRecognizerFrontend.g:241:24: ( messages_item )+
                cnt48 = 0
                while True: #loop48
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == ID) :
                        alt48 = 1


                    if alt48 == 1:
                        # grammar/ShyRecognizerFrontend.g:241:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2606)
                        messages_item242 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item242.tree)



                    else:
                        if cnt48 >= 1:
                            break #loop48

                        eee = EarlyExitException(48, self.input)
                        raise eee

                    cnt48 += 1


                DEDENT243 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2610) 
                stream_DEDENT.add(DEDENT243)


                NEWLINE244 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2612) 
                stream_NEWLINE.add(NEWLINE244)


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
                # 242:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:242:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:242:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:244:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID245 = None
        attrs_hints246 = None


        ID245_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:244:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:244:17: ID attrs_hints
                pass 
                ID245 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2646) 
                stream_ID.add(ID245)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2648)
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
                # 244:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:244:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:246:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS247 = None
        ID248 = None
        attrs_hints249 = None


        VARS247_tree = None
        ID248_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:247:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:247:9: VARS ID attrs_hints
                pass 
                VARS247 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars2675) 
                stream_VARS.add(VARS247)


                ID248 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2677) 
                stream_ID.add(ID248)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2679)
                attrs_hints249 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints249.tree)


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
                # 248:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:248:12: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:251:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE251 = None
        NEWLINE252 = None
        INDENT253 = None
        NEWLINE254 = None
        NEWLINE256 = None
        DEDENT257 = None
        NEWLINE258 = None
        NEWLINE260 = None
        INDENT261 = None
        NEWLINE262 = None
        NEWLINE264 = None
        DEDENT265 = None
        NEWLINE266 = None
        attr_hint250 = None

        attr_hint255 = None

        attr_hint259 = None

        attr_hint263 = None


        NEWLINE251_tree = None
        NEWLINE252_tree = None
        INDENT253_tree = None
        NEWLINE254_tree = None
        NEWLINE256_tree = None
        DEDENT257_tree = None
        NEWLINE258_tree = None
        NEWLINE260_tree = None
        INDENT261_tree = None
        NEWLINE262_tree = None
        NEWLINE264_tree = None
        DEDENT265_tree = None
        NEWLINE266_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:252:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt51 = 3
                alt51 = self.dfa51.predict(self.input)
                if alt51 == 1:
                    # grammar/ShyRecognizerFrontend.g:252:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2718)
                    attr_hint250 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint250.tree)


                    NEWLINE251 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2720) 
                    stream_NEWLINE.add(NEWLINE251)


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
                    # 253:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt51 == 2:
                    # grammar/ShyRecognizerFrontend.g:254:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE252 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2744) 
                    stream_NEWLINE.add(NEWLINE252)


                    # grammar/ShyRecognizerFrontend.g:255:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:255:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT253 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2756) 
                    stream_INDENT.add(INDENT253)


                    NEWLINE254 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2758) 
                    stream_NEWLINE.add(NEWLINE254)


                    # grammar/ShyRecognizerFrontend.g:255:26: ( attr_hint NEWLINE )+
                    cnt49 = 0
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == CURLY_OPEN or LA49_0 == ID) :
                            alt49 = 1


                        if alt49 == 1:
                            # grammar/ShyRecognizerFrontend.g:255:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2762)
                            attr_hint255 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint255.tree)


                            NEWLINE256 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2764) 
                            stream_NEWLINE.add(NEWLINE256)



                        else:
                            if cnt49 >= 1:
                                break #loop49

                            eee = EarlyExitException(49, self.input)
                            raise eee

                        cnt49 += 1


                    DEDENT257 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2770) 
                    stream_DEDENT.add(DEDENT257)


                    NEWLINE258 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2772) 
                    stream_NEWLINE.add(NEWLINE258)





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
                    # 256:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:256:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt51 == 3:
                    # grammar/ShyRecognizerFrontend.g:257:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2800)
                    attr_hint259 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint259.tree)


                    NEWLINE260 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2802) 
                    stream_NEWLINE.add(NEWLINE260)


                    # grammar/ShyRecognizerFrontend.g:258:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:258:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT261 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2814) 
                    stream_INDENT.add(INDENT261)


                    NEWLINE262 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2816) 
                    stream_NEWLINE.add(NEWLINE262)


                    # grammar/ShyRecognizerFrontend.g:258:26: ( attr_hint NEWLINE )+
                    cnt50 = 0
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == CURLY_OPEN or LA50_0 == ID) :
                            alt50 = 1


                        if alt50 == 1:
                            # grammar/ShyRecognizerFrontend.g:258:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2820)
                            attr_hint263 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint263.tree)


                            NEWLINE264 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2822) 
                            stream_NEWLINE.add(NEWLINE264)



                        else:
                            if cnt50 >= 1:
                                break #loop50

                            eee = EarlyExitException(50, self.input)
                            raise eee

                        cnt50 += 1


                    DEDENT265 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2828) 
                    stream_DEDENT.add(DEDENT265)


                    NEWLINE266 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2830) 
                    stream_NEWLINE.add(NEWLINE266)





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
                    # 259:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:259:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:261:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID267 = None
        ID269 = None
        NEWLINE271 = None
        INDENT272 = None
        NEWLINE273 = None
        ID274 = None
        NEWLINE275 = None
        DEDENT276 = None
        hint268 = None

        hint270 = None


        ID267_tree = None
        ID269_tree = None
        NEWLINE271_tree = None
        INDENT272_tree = None
        NEWLINE273_tree = None
        ID274_tree = None
        NEWLINE275_tree = None
        DEDENT276_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:262:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt56 = 3
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # grammar/ShyRecognizerFrontend.g:262:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:262:9: ( ID )+
                    cnt52 = 0
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == ID) :
                            alt52 = 1


                        if alt52 == 1:
                            # grammar/ShyRecognizerFrontend.g:262:9: ID
                            pass 
                            ID267 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2867) 
                            stream_ID.add(ID267)



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
                    # 263:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:263:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:263:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:263:45: ^( TREE_ATTR ID )
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
                    # grammar/ShyRecognizerFrontend.g:264:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2908)
                    hint268 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint268.tree)


                    # grammar/ShyRecognizerFrontend.g:264:14: ( ID )+
                    cnt53 = 0
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == ID) :
                            alt53 = 1


                        if alt53 == 1:
                            # grammar/ShyRecognizerFrontend.g:264:14: ID
                            pass 
                            ID269 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2910) 
                            stream_ID.add(ID269)



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
                    # 265:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:265:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:265:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:265:35: ^( TREE_ATTR ID )
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
                    # grammar/ShyRecognizerFrontend.g:266:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2950)
                    hint270 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint270.tree)


                    NEWLINE271 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2952) 
                    stream_NEWLINE.add(NEWLINE271)


                    INDENT272 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2954) 
                    stream_INDENT.add(INDENT272)


                    NEWLINE273 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2956) 
                    stream_NEWLINE.add(NEWLINE273)


                    # grammar/ShyRecognizerFrontend.g:266:37: ( ( ID )+ NEWLINE )+
                    cnt55 = 0
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == ID) :
                            alt55 = 1


                        if alt55 == 1:
                            # grammar/ShyRecognizerFrontend.g:266:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:266:39: ( ID )+
                            cnt54 = 0
                            while True: #loop54
                                alt54 = 2
                                LA54_0 = self.input.LA(1)

                                if (LA54_0 == ID) :
                                    alt54 = 1


                                if alt54 == 1:
                                    # grammar/ShyRecognizerFrontend.g:266:39: ID
                                    pass 
                                    ID274 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2960) 
                                    stream_ID.add(ID274)



                                else:
                                    if cnt54 >= 1:
                                        break #loop54

                                    eee = EarlyExitException(54, self.input)
                                    raise eee

                                cnt54 += 1


                            NEWLINE275 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2964) 
                            stream_NEWLINE.add(NEWLINE275)



                        else:
                            if cnt55 >= 1:
                                break #loop55

                            eee = EarlyExitException(55, self.input)
                            raise eee

                        cnt55 += 1


                    DEDENT276 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2970) 
                    stream_DEDENT.add(DEDENT276)


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
                    # 267:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:267:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:267:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:267:35: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:270:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN277 = None
        ID278 = None
        CURLY_CLOSE279 = None
        CURLY_OPEN280 = None
        ID281 = None
        CURLY_CLOSE283 = None
        hint_arg282 = None


        CURLY_OPEN277_tree = None
        ID278_tree = None
        CURLY_CLOSE279_tree = None
        CURLY_OPEN280_tree = None
        ID281_tree = None
        CURLY_CLOSE283_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:271:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
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
                    # grammar/ShyRecognizerFrontend.g:271:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN277 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3017) 
                    stream_CURLY_OPEN.add(CURLY_OPEN277)


                    ID278 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3019) 
                    stream_ID.add(ID278)


                    CURLY_CLOSE279 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3021) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE279)


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
                    # 271:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:271:38: ^( TREE_HINT ID )
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
                    # grammar/ShyRecognizerFrontend.g:272:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN280 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint3041) 
                    stream_CURLY_OPEN.add(CURLY_OPEN280)


                    ID281 = self.match(self.input, ID, self.FOLLOW_ID_in_hint3043) 
                    stream_ID.add(ID281)


                    # grammar/ShyRecognizerFrontend.g:272:23: ( hint_arg )+
                    cnt57 = 0
                    while True: #loop57
                        alt57 = 2
                        LA57_0 = self.input.LA(1)

                        if (LA57_0 == ID or LA57_0 == UNDERSCORE) :
                            alt57 = 1


                        if alt57 == 1:
                            # grammar/ShyRecognizerFrontend.g:272:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint3045)
                            hint_arg282 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg282.tree)



                        else:
                            if cnt57 >= 1:
                                break #loop57

                            eee = EarlyExitException(57, self.input)
                            raise eee

                        cnt57 += 1


                    CURLY_CLOSE283 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint3049) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE283)


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
                    # 272:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:272:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:272:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:274:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set284 = None

        set284_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:274:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set284 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set284))

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
    # grammar/ShyRecognizerFrontend.g:276:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS285 = None
        NUMBER286 = None

        MINUS285_tree = None
        NUMBER286_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:276:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:276:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:276:13: ( MINUS )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == MINUS) :
                    alt59 = 1
                if alt59 == 1:
                    # grammar/ShyRecognizerFrontend.g:276:13: MINUS
                    pass 
                    MINUS285 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole3088)
                    MINUS285_tree = self._adaptor.createWithPayload(MINUS285)
                    self._adaptor.addChild(root_0, MINUS285_tree)






                NUMBER286 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole3092)
                NUMBER286_tree = self._adaptor.createWithPayload(NUMBER286)
                self._adaptor.addChild(root_0, NUMBER286_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:277:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS287 = None
        NUMBER288 = None
        DIVIDE289 = None
        NUMBER290 = None

        MINUS287_tree = None
        NUMBER288_tree = None
        DIVIDE289_tree = None
        NUMBER290_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:277:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:277:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:277:13: ( MINUS )?
                alt60 = 2
                LA60_0 = self.input.LA(1)

                if (LA60_0 == MINUS) :
                    alt60 = 1
                if alt60 == 1:
                    # grammar/ShyRecognizerFrontend.g:277:13: MINUS
                    pass 
                    MINUS287 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract3100)
                    MINUS287_tree = self._adaptor.createWithPayload(MINUS287)
                    self._adaptor.addChild(root_0, MINUS287_tree)






                NUMBER288 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3104)
                NUMBER288_tree = self._adaptor.createWithPayload(NUMBER288)
                self._adaptor.addChild(root_0, NUMBER288_tree)



                DIVIDE289 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract3106)
                DIVIDE289_tree = self._adaptor.createWithPayload(DIVIDE289)
                self._adaptor.addChild(root_0, DIVIDE289_tree)



                NUMBER290 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract3108)
                NUMBER290_tree = self._adaptor.createWithPayload(NUMBER290)
                self._adaptor.addChild(root_0, NUMBER290_tree)





                retval.stop = self.input.LT(-1)


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
    FOLLOW_NEWLINE_in_request466 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_request468 = frozenset([13])
    FOLLOW_DEDENT_in_request470 = frozenset([26])
    FOLLOW_NEWLINE_in_request472 = frozenset([1])
    FOLLOW_REQUEST_in_request503 = frozenset([19])
    FOLLOW_ID_in_request505 = frozenset([26])
    FOLLOW_NEWLINE_in_request507 = frozenset([21])
    FOLLOW_INDENT_in_request509 = frozenset([26])
    FOLLOW_NEWLINE_in_request511 = frozenset([13, 28, 78])
    FOLLOW_local_vars_in_request525 = frozenset([13, 28])
    FOLLOW_local_ops_in_request529 = frozenset([13])
    FOLLOW_DEDENT_in_request541 = frozenset([26])
    FOLLOW_NEWLINE_in_request543 = frozenset([1])
    FOLLOW_RECEIVE_in_receive589 = frozenset([19])
    FOLLOW_ID_in_receive591 = frozenset([26])
    FOLLOW_NEWLINE_in_receive593 = frozenset([1])
    FOLLOW_RECEIVE_in_receive622 = frozenset([19])
    FOLLOW_ID_in_receive624 = frozenset([26])
    FOLLOW_NEWLINE_in_receive626 = frozenset([21])
    FOLLOW_INDENT_in_receive628 = frozenset([26])
    FOLLOW_NEWLINE_in_receive630 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_receive632 = frozenset([13])
    FOLLOW_DEDENT_in_receive634 = frozenset([26])
    FOLLOW_NEWLINE_in_receive636 = frozenset([1])
    FOLLOW_RECEIVE_in_receive667 = frozenset([19])
    FOLLOW_ID_in_receive669 = frozenset([26])
    FOLLOW_NEWLINE_in_receive671 = frozenset([21])
    FOLLOW_INDENT_in_receive673 = frozenset([26])
    FOLLOW_NEWLINE_in_receive675 = frozenset([13, 28, 78])
    FOLLOW_local_vars_in_receive689 = frozenset([13, 28])
    FOLLOW_local_ops_in_receive693 = frozenset([13])
    FOLLOW_DEDENT_in_receive705 = frozenset([26])
    FOLLOW_NEWLINE_in_receive707 = frozenset([1])
    FOLLOW_PROC_in_proc753 = frozenset([19])
    FOLLOW_ID_in_proc755 = frozenset([26])
    FOLLOW_NEWLINE_in_proc757 = frozenset([1])
    FOLLOW_PROC_in_proc786 = frozenset([19])
    FOLLOW_ID_in_proc788 = frozenset([26])
    FOLLOW_NEWLINE_in_proc790 = frozenset([21])
    FOLLOW_INDENT_in_proc792 = frozenset([26])
    FOLLOW_NEWLINE_in_proc794 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_proc796 = frozenset([13])
    FOLLOW_DEDENT_in_proc798 = frozenset([26])
    FOLLOW_NEWLINE_in_proc800 = frozenset([1])
    FOLLOW_PROC_in_proc831 = frozenset([19])
    FOLLOW_ID_in_proc833 = frozenset([26])
    FOLLOW_NEWLINE_in_proc835 = frozenset([21])
    FOLLOW_INDENT_in_proc837 = frozenset([26])
    FOLLOW_NEWLINE_in_proc839 = frozenset([6, 13, 28, 78])
    FOLLOW_proc_args_in_proc853 = frozenset([13, 28, 78])
    FOLLOW_local_vars_in_proc857 = frozenset([13, 28])
    FOLLOW_local_ops_in_proc861 = frozenset([13])
    FOLLOW_DEDENT_in_proc873 = frozenset([26])
    FOLLOW_NEWLINE_in_proc875 = frozenset([1])
    FOLLOW_ARGS_in_proc_args925 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args927 = frozenset([1])
    FOLLOW_VARS_in_local_vars956 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_local_vars958 = frozenset([1])
    FOLLOW_OPS_in_local_ops987 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops989 = frozenset([21])
    FOLLOW_INDENT_in_local_ops991 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops993 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_local_ops995 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops997 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops999 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement1030 = frozenset([26])
    FOLLOW_NEWLINE_in_statement1032 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement1058 = frozenset([1])
    FOLLOW_statement_if_in_statement1068 = frozenset([1])
    FOLLOW_statement_assign_in_statement1078 = frozenset([1])
    FOLLOW_statement_while_in_statement1088 = frozenset([1])
    FOLLOW_statement_with_in_statement1098 = frozenset([1])
    FOLLOW_statement_in_statements1117 = frozenset([1, 18, 19, 20, 23, 27, 79, 81])
    FOLLOW_WITH_in_statement_with1159 = frozenset([19])
    FOLLOW_ID_in_statement_with1161 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1163 = frozenset([21])
    FOLLOW_INDENT_in_statement_with1173 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1175 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_with1177 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with1179 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with1181 = frozenset([1])
    FOLLOW_ID_in_statement_assign1221 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1225 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign1227 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign1231 = frozenset([1])
    FOLLOW_ID_in_statement_assign1284 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1288 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1290 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1292 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1294 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign1306 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign1310 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_assign1316 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1318 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1371 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1375 = frozenset([19])
    FOLLOW_ID_in_statement_assign1377 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1381 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1434 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1438 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1440 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1442 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1444 = frozenset([19])
    FOLLOW_ID_in_statement_assign1456 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1460 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1466 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1468 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1530 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1532 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1534 = frozenset([15])
    FOLLOW_DO_in_statement_while1538 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1540 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1554 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1556 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_while1558 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1560 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1562 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1602 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1612 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1624 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1732 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1734 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1766 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1768 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1800 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1802 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1806 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1808 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1822 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1824 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_elif_body1826 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1828 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1830 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1870 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1872 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1886 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1888 = frozenset([18, 19, 20, 23, 27, 79, 81])
    FOLLOW_statements_in_statement_else1890 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1892 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1894 = frozenset([1])
    FOLLOW_condition_call_in_condition1932 = frozenset([1])
    FOLLOW_ANY_in_condition1961 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1963 = frozenset([1])
    FOLLOW_ALL_in_condition1992 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1994 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls2032 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls2042 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls2044 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2046 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls2048 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls2052 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls2054 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call2088 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call2098 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line2117 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line2119 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line2145 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line2164 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line2166 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line2210 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line2212 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2216 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line2226 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2228 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line2232 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2234 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line2240 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line2242 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args2278 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value2295 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2305 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2315 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2325 = frozenset([1])
    FOLLOW_CONSTS_in_consts2344 = frozenset([19])
    FOLLOW_ID_in_consts2346 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2348 = frozenset([21])
    FOLLOW_INDENT_in_consts2358 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2360 = frozenset([19])
    FOLLOW_consts_items_in_consts2362 = frozenset([13])
    FOLLOW_DEDENT_in_consts2364 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2366 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2398 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2414 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2416 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2418 = frozenset([1])
    FOLLOW_ID_in_consts_item2440 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2442 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2444 = frozenset([1])
    FOLLOW_ID_in_consts_item2466 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2468 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2470 = frozenset([1])
    FOLLOW_TYPES_in_types2501 = frozenset([19])
    FOLLOW_ID_in_types2503 = frozenset([26])
    FOLLOW_NEWLINE_in_types2505 = frozenset([21])
    FOLLOW_INDENT_in_types2515 = frozenset([26])
    FOLLOW_NEWLINE_in_types2517 = frozenset([19])
    FOLLOW_types_item_in_types2519 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2523 = frozenset([26])
    FOLLOW_NEWLINE_in_types2525 = frozenset([1])
    FOLLOW_ID_in_types_item2559 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2561 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2588 = frozenset([19])
    FOLLOW_ID_in_messages2590 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2592 = frozenset([21])
    FOLLOW_INDENT_in_messages2602 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2604 = frozenset([19])
    FOLLOW_messages_item_in_messages2606 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2610 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2612 = frozenset([1])
    FOLLOW_ID_in_messages_item2646 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2648 = frozenset([1])
    FOLLOW_VARS_in_vars2675 = frozenset([19])
    FOLLOW_ID_in_vars2677 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars2679 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2718 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2720 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints2744 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2756 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2758 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2762 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2764 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2770 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2772 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2800 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2802 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2814 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2816 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2820 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2822 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2828 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2830 = frozenset([1])
    FOLLOW_ID_in_attr_hint2867 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2908 = frozenset([19])
    FOLLOW_ID_in_attr_hint2910 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2950 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2952 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2954 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2956 = frozenset([19])
    FOLLOW_ID_in_attr_hint2960 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2964 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2970 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3017 = frozenset([19])
    FOLLOW_ID_in_hint3019 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint3021 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint3041 = frozenset([19])
    FOLLOW_ID_in_hint3043 = frozenset([19, 77])
    FOLLOW_hint_arg_in_hint3045 = frozenset([11, 19, 77])
    FOLLOW_CURLY_CLOSE_in_hint3049 = frozenset([1])
    FOLLOW_MINUS_in_num_whole3088 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole3092 = frozenset([1])
    FOLLOW_MINUS_in_num_fract3100 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3104 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract3106 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract3108 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
