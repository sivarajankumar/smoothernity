# $ANTLR 3.4 Eval.g 2012-01-05 18:10:23

import sys
from antlr3 import *
from antlr3.tree import *

from antlr3.compat import set, frozenset



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




class Eval(TreeParser):
    grammarFileName = "Eval.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(Eval, self).__init__(input, state, *args, **kwargs)




        self.delegates = []




             
    memory = dict()



    # $ANTLR start "prog"
    # Eval.g:13:1: prog returns [value] : ( stat )+ ;
    def prog(self, ):
        value = None


        stat1 = None


        value = list()
        try:
            try:
                # Eval.g:15:5: ( ( stat )+ )
                # Eval.g:15:7: ( stat )+
                pass 
                # Eval.g:15:7: ( stat )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((ID <= LA1_0 <= INT) or (10 <= LA1_0 <= 13)) :
                        alt1 = 1


                    if alt1 == 1:
                        # Eval.g:15:8: stat
                        pass 
                        self._state.following.append(self.FOLLOW_stat_in_prog68)
                        stat1 = self.stat()

                        self._state.following.pop()

                        #action start
                        value.append(stat1)
                        #action end



                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "prog"



    # $ANTLR start "stat"
    # Eval.g:17:1: stat returns [value] : ( expr | ^( '=' ID expr ) );
    def stat(self, ):
        value = None


        ID3 = None
        expr2 = None

        expr4 = None


        try:
            try:
                # Eval.g:17:21: ( expr | ^( '=' ID expr ) )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((ID <= LA2_0 <= INT) or (10 <= LA2_0 <= 12)) :
                    alt2 = 1
                elif (LA2_0 == 13) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # Eval.g:17:23: expr
                    pass 
                    self._state.following.append(self.FOLLOW_expr_in_stat83)
                    expr2 = self.expr()

                    self._state.following.pop()

                    #action start
                    value = expr2
                    #action end



                elif alt2 == 2:
                    # Eval.g:18:7: ^( '=' ID expr )
                    pass 
                    self.match(self.input, 13, self.FOLLOW_13_in_stat94)

                    self.match(self.input, DOWN, None)
                    ID3 = self.match(self.input, ID, self.FOLLOW_ID_in_stat96)

                    self._state.following.append(self.FOLLOW_expr_in_stat98)
                    expr4 = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                            
                    self.memory[ID3.text] = int(expr4)
                    value = None
                            
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "stat"



    # $ANTLR start "expr"
    # Eval.g:25:1: expr returns [value] : ( ^( '+' a= expr b= expr ) | ^( '-' a= expr b= expr ) | ^( '*' a= expr b= expr ) | ID | INT );
    def expr(self, ):
        value = None


        ID5 = None
        INT6 = None
        a = None

        b = None


        try:
            try:
                # Eval.g:26:5: ( ^( '+' a= expr b= expr ) | ^( '-' a= expr b= expr ) | ^( '*' a= expr b= expr ) | ID | INT )
                alt3 = 5
                LA3 = self.input.LA(1)
                if LA3 == 11:
                    alt3 = 1
                elif LA3 == 12:
                    alt3 = 2
                elif LA3 == 10:
                    alt3 = 3
                elif LA3 == ID:
                    alt3 = 4
                elif LA3 == INT:
                    alt3 = 5
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # Eval.g:26:7: ^( '+' a= expr b= expr )
                    pass 
                    self.match(self.input, 11, self.FOLLOW_11_in_expr132)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr136)
                    a = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr140)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = a + b
                    #action end



                elif alt3 == 2:
                    # Eval.g:27:7: ^( '-' a= expr b= expr )
                    pass 
                    self.match(self.input, 12, self.FOLLOW_12_in_expr152)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr156)
                    a = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr160)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = a - b
                    #action end



                elif alt3 == 3:
                    # Eval.g:28:7: ^( '*' a= expr b= expr )
                    pass 
                    self.match(self.input, 10, self.FOLLOW_10_in_expr172)

                    self.match(self.input, DOWN, None)
                    self._state.following.append(self.FOLLOW_expr_in_expr176)
                    a = self.expr()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_expr_in_expr180)
                    b = self.expr()

                    self._state.following.pop()

                    self.match(self.input, UP, None)


                    #action start
                    value = a * b
                    #action end



                elif alt3 == 4:
                    # Eval.g:29:7: ID
                    pass 
                    ID5 = self.match(self.input, ID, self.FOLLOW_ID_in_expr191)

                    #action start
                          
                    if ID5.text in self.memory:
                        value = self.memory[ID5.text]
                    else:
                        print 'undefined variable', ID5.text
                        value = 0
                          
                    #action end



                elif alt3 == 5:
                    # Eval.g:37:7: INT
                    pass 
                    INT6 = self.match(self.input, INT, self.FOLLOW_INT_in_expr207)

                    #action start
                    value = int(INT6.text)
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "expr"



 

    FOLLOW_stat_in_prog68 = frozenset([1, 4, 5, 10, 11, 12, 13])
    FOLLOW_expr_in_stat83 = frozenset([1])
    FOLLOW_13_in_stat94 = frozenset([2])
    FOLLOW_ID_in_stat96 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_stat98 = frozenset([3])
    FOLLOW_11_in_expr132 = frozenset([2])
    FOLLOW_expr_in_expr136 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_expr140 = frozenset([3])
    FOLLOW_12_in_expr152 = frozenset([2])
    FOLLOW_expr_in_expr156 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_expr160 = frozenset([3])
    FOLLOW_10_in_expr172 = frozenset([2])
    FOLLOW_expr_in_expr176 = frozenset([4, 5, 10, 11, 12])
    FOLLOW_expr_in_expr180 = frozenset([3])
    FOLLOW_ID_in_expr191 = frozenset([1])
    FOLLOW_INT_in_expr207 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import WalkerMain
    main = WalkerMain(Eval)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
