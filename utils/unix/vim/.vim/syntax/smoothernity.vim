" smoothernity syntax file

syntax keyword shy_statement system machine state consts on to is command if do input entry exit initial discard vars ops receive request module trace with else while args proc init done copy paste replace module_name types reply messages stateless elif module_queue any all send indent dedent
syntax match shy_constant "\(\(^\| \)[\-]\? *\d\+\( *\/ *\d\+\)\?\)\|\<true\>\|\<false\>"
syntax match shy_special "[\{\}\(\)\*]\|<\-\|\->\|\<msg\|\<reply\|\<guts\|\<platform\|trace\|consts\|stateless\|\[[^\]]*\]\|\s_\s"
syntax match shy_string "'[^']*'"

highlight def link shy_statement Statement
highlight def link shy_constant Constant
highlight def link shy_special Special
highlight def link shy_string String
