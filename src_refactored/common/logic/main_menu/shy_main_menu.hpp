namespace shy_guts
{
    static so_called_type_platform_math_num_whole creation_permitted ;
    static so_called_type_platform_math_num_whole launch_permitted ;
    static so_called_type_platform_math_num_whole created ;
    static so_called_type_platform_math_num_whole launched ;
    static so_called_type_platform_math_num_whole disappearing ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu :: receive ( so_called_message_common_init )
{
    shy_guts :: launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: creation_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: launched = so_called_platform_math_consts :: whole_false ;
    shy_guts :: created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: disappearing = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_creation_permit )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_launch_permit )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_letters_animation_disappear_finished )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_letters_create_finished )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_letters_meshes_creation_finished )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_letters_meshes_destroy_reply )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_row_chosen )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_selection_mesh_create_finished )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_selection_mesh_destroy_reply )
{
}

void _shy_common_logic_main_menu :: receive ( so_called_message_common_logic_main_menu_update )
{
}
