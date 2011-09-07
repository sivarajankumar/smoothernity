" smoothernity syntax file

syntax keyword shy_statement system machine state consts on to is command if do input entry exit initial discard
syntax match shy_constant "\(^\| \)[\-]\? *\d\+\( *\/ *\d\+\)\?"
syntax match shy_special "[\{\}\(\)]"

highlight def link shy_statement Statement
highlight def link shy_constant Constant
highlight def link shy_special Special

