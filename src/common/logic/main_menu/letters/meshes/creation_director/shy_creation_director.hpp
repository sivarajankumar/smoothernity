namespace shy_guts
{
    static so_called_platform_math_num_whole_type creation_in_progress ;
    static so_called_platform_math_num_fract_type time_passed ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creation_director > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_common_init_message )
{
    shy_guts :: creation_in_progress = so_called_platform_math_consts :: whole_false ;
    shy_guts :: time_passed = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_common_logic_main_menu_letters_meshes_create_message )
{
    shy_guts :: creation_in_progress = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_common_logic_main_menu_letters_meshes_creation_finished_message )
{
    shy_guts :: creation_in_progress = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_letters_meshes_creation_director :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: creation_in_progress ) )
    {
        so_called_platform_math_num_fract_type frame_time ;
        so_called_platform_math_num_fract_type time_between_creation ;

        time_between_creation = so_called_common_logic_main_menu_letters_meshes_consts :: time_between_creation ;

        so_called_platform_math :: make_num_fract ( frame_time , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( shy_guts :: time_passed , frame_time ) ;

        while ( so_called_platform_conditions :: fract_greater_than_fract ( shy_guts :: time_passed , time_between_creation ) )
        {
            so_called_platform_math :: sub_from_fract ( shy_guts :: time_passed , time_between_creation ) ;
            so_called_common_logic_main_menu_letters_meshes_mesh_create_next_sender :: send ( so_called_common_logic_main_menu_letters_meshes_mesh_create_next_message ( ) ) ;
            if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: creation_in_progress ) )
                break ;
        }
    }
}

void _shy_common_logic_main_menu_letters_meshes_creation_director :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
