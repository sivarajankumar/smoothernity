typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_shaper > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_meshes_shaper :: receive ( so_called_message_common_logic_salutation_letters_meshes_shaper_shape_request msg )
{
    so_called_message_common_logic_salutation_letters_meshes_shaper_shape_reply reply_msg ;
    reply_msg . letter_index = msg . letter_index ;
    so_called_sender_common_logic_salutation_letters_meshes_shaper_shape_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_salutation_letters_meshes_shaper :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
