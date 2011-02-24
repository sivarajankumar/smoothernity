namespace shy_guts
{
    namespace logic_amusement_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_observer_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_matrix_data transform ;
    }

    namespace logic_ortho_planes_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract x_left ;
        static so_called_type_platform_math_num_fract x_right ;
        static so_called_type_platform_math_num_fract y_bottom ;
        static so_called_type_platform_math_num_fract y_top ;
        static so_called_type_platform_math_num_fract z_near ;
        static so_called_type_platform_math_num_fract z_far ;
    }

    namespace logic_perspective_planes_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract x_left ;
        static so_called_type_platform_math_num_fract x_right ;
        static so_called_type_platform_math_num_fract y_bottom ;
        static so_called_type_platform_math_num_fract y_top ;
        static so_called_type_platform_math_num_fract z_near ;
        static so_called_type_platform_math_num_fract z_far ;
        static so_called_type_platform_math_num_fract scene_scale ;
    }

    namespace logic_blanket_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    namespace logic_door_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    namespace logic_room_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_render ( ) ;
    static void prepare_ortho_render ( ) ;
    static void prepare_perspective_render ( ) ;
    static void request_observer_size ( ) ;
    static void request_observer_transform ( ) ;
    static void request_ortho_planes ( ) ;
    static void request_perspective_planes ( ) ;
    static void request_blanket_render ( ) ;
    static void request_door_render ( ) ;
    static void request_room_render ( ) ;
    static void observer_transform_received ( ) ;
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

void shy_guts :: request_observer_size ( )
{
}

void shy_guts :: request_observer_transform ( )
{
    shy_guts :: logic_observer_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_observer_animation_transform_request :: send ( so_called_message_common_logic_observer_animation_transform_request ( ) ) ;
}

void shy_guts :: request_ortho_planes ( )
{
    shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_ortho_planes_request :: send ( so_called_message_common_logic_ortho_planes_request ( ) ) ;
}

void shy_guts :: request_perspective_planes ( )
{
    shy_guts :: logic_perspective_planes_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_perspective_planes_request :: send ( so_called_message_common_logic_perspective_planes_request ( ) ) ;
}

void shy_guts :: request_blanket_render ( )
{
}

void shy_guts :: request_door_render ( )
{
}

void shy_guts :: request_room_render ( )
{
}

void shy_guts :: observer_transform_received ( )
{
}

void shy_guts :: clear_screen ( )
{
    so_called_message_common_engine_render_clear_screen msg ;
    msg . r = so_called_common_logic_amusement_consts :: renderer_clear_color_r ; 
    msg . g = so_called_common_logic_amusement_consts :: renderer_clear_color_g ; 
    msg . b = so_called_common_logic_amusement_consts :: renderer_clear_color_b ; 
    so_called_sender_common_engine_render_clear_screen :: send ( msg ) ;
}

void shy_guts :: disable_depth_test ( )
{
    so_called_sender_common_engine_render_disable_depth_test :: send ( so_called_message_common_engine_render_disable_depth_test ( ) ) ;
}

void shy_guts :: enable_depth_test ( )
{
    so_called_sender_common_engine_render_enable_depth_test :: send ( so_called_message_common_engine_render_enable_depth_test ( ) ) ;
}

void shy_guts :: use_ortho_projection ( )
{
    so_called_message_common_engine_render_projection_ortho msg ;
    msg . x_left = shy_guts :: logic_ortho_planes_state :: x_left ;
    msg . x_right = shy_guts :: logic_ortho_planes_state :: x_right ;
    msg . y_bottom = shy_guts :: logic_ortho_planes_state :: y_bottom ;
    msg . y_top = shy_guts :: logic_ortho_planes_state :: y_top ;
    msg . z_near = shy_guts :: logic_ortho_planes_state :: z_near ;
    msg . z_far = shy_guts :: logic_ortho_planes_state :: z_far ;
    so_called_sender_common_engine_render_projection_ortho :: send ( msg ) ;
}

void shy_guts :: use_perspective_projection ( )
{
    so_called_message_common_engine_render_projection_frustum msg ;
    msg . x_left = shy_guts :: logic_perspective_planes_state :: x_left ;
    msg . x_right = shy_guts :: logic_perspective_planes_state :: x_right ;
    msg . y_bottom = shy_guts :: logic_perspective_planes_state :: y_bottom ;
    msg . y_top = shy_guts :: logic_perspective_planes_state :: y_top ;
    msg . z_near = shy_guts :: logic_perspective_planes_state :: z_near ;
    msg . z_far = shy_guts :: logic_perspective_planes_state :: z_far ;
    so_called_sender_common_engine_render_projection_frustum :: send ( msg ) ;
}

void shy_guts :: use_identity_transform ( )
{
    so_called_sender_common_engine_render_matrix_identity :: send ( so_called_message_common_engine_render_matrix_identity ( ) ) ;
}

void shy_guts :: use_observer_transform ( )
{
    so_called_message_common_engine_render_matrix_mult msg ;
    msg . matrix = shy_guts :: logic_observer_animation_transform_state :: transform ;
    so_called_sender_common_engine_render_matrix_mult :: send ( msg ) ;
}

void shy_guts :: use_observer_size ( )
{
    so_called_type_platform_math_num_fract scene_scale ;
    so_called_type_platform_matrix_data transform ;

    scene_scale = shy_guts :: logic_perspective_planes_state :: scene_scale ;
    so_called_common_engine_math_stateless :: scale ( transform , scene_scale ) ;

    so_called_message_common_engine_render_matrix_load msg ;
    msg . matrix = transform ;
    so_called_sender_common_engine_render_matrix_load :: send ( msg ) ;
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_amusement_render )
{
    shy_guts :: logic_amusement_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_render ( ) ;
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_blanket_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_render_state :: requested ) )
    {
        shy_guts :: logic_blanket_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_blanket_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_door_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_render_state :: requested ) )
    {
        shy_guts :: logic_door_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_door_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_observer_animation_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_observer_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_observer_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_observer_animation_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_observer_animation_transform_state :: transform = msg . transform ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_ortho_planes_reply msg )
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

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_perspective_planes_reply msg )
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

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_room_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_render_state :: requested ) )
    {
        shy_guts :: logic_room_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
}
