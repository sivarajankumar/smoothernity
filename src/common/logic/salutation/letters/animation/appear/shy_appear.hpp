namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_appear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_appear :: receive ( so_called_common_logic_salutation_letters_animation_appear_play_message )
{
}

void _shy_common_logic_salutation_letters_animation_appear :: receive ( so_called_common_logic_salutation_letters_animation_appear_transform_request_message msg )
{
    so_called_common_logic_salutation_letters_animation_appear_transform_reply_message msg_reply ;
    msg_reply . letter = msg . letter ;
    msg_reply . scale = so_called_platform_math_consts :: fract_1 ;
    so_called_common_logic_salutation_letters_animation_appear_transform_reply_sender :: send ( msg_reply ) ;
}

void _shy_common_logic_salutation_letters_animation_appear :: receive ( so_called_common_logic_salutation_letters_animation_update_message )
{
}

void _shy_common_logic_salutation_letters_animation_appear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
