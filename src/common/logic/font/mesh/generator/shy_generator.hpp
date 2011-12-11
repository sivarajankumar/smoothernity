namespace shy_guts
{
    static so_called_platform_math_num_fract_type time ;
    static so_called_platform_math_num_whole_type letter ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_font_mesh_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_font_mesh_generator :: receive ( so_called_common_init_message )
{
}

void _shy_common_logic_font_mesh_generator :: receive ( so_called_common_logic_font_mesh_generator_generate_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: letter = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_font_mesh_generator :: receive ( so_called_common_logic_font_mesh_generator_update_message )
{
    so_called_platform_math_num_whole_type max_letters ;
    so_called_platform_math_num_fract_type step ;
    step = so_called_common_logic_font_mesh_consts :: time_between_letters_creation ;
    max_letters = so_called_common_logic_font_consts :: max_letters_whole ;
    so_called_common_engine_math_stateless :: add_frame_to_time ( shy_guts :: time ) ;
    while ( so_called_platform_conditions :: fract_greater_than_fract ( shy_guts :: time , step ) )
    {
        so_called_platform_math :: sub_from_fract ( shy_guts :: time , step ) ;
        so_called_platform_math :: inc_whole ( shy_guts :: letter ) ;
        if ( so_called_platform_conditions :: wholes_are_equal ( shy_guts :: letter , max_letters ) )
            so_called_common_logic_font_mesh_generator_generate_finished_sender :: send ( so_called_common_logic_font_mesh_generator_generate_finished_message ( ) ) ;
    }
}

void _shy_common_logic_font_mesh_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
