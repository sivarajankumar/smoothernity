tree grammar Eval;

options {
    language=Python;
    tokenVocab=Expr;
    ASTLabelType=object;
}

@members {
memory = dict()
}

prog returns [value]
    @init {$value = list()}
    : (stat {$value.append($stat.value)})+;

stat returns [value]: expr {$value = $expr.value}
    | ^('=' ID expr) 
        {
            self.memory[$ID.text] = int($expr.value)
            $value = None
        }
    ;

expr returns [value]
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
