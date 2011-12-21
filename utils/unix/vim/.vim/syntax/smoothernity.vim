" smoothernity syntax file

syntax keyword shy_statement system machine state consts on to is command if do input entry exit initial discard vars ops receive request module trace with else while args proc guts
syntax match shy_constant "\(\(^\| \)[\-]\? *\d\+\( *\/ *\d\+\)\?\)\|\<true\>\|\<false\>"
syntax match shy_special "[\{\}\(\)\*]\|<\-\|\->\|\<msg\|\<reply\|\<guts"
syntax match shy_string "\'.*\'"

highlight def link shy_statement Statement
highlight def link shy_constant Constant
highlight def link shy_special Special
highlight def link shy_string String
