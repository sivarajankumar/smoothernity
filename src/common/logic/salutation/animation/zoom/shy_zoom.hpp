namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_animation_zoom > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_message_common_logic_salutation_animation_update )
{
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_message_common_logic_salutation_animation_zoom_play )
{
}

void _shy_common_logic_salutation_animation_zoom :: receive ( so_called_message_common_logic_salutation_animation_zoom_transform_request )
{
    so_called_message_common_logic_salutation_animation_zoom_transform_reply msg ;
    so_called_platform_math :: make_num_fract ( msg . scale , 1 , 1 ) ;
    so_called_sender_common_logic_salutation_animation_zoom_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_animation_zoom :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
