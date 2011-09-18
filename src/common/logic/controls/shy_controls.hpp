namespace shy_guts
{
    namespace logic_controls_state
    {
        static so_called_platform_math_num_whole_type primary_button_down ;
        static so_called_platform_math_num_fract_type cursor_x ;
        static so_called_platform_math_num_fract_type cursor_y ;
    }

    static void compute_identity_state ( ) ;
    static void compute_mouse_state ( ) ;
    static void compute_touch_state ( ) ;
    static void reply_controls_state ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_controls > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_identity_state ( )
{
    so_called_platform_math_num_fract_type cursor_x ;
    so_called_platform_math_num_fract_type cursor_y ;
    so_called_platform_math_num_whole_type primary_button_down ;

    cursor_x = so_called_platform_math_consts :: fract_0 ;
    cursor_y = so_called_platform_math_consts :: fract_0 ;
    primary_button_down = so_called_platform_math_consts :: whole_false ;
}

void shy_guts :: compute_mouse_state ( )
{
    so_called_platform_math_num_fract_type cursor_x ;
    so_called_platform_math_num_fract_type cursor_y ;
    so_called_platform_math_num_whole_type mouse_enabled ;
    so_called_platform_math_num_whole_type primary_button_down ;

    so_called_platform_mouse :: enabled ( mouse_enabled ) ;
    if ( so_called_platform_conditions :: whole_is_true ( mouse_enabled ) )
    {
        so_called_platform_mouse :: left_button_down ( primary_button_down ) ;
        so_called_platform_mouse :: x ( cursor_x ) ;
        so_called_platform_mouse :: y ( cursor_y ) ;

        shy_guts :: logic_controls_state :: cursor_x = cursor_x ;
        shy_guts :: logic_controls_state :: cursor_y = cursor_y ;
        shy_guts :: logic_controls_state :: primary_button_down = primary_button_down ;
    }
}

void shy_guts :: compute_touch_state ( )
{
    so_called_platform_math_num_fract_type cursor_x ;
    so_called_platform_math_num_fract_type cursor_y ;
    so_called_platform_math_num_whole_type touch_enabled ;
    so_called_platform_math_num_whole_type primary_button_down ;

    so_called_platform_touch :: enabled ( touch_enabled ) ;
    if ( so_called_platform_conditions :: whole_is_true ( touch_enabled ) )
    {
        so_called_platform_touch :: occured ( primary_button_down ) ;
        so_called_platform_touch :: x ( cursor_x ) ;
        so_called_platform_touch :: y ( cursor_y ) ;

        shy_guts :: logic_controls_state :: cursor_x = cursor_x ;
        shy_guts :: logic_controls_state :: cursor_y = cursor_y ;
        shy_guts :: logic_controls_state :: primary_button_down = primary_button_down ;
    }
}

void shy_guts :: reply_controls_state ( )
{
    so_called_common_logic_controls_state_reply_message msg ;
    msg . primary_button_down = shy_guts :: logic_controls_state :: primary_button_down ;
    msg . cursor_x = shy_guts :: logic_controls_state :: cursor_x ;
    msg . cursor_y = shy_guts :: logic_controls_state :: cursor_y ;
    so_called_common_logic_controls_state_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_controls :: receive ( so_called_common_logic_controls_state_request_message )
{
    shy_guts :: compute_identity_state ( ) ;
    shy_guts :: compute_mouse_state ( ) ;
    shy_guts :: compute_touch_state ( ) ;
    shy_guts :: reply_controls_state ( ) ;
}

void _shy_common_logic_controls :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
