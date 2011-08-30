import optparse
import os

class consts :
    def msg_done ( self , file ) :
        return "File \"" + file + "\" done."
    mode_read = "r"
    mode_write = "w"
    prefix_shy = "shy_"
    prefix_so_called = "so_called_"
    prefix_underscored_shy = "_shy_"
    postfix_injections_included = "_injections_included"
    underscore = "_"
    usage_long = str \
        ( "%prog [options] dir-path prefix\n"
        + "\n"
        + "Smoothernity identifiers prefix to postfix notation renamer.\n"
        + "\n"
        + "For every file in subdirectories it replaces:\n"
        + prefix_so_called + "<prefix>_blablabla\n"
        + prefix_shy + "<prefix>_blablabla\n"
        + prefix_underscored_shy + "<prefix>_blablabla" + postfix_injections_included + "\n"
        + "\n"
        + "With:\n"
        + prefix_so_called + "blablabla_<prefix>\n"
        + prefix_shy + "blablabla_<prefix>\n"
        + prefix_underscored_shy + "blablabla_<prefix>" + postfix_injections_included
        )
    usage_short = "[--help] dir-from dir-to"

def check_replace ( replace_list , word , prefix , postfix , arg_prefix ) :
    if word . startswith ( prefix + arg_prefix + consts . underscore ) and word . endswith ( postfix ) :
        new_word = word
        new_word = new_word . replace ( prefix + arg_prefix + consts . underscore , prefix )
        new_word = new_word . replace ( postfix , str ( ) )
        new_word = new_word + consts . underscore + arg_prefix
        new_word = new_word + postfix
        replace_list [ word ] = new_word

parser = optparse . OptionParser ( usage = consts . usage_long )
options , args = parser . parse_args ( )
if len ( args ) < 2 :
    print consts . usage_short
else :
    arg_dir_path = args [ 0 ]
    arg_prefix = args [ 1 ]
    for dir , dirs , files in os . walk ( arg_dir_path ) :
        for file in files :
            file_path = os . path . join ( dir , file )
            old_lines = open ( file_path , consts . mode_read ) . readlines ( ) 
            new_lines = [ ]
            changed = False
            for line in old_lines :
                replace_list = { }
                for word in line . split ( ) :
                    check_replace ( replace_list , word , consts . prefix_shy , str ( ) , arg_prefix )
                    check_replace ( replace_list , word , consts . prefix_so_called , str ( ) , arg_prefix )
                    check_replace ( replace_list , word , consts . prefix_underscored_shy , consts . postfix_injections_included , arg_prefix )
                for what , to_what in replace_list . items ( ) :
                    line = line . replace ( what , to_what )
                    changed = True
                new_lines += line
            if changed :
                open ( file_path , consts . mode_write ) . writelines ( new_lines )
                print consts ( ) . msg_done ( file_path )
