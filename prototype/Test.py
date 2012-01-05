from sys import argv, stdin, stdout, stderr
from antlr3 import ANTLRInputStream, CommonTokenStream
from antlr3.main import ParserMain
from antlr3.tree import CommonTreeNodeStream
from ExprParser import ExprParser
from ExprLexer import ExprLexer
from Eval import Eval

inStream = ANTLRInputStream(stdin)
exprLexer = ExprLexer(inStream)
tokenStream = CommonTokenStream(exprLexer)
exprParser = ExprParser(tokenStream)
r = exprParser.prog()
nodeStream = CommonTreeNodeStream(r.tree)
evalWalker = Eval(nodeStream)
evalWalker.prog()
