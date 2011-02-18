namespace shy_guts
{
    class logic_controls_state_type
    {
    public :
        so_called_type_platform_math_num_whole primary_button_down ;
        so_called_type_platform_math_num_fract cursor_x ;
        so_called_type_platform_math_num_fract cursor_y ;
    } ;

    static void compute_identity_state ( ) ;
    static void compute_mouse_state ( ) ;
    static void compute_touch_state ( ) ;
    static void reply_controls_state ( ) ;

    static logic_controls_state_type logic_controls_state ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_controls > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_identity_state ( )
{
    so_called_type_platform_math_num_fract cursor_x ;
    so_called_type_platform_math_num_fract cursor_y ;
    so_called_type_platform_math_num_whole primary_button_down ;

    cursor_x = so_called_platform_math_consts :: fract_0 ;
    cursor_y = so_called_platform_math_consts :: fract_0 ;
    primary_button_down = so_called_platform_math_consts :: whole_false ;
}

void shy_guts :: compute_mouse_state ( )
{
}

void shy_guts :: compute_touch_state ( )
{
}

void shy_guts :: reply_controls_state ( )
{
}

void _shy_common_logic_controls :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_controls :: receive ( so_called_message_common_logic_controls_state_request )
{
    shy_guts :: compute_identity_state ( ) ;
    shy_guts :: compute_mouse_state ( ) ;
    shy_guts :: compute_touch_state ( ) ;
    shy_guts :: reply_controls_state ( ) ;
}
