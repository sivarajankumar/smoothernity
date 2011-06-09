namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_roll_out > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_message_common_logic_salutation_letters_animation_roll_out_play )
{
}

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_message_common_logic_salutation_letters_animation_update )
{
}

void _shy_common_logic_salutation_letters_animation_roll_out :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
