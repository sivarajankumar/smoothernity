namespace shy_guts
{
    static so_called_type_platform_math_num_whole creation_in_progress ;
    static so_called_type_platform_math_num_fract time_passed ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creation_director > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_message_common_init )
{
    shy_guts :: creation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: time_passed = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_message_common_logic_main_menu_letters_meshes_create )
{
    shy_guts :: creation_in_progress = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_message_common_logic_main_menu_letters_meshes_creation_finished )
{
    shy_guts :: creation_in_progress = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_message_common_logic_main_menu_update )
{
}
