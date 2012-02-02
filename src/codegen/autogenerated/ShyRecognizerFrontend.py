# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-02 18:47:16

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
TREE_STATELESS=62
TREE_STATEMENTS=63
TREE_STATEMENT_ASSIGN=64
TREE_STATEMENT_ASSIGN_TO=65
TREE_STATEMENT_CALL=66
TREE_STATEMENT_ELIF=67
TREE_STATEMENT_ELSE=68
TREE_STATEMENT_IF=69
TREE_STATEMENT_WHILE=70
TREE_STATEMENT_WITH=71
TREE_TYPES=72
TREE_TYPES_ITEM=73
TREE_VARS=74
TYPES=75
UNDERSCORE=76
VARS=77
WHILE=78
WHITESPACE=79
WITH=80

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
    "TREE_PROC_ARGS", "TREE_RECEIVE", "TREE_STATELESS", "TREE_STATEMENTS", 
    "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", "TREE_STATEMENT_CALL", 
    "TREE_STATEMENT_ELIF", "TREE_STATEMENT_ELSE", "TREE_STATEMENT_IF", "TREE_STATEMENT_WHILE", 
    "TREE_STATEMENT_WITH", "TREE_TYPES", "TREE_TYPES_ITEM", "TREE_VARS", 
    "TYPES", "UNDERSCORE", "VARS", "WHILE", "WHITESPACE", "WITH"
]




