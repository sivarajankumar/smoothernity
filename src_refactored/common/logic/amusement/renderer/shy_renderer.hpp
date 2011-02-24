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
}

void shy_guts :: prepare_ortho_render ( )
{
}

void shy_guts :: prepare_perspective_render ( )
{
}

void shy_guts :: request_observer_size ( )
{
}

void shy_guts :: request_observer_transform ( )
{
}

void shy_guts :: request_ortho_planes ( )
{
}

void shy_guts :: request_perspective_planes ( )
{
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
}

void shy_guts :: disable_depth_test ( )
{
}

void shy_guts :: enable_depth_test ( )
{
}

void shy_guts :: use_ortho_projection ( )
{
}

void shy_guts :: use_perspective_projection ( )
{
}

void shy_guts :: use_identity_transform ( )
{
}

void shy_guts :: use_observer_transform ( )
{
}

void shy_guts :: use_observer_size ( )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_amusement_render )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_blanket_render_reply )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_door_render_reply )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_observer_animation_transform_reply )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_ortho_planes_reply )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_perspective_planes_reply )
{
}

void _shy_common_logic_amusement_renderer :: receive ( so_called_message_common_logic_room_render_reply )
{
}
