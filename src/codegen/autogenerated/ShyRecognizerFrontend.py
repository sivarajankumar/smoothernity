# $ANTLR 3.4 grammar/ShyRecognizerFrontend.g 2012-02-01 19:37:36

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
                    # elements: ID, proc_ops, proc_attrs, proc_args
                    # token labels: 
                    # rule labels: retval
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

                    if ((ID <= LA11_0 <= IF) or LA11_0 == WHILE or LA11_0 == WITH) :
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
    # grammar/ShyRecognizerFrontend.g:90:1: statement_assign : ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) ;
    def statement_assign(self, ):
        retval = self.statement_assign_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID67 = None
        ARROW_LEFT68 = None
        NEWLINE70 = None
        arbitrary_value69 = None


        ID67_tree = None
        ARROW_LEFT68_tree = None
        NEWLINE70_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_ARROW_LEFT = RewriteRuleTokenStream(self._adaptor, "token ARROW_LEFT")
        stream_arbitrary_value = RewriteRuleSubtreeStream(self._adaptor, "rule arbitrary_value")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:91:5: ( ( ID )+ ARROW_LEFT ( arbitrary_value )+ NEWLINE -> ^( TREE_STATEMENT_ASSIGN ( arbitrary_value )+ TREE_STATEMENT_ASSIGN_TO ( ID )+ ) )
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

                # grammar/ShyRecognizerFrontend.g:93:17: ( arbitrary_value )+
                if not (stream_arbitrary_value.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_arbitrary_value.hasNext():
                    self._adaptor.addChild(root_1, stream_arbitrary_value.nextTree())


                stream_arbitrary_value.reset()

                self._adaptor.addChild(root_1, 
                self._adaptor.createFromType(TREE_STATEMENT_ASSIGN_TO, "TREE_STATEMENT_ASSIGN_TO")
                )

                # grammar/ShyRecognizerFrontend.g:95:17: ( ID )+
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
    # grammar/ShyRecognizerFrontend.g:98:1: statement_while : WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) ;
    def statement_while(self, ):
        retval = self.statement_while_return()
        retval.start = self.input.LT(1)


        root_0 = None

        WHILE71 = None
        NEWLINE73 = None
        DO74 = None
        NEWLINE75 = None
        INDENT76 = None
        NEWLINE77 = None
        DEDENT79 = None
        NEWLINE80 = None
        condition72 = None

        statements78 = None


        WHILE71_tree = None
        NEWLINE73_tree = None
        DO74_tree = None
        NEWLINE75_tree = None
        INDENT76_tree = None
        NEWLINE77_tree = None
        DEDENT79_tree = None
        NEWLINE80_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_WHILE = RewriteRuleTokenStream(self._adaptor, "token WHILE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:99:5: ( WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_WHILE condition statements ) )
                # grammar/ShyRecognizerFrontend.g:99:9: WHILE condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                WHILE71 = self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement_while888) 
                stream_WHILE.add(WHILE71)


                self._state.following.append(self.FOLLOW_condition_in_statement_while890)
                condition72 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition72.tree)


                # grammar/ShyRecognizerFrontend.g:99:25: ( NEWLINE )?
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == NEWLINE) :
                    alt14 = 1
                if alt14 == 1:
                    # grammar/ShyRecognizerFrontend.g:99:25: NEWLINE
                    pass 
                    NEWLINE73 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while892) 
                    stream_NEWLINE.add(NEWLINE73)





                DO74 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_while896) 
                stream_DO.add(DO74)


                NEWLINE75 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while898) 
                stream_NEWLINE.add(NEWLINE75)


                INDENT76 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_while912) 
                stream_INDENT.add(INDENT76)


                NEWLINE77 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while914) 
                stream_NEWLINE.add(NEWLINE77)


                self._state.following.append(self.FOLLOW_statements_in_statement_while916)
                statements78 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements78.tree)


                DEDENT79 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_while918) 
                stream_DEDENT.add(DEDENT79)


                NEWLINE80 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_while920) 
                stream_NEWLINE.add(NEWLINE80)


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
                # 101:9: -> ^( TREE_STATEMENT_WHILE condition statements )
                # grammar/ShyRecognizerFrontend.g:101:13: ^( TREE_STATEMENT_WHILE condition statements )
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
    # grammar/ShyRecognizerFrontend.g:104:1: statement_if : statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) ;
    def statement_if(self, ):
        retval = self.statement_if_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_if_head81 = None

        statement_elif82 = None

        statement_else83 = None


        stream_statement_else = RewriteRuleSubtreeStream(self._adaptor, "rule statement_else")
        stream_statement_elif = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif")
        stream_statement_if_head = RewriteRuleSubtreeStream(self._adaptor, "rule statement_if_head")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:105:5: ( statement_if_head ( statement_elif )* ( statement_else )? -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? ) )
                # grammar/ShyRecognizerFrontend.g:105:9: statement_if_head ( statement_elif )* ( statement_else )?
                pass 
                self._state.following.append(self.FOLLOW_statement_if_head_in_statement_if960)
                statement_if_head81 = self.statement_if_head()

                self._state.following.pop()
                stream_statement_if_head.add(statement_if_head81.tree)


                # grammar/ShyRecognizerFrontend.g:106:9: ( statement_elif )*
                while True: #loop15
                    alt15 = 2
                    LA15_0 = self.input.LA(1)

                    if (LA15_0 == ELIF) :
                        alt15 = 1


                    if alt15 == 1:
                        # grammar/ShyRecognizerFrontend.g:106:9: statement_elif
                        pass 
                        self._state.following.append(self.FOLLOW_statement_elif_in_statement_if970)
                        statement_elif82 = self.statement_elif()

                        self._state.following.pop()
                        stream_statement_elif.add(statement_elif82.tree)



                    else:
                        break #loop15


                # grammar/ShyRecognizerFrontend.g:107:9: ( statement_else )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == ELSE) :
                    alt16 = 1
                if alt16 == 1:
                    # grammar/ShyRecognizerFrontend.g:107:9: statement_else
                    pass 
                    self._state.following.append(self.FOLLOW_statement_else_in_statement_if982)
                    statement_else83 = self.statement_else()

                    self._state.following.pop()
                    stream_statement_else.add(statement_else83.tree)





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
                # 108:9: -> ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                # grammar/ShyRecognizerFrontend.g:108:13: ^( TREE_STATEMENT_IF statement_if_head ( statement_elif )* ( statement_else )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_IF, "TREE_STATEMENT_IF")
                , root_1)

                self._adaptor.addChild(root_1, stream_statement_if_head.nextTree())

                # grammar/ShyRecognizerFrontend.g:110:17: ( statement_elif )*
                while stream_statement_elif.hasNext():
                    self._adaptor.addChild(root_1, stream_statement_elif.nextTree())


                stream_statement_elif.reset();

                # grammar/ShyRecognizerFrontend.g:111:17: ( statement_else )?
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
    # grammar/ShyRecognizerFrontend.g:115:1: statement_if_head : IF statement_elif_body -> statement_elif_body ;
    def statement_if_head(self, ):
        retval = self.statement_if_head_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IF84 = None
        statement_elif_body85 = None


        IF84_tree = None
        stream_IF = RewriteRuleTokenStream(self._adaptor, "token IF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:116:5: ( IF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:116:9: IF statement_elif_body
                pass 
                IF84 = self.match(self.input, IF, self.FOLLOW_IF_in_statement_if_head1090) 
                stream_IF.add(IF84)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_if_head1092)
                statement_elif_body85 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body85.tree)


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
                # 117:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:120:1: statement_elif : ELIF statement_elif_body -> statement_elif_body ;
    def statement_elif(self, ):
        retval = self.statement_elif_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELIF86 = None
        statement_elif_body87 = None


        ELIF86_tree = None
        stream_ELIF = RewriteRuleTokenStream(self._adaptor, "token ELIF")
        stream_statement_elif_body = RewriteRuleSubtreeStream(self._adaptor, "rule statement_elif_body")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:121:5: ( ELIF statement_elif_body -> statement_elif_body )
                # grammar/ShyRecognizerFrontend.g:121:9: ELIF statement_elif_body
                pass 
                ELIF86 = self.match(self.input, ELIF, self.FOLLOW_ELIF_in_statement_elif1124) 
                stream_ELIF.add(ELIF86)


                self._state.following.append(self.FOLLOW_statement_elif_body_in_statement_elif1126)
                statement_elif_body87 = self.statement_elif_body()

                self._state.following.pop()
                stream_statement_elif_body.add(statement_elif_body87.tree)


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
                # 122:9: -> statement_elif_body
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
    # grammar/ShyRecognizerFrontend.g:125:1: statement_elif_body : condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) ;
    def statement_elif_body(self, ):
        retval = self.statement_elif_body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE89 = None
        DO90 = None
        NEWLINE91 = None
        INDENT92 = None
        NEWLINE93 = None
        DEDENT95 = None
        NEWLINE96 = None
        condition88 = None

        statements94 = None


        NEWLINE89_tree = None
        DO90_tree = None
        NEWLINE91_tree = None
        INDENT92_tree = None
        NEWLINE93_tree = None
        DEDENT95_tree = None
        NEWLINE96_tree = None
        stream_DO = RewriteRuleTokenStream(self._adaptor, "token DO")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition = RewriteRuleSubtreeStream(self._adaptor, "rule condition")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:126:5: ( condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELIF condition statements ) )
                # grammar/ShyRecognizerFrontend.g:126:9: condition ( NEWLINE )? DO NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_condition_in_statement_elif_body1158)
                condition88 = self.condition()

                self._state.following.pop()
                stream_condition.add(condition88.tree)


                # grammar/ShyRecognizerFrontend.g:126:19: ( NEWLINE )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == NEWLINE) :
                    alt17 = 1
                if alt17 == 1:
                    # grammar/ShyRecognizerFrontend.g:126:19: NEWLINE
                    pass 
                    NEWLINE89 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1160) 
                    stream_NEWLINE.add(NEWLINE89)





                DO90 = self.match(self.input, DO, self.FOLLOW_DO_in_statement_elif_body1164) 
                stream_DO.add(DO90)


                NEWLINE91 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1166) 
                stream_NEWLINE.add(NEWLINE91)


                INDENT92 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_elif_body1180) 
                stream_INDENT.add(INDENT92)


                NEWLINE93 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1182) 
                stream_NEWLINE.add(NEWLINE93)


                self._state.following.append(self.FOLLOW_statements_in_statement_elif_body1184)
                statements94 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements94.tree)


                DEDENT95 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_elif_body1186) 
                stream_DEDENT.add(DEDENT95)


                NEWLINE96 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_elif_body1188) 
                stream_NEWLINE.add(NEWLINE96)


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
                # 128:9: -> ^( TREE_STATEMENT_ELIF condition statements )
                # grammar/ShyRecognizerFrontend.g:128:13: ^( TREE_STATEMENT_ELIF condition statements )
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
    # grammar/ShyRecognizerFrontend.g:131:1: statement_else : ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) ;
    def statement_else(self, ):
        retval = self.statement_else_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ELSE97 = None
        NEWLINE98 = None
        INDENT99 = None
        NEWLINE100 = None
        DEDENT102 = None
        NEWLINE103 = None
        statements101 = None


        ELSE97_tree = None
        NEWLINE98_tree = None
        INDENT99_tree = None
        NEWLINE100_tree = None
        DEDENT102_tree = None
        NEWLINE103_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_ELSE = RewriteRuleTokenStream(self._adaptor, "token ELSE")
        stream_statements = RewriteRuleSubtreeStream(self._adaptor, "rule statements")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:132:5: ( ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE -> ^( TREE_STATEMENT_ELSE statements ) )
                # grammar/ShyRecognizerFrontend.g:132:9: ELSE NEWLINE INDENT NEWLINE statements DEDENT NEWLINE
                pass 
                ELSE97 = self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement_else1228) 
                stream_ELSE.add(ELSE97)


                NEWLINE98 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1230) 
                stream_NEWLINE.add(NEWLINE98)


                INDENT99 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_else1244) 
                stream_INDENT.add(INDENT99)


                NEWLINE100 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1246) 
                stream_NEWLINE.add(NEWLINE100)


                self._state.following.append(self.FOLLOW_statements_in_statement_else1248)
                statements101 = self.statements()

                self._state.following.pop()
                stream_statements.add(statements101.tree)


                DEDENT102 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_else1250) 
                stream_DEDENT.add(DEDENT102)


                NEWLINE103 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_else1252) 
                stream_NEWLINE.add(NEWLINE103)


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
                # 134:9: -> ^( TREE_STATEMENT_ELSE statements )
                # grammar/ShyRecognizerFrontend.g:134:13: ^( TREE_STATEMENT_ELSE statements )
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
    # grammar/ShyRecognizerFrontend.g:137:1: condition : ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) );
    def condition(self, ):
        retval = self.condition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ANY105 = None
        ALL107 = None
        condition_call104 = None

        condition_calls106 = None

        condition_calls108 = None


        ANY105_tree = None
        ALL107_tree = None
        stream_ANY = RewriteRuleTokenStream(self._adaptor, "token ANY")
        stream_ALL = RewriteRuleTokenStream(self._adaptor, "token ALL")
        stream_condition_call = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call")
        stream_condition_calls = RewriteRuleSubtreeStream(self._adaptor, "rule condition_calls")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:138:5: ( condition_call -> ^( TREE_CONDITION_ANY condition_call ) | ANY condition_calls -> ^( TREE_CONDITION_ANY condition_calls ) | ALL condition_calls -> ^( TREE_CONDITION_ALL condition_calls ) )
                alt18 = 3
                LA18 = self.input.LA(1)
                if LA18 == ID:
                    alt18 = 1
                elif LA18 == ANY:
                    alt18 = 2
                elif LA18 == ALL:
                    alt18 = 3
                else:
                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # grammar/ShyRecognizerFrontend.g:138:9: condition_call
                    pass 
                    self._state.following.append(self.FOLLOW_condition_call_in_condition1290)
                    condition_call104 = self.condition_call()

                    self._state.following.pop()
                    stream_condition_call.add(condition_call104.tree)


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
                    # 139:9: -> ^( TREE_CONDITION_ANY condition_call )
                    # grammar/ShyRecognizerFrontend.g:139:13: ^( TREE_CONDITION_ANY condition_call )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_call.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt18 == 2:
                    # grammar/ShyRecognizerFrontend.g:140:9: ANY condition_calls
                    pass 
                    ANY105 = self.match(self.input, ANY, self.FOLLOW_ANY_in_condition1319) 
                    stream_ANY.add(ANY105)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1321)
                    condition_calls106 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls106.tree)


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
                    # 141:9: -> ^( TREE_CONDITION_ANY condition_calls )
                    # grammar/ShyRecognizerFrontend.g:141:13: ^( TREE_CONDITION_ANY condition_calls )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_CONDITION_ANY, "TREE_CONDITION_ANY")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_condition_calls.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt18 == 3:
                    # grammar/ShyRecognizerFrontend.g:142:9: ALL condition_calls
                    pass 
                    ALL107 = self.match(self.input, ALL, self.FOLLOW_ALL_in_condition1350) 
                    stream_ALL.add(ALL107)


                    self._state.following.append(self.FOLLOW_condition_calls_in_condition1352)
                    condition_calls108 = self.condition_calls()

                    self._state.following.pop()
                    stream_condition_calls.add(condition_calls108.tree)


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
                    # 143:9: -> ^( TREE_CONDITION_ALL condition_calls )
                    # grammar/ShyRecognizerFrontend.g:143:13: ^( TREE_CONDITION_ALL condition_calls )
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
    # grammar/ShyRecognizerFrontend.g:146:1: condition_calls : ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ );
    def condition_calls(self, ):
        retval = self.condition_calls_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE110 = None
        INDENT111 = None
        NEWLINE112 = None
        DEDENT114 = None
        NEWLINE115 = None
        condition_call109 = None

        condition_call_line113 = None


        NEWLINE110_tree = None
        INDENT111_tree = None
        NEWLINE112_tree = None
        DEDENT114_tree = None
        NEWLINE115_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_condition_call_line = RewriteRuleSubtreeStream(self._adaptor, "rule condition_call_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:147:5: ( condition_call | NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE -> ( condition_call_line )+ )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == ID) :
                    alt20 = 1
                elif (LA20_0 == NEWLINE) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # grammar/ShyRecognizerFrontend.g:147:9: condition_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_condition_call_in_condition_calls1390)
                    condition_call109 = self.condition_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, condition_call109.tree)



                elif alt20 == 2:
                    # grammar/ShyRecognizerFrontend.g:148:9: NEWLINE INDENT NEWLINE ( condition_call_line )+ DEDENT NEWLINE
                    pass 
                    NEWLINE110 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1400) 
                    stream_NEWLINE.add(NEWLINE110)


                    INDENT111 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_condition_calls1402) 
                    stream_INDENT.add(INDENT111)


                    NEWLINE112 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1404) 
                    stream_NEWLINE.add(NEWLINE112)


                    # grammar/ShyRecognizerFrontend.g:148:32: ( condition_call_line )+
                    cnt19 = 0
                    while True: #loop19
                        alt19 = 2
                        LA19_0 = self.input.LA(1)

                        if (LA19_0 == ID) :
                            alt19 = 1


                        if alt19 == 1:
                            # grammar/ShyRecognizerFrontend.g:148:32: condition_call_line
                            pass 
                            self._state.following.append(self.FOLLOW_condition_call_line_in_condition_calls1406)
                            condition_call_line113 = self.condition_call_line()

                            self._state.following.pop()
                            stream_condition_call_line.add(condition_call_line113.tree)



                        else:
                            if cnt19 >= 1:
                                break #loop19

                            eee = EarlyExitException(19, self.input)
                            raise eee

                        cnt19 += 1


                    DEDENT114 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_condition_calls1410) 
                    stream_DEDENT.add(DEDENT114)


                    NEWLINE115 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_calls1412) 
                    stream_NEWLINE.add(NEWLINE115)


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
                    # 149:9: -> ( condition_call_line )+
                    # grammar/ShyRecognizerFrontend.g:149:13: ( condition_call_line )+
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
    # grammar/ShyRecognizerFrontend.g:152:1: condition_call : ( statement_call_single_line | statement_call_multi_line );
    def condition_call(self, ):
        retval = self.condition_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        statement_call_single_line116 = None

        statement_call_multi_line117 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:153:5: ( statement_call_single_line | statement_call_multi_line )
                alt21 = 2
                alt21 = self.dfa21.predict(self.input)
                if alt21 == 1:
                    # grammar/ShyRecognizerFrontend.g:153:9: statement_call_single_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call1446)
                    statement_call_single_line116 = self.statement_call_single_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_single_line116.tree)



                elif alt21 == 2:
                    # grammar/ShyRecognizerFrontend.g:154:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call1456)
                    statement_call_multi_line117 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line117.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:157:1: condition_call_line : ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line );
    def condition_call_line(self, ):
        retval = self.condition_call_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE119 = None
        statement_call_single_line118 = None

        statement_call_multi_line120 = None


        NEWLINE119_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_statement_call_single_line = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_single_line")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:158:5: ( statement_call_single_line NEWLINE -> statement_call_single_line | statement_call_multi_line )
                alt22 = 2
                alt22 = self.dfa22.predict(self.input)
                if alt22 == 1:
                    # grammar/ShyRecognizerFrontend.g:158:9: statement_call_single_line NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_single_line_in_condition_call_line1475)
                    statement_call_single_line118 = self.statement_call_single_line()

                    self._state.following.pop()
                    stream_statement_call_single_line.add(statement_call_single_line118.tree)


                    NEWLINE119 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_condition_call_line1477) 
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
                    # 159:13: -> statement_call_single_line
                    self._adaptor.addChild(root_0, stream_statement_call_single_line.nextTree())




                    retval.tree = root_0




                elif alt22 == 2:
                    # grammar/ShyRecognizerFrontend.g:160:9: statement_call_multi_line
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_statement_call_multi_line_in_condition_call_line1503)
                    statement_call_multi_line120 = self.statement_call_multi_line()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, statement_call_multi_line120.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:163:1: statement_call_single_line : ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) ;
    def statement_call_single_line(self, ):
        retval = self.statement_call_single_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID121 = None
        statement_call_args122 = None


        ID121_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:164:5: ( ID ( statement_call_args )? -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? ) )
                # grammar/ShyRecognizerFrontend.g:164:9: ID ( statement_call_args )?
                pass 
                ID121 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_single_line1522) 
                stream_ID.add(ID121)


                # grammar/ShyRecognizerFrontend.g:164:12: ( statement_call_args )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if ((EXPRESSION <= LA23_0 <= ID) or LA23_0 == MINUS or LA23_0 == NUMBER) :
                    alt23 = 1
                if alt23 == 1:
                    # grammar/ShyRecognizerFrontend.g:164:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_single_line1524)
                    statement_call_args122 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args122.tree)





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
                # 165:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                # grammar/ShyRecognizerFrontend.g:165:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:165:39: ( statement_call_args )?
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
    # grammar/ShyRecognizerFrontend.g:168:1: statement_call_multi_line : ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) ;
    def statement_call_multi_line(self, ):
        retval = self.statement_call_multi_line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID123 = None
        NEWLINE125 = None
        INDENT126 = None
        NEWLINE127 = None
        NEWLINE129 = None
        DEDENT130 = None
        NEWLINE131 = None
        statement_call_args124 = None

        statement_call_args128 = None


        ID123_tree = None
        NEWLINE125_tree = None
        INDENT126_tree = None
        NEWLINE127_tree = None
        NEWLINE129_tree = None
        DEDENT130_tree = None
        NEWLINE131_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_statement_call_args = RewriteRuleSubtreeStream(self._adaptor, "rule statement_call_args")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:169:5: ( ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* ) )
                # grammar/ShyRecognizerFrontend.g:169:9: ID ( statement_call_args )? NEWLINE INDENT NEWLINE ( statement_call_args NEWLINE )+ DEDENT NEWLINE
                pass 
                ID123 = self.match(self.input, ID, self.FOLLOW_ID_in_statement_call_multi_line1568) 
                stream_ID.add(ID123)


                # grammar/ShyRecognizerFrontend.g:169:12: ( statement_call_args )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if ((EXPRESSION <= LA24_0 <= ID) or LA24_0 == MINUS or LA24_0 == NUMBER) :
                    alt24 = 1
                if alt24 == 1:
                    # grammar/ShyRecognizerFrontend.g:169:12: statement_call_args
                    pass 
                    self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1570)
                    statement_call_args124 = self.statement_call_args()

                    self._state.following.pop()
                    stream_statement_call_args.add(statement_call_args124.tree)





                NEWLINE125 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1574) 
                stream_NEWLINE.add(NEWLINE125)


                INDENT126 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_statement_call_multi_line1584) 
                stream_INDENT.add(INDENT126)


                NEWLINE127 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1586) 
                stream_NEWLINE.add(NEWLINE127)


                # grammar/ShyRecognizerFrontend.g:170:24: ( statement_call_args NEWLINE )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA25_0 <= ID) or LA25_0 == MINUS or LA25_0 == NUMBER) :
                        alt25 = 1


                    if alt25 == 1:
                        # grammar/ShyRecognizerFrontend.g:170:26: statement_call_args NEWLINE
                        pass 
                        self._state.following.append(self.FOLLOW_statement_call_args_in_statement_call_multi_line1590)
                        statement_call_args128 = self.statement_call_args()

                        self._state.following.pop()
                        stream_statement_call_args.add(statement_call_args128.tree)


                        NEWLINE129 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1592) 
                        stream_NEWLINE.add(NEWLINE129)



                    else:
                        if cnt25 >= 1:
                            break #loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1


                DEDENT130 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_statement_call_multi_line1598) 
                stream_DEDENT.add(DEDENT130)


                NEWLINE131 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_statement_call_multi_line1600) 
                stream_NEWLINE.add(NEWLINE131)


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
                # 171:9: -> ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                # grammar/ShyRecognizerFrontend.g:171:13: ^( TREE_STATEMENT_CALL ID ( statement_call_args )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_STATEMENT_CALL, "TREE_STATEMENT_CALL")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:171:39: ( statement_call_args )*
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
    # grammar/ShyRecognizerFrontend.g:174:1: statement_call_args : ( arbitrary_value )+ ;
    def statement_call_args(self, ):
        retval = self.statement_call_args_return()
        retval.start = self.input.LT(1)


        root_0 = None

        arbitrary_value132 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:174:21: ( ( arbitrary_value )+ )
                # grammar/ShyRecognizerFrontend.g:174:23: ( arbitrary_value )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:174:23: ( arbitrary_value )+
                cnt26 = 0
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if ((EXPRESSION <= LA26_0 <= ID) or LA26_0 == MINUS or LA26_0 == NUMBER) :
                        alt26 = 1


                    if alt26 == 1:
                        # grammar/ShyRecognizerFrontend.g:174:23: arbitrary_value
                        pass 
                        self._state.following.append(self.FOLLOW_arbitrary_value_in_statement_call_args1636)
                        arbitrary_value132 = self.arbitrary_value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, arbitrary_value132.tree)



                    else:
                        if cnt26 >= 1:
                            break #loop26

                        eee = EarlyExitException(26, self.input)
                        raise eee

                    cnt26 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:176:1: arbitrary_value : ( ID | EXPRESSION | num_whole | num_fract );
    def arbitrary_value(self, ):
        retval = self.arbitrary_value_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID133 = None
        EXPRESSION134 = None
        num_whole135 = None

        num_fract136 = None


        ID133_tree = None
        EXPRESSION134_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:177:5: ( ID | EXPRESSION | num_whole | num_fract )
                alt27 = 4
                LA27 = self.input.LA(1)
                if LA27 == ID:
                    alt27 = 1
                elif LA27 == EXPRESSION:
                    alt27 = 2
                elif LA27 == MINUS:
                    LA27_3 = self.input.LA(2)

                    if (LA27_3 == NUMBER) :
                        LA27_4 = self.input.LA(3)

                        if (LA27_4 == DIVIDE) :
                            alt27 = 4
                        elif (LA27_4 == DO or (EXPRESSION <= LA27_4 <= ID) or LA27_4 == MINUS or (NEWLINE <= LA27_4 <= NUMBER)) :
                            alt27 = 3
                        else:
                            nvae = NoViableAltException("", 27, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 27, 3, self.input)

                        raise nvae


                elif LA27 == NUMBER:
                    LA27_4 = self.input.LA(2)

                    if (LA27_4 == DIVIDE) :
                        alt27 = 4
                    elif (LA27_4 == DO or (EXPRESSION <= LA27_4 <= ID) or LA27_4 == MINUS or (NEWLINE <= LA27_4 <= NUMBER)) :
                        alt27 = 3
                    else:
                        nvae = NoViableAltException("", 27, 4, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 27, 0, self.input)

                    raise nvae


                if alt27 == 1:
                    # grammar/ShyRecognizerFrontend.g:177:9: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID133 = self.match(self.input, ID, self.FOLLOW_ID_in_arbitrary_value1653)
                    ID133_tree = self._adaptor.createWithPayload(ID133)
                    self._adaptor.addChild(root_0, ID133_tree)




                elif alt27 == 2:
                    # grammar/ShyRecognizerFrontend.g:178:9: EXPRESSION
                    pass 
                    root_0 = self._adaptor.nil()


                    EXPRESSION134 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_arbitrary_value1663)
                    EXPRESSION134_tree = self._adaptor.createWithPayload(EXPRESSION134)
                    self._adaptor.addChild(root_0, EXPRESSION134_tree)




                elif alt27 == 3:
                    # grammar/ShyRecognizerFrontend.g:179:9: num_whole
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_whole_in_arbitrary_value1673)
                    num_whole135 = self.num_whole()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_whole135.tree)



                elif alt27 == 4:
                    # grammar/ShyRecognizerFrontend.g:180:9: num_fract
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_num_fract_in_arbitrary_value1683)
                    num_fract136 = self.num_fract()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, num_fract136.tree)



                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:183:1: consts : CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) ;
    def consts(self, ):
        retval = self.consts_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONSTS137 = None
        ID138 = None
        NEWLINE139 = None
        INDENT140 = None
        NEWLINE141 = None
        DEDENT143 = None
        NEWLINE144 = None
        consts_items142 = None


        CONSTS137_tree = None
        ID138_tree = None
        NEWLINE139_tree = None
        INDENT140_tree = None
        NEWLINE141_tree = None
        DEDENT143_tree = None
        NEWLINE144_tree = None
        stream_CONSTS = RewriteRuleTokenStream(self._adaptor, "token CONSTS")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_consts_items = RewriteRuleSubtreeStream(self._adaptor, "rule consts_items")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:184:5: ( CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE -> ^( TREE_CONSTS ID consts_items ) )
                # grammar/ShyRecognizerFrontend.g:184:9: CONSTS ID NEWLINE INDENT NEWLINE consts_items DEDENT NEWLINE
                pass 
                CONSTS137 = self.match(self.input, CONSTS, self.FOLLOW_CONSTS_in_consts1702) 
                stream_CONSTS.add(CONSTS137)


                ID138 = self.match(self.input, ID, self.FOLLOW_ID_in_consts1704) 
                stream_ID.add(ID138)


                NEWLINE139 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1706) 
                stream_NEWLINE.add(NEWLINE139)


                INDENT140 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_consts1716) 
                stream_INDENT.add(INDENT140)


                NEWLINE141 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1718) 
                stream_NEWLINE.add(NEWLINE141)


                self._state.following.append(self.FOLLOW_consts_items_in_consts1720)
                consts_items142 = self.consts_items()

                self._state.following.pop()
                stream_consts_items.add(consts_items142.tree)


                DEDENT143 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_consts1722) 
                stream_DEDENT.add(DEDENT143)


                NEWLINE144 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts1724) 
                stream_NEWLINE.add(NEWLINE144)


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
                # 186:9: -> ^( TREE_CONSTS ID consts_items )
                # grammar/ShyRecognizerFrontend.g:186:12: ^( TREE_CONSTS ID consts_items )
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
    # grammar/ShyRecognizerFrontend.g:188:1: consts_items : ( consts_item )+ ;
    def consts_items(self, ):
        retval = self.consts_items_return()
        retval.start = self.input.LT(1)


        root_0 = None

        consts_item145 = None



        try:
            try:
                # grammar/ShyRecognizerFrontend.g:188:14: ( ( consts_item )+ )
                # grammar/ShyRecognizerFrontend.g:188:16: ( consts_item )+
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:188:16: ( consts_item )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == ID) :
                        alt28 = 1


                    if alt28 == 1:
                        # grammar/ShyRecognizerFrontend.g:188:16: consts_item
                        pass 
                        self._state.following.append(self.FOLLOW_consts_item_in_consts_items1756)
                        consts_item145 = self.consts_item()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, consts_item145.tree)



                    else:
                        if cnt28 >= 1:
                            break #loop28

                        eee = EarlyExitException(28, self.input)
                        raise eee

                    cnt28 += 1




                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:189:1: consts_item : ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) );
    def consts_item(self, ):
        retval = self.consts_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID146 = None
        NEWLINE148 = None
        ID149 = None
        NEWLINE151 = None
        ID152 = None
        EXPRESSION153 = None
        NEWLINE154 = None
        num_whole147 = None

        num_fract150 = None


        ID146_tree = None
        NEWLINE148_tree = None
        ID149_tree = None
        NEWLINE151_tree = None
        ID152_tree = None
        EXPRESSION153_tree = None
        NEWLINE154_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_EXPRESSION = RewriteRuleTokenStream(self._adaptor, "token EXPRESSION")
        stream_num_fract = RewriteRuleSubtreeStream(self._adaptor, "rule num_fract")
        stream_num_whole = RewriteRuleSubtreeStream(self._adaptor, "rule num_whole")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:190:5: ( ID num_whole NEWLINE -> ^( TREE_NUM_WHOLE ID num_whole ) | ID num_fract NEWLINE -> ^( TREE_NUM_FRACT ID num_fract ) | ID EXPRESSION NEWLINE -> ^( TREE_EXPRESSION ID EXPRESSION ) )
                alt29 = 3
                LA29_0 = self.input.LA(1)

                if (LA29_0 == ID) :
                    LA29 = self.input.LA(2)
                    if LA29 == EXPRESSION:
                        alt29 = 3
                    elif LA29 == MINUS:
                        LA29_3 = self.input.LA(3)

                        if (LA29_3 == NUMBER) :
                            LA29_4 = self.input.LA(4)

                            if (LA29_4 == DIVIDE) :
                                alt29 = 2
                            elif (LA29_4 == NEWLINE) :
                                alt29 = 1
                            else:
                                nvae = NoViableAltException("", 29, 4, self.input)

                                raise nvae


                        else:
                            nvae = NoViableAltException("", 29, 3, self.input)

                            raise nvae


                    elif LA29 == NUMBER:
                        LA29_4 = self.input.LA(3)

                        if (LA29_4 == DIVIDE) :
                            alt29 = 2
                        elif (LA29_4 == NEWLINE) :
                            alt29 = 1
                        else:
                            nvae = NoViableAltException("", 29, 4, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 29, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # grammar/ShyRecognizerFrontend.g:190:9: ID num_whole NEWLINE
                    pass 
                    ID146 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1772) 
                    stream_ID.add(ID146)


                    self._state.following.append(self.FOLLOW_num_whole_in_consts_item1774)
                    num_whole147 = self.num_whole()

                    self._state.following.pop()
                    stream_num_whole.add(num_whole147.tree)


                    NEWLINE148 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1776) 
                    stream_NEWLINE.add(NEWLINE148)


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
                    # 190:30: -> ^( TREE_NUM_WHOLE ID num_whole )
                    # grammar/ShyRecognizerFrontend.g:190:33: ^( TREE_NUM_WHOLE ID num_whole )
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




                elif alt29 == 2:
                    # grammar/ShyRecognizerFrontend.g:191:9: ID num_fract NEWLINE
                    pass 
                    ID149 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1798) 
                    stream_ID.add(ID149)


                    self._state.following.append(self.FOLLOW_num_fract_in_consts_item1800)
                    num_fract150 = self.num_fract()

                    self._state.following.pop()
                    stream_num_fract.add(num_fract150.tree)


                    NEWLINE151 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1802) 
                    stream_NEWLINE.add(NEWLINE151)


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
                    # 191:30: -> ^( TREE_NUM_FRACT ID num_fract )
                    # grammar/ShyRecognizerFrontend.g:191:33: ^( TREE_NUM_FRACT ID num_fract )
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




                elif alt29 == 3:
                    # grammar/ShyRecognizerFrontend.g:192:9: ID EXPRESSION NEWLINE
                    pass 
                    ID152 = self.match(self.input, ID, self.FOLLOW_ID_in_consts_item1824) 
                    stream_ID.add(ID152)


                    EXPRESSION153 = self.match(self.input, EXPRESSION, self.FOLLOW_EXPRESSION_in_consts_item1826) 
                    stream_EXPRESSION.add(EXPRESSION153)


                    NEWLINE154 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_consts_item1828) 
                    stream_NEWLINE.add(NEWLINE154)


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
                    # 192:31: -> ^( TREE_EXPRESSION ID EXPRESSION )
                    # grammar/ShyRecognizerFrontend.g:192:34: ^( TREE_EXPRESSION ID EXPRESSION )
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
    # grammar/ShyRecognizerFrontend.g:195:1: types : TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) ;
    def types(self, ):
        retval = self.types_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPES155 = None
        ID156 = None
        NEWLINE157 = None
        INDENT158 = None
        NEWLINE159 = None
        DEDENT161 = None
        NEWLINE162 = None
        types_item160 = None


        TYPES155_tree = None
        ID156_tree = None
        NEWLINE157_tree = None
        INDENT158_tree = None
        NEWLINE159_tree = None
        DEDENT161_tree = None
        NEWLINE162_tree = None
        stream_TYPES = RewriteRuleTokenStream(self._adaptor, "token TYPES")
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_types_item = RewriteRuleSubtreeStream(self._adaptor, "rule types_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:196:5: ( TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE -> ^( TREE_TYPES ID ( types_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:196:9: TYPES ID NEWLINE INDENT NEWLINE ( types_item )+ DEDENT NEWLINE
                pass 
                TYPES155 = self.match(self.input, TYPES, self.FOLLOW_TYPES_in_types1859) 
                stream_TYPES.add(TYPES155)


                ID156 = self.match(self.input, ID, self.FOLLOW_ID_in_types1861) 
                stream_ID.add(ID156)


                NEWLINE157 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1863) 
                stream_NEWLINE.add(NEWLINE157)


                INDENT158 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_types1873) 
                stream_INDENT.add(INDENT158)


                NEWLINE159 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1875) 
                stream_NEWLINE.add(NEWLINE159)


                # grammar/ShyRecognizerFrontend.g:197:24: ( types_item )+
                cnt30 = 0
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == ID) :
                        alt30 = 1


                    if alt30 == 1:
                        # grammar/ShyRecognizerFrontend.g:197:24: types_item
                        pass 
                        self._state.following.append(self.FOLLOW_types_item_in_types1877)
                        types_item160 = self.types_item()

                        self._state.following.pop()
                        stream_types_item.add(types_item160.tree)



                    else:
                        if cnt30 >= 1:
                            break #loop30

                        eee = EarlyExitException(30, self.input)
                        raise eee

                    cnt30 += 1


                DEDENT161 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_types1881) 
                stream_DEDENT.add(DEDENT161)


                NEWLINE162 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_types1883) 
                stream_NEWLINE.add(NEWLINE162)


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
                # 198:9: -> ^( TREE_TYPES ID ( types_item )+ )
                # grammar/ShyRecognizerFrontend.g:198:12: ^( TREE_TYPES ID ( types_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_TYPES, "TREE_TYPES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:198:29: ( types_item )+
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
    # grammar/ShyRecognizerFrontend.g:200:1: types_item : ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) ;
    def types_item(self, ):
        retval = self.types_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID163 = None
        attrs_hints164 = None


        ID163_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:200:12: ( ID attrs_hints -> ^( TREE_TYPES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:200:14: ID attrs_hints
                pass 
                ID163 = self.match(self.input, ID, self.FOLLOW_ID_in_types_item1917) 
                stream_ID.add(ID163)


                self._state.following.append(self.FOLLOW_attrs_hints_in_types_item1919)
                attrs_hints164 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints164.tree)


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
                # 200:29: -> ^( TREE_TYPES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:200:32: ^( TREE_TYPES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:202:1: messages : MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) ;
    def messages(self, ):
        retval = self.messages_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MESSAGES165 = None
        ID166 = None
        NEWLINE167 = None
        INDENT168 = None
        NEWLINE169 = None
        DEDENT171 = None
        NEWLINE172 = None
        messages_item170 = None


        MESSAGES165_tree = None
        ID166_tree = None
        NEWLINE167_tree = None
        INDENT168_tree = None
        NEWLINE169_tree = None
        DEDENT171_tree = None
        NEWLINE172_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_MESSAGES = RewriteRuleTokenStream(self._adaptor, "token MESSAGES")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_messages_item = RewriteRuleSubtreeStream(self._adaptor, "rule messages_item")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:203:5: ( MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE -> ^( TREE_MESSAGES ID ( messages_item )+ ) )
                # grammar/ShyRecognizerFrontend.g:203:9: MESSAGES ID NEWLINE INDENT NEWLINE ( messages_item )+ DEDENT NEWLINE
                pass 
                MESSAGES165 = self.match(self.input, MESSAGES, self.FOLLOW_MESSAGES_in_messages1946) 
                stream_MESSAGES.add(MESSAGES165)


                ID166 = self.match(self.input, ID, self.FOLLOW_ID_in_messages1948) 
                stream_ID.add(ID166)


                NEWLINE167 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1950) 
                stream_NEWLINE.add(NEWLINE167)


                INDENT168 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_messages1960) 
                stream_INDENT.add(INDENT168)


                NEWLINE169 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1962) 
                stream_NEWLINE.add(NEWLINE169)


                # grammar/ShyRecognizerFrontend.g:204:24: ( messages_item )+
                cnt31 = 0
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == ID) :
                        alt31 = 1


                    if alt31 == 1:
                        # grammar/ShyRecognizerFrontend.g:204:24: messages_item
                        pass 
                        self._state.following.append(self.FOLLOW_messages_item_in_messages1964)
                        messages_item170 = self.messages_item()

                        self._state.following.pop()
                        stream_messages_item.add(messages_item170.tree)



                    else:
                        if cnt31 >= 1:
                            break #loop31

                        eee = EarlyExitException(31, self.input)
                        raise eee

                    cnt31 += 1


                DEDENT171 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_messages1968) 
                stream_DEDENT.add(DEDENT171)


                NEWLINE172 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_messages1970) 
                stream_NEWLINE.add(NEWLINE172)


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
                # 205:9: -> ^( TREE_MESSAGES ID ( messages_item )+ )
                # grammar/ShyRecognizerFrontend.g:205:12: ^( TREE_MESSAGES ID ( messages_item )+ )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(
                self._adaptor.createFromType(TREE_MESSAGES, "TREE_MESSAGES")
                , root_1)

                self._adaptor.addChild(root_1, 
                stream_ID.nextNode()
                )

                # grammar/ShyRecognizerFrontend.g:205:32: ( messages_item )+
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
    # grammar/ShyRecognizerFrontend.g:207:1: messages_item : ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) ;
    def messages_item(self, ):
        retval = self.messages_item_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID173 = None
        attrs_hints174 = None


        ID173_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:207:15: ( ID attrs_hints -> ^( TREE_MESSAGES_ITEM ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:207:17: ID attrs_hints
                pass 
                ID173 = self.match(self.input, ID, self.FOLLOW_ID_in_messages_item2004) 
                stream_ID.add(ID173)


                self._state.following.append(self.FOLLOW_attrs_hints_in_messages_item2006)
                attrs_hints174 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints174.tree)


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
                # 207:32: -> ^( TREE_MESSAGES_ITEM ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:207:35: ^( TREE_MESSAGES_ITEM ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:209:1: vars : VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) ;
    def vars(self, ):
        retval = self.vars_return()
        retval.start = self.input.LT(1)


        root_0 = None

        VARS175 = None
        ID176 = None
        attrs_hints177 = None


        VARS175_tree = None
        ID176_tree = None
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_VARS = RewriteRuleTokenStream(self._adaptor, "token VARS")
        stream_attrs_hints = RewriteRuleSubtreeStream(self._adaptor, "rule attrs_hints")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:210:5: ( VARS ID attrs_hints -> ^( TREE_VARS ID attrs_hints ) )
                # grammar/ShyRecognizerFrontend.g:210:9: VARS ID attrs_hints
                pass 
                VARS175 = self.match(self.input, VARS, self.FOLLOW_VARS_in_vars2033) 
                stream_VARS.add(VARS175)


                ID176 = self.match(self.input, ID, self.FOLLOW_ID_in_vars2035) 
                stream_ID.add(ID176)


                self._state.following.append(self.FOLLOW_attrs_hints_in_vars2037)
                attrs_hints177 = self.attrs_hints()

                self._state.following.pop()
                stream_attrs_hints.add(attrs_hints177.tree)


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
                # 211:9: -> ^( TREE_VARS ID attrs_hints )
                # grammar/ShyRecognizerFrontend.g:211:12: ^( TREE_VARS ID attrs_hints )
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
    # grammar/ShyRecognizerFrontend.g:214:1: attrs_hints : ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ );
    def attrs_hints(self, ):
        retval = self.attrs_hints_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE179 = None
        NEWLINE180 = None
        INDENT181 = None
        NEWLINE182 = None
        NEWLINE184 = None
        DEDENT185 = None
        NEWLINE186 = None
        NEWLINE188 = None
        INDENT189 = None
        NEWLINE190 = None
        NEWLINE192 = None
        DEDENT193 = None
        NEWLINE194 = None
        attr_hint178 = None

        attr_hint183 = None

        attr_hint187 = None

        attr_hint191 = None


        NEWLINE179_tree = None
        NEWLINE180_tree = None
        INDENT181_tree = None
        NEWLINE182_tree = None
        NEWLINE184_tree = None
        DEDENT185_tree = None
        NEWLINE186_tree = None
        NEWLINE188_tree = None
        INDENT189_tree = None
        NEWLINE190_tree = None
        NEWLINE192_tree = None
        DEDENT193_tree = None
        NEWLINE194_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_attr_hint = RewriteRuleSubtreeStream(self._adaptor, "rule attr_hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:215:5: ( attr_hint NEWLINE -> TREE_ATTRS_HINTS attr_hint | NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ | attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE ) -> TREE_ATTRS_HINTS ( attr_hint )+ )
                alt34 = 3
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # grammar/ShyRecognizerFrontend.g:215:9: attr_hint NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2076)
                    attr_hint178 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint178.tree)


                    NEWLINE179 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2078) 
                    stream_NEWLINE.add(NEWLINE179)


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
                    # 216:9: -> TREE_ATTRS_HINTS attr_hint
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    self._adaptor.addChild(root_0, stream_attr_hint.nextTree())




                    retval.tree = root_0




                elif alt34 == 2:
                    # grammar/ShyRecognizerFrontend.g:217:9: NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    NEWLINE180 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2102) 
                    stream_NEWLINE.add(NEWLINE180)


                    # grammar/ShyRecognizerFrontend.g:218:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:218:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT181 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2114) 
                    stream_INDENT.add(INDENT181)


                    NEWLINE182 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2116) 
                    stream_NEWLINE.add(NEWLINE182)


                    # grammar/ShyRecognizerFrontend.g:218:26: ( attr_hint NEWLINE )+
                    cnt32 = 0
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == CURLY_OPEN or LA32_0 == ID) :
                            alt32 = 1


                        if alt32 == 1:
                            # grammar/ShyRecognizerFrontend.g:218:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2120)
                            attr_hint183 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint183.tree)


                            NEWLINE184 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2122) 
                            stream_NEWLINE.add(NEWLINE184)



                        else:
                            if cnt32 >= 1:
                                break #loop32

                            eee = EarlyExitException(32, self.input)
                            raise eee

                        cnt32 += 1


                    DEDENT185 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2128) 
                    stream_DEDENT.add(DEDENT185)


                    NEWLINE186 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2130) 
                    stream_NEWLINE.add(NEWLINE186)





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
                    # 219:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:219:29: ( attr_hint )+
                    if not (stream_attr_hint.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_attr_hint.hasNext():
                        self._adaptor.addChild(root_0, stream_attr_hint.nextTree())


                    stream_attr_hint.reset()




                    retval.tree = root_0




                elif alt34 == 3:
                    # grammar/ShyRecognizerFrontend.g:220:9: attr_hint NEWLINE ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    pass 
                    self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2158)
                    attr_hint187 = self.attr_hint()

                    self._state.following.pop()
                    stream_attr_hint.add(attr_hint187.tree)


                    NEWLINE188 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2160) 
                    stream_NEWLINE.add(NEWLINE188)


                    # grammar/ShyRecognizerFrontend.g:221:9: ( INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE )
                    # grammar/ShyRecognizerFrontend.g:221:11: INDENT NEWLINE ( attr_hint NEWLINE )+ DEDENT NEWLINE
                    pass 
                    INDENT189 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attrs_hints2172) 
                    stream_INDENT.add(INDENT189)


                    NEWLINE190 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2174) 
                    stream_NEWLINE.add(NEWLINE190)


                    # grammar/ShyRecognizerFrontend.g:221:26: ( attr_hint NEWLINE )+
                    cnt33 = 0
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == CURLY_OPEN or LA33_0 == ID) :
                            alt33 = 1


                        if alt33 == 1:
                            # grammar/ShyRecognizerFrontend.g:221:28: attr_hint NEWLINE
                            pass 
                            self._state.following.append(self.FOLLOW_attr_hint_in_attrs_hints2178)
                            attr_hint191 = self.attr_hint()

                            self._state.following.pop()
                            stream_attr_hint.add(attr_hint191.tree)


                            NEWLINE192 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2180) 
                            stream_NEWLINE.add(NEWLINE192)



                        else:
                            if cnt33 >= 1:
                                break #loop33

                            eee = EarlyExitException(33, self.input)
                            raise eee

                        cnt33 += 1


                    DEDENT193 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attrs_hints2186) 
                    stream_DEDENT.add(DEDENT193)


                    NEWLINE194 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attrs_hints2188) 
                    stream_NEWLINE.add(NEWLINE194)





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
                    # 222:9: -> TREE_ATTRS_HINTS ( attr_hint )+
                    self._adaptor.addChild(root_0, 
                    self._adaptor.createFromType(TREE_ATTRS_HINTS, "TREE_ATTRS_HINTS")
                    )

                    # grammar/ShyRecognizerFrontend.g:222:29: ( attr_hint )+
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
    # grammar/ShyRecognizerFrontend.g:224:1: attr_hint : ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) );
    def attr_hint(self, ):
        retval = self.attr_hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ID195 = None
        ID197 = None
        NEWLINE199 = None
        INDENT200 = None
        NEWLINE201 = None
        ID202 = None
        NEWLINE203 = None
        DEDENT204 = None
        hint196 = None

        hint198 = None


        ID195_tree = None
        ID197_tree = None
        NEWLINE199_tree = None
        INDENT200_tree = None
        NEWLINE201_tree = None
        ID202_tree = None
        NEWLINE203_tree = None
        DEDENT204_tree = None
        stream_DEDENT = RewriteRuleTokenStream(self._adaptor, "token DEDENT")
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_INDENT = RewriteRuleTokenStream(self._adaptor, "token INDENT")
        stream_hint = RewriteRuleSubtreeStream(self._adaptor, "rule hint")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:225:5: ( ( ID )+ -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ ) | hint ( ID )+ -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) | hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ ) )
                alt39 = 3
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # grammar/ShyRecognizerFrontend.g:225:9: ( ID )+
                    pass 
                    # grammar/ShyRecognizerFrontend.g:225:9: ( ID )+
                    cnt35 = 0
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == ID) :
                            alt35 = 1


                        if alt35 == 1:
                            # grammar/ShyRecognizerFrontend.g:225:9: ID
                            pass 
                            ID195 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2225) 
                            stream_ID.add(ID195)



                        else:
                            if cnt35 >= 1:
                                break #loop35

                            eee = EarlyExitException(35, self.input)
                            raise eee

                        cnt35 += 1


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
                    # 226:9: -> ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:226:12: ^( TREE_ATTR_HINT TREE_HINT_NONE ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    self._adaptor.createFromType(TREE_HINT_NONE, "TREE_HINT_NONE")
                    )

                    # grammar/ShyRecognizerFrontend.g:226:45: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:226:45: ^( TREE_ATTR ID )
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




                elif alt39 == 2:
                    # grammar/ShyRecognizerFrontend.g:227:9: hint ( ID )+
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2266)
                    hint196 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint196.tree)


                    # grammar/ShyRecognizerFrontend.g:227:14: ( ID )+
                    cnt36 = 0
                    while True: #loop36
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == ID) :
                            alt36 = 1


                        if alt36 == 1:
                            # grammar/ShyRecognizerFrontend.g:227:14: ID
                            pass 
                            ID197 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2268) 
                            stream_ID.add(ID197)



                        else:
                            if cnt36 >= 1:
                                break #loop36

                            eee = EarlyExitException(36, self.input)
                            raise eee

                        cnt36 += 1


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
                    # 228:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:228:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:228:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:228:35: ^( TREE_ATTR ID )
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




                elif alt39 == 3:
                    # grammar/ShyRecognizerFrontend.g:229:9: hint NEWLINE INDENT NEWLINE ( ( ID )+ NEWLINE )+ DEDENT
                    pass 
                    self._state.following.append(self.FOLLOW_hint_in_attr_hint2308)
                    hint198 = self.hint()

                    self._state.following.pop()
                    stream_hint.add(hint198.tree)


                    NEWLINE199 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2310) 
                    stream_NEWLINE.add(NEWLINE199)


                    INDENT200 = self.match(self.input, INDENT, self.FOLLOW_INDENT_in_attr_hint2312) 
                    stream_INDENT.add(INDENT200)


                    NEWLINE201 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2314) 
                    stream_NEWLINE.add(NEWLINE201)


                    # grammar/ShyRecognizerFrontend.g:229:37: ( ( ID )+ NEWLINE )+
                    cnt38 = 0
                    while True: #loop38
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == ID) :
                            alt38 = 1


                        if alt38 == 1:
                            # grammar/ShyRecognizerFrontend.g:229:39: ( ID )+ NEWLINE
                            pass 
                            # grammar/ShyRecognizerFrontend.g:229:39: ( ID )+
                            cnt37 = 0
                            while True: #loop37
                                alt37 = 2
                                LA37_0 = self.input.LA(1)

                                if (LA37_0 == ID) :
                                    alt37 = 1


                                if alt37 == 1:
                                    # grammar/ShyRecognizerFrontend.g:229:39: ID
                                    pass 
                                    ID202 = self.match(self.input, ID, self.FOLLOW_ID_in_attr_hint2318) 
                                    stream_ID.add(ID202)



                                else:
                                    if cnt37 >= 1:
                                        break #loop37

                                    eee = EarlyExitException(37, self.input)
                                    raise eee

                                cnt37 += 1


                            NEWLINE203 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_attr_hint2322) 
                            stream_NEWLINE.add(NEWLINE203)



                        else:
                            if cnt38 >= 1:
                                break #loop38

                            eee = EarlyExitException(38, self.input)
                            raise eee

                        cnt38 += 1


                    DEDENT204 = self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_attr_hint2328) 
                    stream_DEDENT.add(DEDENT204)


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
                    # 230:9: -> ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    # grammar/ShyRecognizerFrontend.g:230:12: ^( TREE_ATTR_HINT hint ( ^( TREE_ATTR ID ) )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_ATTR_HINT, "TREE_ATTR_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_hint.nextTree())

                    # grammar/ShyRecognizerFrontend.g:230:35: ( ^( TREE_ATTR ID ) )+
                    if not (stream_ID.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_ID.hasNext():
                        # grammar/ShyRecognizerFrontend.g:230:35: ^( TREE_ATTR ID )
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
    # grammar/ShyRecognizerFrontend.g:233:1: hint : ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) );
    def hint(self, ):
        retval = self.hint_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CURLY_OPEN205 = None
        ID206 = None
        CURLY_CLOSE207 = None
        CURLY_OPEN208 = None
        ID209 = None
        CURLY_CLOSE211 = None
        hint_arg210 = None


        CURLY_OPEN205_tree = None
        ID206_tree = None
        CURLY_CLOSE207_tree = None
        CURLY_OPEN208_tree = None
        ID209_tree = None
        CURLY_CLOSE211_tree = None
        stream_CURLY_OPEN = RewriteRuleTokenStream(self._adaptor, "token CURLY_OPEN")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_CURLY_CLOSE = RewriteRuleTokenStream(self._adaptor, "token CURLY_CLOSE")
        stream_hint_arg = RewriteRuleSubtreeStream(self._adaptor, "rule hint_arg")
        try:
            try:
                # grammar/ShyRecognizerFrontend.g:234:5: ( CURLY_OPEN ID CURLY_CLOSE -> ^( TREE_HINT ID ) | CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE -> ^( TREE_HINT ID ( hint_arg )+ ) )
                alt41 = 2
                LA41_0 = self.input.LA(1)

                if (LA41_0 == CURLY_OPEN) :
                    LA41_1 = self.input.LA(2)

                    if (LA41_1 == ID) :
                        LA41_2 = self.input.LA(3)

                        if (LA41_2 == CURLY_CLOSE) :
                            alt41 = 1
                        elif (LA41_2 == ID or LA41_2 == UNDERSCORE) :
                            alt41 = 2
                        else:
                            nvae = NoViableAltException("", 41, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 41, 1, self.input)

                        raise nvae


                else:
                    nvae = NoViableAltException("", 41, 0, self.input)

                    raise nvae


                if alt41 == 1:
                    # grammar/ShyRecognizerFrontend.g:234:9: CURLY_OPEN ID CURLY_CLOSE
                    pass 
                    CURLY_OPEN205 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2375) 
                    stream_CURLY_OPEN.add(CURLY_OPEN205)


                    ID206 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2377) 
                    stream_ID.add(ID206)


                    CURLY_CLOSE207 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2379) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE207)


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
                    # 234:35: -> ^( TREE_HINT ID )
                    # grammar/ShyRecognizerFrontend.g:234:38: ^( TREE_HINT ID )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt41 == 2:
                    # grammar/ShyRecognizerFrontend.g:235:9: CURLY_OPEN ID ( hint_arg )+ CURLY_CLOSE
                    pass 
                    CURLY_OPEN208 = self.match(self.input, CURLY_OPEN, self.FOLLOW_CURLY_OPEN_in_hint2399) 
                    stream_CURLY_OPEN.add(CURLY_OPEN208)


                    ID209 = self.match(self.input, ID, self.FOLLOW_ID_in_hint2401) 
                    stream_ID.add(ID209)


                    # grammar/ShyRecognizerFrontend.g:235:23: ( hint_arg )+
                    cnt40 = 0
                    while True: #loop40
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == ID or LA40_0 == UNDERSCORE) :
                            alt40 = 1


                        if alt40 == 1:
                            # grammar/ShyRecognizerFrontend.g:235:23: hint_arg
                            pass 
                            self._state.following.append(self.FOLLOW_hint_arg_in_hint2403)
                            hint_arg210 = self.hint_arg()

                            self._state.following.pop()
                            stream_hint_arg.add(hint_arg210.tree)



                        else:
                            if cnt40 >= 1:
                                break #loop40

                            eee = EarlyExitException(40, self.input)
                            raise eee

                        cnt40 += 1


                    CURLY_CLOSE211 = self.match(self.input, CURLY_CLOSE, self.FOLLOW_CURLY_CLOSE_in_hint2407) 
                    stream_CURLY_CLOSE.add(CURLY_CLOSE211)


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
                    # 235:46: -> ^( TREE_HINT ID ( hint_arg )+ )
                    # grammar/ShyRecognizerFrontend.g:235:49: ^( TREE_HINT ID ( hint_arg )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(TREE_HINT, "TREE_HINT")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    # grammar/ShyRecognizerFrontend.g:235:65: ( hint_arg )+
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
    # grammar/ShyRecognizerFrontend.g:237:1: hint_arg : ( ID | UNDERSCORE );
    def hint_arg(self, ):
        retval = self.hint_arg_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set212 = None

        set212_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:237:10: ( ID | UNDERSCORE )
                # grammar/ShyRecognizerFrontend.g:
                pass 
                root_0 = self._adaptor.nil()


                set212 = self.input.LT(1)

                if self.input.LA(1) == ID or self.input.LA(1) == UNDERSCORE:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set212))

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
    # grammar/ShyRecognizerFrontend.g:239:1: num_whole : ( MINUS )? NUMBER ;
    def num_whole(self, ):
        retval = self.num_whole_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS213 = None
        NUMBER214 = None

        MINUS213_tree = None
        NUMBER214_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:239:11: ( ( MINUS )? NUMBER )
                # grammar/ShyRecognizerFrontend.g:239:13: ( MINUS )? NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:239:13: ( MINUS )?
                alt42 = 2
                LA42_0 = self.input.LA(1)

                if (LA42_0 == MINUS) :
                    alt42 = 1
                if alt42 == 1:
                    # grammar/ShyRecognizerFrontend.g:239:13: MINUS
                    pass 
                    MINUS213 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_whole2446)
                    MINUS213_tree = self._adaptor.createWithPayload(MINUS213)
                    self._adaptor.addChild(root_0, MINUS213_tree)






                NUMBER214 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_whole2450)
                NUMBER214_tree = self._adaptor.createWithPayload(NUMBER214)
                self._adaptor.addChild(root_0, NUMBER214_tree)





                retval.stop = self.input.LT(-1)


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
    # grammar/ShyRecognizerFrontend.g:240:1: num_fract : ( MINUS )? NUMBER DIVIDE NUMBER ;
    def num_fract(self, ):
        retval = self.num_fract_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MINUS215 = None
        NUMBER216 = None
        DIVIDE217 = None
        NUMBER218 = None

        MINUS215_tree = None
        NUMBER216_tree = None
        DIVIDE217_tree = None
        NUMBER218_tree = None

        try:
            try:
                # grammar/ShyRecognizerFrontend.g:240:11: ( ( MINUS )? NUMBER DIVIDE NUMBER )
                # grammar/ShyRecognizerFrontend.g:240:13: ( MINUS )? NUMBER DIVIDE NUMBER
                pass 
                root_0 = self._adaptor.nil()


                # grammar/ShyRecognizerFrontend.g:240:13: ( MINUS )?
                alt43 = 2
                LA43_0 = self.input.LA(1)

                if (LA43_0 == MINUS) :
                    alt43 = 1
                if alt43 == 1:
                    # grammar/ShyRecognizerFrontend.g:240:13: MINUS
                    pass 
                    MINUS215 = self.match(self.input, MINUS, self.FOLLOW_MINUS_in_num_fract2458)
                    MINUS215_tree = self._adaptor.createWithPayload(MINUS215)
                    self._adaptor.addChild(root_0, MINUS215_tree)






                NUMBER216 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2462)
                NUMBER216_tree = self._adaptor.createWithPayload(NUMBER216)
                self._adaptor.addChild(root_0, NUMBER216_tree)



                DIVIDE217 = self.match(self.input, DIVIDE, self.FOLLOW_DIVIDE_in_num_fract2464)
                DIVIDE217_tree = self._adaptor.createWithPayload(DIVIDE217)
                self._adaptor.addChild(root_0, DIVIDE217_tree)



                NUMBER218 = self.match(self.input, NUMBER, self.FOLLOW_NUMBER_in_num_fract2466)
                NUMBER218_tree = self._adaptor.createWithPayload(NUMBER218)
                self._adaptor.addChild(root_0, NUMBER218_tree)





                retval.stop = self.input.LT(-1)


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
        u"\1\23\1\7\3\uffff\1\7\1\22\1\33\1\16\1\15\1\uffff\1\22\1\33\2\uffff"
        u"\1\22"
        )

    DFA10_max = DFA.unpack(
        u"\1\116\1\33\3\uffff\4\33\1\116\1\uffff\2\33\2\uffff\1\33"
        )

    DFA10_accept = DFA.unpack(
        u"\2\uffff\1\3\1\5\1\6\5\uffff\1\4\2\uffff\1\2\1\1\1\uffff"
        )

    DFA10_special = DFA.unpack(
        u"\20\uffff"
        )


    DFA10_transition = [
        DFA.unpack(u"\1\1\1\2\67\uffff\1\3\1\uffff\1\4"),
        DFA.unpack(u"\1\12\12\uffff\1\6\1\5\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\12\12\uffff\1\6\1\5\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u"\1\6\1\13\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u"\1\10"),
        DFA.unpack(u"\1\14\3\uffff\1\6\1\13\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u"\1\16\5\uffff\2\16\1\15\66\uffff\1\16\1\uffff\1\16"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\13\3\uffff\1\7\2\uffff\1\11\1\10"),
        DFA.unpack(u"\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\6\1\13\3\uffff\1\7\2\uffff\1\11\1\10")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #21

    DFA21_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA21_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA21_min = DFA.unpack(
        u"\1\23\3\17\1\33\1\16\1\17\1\uffff\1\33\1\uffff\1\17"
        )

    DFA21_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\uffff\1\33\1\uffff\1\33"
        )

    DFA21_accept = DFA.unpack(
        u"\7\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA21_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA21_transition = [
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

    # class definition for DFA #21

    class DFA21(DFA):
        pass


    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\13\uffff"
        )

    DFA22_eof = DFA.unpack(
        u"\13\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\1\23\3\22\1\33\1\16\1\15\1\33\2\uffff\1\22"
        )

    DFA22_max = DFA.unpack(
        u"\1\23\5\33\1\25\1\33\2\uffff\1\33"
        )

    DFA22_accept = DFA.unpack(
        u"\10\uffff\1\2\1\1\1\uffff"
        )

    DFA22_special = DFA.unpack(
        u"\13\uffff"
        )


    DFA22_transition = [
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

    # class definition for DFA #22

    class DFA22(DFA):
        pass


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\4\uffff\1\6\15\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\1\14\2\23\1\uffff\1\11\1\13\2\uffff\1\23\1\13\1\23\1\25\1\23\1"
        u"\32\2\23\1\15\1\32"
        )

    DFA34_max = DFA.unpack(
        u"\2\32\1\23\1\uffff\1\113\1\112\2\uffff\1\32\1\112\1\32\1\25\2\32"
        u"\1\23\1\32\1\23\1\32"
        )

    DFA34_accept = DFA.unpack(
        u"\3\uffff\1\2\2\uffff\1\1\1\3\12\uffff"
        )

    DFA34_special = DFA.unpack(
        u"\22\uffff"
        )


    DFA34_transition = [
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

    # class definition for DFA #34

    class DFA34(DFA):
        pass


    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        u"\11\uffff"
        )

    DFA39_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA39_min = DFA.unpack(
        u"\1\14\1\uffff\1\23\1\13\1\23\1\13\2\uffff\1\23"
        )

    DFA39_max = DFA.unpack(
        u"\1\23\1\uffff\1\23\1\112\1\32\1\112\2\uffff\1\32"
        )

    DFA39_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\2\1\3\1\uffff"
        )

    DFA39_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA39_transition = [
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

    # class definition for DFA #39

    class DFA39(DFA):
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
    FOLLOW_NEWLINE_in_proc_ops556 = frozenset([19, 20, 76, 78])
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
    FOLLOW_statement_in_statements680 = frozenset([1, 19, 20, 76, 78])
    FOLLOW_WITH_in_statement_with722 = frozenset([19])
    FOLLOW_ID_in_statement_with724 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with726 = frozenset([21])
    FOLLOW_INDENT_in_statement_with736 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with738 = frozenset([19, 20, 76, 78])
    FOLLOW_statements_in_statement_with740 = frozenset([13])
    FOLLOW_DEDENT_in_statement_with742 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_with744 = frozenset([1])
    FOLLOW_ID_in_statement_assign784 = frozenset([7, 19])
    FOLLOW_ARROW_LEFT_in_statement_assign788 = frozenset([18, 19, 23, 27])
    FOLLOW_arbitrary_value_in_statement_assign790 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_NEWLINE_in_statement_assign794 = frozenset([1])
    FOLLOW_WHILE_in_statement_while888 = frozenset([4, 5, 19])
    FOLLOW_condition_in_statement_while890 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_while892 = frozenset([15])
    FOLLOW_DO_in_statement_while896 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while898 = frozenset([21])
    FOLLOW_INDENT_in_statement_while912 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while914 = frozenset([19, 20, 76, 78])
    FOLLOW_statements_in_statement_while916 = frozenset([13])
    FOLLOW_DEDENT_in_statement_while918 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_while920 = frozenset([1])
    FOLLOW_statement_if_head_in_statement_if960 = frozenset([1, 16, 17])
    FOLLOW_statement_elif_in_statement_if970 = frozenset([1, 16, 17])
    FOLLOW_statement_else_in_statement_if982 = frozenset([1])
    FOLLOW_IF_in_statement_if_head1090 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_if_head1092 = frozenset([1])
    FOLLOW_ELIF_in_statement_elif1124 = frozenset([4, 5, 19])
    FOLLOW_statement_elif_body_in_statement_elif1126 = frozenset([1])
    FOLLOW_condition_in_statement_elif_body1158 = frozenset([15, 26])
    FOLLOW_NEWLINE_in_statement_elif_body1160 = frozenset([15])
    FOLLOW_DO_in_statement_elif_body1164 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1166 = frozenset([21])
    FOLLOW_INDENT_in_statement_elif_body1180 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1182 = frozenset([19, 20, 76, 78])
    FOLLOW_statements_in_statement_elif_body1184 = frozenset([13])
    FOLLOW_DEDENT_in_statement_elif_body1186 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_elif_body1188 = frozenset([1])
    FOLLOW_ELSE_in_statement_else1228 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1230 = frozenset([21])
    FOLLOW_INDENT_in_statement_else1244 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1246 = frozenset([19, 20, 76, 78])
    FOLLOW_statements_in_statement_else1248 = frozenset([13])
    FOLLOW_DEDENT_in_statement_else1250 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_else1252 = frozenset([1])
    FOLLOW_condition_call_in_condition1290 = frozenset([1])
    FOLLOW_ANY_in_condition1319 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1321 = frozenset([1])
    FOLLOW_ALL_in_condition1350 = frozenset([19, 26])
    FOLLOW_condition_calls_in_condition1352 = frozenset([1])
    FOLLOW_condition_call_in_condition_calls1390 = frozenset([1])
    FOLLOW_NEWLINE_in_condition_calls1400 = frozenset([21])
    FOLLOW_INDENT_in_condition_calls1402 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1404 = frozenset([19])
    FOLLOW_condition_call_line_in_condition_calls1406 = frozenset([13, 19])
    FOLLOW_DEDENT_in_condition_calls1410 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_calls1412 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call1446 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call1456 = frozenset([1])
    FOLLOW_statement_call_single_line_in_condition_call_line1475 = frozenset([26])
    FOLLOW_NEWLINE_in_condition_call_line1477 = frozenset([1])
    FOLLOW_statement_call_multi_line_in_condition_call_line1503 = frozenset([1])
    FOLLOW_ID_in_statement_call_single_line1522 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_single_line1524 = frozenset([1])
    FOLLOW_ID_in_statement_call_multi_line1568 = frozenset([18, 19, 23, 26, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1570 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1574 = frozenset([21])
    FOLLOW_INDENT_in_statement_call_multi_line1584 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1586 = frozenset([18, 19, 23, 27])
    FOLLOW_statement_call_args_in_statement_call_multi_line1590 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1592 = frozenset([13, 18, 19, 23, 27])
    FOLLOW_DEDENT_in_statement_call_multi_line1598 = frozenset([26])
    FOLLOW_NEWLINE_in_statement_call_multi_line1600 = frozenset([1])
    FOLLOW_arbitrary_value_in_statement_call_args1636 = frozenset([1, 18, 19, 23, 27])
    FOLLOW_ID_in_arbitrary_value1653 = frozenset([1])
    FOLLOW_EXPRESSION_in_arbitrary_value1663 = frozenset([1])
    FOLLOW_num_whole_in_arbitrary_value1673 = frozenset([1])
    FOLLOW_num_fract_in_arbitrary_value1683 = frozenset([1])
    FOLLOW_CONSTS_in_consts1702 = frozenset([19])
    FOLLOW_ID_in_consts1704 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1706 = frozenset([21])
    FOLLOW_INDENT_in_consts1716 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1718 = frozenset([19])
    FOLLOW_consts_items_in_consts1720 = frozenset([13])
    FOLLOW_DEDENT_in_consts1722 = frozenset([26])
    FOLLOW_NEWLINE_in_consts1724 = frozenset([1])
    FOLLOW_consts_item_in_consts_items1756 = frozenset([1, 19])
    FOLLOW_ID_in_consts_item1772 = frozenset([23, 27])
    FOLLOW_num_whole_in_consts_item1774 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1776 = frozenset([1])
    FOLLOW_ID_in_consts_item1798 = frozenset([23, 27])
    FOLLOW_num_fract_in_consts_item1800 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1802 = frozenset([1])
    FOLLOW_ID_in_consts_item1824 = frozenset([18])
    FOLLOW_EXPRESSION_in_consts_item1826 = frozenset([26])
    FOLLOW_NEWLINE_in_consts_item1828 = frozenset([1])
    FOLLOW_TYPES_in_types1859 = frozenset([19])
    FOLLOW_ID_in_types1861 = frozenset([26])
    FOLLOW_NEWLINE_in_types1863 = frozenset([21])
    FOLLOW_INDENT_in_types1873 = frozenset([26])
    FOLLOW_NEWLINE_in_types1875 = frozenset([19])
    FOLLOW_types_item_in_types1877 = frozenset([13, 19])
    FOLLOW_DEDENT_in_types1881 = frozenset([26])
    FOLLOW_NEWLINE_in_types1883 = frozenset([1])
    FOLLOW_ID_in_types_item1917 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_types_item1919 = frozenset([1])
    FOLLOW_MESSAGES_in_messages1946 = frozenset([19])
    FOLLOW_ID_in_messages1948 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1950 = frozenset([21])
    FOLLOW_INDENT_in_messages1960 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1962 = frozenset([19])
    FOLLOW_messages_item_in_messages1964 = frozenset([13, 19])
    FOLLOW_DEDENT_in_messages1968 = frozenset([26])
    FOLLOW_NEWLINE_in_messages1970 = frozenset([1])
    FOLLOW_ID_in_messages_item2004 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_messages_item2006 = frozenset([1])
    FOLLOW_VARS_in_vars2033 = frozenset([19])
    FOLLOW_ID_in_vars2035 = frozenset([12, 19, 26])
    FOLLOW_attrs_hints_in_vars2037 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2076 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2078 = frozenset([1])
    FOLLOW_NEWLINE_in_attrs_hints2102 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2114 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2116 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2120 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2122 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2128 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2130 = frozenset([1])
    FOLLOW_attr_hint_in_attrs_hints2158 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2160 = frozenset([21])
    FOLLOW_INDENT_in_attrs_hints2172 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2174 = frozenset([12, 19])
    FOLLOW_attr_hint_in_attrs_hints2178 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2180 = frozenset([12, 13, 19])
    FOLLOW_DEDENT_in_attrs_hints2186 = frozenset([26])
    FOLLOW_NEWLINE_in_attrs_hints2188 = frozenset([1])
    FOLLOW_ID_in_attr_hint2225 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2266 = frozenset([19])
    FOLLOW_ID_in_attr_hint2268 = frozenset([1, 19])
    FOLLOW_hint_in_attr_hint2308 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2310 = frozenset([21])
    FOLLOW_INDENT_in_attr_hint2312 = frozenset([26])
    FOLLOW_NEWLINE_in_attr_hint2314 = frozenset([19])
    FOLLOW_ID_in_attr_hint2318 = frozenset([19, 26])
    FOLLOW_NEWLINE_in_attr_hint2322 = frozenset([13, 19])
    FOLLOW_DEDENT_in_attr_hint2328 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2375 = frozenset([19])
    FOLLOW_ID_in_hint2377 = frozenset([11])
    FOLLOW_CURLY_CLOSE_in_hint2379 = frozenset([1])
    FOLLOW_CURLY_OPEN_in_hint2399 = frozenset([19])
    FOLLOW_ID_in_hint2401 = frozenset([19, 74])
    FOLLOW_hint_arg_in_hint2403 = frozenset([11, 19, 74])
    FOLLOW_CURLY_CLOSE_in_hint2407 = frozenset([1])
    FOLLOW_MINUS_in_num_whole2446 = frozenset([27])
    FOLLOW_NUMBER_in_num_whole2450 = frozenset([1])
    FOLLOW_MINUS_in_num_fract2458 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2462 = frozenset([14])
    FOLLOW_DIVIDE_in_num_fract2464 = frozenset([27])
    FOLLOW_NUMBER_in_num_fract2466 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ShyRecognizerFrontendLexer", ShyRecognizerFrontend)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
