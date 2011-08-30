namespace shy_guts
{
    namespace logic_perspective_planes_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_fract_type x_left ;
        static so_called_platform_math_num_fract_type x_right ;
        static so_called_platform_math_num_fract_type y_top ;
        static so_called_platform_math_num_fract_type y_bottom ;
        static so_called_platform_math_num_fract_type z_near ;
        static so_called_platform_math_num_fract_type z_far ;
        static so_called_platform_math_num_fract_type scene_scale ;
    }

    namespace engine_render_aspect_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type width ;
        static so_called_platform_math_num_fract_type height ;
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
    static void scene_scale ( so_called_platform_math_num_fract_type & ) ;
    static void z_near ( so_called_platform_math_num_fract_type & ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_perspective > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_planes ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_perspective_planes_state :: requested ) )
    {
        shy_guts :: logic_perspective_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_aspect ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: replied ) )
    {
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_computed_planes ( ) ;
    }
}

void shy_guts :: request_aspect ( )
{
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_render_aspect_request_sender :: send ( so_called_common_engine_render_aspect_request_message ( ) ) ;
}

void shy_guts :: compute_x_left ( )
{
    so_called_platform_math_num_fract_type x_left ;
    so_called_platform_math_num_fract_type aspect_width ;

    aspect_width = shy_guts :: engine_render_aspect_state :: width ;
    so_called_platform_math :: mul_fracts ( x_left , aspect_width , so_called_platform_math_consts :: fract_minus_1 ) ;

    shy_guts :: logic_perspective_planes_state :: x_left = x_left ;
}

void shy_guts :: compute_x_right ( )
{
    so_called_platform_math_num_fract_type x_right ;
    so_called_platform_math_num_fract_type aspect_width ;

    aspect_width = shy_guts :: engine_render_aspect_state :: width ;
    x_right = aspect_width ;

    shy_guts :: logic_perspective_planes_state :: x_right = x_right ;
}

void shy_guts :: compute_y_top ( )
{
    so_called_platform_math_num_fract_type y_top ;
    so_called_platform_math_num_fract_type aspect_height ;

    aspect_height = shy_guts :: engine_render_aspect_state :: height ;
    y_top = aspect_height ;

    shy_guts :: logic_perspective_planes_state :: y_top = y_top ;
}

void shy_guts :: compute_y_bottom ( )
{
    so_called_platform_math_num_fract_type y_bottom ;
    so_called_platform_math_num_fract_type aspect_height ;

    aspect_height = shy_guts :: engine_render_aspect_state :: height ;
    so_called_platform_math :: mul_fracts ( y_bottom , aspect_height , so_called_platform_math_consts :: fract_minus_1 ) ;

    shy_guts :: logic_perspective_planes_state :: y_bottom = y_bottom ;
}

void shy_guts :: compute_z_near ( )
{
    so_called_platform_math_num_fract_type z_near ;
    shy_guts :: z_near ( z_near ) ;
    shy_guts :: logic_perspective_planes_state :: z_near = z_near ;
}

void shy_guts :: compute_z_far ( )
{
    so_called_platform_math_num_fract_type scene_scale ;
    so_called_platform_math_num_fract_type z_far_unscaled ;
    so_called_platform_math_num_fract_type z_far ;

    z_far_unscaled = so_called_common_logic_perspective_consts :: z_far_unscaled ;
    shy_guts :: scene_scale ( scene_scale ) ;
    so_called_platform_math :: mul_fracts ( z_far , z_far_unscaled , scene_scale ) ;

    shy_guts :: logic_perspective_planes_state :: z_far = z_far ;
}

void shy_guts :: compute_scene_scale ( )
{
    so_called_platform_math_num_fract_type scene_scale ;
    shy_guts :: scene_scale ( scene_scale ) ;
    shy_guts :: logic_perspective_planes_state :: scene_scale = scene_scale ;
}

void shy_guts :: reply_computed_planes ( )
{
    shy_guts :: compute_x_left ( ) ;
    shy_guts :: compute_x_right ( ) ;
    shy_guts :: compute_y_top ( ) ;
    shy_guts :: compute_y_bottom ( ) ;
    shy_guts :: compute_z_near ( ) ;
    shy_guts :: compute_z_far ( ) ;
    shy_guts :: compute_scene_scale ( ) ;
    shy_guts :: reply_planes ( ) ;
}

void shy_guts :: reply_planes ( )
{
    so_called_common_logic_perspective_planes_reply_message msg ;
    msg . x_left = shy_guts :: logic_perspective_planes_state :: x_left ;
    msg . x_right = shy_guts :: logic_perspective_planes_state :: x_right ;
    msg . y_top = shy_guts :: logic_perspective_planes_state :: y_top ;
    msg . y_bottom = shy_guts :: logic_perspective_planes_state :: y_bottom ;
    msg . z_near = shy_guts :: logic_perspective_planes_state :: z_near ;
    msg . z_far = shy_guts :: logic_perspective_planes_state :: z_far ;
    msg . scene_scale = shy_guts :: logic_perspective_planes_state :: scene_scale ;
    so_called_common_logic_perspective_planes_reply_sender :: send ( msg ) ;
}

void shy_guts :: scene_scale ( so_called_platform_math_num_fract_type & arg_scene_scale )
{
    so_called_platform_math_num_fract_type aspect_width ;
    so_called_platform_math_num_fract_type aspect_height ;
    so_called_platform_math_num_fract_type z_near_value ;

    aspect_width = shy_guts :: engine_render_aspect_state :: width ;
    aspect_height = shy_guts :: engine_render_aspect_state :: height ;
    shy_guts :: z_near ( z_near_value ) ;

    so_called_platform_math :: add_fracts ( arg_scene_scale , aspect_width , aspect_height ) ;
    so_called_platform_math :: add_to_fract ( arg_scene_scale , z_near_value ) ;
}

void shy_guts :: z_near ( so_called_platform_math_num_fract_type & arg_z_near )
{
    so_called_platform_math_num_fract_type aspect_width ;
    so_called_platform_math_num_fract_type aspect_height ;

    aspect_width = shy_guts :: engine_render_aspect_state :: width ;
    aspect_height = shy_guts :: engine_render_aspect_state :: height ;
    so_called_platform_math :: add_fracts ( arg_z_near , aspect_width , aspect_height ) ;
}

void _shy_common_logic_perspective :: receive ( so_called_common_init_message )
{
    shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_perspective_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_perspective :: receive ( so_called_common_engine_render_aspect_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_aspect_state :: requested ) )
    {
        shy_guts :: engine_render_aspect_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_aspect_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_aspect_state :: width = msg . width ;
        shy_guts :: engine_render_aspect_state :: height = msg . height ;
        shy_guts :: proceed_with_planes ( ) ;
    }
}

void _shy_common_logic_perspective :: receive ( so_called_common_logic_perspective_planes_request_message )
{
    shy_guts :: logic_perspective_planes_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_planes ( ) ;
}

void _shy_common_logic_perspective :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

