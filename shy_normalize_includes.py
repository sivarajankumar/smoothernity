import optparse
import os
from shy_normalizer import make_normalized_path

class consts :
    def msg_done ( self , file ) :
        return "File \"" + file + "\" done."
    dot = "."
    exclude_dir = "some exclude directory"
    include = "#include "
    mode_read = "r"
    mode_write = "w"
    quote = "\""
    usage_long = str \
        ( "%prog [options] dir-path\n"
        + "\n"
        + "Smoothernity #include paths normalizer.\n"
        + "\n"
        + "For every file in subdirectories it replaces:\n"
        + "#include \"some_parent_dir/some_module/shy_some_module.h\"\n"
        + "#include \"some_parent_dir/some_module/shy_some_module_injections.h\"\n"
        + "\n"
        + "With:\n"
        + "#include \"some/parent/dir/some/module/shy_module.h\"\n"
        + "#include \"some/parent/dir/some/module/shy_module_injections.h\""
        )
    usage_short = "[--help] dir-path"

parser = optparse . OptionParser ( usage = consts . usage_long )
options , args = parser . parse_args ( )
if len ( args ) < 1 :
    print consts . usage_short
else :
    arg_dir_path = args [ 0 ]
    for dir , dirs , files in os . walk ( arg_dir_path ) :
        for file in files :
            file_path = os . path . join ( dir , file )
            if len ( file_path . split ( consts . exclude_dir ) ) == 1 :
                old_lines = open ( file_path , consts . mode_read ) . readlines ( ) 
                new_lines = [ ]
                changed = False
                for line in old_lines :
                    replace_list = { }
                    if line . strip ( ) . startswith ( consts . include ) :
                        include_path = line . strip ( ) . split ( consts . include ) [ 1 ]
                        if include_path . startswith ( consts . quote ) :
                            include_path = include_path . split ( consts . quote ) [ 1 ]
                            replace_list [ include_path ] = make_normalized_path ( file , include_path )
                    for what , to_what in replace_list . items ( ) :
                        line = line . replace ( what , to_what )
                        changed = True
                    new_lines += line
                if changed :
                    open ( file_path , consts . mode_write ) . writelines ( new_lines )
                    print consts ( ) . msg_done ( file_path )
