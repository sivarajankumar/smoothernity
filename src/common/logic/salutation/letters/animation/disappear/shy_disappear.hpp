namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_disappear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_disappear :: receive ( so_called_common_logic_salutation_letters_animation_disappear_rewind_message )
{
}

void _shy_common_logic_salutation_letters_animation_disappear :: receive ( so_called_common_logic_salutation_letters_animation_disappear_step_message )
{
}

void _shy_common_logic_salutation_letters_animation_disappear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
