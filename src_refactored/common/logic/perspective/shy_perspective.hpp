namespace shy_guts
{
    namespace logic_perspective_planes_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_fract x_left ;
        static so_called_type_platform_math_num_fract x_right ;
        static so_called_type_platform_math_num_fract y_top ;
        static so_called_type_platform_math_num_fract y_bottom ;
        static so_called_type_platform_math_num_fract z_near ;
        static so_called_type_platform_math_num_fract z_far ;
        static so_called_type_platform_math_num_fract scene_scale ;
    }

    namespace engine_render_aspect_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract width ;
        static so_called_type_platform_math_num_fract height ;
    }

    static void proceed_with_planes ( ) ;
    static void request_aspect ( ) ;
    static void compute_x_left ( ) ;
    static void compute_x_right ( ) ;
    static void compute_y_top ( ) ;
    static void compute_y_bottom ( ) ;
    static void compute_z_near ( ) ;
    static void compute_z_far ( ) ;
    static void compute_scene_scale ( ) ;
    static void reply_computed_planes ( ) ;
    static void reply_planes ( ) ;
    static void scene_scale ( so_called_type_platform_math_num_fract & ) ;
    static void z_near ( so_called_type_platform_math_num_fract & ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_perspective > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_planes ( )
{
}

void shy_guts :: request_aspect ( )
{
}

void shy_guts :: compute_x_left ( )
{
}

void shy_guts :: compute_x_right ( )
{
}

void shy_guts :: compute_y_top ( )
{
}

void shy_guts :: compute_y_bottom ( )
{
}

void shy_guts :: compute_z_near ( )
{
}

void shy_guts :: compute_z_far ( )
{
}

void shy_guts :: compute_scene_scale ( )
{
}

void shy_guts :: reply_computed_planes ( )
{
}

void shy_guts :: reply_planes ( )
{
}

void shy_guts :: scene_scale ( so_called_type_platform_math_num_fract & )
{
}

void shy_guts :: z_near ( so_called_type_platform_math_num_fract & )
{
}

void _shy_common_logic_perspective :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_perspective :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_perspective :: receive ( so_called_message_common_logic_perspective_planes_request )
{
}
