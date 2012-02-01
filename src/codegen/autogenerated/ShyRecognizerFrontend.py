# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-01 22:16:34

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
TREE_STATEMENT_ASSIGN_TO=63
TREE_STATEMENT_CALL=64
TREE_STATEMENT_ELIF=65
TREE_STATEMENT_ELSE=66
TREE_STATEMENT_IF=67
TREE_STATEMENT_WHILE=68
TREE_STATEMENT_WITH=69
TREE_TYPES=70
TREE_TYPES_ITEM=71
TREE_VARS=72
TYPES=73
UNDERSCORE=74
VARS=75
WHILE=76
WHITESPACE=77
WITH=78

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
    "TREE_STATELESS", "TREE_STATEMENTS", "TREE_STATEMENT_ASSIGN", "TREE_STATEMENT_ASSIGN_TO", 
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

        self.dfa22 = self.DFA22(
            self, 22,
            eot = self.DFA22_eot,
            eof = self.DFA22_eof,
            min = self.DFA22_min,
            max = self.DFA22_max,
            accept = self.DFA22_accept,
            special = self.DFA22_special,
            transition = self.DFA22_transition
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

        self.dfa43 = self.DFA43(
            self, 43,
            eot = self.DFA43_eot,
            eof = self.DFA43_eof,
            min = self.DFA43_min,
            max = self.DFA43_max,
            accept = self.DFA43_accept,
            special = self.DFA43_special,
            transition = self.DFA43_transition
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
                    # elements: proc_args, ID, proc_attrs, proc_ops
                    # token labels: 
                    # rule labels: retval
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
    # grammar/ShyRecognizerFrontend.g:69:1: statement : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with );
    def statement(self, ):
        retval = self.statement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE52 = None
        statement_call_single_line51 = None

        statement_call_multi_line53 = None

        statement_if54 = None

        statement_assign55 = None

        statement_while56 = None

        statement_with57 = None


        NEWLINE52_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:70:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line | statement_if | statement_assign | statement_while | statement_with )
                alt10 = 6
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
                    # grammar/ShyRecognizerFrontend.g:75:9: statement_while
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_while_in_statement651)
                    statement_while56 = self.statement_while()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_while56.tree)



                elif alt10 == 6:
                    # grammar/ShyRecognizerFrontend.g:76:9: statement_with
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_with_in_statement661)
                    statement_with57 = self.statement_with()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_with57.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:79:1: statements : ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) ;
    def statements(self, ):
        retval = self.statements_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement58 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:80:5: ( ( statement )+ -> ^( TREE_STATEMENTS ( statement )+ ) )
                # grammar/ShyRecognizerFrontend.g:80:9: ( statement )+
                pass 
                # grammar/ShyRecognizerFrontend.g:80:9: ( statement )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA11_0 <= IF) or LA11_0 == MINUS or LA11_0 == NUMBER or LA11_0 == WHILE or LA11_0 == WITH) :
                        alt11 = 1


                    if alt11 == 1:
                        # grammar/ShyRecognizerFrontend.g:80:9: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_statements680)
                        statement58 = self.statement()

                        self._state.following.pop()
                        stream_statement.add(statement58.tree)



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
                # 81:9: -> ^( TREE_STATEMENTS ( statement )+ )
                # grammar/ShyRecognizerFrontend.g:81:13: ^( TREE_STATEMENTS ( statement )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENTS, "TREE_STATEMENTS")
                , root_1)

                # grammar/ShyRecognizerFrontend.g:81:32: ( statement )+
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
    # grammar/ShyRecognizerFrontend.g:84:1: statement_with : WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) ;
    def statement_with(self, ):
        retval = self.statement_with_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WITH59 = None
        ID60 = None
        NEWLINE61 = None
        INDENT62 = None
        NEWLINE63 = None
        DEDENT65 = None
        NEWLINE66 = None
        statements64 = None


        WITH59_tree = None
        ID60_tree = None
        NEWLINE61_tree = None
        INDENT62_tree = None
        NEWLINE63_tree = None
        DEDENT65_tree = None
        NEWLINE66_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_WITH = RewriteRuleTokenStream(self._adaptor, "token WITH")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:85:5: ( WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WITH ID statements ) )
                # grammar/ShyRecognizerFrontend.g:85:9: WITH ID NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WITH59 = self.match(self.input, WITH, self.FOLLOW_WITH_in_statement_with722) 
                stream_WITH.add(WITH59)


                ID60 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_with724) 
                stream_ID.add(ID60)


                NEWLINE61 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with726) 
                stream_NEWLINE.add(NEWLINE61)


                INDENT62 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_with736) 
                stream_INDENT.add(INDENT62)


                NEWLINE63 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with738) 
                stream_NEWLINE.add(NEWLINE63)


                self._state.following.append(self.FOLLOW_statements_in_statement_with740)
                statements64 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements64.tree)


                DEDENT65 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_with742) 
                stream_DEDENT.add(DEDENT65)


                NEWLINE66 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_with744) 
                stream_NEWLINE.add(NEWLINE66)


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
                # 87:9: -> ^( TREE_STATEMENT_WITH ID statements )
                # grammar/ShyRecognizerFrontend.g:87:13: ^( TREE_STATEMENT_WITH ID statements )
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
    # grammar/ShyRecognizerFrontend.g:90:1: statement_assign : ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) );
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID67 = None
        ARROW_LEFT68 = None
        NEWLINE70 = None
        ID71 = None
        ARROW_LEFT72 = None
        NEWLINE73 = None
        INDENT74 = None
        NEWLINE75 = None
        NEWLINE77 = None
        DEDENT78 = None
        NEWLINE79 = None
        ARROW_RIGHT81 = None
        ID82 = None
        NEWLINE83 = None
        ARROW_RIGHT85 = None
        NEWLINE86 = None
        INDENT87 = None
        NEWLINE88 = None
        ID89 = None
        NEWLINE90 = None
        DEDENT91 = None
        NEWLINE92 = None
        arbitrary_value69 = None

        arbitrary_value76 = None

        arbitrary_value80 = None

        arbitrary_value84 = None


        ID67_tree = None
        ARROW_LEFT68_tree = None
        NEWLINE70_tree = None
        ID71_tree = None
        ARROW_LEFT72_tree = None
        NEWLINE73_tree = None
        INDENT74_tree = None
        NEWLINE75_tree = None
        NEWLINE77_tree = None
        DEDENT78_tree = None
        NEWLINE79_tree = None
        ARROW_RIGHT81_tree = None
        ID82_tree = None
        NEWLINE83_tree = None
        ARROW_RIGHT85_tree = None
        NEWLINE86_tree = None
        INDENT87_tree = None
        NEWLINE88_tree = None
        ID89_tree = None
        NEWLINE90_tree = None
        DEDENT91_tree = None
        NEWLINE92_tree = None
        stream_ARROW_RIGHT = RewriteRuleTokenStream(self._adaptor, "token ARROW_RIGHT")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:91:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) | ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
                alt22 = 4
                alt22 = self.dfa22.predict(self.input)
                if alt22 == 1:
                    # grammar/ShyRecognizerFrontend.g:91:9: ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:91:9: ( ID )+
                    cnt12 = 0
                    while True: #loop12
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == ID) :
                            alt12 = 1


                        if alt12 == 1:
                            # grammar/ShyRecognizerFrontend.g:91:9: ID
                            pass 
                            ID67 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign784) 
                            stream_ID.add(ID67)



                        else:
                            if cnt12 >= 1:
                                break #loop12

                            eee = EarlyExitException(12, self.input)
                            raise eee

                        cnt12 += 1


                    ARROW_LEFT68 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign788) 
                    stream_ARROW_LEFT.add(ARROW_LEFT68)


                    # grammar/ShyRecognizerFrontend.g:91:25: ( arbitrary_value )+
                    cnt13 = 0
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA13_0 <= ID) or LA13_0 == MINUS or LA13_0 == NUMBER) :
                            alt13 = 1


                        if alt13 == 1:
                            # grammar/ShyRecognizerFrontend.g:91:25: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign790)
                            arbitrary_value69 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value69.tree)



                        else:
                            if cnt13 >= 1:
                                break #loop13

                            eee = EarlyExitException(13, self.input)
                            raise eee

                        cnt13 += 1


                    NEWLINE70 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign794) 
                    stream_NEWLINE.add(NEWLINE70)


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
                    # 92:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:92:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:92:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:93:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt22 == 2:
                    # grammar/ShyRecognizerFrontend.g:94:9: ( ID )+ ARROW_LEFT NEWLINE INDENT NEWLINE ( ( arbitrary_value )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:94:9: ( ID )+
                    cnt14 = 0
                    while True: #loop14
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == ID) :
                            alt14 = 1


                        if alt14 == 1:
                            # grammar/ShyRecognizerFrontend.g:94:9: ID
                            pass 
                            ID71 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign847) 
                            stream_ID.add(ID71)



                        else:
                            if cnt14 >= 1:
                                break #loop14

                            eee = EarlyExitException(14, self.input)
                            raise eee

                        cnt14 += 1


                    ARROW_LEFT72 = self.match(self.input, ARROW_LEFT, self.FOLLOW_ARROW_LEFT_in_statement_assign851) 
                    stream_ARROW_LEFT.add(ARROW_LEFT72)


                    NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign853) 
                    stream_NEWLINE.add(NEWLINE73)


                    INDENT74 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign855) 
                    stream_INDENT.add(INDENT74)


                    NEWLINE75 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign857) 
                    stream_NEWLINE.add(NEWLINE75)


                    # grammar/ShyRecognizerFrontend.g:95:9: ( ( arbitrary_value )+ NEWLINE )+
                    cnt16 = 0
                    while True: #loop16
                        alt16 = 2
                        LA16_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA16_0 <= ID) or LA16_0 == MINUS or LA16_0 == NUMBER) :
                            alt16 = 1


                        if alt16 == 1:
                            # grammar/ShyRecognizerFrontend.g:95:11: ( arbitrary_value )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:95:11: ( arbitrary_value )+
                            cnt15 = 0
                            while True: #loop15
                                alt15 = 2
                                LA15_0 = self.input.LA(1)

                                if ((EXPRESSION <= LA15_0 <= ID) or LA15_0 == MINUS or LA15_0 == NUMBER) :
                                    alt15 = 1


                                if alt15 == 1:
                                    # grammar/ShyRecognizerFrontend.g:95:11: arbitrary_value
                                    pass 
                                    self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign869)
                                    arbitrary_value76 = self.arbitrary_value()

                                    self._state.following.pop()
                                    stream_arbitrary_value.add(arbitrary_value76.tree)



                                else:
                                    if cnt15 >= 1:
                                        break #loop15

                                    eee = EarlyExitException(15, self.input)
                                    raise eee

                                cnt15 += 1


                            NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign873) 
                            stream_NEWLINE.add(NEWLINE77)



                        else:
                            if cnt16 >= 1:
                                break #loop16

                            eee = EarlyExitException(16, self.input)
                            raise eee

                        cnt16 += 1


                    DEDENT78 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign879) 
                    stream_DEDENT.add(DEDENT78)


                    NEWLINE79 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign881) 
                    stream_NEWLINE.add(NEWLINE79)


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
                    # 96:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:96:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:96:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:97:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt22 == 3:
                    # grammar/ShyRecognizerFrontend.g:98:9: ( arbitrary_value )+ ARROW_RIGHT ( ID )+ NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:98:9: ( arbitrary_value )+
                    cnt17 = 0
                    while True: #loop17
                        alt17 = 2
                        LA17_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA17_0 <= ID) or LA17_0 == MINUS or LA17_0 == NUMBER) :
                            alt17 = 1


                        if alt17 == 1:
                            # grammar/ShyRecognizerFrontend.g:98:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign934)
                            arbitrary_value80 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value80.tree)



                        else:
                            if cnt17 >= 1:
                                break #loop17

                            eee = EarlyExitException(17, self.input)
                            raise eee

                        cnt17 += 1


                    ARROW_RIGHT81 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign938) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT81)


                    # grammar/ShyRecognizerFrontend.g:98:39: ( ID )+
                    cnt18 = 0
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == ID) :
                            alt18 = 1


                        if alt18 == 1:
                            # grammar/ShyRecognizerFrontend.g:98:39: ID
                            pass 
                            ID82 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign940) 
                            stream_ID.add(ID82)



                        else:
                            if cnt18 >= 1:
                                break #loop18

                            eee = EarlyExitException(18, self.input)
                            raise eee

                        cnt18 += 1


                    NEWLINE83 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign944) 
                    stream_NEWLINE.add(NEWLINE83)


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
                    # 99:9: -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    # grammar/ShyRecognizerFrontend.g:99:13: ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN, "TREE_STATEMENT_ASSIGN")
                    , root_1)

                    # grammar/ShyRecognizerFrontend.g:99:38: ( arbitrary_value )+
                    if not (stream_arbitrary_value.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_arbitrary_value.hasNext():
                        self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                    stream_arbitrary_value.reset()

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                    )

                    # grammar/ShyRecognizerFrontend.g:100:42: ( ID )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        self._adaptor.addChild(root_1, 
                        stream_ID.nextNode()
                        )


                    stream_ID.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt22 == 4:
                    # grammar/ShyRecognizerFrontend.g:101:9: ( arbitrary_value )+ ARROW_RIGHT NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT NEWLINE
                    pass 
                    # grammar/ShyRecognizerFrontend.g:101:9: ( arbitrary_value )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if ((EXPRESSION <= LA19_0 <= ID) or LA19_0 == MINUS or LA19_0 == NUMBER) :
                            alt19 = 1


                        if alt19 == 1:
                            # grammar/ShyRecognizerFrontend.g:101:9: arbitrary_value
                            pass 
                            self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_assign997)
                            arbitrary_value84 = self.arbitrary_value()

                            self._state.following.pop()
                            stream_arbitrary_value.add(arbitrary_value84.tree)



                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1


                    ARROW_RIGHT85 = self.match(self.input, ARROW_RIGHT, self.FOLLOW_ARROW_RIGHT_in_statement_assign1001) 
                    stream_ARROW_RIGHT.add(ARROW_RIGHT85)


                    NEWLINE86 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1003) 
                    stream_NEWLINE.add(NEWLINE86)


                    INDENT87 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_assign1005) 
                    stream_INDENT.add(INDENT87)


                    NEWLINE88 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1007) 
                    stream_NEWLINE.add(NEWLINE88)


                    # grammar/ShyRecognizerFrontend.g:102:9: ( ( ID )+ NEWLINE )+
                    cnt21 = 0
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == ID) :
                            alt21 = 1


                        if alt21 == 1:
                            # grammar/ShyRecognizerFrontend.g:102:11: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:102:11: ( ID )+
                            cnt20 = 0
                            while True: #loop20
                                alt20 = 2
                                LA20_0 = self.input.LA(1)

                                if (LA20_0 == ID) :
                                    alt20 = 1


                                if alt20 == 1:
                                    # grammar/ShyRecognizerFrontend.g:102:11: ID
                                    pass 
                                    ID89 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_assign1019) 
                                    stream_ID.add(ID89)



                                else:
                                    if cnt20 >= 1:
                                        break #loop20

                                    eee = EarlyExitException(20, self.input)
                                    raise eee

                                cnt20 += 1


                            NEWLINE90 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1023) 
                            stream_NEWLINE.add(NEWLINE90)



                        else:
                            if cnt21 >= 1:
                                break #loop21

                            eee = EarlyExitException(21, self.input)
                            raise eee

                        cnt21 += 1


                    DEDENT91 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_assign1029) 
                    stream_DEDENT.add(DEDENT91)


                    NEWLINE92 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_assign1031) 
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




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:107:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE93 = None
        NEWLINE95 = None
        DO96 = None
        NEWLINE97 = None
        INDENT98 = None
        NEWLINE99 = None
        DEDENT101 = None
        NEWLINE102 = None
        condition94 = None

        statements100 = None


        WHILE93_tree = None
        NEWLINE95_tree = None
        DO96_tree = None
        NEWLINE97_tree = None
        INDENT98_tree = None
        NEWLINE99_tree = None
        DEDENT101_tree = None
        NEWLINE102_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:108:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:108:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE93 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while1093) 
                stream_WHILE.add(WHILE93)


                self._state.following.append(self.FOLLOW_condition_in_statement_while1095)
                condition94 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition94.tree)


                # grammar/ShyRecognizerFrontend.g:108:25: ( NEWLINE )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == NEWLINE) :
                    alt23 = 1
                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:108:25: NEWLINE
                    pass 
                    NEWLINE95 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1097) 
                    stream_NEWLINE.add(NEWLINE95)





                DO96 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while1101) 
                stream_DO.add(DO96)


                NEWLINE97 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1103) 
                stream_NEWLINE.add(NEWLINE97)


                INDENT98 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while1117) 
                stream_INDENT.add(INDENT98)


                NEWLINE99 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1119) 
                stream_NEWLINE.add(NEWLINE99)


                self._state.following.append(self.FOLLOW_statements_in_statement_while1121)
                statements100 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements100.tree)


                DEDENT101 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while1123) 
                stream_DEDENT.add(DEDENT101)


                NEWLINE102 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while1125) 
                stream_NEWLINE.add(NEWLINE102)


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
                # 110:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:110:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:113:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head103 = None

        statement_elif104 = None

        statement_else105 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:114:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:114:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if1165)
                statement_if_head103 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head103.tree)


                # grammar/ShyRecognizerFrontend.g:115:9: ( statement_elif )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == ELIF) :
                        alt24 = 1


                    if alt24 == 1:
                        # grammar/ShyRecognizerFrontend.g:115:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if1175)
                        statement_elif104 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif104.tree)



                    else:
                        break #loop24


                # grammar/ShyRecognizerFrontend.g:116:9: ( statement_else )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == ELSE) :
                    alt25 = 1
                if alt25 == 1:
                    # grammar/ShyRecognizerFrontend.g:116:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if1187)
                    statement_else105 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else105.tree)





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
                # 117:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:117:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:119:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:120:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:124:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF106 = None
        statement_elif_body107 = None


        IF106_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:125:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:125:9: IF statement_elif_body
                pass 
                IF106 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1295) 
                stream_IF.add(IF106)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1297)
                statement_elif_body107 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body107.tree)


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
                # 126:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:129:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF108 = None
        statement_elif_body109 = None


        ELIF108_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:130:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:130:9: ELIF statement_elif_body
                pass 
                ELIF108 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1329) 
                stream_ELIF.add(ELIF108)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1331)
                statement_elif_body109 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body109.tree)


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
                # 131:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:134:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE111 = None
        DO112 = None
        NEWLINE113 = None
        INDENT114 = None
        NEWLINE115 = None
        DEDENT117 = None
        NEWLINE118 = None
        condition110 = None

        statements116 = None


        NEWLINE111_tree = None
        DO112_tree = None
        NEWLINE113_tree = None
        INDENT114_tree = None
        NEWLINE115_tree = None
        DEDENT117_tree = None
        NEWLINE118_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:135:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:135:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1363)
                condition110 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition110.tree)


                # grammar/ShyRecognizerFrontend.g:135:19: ( NEWLINE )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == NEWLINE) :
                    alt26 = 1
                if alt26 == 1:
                    # grammar/ShyRecognizerFrontend.g:135:19: NEWLINE
                    pass 
                    NEWLINE111 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1365) 
                    stream_NEWLINE.add(NEWLINE111)





                DO112 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1369) 
                stream_DO.add(DO112)


                NEWLINE113 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1371) 
                stream_NEWLINE.add(NEWLINE113)


                INDENT114 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1385) 
                stream_INDENT.add(INDENT114)


                NEWLINE115 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1387) 
                stream_NEWLINE.add(NEWLINE115)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1389)
                statements116 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements116.tree)


                DEDENT117 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1391) 
                stream_DEDENT.add(DEDENT117)


                NEWLINE118 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1393) 
                stream_NEWLINE.add(NEWLINE118)


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
                # 137:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:137:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:140:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE119 = None
        NEWLINE120 = None
        INDENT121 = None
        NEWLINE122 = None
        DEDENT124 = None
        NEWLINE125 = None
        statements123 = None


        ELSE119_tree = None
        NEWLINE120_tree = None
        INDENT121_tree = None
        NEWLINE122_tree = None
        DEDENT124_tree = None
        NEWLINE125_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:141:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:141:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE119 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1433) 
                stream_ELSE.add(ELSE119)


                NEWLINE120 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1435) 
                stream_NEWLINE.add(NEWLINE120)


                INDENT121 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1449) 
                stream_INDENT.add(INDENT121)


                NEWLINE122 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1451) 
                stream_NEWLINE.add(NEWLINE122)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1453)
                statements123 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements123.tree)


                DEDENT124 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1455) 
                stream_DEDENT.add(DEDENT124)


                NEWLINE125 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1457) 
                stream_NEWLINE.add(NEWLINE125)


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
                # 143:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:143:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:146:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY127 = None
        ALL129 = None
        condition_call126 = None

        condition_calls128 = None

        condition_calls130 = None


        ANY127_tree = None
        ALL129_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:147:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt27 = 3
                LA27 = self.input.LA(1)
                if LA27 == ID:
                    alt27 = 1
                elif LA27 == ANY:
                    alt27 = 2
                elif LA27 == ALL:
                    alt27 = 3
                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammar/ShyRecognizerFrontend.g:147:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1495)
                    condition_call126 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call126.tree)


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
                    # 148:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:148:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt27 == 2:
                    # grammar/ShyRecognizerFrontend.g:149:9: ANY condition_calls
                    pass 
                    ANY127 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1524) 
                    stream_ANY.add(ANY127)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1526)
                    condition_calls128 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls128.tree)


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
                    # 150:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:150:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt27 == 3:
                    # grammar/ShyRecognizerFrontend.g:151:9: ALL condition_calls
                    pass 
                    ALL129 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1555) 
                    stream_ALL.add(ALL129)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1557)
                    condition_calls130 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls130.tree)


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
                    # 152:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:152:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:155:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE132 = None
        INDENT133 = None
        NEWLINE134 = None
        DEDENT136 = None
        NEWLINE137 = None
        condition_call131 = None

        condition_call_line135 = None


        NEWLINE132_tree = None
        INDENT133_tree = None
        NEWLINE134_tree = None
        DEDENT136_tree = None
        NEWLINE137_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:156:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == ID) :
                    alt29 = 1
                elif (LA29_0 == NEWLINE) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # grammar/ShyRecognizerFrontend.g:156:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1595)
                    condition_call131 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call131.tree)



                elif alt29 == 2:
                    # grammar/ShyRecognizerFrontend.g:157:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE132 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1605) 
                    stream_NEWLINE.add(NEWLINE132)


                    INDENT133 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1607) 
                    stream_INDENT.add(INDENT133)


                    NEWLINE134 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1609) 
                    stream_NEWLINE.add(NEWLINE134)


                    # grammar/ShyRecognizerFrontend.g:157:32: ( condition_call_line )+
                    cnt28 = 0
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == ID) :
                            alt28 = 1


                        if alt28 == 1:
                            # grammar/ShyRecognizerFrontend.g:157:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1611)
                            condition_call_line135 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line135.tree)



                        else:
                            if cnt28 >= 1:
                                break #loop28

                            eee = EarlyExitException(28, self.input)
                            raise eee

                        cnt28 += 1


                    DEDENT136 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1615) 
                    stream_DEDENT.add(DEDENT136)


                    NEWLINE137 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1617) 
                    stream_NEWLINE.add(NEWLINE137)


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
                    # 158:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:158:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:161:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line138 = None

        statement_call_multi_line139 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:162:5: ( statement_call_single_line | statement_call_multi_line )
                alt30 = 2
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # grammar/ShyRecognizerFrontend.g:162:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1651)
                    statement_call_single_line138 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line138.tree)



                elif alt30 == 2:
                    # grammar/ShyRecognizerFrontend.g:163:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1661)
                    statement_call_multi_line139 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line139.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:166:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE141 = None
        statement_call_single_line140 = None

        statement_call_multi_line142 = None


        NEWLINE141_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:167:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt31 = 2
                alt31 = self.dfa31.predict(self.input)
                if alt31 == 1:
                    # grammar/ShyRecognizerFrontend.g:167:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1680)
                    statement_call_single_line140 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line140.tree)


                    NEWLINE141 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1682) 
                    stream_NEWLINE.add(NEWLINE141)


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
                    # 168:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt31 == 2:
                    # grammar/ShyRecognizerFrontend.g:169:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1708)
                    statement_call_multi_line142 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line142.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:172:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID143 = None
        statement_call_args144 = None


        ID143_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:173:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:173:9: ID ( statement_call_args )?
                pass 
                ID143 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1727) 
                stream_ID.add(ID143)


                # grammar/ShyRecognizerFrontend.g:173:12: ( statement_call_args )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if ((EXPRESSION <= LA32_0 <= ID) or LA32_0 == MINUS or LA32_0 == NUMBER) :
                    alt32 = 1
                if alt32 == 1:
                    # grammar/ShyRecognizerFrontend.g:173:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1729)
                    statement_call_args144 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args144.tree)





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
                # 174:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:174:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:174:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:177:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID145 = None
        NEWLINE147 = None
        INDENT148 = None
        NEWLINE149 = None
        NEWLINE151 = None
        DEDENT152 = None
        NEWLINE153 = None
        statement_call_args146 = None

        statement_call_args150 = None


        ID145_tree = None
        NEWLINE147_tree = None
        INDENT148_tree = None
        NEWLINE149_tree = None
        NEWLINE151_tree = None
        DEDENT152_tree = None
        NEWLINE153_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:178:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:178:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID145 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1773) 
                stream_ID.add(ID145)


                # grammar/ShyRecognizerFrontend.g:178:12: ( statement_call_args )?
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if ((EXPRESSION <= LA33_0 <= ID) or LA33_0 == MINUS or LA33_0 == NUMBER) :
                    alt33 = 1
                if alt33 == 1:
                    # grammar/ShyRecognizerFrontend.g:178:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1775)
                    statement_call_args146 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args146.tree)





                NEWLINE147 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1779) 
                stream_NEWLINE.add(NEWLINE147)


                INDENT148 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1789) 
                stream_INDENT.add(INDENT148)


                NEWLINE149 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1791) 
                stream_NEWLINE.add(NEWLINE149)


                # grammar/ShyRecognizerFrontend.g:179:24: ( statement_call_args NEWLINE )+
                cnt34 = 0
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA34_0 <= ID) or LA34_0 == MINUS or LA34_0 == NUMBER) :
                        alt34 = 1


                    if alt34 == 1:
                        # grammar/ShyRecognizerFrontend.g:179:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1795)
                        statement_call_args150 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args150.tree)


                        NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1797) 
                        stream_NEWLINE.add(NEWLINE151)



                    else:
                        if cnt34 >= 1:
                            break #loop34

                        eee = EarlyExitException(34, self.input)
                        raise eee

                    cnt34 += 1


                DEDENT152 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1803) 
                stream_DEDENT.add(DEDENT152)


                NEWLINE153 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1805) 
                stream_NEWLINE.add(NEWLINE153)


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
                # 180:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:180:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:180:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:183:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value154 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:183:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:183:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:183:23: ( arbitrary_value )+
                cnt35 = 0
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA35_0 <= ID) or LA35_0 == MINUS or LA35_0 == NUMBER) :
                        alt35 = 1


                    if alt35 == 1:
                        # grammar/ShyRecognizerFrontend.g:183:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1841)
                        arbitrary_value154 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value154.tree)



                    else:
                        if cnt35 >= 1:
                            break #loop35

                        eee = EarlyExitException(35, self.input)
                        raise eee

                    cnt35 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:185:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID155 = None
        EXPRESSION156 = None
        num_whole157 = None

        num_fract158 = None


        ID155_tree = None
        EXPRESSION156_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:186:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt36 = 4
                LA36 = self.input.LA(1)
                if LA36 == ID:
                    alt36 = 1
                elif LA36 == EXPRESSION:
                    alt36 = 2
                elif LA36 == MINUS:
                    LA36_3 = self.input.LA(2)

                    if (LA36_3 == NUMBER) :
                        LA36_4 = self.input.LA(3)

                        if (LA36_4 == DIVIDE) :
                            alt36 = 4
                        elif (LA36_4 == ARROW_RIGHT or LA36_4 == DO or (EXPRESSION <= LA36_4 <= ID) or LA36_4 == MINUS or (NEWLINE <= LA36_4 <= NUMBER)) :
                            alt36 = 3
                        else:
                            nvae = NoViableAltException("", 36, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 36, 3, self.input)

                        raise nvae


                elif LA36 == NUMBER:
                    LA36_4 = self.input.LA(2)

                    if (LA36_4 == DIVIDE) :
                        alt36 = 4
                    elif (LA36_4 == ARROW_RIGHT or LA36_4 == DO or (EXPRESSION <= LA36_4 <= ID) or LA36_4 == MINUS or (NEWLINE <= LA36_4 <= NUMBER)) :
                        alt36 = 3
                    else:
                        nvae = NoViableAltException("", 36, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # grammar/ShyRecognizerFrontend.g:186:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID155 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1858)
                    ID155_tree = self._adaptor.createWithPayload(ID155)
                    self._adaptor.addChild(root_0, ID155_tree)




                elif alt36 == 2:
                    # grammar/ShyRecognizerFrontend.g:187:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION156 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1868)
                    EXPRESSION156_tree = self._adaptor.createWithPayload(EXPRESSION156)
                    self._adaptor.addChild(root_0, EXPRESSION156_tree)




                elif alt36 == 3:
                    # grammar/ShyRecognizerFrontend.g:188:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1878)
                    num_whole157 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole157.tree)



                elif alt36 == 4:
                    # grammar/ShyRecognizerFrontend.g:189:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1888)
                    num_fract158 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract158.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:192:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS159 = None
        ID160 = None
        NEWLINE161 = None
        INDENT162 = None
        NEWLINE163 = None
        DEDENT165 = None
        NEWLINE166 = None
        consts_items164 = None


        CONSTS159_tree = None
        ID160_tree = None
        NEWLINE161_tree = None
        INDENT162_tree = None
        NEWLINE163_tree = None
        DEDENT165_tree = None
        NEWLINE166_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:193:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:193:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS159 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1907) 
                stream_CONSTS.add(CONSTS159)


                ID160 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1909) 
                stream_ID.add(ID160)


                NEWLINE161 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1911) 
                stream_NEWLINE.add(NEWLINE161)


                INDENT162 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1921) 
                stream_INDENT.add(INDENT162)


                NEWLINE163 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1923) 
                stream_NEWLINE.add(NEWLINE163)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1925)
                consts_items164 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items164.tree)


                DEDENT165 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1927) 
                stream_DEDENT.add(DEDENT165)


                NEWLINE166 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1929) 
                stream_NEWLINE.add(NEWLINE166)


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
                # 195:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:195:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:197:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item167 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:197:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:197:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:197:16: ( consts_item )+
                cnt37 = 0
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == ID) :
                        alt37 = 1


                    if alt37 == 1:
                        # grammar/ShyRecognizerFrontend.g:197:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1961)
                        consts_item167 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item167.tree)



                    else:
                        if cnt37 >= 1:
                            break #loop37

                        eee = EarlyExitException(37, self.input)
                        raise eee

                    cnt37 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:198:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID168 = None
        NEWLINE170 = None
        ID171 = None
        NEWLINE173 = None
        ID174 = None
        EXPRESSION175 = None
        NEWLINE176 = None
        num_whole169 = None

        num_fract172 = None


        ID168_tree = None
        NEWLINE170_tree = None
        ID171_tree = None
        NEWLINE173_tree = None
        ID174_tree = None
        EXPRESSION175_tree = None
        NEWLINE176_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:199:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt38 = 3
                LA38_0 = self.input.LA(1)

                if (LA38_0 == ID) :
                    LA38 = self.input.LA(2)
                    if LA38 == EXPRESSION:
                        alt38 = 3
                    elif LA38 == MINUS:
                        LA38_3 = self.input.LA(3)

                        if (LA38_3 == NUMBER) :
                            LA38_4 = self.input.LA(4)

                            if (LA38_4 == DIVIDE) :
                                alt38 = 2
                            elif (LA38_4 == NEWLINE) :
                                alt38 = 1
                            else:
                                nvae = NoViableAltException("", 38, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 38, 3, self.input)

                            raise nvae


                    elif LA38 == NUMBER:
                        LA38_4 = self.input.LA(3)

                        if (LA38_4 == DIVIDE) :
                            alt38 = 2
                        elif (LA38_4 == NEWLINE) :
                            alt38 = 1
                        else:
                            nvae = NoViableAltException("", 38, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 38, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 38, 0, self.input)

                    raise nvae


                if alt38 == 1:
                    # grammar/ShyRecognizerFrontend.g:199:9: ID num_whole NEWLINE
                    pass 
                    ID168 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1977) 
                    stream_ID.add(ID168)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1979)
                    num_whole169 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole169.tree)


                    NEWLINE170 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1981) 
                    stream_NEWLINE.add(NEWLINE170)


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
                    # 199:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:199:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt38 == 2:
                    # grammar/ShyRecognizerFrontend.g:200:9: ID num_fract NEWLINE
                    pass 
                    ID171 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2003) 
                    stream_ID.add(ID171)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item2005)
                    num_fract172 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract172.tree)


                    NEWLINE173 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2007) 
                    stream_NEWLINE.add(NEWLINE173)


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
                    # 200:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:200:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt38 == 3:
                    # grammar/ShyRecognizerFrontend.g:201:9: ID EXPRESSION NEWLINE
                    pass 
                    ID174 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item2029) 
                    stream_ID.add(ID174)


                    EXPRESSION175 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item2031) 
                    stream_EXPRESSION.add(EXPRESSION175)


                    NEWLINE176 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item2033) 
                    stream_NEWLINE.add(NEWLINE176)


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
                    # 201:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:201:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:204:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES177 = None
        ID178 = None
        NEWLINE179 = None
        INDENT180 = None
        NEWLINE181 = None
        DEDENT183 = None
        NEWLINE184 = None
        types_item182 = None


        TYPES177_tree = None
        ID178_tree = None
        NEWLINE179_tree = None
        INDENT180_tree = None
        NEWLINE181_tree = None
        DEDENT183_tree = None
        NEWLINE184_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:205:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:205:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES177 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types2064) 
                stream_TYPES.add(TYPES177)


                ID178 = self.match(self.input, ID, self.FOLLOW_ID_in_types2066) 
                stream_ID.add(ID178)


                NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2068) 
                stream_NEWLINE.add(NEWLINE179)


                INDENT180 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types2078) 
                stream_INDENT.add(INDENT180)


                NEWLINE181 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2080) 
                stream_NEWLINE.add(NEWLINE181)


                # grammar/ShyRecognizerFrontend.g:206:24: ( types_item )+
                cnt39 = 0
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == ID) :
                        alt39 = 1


                    if alt39 == 1:
                        # grammar/ShyRecognizerFrontend.g:206:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types2082)
                        types_item182 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item182.tree)



                    else:
                        if cnt39 >= 1:
                            break #loop39

                        eee = EarlyExitException(39, self.input)
                        raise eee

                    cnt39 += 1


                DEDENT183 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types2086) 
                stream_DEDENT.add(DEDENT183)


                NEWLINE184 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types2088) 
                stream_NEWLINE.add(NEWLINE184)


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
                # 207:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:207:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:207:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:209:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID185 = None
        attrs_hints186 = None


        ID185_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:209:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:209:14: ID attrs_hints
                pass 
                ID185 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item2122) 
                stream_ID.add(ID185)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item2124)
                attrs_hints186 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints186.tree)


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
                # 209:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:209:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:211:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES187 = None
        ID188 = None
        NEWLINE189 = None
        INDENT190 = None
        NEWLINE191 = None
        DEDENT193 = None
        NEWLINE194 = None
        messages_item192 = None


        MESSAGES187_tree = None
        ID188_tree = None
        NEWLINE189_tree = None
        INDENT190_tree = None
        NEWLINE191_tree = None
        DEDENT193_tree = None
        NEWLINE194_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:212:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:212:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES187 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages2151) 
                stream_MESSAGES.add(MESSAGES187)


                ID188 = self.match(self.input, ID, self.FOLLOW_ID_in_messages2153) 
                stream_ID.add(ID188)


                NEWLINE189 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2155) 
                stream_NEWLINE.add(NEWLINE189)


                INDENT190 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages2165) 
                stream_INDENT.add(INDENT190)


                NEWLINE191 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2167) 
                stream_NEWLINE.add(NEWLINE191)


                # grammar/ShyRecognizerFrontend.g:213:24: ( messages_item )+
                cnt40 = 0
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == ID) :
                        alt40 = 1


                    if alt40 == 1:
                        # grammar/ShyRecognizerFrontend.g:213:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages2169)
                        messages_item192 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item192.tree)



                    else:
                        if cnt40 >= 1:
                            break #loop40

                        eee = EarlyExitException(40, self.input)
                        raise eee

                    cnt40 += 1


                DEDENT193 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages2173) 
                stream_DEDENT.add(DEDENT193)


                NEWLINE194 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages2175) 
                stream_NEWLINE.add(NEWLINE194)


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
                # 214:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:214:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:214:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:216:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID195 = None
        attrs_hints196 = None


        ID195_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:216:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:216:17: ID attrs_hints
                pass 
                ID195 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2209) 
                stream_ID.add(ID195)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2211)
                attrs_hints196 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints196.tree)


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
                # 216:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:216:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:218:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS197 = None
        ID198 = None
        attrs_hints199 = None


        VARS197_tree = None
        ID198_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:219:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:219:9: VARS ID attrs_hints
                pass 
                VARS197 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars2238) 
                stream_VARS.add(VARS197)


                ID198 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2240) 
                stream_ID.add(ID198)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2242)
                attrs_hints199 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints199.tree)


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
                # 220:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:220:12: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:223:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE201 = None
        NEWLINE202 = None
        INDENT203 = None
        NEWLINE204 = None
        NEWLINE206 = None
        DEDENT207 = None
        NEWLINE208 = None
        NEWLINE210 = None
        INDENT211 = None
        NEWLINE212 = None
        NEWLINE214 = None
        DEDENT215 = None
        NEWLINE216 = None
        attr_hint200 = None

        attr_hint205 = None

        attr_hint209 = None

        attr_hint213 = None


        NEWLINE201_tree = None
        NEWLINE202_tree = None
        INDENT203_tree = None
        NEWLINE204_tree = None
        NEWLINE206_tree = None
        DEDENT207_tree = None
        NEWLINE208_tree = None
        NEWLINE210_tree = None
        INDENT211_tree = None
        NEWLINE212_tree = None
        NEWLINE214_tree = None
        DEDENT215_tree = None
        NEWLINE216_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:224:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt43 = 3
                alt43 = self.dfa43.predict(self.input)
                if alt43 == 1:
                    # grammar/ShyRecognizerFrontend.g:224:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2281)
                    attr_hint200 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint200.tree)


                    NEWLINE201 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2283) 
                    stream_NEWLINE.add(NEWLINE201)


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
                    # 225:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt43 == 2:
                    # grammar/ShyRecognizerFrontend.g:226:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE202 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2307) 
                    stream_NEWLINE.add(NEWLINE202)


                    # grammar/ShyRecognizerFrontend.g:227:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:227:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT203 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2319) 
                    stream_INDENT.add(INDENT203)


                    NEWLINE204 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2321) 
                    stream_NEWLINE.add(NEWLINE204)


                    # grammar/ShyRecognizerFrontend.g:227:26: ( attr_hint NEWLINE )+
                    cnt41 = 0
                    while True: #loop41
                        alt41 = 2
                        LA41_0 = self.input.LA(1)

                        if (LA41_0 == CURLY_OPEN or LA41_0 == ID) :
                            alt41 = 1


                        if alt41 == 1:
                            # grammar/ShyRecognizerFrontend.g:227:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2325)
                            attr_hint205 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint205.tree)


                            NEWLINE206 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2327) 
                            stream_NEWLINE.add(NEWLINE206)



                        else:
                            if cnt41 >= 1:
                                break #loop41

                            eee = EarlyExitException(41, self.input)
                            raise eee

                        cnt41 += 1


                    DEDENT207 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2333) 
                    stream_DEDENT.add(DEDENT207)


                    NEWLINE208 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2335) 
                    stream_NEWLINE.add(NEWLINE208)





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
                    # 228:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:228:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt43 == 3:
                    # grammar/ShyRecognizerFrontend.g:229:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2363)
                    attr_hint209 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint209.tree)


                    NEWLINE210 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2365) 
                    stream_NEWLINE.add(NEWLINE210)


                    # grammar/ShyRecognizerFrontend.g:230:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:230:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT211 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2377) 
                    stream_INDENT.add(INDENT211)


                    NEWLINE212 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2379) 
                    stream_NEWLINE.add(NEWLINE212)


                    # grammar/ShyRecognizerFrontend.g:230:26: ( attr_hint NEWLINE )+
                    cnt42 = 0
                    while True: #loop42
                        alt42 = 2
                        LA42_0 = self.input.LA(1)

                        if (LA42_0 == CURLY_OPEN or LA42_0 == ID) :
                            alt42 = 1


                        if alt42 == 1:
                            # grammar/ShyRecognizerFrontend.g:230:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2383)
                            attr_hint213 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint213.tree)


                            NEWLINE214 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2385) 
                            stream_NEWLINE.add(NEWLINE214)



                        else:
                            if cnt42 >= 1:
                                break #loop42

                            eee = EarlyExitException(42, self.input)
                            raise eee

                        cnt42 += 1


                    DEDENT215 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2391) 
                    stream_DEDENT.add(DEDENT215)


                    NEWLINE216 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2393) 
                    stream_NEWLINE.add(NEWLINE216)





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
                    # 231:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:231:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:233:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID217 = None
        ID219 = None
        NEWLINE221 = None
        INDENT222 = None
        NEWLINE223 = None
        ID224 = None
        NEWLINE225 = None
        DEDENT226 = None
        hint218 = None

        hint220 = None


        ID217_tree = None
        ID219_tree = None
        NEWLINE221_tree = None
        INDENT222_tree = None
        NEWLINE223_tree = None
        ID224_tree = None
        NEWLINE225_tree = None
        DEDENT226_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:234:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt48 = 3
                alt48 = self.dfa48.predict(self.input)
                if alt48 == 1:
                    # grammar/ShyRecognizerFrontend.g:234:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:234:9: ( ID )+
                    cnt44 = 0
                    while True: #loop44
                        alt44 = 2
                        LA44_0 = self.input.LA(1)

                        if (LA44_0 == ID) :
                            alt44 = 1


                        if alt44 == 1:
                            # grammar/ShyRecognizerFrontend.g:234:9: ID
                            pass 
                            ID217 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2430) 
                            stream_ID.add(ID217)



                        else:
                            if cnt44 >= 1:
                                break #loop44

                            eee = EarlyExitException(44, self.input)
                            raise eee

                        cnt44 += 1


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
                    # 235:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:235:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:235:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:235:45: ^( TREE_ATTR ID )
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




                elif alt48 == 2:
                    # grammar/ShyRecognizerFrontend.g:236:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2471)
                    hint218 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint218.tree)


                    # grammar/ShyRecognizerFrontend.g:236:14: ( ID )+
                    cnt45 = 0
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == ID) :
                            alt45 = 1


                        if alt45 == 1:
                            # grammar/ShyRecognizerFrontend.g:236:14: ID
                            pass 
                            ID219 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2473) 
                            stream_ID.add(ID219)



                        else:
                            if cnt45 >= 1:
                                break #loop45

                            eee = EarlyExitException(45, self.input)
                            raise eee

                        cnt45 += 1


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
                    # 237:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:237:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:237:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:237:35: ^( TREE_ATTR ID )
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




                elif alt48 == 3:
                    # grammar/ShyRecognizerFrontend.g:238:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2513)
                    hint220 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint220.tree)


                    NEWLINE221 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2515) 
                    stream_NEWLINE.add(NEWLINE221)


                    INDENT222 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2517) 
                    stream_INDENT.add(INDENT222)


                    NEWLINE223 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2519) 
                    stream_NEWLINE.add(NEWLINE223)


                    # grammar/ShyRecognizerFrontend.g:238:37: ( ( ID )+ NEWLINE )+
                    cnt47 = 0
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == ID) :
                            alt47 = 1


                        if alt47 == 1:
                            # grammar/ShyRecognizerFrontend.g:238:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:238:39: ( ID )+
                            cnt46 = 0
                            while True: #loop46
                                alt46 = 2
                                LA46_0 = self.input.LA(1)

                                if (LA46_0 == ID) :
                                    alt46 = 1


                                if alt46 == 1:
                                    # grammar/ShyRecognizerFrontend.g:238:39: ID
                                    pass 
                                    ID224 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2523) 
                                    stream_ID.add(ID224)



                                else:
                                    if cnt46 >= 1:
                                        break #loop46

                                    eee = EarlyExitException(46, self.input)
                                    raise eee

                                cnt46 += 1


                            NEWLINE225 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2527) 
                            stream_NEWLINE.add(NEWLINE225)



                        else:
                            if cnt47 >= 1:
                                break #loop47

                            eee = EarlyExitException(47, self.input)
                            raise eee

                        cnt47 += 1


                    DEDENT226 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2533) 
                    stream_DEDENT.add(DEDENT226)


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
                    # 239:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:239:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:239:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:239:35: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:242:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN227 = None
        ID228 = None
        CURLY_CLOSE229 = None
        CURLY_OPEN230 = None
        ID231 = None
        CURLY_CLOSE233 = None
        hint_arg232 = None


        CURLY_OPEN227_tree = None
        ID228_tree = None
        CURLY_CLOSE229_tree = None
        CURLY_OPEN230_tree = None
        ID231_tree = None
        CURLY_CLOSE233_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:243:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt50 = 2
                LA50_0 = self.input.LA(1)

                if (LA50_0 == CURLY_OPEN) :
                    LA50_1 = self.input.LA(2)

                    if (LA50_1 == ID) :
                        LA50_2 = self.input.LA(3)

                        if (LA50_2 == CURLY_CLOSE) :
                            alt50 = 1
                        elif (LA50_2 == ID or LA50_2 == UNDERSCORE) :
                            alt50 = 2
                        else:
                            nvae = NoViableAltException("", 50, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 50, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 50, 0, self.input)

                    raise nvae


                if alt50 == 1:
                    # grammar/ShyRecognizerFrontend.g:243:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN227 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2580) 
                    stream_CURLY_OPEN.add(CURLY_OPEN227)


                    ID228 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2582) 
                    stream_ID.add(ID228)


                    CURLY_CLOSE229 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2584) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE229)


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
                    # 243:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:243:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt50 == 2:
                    # grammar/ShyRecognizerFrontend.g:244:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN230 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2604) 
                    stream_CURLY_OPEN.add(CURLY_OPEN230)


                    ID231 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2606) 
                    stream_ID.add(ID231)


                    # grammar/ShyRecognizerFrontend.g:244:23: ( hint_arg )+
                    cnt49 = 0
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == ID or LA49_0 == UNDERSCORE) :
                            alt49 = 1


                        if alt49 == 1:
                            # grammar/ShyRecognizerFrontend.g:244:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2608)
                            hint_arg232 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg232.tree)



                        else:
                            if cnt49 >= 1:
                                break #loop49

                            eee = EarlyExitException(49, self.input)
                            raise eee

                        cnt49 += 1


                    CURLY_CLOSE233 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2612) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE233)


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
                    # 244:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:244:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:244:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:246:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set234 = None

        set234_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:246:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set234 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set234))

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
    # grammar/ShyRecognizerFrontend.g:248:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS235 = None
        NUMBER236 = None

        MINUS235_tree = None
        NUMBER236_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:248:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:248:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:248:13: ( MINUS )?
                alt51 = 2
                LA51_0 = self.input.LA(1)

                if (LA51_0 == MINUS) :
                    alt51 = 1
                if alt51 == 1:
                    # grammar/ShyRecognizerFrontend.g:248:13: MINUS
                    pass 
                    MINUS235 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2651)
                    MINUS235_tree = self._adaptor.createWithPayload(MINUS235)
                    self._adaptor.addChild(root_0, MINUS235_tree)






                NUMBER236 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2655)
                NUMBER236_tree = self._adaptor.createWithPayload(NUMBER236)
                self._adaptor.addChild(root_0, NUMBER236_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:249:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS237 = None
        NUMBER238 = None
        DIVIDE239 = None
        NUMBER240 = None

        MINUS237_tree = None
        NUMBER238_tree = None
        DIVIDE239_tree = None
        NUMBER240_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:249:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:249:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:249:13: ( MINUS )?
                alt52 = 2
                LA52_0 = self.input.LA(1)

                if (LA52_0 == MINUS) :
                    alt52 = 1
                if alt52 == 1:
                    # grammar/ShyRecognizerFrontend.g:249:13: MINUS
                    pass 
                    MINUS237 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2663)
                    MINUS237_tree = self._adaptor.createWithPayload(MINUS237)
                    self._adaptor.addChild(root_0, MINUS237_tree)






                NUMBER238 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2667)
                NUMBER238_tree = self._adaptor.createWithPayload(NUMBER238)
                self._adaptor.addChild(root_0, NUMBER238_tree)



                DIVIDE239 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2669)
                DIVIDE239_tree = self._adaptor.createWithPayload(DIVIDE239)
                self._adaptor.addChild(root_0, DIVIDE239_tree)



                NUMBER240 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2671)
                NUMBER240_tree = self._adaptor.createWithPayload(NUMBER240)
                self._adaptor.addChild(root_0, NUMBER240_tree)





                retval.stop = self.input.LT(-1)


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
        u"\20\uffff"
        )

    DFA10_eof = DFA.unpack(
        u"\20\uffff"
        )

    DFA10_min = DFA.unpack(
        u"\1\22\1\7\4\uffff\1\7\1\10\1\33\1\10\1\15\1\10\1\33\2\uffff\1\10"
        )

    DFA10_max = DFA.unpack(
        u"\1\116\1\33\4\uffff\4\33\1\116\2\33\2\uffff\1\33"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\3\1\4\1\5\1\6\7\uffff\1\2\1\1\1\uffff"
        )

    DFA10_special = DFA.unpack(
        u"\20\uffff"
        )


    DFA10_transition = [
        DFA.unpack(u"\1\3\1\1\1\2\2\uffff\1\3\3\uffff\1\3\60\uffff\1\4\1"
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
        DFA.unpack(u"\1\16\4\uffff\3\16\1\15\1\uffff\1\16\3\uffff\1\16\60"
        u"\uffff\1\16\1\uffff\1\16"),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\13\3\uffff\1\10\2\uffff\1\12\1"
        u"\11"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\11\uffff\1\7\1\13\3\uffff\1\10\2\uffff\1\12\1"
        u"\11")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\16\uffff"
        )

    DFA22_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\1\22\1\7\1\10\1\33\1\10\1\22\1\23\1\10\1\33\4\uffff\1\10"
        )

    DFA22_max = DFA.unpack(
        u"\6\33\1\32\2\33\4\uffff\1\33"
        )

    DFA22_accept = DFA.unpack(
        u"\11\uffff\1\2\1\1\1\4\1\3\1\uffff"
        )

    DFA22_special = DFA.unpack(
        u"\16\uffff"
        )


    DFA22_transition = [
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

    # class definition for DFA #22

    class DFA22(DFA):
        pass


    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\1\23\3\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA30_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\uffff\1\33\1\uffff\1\33"
        )

    DFA30_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA30_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA30_transition = [
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

    # class definition for DFA #30

    class DFA30(DFA):
        pass


    # lookup tables for DFA #31

    DFA31_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA31_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA31_min = DFA.unpack(
        u"\1\23\3\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA31_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\33\2\uffff\1\33"
        )

    DFA31_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA31_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA31_transition = [
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

    # class definition for DFA #31

    class DFA31(DFA):
        pass


    # lookup tables for DFA #43

    DFA43_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA43_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA43_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA43_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\113\1\112\2\uffff\1\32\1\112\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA43_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA43_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA43_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1\6\uffff\1\3"),
        DFA.unpack(u"\1\1\6\uffff\1\4"),
        DFA.unpack(u"\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\3\uffff\1\6\5\uffff\1\6\1\uffff\1\7\1\6\1\uffff"
        u"\1\6\3\uffff\1\6\5\uffff\1\6\46\uffff\1\6\1\uffff\1\6"),
        DFA.unpack(u"\1\10\7\uffff\1\11\66\uffff\1\11"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\14\7\uffff\1\11\66\uffff\1\11"),
        DFA.unpack(u"\1\12\6\uffff\1\4"),
        DFA.unpack(u"\1\15"),
        DFA.unpack(u"\1\12\6\uffff\1\13"),
        DFA.unpack(u"\1\16"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u"\1\17\6\uffff\1\20"),
        DFA.unpack(u"\1\21\5\uffff\1\17"),
        DFA.unpack(u"\1\4")
    ]

    # class definition for DFA #43

    class DFA43(DFA):
        pass


    # lookup tables for DFA #48

    DFA48_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA48_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA48_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA48_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\112\1\32\1\112\2\uffff\1\32"
        )

    DFA48_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA48_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA48_transition = [
        DFA.unpack(u"\1\2\6\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3"),
        DFA.unpack(u"\1\4\7\uffff\1\5\66\uffff\1\5"),
        DFA.unpack(u"\1\6\6\uffff\1\7"),
        DFA.unpack(u"\1\10\7\uffff\1\5\66\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\6\uffff\1\7")
    ]

    # class definition for DFA #48

    class DFA48(DFA):
        pass


 

    FOLLOW_module_in_start82 = frozenset([1, 9, 22, 24, 34, 73, 75])
    FOLLOW_stateless_in_start86 = frozenset([1, 9, 22, 24, 34, 73, 75])
    FOLLOW_consts_in_start90 = frozenset([1, 9, 22, 24, 34, 73, 75])
    FOLLOW_types_in_start94 = frozenset([1, 9, 22, 24, 34, 73, 75])
    FOLLOW_messages_in_start98 = frozenset([1, 9, 22, 24, 34, 73, 75])
    FOLLOW_vars_in_start102 = frozenset([1, 9, 22, 24, 34, 73, 75])
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
    FOLLOW_NEWLINE_in_proc402 = frozenset([6, 13, 28, 75])
    FOLLOW_proc_args_in_proc416 = frozenset([13, 28, 75])
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
    FOLLOW_NEWLINE_in_proc_ops556 = frozenset([18, 19, 20, 23, 27, 76, 78])
    FOLLOW_statements_in_proc_ops558 = frozenset([13])
    FOLLOW_DEDENT_in_proc_ops560 = frozenset([26])
    FOLLOW_NEWLINE_in_proc_ops562 = frozenset([1])
    FOLLOW_statement_call_single_line_in_statement593 = frozenset([26])
    FOLLOW_NEWLINE_in_statement595 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_statement621 = frozenset([1])
    FOLLOW_statement_if_in_statement631 = frozenset([1])
    FOLLOW_statement_assign_in_statement641 = frozenset([1])
    FOLLOW_statement_while_in_statement651 = frozenset([1])
    FOLLOW_statement_with_in_statement661 = frozenset([1])
    FOLLOW_statement_in_statements680 = frozenset([1, 18, 19, 20, 23, 27, 76, 78])
    FOLLOW_WITH_in_statement_with722 = frozenset([19])
    FOLLOW_ID_in_statement_with724 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with726 = frozenset([21])
    FOLLOW_INDENT_in_statement_with736 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with738 = frozenset([18, 19, 20, 23, 27, 76, 78])
    FOLLOW_statements_in_statement_with740 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with742 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with744 = frozenset([1])
    FOLLOW_ID_in_statement_assign784 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign788 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign790 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign794 = frozenset([1])
    FOLLOW_ID_in_statement_assign847 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign851 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign853 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign855 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign857 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign869 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign873 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_assign879 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign881 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign934 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign938 = frozenset([19])
    FOLLOW_ID_in_statement_assign940 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign944 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_assign997 = frozenset([8, 18, 19, 23, 27])
    FOLLOW_ARROW_RIGHT_in_statement_assign1001 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1003 = frozenset([21])
    FOLLOW_INDENT_in_statement_assign1005 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1007 = frozenset([19])
    FOLLOW_ID_in_statement_assign1019 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_statement_assign1023 = frozenset([13, 19])
    FOLLOW_DEDENT_in_statement_assign1029 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_assign1031 = frozenset([1])
    FOLLOW_WHILE_in_statement_while1093 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while1095 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while1097 = frozenset([15])
    FOLLOW_DO_in_statement_while1101 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1103 = frozenset([21])
    FOLLOW_INDENT_in_statement_while1117 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1119 = frozenset([18, 19, 20, 23, 27, 76, 78])
    FOLLOW_statements_in_statement_while1121 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while1123 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while1125 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if1165 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if1175 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if1187 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1295 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1297 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1329 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1331 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1363 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1365 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1369 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1371 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1385 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1387 = frozenset([18, 19, 20, 23, 27, 76, 78])
    FOLLOW_statements_in_statement_elif_body1389 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1391 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1393 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1433 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1435 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1449 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1451 = frozenset([18, 19, 20, 23, 27, 76, 78])
    FOLLOW_statements_in_statement_else1453 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1455 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1457 = frozenset([1])
    FOLLOW_condition_call_in_condition1495 = frozenset([1])
    FOLLOW_ANY_in_condition1524 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1526 = frozenset([1])
    FOLLOW_ALL_in_condition1555 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1557 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1595 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1605 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1607 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1609 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1611 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1615 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1617 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1651 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1661 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1680 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line1682 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1708 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1727 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line1729 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1773 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1775 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1779 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1789 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1791 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1795 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1797 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line1803 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1805 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args1841 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value1858 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1868 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1878 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1888 = frozenset([1])
    FOLLOW_CONSTS_in_consts1907 = frozenset([19])
    FOLLOW_ID_in_consts1909 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1911 = frozenset([21])
    FOLLOW_INDENT_in_consts1921 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1923 = frozenset([19])
    FOLLOW_consts_items_in_consts1925 = frozenset([13])
    FOLLOW_DEDENT_in_consts1927 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1929 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1961 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1977 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item1979 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1981 = frozenset([1])
    FOLLOW_ID_in_consts_item2003 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item2005 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2007 = frozenset([1])
    FOLLOW_ID_in_consts_item2029 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item2031 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item2033 = frozenset([1])
    FOLLOW_TYPES_in_types2064 = frozenset([19])
    FOLLOW_ID_in_types2066 = frozenset([26])
    FOLLOW_NEWLINE_in_types2068 = frozenset([21])
    FOLLOW_INDENT_in_types2078 = frozenset([26])
    FOLLOW_NEWLINE_in_types2080 = frozenset([19])
    FOLLOW_types_item_in_types2082 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types2086 = frozenset([26])
    FOLLOW_NEWLINE_in_types2088 = frozenset([1])
    FOLLOW_ID_in_types_item2122 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item2124 = frozenset([1])
    FOLLOW_MESSAGES_in_messages2151 = frozenset([19])
    FOLLOW_ID_in_messages2153 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2155 = frozenset([21])
    FOLLOW_INDENT_in_messages2165 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2167 = frozenset([19])
    FOLLOW_messages_item_in_messages2169 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages2173 = frozenset([26])
    FOLLOW_NEWLINE_in_messages2175 = frozenset([1])
    FOLLOW_ID_in_messages_item2209 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2211 = frozenset([1])
    FOLLOW_VARS_in_vars2238 = frozenset([19])
    FOLLOW_ID_in_vars2240 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars2242 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2281 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2283 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints2307 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2319 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2321 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2325 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2327 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2333 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2335 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2363 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2365 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2377 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2379 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2383 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2385 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2391 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2393 = frozenset([1])
    FOLLOW_ID_in_attr_hint2430 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2471 = frozenset([19])
    FOLLOW_ID_in_attr_hint2473 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2513 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2515 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2517 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2519 = frozenset([19])
    FOLLOW_ID_in_attr_hint2523 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2527 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2533 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2580 = frozenset([19])
    FOLLOW_ID_in_hint2582 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2584 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2604 = frozenset([19])
    FOLLOW_ID_in_hint2606 = frozenset([19, 74])
    FOLLOW_hint_arg_in_hint2608 = frozenset([11, 19, 74])
    FOLLOW_CURLY_CLOSE_in_hint2612 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2651 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2655 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2663 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2667 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2669 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2671 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
