namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_fract entity_color_roof_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract entity_color_roof_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract entity_color_roof_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract entity_mesh_height = so_called_platform_math :: init_num_fract ( 2 , 1 ) ;
        static const so_called_type_platform_math_num_fract scale_wave = so_called_platform_math :: init_num_fract ( 2 , 1 ) ;
        static const so_called_type_platform_math_num_whole entity_mesh_spans = so_called_platform_math :: init_num_whole ( 50 ) ;
        static const so_called_type_platform_math_num_whole scale_in_frames = so_called_platform_math :: init_num_whole ( 120 ) ;
        static const so_called_type_platform_math_num_whole grid_step = so_called_platform_math :: init_num_whole ( 5 ) ;
        static const so_called_type_platform_math_num_whole color_bias = so_called_platform_math :: init_num_whole ( 21 ) ;
        static const so_called_type_platform_math_num_whole colors_max = so_called_platform_math :: init_num_whole ( 7 ) ;
        static const so_called_type_platform_math_num_whole frames_wait_before_render = so_called_platform_math :: init_num_whole ( 1 ) ;
        static const so_called_type_platform_math_num_whole frames_between_render_count_increases = so_called_platform_math :: init_num_whole ( 10 ) ;
        static so_called_type_platform_math_const_int_32 entity_mesh_grid = 5 ;
    }
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_entities > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_entities :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_height_request )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_mesh_grid_request )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_origin_request )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_prepare_permit )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_render_request )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_update )
{
}
