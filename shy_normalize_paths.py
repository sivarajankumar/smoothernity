import optparse
import os
from shy_normalizer import make_normalized_path

class consts :
    cp = "cp"
    hg_remove = "hg remove"
    makedirs = "mkdir -p"
    usage_long = str \
        ( "%prog [options] path\n"
        + "\n"
        + "Smoothernity source files paths normalizer.\n"
        + "\n"
        + "Before:\n"
        + "some_parent_dir/some_module/shy_some_module.h\n"
        + "some_parent_dir/some_module/shy_some_module.hpp\n"
        + "some_parent_dir/some_module/shy_some_module_injections.h\n"
        + "some_parent_dir/some_module/shy_some_module_injections.cpp\n"
        + "\n"
        + "After:\n"
        + "some/parent/dir/some/module/shy_module.h\n"
        + "some/parent/dir/some/module/shy_module.hpp\n"
        + "some/parent/dir/some/module/shy_module_injections.h\n"
        + "some/parent/dir/some/module/shy_module_injections.cpp"
        )
    usage_short = "[--help] path"

parser = optparse . OptionParser ( usage = consts . usage_long )
options , args = parser . parse_args ( )
if len ( args ) < 1 :
    print consts . usage_short
else :
    arg_path = args [ 0 ]
    make_dirs = set ( )
    rm_dirs = set ( )
    copy_files = { }
    for old_dir , old_dirs , old_files in os . walk ( arg_path ) :
        for old_file in old_files :
            old_path = os . path . join ( old_dir , old_file )
            new_path = make_normalized_path ( str ( ) , old_path )
            if new_path != old_path :
                new_dir , new_file = os . path . split ( new_path )
                make_dirs . add ( new_dir )
                rm_dirs . add ( old_dir )
                copy_files [ old_path ] = new_path

    for dir in make_dirs :
        print consts . makedirs , dir
    for file_from , file_to in copy_files . items ( ) :
        print consts . cp , file_from , file_to
    for dir in rm_dirs :
        print consts . hg_remove , dir
