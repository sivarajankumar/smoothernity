namespace shy_guts
{
    namespace logic_ortho_planes_state
    {
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_fract x_left ;
        static so_called_type_platform_math_num_fract x_right ;
        static so_called_type_platform_math_num_fract y_bottom ;
        static so_called_type_platform_math_num_fract y_top ;
        static so_called_type_platform_math_num_fract z_near ;
        static so_called_type_platform_math_num_fract z_far ;
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

    static void clear_screen ( ) ;
    static void request_letters_render ( ) ;
    static void request_ortho_projection_planes ( ) ;
    static void use_ortho_projection ( ) ;
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
    shy_guts :: use_ortho_projection ( ) ;
    shy_guts :: request_letters_render ( ) ;
}

void shy_guts :: logic_salutation_letters_renderer_render_state :: on_replied ( )
{
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

void shy_guts :: clear_screen ( )
{
    so_called_message_common_engine_render_clear_screen msg ;
    msg . r = so_called_common_logic_salutation_renderer_consts :: background_r ;
    msg . g = so_called_common_logic_salutation_renderer_consts :: background_g ;
    msg . b = so_called_common_logic_salutation_renderer_consts :: background_b ;
    so_called_sender_common_engine_render_clear_screen :: send ( msg ) ;
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
    so_called_sender_common_logic_ortho_planes_request :: send ( so_called_message_common_logic_ortho_planes_request ( ) ) ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_renderer :: receive ( so_called_message_common_logic_ortho_planes_reply msg )
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

void _shy_common_logic_salutation_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
