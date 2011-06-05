namespace shy_guts
{
    static so_called_type_platform_math_num_whole launch_permitted ;
    static so_called_type_platform_math_num_whole created ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_door :: receive ( so_called_message_common_logic_door_creation_permit )
{
    so_called_sender_common_logic_door_mesh_create :: send ( so_called_message_common_logic_door_mesh_create ( ) ) ;
}

void _shy_common_logic_door :: receive ( so_called_message_common_logic_door_launch_permit )
{
    shy_guts :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_door_animation_appear_start :: send ( so_called_message_common_logic_door_animation_appear_start ( ) ) ;
}

void _shy_common_logic_door :: receive ( so_called_message_common_logic_door_mesh_creation_finished )
{
    so_called_sender_common_logic_door_texture_create :: send ( so_called_message_common_logic_door_texture_create ( ) ) ;
}

void _shy_common_logic_door :: receive ( so_called_message_common_logic_door_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: launch_permitted )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: created )
       )
    {
        so_called_sender_common_logic_door_place :: send ( so_called_message_common_logic_door_place ( ) ) ;
    }
}

void _shy_common_logic_door :: receive ( so_called_message_common_logic_door_texture_creation_finished )
{
    shy_guts :: created = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_door_creation_finished :: send ( so_called_message_common_logic_door_creation_finished ( ) ) ;
    so_called_sender_common_logic_door_place :: send ( so_called_message_common_logic_door_place ( ) ) ;
}

void _shy_common_logic_door :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

