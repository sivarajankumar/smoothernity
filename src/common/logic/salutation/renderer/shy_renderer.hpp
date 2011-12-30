namespace shy_guts
{
    namespace logic_ortho_planes_state
    {
        static so_called_common_engine_taker_helper ( logic_ortho_planes ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_animation_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_animation_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_renderer_render_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_renderer_render ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_renderer_render_state
    {
        static void on_request ( ) ;
    }

    namespace logic_text_use_text_texture_state
    {
        static so_called_common_engine_taker_helper ( logic_text_use_text_texture ) taker ;
        static void on_reply ( ) ;
    }
    
    static void blend_enable ( ) ;
    static void clear_screen ( ) ;
    static void depth_test_disable ( ) ;
    static void fog_disable ( ) ;
    static void prepare_render_state ( ) ;
    static void request_animation_transform ( ) ;
    static void request_letters_render ( ) ;
    static void request_ortho_projection_planes ( ) ;
    static void request_use_text_texture ( ) ;
    static void use_ortho_projection ( ) ;
    static void use_view_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_renderer_render_state :: on_request ( )
{
    shy_guts :: clear_screen ( ) ;
    shy_guts :: request_ortho_projection_planes ( ) ;
}

void shy_guts :: logic_ortho_planes_state :: on_reply ( )
{
    shy_guts :: prepare_render_state ( ) ;
    shy_guts :: request_animation_transform ( ) ;
}

void shy_guts :: logic_salutation_animation_transform_state :: on_reply ( )
{
    shy_guts :: use_view_transform ( ) ;
    shy_guts :: request_use_text_texture ( ) ;
}

void shy_guts :: logic_text_use_text_texture_state :: on_reply ( )
{
    shy_guts :: request_letters_render ( ) ;
}

void shy_guts :: logic_salutation_letters_renderer_render_state :: on_reply ( )
{
}

void shy_guts :: prepare_render_state ( )
{
    shy_guts :: use_ortho_projection ( ) ;
    shy_guts :: blend_enable ( ) ;
    shy_guts :: depth_test_disable ( ) ;
    shy_guts :: fog_disable ( ) ;
}

void shy_guts :: depth_test_disable ( )
{
    so_called_common_engine_render_disable_depth_test_sender :: send 
        ( so_called_common_engine_render_disable_depth_test_message ( ) 
        ) ;
}

void shy_guts :: fog_disable ( )
{
    so_called_common_engine_render_fog_disable_sender :: send 
        ( so_called_common_engine_render_fog_disable_message ( ) 
        ) ;
}

void shy_guts :: blend_enable ( )
{
    so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_sender :: send 
        ( so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_message ( ) 
        ) ;
}

void shy_guts :: use_view_transform ( )
{
    so_called_common_engine_render_matrix_load_message msg ;
    msg . matrix = shy_guts :: logic_salutation_animation_transform_state :: taker . msg_reply . transform ;
    so_called_common_engine_render_matrix_load_sender :: send ( msg ) ;
}

void shy_guts :: use_ortho_projection ( )
{
    so_called_common_engine_render_projection_ortho_message msg ;
    msg . x_left = shy_guts :: logic_ortho_planes_state :: taker . msg_reply . x_left ;
    msg . x_right = shy_guts :: logic_ortho_planes_state :: taker . msg_reply . x_right ;
    msg . y_bottom = shy_guts :: logic_ortho_planes_state :: taker . msg_reply . y_bottom ;
    msg . y_top = shy_guts :: logic_ortho_planes_state :: taker . msg_reply . y_top ;
    msg . z_near = shy_guts :: logic_ortho_planes_state :: taker . msg_reply . z_near ;
    msg . z_far = shy_guts :: logic_ortho_planes_state :: taker . msg_reply . z_far ;
    so_called_common_engine_render_projection_ortho_sender :: send ( msg ) ;
}

void shy_guts :: clear_screen ( )
{
    so_called_common_engine_render_clear_screen_message msg ;
    msg . r = so_called_common_logic_salutation_renderer_consts :: background_r ;
    msg . g = so_called_common_logic_salutation_renderer_consts :: background_g ;
    msg . b = so_called_common_logic_salutation_renderer_consts :: background_b ;
    so_called_common_engine_render_clear_screen_sender :: send ( msg ) ;
}

void shy_guts :: request_animation_transform ( )
{
    shy_guts :: logic_salutation_animation_transform_state :: taker . request ( ) ;
}

void shy_guts :: request_letters_render ( )
{
    shy_guts :: logic_salutation_letters_renderer_render_state :: taker . request ( ) ;
}

void shy_guts :: request_ortho_projection_planes ( )
{
    shy_guts :: logic_ortho_planes_state :: taker . request ( ) ;
}

void shy_guts :: request_use_text_texture ( )
{
    shy_guts :: logic_text_use_text_texture_state :: taker . request ( ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_ortho_planes_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_animation_transform_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: taker . init ( ) ;
    shy_guts :: logic_text_use_text_texture_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_common_logic_ortho_planes_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_ortho_planes_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_ortho_planes_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_common_logic_salutation_animation_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_animation_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_animation_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_common_logic_salutation_letters_renderer_render_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_renderer_render_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_common_logic_salutation_renderer_render_message )
{
    shy_guts :: logic_salutation_renderer_render_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_common_logic_text_use_text_texture_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_text_use_text_texture_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_text_use_text_texture_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
