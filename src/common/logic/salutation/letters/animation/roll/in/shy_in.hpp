namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_roll_in > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_roll_in :: receive ( so_called_common_init_message )
{
}

void _shy_common_logic_salutation_letters_animation_roll_in :: receive ( so_called_common_logic_salutation_letters_animation_roll_in_rewind_message )
{
}

void _shy_common_logic_salutation_letters_animation_roll_in :: receive ( so_called_common_logic_salutation_letters_animation_roll_in_step_message )
{
}

void _shy_common_logic_salutation_letters_animation_roll_in :: receive ( so_called_common_logic_salutation_letters_animation_roll_in_transform_request_message msg )
{
    so_called_common_logic_salutation_letters_animation_roll_in_transform_reply_message msg_reply ;
    msg_reply . letter = msg . letter ;
    msg_reply . position_radius = so_called_platform_math_consts :: fract_0 ;
    msg_reply . position_spin_periods = so_called_platform_math_consts :: fract_0 ;
    msg_reply . rotation_periods = so_called_platform_math_consts :: fract_0 ;
    so_called_common_logic_salutation_letters_animation_roll_in_transform_reply_sender :: send ( msg_reply ) ;
}

void _shy_common_logic_salutation_letters_animation_roll_in :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