class ShyRecognizerFrontend(Parser):
    grammarFileName = "grammar/ShyRecognizerFrontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ShyRecognizerFrontend, self).__init__(input, state, *args, **kwargs)

        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )

        self.dfa26 = self.DFA26(
            self, 26,
            eot = self.DFA26_eot,
            eof = self.DFA26_eof,
            min = self.DFA26_min,
            max = self.DFA26_max,
            accept = self.DFA26_accept,
            special = self.DFA26_special,
            transition = self.DFA26_transition
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

        self.dfa47 = self.DFA47(
            self, 47,
            eot = self.DFA47_eot,
            eof = self.DFA47_eof,
            min = self.DFA47_min,
            max = self.DFA47_max,
            accept = self.DFA47_accept,
            special = self.DFA47_special,
            transition = self.DFA47_transition
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
    # grammar/ShyRecognizerFrontend.g:26:1: module : MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* ( receive )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE7 = None
        ID8 = None
        NEWLINE9 = None
        INDENT10 = None
        NEWLINE11 = None
        DEDENT15 = None
        NEWLINE16 = None
        module_queue12 = None

        proc13 = None

        receive14 = None


        MODULE7_tree = None
        ID8_tree = None
        NEWLINE9_tree = None
        INDENT10_tree = None
        NEWLINE11_tree = None
        DEDENT15_tree = None
        NEWLINE16_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_module_queue = RewriteRuleSubtreeStream(self._adaptor, "rule module_queue")
        stream_receive = RewriteRuleSubtreeStream(self._adaptor, "rule receive")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:27:5: ( MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* ( receive )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* ) )
                # grammar/ShyRecognizerFrontend.g:27:9: MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* ( receive )* DEDENT NEWLINE
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


                DEDENT15 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_module175) 
                stream_DEDENT.add(DEDENT15)


                NEWLINE16 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module177) 
                stream_NEWLINE.add(NEWLINE16)


                # AST Rewrite
                # elements: proc, receive, module_queue, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 32:9: -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* )
                # grammar/ShyRecognizerFrontend.g:32:13: ^( TREE_MODULE ID ( module_queue )? ( proc )* ( receive )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MODULE, "TREE_MODULE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:33:17: ( module_queue )?
                if stream_module_queue.hasNext():
                    self._adaptor.addChild(root_1, stream_module_queue.nextTree())


                stream_module_queue.reset();

                # grammar/ShyRecognizerFrontend.g:34:17: ( proc )*
                while stream_proc.hasNext():
                    self._adaptor.addChild(root_1, stream_proc.nextTree())


                stream_proc.reset();

                # grammar/ShyRecognizerFrontend.g:35:17: ( receive )*
                while stream_receive.hasNext():
                    self._adaptor.addChild(root_1, stream_receive.nextTree())


                stream_receive.reset();

                self._adaptor.addChild(root_0, root_1)




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:39:1: module_queue : MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        retval = self.module_queue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE_QUEUE17 = None
        ID18 = None
        NEWLINE19 = None

        MODULE_QUEUE17_tree = None
        ID18_tree = None
        NEWLINE19_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE_QUEUE = RewriteRuleTokenStream(self._adaptor, "token MODULE_QUEUE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:40:5: ( MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerFrontend.g:40:9: MODULE_QUEUE ID NEWLINE
                pass 
                MODULE_QUEUE17 = self.match(self.input, MODULE_QUEUE, self.FOLLOW_MODULE_QUEUE_in_module_queue287) 
                stream_MODULE_QUEUE.add(MODULE_QUEUE17)


                ID18 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue289) 
                stream_ID.add(ID18)


                NEWLINE19 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module_queue291) 
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
                # 41:9: -> ^( TREE_MODULE_QUEUE ID )
                # grammar/ShyRecognizerFrontend.g:41:13: ^( TREE_MODULE_QUEUE ID )
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
    # grammar/ShyRecognizerFrontend.g:44:1: stateless : STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS20 = None
        ID21 = None
        NEWLINE22 = None
        INDENT23 = None
        NEWLINE24 = None
        DEDENT26 = None
        NEWLINE27 = None
        proc25 = None


        STATELESS20_tree = None
        ID21_tree = None
        NEWLINE22_tree = None
        INDENT23_tree = None
        NEWLINE24_tree = None
        DEDENT26_tree = None
        NEWLINE27_tree = None
        stream_STATELESS = RewriteRuleTokenStream(self._adaptor, "token STATELESS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:45:5: ( STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:45:9: STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                pass 
                STATELESS20 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless329) 
                stream_STATELESS.add(STATELESS20)


                ID21 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless331) 
                stream_ID.add(ID21)


                NEWLINE22 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless333) 
                stream_NEWLINE.add(NEWLINE22)


                # grammar/ShyRecognizerFrontend.g:45:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == INDENT) :
                    alt6 = 1
                if alt6 == 1:
                    # grammar/ShyRecognizerFrontend.g:45:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT23 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless337) 
                    stream_INDENT.add(INDENT23)


                    NEWLINE24 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless339) 
                    stream_NEWLINE.add(NEWLINE24)


                    # grammar/ShyRecognizerFrontend.g:45:47: ( proc )+
                    cnt5 = 0
                    while True: #loop5
                        alt5 = 2
                        LA5_0 = self.input.LA(1)

                        if (LA5_0 == PROC) :
                            alt5 = 1


                        if alt5 == 1:
                            # grammar/ShyRecognizerFrontend.g:45:47: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless341)
                            proc25 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc25.tree)



                        else:
                            if cnt5 >= 1:
                                break #loop5

                            eee = EarlyExitException(5, self.input)
                            raise eee

                        cnt5 += 1


                    DEDENT26 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless345) 
                    stream_DEDENT.add(DEDENT26)


                    NEWLINE27 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless347) 
                    stream_NEWLINE.add(NEWLINE27)





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
                # 46:9: -> ^( TREE_STATELESS ID ( proc )* )
                # grammar/ShyRecognizerFrontend.g:46:13: ^( TREE_STATELESS ID ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATELESS, "TREE_STATELESS")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:46:34: ( proc )*
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


    class receive_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.receive_return, self).__init__()

            self.tree = None





    # $ANTLR start "receive"
    # grammar/ShyRecognizerFrontend.g:49:1: receive : ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) );
    def receive(self, ):
        retval = self.receive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECEIVE28 = None
        ID29 = None
        NEWLINE30 = None
        RECEIVE31 = None
        ID32 = None
        NEWLINE33 = None
        INDENT34 = None
        NEWLINE35 = None
        DEDENT38 = None
        NEWLINE39 = None
        local_vars36 = None

        local_ops37 = None


        RECEIVE28_tree = None
        ID29_tree = None
        NEWLINE30_tree = None
        RECEIVE31_tree = None
        ID32_tree = None
        NEWLINE33_tree = None
        INDENT34_tree = None
        NEWLINE35_tree = None
        DEDENT38_tree = None
        NEWLINE39_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_RECEIVE = RewriteRuleTokenStream(self._adaptor, "token RECEIVE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_local_ops = RewriteRuleSubtreeStream(self._adaptor, "rule local_ops")
        stream_local_vars = RewriteRuleSubtreeStream(self._adaptor, "rule local_vars")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:50:5: ( RECEIVE ID NEWLINE -> ^( TREE_RECEIVE ID ) | RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? ) )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == RECEIVE) :
                    LA9_1 = self.input.LA(2)

                    if (LA9_1 == ID) :
                        LA9_2 = self.input.LA(3)

                        if (LA9_2 == NEWLINE) :
                            LA9_3 = self.input.LA(4)

                            if (LA9_3 == INDENT) :
                                alt9 = 2
                            elif (LA9_3 == DEDENT or LA9_3 == RECEIVE) :
                                alt9 = 1
                            else:
                                nvae = NoViableAltException("", 9, 3, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 9, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 9, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae


                if alt9 == 1:
                    # grammar/ShyRecognizerFrontend.g:50:9: RECEIVE ID NEWLINE
                    pass 
                    RECEIVE28 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive393) 
                    stream_RECEIVE.add(RECEIVE28)


                    ID29 = self.match(self.input, ID, self.FOLLOW_ID_in_receive395) 
                    stream_ID.add(ID29)


                    NEWLINE30 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive397) 
                    stream_NEWLINE.add(NEWLINE30)


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
                    # 51:9: -> ^( TREE_RECEIVE ID )
                    # grammar/ShyRecognizerFrontend.g:51:13: ^( TREE_RECEIVE ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt9 == 2:
                    # grammar/ShyRecognizerFrontend.g:52:9: RECEIVE ID NEWLINE INDENT NEWLINE ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    RECEIVE31 = self.match(self.input, RECEIVE, self.FOLLOW_RECEIVE_in_receive426) 
                    stream_RECEIVE.add(RECEIVE31)


                    ID32 = self.match(self.input, ID, self.FOLLOW_ID_in_receive428) 
                    stream_ID.add(ID32)


                    NEWLINE33 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive430) 
                    stream_NEWLINE.add(NEWLINE33)


                    INDENT34 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_receive432) 
                    stream_INDENT.add(INDENT34)


                    NEWLINE35 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive434) 
                    stream_NEWLINE.add(NEWLINE35)


                    # grammar/ShyRecognizerFrontend.g:53:13: ( local_vars )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == VARS) :
                        alt7 = 1
                    if alt7 == 1:
                        # grammar/ShyRecognizerFrontend.g:53:13: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_receive448)
                        local_vars36 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars36.tree)





                    # grammar/ShyRecognizerFrontend.g:53:26: ( local_ops )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == OPS) :
                        alt8 = 1
                    if alt8 == 1:
                        # grammar/ShyRecognizerFrontend.g:53:26: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_receive452)
                        local_ops37 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops37.tree)





                    DEDENT38 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_receive464) 
                    stream_DEDENT.add(DEDENT38)


                    NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_receive466) 
                    stream_NEWLINE.add(NEWLINE39)


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
                    # 55:9: -> ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:55:13: ^( TREE_RECEIVE ID ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_RECEIVE, "TREE_RECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:55:32: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:55:45: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:58:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC40 = None
        ID41 = None
        NEWLINE42 = None
        PROC43 = None
        ID44 = None
        NEWLINE45 = None
        INDENT46 = None
        NEWLINE47 = None
        DEDENT51 = None
        NEWLINE52 = None
        proc_args48 = None

        local_vars49 = None

        local_ops50 = None


        PROC40_tree = None
        ID41_tree = None
        NEWLINE42_tree = None
        PROC43_tree = None
        ID44_tree = None
        NEWLINE45_tree = None
        INDENT46_tree = None
        NEWLINE47_tree = None
        DEDENT51_tree = None
        NEWLINE52_tree = None
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
                # grammar/ShyRecognizerFrontend.g:59:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? ) )
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == PROC) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == ID) :
                        LA13_2 = self.input.LA(3)

                        if (LA13_2 == NEWLINE) :
                            LA13_3 = self.input.LA(4)

                            if (LA13_3 == INDENT) :
                                alt13 = 2
                            elif (LA13_3 == DEDENT or (PROC <= LA13_3 <= RECEIVE)) :
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
                    # grammar/ShyRecognizerFrontend.g:59:9: PROC ID NEWLINE
                    pass 
                    PROC40 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc512) 
                    stream_PROC.add(PROC40)


                    ID41 = self.match(self.input, ID, self.FOLLOW_ID_in_proc514) 
                    stream_ID.add(ID41)


                    NEWLINE42 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc516) 
                    stream_NEWLINE.add(NEWLINE42)


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
                    # 60:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:60:13: ^( TREE_PROC ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt13 == 2:
                    # grammar/ShyRecognizerFrontend.g:61:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( local_vars )? ( local_ops )? DEDENT NEWLINE
                    pass 
                    PROC43 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc545) 
                    stream_PROC.add(PROC43)


                    ID44 = self.match(self.input, ID, self.FOLLOW_ID_in_proc547) 
                    stream_ID.add(ID44)


                    NEWLINE45 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc549) 
                    stream_NEWLINE.add(NEWLINE45)


                    INDENT46 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc551) 
                    stream_INDENT.add(INDENT46)


                    NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc553) 
                    stream_NEWLINE.add(NEWLINE47)


                    # grammar/ShyRecognizerFrontend.g:62:13: ( proc_args )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == ARGS) :
                        alt10 = 1
                    if alt10 == 1:
                        # grammar/ShyRecognizerFrontend.g:62:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc567)
                        proc_args48 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args48.tree)





                    # grammar/ShyRecognizerFrontend.g:62:25: ( local_vars )?
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == VARS) :
                        alt11 = 1
                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:62:25: local_vars
                        pass 
                        self._state.following.append(self.FOLLOW_local_vars_in_proc571)
                        local_vars49 = self.local_vars()

                        self._state.following.pop()
                        stream_local_vars.add(local_vars49.tree)





                    # grammar/ShyRecognizerFrontend.g:62:38: ( local_ops )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == OPS) :
                        alt12 = 1
                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:62:38: local_ops
                        pass 
                        self._state.following.append(self.FOLLOW_local_ops_in_proc575)
                        local_ops50 = self.local_ops()

                        self._state.following.pop()
                        stream_local_ops.add(local_ops50.tree)





                    DEDENT51 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc587) 
                    stream_DEDENT.add(DEDENT51)


                    NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc589) 
                    stream_NEWLINE.add(NEWLINE52)


                    # AST Rewrite
                    # elements: local_ops, ID, local_vars, proc_args
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 64:9: -> ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    # grammar/ShyRecognizerFrontend.g:64:13: ^( TREE_PROC ID ( proc_args )? ( local_vars )? ( local_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:64:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:64:41: ( local_vars )?
                    if stream_local_vars.hasNext():
                        self._adaptor.addChild(root_1, stream_local_vars.nextTree())


                    stream_local_vars.reset();

                    # grammar/ShyRecognizerFrontend.g:64:54: ( local_ops )?
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
    # grammar/ShyRecognizerFrontend.g:67:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS53 = None
        attrs_hints54 = None


        ARGS53_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:68:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:68:9: ARGS attrs_hints
                pass 
                ARGS53 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args639) 
                stream_ARGS.add(ARGS53)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args641)
                attrs_hints54 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints54.tree)


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
                # 68:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:68:29: ^( TREE_PROC_ARGS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:71:1: local_vars : VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) ;
    def local_vars(self, ):
        retval = self.local_vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS55 = None
        attrs_hints56 = None


        VARS55_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:72:5: ( VARS attrs_hints -> ^( TREE_LOCAL_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:72:9: VARS attrs_hints
                pass 
                VARS55 = self.match(self.input, VARS, self.FOLLOW_VARS_in_local_vars670) 
                stream_VARS.add(VARS55)


                self._state.following.append(self.FOLLOW_attrs_hints_in_local_vars672)
                attrs_hints56 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints56.tree)


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
                # 72:26: -> ^( TREE_LOCAL_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:72:29: ^( TREE_LOCAL_VARS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:75:1: local_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
    def local_ops(self, ):
        retval = self.local_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS57 = None
        NEWLINE58 = None
        INDENT59 = None
        NEWLINE60 = None
        DEDENT62 = None
        NEWLINE63 = None
        statements61 = None


        OPS57_tree = None
        NEWLINE58_tree = None
        INDENT59_tree = None
        NEWLINE60_tree = None
        DEDENT62_tree = None
        NEWLINE63_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:76:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
                # grammar/ShyRecognizerFrontend.g:76:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                OPS57 = self.match(self.input, OPS, self.FOLLOW_OPS_in_local_ops701) 
                stream_OPS.add(OPS57)


                NEWLINE58 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops703) 
                stream_NEWLINE.add(NEWLINE58)


                INDENT59 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_local_ops705) 
                stream_INDENT.add(INDENT59)


                NEWLINE60 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops707) 
                stream_NEWLINE.add(NEWLINE60)


                self._state.following.append(self.FOLLOW_statements_in_local_ops709)
                statements61 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements61.tree)


                DEDENT62 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_local_ops711) 
                stream_DEDENT.add(DEDENT62)


                NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_local_ops713) 
                stream_NEWLINE.add(NEWLINE63)


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
                # 77:9: -> statements
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
    # grammar/ShyRecognizerFrontend.g:80:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE65 = None
        statement_call_single_line64 = None

        statement_call_multi_line66 = None

        statement_if67 = None

        statement_assign68 = None

        statement_while69 = None

        statement_with70 = None


        NEWLINE65_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:81:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt14 = 6
                alt14 = self.dfa14.predict(self.input)
                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:81:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement744)
                    statement_call_single_line64 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line64.tree)


                    NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement746) 
                    stream_NEWLINE.add(NEWLINE65)


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
                    # 82:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt14 == 2:
                    # grammar/ShyRecognizerFrontend.g:83:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement772)
                    statement_call_multi_line66 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line66.tree)



                elif alt14 == 3:
                    # grammar/ShyRecognizerFrontend.g:84:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement782)
                    statement_if67 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if67.tree)



                elif alt14 == 4:
                    # grammar/ShyRecognizerFrontend.g:85:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement792)
                    statement_assign68 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign68.tree)



                elif alt14 == 5:
                    # grammar/ShyRecognizerFrontend.g:86:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement802)
                    statement_while69 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while69.tree)



                elif alt14 == 6:
                    # grammar/ShyRecognizerFrontend.g:87:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement812)
                    statement_with70 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with70.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:90:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement71 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:91:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:91:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:91:9: ( statement )+
                cnt15 = 0
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA15_0 <= IF) or LA15_0 == MINUS or LA15_0 == NUMBER or LA15_0 == WHILE or LA15_0 == WITH) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:91:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements831)
                        statement71 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement71.tree)



                    else:
                        if cnt15 >= 1:
                            break #loop15

                        eee = EarlyExitException(15, self.input)
                        raise eee

                    cnt15 += 1


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
                # 92:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:92:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:92:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:95:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH72 = None
        ID73 = None
        NEWLINE74 = None
        INDENT75 = None
        NEWLINE76 = None
        DEDENT78 = None
        NEWLINE79 = None
        statements77 = None


        WITH72_tree = None
        ID73_tree = None
        NEWLINE74_tree = None
        INDENT75_tree = None
        NEWLINE76_tree = None
        DEDENT78_tree = None
        NEWLINE79_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:96:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:96:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH72 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with873) 
                stream_WITH.add(WITH72)


                ID73 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with875) 
                stream_ID.add(ID73)


                NEWLINE74 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with877) 
                stream_NEWLINE.add(NEWLINE74)


                INDENT75 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with887) 
                stream_INDENT.add(INDENT75)


                NEWLINE76 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with889) 
                stream_NEWLINE.add(NEWLINE76)


                self._state.following.append(self.FOLLOW_statements_in_statement_with891)
                statements77 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements77.tree)


                DEDENT78 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with893) 
                stream_DEDENT.add(DEDENT78)


                NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with895) 
                stream_NEWLINE.add(NEWLINE79)


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
                # 98:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:98:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:101:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID80 = None
        ARROW_LEFT81 = None
        NEWLINE83 = None
        ID84 = None
        ARROW_LEFT85 = None
        NEWLINE86 = None
        INDENT87 = None
        NEWLINE88 = None
        NEWLINE90 = None
        DEDENT91 = None
        NEWLINE92 = None
        ARROW_RIGHT94 = None
        ID95 = None
        NEWLINE96 = None
        ARROW_RIGHT98 = None
        NEWLINE99 = None
        INDENT100 = None
        NEWLINE101 = None
        ID102 = None
        NEWLINE103 = None
        DEDENT104 = None
        NEWLINE105 = None
        arbitrary_value82 = None

        arbitrary_value89 = None

        arbitrary_value93 = None

        arbitrary_value97 = None


        ID80_tree = None
        ARROW_LEFT81_tree = None
        NEWLINE83_tree = None
        ID84_tree = None
        ARROW_LEFT85_tree = None
        NEWLINE86_tree = None
        INDENT87_tree = None
        NEWLINE88_tree = None
        NEWLINE90_tree = None
        DEDENT91_tree = None
        NEWLINE92_tree = None
        ARROW_RIGHT94_tree = None
        ID95_tree = None
        NEWLINE96_tree = None
        ARROW_RIGHT98_tree = None
        NEWLINE99_tree = None
        INDENT100_tree = None
        NEWLINE101_tree = None
        ID102_tree = None
        NEWLINE103_tree = None
        DEDENT104_tree = None
        NEWLINE105_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:102:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt26 = 4
                alt26 = self.dfa26.predict(self.input)
                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:102:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:102:9: ( ID )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == ID) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:102:9: ID
                            pass 
                            ID80 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign935) 
                            stream_ID.add(ID80)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    ARROW_LEFT81 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign939) 
                    stream_ARROW_LEFT.add(ARROW_LEFT81)


                    # grammar/ShyRecognizerFrontend.g:102:25: ( arbitrary_value )+
                    cnt17 = 0
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA17_0 <= ID) or LA17_0 == MINUS or LA17_0 == NUMBER) :
                            alt17 = 1


                        if alt17 == 1:
                            # grammar/ShyRecognizerFrontend.g:102:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign941)
                            arbitrary_value82 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value82.tree)



                        else:
                            if cnt17 >= 1:
                                break #loop17

                            eee = EarlyExitException(17, self.input)
                            raise eee

                        cnt17 += 1


                    NEWLINE83 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign945) 
                    stream_NEWLINE.add(NEWLINE83)


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
                    # 103:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:103:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:103:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:104:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt26 == 2:
                    # grammar/ShyRecognizerFrontend.g:105:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:105:9: ( ID )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == ID) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerFrontend.g:105:9: ID
                            pass 
                            ID84 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign998) 
                            stream_ID.add(ID84)



                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


                    ARROW_LEFT85 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign1002) 
                    stream_ARROW_LEFT.add(ARROW_LEFT85)


                    NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1004) 
                    stream_NEWLINE.add(NEWLINE86)


                    INDENT87 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1006) 
                    stream_INDENT.add(INDENT87)


                    NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1008) 
                    stream_NEWLINE.add(NEWLINE88)


                    # grammar/ShyRecognizerFrontend.g:106:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt20 = 0
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER) :
                            alt20 = 1


                        if alt20 == 1:
                            # grammar/ShyRecognizerFrontend.g:106:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:106:11: ( arbitrary_value )+
                            cnt19 = 0
                            while True: #loop19
                                alt19 = 2
                                LA19_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                                    alt19 = 1


                                if alt19 == 1:
                                    # grammar/ShyRecognizerFrontend.g:106:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1020)
                                    arbitrary_value89 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value89.tree)



                                else:
                                    if cnt19 >= 1:
                                        break #loop19

                                    eee = EarlyExitException(19, self.input)
                                    raise eee

                                cnt19 += 1


                            NEWLINE90 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1024) 
                            stream_NEWLINE.add(NEWLINE90)



                        else:
                            if cnt20 >= 1:
                                break #loop20

                            eee = EarlyExitException(20, self.input)
                            raise eee

                        cnt20 += 1


                    DEDENT91 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1030) 
                    stream_DEDENT.add(DEDENT91)


                    NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1032) 
                    stream_NEWLINE.add(NEWLINE92)


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
                    # 107:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:107:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:107:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:108:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt26 == 3:
                    # grammar/ShyRecognizerFrontend.g:109:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:109:9: ( arbitrary_value )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:109:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1085)
                            arbitrary_value93 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value93.tree)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    ARROW_RIGHT94 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1089) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT94)


                    # grammar/ShyRecognizerFrontend.g:109:39: ( ID )+
                    cnt22 = 0
                    while True: #loop22
                        alt22 = 2
                        LA22_0 = self.input.LA(1)

                        if (LA22_0 == ID) :
                            alt22 = 1


                        if alt22 == 1:
                            # grammar/ShyRecognizerFrontend.g:109:39: ID
                            pass 
                            ID95 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1091) 
                            stream_ID.add(ID95)



                        else:
                            if cnt22 >= 1:
                                break #loop22

                            eee = EarlyExitException(22, self.input)
                            raise eee

                        cnt22 += 1


                    NEWLINE96 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1095) 
                    stream_NEWLINE.add(NEWLINE96)


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
                    # 110:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:110:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:110:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:111:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt26 == 4:
                    # grammar/ShyRecognizerFrontend.g:112:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:112:9: ( arbitrary_value )+
                    cnt23 = 0
                    while True: #loop23
                        alt23 = 2
                        LA23_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                            alt23 = 1


                        if alt23 == 1:
                            # grammar/ShyRecognizerFrontend.g:112:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign1148)
                            arbitrary_value97 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value97.tree)



                        else:
                            if cnt23 >= 1:
                                break #loop23

                            eee = EarlyExitException(23, self.input)
                            raise eee

                        cnt23 += 1


                    ARROW_RIGHT98 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1152) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT98)


                    NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1154) 
                    stream_NEWLINE.add(NEWLINE99)


                    INDENT100 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1156) 
                    stream_INDENT.add(INDENT100)


                    NEWLINE101 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1158) 
                    stream_NEWLINE.add(NEWLINE101)


                    # grammar/ShyRecognizerFrontend.g:113:9: ( ( ID )+ NEWLINE )+
                    cnt25 = 0
                    while True: #loop25
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == ID) :
                            alt25 = 1


                        if alt25 == 1:
                            # grammar/ShyRecognizerFrontend.g:113:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:113:11: ( ID )+
                            cnt24 = 0
                            while True: #loop24
                                alt24 = 2
                                LA24_0 = self.input.LA(1)

                                if (LA24_0 == ID) :
                                    alt24 = 1


                                if alt24 == 1:
                                    # grammar/ShyRecognizerFrontend.g:113:11: ID
                                    pass 
                                    ID102 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1170) 
                                    stream_ID.add(ID102)



                                else:
                                    if cnt24 >= 1:
                                        break #loop24

                                    eee = EarlyExitException(24, self.input)
                                    raise eee

                                cnt24 += 1


                            NEWLINE103 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1174) 
                            stream_NEWLINE.add(NEWLINE103)



                        else:
                            if cnt25 >= 1:
                                break #loop25

                            eee = EarlyExitException(25, self.input)
                            raise eee

                        cnt25 += 1


                    DEDENT104 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1180) 
                    stream_DEDENT.add(DEDENT104)


                    NEWLINE105 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1182) 
                    stream_NEWLINE.add(NEWLINE105)


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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:118:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE106 = None
        NEWLINE108 = None
        DO109 = None
        NEWLINE110 = None
        INDENT111 = None
        NEWLINE112 = None
        DEDENT114 = None
        NEWLINE115 = None
        condition107 = None

        statements113 = None


        WHILE106_tree = None
        NEWLINE108_tree = None
        DO109_tree = None
        NEWLINE110_tree = None
        INDENT111_tree = None
        NEWLINE112_tree = None
        DEDENT114_tree = None
        NEWLINE115_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:119:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:119:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE106 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1244) 
                stream_WHILE.add(WHILE106)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1246)
                condition107 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition107.tree)


                # grammar/ShyRecognizerFrontend.g:119:25: ( NEWLINE )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == NEWLINE) :
                    alt27 = 1
                if alt27 == 1:
                    # grammar/ShyRecognizerFrontend.g:119:25: NEWLINE
                    pass 
                    NEWLINE108 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1248) 
                    stream_NEWLINE.add(NEWLINE108)





                DO109 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1252) 
                stream_DO.add(DO109)


                NEWLINE110 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1254) 
                stream_NEWLINE.add(NEWLINE110)


                INDENT111 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1268) 
                stream_INDENT.add(INDENT111)


                NEWLINE112 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1270) 
                stream_NEWLINE.add(NEWLINE112)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1272)
                statements113 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements113.tree)


                DEDENT114 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1274) 
                stream_DEDENT.add(DEDENT114)


                NEWLINE115 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1276) 
                stream_NEWLINE.add(NEWLINE115)


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
                # 121:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:121:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:124:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head116 = None

        statement_elif117 = None

        statement_else118 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:125:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:125:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1316)
                statement_if_head116 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head116.tree)


                # grammar/ShyRecognizerFrontend.g:126:9: ( statement_elif )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == ELIF) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerFrontend.g:126:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1326)
                        statement_elif117 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif117.tree)



                    else:
                        break #loop28


                # grammar/ShyRecognizerFrontend.g:127:9: ( statement_else )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == ELSE) :
                    alt29 = 1
                if alt29 == 1:
                    # grammar/ShyRecognizerFrontend.g:127:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1338)
                    statement_else118 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else118.tree)





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
                # 128:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:128:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:130:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:131:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:135:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF119 = None
        statement_elif_body120 = None


        IF119_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:136:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:136:9: IF statement_elif_body
                pass 
                IF119 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1446) 
                stream_IF.add(IF119)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1448)
                statement_elif_body120 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body120.tree)


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
                # 137:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:140:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF121 = None
        statement_elif_body122 = None


        ELIF121_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:141:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:141:9: ELIF statement_elif_body
                pass 
                ELIF121 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1480) 
                stream_ELIF.add(ELIF121)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1482)
                statement_elif_body122 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body122.tree)


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
                # 142:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:145:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE124 = None
        DO125 = None
        NEWLINE126 = None
        INDENT127 = None
        NEWLINE128 = None
        DEDENT130 = None
        NEWLINE131 = None
        condition123 = None

        statements129 = None


        NEWLINE124_tree = None
        DO125_tree = None
        NEWLINE126_tree = None
        INDENT127_tree = None
        NEWLINE128_tree = None
        DEDENT130_tree = None
        NEWLINE131_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:146:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:146:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1514)
                condition123 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition123.tree)


                # grammar/ShyRecognizerFrontend.g:146:19: ( NEWLINE )?
                alt30 = 2
                LA30_0 = self.input.LA(1)

                if (LA30_0 == NEWLINE) :
                    alt30 = 1
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:146:19: NEWLINE
                    pass 
                    NEWLINE124 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1516) 
                    stream_NEWLINE.add(NEWLINE124)





                DO125 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1520) 
                stream_DO.add(DO125)


                NEWLINE126 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1522) 
                stream_NEWLINE.add(NEWLINE126)


                INDENT127 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1536) 
                stream_INDENT.add(INDENT127)


                NEWLINE128 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1538) 
                stream_NEWLINE.add(NEWLINE128)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1540)
                statements129 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements129.tree)


                DEDENT130 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1542) 
                stream_DEDENT.add(DEDENT130)


                NEWLINE131 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1544) 
                stream_NEWLINE.add(NEWLINE131)


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
                # 148:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:148:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:151:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE132 = None
        NEWLINE133 = None
        INDENT134 = None
        NEWLINE135 = None
        DEDENT137 = None
        NEWLINE138 = None
        statements136 = None


        ELSE132_tree = None
        NEWLINE133_tree = None
        INDENT134_tree = None
        NEWLINE135_tree = None
        DEDENT137_tree = None
        NEWLINE138_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:152:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:152:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE132 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1584) 
                stream_ELSE.add(ELSE132)


                NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1586) 
                stream_NEWLINE.add(NEWLINE133)


                INDENT134 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1600) 
                stream_INDENT.add(INDENT134)


                NEWLINE135 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1602) 
                stream_NEWLINE.add(NEWLINE135)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1604)
                statements136 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements136.tree)


                DEDENT137 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1606) 
                stream_DEDENT.add(DEDENT137)


                NEWLINE138 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1608) 
                stream_NEWLINE.add(NEWLINE138)


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
                # 154:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:154:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:157:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY140 = None
        ALL142 = None
        condition_call139 = None

        condition_calls141 = None

        condition_calls143 = None


        ANY140_tree = None
        ALL142_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:158:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt31 = 3
                LA31 = self.input.LA(1)
                if LA31 == ID:
                    alt31 = 1
                elif LA31 == ANY:
                    alt31 = 2
                elif LA31 == ALL:
                    alt31 = 3
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae


                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:158:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1646)
                    condition_call139 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call139.tree)


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
                    # 159:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:159:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt31 == 2:
                    # grammar/ShyRecognizerFrontend.g:160:9: ANY condition_calls
                    pass 
                    ANY140 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1675) 
                    stream_ANY.add(ANY140)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1677)
                    condition_calls141 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls141.tree)


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
                    # 161:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:161:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt31 == 3:
                    # grammar/ShyRecognizerFrontend.g:162:9: ALL condition_calls
                    pass 
                    ALL142 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1706) 
                    stream_ALL.add(ALL142)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1708)
                    condition_calls143 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls143.tree)


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
                    # 163:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:163:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:166:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE145 = None
        INDENT146 = None
        NEWLINE147 = None
        DEDENT149 = None
        NEWLINE150 = None
        condition_call144 = None

        condition_call_line148 = None


        NEWLINE145_tree = None
        INDENT146_tree = None
        NEWLINE147_tree = None
        DEDENT149_tree = None
        NEWLINE150_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:167:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == ID) :
                    alt33 = 1
                elif (LA33_0 == NEWLINE) :
                    alt33 = 2
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae


                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:167:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1746)
                    condition_call144 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call144.tree)



                elif alt33 == 2:
                    # grammar/ShyRecognizerFrontend.g:168:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE145 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1756) 
                    stream_NEWLINE.add(NEWLINE145)


                    INDENT146 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1758) 
                    stream_INDENT.add(INDENT146)


                    NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1760) 
                    stream_NEWLINE.add(NEWLINE147)


                    # grammar/ShyRecognizerFrontend.g:168:32: ( condition_call_line )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:168:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1762)
                            condition_call_line148 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line148.tree)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


                    DEDENT149 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1766) 
                    stream_DEDENT.add(DEDENT149)


                    NEWLINE150 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1768) 
                    stream_NEWLINE.add(NEWLINE150)


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
                    # 169:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:169:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:172:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line151 = None

        statement_call_multi_line152 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:173:5: ( statement_call_single_line | statement_call_multi_line )
                alt34 = 2
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:173:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1802)
                    statement_call_single_line151 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line151.tree)



                elif alt34 == 2:
                    # grammar/ShyRecognizerFrontend.g:174:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1812)
                    statement_call_multi_line152 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line152.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:177:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE154 = None
        statement_call_single_line153 = None

        statement_call_multi_line155 = None


        NEWLINE154_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:178:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt35 = 2
                alt35 = self.dfa35.predict(self.input)
                if alt35 == 1:
                    # grammar/ShyRecognizerFrontend.g:178:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1831)
                    statement_call_single_line153 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line153.tree)


                    NEWLINE154 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1833) 
                    stream_NEWLINE.add(NEWLINE154)


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
                    # 179:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt35 == 2:
                    # grammar/ShyRecognizerFrontend.g:180:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1859)
                    statement_call_multi_line155 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line155.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:183:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID156 = None
        statement_call_args157 = None


        ID156_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:184:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:184:9: ID ( statement_call_args )?
                pass 
                ID156 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1878) 
                stream_ID.add(ID156)


                # grammar/ShyRecognizerFrontend.g:184:12: ( statement_call_args )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if ((EXPRESSION <= LA36_0 <= ID) or LA36_0 == MINUS or LA36_0 == NUMBER) :
                    alt36 = 1
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:184:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1880)
                    statement_call_args157 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args157.tree)





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
                # 185:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:185:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:185:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:188:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID158 = None
        NEWLINE160 = None
        INDENT161 = None
        NEWLINE162 = None
        NEWLINE164 = None
        DEDENT165 = None
        NEWLINE166 = None
        statement_call_args159 = None

        statement_call_args163 = None


        ID158_tree = None
        NEWLINE160_tree = None
        INDENT161_tree = None
        NEWLINE162_tree = None
        NEWLINE164_tree = None
        DEDENT165_tree = None
        NEWLINE166_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:189:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:189:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID158 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1924) 
                stream_ID.add(ID158)


                # grammar/ShyRecognizerFrontend.g:189:12: ( statement_call_args )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if ((EXPRESSION <= LA37_0 <= ID) or LA37_0 == MINUS or LA37_0 == NUMBER) :
                    alt37 = 1
                if alt37 == 1:
                    # grammar/ShyRecognizerFrontend.g:189:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1926)
                    statement_call_args159 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args159.tree)





                NEWLINE160 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1930) 
                stream_NEWLINE.add(NEWLINE160)


                INDENT161 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1940) 
                stream_INDENT.add(INDENT161)


                NEWLINE162 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1942) 
                stream_NEWLINE.add(NEWLINE162)


                # grammar/ShyRecognizerFrontend.g:190:24: ( statement_call_args NEWLINE )+
                cnt38 = 0
                while True: #loop38
                    alt38 = 2
                    LA38_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA38_0 <= ID) or LA38_0 == MINUS or LA38_0 == NUMBER) :
                        alt38 = 1


                    if alt38 == 1:
                        # grammar/ShyRecognizerFrontend.g:190:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1946)
                        statement_call_args163 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args163.tree)


                        NEWLINE164 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1948) 
                        stream_NEWLINE.add(NEWLINE164)



                    else:
                        if cnt38 >= 1:
                            break #loop38

                        eee = EarlyExitException(38, self.input)
                        raise eee

                    cnt38 += 1


                DEDENT165 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1954) 
                stream_DEDENT.add(DEDENT165)


                NEWLINE166 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1956) 
                stream_NEWLINE.add(NEWLINE166)


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
                # 191:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:191:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:191:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:194:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value167 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:194:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:194:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:194:23: ( arbitrary_value )+
                cnt39 = 0
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA39_0 <= ID) or LA39_0 == MINUS or LA39_0 == NUMBER) :
                        alt39 = 1


                    if alt39 == 1:
                        # grammar/ShyRecognizerFrontend.g:194:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1992)
                        arbitrary_value167 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value167.tree)



                    else:
                        if cnt39 >= 1:
                            break #loop39

                        eee = EarlyExitException(39, self.input)
                        raise eee

                    cnt39 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:196:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID168 = None
        EXPRESSION169 = None
        num_whole170 = None

        num_fract171 = None


        ID168_tree = None
        EXPRESSION169_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:197:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt40 = 4
                LA40 = self.input.LA(1)
                if LA40 == ID:
                    alt40 = 1
                elif LA40 == EXPRESSION:
                    alt40 = 2
                elif LA40 == MINUS:
                    LA40_3 = self.input.LA(2)

                    if (LA40_3 == NUMBER) :
                        LA40_4 = self.input.LA(3)

                        if (LA40_4 == DIVIDE) :
                            alt40 = 4
                        elif (LA40_4 == ARROW_RIGHT or LA40_4 == DO or (EXPRESSION <= LA40_4 <= ID) or LA40_4 == MINUS or (NEWLINE <= LA40_4 <= NUMBER)) :
                            alt40 = 3
                        else:
                            nvae = NoViableAltException("", 40, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 40, 3, self.input)

                        raise nvae


                elif LA40 == NUMBER:
                    LA40_4 = self.input.LA(2)

                    if (LA40_4 == DIVIDE) :
                        alt40 = 4
                    elif (LA40_4 == ARROW_RIGHT or LA40_4 == DO or (EXPRESSION <= LA40_4 <= ID) or LA40_4 == MINUS or (NEWLINE <= LA40_4 <= NUMBER)) :
                        alt40 = 3
                    else:
                        nvae = NoViableAltException("", 40, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae


                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:197:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID168 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value2009)
                    ID168_tree = self._adaptor.createWithPayload(ID168)
                    self._adaptor.addChild(root_0, ID168_tree)




                elif alt40 == 2:
                    # grammar/ShyRecognizerFrontend.g:198:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION169 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value2019)
                    EXPRESSION169_tree = self._adaptor.createWithPayload(EXPRESSION169)
                    self._adaptor.addChild(root_0, EXPRESSION169_tree)




                elif alt40 == 3:
                    # grammar/ShyRecognizerFrontend.g:199:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value2029)
                    num_whole170 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole170.tree)



                elif alt40 == 4:
                    # grammar/ShyRecognizerFrontend.g:200:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value2039)
                    num_fract171 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract171.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:203:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS172 = None
        ID173 = None
        NEWLINE174 = None
        INDENT175 = None
        NEWLINE176 = None
        DEDENT178 = None
        NEWLINE179 = None
        consts_items177 = None


        CONSTS172_tree = None
        ID173_tree = None
        NEWLINE174_tree = None
        INDENT175_tree = None
        NEWLINE176_tree = None
        DEDENT178_tree = None
        NEWLINE179_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:204:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:204:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS172 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts2058) 
                stream_CONSTS.add(CONSTS172)


                ID173 = self.match(self.input, ID, self.FOLLOW_ID_in_consts2060) 
                stream_ID.add(ID173)


                NEWLINE174 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2062) 
                stream_NEWLINE.add(NEWLINE174)


                INDENT175 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts2072) 
                stream_INDENT.add(INDENT175)


                NEWLINE176 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2074) 
                stream_NEWLINE.add(NEWLINE176)


                self._state.following.append(self.FOLLOW_consts_items_in_consts2076)
                consts_items177 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items177.tree)


                DEDENT178 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts2078) 
                stream_DEDENT.add(DEDENT178)


                NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts2080) 
                stream_NEWLINE.add(NEWLINE179)


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
                # 206:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:206:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:208:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item180 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:208:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:208:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:208:16: ( consts_item )+
                cnt41 = 0
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if (LA41_0 == ID) :
                        alt41 = 1


                    if alt41 == 1:
                        # grammar/ShyRecognizerFrontend.g:208:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items2112)
                        consts_item180 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item180.tree)



                    else:
                        if cnt41 >= 1:
                            break #loop41

                        eee = EarlyExitException(41, self.input)
                        raise eee

                    cnt41 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:209:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID181 = None
        NEWLINE183 = None
        ID184 = None
        NEWLINE186 = None
        ID187 = None
        EXPRESSION188 = None
        NEWLINE189 = None
        num_whole182 = None

        num_fract185 = None


        ID181_tree = None
        NEWLINE183_tree = None
        ID184_tree = None
        NEWLINE186_tree = None
        ID187_tree = None
        EXPRESSION188_tree = None
        NEWLINE189_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:210:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt42 = 3
                LA42_0 = self.input.LA(1)

                if (LA42_0 == ID) :
                    LA42 = self.input.LA(2)
                    if LA42 == EXPRESSION:
                        alt42 = 3
                    elif LA42 == MINUS:
                        LA42_3 = self.input.LA(3)

                        if (LA42_3 == NUMBER) :
                            LA42_4 = self.input.LA(4)

                            if (LA42_4 == DIVIDE) :
                                alt42 = 2
                            elif (LA42_4 == NEWLINE) :
                                alt42 = 1
                            else:
                                nvae = NoViableAltException("", 42, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 42, 3, self.input)

                            raise nvae


                    elif LA42 == NUMBER:
                        LA42_4 = self.input.LA(3)

                        if (LA42_4 == DIVIDE) :
                            alt42 = 2
                        elif (LA42_4 == NEWLINE) :
                            alt42 = 1
                        else:
                            nvae = NoViableAltException("", 42, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 42, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae


                if alt42 == 1:
                    # grammar/ShyRecognizerFrontend.g:210:9: ID num_whole NEWLINE
                    pass 
                    ID181 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2128) 
                    stream_ID.add(ID181)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item2130)
                    num_whole182 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole182.tree)


                    NEWLINE183 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2132) 
                    stream_NEWLINE.add(NEWLINE183)


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
                    # 210:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:210:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt42 == 2:
                    # grammar/ShyRecognizerFrontend.g:211:9: ID num_fract NEWLINE
                    pass 
                    ID184 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2154) 
                    stream_ID.add(ID184)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2156)
                    num_fract185 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract185.tree)


                    NEWLINE186 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2158) 
                    stream_NEWLINE.add(NEWLINE186)


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
                    # 211:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:211:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt42 == 3:
                    # grammar/ShyRecognizerFrontend.g:212:9: ID EXPRESSION NEWLINE
                    pass 
                    ID187 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2180) 
                    stream_ID.add(ID187)


                    EXPRESSION188 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2182) 
                    stream_EXPRESSION.add(EXPRESSION188)


                    NEWLINE189 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2184) 
                    stream_NEWLINE.add(NEWLINE189)


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
                    # 212:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:212:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:215:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES190 = None
        ID191 = None
        NEWLINE192 = None
        INDENT193 = None
        NEWLINE194 = None
        DEDENT196 = None
        NEWLINE197 = None
        types_item195 = None


        TYPES190_tree = None
        ID191_tree = None
        NEWLINE192_tree = None
        INDENT193_tree = None
        NEWLINE194_tree = None
        DEDENT196_tree = None
        NEWLINE197_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:216:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:216:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES190 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2215) 
                stream_TYPES.add(TYPES190)


                ID191 = self.match(self.input, ID, self.FOLLOW_ID_in_types2217) 
                stream_ID.add(ID191)


                NEWLINE192 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2219) 
                stream_NEWLINE.add(NEWLINE192)


                INDENT193 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2229) 
                stream_INDENT.add(INDENT193)


                NEWLINE194 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2231) 
                stream_NEWLINE.add(NEWLINE194)


                # grammar/ShyRecognizerFrontend.g:217:24: ( types_item )+
                cnt43 = 0
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == ID) :
                        alt43 = 1


                    if alt43 == 1:
                        # grammar/ShyRecognizerFrontend.g:217:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2233)
                        types_item195 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item195.tree)



                    else:
                        if cnt43 >= 1:
                            break #loop43

                        eee = EarlyExitException(43, self.input)
                        raise eee

                    cnt43 += 1


                DEDENT196 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2237) 
                stream_DEDENT.add(DEDENT196)


                NEWLINE197 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2239) 
                stream_NEWLINE.add(NEWLINE197)


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
                # 218:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:218:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:218:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:220:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID198 = None
        attrs_hints199 = None


        ID198_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:220:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:220:14: ID attrs_hints
                pass 
                ID198 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2273) 
                stream_ID.add(ID198)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2275)
                attrs_hints199 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints199.tree)


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
                # 220:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:220:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:222:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES200 = None
        ID201 = None
        NEWLINE202 = None
        INDENT203 = None
        NEWLINE204 = None
        DEDENT206 = None
        NEWLINE207 = None
        messages_item205 = None


        MESSAGES200_tree = None
        ID201_tree = None
        NEWLINE202_tree = None
        INDENT203_tree = None
        NEWLINE204_tree = None
        DEDENT206_tree = None
        NEWLINE207_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:223:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:223:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES200 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2302) 
                stream_MESSAGES.add(MESSAGES200)


                ID201 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2304) 
                stream_ID.add(ID201)


                NEWLINE202 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2306) 
                stream_NEWLINE.add(NEWLINE202)


                INDENT203 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2316) 
                stream_INDENT.add(INDENT203)


                NEWLINE204 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2318) 
                stream_NEWLINE.add(NEWLINE204)


                # grammar/ShyRecognizerFrontend.g:224:24: ( messages_item )+
                cnt44 = 0
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == ID) :
                        alt44 = 1


                    if alt44 == 1:
                        # grammar/ShyRecognizerFrontend.g:224:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2320)
                        messages_item205 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item205.tree)



                    else:
                        if cnt44 >= 1:
                            break #loop44

                        eee = EarlyExitException(44, self.input)
                        raise eee

                    cnt44 += 1


                DEDENT206 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2324) 
                stream_DEDENT.add(DEDENT206)


                NEWLINE207 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2326) 
                stream_NEWLINE.add(NEWLINE207)


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
                # 225:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:225:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:225:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:227:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID208 = None
        attrs_hints209 = None


        ID208_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:227:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:227:17: ID attrs_hints
                pass 
                ID208 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2360) 
                stream_ID.add(ID208)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2362)
                attrs_hints209 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints209.tree)


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
                # 227:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:227:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:229:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS210 = None
        ID211 = None
        attrs_hints212 = None


        VARS210_tree = None
        ID211_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:230:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:230:9: VARS ID attrs_hints
                pass 
                VARS210 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars2389) 
                stream_VARS.add(VARS210)


                ID211 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2391) 
                stream_ID.add(ID211)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2393)
                attrs_hints212 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints212.tree)


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
                # 231:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:231:12: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:234:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE214 = None
        NEWLINE215 = None
        INDENT216 = None
        NEWLINE217 = None
        NEWLINE219 = None
        DEDENT220 = None
        NEWLINE221 = None
        NEWLINE223 = None
        INDENT224 = None
        NEWLINE225 = None
        NEWLINE227 = None
        DEDENT228 = None
        NEWLINE229 = None
        attr_hint213 = None

        attr_hint218 = None

        attr_hint222 = None

        attr_hint226 = None


        NEWLINE214_tree = None
        NEWLINE215_tree = None
        INDENT216_tree = None
        NEWLINE217_tree = None
        NEWLINE219_tree = None
        DEDENT220_tree = None
        NEWLINE221_tree = None
        NEWLINE223_tree = None
        INDENT224_tree = None
        NEWLINE225_tree = None
        NEWLINE227_tree = None
        DEDENT228_tree = None
        NEWLINE229_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:235:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt47 = 3
                alt47 = self.dfa47.predict(self.input)
                if alt47 == 1:
                    # grammar/ShyRecognizerFrontend.g:235:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2432)
                    attr_hint213 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint213.tree)


                    NEWLINE214 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2434) 
                    stream_NEWLINE.add(NEWLINE214)


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
                    # 236:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt47 == 2:
                    # grammar/ShyRecognizerFrontend.g:237:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE215 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2458) 
                    stream_NEWLINE.add(NEWLINE215)


                    # grammar/ShyRecognizerFrontend.g:238:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:238:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT216 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2470) 
                    stream_INDENT.add(INDENT216)


                    NEWLINE217 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2472) 
                    stream_NEWLINE.add(NEWLINE217)


                    # grammar/ShyRecognizerFrontend.g:238:26: ( attr_hint NEWLINE )+
                    cnt45 = 0
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == CURLY_OPEN or LA45_0 == ID) :
                            alt45 = 1


                        if alt45 == 1:
                            # grammar/ShyRecognizerFrontend.g:238:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2476)
                            attr_hint218 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint218.tree)


                            NEWLINE219 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2478) 
                            stream_NEWLINE.add(NEWLINE219)



                        else:
                            if cnt45 >= 1:
                                break #loop45

                            eee = EarlyExitException(45, self.input)
                            raise eee

                        cnt45 += 1


                    DEDENT220 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2484) 
                    stream_DEDENT.add(DEDENT220)


                    NEWLINE221 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2486) 
                    stream_NEWLINE.add(NEWLINE221)





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
                    # 239:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:239:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt47 == 3:
                    # grammar/ShyRecognizerFrontend.g:240:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2514)
                    attr_hint222 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint222.tree)


                    NEWLINE223 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2516) 
                    stream_NEWLINE.add(NEWLINE223)


                    # grammar/ShyRecognizerFrontend.g:241:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:241:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT224 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2528) 
                    stream_INDENT.add(INDENT224)


                    NEWLINE225 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2530) 
                    stream_NEWLINE.add(NEWLINE225)


                    # grammar/ShyRecognizerFrontend.g:241:26: ( attr_hint NEWLINE )+
                    cnt46 = 0
                    while True: #loop46
                        alt46 = 2
                        LA46_0 = self.input.LA(1)

                        if (LA46_0 == CURLY_OPEN or LA46_0 == ID) :
                            alt46 = 1


                        if alt46 == 1:
                            # grammar/ShyRecognizerFrontend.g:241:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2534)
                            attr_hint226 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint226.tree)


                            NEWLINE227 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2536) 
                            stream_NEWLINE.add(NEWLINE227)



                        else:
                            if cnt46 >= 1:
                                break #loop46

                            eee = EarlyExitException(46, self.input)
                            raise eee

                        cnt46 += 1


                    DEDENT228 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2542) 
                    stream_DEDENT.add(DEDENT228)


                    NEWLINE229 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2544) 
                    stream_NEWLINE.add(NEWLINE229)





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
                    # 242:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:242:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:244:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID230 = None
        ID232 = None
        NEWLINE234 = None
        INDENT235 = None
        NEWLINE236 = None
        ID237 = None
        NEWLINE238 = None
        DEDENT239 = None
        hint231 = None

        hint233 = None


        ID230_tree = None
        ID232_tree = None
        NEWLINE234_tree = None
        INDENT235_tree = None
        NEWLINE236_tree = None
        ID237_tree = None
        NEWLINE238_tree = None
        DEDENT239_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:245:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt52 = 3
                alt52 = self.dfa52.predict(self.input)
                if alt52 == 1:
                    # grammar/ShyRecognizerFrontend.g:245:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:245:9: ( ID )+
                    cnt48 = 0
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == ID) :
                            alt48 = 1


                        if alt48 == 1:
                            # grammar/ShyRecognizerFrontend.g:245:9: ID
                            pass 
                            ID230 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2581) 
                            stream_ID.add(ID230)



                        else:
                            if cnt48 >= 1:
                                break #loop48

                            eee = EarlyExitException(48, self.input)
                            raise eee

                        cnt48 += 1


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
                    # 246:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:246:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:246:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:246:45: ^( TREE_ATTR ID )
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




                elif alt52 == 2:
                    # grammar/ShyRecognizerFrontend.g:247:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2622)
                    hint231 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint231.tree)


                    # grammar/ShyRecognizerFrontend.g:247:14: ( ID )+
                    cnt49 = 0
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == ID) :
                            alt49 = 1


                        if alt49 == 1:
                            # grammar/ShyRecognizerFrontend.g:247:14: ID
                            pass 
                            ID232 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2624) 
                            stream_ID.add(ID232)



                        else:
                            if cnt49 >= 1:
                                break #loop49

                            eee = EarlyExitException(49, self.input)
                            raise eee

                        cnt49 += 1


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
                    # 248:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:248:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:248:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:248:35: ^( TREE_ATTR ID )
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




                elif alt52 == 3:
                    # grammar/ShyRecognizerFrontend.g:249:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2664)
                    hint233 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint233.tree)


                    NEWLINE234 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2666) 
                    stream_NEWLINE.add(NEWLINE234)


                    INDENT235 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2668) 
                    stream_INDENT.add(INDENT235)


                    NEWLINE236 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2670) 
                    stream_NEWLINE.add(NEWLINE236)


                    # grammar/ShyRecognizerFrontend.g:249:37: ( ( ID )+ NEWLINE )+
                    cnt51 = 0
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == ID) :
                            alt51 = 1


                        if alt51 == 1:
                            # grammar/ShyRecognizerFrontend.g:249:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:249:39: ( ID )+
                            cnt50 = 0
                            while True: #loop50
                                alt50 = 2
                                LA50_0 = self.input.LA(1)

                                if (LA50_0 == ID) :
                                    alt50 = 1


                                if alt50 == 1:
                                    # grammar/ShyRecognizerFrontend.g:249:39: ID
                                    pass 
                                    ID237 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2674) 
                                    stream_ID.add(ID237)



                                else:
                                    if cnt50 >= 1:
                                        break #loop50

                                    eee = EarlyExitException(50, self.input)
                                    raise eee

                                cnt50 += 1


                            NEWLINE238 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2678) 
                            stream_NEWLINE.add(NEWLINE238)



                        else:
                            if cnt51 >= 1:
                                break #loop51

                            eee = EarlyExitException(51, self.input)
                            raise eee

                        cnt51 += 1


                    DEDENT239 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2684) 
                    stream_DEDENT.add(DEDENT239)


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
                    # 250:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:250:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:250:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:250:35: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:253:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN240 = None
        ID241 = None
        CURLY_CLOSE242 = None
        CURLY_OPEN243 = None
        ID244 = None
        CURLY_CLOSE246 = None
        hint_arg245 = None


        CURLY_OPEN240_tree = None
        ID241_tree = None
        CURLY_CLOSE242_tree = None
        CURLY_OPEN243_tree = None
        ID244_tree = None
        CURLY_CLOSE246_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:254:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt54 = 2
                LA54_0 = self.input.LA(1)

                if (LA54_0 == CURLY_OPEN) :
                    LA54_1 = self.input.LA(2)

                    if (LA54_1 == ID) :
                        LA54_2 = self.input.LA(3)

                        if (LA54_2 == CURLY_CLOSE) :
                            alt54 = 1
                        elif (LA54_2 == ID or LA54_2 == UNDERSCORE) :
                            alt54 = 2
                        else:
                            nvae = NoViableAltException("", 54, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 54, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 54, 0, self.input)

                    raise nvae


                if alt54 == 1:
                    # grammar/ShyRecognizerFrontend.g:254:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN240 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2731) 
                    stream_CURLY_OPEN.add(CURLY_OPEN240)


                    ID241 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2733) 
                    stream_ID.add(ID241)


                    CURLY_CLOSE242 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2735) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE242)


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
                    # 254:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:254:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt54 == 2:
                    # grammar/ShyRecognizerFrontend.g:255:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN243 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2755) 
                    stream_CURLY_OPEN.add(CURLY_OPEN243)


                    ID244 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2757) 
                    stream_ID.add(ID244)


                    # grammar/ShyRecognizerFrontend.g:255:23: ( hint_arg )+
                    cnt53 = 0
                    while True: #loop53
                        alt53 = 2
                        LA53_0 = self.input.LA(1)

                        if (LA53_0 == ID or LA53_0 == UNDERSCORE) :
                            alt53 = 1


                        if alt53 == 1:
                            # grammar/ShyRecognizerFrontend.g:255:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2759)
                            hint_arg245 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg245.tree)



                        else:
                            if cnt53 >= 1:
                                break #loop53

                            eee = EarlyExitException(53, self.input)
                            raise eee

                        cnt53 += 1


                    CURLY_CLOSE246 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2763) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE246)


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
                    # 255:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:255:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:255:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:257:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set247 = None

        set247_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:257:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set247 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set247))

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
    # grammar/ShyRecognizerFrontend.g:259:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS248 = None
        NUMBER249 = None

        MINUS248_tree = None
        NUMBER249_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:259:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:259:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:259:13: ( MINUS )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == MINUS) :
                    alt55 = 1
                if alt55 == 1:
                    # grammar/ShyRecognizerFrontend.g:259:13: MINUS
                    pass 
                    MINUS248 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2802)
                    MINUS248_tree = self._adaptor.createWithPayload(MINUS248)
                    self._adaptor.addChild(root_0, MINUS248_tree)






                NUMBER249 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2806)
                NUMBER249_tree = self._adaptor.createWithPayload(NUMBER249)
                self._adaptor.addChild(root_0, NUMBER249_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:260:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS250 = None
        NUMBER251 = None
        DIVIDE252 = None
        NUMBER253 = None

        MINUS250_tree = None
        NUMBER251_tree = None
        DIVIDE252_tree = None
        NUMBER253_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:260:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:260:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:260:13: ( MINUS )?
                alt56 = 2
                LA56_0 = self.input.LA(1)

                if (LA56_0 == MINUS) :
                    alt56 = 1
                if alt56 == 1:
                    # grammar/ShyRecognizerFrontend.g:260:13: MINUS
                    pass 
                    MINUS250 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2814)
                    MINUS250_tree = self._adaptor.createWithPayload(MINUS250)
                    self._adaptor.addChild(root_0, MINUS250_tree)






                NUMBER251 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2818)
                NUMBER251_tree = self._adaptor.createWithPayload(NUMBER251)
                self._adaptor.addChild(root_0, NUMBER251_tree)



                DIVIDE252 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2820)
                DIVIDE252_tree = self._adaptor.createWithPayload(DIVIDE252)
                self._adaptor.addChild(root_0, DIVIDE252_tree)



                NUMBER253 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2822)
                NUMBER253_tree = self._adaptor.createWithPayload(NUMBER253)
                self._adaptor.addChild(root_0, NUMBER253_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\20\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\22\1\7\4\uffff\1\7\1\10\1\33\1\10\1\15\1\10\1\33\2\uffff\1\10"
        )

    DFA14_max = DFA.unpack(
        u"\1\120\1\33\4\uffff\4\33\1\120\2\33\2\uffff\1\33"
        )

    DFA14_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\7\uffff\1\2\1\1\1\uffff"
        )

    DFA14_special = DFA.unpack(
        u"\20\uffff"
        )


    DFA14_transition = [
        DFA.unpack(u"\1\3\1\1\1\2\2\uffff\1\3\3\uffff\1\3\62\uffff\1\4\1"
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
        DFA.unpack(u"\1\16\4\uffff\3\16\1\15\1\uffff\1\16\3\uffff\1\16\62"
        u"\uffff\1\16\1\uffff\1\16"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\13\3\uffff\1\10\2\uffff\1\12\1"
        u"\11"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\13\3\uffff\1\10\2\uffff\1\12\1"
        u"\11")
    ]

    # class definition for DFA #14

    class DFA14(DFA):
        pass


    # lookup tables for DFA #26

    DFA26_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA26_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA26_min = DFA.unpack(
        u"\1\22\1\7\1\10\1\33\1\10\1\22\1\23\1\10\1\33\4\uffff\1\10"
        )

    DFA26_max = DFA.unpack(
        u"\6\33\1\32\2\33\4\uffff\1\33"
        )

    DFA26_accept = DFA.unpack(
        u"\11\uffff\1\2\1\1\1\4\1\3\1\uffff"
        )

    DFA26_special = DFA.unpack(
        u"\16\uffff"
        )


    DFA26_transition = [
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

    # class definition for DFA #26

    class DFA26(DFA):
        pass


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\1\23\3\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA34_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\uffff\1\33\1\uffff\1\33"
        )

    DFA34_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA34_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA34_transition = [
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

    # class definition for DFA #34

    class DFA34(DFA):
        pass


    # lookup tables for DFA #35

    DFA35_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA35_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA35_min = DFA.unpack(
        u"\1\23\3\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA35_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\33\2\uffff\1\33"
        )

    DFA35_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA35_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA35_transition = [
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

    # class definition for DFA #35

    class DFA35(DFA):
        pass


    # lookup tables for DFA #47

    DFA47_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA47_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA47_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA47_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\115\1\114\2\uffff\1\32\1\114\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA47_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA47_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA47_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1\6\uffff\1\3"),
        DFA.unpack(u"\1\1\6\uffff\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\6\5\uffff\1\6\1\uffff\1\7\1\6\1\uffff"
        u"\1\6\3\uffff\1\6\6\uffff\1\6\47\uffff\1\6\1\uffff\1\6"),
        DFA.unpack(u"\1\10\7\uffff\1\11\70\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\14\7\uffff\1\11\70\uffff\1\11"),
        DFA.unpack(u"\1\12\6\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\17\6\uffff\1\20"),
        DFA.unpack(u"\1\21\5\uffff\1\17"),
        DFA.unpack(u"\1\4")
    ]

    # class definition for DFA #47

    class DFA47(DFA):
        pass


    # lookup tables for DFA #52

    DFA52_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA52_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA52_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA52_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\114\1\32\1\114\2\uffff\1\32"
        )

    DFA52_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA52_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA52_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\7\uffff\1\5\70\uffff\1\5"),
        DFA.unpack(u"\1\6\6\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\70\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\6\uffff\1\7")
    ]

    # class definition for DFA #52

    class DFA52(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 22, 24, 35, 75, 77])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 22, 24, 35, 75, 77])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 22, 24, 35, 75, 77])
    FOLLOW_types_in_start94 = frozenset([1, 9, 22, 24, 35, 75, 77])
    FOLLOW_messages_in_start98 = frozenset([1, 9, 22, 24, 35, 75, 77])
    FOLLOW_vars_in_start102 = frozenset([1, 9, 22, 24, 35, 75, 77])
    FOLLOW_MODULE_in_module121 = frozenset([19])
    FOLLOW_ID_in_module123 = frozenset([26])
    FOLLOW_NEWLINE_in_module125 = frozenset([21])
    FOLLOW_INDENT_in_module127 = frozenset([26])
    FOLLOW_NEWLINE_in_module129 = frozenset([13, 25, 30, 31])
    FOLLOW_module_queue_in_module139 = frozenset([13, 30, 31])
    FOLLOW_proc_in_module151 = frozenset([13, 30, 31])
    FOLLOW_receive_in_module163 = frozenset([13, 31])
    FOLLOW_DEDENT_in_module175 = frozenset([26])
    FOLLOW_NEWLINE_in_module177 = frozenset([1])
    FOLLOW_MODULE_QUEUE_in_module_queue287 = frozenset([19])
    FOLLOW_ID_in_module_queue289 = frozenset([26])
    FOLLOW_NEWLINE_in_module_queue291 = frozenset([1])
    FOLLOW_STATELESS_in_stateless329 = frozenset([19])
    FOLLOW_ID_in_stateless331 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless333 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless337 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless339 = frozenset([30])
    FOLLOW_proc_in_stateless341 = frozenset([13, 30])
    FOLLOW_DEDENT_in_stateless345 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless347 = frozenset([1])
    FOLLOW_RECEIVE_in_receive393 = frozenset([19])
    FOLLOW_ID_in_receive395 = frozenset([26])
    FOLLOW_NEWLINE_in_receive397 = frozenset([1])
    FOLLOW_RECEIVE_in_receive426 = frozenset([19])
    FOLLOW_ID_in_receive428 = frozenset([26])
    FOLLOW_NEWLINE_in_receive430 = frozenset([21])
    FOLLOW_INDENT_in_receive432 = frozenset([26])
    FOLLOW_NEWLINE_in_receive434 = frozenset([13, 28, 77])
    FOLLOW_local_vars_in_receive448 = frozenset([13, 28])
    FOLLOW_local_ops_in_receive452 = frozenset([13])
    FOLLOW_DEDENT_in_receive464 = frozenset([26])
    FOLLOW_NEWLINE_in_receive466 = frozenset([1])
    FOLLOW_PROC_in_proc512 = frozenset([19])
    FOLLOW_ID_in_proc514 = frozenset([26])
    FOLLOW_NEWLINE_in_proc516 = frozenset([1])
    FOLLOW_PROC_in_proc545 = frozenset([19])
    FOLLOW_ID_in_proc547 = frozenset([26])
    FOLLOW_NEWLINE_in_proc549 = frozenset([21])
    FOLLOW_INDENT_in_proc551 = frozenset([26])
    FOLLOW_NEWLINE_in_proc553 = frozenset([6, 13, 28, 77])
    FOLLOW_proc_args_in_proc567 = frozenset([13, 28, 77])
    FOLLOW_local_vars_in_proc571 = frozenset([13, 28])
    FOLLOW_local_ops_in_proc575 = frozenset([13])
    FOLLOW_DEDENT_in_proc587 = frozenset([26])
    FOLLOW_NEWLINE_in_proc589 = frozenset([1])
    FOLLOW_ARGS_in_proc_args639 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args641 = frozenset([1])
    FOLLOW_VARS_in_local_vars670 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_local_vars672 = frozenset([1])
    FOLLOW_OPS_in_local_ops701 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops703 = frozenset([21])
    FOLLOW_INDENT_in_local_ops705 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops707 = frozenset([18, 19, 20, 23, 27, 78, 80])
    FOLLOW_statements_in_local_ops709 = frozenset([13])
    FOLLOW_DEDENT_in_local_ops711 = frozenset([26])
    FOLLOW_NEWLINE_in_local_ops713 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement744 = frozenset([26])
    FOLLOW_NEWLINE_in_statement746 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement772 = frozenset([1])
    FOLLOW_statement_if_in_statement782 = frozenset([1])
    FOLLOW_statement_assign_in_statement792 = frozenset([1])
    FOLLOW_statement_while_in_statement802 = frozenset([1])
    FOLLOW_statement_with_in_statement812 = frozenset([1])
    FOLLOW_statement_in_statements831 = frozenset([1, 18, 19, 20, 23, 27, 78, 80])
    FOLLOW_WITH_in_statement_with873 = frozenset([19])
    FOLLOW_ID_in_statement_with875 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with877 = frozenset([21])
    FOLLOW_INDENT_in_statement_with887 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with889 = frozenset([18, 19, 20, 23, 27, 78, 80])
    FOLLOW_statements_in_statement_with891 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with893 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with895 = frozenset([1])
    FOLLOW_ID_in_statement_assign935 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign939 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign941 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign945 = frozenset([1])
    FOLLOW_ID_in_statement_assign998 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign1002 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1004 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1006 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1008 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign1020 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign1024 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_assign1030 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1032 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1085 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1089 = frozenset([19])
    FOLLOW_ID_in_statement_assign1091 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1095 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign1148 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1152 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1154 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1156 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1158 = frozenset([19])
    FOLLOW_ID_in_statement_assign1170 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1174 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1180 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1182 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1244 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1246 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1248 = frozenset([15])
    FOLLOW_DO_in_statement_while1252 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1254 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1268 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1270 = frozenset([18, 19, 20, 23, 27, 78, 80])
    FOLLOW_statements_in_statement_while1272 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1274 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1276 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1316 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1326 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1338 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1446 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1448 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1480 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1482 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1514 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1516 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1520 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1522 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1536 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1538 = frozenset([18, 19, 20, 23, 27, 78, 80])
    FOLLOW_statements_in_statement_elif_body1540 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1542 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1544 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1584 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1586 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1600 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1602 = frozenset([18, 19, 20, 23, 27, 78, 80])
    FOLLOW_statements_in_statement_else1604 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1606 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1608 = frozenset([1])
    FOLLOW_condition_call_in_condition1646 = frozenset([1])
    FOLLOW_ANY_in_condition1675 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1677 = frozenset([1])
    FOLLOW_ALL_in_condition1706 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1708 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1746 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1756 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1758 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1760 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1762 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1766 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1768 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1802 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1812 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1831 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line1833 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1859 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1878 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line1880 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1924 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1926 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1930 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1940 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1942 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1946 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1948 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line1954 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1956 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args1992 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value2009 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value2019 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value2029 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value2039 = frozenset([1])
    FOLLOW_CONSTS_in_consts2058 = frozenset([19])
    FOLLOW_ID_in_consts2060 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2062 = frozenset([21])
    FOLLOW_INDENT_in_consts2072 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2074 = frozenset([19])
    FOLLOW_consts_items_in_consts2076 = frozenset([13])
    FOLLOW_DEDENT_in_consts2078 = frozenset([26])
    FOLLOW_NEWLINE_in_consts2080 = frozenset([1])
    FOLLOW_consts_item_in_consts_items2112 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item2128 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item2130 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2132 = frozenset([1])
    FOLLOW_ID_in_consts_item2154 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2156 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2158 = frozenset([1])
    FOLLOW_ID_in_consts_item2180 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2182 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2184 = frozenset([1])
    FOLLOW_TYPES_in_types2215 = frozenset([19])
    FOLLOW_ID_in_types2217 = frozenset([26])
    FOLLOW_NEWLINE_in_types2219 = frozenset([21])
    FOLLOW_INDENT_in_types2229 = frozenset([26])
    FOLLOW_NEWLINE_in_types2231 = frozenset([19])
    FOLLOW_types_item_in_types2233 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2237 = frozenset([26])
    FOLLOW_NEWLINE_in_types2239 = frozenset([1])
    FOLLOW_ID_in_types_item2273 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2275 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2302 = frozenset([19])
    FOLLOW_ID_in_messages2304 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2306 = frozenset([21])
    FOLLOW_INDENT_in_messages2316 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2318 = frozenset([19])
    FOLLOW_messages_item_in_messages2320 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2324 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2326 = frozenset([1])
    FOLLOW_ID_in_messages_item2360 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2362 = frozenset([1])
    FOLLOW_VARS_in_vars2389 = frozenset([19])
    FOLLOW_ID_in_vars2391 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars2393 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2432 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2434 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints2458 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2470 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2472 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2476 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2478 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2484 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2486 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2514 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2516 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2528 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2530 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2534 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2536 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2542 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2544 = frozenset([1])
    FOLLOW_ID_in_attr_hint2581 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2622 = frozenset([19])
    FOLLOW_ID_in_attr_hint2624 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2664 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2666 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2668 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2670 = frozenset([19])
    FOLLOW_ID_in_attr_hint2674 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2678 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2684 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2731 = frozenset([19])
    FOLLOW_ID_in_hint2733 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2735 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2755 = frozenset([19])
    FOLLOW_ID_in_hint2757 = frozenset([19, 76])
    FOLLOW_hint_arg_in_hint2759 = frozenset([11, 19, 76])
    FOLLOW_CURLY_CLOSE_in_hint2763 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2802 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2806 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2814 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2818 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2820 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2822 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
