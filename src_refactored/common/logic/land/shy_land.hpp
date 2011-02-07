namespace shy_guts
{
    namespace consts
    {
        static so_called_type_platform_math_num_whole create_rows_per_frame = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_type_platform_math_num_whole land_grid = so_called_platform_math :: init_num_whole ( 10 ) ;
        static so_called_type_platform_math_num_whole scale_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
        static so_called_type_platform_math_num_whole modulator_1 = so_called_platform_math :: init_num_whole ( 32 ) ;
        static so_called_type_platform_math_num_whole modulator_2 = so_called_platform_math :: init_num_whole ( 64 ) ;
        static so_called_type_platform_math_num_whole modulator_3 = so_called_platform_math :: init_num_whole ( 128 ) ;
        static so_called_type_platform_math_num_whole multiplier_1 = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_type_platform_math_num_whole multiplier_2 = so_called_platform_math :: init_num_whole ( 4 ) ;
        static so_called_type_platform_math_num_whole multiplier_3 = so_called_platform_math :: init_num_whole ( 2 ) ;
        static so_called_type_platform_math_num_fract color_scale = so_called_platform_math :: init_num_fract ( 255 , 1 ) ;
        static so_called_type_platform_math_num_fract land_radius = so_called_platform_math :: init_num_fract ( 10 , 1 ) ;
        static so_called_type_platform_math_num_fract land_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_type_platform_math_num_fract land_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_type_platform_math_num_fract land_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
    }
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_land > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_land :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_land :: receive ( so_called_message_common_engine_render_texture_create_reply )
{
}

void _shy_common_logic_land :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_prepare_permit )
{
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_render_request )
{
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_update )
{
}
