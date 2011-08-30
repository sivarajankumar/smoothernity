namespace shy_guts
{
    namespace logic_amusement_render_state
    {
        static so_called_platform_math_num_whole_type requested ;
    }

    namespace logic_observer_animation_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_matrix_data_type transform ;
    }

    namespace logic_ortho_planes_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type x_left ;
        static so_called_platform_math_num_fract_type x_right ;
        static so_called_platform_math_num_fract_type y_bottom ;
        static so_called_platform_math_num_fract_type y_top ;
        static so_called_platform_math_num_fract_type z_near ;
        static so_called_platform_math_num_fract_type z_far ;
    }

    namespace logic_perspective_planes_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type x_left ;
        static so_called_platform_math_num_fract_type x_right ;
        static so_called_platform_math_num_fract_type y_bottom ;
        static so_called_platform_math_num_fract_type y_top ;
        static so_called_platform_math_num_fract_type z_near ;
        static so_called_platform_math_num_fract_type z_far ;
        static so_called_platform_math_num_fract_type scene_scale ;
    }

    namespace logic_blanket_render_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
    }

    namespace logic_door_render_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
    }

    namespace logic_room_render_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
    }

    static void proceed_with_render ( ) ;
    static void prepare_ortho_render ( ) ;
    static void prepare_perspective_render ( ) ;
    static void request_observer_transform ( ) ;
    static void request_ortho_planes ( ) ;
    static void request_perspective_planes ( ) ;
    static void request_blanket_render ( ) ;
    static void request_door_render ( ) ;
    static void request_room_render ( ) ;
    static void clear_screen ( ) ;
    static void disable_depth_test ( ) ;
    static void enable_depth_test ( ) ;
    static void use_ortho_projection ( ) ;
    static void use_perspective_projection ( ) ;
    static void use_identity_transform ( ) ;
    static void use_observer_transform ( ) ;
    static void use_observer_size ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_amusement_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_render ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_amusement_render_state :: requested ) )
    {
        shy_guts :: logic_amusement_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_perspective_planes ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_perspective_planes_state :: replied ) )
    {
        shy_guts :: logic_perspective_planes_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_observer_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_observer_animation_transform_state :: replied ) )
    {
        shy_guts :: logic_observer_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: prepare_perspective_render ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_render_state :: replied ) )
    {
        shy_guts :: logic_room_render_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_door_render ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_render_state :: replied ) )
    {
        shy_guts :: logic_door_render_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_ortho_planes ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_ortho_planes_state :: replied ) )
    {
        shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: prepare_ortho_render ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_render_state :: replied ) )
    {
        shy_guts :: logic_blanket_render_state :: replied = so_called_platform_math_consts :: whole_false ;
    }
}

void shy_guts :: prepare_ortho_render ( )
{
    shy_guts :: disable_depth_test ( ) ;
    shy_guts :: use_ortho_projection ( ) ;
    shy_guts :: use_identity_transform ( ) ;
    shy_guts :: request_blanket_render ( ) ;
}

void shy_guts :: prepare_perspective_render ( )
{
    shy_guts :: clear_screen ( ) ;
    shy_guts :: enable_depth_test ( ) ;
    shy_guts :: use_perspective_projection ( ) ;
    shy_guts :: use_observer_size ( ) ;
    shy_guts :: use_observer_transform ( ) ;
    shy_guts :: request_room_render ( ) ;
}

void shy_guts :: request_observer_transform ( )
{
    shy_guts :: logic_observer_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_observer_animation_transform_request_sender :: send ( so_called_common_logic_observer_animation_transform_request_message ( ) ) ;
}

void shy_guts :: request_ortho_planes ( )
{
    shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_ortho_planes_request_sender :: send ( so_called_common_logic_ortho_planes_request_message ( ) ) ;
}

void shy_guts :: request_perspective_planes ( )
{
    shy_guts :: logic_perspective_planes_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_perspective_planes_request_sender :: send ( so_called_common_logic_perspective_planes_request_message ( ) ) ;
}

void shy_guts :: request_blanket_render ( )
{
    shy_guts :: logic_blanket_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_blanket_render_request_sender :: send ( so_called_common_logic_blanket_render_request_message ( ) ) ;
}

void shy_guts :: request_door_render ( )
{
    shy_guts :: logic_door_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_door_render_request_sender :: send ( so_called_common_logic_door_render_request_message ( ) ) ;
}

void shy_guts :: request_room_render ( )
{
    shy_guts :: logic_room_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_room_render_request_sender :: send ( so_called_common_logic_room_render_request_message ( ) ) ;
}

void shy_guts :: clear_screen ( )
{
    so_called_common_engine_render_clear_screen_message msg ;
    msg . r = so_called_common_logic_amusement_consts :: renderer_clear_color_r ; 
    msg . g = so_called_common_logic_amusement_consts :: renderer_clear_color_g ; 
    msg . b = so_called_common_logic_amusement_consts :: renderer_clear_color_b ; 
    so_called_common_engine_render_clear_screen_sender :: send ( msg ) ;
}

