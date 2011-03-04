namespace shy_guts
{
    namespace logic_room_update_state
    {
        static so_called_type_platform_math_num_whole launch_permitted ;
        static so_called_type_platform_math_num_fract time ;
    }

    namespace logic_room_creation_permit_state
    {
        static so_called_type_platform_math_num_whole creation_permitted ;
    }

    namespace logic_room_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    namespace logic_room_texture_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_creation ( ) ;
    static void request_mesh_create ( ) ;
    static void request_texture_create ( ) ;
    static void texture_created ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
}

void shy_guts :: request_mesh_create ( )
{
}

void shy_guts :: request_texture_create ( )
{
}

void shy_guts :: texture_created ( )
{
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_creation_permit )
{
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_launch_permit )
{
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_mesh_creation_finished )
{
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_texture_creation_finished )
{
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_update )
{
}
