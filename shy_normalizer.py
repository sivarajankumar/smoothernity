import os

class consts :
    dot = "."
    injections_postfix = "_injections"
    message = "message"
    sender = "sender"
    type = "type"
    shy_prefix = "shy_"
    slash = "/"
    underscore = "_"

def move_to_tail ( s , what ) :
    if s . find ( what ) != - 1 :
        return s . replace ( consts . slash + what , str ( ) ) + consts . slash + what
    else :
        return s

def make_normalized_path ( old_file_path ) :
    old_file_dir , old_file_name = os . path . split ( old_file_path )
    new_file_dir = old_file_dir . replace ( consts . underscore , consts . slash )

    new_file_dir = move_to_tail ( new_file_dir , consts . message )
    new_file_dir = move_to_tail ( new_file_dir , consts . sender )
    new_file_dir = move_to_tail ( new_file_dir , consts . type )

    new_file_name = old_file_name
    if old_file_name . startswith ( consts . shy_prefix ) :
        old_name = old_file_name . split ( consts . dot ) [ 0 ]
        old_ext = old_file_name . split ( consts . dot ) [ 1 ]
        old_parts = old_name . split ( consts . underscore )
        if old_name . endswith ( consts . injections_postfix ) :
            meaning_part = old_parts [ - 2 ]
            injections_part = consts . injections_postfix
        else :
            meaning_part = old_parts [ - 1 ]
            injections_part = str ( )
        if old_file_dir . find ( consts . sender ) != - 1 :
            meaning_part = consts . sender
        if old_file_dir . find ( consts . message ) != - 1 :
            meaning_part = consts . message
        if old_file_dir . find ( consts . type ) != - 1 :
            meaning_part = consts . type
        new_file_name = consts . shy_prefix + meaning_part + injections_part + consts . dot + old_ext
        return os . path . join ( new_file_dir , new_file_name )
    else :
        return old_file_path

assert make_normalized_path ( "some_parent_dir/some_module/shy_some_module.h" ) == "some/parent/dir/some/module/shy_module.h"
assert make_normalized_path ( "some_parent_dir/some_module/shy_some_module_injections.cpp" ) == "some/parent/dir/some/module/shy_module_injections.cpp"
assert make_normalized_path ( "some_parent_dir/some_module/message/some_action/shy_some_action.h" ) == "some/parent/dir/some/module/some/action/message/shy_message.h"
assert make_normalized_path ( "some_parent_dir/some_module/message/some_action/shy_some_action_injections.h" ) == "some/parent/dir/some/module/some/action/message/shy_message_injections.h"
assert make_normalized_path ( "some_parent_dir/some_module/sender/some_action/shy_some_action.h" ) == "some/parent/dir/some/module/some/action/sender/shy_sender.h"
assert make_normalized_path ( "some_parent_dir/some_module/sender/some_action/shy_some_action_injections.h" ) == "some/parent/dir/some/module/some/action/sender/shy_sender_injections.h"
assert make_normalized_path ( "some_parent_dir/some_module/type/some_data/shy_some_data.h" ) == "some/parent/dir/some/module/some/data/type/shy_type.h"
assert make_normalized_path ( "some_parent_dir/some_module/type/some_data/shy_some_data_injections.h" ) == "some/parent/dir/some/module/some/data/type/shy_type_injections.h"
assert make_normalized_path ( "some_parent_dir/some_module/some_file.h" ) == "some_parent_dir/some_module/some_file.h"
assert make_normalized_path ( "some_parent_dir/shy_some_module/some_file.h" ) == "some_parent_dir/shy_some_module/some_file.h"
assert make_normalized_path ( "./shy_some_module.h" ) == "./shy_module.h"
assert make_normalized_path ( "./shy_some_module_injections.cpp" ) == "./shy_module_injections.cpp"

