namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_fract final_r = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static const so_called_type_platform_math_num_fract final_g = so_called_platform_math :: init_num_fract ( 1 , 10 ) ;
        static const so_called_type_platform_math_num_fract final_b = so_called_platform_math :: init_num_fract ( 4 , 10 ) ;
        static const so_called_type_platform_math_num_fract fog_far_shift = so_called_platform_math :: init_num_fract ( 20 , 1 ) ;
        static const so_called_type_platform_math_num_fract fog_near_shift = so_called_platform_math :: init_num_fract ( 10 , 1 ) ;
        static const so_called_type_platform_math_num_whole fade_in_frames = so_called_platform_math :: init_num_whole ( 90 ) ;
    }

    static void clear_screen ( ) ;
    static void update_color ( ) ;
    static void proceed_with_render ( ) ;

    static so_called_type_platform_math_num_fract color_r ;
    static so_called_type_platform_math_num_fract color_g ;
    static so_called_type_platform_math_num_fract color_b ;
    static so_called_type_platform_math_num_whole color_frames ;
    static so_called_type_platform_math_num_whole game_launched ;
    static so_called_type_platform_math_num_whole game_launch_permitted ;
    
    static so_called_type_platform_math_num_whole near_plane_distance_requested ;
    static so_called_type_platform_math_num_whole near_plane_distance_replied ;
    static so_called_type_platform_math_num_fract near_plane_distance ;
    
    static so_called_type_platform_math_num_whole camera_matrix_requested ;
    static so_called_type_platform_math_num_whole camera_matrix_replied ;
    static so_called_type_platform_matrix_data camera_matrix ;
    
    static so_called_type_platform_math_num_whole use_perspective_projection_requested ;
    static so_called_type_platform_math_num_whole use_perspective_projection_replied ;

    static so_called_type_platform_math_num_whole use_ortho_projection_requested ;
    static so_called_type_platform_math_num_whole use_ortho_projection_replied ;
    
    static so_called_type_platform_math_num_whole land_render_requested ;
    static so_called_type_platform_math_num_whole land_render_replied ;
    
    static so_called_type_platform_math_num_whole entities_render_requested ;
    static so_called_type_platform_math_num_whole entities_render_replied ;
    
    static so_called_type_platform_math_num_whole fidget_render_requested ;
    static so_called_type_platform_math_num_whole fidget_render_replied ;
    
    static so_called_type_platform_math_num_whole text_render_requested ;
    static so_called_type_platform_math_num_whole text_render_replied ;

    static so_called_type_platform_math_num_whole image_render_requested ;
    static so_called_type_platform_math_num_whole image_render_replied ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_game > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: clear_screen ( )
{
}

void shy_guts :: update_color ( )
{
}

void shy_guts :: proceed_with_render ( )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_camera_matrix_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_camera_prepared )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_core_near_plane_distance_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_core_use_ortho_projection_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_core_use_perspective_projection_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_entities_prepared )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_entities_render_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_fidget_render_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_game_launch_permit )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_game_render )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_game_update )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_image_prepared )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_image_render_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_land_prepared )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_land_render_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_sound_prepared )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_text_render_reply )
{
}

void _shy_common_logic_game :: receive ( so_called_message_common_logic_touch_prepared )
{
}
