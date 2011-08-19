namespace shy_guts
{
    namespace logic_ortho_planes_state
    {
        static so_called_message_common_logic_ortho_planes_reply msg_replied ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_animation_transform_state
    {
        static so_called_message_common_logic_salutation_animation_transform_reply msg_replied ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_letters_renderer_render_state
    {
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_renderer_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
    }

    namespace logic_text_use_text_texture_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static void on_replied ( ) ;
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
    static void work ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: work ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_renderer_render_state :: requested ) )
    {
        shy_guts :: logic_salutation_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_renderer_render_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_ortho_planes_state :: replied ) )
    {
        shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_ortho_planes_state :: on_replied ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_animation_transform_state :: replied ) )
    {
        shy_guts :: logic_salutation_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_animation_transform_state :: on_replied ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_use_text_texture_state :: replied ) )
    {
        shy_guts :: logic_text_use_text_texture_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_text_use_text_texture_state :: on_replied ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_renderer_render_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_renderer_render_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_renderer_render_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_renderer_render_state :: on_requested ( )
{
    shy_guts :: clear_screen ( ) ;
    shy_guts :: request_ortho_projection_planes ( ) ;
}

void shy_guts :: logic_ortho_planes_state :: on_replied ( )
{
    shy_guts :: prepare_render_state ( ) ;
    shy_guts :: request_animation_transform ( ) ;
}

void shy_guts :: logic_salutation_animation_transform_state :: on_replied ( )
{
    shy_guts :: use_view_transform ( ) ;
    shy_guts :: request_use_text_texture ( ) ;
}

void shy_guts :: logic_text_use_text_texture_state :: on_replied ( )
{
    shy_guts :: request_letters_render ( ) ;
}

void shy_guts :: logic_salutation_letters_renderer_render_state :: on_replied ( )
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
    so_called_sender_common_engine_render_disable_depth_test :: send 
        ( so_called_message_common_engine_render_disable_depth_test ( ) 
        ) ;
}

void shy_guts :: fog_disable ( )
{
    so_called_sender_common_engine_render_fog_disable :: send 
        ( so_called_message_common_engine_render_fog_disable ( ) 
        ) ;
}

void shy_guts :: blend_enable ( )
{
    so_called_sender_common_engine_render_blend_src_alpha_dst_one_minus_alpha :: send 
        ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha ( ) 
        ) ;
}

void shy_guts :: use_view_transform ( )
{
    so_called_message_common_engine_render_matrix_load msg ;
    msg . matrix = shy_guts :: logic_salutation_animation_transform_state :: msg_replied . transform ;
    so_called_sender_common_engine_render_matrix_load :: send ( msg ) ;
}

void shy_guts :: use_ortho_projection ( )
{
    so_called_message_common_engine_render_projection_ortho msg ;
    msg . x_left = shy_guts :: logic_ortho_planes_state :: msg_replied . x_left ;
    msg . x_right = shy_guts :: logic_ortho_planes_state :: msg_replied . x_right ;
    msg . y_bottom = shy_guts :: logic_ortho_planes_state :: msg_replied . y_bottom ;
    msg . y_top = shy_guts :: logic_ortho_planes_state :: msg_replied . y_top ;
    msg . z_near = shy_guts :: logic_ortho_planes_state :: msg_replied . z_near ;
    msg . z_far = shy_guts :: logic_ortho_planes_state :: msg_replied . z_far ;
    so_called_sender_common_engine_render_projection_ortho :: send ( msg ) ;
}

void shy_guts :: clear_screen ( )
{
    so_called_message_common_engine_render_clear_screen msg ;
    msg . r = so_called_common_logic_salutation_renderer_consts :: background_r ;
    msg . g = so_called_common_logic_salutation_renderer_consts :: background_g ;
    msg . b = so_called_common_logic_salutation_renderer_consts :: background_b ;
    so_called_sender_common_engine_render_clear_screen :: send ( msg ) ;
}

void shy_guts :: request_animation_transform ( )
{
    shy_guts :: logic_salutation_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_salutation_animation_transform_request :: send
        ( so_called_message_common_logic_salutation_animation_transform_request ( )
        ) ;
}

void shy_guts :: request_letters_render ( )
{
    shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_salutation_letters_renderer_render_request :: send
        ( so_called_message_common_logic_salutation_letters_renderer_render_request ( )
        ) ;
}

void shy_guts :: request_ortho_projection_planes ( )
{
    shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_ortho_planes_request :: send 
        ( so_called_message_common_logic_ortho_planes_request ( ) 
        ) ;
}

void shy_guts :: request_use_text_texture ( )
{
    shy_guts :: logic_text_use_text_texture_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_text_use_text_texture_request :: send 
        ( so_called_message_common_logic_text_use_text_texture_request ( ) 
        ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_use_text_texture_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_use_text_texture_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_logic_ortho_planes_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_ortho_planes_state :: requested ) )
    {
        shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_ortho_planes_state :: msg_replied = msg ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_logic_salutation_animation_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_salutation_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_animation_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_salutation_animation_transform_state :: msg_replied = msg ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_logic_salutation_letters_renderer_render_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_renderer_render_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_renderer_render_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_logic_salutation_renderer_render )
{
    shy_guts :: logic_salutation_renderer_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: work ( ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_logic_text_use_text_texture_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_use_text_texture_state :: requested ) )
    {
        shy_guts :: logic_text_use_text_texture_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_text_use_text_texture_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
