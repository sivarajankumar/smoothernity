# $ANTLR 3.4 copypaster/Frontend.g 2012-01-16 18:05:34

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
CHARS=4
DEDENT=5
INDENT=6
NEWLINE=7
WHITESPACE=8

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "CHARS", "DEDENT", "INDENT", "NEWLINE", "WHITESPACE"
]




class FrontendParser(Parser):
    grammarFileName = "copypaster/Frontend.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(FrontendParser, self).__init__(input, state, *args, **kwargs)




        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class start_return(ParserRuleReturnScope):
        def __init__(self):
            super(FrontendParser.start_return, self).__init__()

            self.tree = None





    # $ANTLR start "start"
    # copypaster/Frontend.g:10:1: start : ( INDENT | DEDENT | NEWLINE | CHARS )* ;
    def start(self, ):
        retval = self.start_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set1 = None

        set1_tree = None

        try:
            try:
                # copypaster/Frontend.g:10:7: ( ( INDENT | DEDENT | NEWLINE | CHARS )* )
                # copypaster/Frontend.g:10:9: ( INDENT | DEDENT | NEWLINE | CHARS )*
                pass 
                root_0 = self._adaptor.nil()


                # copypaster/Frontend.g:10:9: ( INDENT | DEDENT | NEWLINE | CHARS )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((CHARS <= LA1_0 <= NEWLINE)) :
                        alt1 = 1


                    if alt1 == 1:
                        # copypaster/Frontend.g:
                        pass 
                        set1 = self.input.LT(1)

                        if (CHARS <= self.input.LA(1) <= NEWLINE):
                            self.input.consume()
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set1))

                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse




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



 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FrontendLexer", FrontendParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
