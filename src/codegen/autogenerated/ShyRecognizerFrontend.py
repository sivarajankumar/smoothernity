# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-01-31 19:55:20

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

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
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

        self.dfa36 = self.DFA36(
            self, 36,
            eot = self.DFA36_eot,
            eof = self.DFA36_eof,
            min = self.DFA36_min,
            max = self.DFA36_max,
            accept = self.DFA36_accept,
            special = self.DFA36_special,
            transition = self.DFA36_transition
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
    # grammar/ShyRecognizerFrontend.g:26:1: module : MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE7 = None
        ID8 = None
        NEWLINE9 = None
        INDENT10 = None
        NEWLINE11 = None
        DEDENT14 = None
        NEWLINE15 = None
        module_queue12 = None

        proc13 = None


        MODULE7_tree = None
        ID8_tree = None
        NEWLINE9_tree = None
        INDENT10_tree = None
        NEWLINE11_tree = None
        DEDENT14_tree = None
        NEWLINE15_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE = RewriteRuleTokenStream(self._adaptor, "token MODULE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_module_queue = RewriteRuleSubtreeStream(self._adaptor, "rule module_queue")
        stream_proc = RewriteRuleSubtreeStream(self._adaptor, "rule proc")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:27:5: ( MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* DEDENT NEWLINE -> ^( TREE_MODULE ID ( module_queue )? ( proc )* ) )
                # grammar/ShyRecognizerFrontend.g:27:9: MODULE ID NEWLINE INDENT NEWLINE ( module_queue )? ( proc )* DEDENT NEWLINE
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


                DEDENT14 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_module163) 
                stream_DEDENT.add(DEDENT14)


                NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module165) 
                stream_NEWLINE.add(NEWLINE15)


                # AST Rewrite
                # elements: module_queue, proc, ID
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 31:9: -> ^( TREE_MODULE ID ( module_queue )? ( proc )* )
                # grammar/ShyRecognizerFrontend.g:31:13: ^( TREE_MODULE ID ( module_queue )? ( proc )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MODULE, "TREE_MODULE")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:32:17: ( module_queue )?
                if stream_module_queue.hasNext():
                    self._adaptor.addChild(root_1, stream_module_queue.nextTree())


                stream_module_queue.reset();

                # grammar/ShyRecognizerFrontend.g:33:17: ( proc )*
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

    # $ANTLR end "module"


    class module_queue_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.module_queue_return, self).__init__()

            self.tree = None





    # $ANTLR start "module_queue"
    # grammar/ShyRecognizerFrontend.g:37:1: module_queue : MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) ;
    def module_queue(self, ):
        retval = self.module_queue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULE_QUEUE16 = None
        ID17 = None
        NEWLINE18 = None

        MODULE_QUEUE16_tree = None
        ID17_tree = None
        NEWLINE18_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_MODULE_QUEUE = RewriteRuleTokenStream(self._adaptor, "token MODULE_QUEUE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:38:5: ( MODULE_QUEUE ID NEWLINE -> ^( TREE_MODULE_QUEUE ID ) )
                # grammar/ShyRecognizerFrontend.g:38:9: MODULE_QUEUE ID NEWLINE
                pass 
                MODULE_QUEUE16 = self.match(self.input, MODULE_QUEUE, self.FOLLOW_MODULE_QUEUE_in_module_queue255) 
                stream_MODULE_QUEUE.add(MODULE_QUEUE16)


                ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_module_queue257) 
                stream_ID.add(ID17)


                NEWLINE18 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_module_queue259) 
                stream_NEWLINE.add(NEWLINE18)


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
                # 39:9: -> ^( TREE_MODULE_QUEUE ID )
                # grammar/ShyRecognizerFrontend.g:39:13: ^( TREE_MODULE_QUEUE ID )
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
    # grammar/ShyRecognizerFrontend.g:42:1: stateless : STATELESS ID NEWLINE ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )? -> ^( TREE_STATELESS ID ( proc )* ) ;
    def stateless(self, ):
        retval = self.stateless_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STATELESS19 = None
        ID20 = None
        NEWLINE21 = None
        INDENT22 = None
        NEWLINE23 = None
        DEDENT25 = None
        NEWLINE26 = None
        proc24 = None


        STATELESS19_tree = None
        ID20_tree = None
        NEWLINE21_tree = None
        INDENT22_tree = None
        NEWLINE23_tree = None
        DEDENT25_tree = None
        NEWLINE26_tree = None
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
                STATELESS19 = self.match(self.input, STATELESS, self.FOLLOW_STATELESS_in_stateless297) 
                stream_STATELESS.add(STATELESS19)


                ID20 = self.match(self.input, ID, self.FOLLOW_ID_in_stateless299) 
                stream_ID.add(ID20)


                NEWLINE21 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless301) 
                stream_NEWLINE.add(NEWLINE21)


                # grammar/ShyRecognizerFrontend.g:43:30: ( INDENT NEWLINE ( proc )+ DEDENT NEWLINE )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == INDENT) :
                    alt5 = 1
                if alt5 == 1:
                    # grammar/ShyRecognizerFrontend.g:43:32: INDENT NEWLINE ( proc )+ DEDENT NEWLINE
                    pass 
                    INDENT22 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_stateless305) 
                    stream_INDENT.add(INDENT22)


                    NEWLINE23 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless307) 
                    stream_NEWLINE.add(NEWLINE23)


                    # grammar/ShyRecognizerFrontend.g:43:47: ( proc )+
                    cnt4 = 0
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == PROC) :
                            alt4 = 1


                        if alt4 == 1:
                            # grammar/ShyRecognizerFrontend.g:43:47: proc
                            pass 
                            self._state.following.append(self.FOLLOW_proc_in_stateless309)
                            proc24 = self.proc()

                            self._state.following.pop()
                            stream_proc.add(proc24.tree)



                        else:
                            if cnt4 >= 1:
                                break #loop4

                            eee = EarlyExitException(4, self.input)
                            raise eee

                        cnt4 += 1


                    DEDENT25 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_stateless313) 
                    stream_DEDENT.add(DEDENT25)


                    NEWLINE26 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stateless315) 
                    stream_NEWLINE.add(NEWLINE26)





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


    class proc_return(ParserRuleReturnScope):
        def __init__(self):
            super(ShyRecognizerFrontend.proc_return, self).__init__()

            self.tree = None





    # $ANTLR start "proc"
    # grammar/ShyRecognizerFrontend.g:47:1: proc : ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? ) );
    def proc(self, ):
        retval = self.proc_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PROC27 = None
        ID28 = None
        NEWLINE29 = None
        PROC30 = None
        ID31 = None
        NEWLINE32 = None
        INDENT33 = None
        NEWLINE34 = None
        DEDENT38 = None
        NEWLINE39 = None
        proc_args35 = None

        proc_attrs36 = None

        proc_ops37 = None


        PROC27_tree = None
        ID28_tree = None
        NEWLINE29_tree = None
        PROC30_tree = None
        ID31_tree = None
        NEWLINE32_tree = None
        INDENT33_tree = None
        NEWLINE34_tree = None
        DEDENT38_tree = None
        NEWLINE39_tree = None
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
                # grammar/ShyRecognizerFrontend.g:48:5: ( PROC ID NEWLINE -> ^( TREE_PROC ID ) | PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? ) )
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if (LA9_0 == PROC) :
                    LA9_1 = self.input.LA(2)

                    if (LA9_1 == ID) :
                        LA9_2 = self.input.LA(3)

                        if (LA9_2 == NEWLINE) :
                            LA9_3 = self.input.LA(4)

                            if (LA9_3 == INDENT) :
                                alt9 = 2
                            elif (LA9_3 == DEDENT or LA9_3 == PROC) :
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
                    # grammar/ShyRecognizerFrontend.g:48:9: PROC ID NEWLINE
                    pass 
                    PROC27 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc361) 
                    stream_PROC.add(PROC27)


                    ID28 = self.match(self.input, ID, self.FOLLOW_ID_in_proc363) 
                    stream_ID.add(ID28)


                    NEWLINE29 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc365) 
                    stream_NEWLINE.add(NEWLINE29)


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
                    # 49:9: -> ^( TREE_PROC ID )
                    # grammar/ShyRecognizerFrontend.g:49:13: ^( TREE_PROC ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt9 == 2:
                    # grammar/ShyRecognizerFrontend.g:50:9: PROC ID NEWLINE INDENT NEWLINE ( proc_args )? ( proc_attrs )? ( proc_ops )? DEDENT NEWLINE
                    pass 
                    PROC30 = self.match(self.input, PROC, self.FOLLOW_PROC_in_proc394) 
                    stream_PROC.add(PROC30)


                    ID31 = self.match(self.input, ID, self.FOLLOW_ID_in_proc396) 
                    stream_ID.add(ID31)


                    NEWLINE32 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc398) 
                    stream_NEWLINE.add(NEWLINE32)


                    INDENT33 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc400) 
                    stream_INDENT.add(INDENT33)


                    NEWLINE34 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc402) 
                    stream_NEWLINE.add(NEWLINE34)


                    # grammar/ShyRecognizerFrontend.g:51:13: ( proc_args )?
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == ARGS) :
                        alt6 = 1
                    if alt6 == 1:
                        # grammar/ShyRecognizerFrontend.g:51:13: proc_args
                        pass 
                        self._state.following.append(self.FOLLOW_proc_args_in_proc416)
                        proc_args35 = self.proc_args()

                        self._state.following.pop()
                        stream_proc_args.add(proc_args35.tree)





                    # grammar/ShyRecognizerFrontend.g:51:25: ( proc_attrs )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == VARS) :
                        alt7 = 1
                    if alt7 == 1:
                        # grammar/ShyRecognizerFrontend.g:51:25: proc_attrs
                        pass 
                        self._state.following.append(self.FOLLOW_proc_attrs_in_proc420)
                        proc_attrs36 = self.proc_attrs()

                        self._state.following.pop()
                        stream_proc_attrs.add(proc_attrs36.tree)





                    # grammar/ShyRecognizerFrontend.g:51:38: ( proc_ops )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == OPS) :
                        alt8 = 1
                    if alt8 == 1:
                        # grammar/ShyRecognizerFrontend.g:51:38: proc_ops
                        pass 
                        self._state.following.append(self.FOLLOW_proc_ops_in_proc424)
                        proc_ops37 = self.proc_ops()

                        self._state.following.pop()
                        stream_proc_ops.add(proc_ops37.tree)





                    DEDENT38 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc436) 
                    stream_DEDENT.add(DEDENT38)


                    NEWLINE39 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc438) 
                    stream_NEWLINE.add(NEWLINE39)


                    # AST Rewrite
                    # elements: ID, proc_attrs, proc_ops, proc_args
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 53:9: -> ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? )
                    # grammar/ShyRecognizerFrontend.g:53:13: ^( TREE_PROC ID ( proc_args )? ( proc_attrs )? ( proc_ops )? )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_PROC, "TREE_PROC")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:53:29: ( proc_args )?
                    if stream_proc_args.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_args.nextTree())


                    stream_proc_args.reset();

                    # grammar/ShyRecognizerFrontend.g:53:41: ( proc_attrs )?
                    if stream_proc_attrs.hasNext():
                        self._adaptor.addChild(root_1, stream_proc_attrs.nextTree())


                    stream_proc_attrs.reset();

                    # grammar/ShyRecognizerFrontend.g:53:54: ( proc_ops )?
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
    # grammar/ShyRecognizerFrontend.g:56:1: proc_args : ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) ;
    def proc_args(self, ):
        retval = self.proc_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ARGS40 = None
        attrs_hints41 = None


        ARGS40_tree = None
        stream_ARGS = RewriteRuleTokenStream(self._adaptor, "token ARGS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:57:5: ( ARGS attrs_hints -> ^( TREE_PROC_ARGS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:57:9: ARGS attrs_hints
                pass 
                ARGS40 = self.match(self.input, ARGS, self.FOLLOW_ARGS_in_proc_args488) 
                stream_ARGS.add(ARGS40)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_args490)
                attrs_hints41 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints41.tree)


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
                # 57:26: -> ^( TREE_PROC_ARGS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:57:29: ^( TREE_PROC_ARGS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:60:1: proc_attrs : VARS attrs_hints -> ^( TREE_PROC_VARS attrs_hints ) ;
    def proc_attrs(self, ):
        retval = self.proc_attrs_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS42 = None
        attrs_hints43 = None


        VARS42_tree = None
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:61:5: ( VARS attrs_hints -> ^( TREE_PROC_VARS attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:61:9: VARS attrs_hints
                pass 
                VARS42 = self.match(self.input, VARS, self.FOLLOW_VARS_in_proc_attrs519) 
                stream_VARS.add(VARS42)


                self._state.following.append(self.FOLLOW_attrs_hints_in_proc_attrs521)
                attrs_hints43 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints43.tree)


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
                # 61:26: -> ^( TREE_PROC_VARS attrs_hints )
                # grammar/ShyRecognizerFrontend.g:61:29: ^( TREE_PROC_VARS attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:64:1: proc_ops : OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements ;
    def proc_ops(self, ):
        retval = self.proc_ops_return()
        retval.start = self.input.LT(1)


        root_0 = None

        OPS44 = None
        NEWLINE45 = None
        INDENT46 = None
        NEWLINE47 = None
        DEDENT49 = None
        NEWLINE50 = None
        statements48 = None


        OPS44_tree = None
        NEWLINE45_tree = None
        INDENT46_tree = None
        NEWLINE47_tree = None
        DEDENT49_tree = None
        NEWLINE50_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_OPS = RewriteRuleTokenStream(self._adaptor, "token OPS")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:65:5: ( OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> statements )
                # grammar/ShyRecognizerFrontend.g:65:9: OPS NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                OPS44 = self.match(self.input, OPS, self.FOLLOW_OPS_in_proc_ops550) 
                stream_OPS.add(OPS44)


                NEWLINE45 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops552) 
                stream_NEWLINE.add(NEWLINE45)


                INDENT46 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_proc_ops554) 
                stream_INDENT.add(INDENT46)


                NEWLINE47 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops556) 
                stream_NEWLINE.add(NEWLINE47)


                self._state.following.append(self.FOLLOW_statements_in_proc_ops558)
                statements48 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements48.tree)


                DEDENT49 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_proc_ops560) 
                stream_DEDENT.add(DEDENT49)


                NEWLINE50 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_proc_ops562) 
                stream_NEWLINE.add(NEWLINE50)


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
                # 66:9: -> statements
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
    # grammar/ShyRecognizerFrontend.g:69:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE52 = None
        statement_call_single_line51 = None

        statement_call_multi_line53 = None

        statement_if54 = None

        statement_assign55 = None

        statement_with56 = None


        NEWLINE52_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:70:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_with )
                alt10 = 5
                alt10 = self.dfa10.predict(self.input)
                if alt10 == 1:
                    # grammar/ShyRecognizerFrontend.g:70:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_statement593)
                    statement_call_single_line51 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line51.tree)


                    NEWLINE52 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement595) 
                    stream_NEWLINE.add(NEWLINE52)


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
                    # 71:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt10 == 2:
                    # grammar/ShyRecognizerFrontend.g:72:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_statement621)
                    statement_call_multi_line53 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line53.tree)



                elif alt10 == 3:
                    # grammar/ShyRecognizerFrontend.g:73:9: statement_if
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_if_in_statement631)
                    statement_if54 = self.statement_if()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_if54.tree)



                elif alt10 == 4:
                    # grammar/ShyRecognizerFrontend.g:74:9: statement_assign
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_assign_in_statement641)
                    statement_assign55 = self.statement_assign()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_assign55.tree)



                elif alt10 == 5:
                    # grammar/ShyRecognizerFrontend.g:75:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement651)
                    statement_with56 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with56.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:78:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement57 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:79:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:79:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:79:9: ( statement )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((ID <= LA11_0 <= IF) or LA11_0 == WITH) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:79:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements670)
                        statement57 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement57.tree)



                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1


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
                # 80:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:80:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:80:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:83:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH58 = None
        ID59 = None
        NEWLINE60 = None
        INDENT61 = None
        NEWLINE62 = None
        DEDENT64 = None
        NEWLINE65 = None
        statements63 = None


        WITH58_tree = None
        ID59_tree = None
        NEWLINE60_tree = None
        INDENT61_tree = None
        NEWLINE62_tree = None
        DEDENT64_tree = None
        NEWLINE65_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:84:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:84:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH58 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with712) 
                stream_WITH.add(WITH58)


                ID59 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with714) 
                stream_ID.add(ID59)


                NEWLINE60 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with716) 
                stream_NEWLINE.add(NEWLINE60)


                INDENT61 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with726) 
                stream_INDENT.add(INDENT61)


                NEWLINE62 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with728) 
                stream_NEWLINE.add(NEWLINE62)


                self._state.following.append(self.FOLLOW_statements_in_statement_with730)
                statements63 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements63.tree)


                DEDENT64 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with732) 
                stream_DEDENT.add(DEDENT64)


                NEWLINE65 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with734) 
                stream_NEWLINE.add(NEWLINE65)


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
                # 86:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:86:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:89:1: statement_assign : ID ARROW_LEFT arbitrary_value NEWLINE -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID ) ;
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID66 = None
        ARROW_LEFT67 = None
        NEWLINE69 = None
        arbitrary_value68 = None


        ID66_tree = None
        ARROW_LEFT67_tree = None
        NEWLINE69_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:90:5: ( ID ARROW_LEFT arbitrary_value NEWLINE -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID ) )
                # grammar/ShyRecognizerFrontend.g:90:9: ID ARROW_LEFT arbitrary_value NEWLINE
                pass 
                ID66 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign774) 
                stream_ID.add(ID66)


                ARROW_LEFT67 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign776) 
                stream_ARROW_LEFT.add(ARROW_LEFT67)


                self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign778)
                arbitrary_value68 = self.arbitrary_value()

                self._state.following.pop()
                stream_arbitrary_value.add(arbitrary_value68.tree)


                NEWLINE69 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign780) 
                stream_NEWLINE.add(NEWLINE69)


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
                # 91:9: -> ^( TREE_STATEMENT_ASSIGN arbitrary_value ID )
                # grammar/ShyRecognizerFrontend.g:91:13: ^( TREE_STATEMENT_ASSIGN arbitrary_value ID )
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
    # grammar/ShyRecognizerFrontend.g:94:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head70 = None

        statement_elif71 = None

        statement_else72 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:95:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:95:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if820)
                statement_if_head70 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head70.tree)


                # grammar/ShyRecognizerFrontend.g:96:9: ( statement_elif )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == ELIF) :
                        alt12 = 1


                    if alt12 == 1:
                        # grammar/ShyRecognizerFrontend.g:96:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if830)
                        statement_elif71 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif71.tree)



                    else:
                        break #loop12


                # grammar/ShyRecognizerFrontend.g:97:9: ( statement_else )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == ELSE) :
                    alt13 = 1
                if alt13 == 1:
                    # grammar/ShyRecognizerFrontend.g:97:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if842)
                    statement_else72 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else72.tree)





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
                # 98:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:98:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:100:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:101:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:105:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF73 = None
        statement_elif_body74 = None


        IF73_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:106:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:106:9: IF statement_elif_body
                pass 
                IF73 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head950) 
                stream_IF.add(IF73)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head952)
                statement_elif_body74 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body74.tree)


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
                # 107:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:110:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF75 = None
        statement_elif_body76 = None


        ELIF75_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:111:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:111:9: ELIF statement_elif_body
                pass 
                ELIF75 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif984) 
                stream_ELIF.add(ELIF75)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif986)
                statement_elif_body76 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body76.tree)


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
                # 112:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:115:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE78 = None
        DO79 = None
        NEWLINE80 = None
        INDENT81 = None
        NEWLINE82 = None
        DEDENT84 = None
        NEWLINE85 = None
        condition77 = None

        statements83 = None


        NEWLINE78_tree = None
        DO79_tree = None
        NEWLINE80_tree = None
        INDENT81_tree = None
        NEWLINE82_tree = None
        DEDENT84_tree = None
        NEWLINE85_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:116:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:116:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1018)
                condition77 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition77.tree)


                # grammar/ShyRecognizerFrontend.g:116:19: ( NEWLINE )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == NEWLINE) :
                    alt14 = 1
                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:116:19: NEWLINE
                    pass 
                    NEWLINE78 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1020) 
                    stream_NEWLINE.add(NEWLINE78)





                DO79 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1024) 
                stream_DO.add(DO79)


                NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1026) 
                stream_NEWLINE.add(NEWLINE80)


                INDENT81 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1040) 
                stream_INDENT.add(INDENT81)


                NEWLINE82 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1042) 
                stream_NEWLINE.add(NEWLINE82)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1044)
                statements83 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements83.tree)


                DEDENT84 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1046) 
                stream_DEDENT.add(DEDENT84)


                NEWLINE85 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1048) 
                stream_NEWLINE.add(NEWLINE85)


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
                # 118:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:118:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:121:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE86 = None
        NEWLINE87 = None
        INDENT88 = None
        NEWLINE89 = None
        DEDENT91 = None
        NEWLINE92 = None
        statements90 = None


        ELSE86_tree = None
        NEWLINE87_tree = None
        INDENT88_tree = None
        NEWLINE89_tree = None
        DEDENT91_tree = None
        NEWLINE92_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:122:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:122:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE86 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1088) 
                stream_ELSE.add(ELSE86)


                NEWLINE87 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1090) 
                stream_NEWLINE.add(NEWLINE87)


                INDENT88 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1104) 
                stream_INDENT.add(INDENT88)


                NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1106) 
                stream_NEWLINE.add(NEWLINE89)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1108)
                statements90 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements90.tree)


                DEDENT91 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1110) 
                stream_DEDENT.add(DEDENT91)


                NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1112) 
                stream_NEWLINE.add(NEWLINE92)


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
                # 124:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:124:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:127:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY94 = None
        ALL96 = None
        condition_call93 = None

        condition_calls95 = None

        condition_calls97 = None


        ANY94_tree = None
        ALL96_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:128:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt15 = 3
                LA15 = self.input.LA(1)
                if LA15 == ID:
                    alt15 = 1
                elif LA15 == ANY:
                    alt15 = 2
                elif LA15 == ALL:
                    alt15 = 3
                else:
                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # grammar/ShyRecognizerFrontend.g:128:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1150)
                    condition_call93 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call93.tree)


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
                    # 129:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:129:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 2:
                    # grammar/ShyRecognizerFrontend.g:130:9: ANY condition_calls
                    pass 
                    ANY94 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1179) 
                    stream_ANY.add(ANY94)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1181)
                    condition_calls95 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls95.tree)


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
                    # 131:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:131:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt15 == 3:
                    # grammar/ShyRecognizerFrontend.g:132:9: ALL condition_calls
                    pass 
                    ALL96 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1210) 
                    stream_ALL.add(ALL96)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1212)
                    condition_calls97 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls97.tree)


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
                    # 133:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:133:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:136:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE99 = None
        INDENT100 = None
        NEWLINE101 = None
        DEDENT103 = None
        NEWLINE104 = None
        condition_call98 = None

        condition_call_line102 = None


        NEWLINE99_tree = None
        INDENT100_tree = None
        NEWLINE101_tree = None
        DEDENT103_tree = None
        NEWLINE104_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:137:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == ID) :
                    alt17 = 1
                elif (LA17_0 == NEWLINE) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae


                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:137:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1250)
                    condition_call98 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call98.tree)



                elif alt17 == 2:
                    # grammar/ShyRecognizerFrontend.g:138:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1260) 
                    stream_NEWLINE.add(NEWLINE99)


                    INDENT100 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1262) 
                    stream_INDENT.add(INDENT100)


                    NEWLINE101 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1264) 
                    stream_NEWLINE.add(NEWLINE101)


                    # grammar/ShyRecognizerFrontend.g:138:32: ( condition_call_line )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if (LA16_0 == ID) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:138:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1266)
                            condition_call_line102 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line102.tree)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    DEDENT103 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1270) 
                    stream_DEDENT.add(DEDENT103)


                    NEWLINE104 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1272) 
                    stream_NEWLINE.add(NEWLINE104)


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
                    # 139:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:139:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:142:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line105 = None

        statement_call_multi_line106 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:143:5: ( statement_call_single_line | statement_call_multi_line )
                alt18 = 2
                alt18 = self.dfa18.predict(self.input)
                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:143:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1306)
                    statement_call_single_line105 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line105.tree)



                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:144:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1316)
                    statement_call_multi_line106 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line106.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:147:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE108 = None
        statement_call_single_line107 = None

        statement_call_multi_line109 = None


        NEWLINE108_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:148:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt19 = 2
                alt19 = self.dfa19.predict(self.input)
                if alt19 == 1:
                    # grammar/ShyRecognizerFrontend.g:148:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1335)
                    statement_call_single_line107 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line107.tree)


                    NEWLINE108 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1337) 
                    stream_NEWLINE.add(NEWLINE108)


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
                    # 149:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt19 == 2:
                    # grammar/ShyRecognizerFrontend.g:150:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1363)
                    statement_call_multi_line109 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line109.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:153:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID110 = None
        statement_call_args111 = None


        ID110_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:154:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:154:9: ID ( statement_call_args )?
                pass 
                ID110 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1382) 
                stream_ID.add(ID110)


                # grammar/ShyRecognizerFrontend.g:154:12: ( statement_call_args )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((EXPRESSION <= LA20_0 <= ID) or LA20_0 == MINUS or LA20_0 == NUMBER) :
                    alt20 = 1
                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:154:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1384)
                    statement_call_args111 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args111.tree)





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
                # 155:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:155:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:155:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:158:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID112 = None
        NEWLINE114 = None
        INDENT115 = None
        NEWLINE116 = None
        NEWLINE118 = None
        DEDENT119 = None
        NEWLINE120 = None
        statement_call_args113 = None

        statement_call_args117 = None


        ID112_tree = None
        NEWLINE114_tree = None
        INDENT115_tree = None
        NEWLINE116_tree = None
        NEWLINE118_tree = None
        DEDENT119_tree = None
        NEWLINE120_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:159:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:159:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID112 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1428) 
                stream_ID.add(ID112)


                # grammar/ShyRecognizerFrontend.g:159:12: ( statement_call_args )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if ((EXPRESSION <= LA21_0 <= ID) or LA21_0 == MINUS or LA21_0 == NUMBER) :
                    alt21 = 1
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:159:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1430)
                    statement_call_args113 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args113.tree)





                NEWLINE114 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1434) 
                stream_NEWLINE.add(NEWLINE114)


                INDENT115 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1444) 
                stream_INDENT.add(INDENT115)


                NEWLINE116 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1446) 
                stream_NEWLINE.add(NEWLINE116)


                # grammar/ShyRecognizerFrontend.g:160:24: ( statement_call_args NEWLINE )+
                cnt22 = 0
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA22_0 <= ID) or LA22_0 == MINUS or LA22_0 == NUMBER) :
                        alt22 = 1


                    if alt22 == 1:
                        # grammar/ShyRecognizerFrontend.g:160:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1450)
                        statement_call_args117 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args117.tree)


                        NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1452) 
                        stream_NEWLINE.add(NEWLINE118)



                    else:
                        if cnt22 >= 1:
                            break #loop22

                        eee = EarlyExitException(22, self.input)
                        raise eee

                    cnt22 += 1


                DEDENT119 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1458) 
                stream_DEDENT.add(DEDENT119)


                NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1460) 
                stream_NEWLINE.add(NEWLINE120)


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
                # 161:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:161:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:161:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:164:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value121 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:164:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:164:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:164:23: ( arbitrary_value )+
                cnt23 = 0
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                        alt23 = 1


                    if alt23 == 1:
                        # grammar/ShyRecognizerFrontend.g:164:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1496)
                        arbitrary_value121 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value121.tree)



                    else:
                        if cnt23 >= 1:
                            break #loop23

                        eee = EarlyExitException(23, self.input)
                        raise eee

                    cnt23 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:166:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID122 = None
        EXPRESSION123 = None
        num_whole124 = None

        num_fract125 = None


        ID122_tree = None
        EXPRESSION123_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:167:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt24 = 4
                LA24 = self.input.LA(1)
                if LA24 == ID:
                    alt24 = 1
                elif LA24 == EXPRESSION:
                    alt24 = 2
                elif LA24 == MINUS:
                    LA24_3 = self.input.LA(2)

                    if (LA24_3 == NUMBER) :
                        LA24_4 = self.input.LA(3)

                        if (LA24_4 == DIVIDE) :
                            alt24 = 4
                        elif (LA24_4 == DO or (EXPRESSION <= LA24_4 <= ID) or LA24_4 == MINUS or (NEWLINE <= LA24_4 <= NUMBER)) :
                            alt24 = 3
                        else:
                            nvae = NoViableAltException("", 24, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 24, 3, self.input)

                        raise nvae


                elif LA24 == NUMBER:
                    LA24_4 = self.input.LA(2)

                    if (LA24_4 == DIVIDE) :
                        alt24 = 4
                    elif (LA24_4 == DO or (EXPRESSION <= LA24_4 <= ID) or LA24_4 == MINUS or (NEWLINE <= LA24_4 <= NUMBER)) :
                        alt24 = 3
                    else:
                        nvae = NoViableAltException("", 24, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # grammar/ShyRecognizerFrontend.g:167:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID122 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1513)
                    ID122_tree = self._adaptor.createWithPayload(ID122)
                    self._adaptor.addChild(root_0, ID122_tree)




                elif alt24 == 2:
                    # grammar/ShyRecognizerFrontend.g:168:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION123 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1523)
                    EXPRESSION123_tree = self._adaptor.createWithPayload(EXPRESSION123)
                    self._adaptor.addChild(root_0, EXPRESSION123_tree)




                elif alt24 == 3:
                    # grammar/ShyRecognizerFrontend.g:169:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1533)
                    num_whole124 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole124.tree)



                elif alt24 == 4:
                    # grammar/ShyRecognizerFrontend.g:170:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1543)
                    num_fract125 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract125.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:173:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS126 = None
        ID127 = None
        NEWLINE128 = None
        INDENT129 = None
        NEWLINE130 = None
        DEDENT132 = None
        NEWLINE133 = None
        consts_items131 = None


        CONSTS126_tree = None
        ID127_tree = None
        NEWLINE128_tree = None
        INDENT129_tree = None
        NEWLINE130_tree = None
        DEDENT132_tree = None
        NEWLINE133_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:174:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS126 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1562) 
                stream_CONSTS.add(CONSTS126)


                ID127 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1564) 
                stream_ID.add(ID127)


                NEWLINE128 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1566) 
                stream_NEWLINE.add(NEWLINE128)


                INDENT129 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1576) 
                stream_INDENT.add(INDENT129)


                NEWLINE130 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1578) 
                stream_NEWLINE.add(NEWLINE130)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1580)
                consts_items131 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items131.tree)


                DEDENT132 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1582) 
                stream_DEDENT.add(DEDENT132)


                NEWLINE133 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1584) 
                stream_NEWLINE.add(NEWLINE133)


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
                # 176:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:176:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:178:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item134 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:178:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:178:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:178:16: ( consts_item )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == ID) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:178:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1616)
                        consts_item134 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item134.tree)



                    else:
                        if cnt25 >= 1:
                            break #loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:179:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID135 = None
        NEWLINE137 = None
        ID138 = None
        NEWLINE140 = None
        ID141 = None
        EXPRESSION142 = None
        NEWLINE143 = None
        num_whole136 = None

        num_fract139 = None


        ID135_tree = None
        NEWLINE137_tree = None
        ID138_tree = None
        NEWLINE140_tree = None
        ID141_tree = None
        EXPRESSION142_tree = None
        NEWLINE143_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:180:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt26 = 3
                LA26_0 = self.input.LA(1)

                if (LA26_0 == ID) :
                    LA26 = self.input.LA(2)
                    if LA26 == EXPRESSION:
                        alt26 = 3
                    elif LA26 == MINUS:
                        LA26_3 = self.input.LA(3)

                        if (LA26_3 == NUMBER) :
                            LA26_4 = self.input.LA(4)

                            if (LA26_4 == DIVIDE) :
                                alt26 = 2
                            elif (LA26_4 == NEWLINE) :
                                alt26 = 1
                            else:
                                nvae = NoViableAltException("", 26, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 26, 3, self.input)

                            raise nvae


                    elif LA26 == NUMBER:
                        LA26_4 = self.input.LA(3)

                        if (LA26_4 == DIVIDE) :
                            alt26 = 2
                        elif (LA26_4 == NEWLINE) :
                            alt26 = 1
                        else:
                            nvae = NoViableAltException("", 26, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 26, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:180:9: ID num_whole NEWLINE
                    pass 
                    ID135 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1632) 
                    stream_ID.add(ID135)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1634)
                    num_whole136 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole136.tree)


                    NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1636) 
                    stream_NEWLINE.add(NEWLINE137)


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
                    # 180:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:180:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt26 == 2:
                    # grammar/ShyRecognizerFrontend.g:181:9: ID num_fract NEWLINE
                    pass 
                    ID138 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1658) 
                    stream_ID.add(ID138)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1660)
                    num_fract139 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract139.tree)


                    NEWLINE140 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1662) 
                    stream_NEWLINE.add(NEWLINE140)


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
                    # 181:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:181:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt26 == 3:
                    # grammar/ShyRecognizerFrontend.g:182:9: ID EXPRESSION NEWLINE
                    pass 
                    ID141 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1684) 
                    stream_ID.add(ID141)


                    EXPRESSION142 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1686) 
                    stream_EXPRESSION.add(EXPRESSION142)


                    NEWLINE143 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1688) 
                    stream_NEWLINE.add(NEWLINE143)


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
                    # 182:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:182:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:185:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES144 = None
        ID145 = None
        NEWLINE146 = None
        INDENT147 = None
        NEWLINE148 = None
        DEDENT150 = None
        NEWLINE151 = None
        types_item149 = None


        TYPES144_tree = None
        ID145_tree = None
        NEWLINE146_tree = None
        INDENT147_tree = None
        NEWLINE148_tree = None
        DEDENT150_tree = None
        NEWLINE151_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:186:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:186:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES144 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1719) 
                stream_TYPES.add(TYPES144)


                ID145 = self.match(self.input, ID, self.FOLLOW_ID_in_types1721) 
                stream_ID.add(ID145)


                NEWLINE146 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1723) 
                stream_NEWLINE.add(NEWLINE146)


                INDENT147 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1733) 
                stream_INDENT.add(INDENT147)


                NEWLINE148 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1735) 
                stream_NEWLINE.add(NEWLINE148)


                # grammar/ShyRecognizerFrontend.g:187:24: ( types_item )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == ID) :
                        alt27 = 1


                    if alt27 == 1:
                        # grammar/ShyRecognizerFrontend.g:187:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types1737)
                        types_item149 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item149.tree)



                    else:
                        if cnt27 >= 1:
                            break #loop27

                        eee = EarlyExitException(27, self.input)
                        raise eee

                    cnt27 += 1


                DEDENT150 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1741) 
                stream_DEDENT.add(DEDENT150)


                NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1743) 
                stream_NEWLINE.add(NEWLINE151)


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
                # 188:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:188:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:188:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:190:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID152 = None
        attrs_hints153 = None


        ID152_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:190:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:190:14: ID attrs_hints
                pass 
                ID152 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1777) 
                stream_ID.add(ID152)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item1779)
                attrs_hints153 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints153.tree)


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
                # 190:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:190:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:192:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES154 = None
        ID155 = None
        NEWLINE156 = None
        INDENT157 = None
        NEWLINE158 = None
        DEDENT160 = None
        NEWLINE161 = None
        messages_item159 = None


        MESSAGES154_tree = None
        ID155_tree = None
        NEWLINE156_tree = None
        INDENT157_tree = None
        NEWLINE158_tree = None
        DEDENT160_tree = None
        NEWLINE161_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:193:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:193:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES154 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages1806) 
                stream_MESSAGES.add(MESSAGES154)


                ID155 = self.match(self.input, ID, self.FOLLOW_ID_in_messages1808) 
                stream_ID.add(ID155)


                NEWLINE156 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1810) 
                stream_NEWLINE.add(NEWLINE156)


                INDENT157 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages1820) 
                stream_INDENT.add(INDENT157)


                NEWLINE158 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1822) 
                stream_NEWLINE.add(NEWLINE158)


                # grammar/ShyRecognizerFrontend.g:194:24: ( messages_item )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == ID) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerFrontend.g:194:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages1824)
                        messages_item159 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item159.tree)



                    else:
                        if cnt28 >= 1:
                            break #loop28

                        eee = EarlyExitException(28, self.input)
                        raise eee

                    cnt28 += 1


                DEDENT160 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages1828) 
                stream_DEDENT.add(DEDENT160)


                NEWLINE161 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1830) 
                stream_NEWLINE.add(NEWLINE161)


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
                # 195:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:195:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:195:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:197:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID162 = None
        attrs_hints163 = None


        ID162_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:197:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:197:17: ID attrs_hints
                pass 
                ID162 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item1864) 
                stream_ID.add(ID162)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item1866)
                attrs_hints163 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints163.tree)


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
                # 197:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:197:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:199:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS164 = None
        ID165 = None
        attrs_hints166 = None


        VARS164_tree = None
        ID165_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:200:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:200:9: VARS ID attrs_hints
                pass 
                VARS164 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars1893) 
                stream_VARS.add(VARS164)


                ID165 = self.match(self.input, ID, self.FOLLOW_ID_in_vars1895) 
                stream_ID.add(ID165)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars1897)
                attrs_hints166 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints166.tree)


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
                # 201:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:201:12: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:204:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE168 = None
        NEWLINE169 = None
        INDENT170 = None
        NEWLINE171 = None
        NEWLINE173 = None
        DEDENT174 = None
        NEWLINE175 = None
        NEWLINE177 = None
        INDENT178 = None
        NEWLINE179 = None
        NEWLINE181 = None
        DEDENT182 = None
        NEWLINE183 = None
        attr_hint167 = None

        attr_hint172 = None

        attr_hint176 = None

        attr_hint180 = None


        NEWLINE168_tree = None
        NEWLINE169_tree = None
        INDENT170_tree = None
        NEWLINE171_tree = None
        NEWLINE173_tree = None
        DEDENT174_tree = None
        NEWLINE175_tree = None
        NEWLINE177_tree = None
        INDENT178_tree = None
        NEWLINE179_tree = None
        NEWLINE181_tree = None
        DEDENT182_tree = None
        NEWLINE183_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:205:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt31 = 3
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:205:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1936)
                    attr_hint167 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint167.tree)


                    NEWLINE168 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1938) 
                    stream_NEWLINE.add(NEWLINE168)


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
                    # 206:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt31 == 2:
                    # grammar/ShyRecognizerFrontend.g:207:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE169 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1962) 
                    stream_NEWLINE.add(NEWLINE169)


                    # grammar/ShyRecognizerFrontend.g:208:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:208:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT170 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints1974) 
                    stream_INDENT.add(INDENT170)


                    NEWLINE171 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1976) 
                    stream_NEWLINE.add(NEWLINE171)


                    # grammar/ShyRecognizerFrontend.g:208:26: ( attr_hint NEWLINE )+
                    cnt29 = 0
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == CURLY_OPEN or LA29_0 == ID) :
                            alt29 = 1


                        if alt29 == 1:
                            # grammar/ShyRecognizerFrontend.g:208:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints1980)
                            attr_hint172 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint172.tree)


                            NEWLINE173 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1982) 
                            stream_NEWLINE.add(NEWLINE173)



                        else:
                            if cnt29 >= 1:
                                break #loop29

                            eee = EarlyExitException(29, self.input)
                            raise eee

                        cnt29 += 1


                    DEDENT174 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints1988) 
                    stream_DEDENT.add(DEDENT174)


                    NEWLINE175 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints1990) 
                    stream_NEWLINE.add(NEWLINE175)





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
                    # 209:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:209:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt31 == 3:
                    # grammar/ShyRecognizerFrontend.g:210:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2018)
                    attr_hint176 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint176.tree)


                    NEWLINE177 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2020) 
                    stream_NEWLINE.add(NEWLINE177)


                    # grammar/ShyRecognizerFrontend.g:211:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:211:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT178 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2032) 
                    stream_INDENT.add(INDENT178)


                    NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2034) 
                    stream_NEWLINE.add(NEWLINE179)


                    # grammar/ShyRecognizerFrontend.g:211:26: ( attr_hint NEWLINE )+
                    cnt30 = 0
                    while True: #loop30
                        alt30 = 2
                        LA30_0 = self.input.LA(1)

                        if (LA30_0 == CURLY_OPEN or LA30_0 == ID) :
                            alt30 = 1


                        if alt30 == 1:
                            # grammar/ShyRecognizerFrontend.g:211:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2038)
                            attr_hint180 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint180.tree)


                            NEWLINE181 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2040) 
                            stream_NEWLINE.add(NEWLINE181)



                        else:
                            if cnt30 >= 1:
                                break #loop30

                            eee = EarlyExitException(30, self.input)
                            raise eee

                        cnt30 += 1


                    DEDENT182 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2046) 
                    stream_DEDENT.add(DEDENT182)


                    NEWLINE183 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2048) 
                    stream_NEWLINE.add(NEWLINE183)





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
                    # 212:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:212:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:214:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID184 = None
        ID186 = None
        NEWLINE188 = None
        INDENT189 = None
        NEWLINE190 = None
        ID191 = None
        NEWLINE192 = None
        DEDENT193 = None
        hint185 = None

        hint187 = None


        ID184_tree = None
        ID186_tree = None
        NEWLINE188_tree = None
        INDENT189_tree = None
        NEWLINE190_tree = None
        ID191_tree = None
        NEWLINE192_tree = None
        DEDENT193_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:215:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt36 = 3
                alt36 = self.dfa36.predict(self.input)
                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:215:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:215:9: ( ID )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:215:9: ID
                            pass 
                            ID184 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2085) 
                            stream_ID.add(ID184)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


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
                    # 216:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:216:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:216:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:216:45: ^( TREE_ATTR ID )
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




                elif alt36 == 2:
                    # grammar/ShyRecognizerFrontend.g:217:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2126)
                    hint185 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint185.tree)


                    # grammar/ShyRecognizerFrontend.g:217:14: ( ID )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == ID) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerFrontend.g:217:14: ID
                            pass 
                            ID186 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2128) 
                            stream_ID.add(ID186)



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


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
                    # 218:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:218:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:218:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:218:35: ^( TREE_ATTR ID )
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




                elif alt36 == 3:
                    # grammar/ShyRecognizerFrontend.g:219:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2168)
                    hint187 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint187.tree)


                    NEWLINE188 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2170) 
                    stream_NEWLINE.add(NEWLINE188)


                    INDENT189 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2172) 
                    stream_INDENT.add(INDENT189)


                    NEWLINE190 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2174) 
                    stream_NEWLINE.add(NEWLINE190)


                    # grammar/ShyRecognizerFrontend.g:219:37: ( ( ID )+ NEWLINE )+
                    cnt35 = 0
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == ID) :
                            alt35 = 1


                        if alt35 == 1:
                            # grammar/ShyRecognizerFrontend.g:219:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:219:39: ( ID )+
                            cnt34 = 0
                            while True: #loop34
                                alt34 = 2
                                LA34_0 = self.input.LA(1)

                                if (LA34_0 == ID) :
                                    alt34 = 1


                                if alt34 == 1:
                                    # grammar/ShyRecognizerFrontend.g:219:39: ID
                                    pass 
                                    ID191 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2178) 
                                    stream_ID.add(ID191)



                                else:
                                    if cnt34 >= 1:
                                        break #loop34

                                    eee = EarlyExitException(34, self.input)
                                    raise eee

                                cnt34 += 1


                            NEWLINE192 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2182) 
                            stream_NEWLINE.add(NEWLINE192)



                        else:
                            if cnt35 >= 1:
                                break #loop35

                            eee = EarlyExitException(35, self.input)
                            raise eee

                        cnt35 += 1


                    DEDENT193 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2188) 
                    stream_DEDENT.add(DEDENT193)


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
                    # 220:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:220:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:220:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:220:35: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:223:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN194 = None
        ID195 = None
        CURLY_CLOSE196 = None
        CURLY_OPEN197 = None
        ID198 = None
        CURLY_CLOSE200 = None
        hint_arg199 = None


        CURLY_OPEN194_tree = None
        ID195_tree = None
        CURLY_CLOSE196_tree = None
        CURLY_OPEN197_tree = None
        ID198_tree = None
        CURLY_CLOSE200_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:224:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == CURLY_OPEN) :
                    LA38_1 = self.input.LA(2)

                    if (LA38_1 == ID) :
                        LA38_2 = self.input.LA(3)

                        if (LA38_2 == CURLY_CLOSE) :
                            alt38 = 1
                        elif (LA38_2 == ID or LA38_2 == UNDERSCORE) :
                            alt38 = 2
                        else:
                            nvae = NoViableAltException("", 38, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 38, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:224:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN194 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2235) 
                    stream_CURLY_OPEN.add(CURLY_OPEN194)


                    ID195 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2237) 
                    stream_ID.add(ID195)


                    CURLY_CLOSE196 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2239) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE196)


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
                    # 224:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:224:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:225:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN197 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2259) 
                    stream_CURLY_OPEN.add(CURLY_OPEN197)


                    ID198 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2261) 
                    stream_ID.add(ID198)


                    # grammar/ShyRecognizerFrontend.g:225:23: ( hint_arg )+
                    cnt37 = 0
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == ID or LA37_0 == UNDERSCORE) :
                            alt37 = 1


                        if alt37 == 1:
                            # grammar/ShyRecognizerFrontend.g:225:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2263)
                            hint_arg199 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg199.tree)



                        else:
                            if cnt37 >= 1:
                                break #loop37

                            eee = EarlyExitException(37, self.input)
                            raise eee

                        cnt37 += 1


                    CURLY_CLOSE200 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2267) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE200)


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
                    # 225:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:225:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:225:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:227:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set201 = None

        set201_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:227:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set201 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set201))

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
    # grammar/ShyRecognizerFrontend.g:229:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS202 = None
        NUMBER203 = None

        MINUS202_tree = None
        NUMBER203_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:229:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:229:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:229:13: ( MINUS )?
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 == MINUS) :
                    alt39 = 1
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:229:13: MINUS
                    pass 
                    MINUS202 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2306)
                    MINUS202_tree = self._adaptor.createWithPayload(MINUS202)
                    self._adaptor.addChild(root_0, MINUS202_tree)






                NUMBER203 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2310)
                NUMBER203_tree = self._adaptor.createWithPayload(NUMBER203)
                self._adaptor.addChild(root_0, NUMBER203_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:230:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS204 = None
        NUMBER205 = None
        DIVIDE206 = None
        NUMBER207 = None

        MINUS204_tree = None
        NUMBER205_tree = None
        DIVIDE206_tree = None
        NUMBER207_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:230:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:230:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:230:13: ( MINUS )?
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == MINUS) :
                    alt40 = 1
                if alt40 == 1:
                    # grammar/ShyRecognizerFrontend.g:230:13: MINUS
                    pass 
                    MINUS204 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2318)
                    MINUS204_tree = self._adaptor.createWithPayload(MINUS204)
                    self._adaptor.addChild(root_0, MINUS204_tree)






                NUMBER205 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2322)
                NUMBER205_tree = self._adaptor.createWithPayload(NUMBER205)
                self._adaptor.addChild(root_0, NUMBER205_tree)



                DIVIDE206 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2324)
                DIVIDE206_tree = self._adaptor.createWithPayload(DIVIDE206)
                self._adaptor.addChild(root_0, DIVIDE206_tree)



                NUMBER207 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2326)
                NUMBER207_tree = self._adaptor.createWithPayload(NUMBER207)
                self._adaptor.addChild(root_0, NUMBER207_tree)





                retval.stop = self.input.LT(-1)


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



    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\23\1\7\3\uffff\2\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA10_max = DFA.unpack(
        u"\1\113\1\33\3\uffff\4\33\1\113\1\33\2\uffff\1\33"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\3\1\5\1\4\6\uffff\1\2\1\1\1\uffff"
        )

    DFA10_special = DFA.unpack(
        u"\16\uffff"
        )


    DFA10_transition = [
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

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA18_min = DFA.unpack(
        u"\1\23\3\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA18_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\uffff\1\33\1\uffff\1\33"
        )

    DFA18_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA18_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA18_transition = [
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

    # class definition for DFA #18

    class DFA18(DFA):
        pass


    # lookup tables for DFA #19

    DFA19_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA19_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA19_min = DFA.unpack(
        u"\1\23\3\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA19_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\33\2\uffff\1\33"
        )

    DFA19_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA19_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA19_transition = [
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

    # class definition for DFA #19

    class DFA19(DFA):
        pass


    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA31_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA31_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\111\1\110\2\uffff\1\32\1\110\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA31_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA31_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA31_transition = [
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

    # class definition for DFA #31

    class DFA31(DFA):
        pass


    # lookup tables for DFA #36

    DFA36_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA36_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA36_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA36_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\110\1\32\1\110\2\uffff\1\32"
        )

    DFA36_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA36_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA36_transition = [
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

    # class definition for DFA #36

    class DFA36(DFA):
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
    FOLLOW_NEWLINE_in_module129 = frozenset([13, 25, 30])
    FOLLOW_module_queue_in_module139 = frozenset([13, 30])
    FOLLOW_proc_in_module151 = frozenset([13, 30])
    FOLLOW_DEDENT_in_module163 = frozenset([26])
    FOLLOW_NEWLINE_in_module165 = frozenset([1])
    FOLLOW_MODULE_QUEUE_in_module_queue255 = frozenset([19])
    FOLLOW_ID_in_module_queue257 = frozenset([26])
    FOLLOW_NEWLINE_in_module_queue259 = frozenset([1])
    FOLLOW_STATELESS_in_stateless297 = frozenset([19])
    FOLLOW_ID_in_stateless299 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless301 = frozenset([1, 21])
    FOLLOW_INDENT_in_stateless305 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless307 = frozenset([30])
    FOLLOW_proc_in_stateless309 = frozenset([13, 30])
    FOLLOW_DEDENT_in_stateless313 = frozenset([26])
    FOLLOW_NEWLINE_in_stateless315 = frozenset([1])
    FOLLOW_PROC_in_proc361 = frozenset([19])
    FOLLOW_ID_in_proc363 = frozenset([26])
    FOLLOW_NEWLINE_in_proc365 = frozenset([1])
    FOLLOW_PROC_in_proc394 = frozenset([19])
    FOLLOW_ID_in_proc396 = frozenset([26])
    FOLLOW_NEWLINE_in_proc398 = frozenset([21])
    FOLLOW_INDENT_in_proc400 = frozenset([26])
    FOLLOW_NEWLINE_in_proc402 = frozenset([6, 13, 28, 73])
    FOLLOW_proc_args_in_proc416 = frozenset([13, 28, 73])
    FOLLOW_proc_attrs_in_proc420 = frozenset([13, 28])
    FOLLOW_proc_ops_in_proc424 = frozenset([13])
    FOLLOW_DEDENT_in_proc436 = frozenset([26])
    FOLLOW_NEWLINE_in_proc438 = frozenset([1])
    FOLLOW_ARGS_in_proc_args488 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_args490 = frozenset([1])
    FOLLOW_VARS_in_proc_attrs519 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_proc_attrs521 = frozenset([1])
    FOLLOW_OPS_in_proc_ops550 = frozenset([26])
    FOLLOW_NEWLINE_in_proc_ops552 = frozenset([21])
    FOLLOW_INDENT_in_proc_ops554 = frozenset([26])
    FOLLOW_NEWLINE_in_proc_ops556 = frozenset([19, 20, 75])
    FOLLOW_statements_in_proc_ops558 = frozenset([13])
    FOLLOW_DEDENT_in_proc_ops560 = frozenset([26])
    FOLLOW_NEWLINE_in_proc_ops562 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement593 = frozenset([26])
    FOLLOW_NEWLINE_in_statement595 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement621 = frozenset([1])
    FOLLOW_statement_if_in_statement631 = frozenset([1])
    FOLLOW_statement_assign_in_statement641 = frozenset([1])
    FOLLOW_statement_with_in_statement651 = frozenset([1])
    FOLLOW_statement_in_statements670 = frozenset([1, 19, 20, 75])
    FOLLOW_WITH_in_statement_with712 = frozenset([19])
    FOLLOW_ID_in_statement_with714 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with716 = frozenset([21])
    FOLLOW_INDENT_in_statement_with726 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with728 = frozenset([19, 20, 75])
    FOLLOW_statements_in_statement_with730 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with732 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with734 = frozenset([1])
    FOLLOW_ID_in_statement_assign774 = frozenset([7])
    FOLLOW_ARROW_LEFT_in_statement_assign776 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign778 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign780 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if820 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if830 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if842 = frozenset([1])
    FOLLOW_IF_in_statement_if_head950 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head952 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif984 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif986 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1018 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1020 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1024 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1026 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1040 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1042 = frozenset([19, 20, 75])
    FOLLOW_statements_in_statement_elif_body1044 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1046 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1048 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1088 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1090 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1104 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1106 = frozenset([19, 20, 75])
    FOLLOW_statements_in_statement_else1108 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1110 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1112 = frozenset([1])
    FOLLOW_condition_call_in_condition1150 = frozenset([1])
    FOLLOW_ANY_in_condition1179 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1181 = frozenset([1])
    FOLLOW_ALL_in_condition1210 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1212 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1250 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1260 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1262 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1264 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1266 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1270 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1272 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1306 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1316 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1335 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line1337 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1363 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1382 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line1384 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1428 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1430 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1434 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1444 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1446 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1450 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1452 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line1458 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1460 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args1496 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value1513 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1523 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1533 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1543 = frozenset([1])
    FOLLOW_CONSTS_in_consts1562 = frozenset([19])
    FOLLOW_ID_in_consts1564 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1566 = frozenset([21])
    FOLLOW_INDENT_in_consts1576 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1578 = frozenset([19])
    FOLLOW_consts_items_in_consts1580 = frozenset([13])
    FOLLOW_DEDENT_in_consts1582 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1584 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1616 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1632 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item1634 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1636 = frozenset([1])
    FOLLOW_ID_in_consts_item1658 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item1660 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1662 = frozenset([1])
    FOLLOW_ID_in_consts_item1684 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1686 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1688 = frozenset([1])
    FOLLOW_TYPES_in_types1719 = frozenset([19])
    FOLLOW_ID_in_types1721 = frozenset([26])
    FOLLOW_NEWLINE_in_types1723 = frozenset([21])
    FOLLOW_INDENT_in_types1733 = frozenset([26])
    FOLLOW_NEWLINE_in_types1735 = frozenset([19])
    FOLLOW_types_item_in_types1737 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types1741 = frozenset([26])
    FOLLOW_NEWLINE_in_types1743 = frozenset([1])
    FOLLOW_ID_in_types_item1777 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item1779 = frozenset([1])
    FOLLOW_MESSAGES_in_messages1806 = frozenset([19])
    FOLLOW_ID_in_messages1808 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1810 = frozenset([21])
    FOLLOW_INDENT_in_messages1820 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1822 = frozenset([19])
    FOLLOW_messages_item_in_messages1824 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages1828 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1830 = frozenset([1])
    FOLLOW_ID_in_messages_item1864 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item1866 = frozenset([1])
    FOLLOW_VARS_in_vars1893 = frozenset([19])
    FOLLOW_ID_in_vars1895 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars1897 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints1936 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1938 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints1962 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints1974 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1976 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints1980 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1982 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints1988 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints1990 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2018 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2020 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2032 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2034 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2038 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2040 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2046 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2048 = frozenset([1])
    FOLLOW_ID_in_attr_hint2085 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2126 = frozenset([19])
    FOLLOW_ID_in_attr_hint2128 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2168 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2170 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2172 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2174 = frozenset([19])
    FOLLOW_ID_in_attr_hint2178 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2182 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2188 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2235 = frozenset([19])
    FOLLOW_ID_in_hint2237 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2239 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2259 = frozenset([19])
    FOLLOW_ID_in_hint2261 = frozenset([19, 72])
    FOLLOW_hint_arg_in_hint2263 = frozenset([11, 19, 72])
    FOLLOW_CURLY_CLOSE_in_hint2267 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2306 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2310 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2318 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2322 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2324 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2326 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
