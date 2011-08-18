namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_logic_salutation_animation_transform_request )
{
    so_called_message_common_logic_salutation_animation_transform_reply msg ;
    so_called_platform_matrix :: identity ( msg . transform ) ;
    so_called_sender_common_logic_salutation_animation_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
