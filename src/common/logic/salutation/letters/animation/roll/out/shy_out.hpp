namespace shy_guts
{
    static so_called_platform_math_num_fract_type time ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_roll_out > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_init_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_logic_salutation_letters_animation_roll_out_rewind_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_logic_salutation_letters_animation_roll_out_step_message )
{
    so_called_common_engine_math_stateless :: add_frame_to_time ( shy_guts :: time ) ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_logic_salutation_letters_animation_roll_out_transform_request_message msg )
{
    so_called_common_logic_salutation_letters_animation_roll_out_transform_reply_message msg_reply ;
    msg_reply . letter = msg . letter ;
    msg_reply . position_radius = so_called_platform_math_consts :: fract_0 ;
    msg_reply . position_spin_periods = so_called_platform_math_consts :: fract_0 ;
    msg_reply . rotation_periods = so_called_platform_math_consts :: fract_0 ;
    so_called_common_logic_salutation_letters_animation_roll_out_transform_reply_sender :: send ( msg_reply ) ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
