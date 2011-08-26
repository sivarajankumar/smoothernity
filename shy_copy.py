import optparse
import os

class consts :
    cp = "cp"
    makedirs = "mkdir -p"
    usage_long = str \
        ( "%prog [options] dir-from dir-to\n"
        + "\n"
        + "Smoothernity source files copier.\n"
        + "\n"
        + "Example:\n"
        + "dir-from = old_parent_dir/old_module\n"
        + "dir-to = new_parent_dir/new_module\n"
        + "\n"
        + "Copies:\n"
        + "old_parent_dir/old_module/shy_old_module.h\n"
        + "old_parent_dir/old_module/shy_old_module.hpp\n"
        + "old_parent_dir/old_module/shy_old_module_injections.h\n"
        + "old_parent_dir/old_module/shy_old_module_injections.cpp\n"
        + "\n"
        + "To:\n"
        + "new_parent_dir/new_module/shy_new_module.h\n"
        + "new_parent_dir/new_module/shy_new_module.hpp\n"
        + "new_parent_dir/new_module/shy_new_module_injections.h\n"
        + "new_parent_dir/new_module/shy_new_module_injections.cpp\n"
        + "\n"
        + "Creates target path if necessary."
        )
    usage_short = "[--help] dir-from dir-to"

parser = optparse . OptionParser ( usage = consts . usage_long )
options , args = parser . parse_args ( )
if len ( args ) < 2 :
    print consts . usage_short
else :
    new_dir = args [ 1 ]
    new_name = os . path . basename ( new_dir )
    print consts . makedirs , new_dir
    for old_dir , old_dirs , old_files in os . walk ( args [ 0 ] ) :
        old_name = os . path . basename ( old_dir )
        for old_file in old_files :
            new_file = old_file . replace ( old_name , new_name )
            new_path = os . path . join ( new_dir , new_file ) 
            old_path = os . path . join ( old_dir , old_file )
            print consts . cp , old_path , new_path
