import optparse
import os

class consts :
    def msg_done ( self , file ) :
        return "File \"" + file + "\" done."
    dot = "."
    include = "#include "
    local_prefix = "./shy_"
    mode_read = "r"
    mode_write = "w"
    quote = "\""
    usage_long = str \
        ( "%prog [options] dir-path\n"
        + "\n"
        + "Smoothernity #include relative to absolute path replacer.\n"
        + "\n"
        + "For every file in subdirectories it replaces:\n"
        + "#include \"<path-relative-to-file-directory>/shy_blablabla.*\"\n"
        + "\n"
        + "With:\n"
        + "#include \"<path-relative-to-current-directory>/shy_blablabla.*\""
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
            old_lines = open ( file_path , consts . mode_read ) . readlines ( ) 
            new_lines = [ ]
            changed = False
            for line in old_lines :
                replace_list = { }
                if line . strip ( ) . startswith ( consts . include ) :
                    include_path = line . strip ( ) . split ( consts . include ) [ 1 ] . split ( consts . quote ) [ 1 ]
                    if include_path . startswith ( consts . dot ) :
                        if not include_path . startswith ( consts . local_prefix ) :
                            new_path = os . path . normpath ( os . path . join ( dir , include_path ) )
                            replace_list [ include_path ] = new_path
                for what , to_what in replace_list . items ( ) :
                    line = line . replace ( what , to_what )
                    changed = True
                new_lines += line
            if changed :
                open ( file_path , consts . mode_write ) . writelines ( new_lines )
                print consts ( ) . msg_done ( file_path )