void shy_guts :: disable_depth_test ( )
{
    so_called_common_engine_render_disable_depth_test_sender :: send ( so_called_common_engine_render_disable_depth_test_message ( ) ) ;
}

void shy_guts :: enable_depth_test ( )
{
    so_called_common_engine_render_enable_depth_test_sender :: send ( so_called_common_engine_render_enable_depth_test_message ( ) ) ;
}

void shy_guts :: use_ortho_projection ( )
{
    so_called_common_engine_render_projection_ortho_message msg ;
    msg . x_left = shy_guts :: logic_ortho_planes_state :: x_left ;
    msg . x_right = shy_guts :: logic_ortho_planes_state :: x_right ;
    msg . y_bottom = shy_guts :: logic_ortho_planes_state :: y_bottom ;
    msg . y_top = shy_guts :: logic_ortho_planes_state :: y_top ;
    msg . z_near = shy_guts :: logic_ortho_planes_state :: z_near ;
    msg . z_far = shy_guts :: logic_ortho_planes_state :: z_far ;
    so_called_common_engine_render_projection_ortho_sender :: send ( msg ) ;
}

void shy_guts :: use_perspective_projection ( )
{
    so_called_common_engine_render_projection_frustum_message msg ;
    msg . x_left = shy_guts :: logic_perspective_planes_state :: x_left ;
    msg . x_right = shy_guts :: logic_perspective_planes_state :: x_right ;
    msg . y_bottom = shy_guts :: logic_perspective_planes_state :: y_bottom ;
    msg . y_top = shy_guts :: logic_perspective_planes_state :: y_top ;
    msg . z_near = shy_guts :: logic_perspective_planes_state :: z_near ;
    msg . z_far = shy_guts :: logic_perspective_planes_state :: z_far ;
    so_called_common_engine_render_projection_frustum_sender :: send ( msg ) ;
}

void shy_guts :: use_identity_transform ( )
{
    so_called_common_engine_render_matrix_identity_sender :: send ( so_called_common_engine_render_matrix_identity_message ( ) ) ;
}

void shy_guts :: use_observer_transform ( )
{
    so_called_common_engine_render_matrix_mult_message msg ;
    msg . matrix = shy_guts :: logic_observer_animation_transform_state :: transform ;
    so_called_common_engine_render_matrix_mult_sender :: send ( msg ) ;
}

void shy_guts :: use_observer_size ( )
{
    so_called_platform_math_num_fract_type scene_scale ;
    so_called_platform_matrix_data_type transform ;

    scene_scale = shy_guts :: logic_perspective_planes_state :: scene_scale ;
    so_called_common_engine_math_stateless :: scale ( transform , scene_scale ) ;

    so_called_common_engine_render_matrix_load_message msg ;
    msg . matrix = transform ;
    so_called_common_engine_render_matrix_load_sender :: send ( msg ) ;
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_amusement_render_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_render_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_render_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_door_render_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_door_render_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_observer_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_observer_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_perspective_planes_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_perspective_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_render_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_render_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_logic_amusement_render_message )
{
    shy_guts :: logic_amusement_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_render ( ) ;
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_logic_blanket_render_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_render_state :: requested ) )
    {
        shy_guts :: logic_blanket_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_blanket_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_logic_door_render_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_render_state :: requested ) )
    {
        shy_guts :: logic_door_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_door_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_logic_observer_animation_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_observer_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_observer_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_observer_animation_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_observer_animation_transform_state :: transform = msg . transform ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_logic_ortho_planes_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_ortho_planes_state :: requested ) )
    {
        shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_ortho_planes_state :: x_left = msg . x_left ;
        shy_guts :: logic_ortho_planes_state :: x_right = msg . x_right ;
        shy_guts :: logic_ortho_planes_state :: y_bottom = msg . y_bottom ;
        shy_guts :: logic_ortho_planes_state :: y_top = msg . y_top ;
        shy_guts :: logic_ortho_planes_state :: z_near = msg . z_near ;
        shy_guts :: logic_ortho_planes_state :: z_far = msg . z_far ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_logic_perspective_planes_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_perspective_planes_state :: requested ) )
    {
        shy_guts :: logic_perspective_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_perspective_planes_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_perspective_planes_state :: x_left = msg . x_left ;
        shy_guts :: logic_perspective_planes_state :: x_right = msg . x_right ;
        shy_guts :: logic_perspective_planes_state :: y_bottom = msg . y_bottom ;
        shy_guts :: logic_perspective_planes_state :: y_top = msg . y_top ;
        shy_guts :: logic_perspective_planes_state :: z_near = msg . z_near ;
        shy_guts :: logic_perspective_planes_state :: z_far = msg . z_far ;
        shy_guts :: logic_perspective_planes_state :: scene_scale = msg . scene_scale ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_common_logic_room_render_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_render_state :: requested ) )
    {
        shy_guts :: logic_room_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
