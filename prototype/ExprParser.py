# $ANTLR 3.4 Expr.g 2012-01-05 19:31:34

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__8=8
T__9=9
T__10=10
T__11=11
T__12=12
T__13=13
ID=4
INT=5
NEWLINE=6
WS=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ID", "INT", "NEWLINE", "WS", "'('", "')'", "'*'", "'+'", "'-'", "'='"
]




class ExprParser(Parser):
    grammarFileName = "Expr.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(ExprParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprParser.prog_return, self).__init__()

            self.tree = None





    # $ANTLR start "prog"
    # Expr.g:10:1: prog : ( stat )+ ;
    def prog(self, ):
        retval = self.prog_return()
        retval.start = self.input.LT(1)


        root_0 = None

        stat1 = None



        try:
            try:
                # Expr.g:10:6: ( ( stat )+ )
                # Expr.g:10:8: ( stat )+
                pass 
                root_0 = self._adaptor.nil()


                # Expr.g:10:8: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((ID <= LA1_0 <= NEWLINE) or LA1_0 == 8) :
                        alt1 = 1


                    if alt1 == 1:
                        # Expr.g:10:8: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog52)
                        stat1 = self.stat()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, stat1.tree)



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "prog"


    class stat_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprParser.stat_return, self).__init__()

            self.tree = None





    # $ANTLR start "stat"
    # Expr.g:12:1: stat : ( expr NEWLINE -> expr | ID '=' expr NEWLINE -> ^( '=' ID expr ) | NEWLINE ->);
    def stat(self, ):
        retval = self.stat_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE3 = None
        ID4 = None
        char_literal5 = None
        NEWLINE7 = None
        NEWLINE8 = None
        expr2 = None

        expr6 = None


        NEWLINE3_tree = None
        ID4_tree = None
        char_literal5_tree = None
        NEWLINE7_tree = None
        NEWLINE8_tree = None
        stream_NEWLINE = RewriteRuleTokenStream(self._adaptor, "token NEWLINE")
        stream_ID = RewriteRuleTokenStream(self._adaptor, "token ID")
        stream_13 = RewriteRuleTokenStream(self._adaptor, "token 13")
        stream_expr = RewriteRuleSubtreeStream(self._adaptor, "rule expr")
        try:
            try:
                # Expr.g:12:6: ( expr NEWLINE -> expr | ID '=' expr NEWLINE -> ^( '=' ID expr ) | NEWLINE ->)
                alt2 = 3
                LA2 = self.input.LA(1)
                if LA2 == INT or LA2 == 8:
                    alt2 = 1
                elif LA2 == ID:
                    LA2_2 = self.input.LA(2)

                    if (LA2_2 == 13) :
                        alt2 = 2
                    elif (LA2_2 == NEWLINE or (10 <= LA2_2 <= 12)) :
                        alt2 = 1
                    else:
                        nvae = NoViableAltException("", 2, 2, self.input)

                        raise nvae


                elif LA2 == NEWLINE:
                    alt2 = 3
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # Expr.g:12:8: expr NEWLINE
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_stat63)
                    expr2 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr2.tree)


                    NEWLINE3 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat65) 
                    stream_NEWLINE.add(NEWLINE3)


                    # AST Rewrite
                    # elements: expr
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 12:29: -> expr
                    self._adaptor.addChild(root_0, stream_expr.nextTree())




                    retval.tree = root_0




                elif alt2 == 2:
                    # Expr.g:13:8: ID '=' expr NEWLINE
                    pass 
                    ID4 = self.match(self.input, ID, self.FOLLOW_ID_in_stat86) 
                    stream_ID.add(ID4)


                    char_literal5 = self.match(self.input, 13, self.FOLLOW_13_in_stat88) 
                    stream_13.add(char_literal5)


                    self._state.following.append(self.FOLLOW_expr_in_stat90)
                    expr6 = self.expr()

                    self._state.following.pop()
                    stream_expr.add(expr6.tree)


                    NEWLINE7 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat92) 
                    stream_NEWLINE.add(NEWLINE7)


                    # AST Rewrite
                    # elements: expr, 13, ID
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 13:29: -> ^( '=' ID expr )
                    # Expr.g:13:32: ^( '=' ID expr )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    stream_13.nextNode()
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_ID.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_expr.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0




                elif alt2 == 3:
                    # Expr.g:14:8: NEWLINE
                    pass 
                    NEWLINE8 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_stat114) 
                    stream_NEWLINE.add(NEWLINE8)


                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 14:29: ->
                    root_0 = None



                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "stat"


    class expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprParser.expr_return, self).__init__()

            self.tree = None





    # $ANTLR start "expr"
    # Expr.g:17:1: expr : multExpr ( ( '+' ^| '-' ^) multExpr )* ;
    def expr(self, ):
        retval = self.expr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal10 = None
        char_literal11 = None
        multExpr9 = None

        multExpr12 = None


        char_literal10_tree = None
        char_literal11_tree = None

        try:
            try:
                # Expr.g:17:6: ( multExpr ( ( '+' ^| '-' ^) multExpr )* )
                # Expr.g:17:8: multExpr ( ( '+' ^| '-' ^) multExpr )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_multExpr_in_expr143)
                multExpr9 = self.multExpr()

                self._state.following.pop()
                self._adaptor.addChild(root_0, multExpr9.tree)


                # Expr.g:17:17: ( ( '+' ^| '-' ^) multExpr )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((11 <= LA4_0 <= 12)) :
                        alt4 = 1


                    if alt4 == 1:
                        # Expr.g:17:19: ( '+' ^| '-' ^) multExpr
                        pass 
                        # Expr.g:17:19: ( '+' ^| '-' ^)
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == 11) :
                            alt3 = 1
                        elif (LA3_0 == 12) :
                            alt3 = 2
                        else:
                            nvae = NoViableAltException("", 3, 0, self.input)

                            raise nvae


                        if alt3 == 1:
                            # Expr.g:17:21: '+' ^
                            pass 
                            char_literal10 = self.match(self.input, 11, self.FOLLOW_11_in_expr149)
                            char_literal10_tree = self._adaptor.createWithPayload(char_literal10)
                            root_0 = self._adaptor.becomeRoot(char_literal10_tree, root_0)




                        elif alt3 == 2:
                            # Expr.g:17:29: '-' ^
                            pass 
                            char_literal11 = self.match(self.input, 12, self.FOLLOW_12_in_expr155)
                            char_literal11_tree = self._adaptor.createWithPayload(char_literal11)
                            root_0 = self._adaptor.becomeRoot(char_literal11_tree, root_0)






                        self._state.following.append(self.FOLLOW_multExpr_in_expr161)
                        multExpr12 = self.multExpr()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, multExpr12.tree)



                    else:
                        break #loop4




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "expr"


    class multExpr_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprParser.multExpr_return, self).__init__()

            self.tree = None





    # $ANTLR start "multExpr"
    # Expr.g:20:1: multExpr : atom ( '*' ^ atom )* ;
    def multExpr(self, ):
        retval = self.multExpr_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal14 = None
        atom13 = None

        atom15 = None


        char_literal14_tree = None

        try:
            try:
                # Expr.g:20:10: ( atom ( '*' ^ atom )* )
                # Expr.g:20:12: atom ( '*' ^ atom )*
                pass 
                root_0 = self._adaptor.nil()


                self._state.following.append(self.FOLLOW_atom_in_multExpr179)
                atom13 = self.atom()

                self._state.following.pop()
                self._adaptor.addChild(root_0, atom13.tree)


                # Expr.g:20:17: ( '*' ^ atom )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 == 10) :
                        alt5 = 1


                    if alt5 == 1:
                        # Expr.g:20:19: '*' ^ atom
                        pass 
                        char_literal14 = self.match(self.input, 10, self.FOLLOW_10_in_multExpr183)
                        char_literal14_tree = self._adaptor.createWithPayload(char_literal14)
                        root_0 = self._adaptor.becomeRoot(char_literal14_tree, root_0)



                        self._state.following.append(self.FOLLOW_atom_in_multExpr187)
                        atom15 = self.atom()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, atom15.tree)



                    else:
                        break #loop5




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "multExpr"


    class atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(ExprParser.atom_return, self).__init__()

            self.tree = None





    # $ANTLR start "atom"
    # Expr.g:23:1: atom : ( INT | ID | '(' ! expr ')' !);
    def atom(self, ):
        retval = self.atom_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INT16 = None
        ID17 = None
        char_literal18 = None
        char_literal20 = None
        expr19 = None


        INT16_tree = None
        ID17_tree = None
        char_literal18_tree = None
        char_literal20_tree = None

        try:
            try:
                # Expr.g:23:6: ( INT | ID | '(' ! expr ')' !)
                alt6 = 3
                LA6 = self.input.LA(1)
                if LA6 == INT:
                    alt6 = 1
                elif LA6 == ID:
                    alt6 = 2
                elif LA6 == 8:
                    alt6 = 3
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae


                if alt6 == 1:
                    # Expr.g:23:8: INT
                    pass 
                    root_0 = self._adaptor.nil()


                    INT16 = self.match(self.input, INT, self.FOLLOW_INT_in_atom209)
                    INT16_tree = self._adaptor.createWithPayload(INT16)
                    self._adaptor.addChild(root_0, INT16_tree)




                elif alt6 == 2:
                    # Expr.g:24:8: ID
                    pass 
                    root_0 = self._adaptor.nil()


                    ID17 = self.match(self.input, ID, self.FOLLOW_ID_in_atom218)
                    ID17_tree = self._adaptor.createWithPayload(ID17)
                    self._adaptor.addChild(root_0, ID17_tree)




                elif alt6 == 3:
                    # Expr.g:25:8: '(' ! expr ')' !
                    pass 
                    root_0 = self._adaptor.nil()


                    char_literal18 = self.match(self.input, 8, self.FOLLOW_8_in_atom228)

                    self._state.following.append(self.FOLLOW_expr_in_atom232)
                    expr19 = self.expr()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, expr19.tree)


                    char_literal20 = self.match(self.input, 9, self.FOLLOW_9_in_atom234)


                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "atom"



 

    FOLLOW_stat_in_prog52 = frozenset([1, 4, 5, 6, 8])
    FOLLOW_expr_in_stat63 = frozenset([6])
    FOLLOW_NEWLINE_in_stat65 = frozenset([1])
    FOLLOW_ID_in_stat86 = frozenset([13])
    FOLLOW_13_in_stat88 = frozenset([4, 5, 8])
    FOLLOW_expr_in_stat90 = frozenset([6])
    FOLLOW_NEWLINE_in_stat92 = frozenset([1])
    FOLLOW_NEWLINE_in_stat114 = frozenset([1])
    FOLLOW_multExpr_in_expr143 = frozenset([1, 11, 12])
    FOLLOW_11_in_expr149 = frozenset([4, 5, 8])
    FOLLOW_12_in_expr155 = frozenset([4, 5, 8])
    FOLLOW_multExpr_in_expr161 = frozenset([1, 11, 12])
    FOLLOW_atom_in_multExpr179 = frozenset([1, 10])
    FOLLOW_10_in_multExpr183 = frozenset([4, 5, 8])
    FOLLOW_atom_in_multExpr187 = frozenset([1, 10])
    FOLLOW_INT_in_atom209 = frozenset([1])
    FOLLOW_ID_in_atom218 = frozenset([1])
    FOLLOW_8_in_atom228 = frozenset([4, 5, 8])
    FOLLOW_expr_in_atom232 = frozenset([9])
    FOLLOW_9_in_atom234 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ExprLexer", ExprParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
