tree grammar Eval;

options {
    language=Python;
    tokenVocab=Expr;
    ASTLabelType=object;
}

@members {
memory = dict()
}

prog: stat+;

stat: expr {print $expr.value}
    | ^('=' ID expr) {self.memory[$ID.text] = int($expr.value)}
    ;

expr returns [int value]
    : ^('+' a=expr b=expr) {$value = a + b}
    | ^('-' a=expr b=expr) {$value = a - b}
    | ^('*' a=expr b=expr) {$value = a * b}
    | ID
      {
          if $ID.text in self.memory:
              $value = self.memory[$ID.text]
          else:
              print 'undefined variable', $ID.text
              $value = 0
      }
    | INT {$value = int($INT.text)}
    ;
