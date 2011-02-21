namespace shy_guts
{
    namespace logic_ortho_planes_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_fract x_left ;
        static so_called_type_platform_math_num_fract x_right ;
        static so_called_type_platform_math_num_fract y_bottom ;
        static so_called_type_platform_math_num_fract y_top ;
        static so_called_type_platform_math_num_fract z_near ;
        static so_called_type_platform_math_num_fract z_far ;
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
    static void compute_y_bottom ( ) ;
    static void compute_y_top ( ) ;
    static void compute_z_near ( ) ;
    static void compute_z_far ( ) ;
    static void reply_planes ( ) ;
    static void reply_computed_planes ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_ortho > _scheduled_context_type ;
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

void shy_guts :: compute_y_bottom ( )
{
}

void shy_guts :: compute_y_top ( )
{
}

void shy_guts :: compute_z_near ( )
{
}

void shy_guts :: compute_z_far ( )
{
}

void shy_guts :: reply_planes ( )
{
}

void shy_guts :: reply_computed_planes ( )
{
}

void _shy_common_logic_ortho :: receive ( so_called_message_common_engine_render_aspect_reply msg )
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

void _shy_common_logic_ortho :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_ortho :: receive ( so_called_message_common_logic_ortho_planes_request )
{
    shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_planes ( ) ;
}
