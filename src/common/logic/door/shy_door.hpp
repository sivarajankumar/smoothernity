namespace shy_guts
{
    static so_called_platform_math_num_whole_type launch_permitted ;
    static so_called_platform_math_num_whole_type created ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_door :: receive ( so_called_common_init_message )
{
    shy_guts :: launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: created = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_door :: receive ( so_called_common_logic_door_creation_permit_message )
{
    so_called_common_logic_door_mesh_create_sender :: send ( so_called_common_logic_door_mesh_create_message ( ) ) ;
}

void _shy_common_logic_door :: receive ( so_called_common_logic_door_launch_permit_message )
{
    shy_guts :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_door_animation_appear_start_sender :: send ( so_called_common_logic_door_animation_appear_start_message ( ) ) ;
}

void _shy_common_logic_door :: receive ( so_called_common_logic_door_mesh_creation_finished_message )
{
    so_called_common_logic_door_texture_create_sender :: send ( so_called_common_logic_door_texture_create_message ( ) ) ;
}

void _shy_common_logic_door :: receive ( so_called_common_logic_door_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: launch_permitted )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: created )
       )
    {
        so_called_common_logic_door_place_sender :: send ( so_called_common_logic_door_place_message ( ) ) ;
    }
}

void _shy_common_logic_door :: receive ( so_called_common_logic_door_texture_creation_finished_message )
{
    shy_guts :: created = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_door_creation_finished_sender :: send ( so_called_common_logic_door_creation_finished_message ( ) ) ;
    so_called_common_logic_door_place_sender :: send ( so_called_common_logic_door_place_message ( ) ) ;
}

void _shy_common_logic_door :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

