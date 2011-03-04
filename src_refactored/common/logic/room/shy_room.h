class _shy_common_logic_room
{
public :
    static void receive ( so_called_message_common_logic_room_creation_permit ) ;
    static void receive ( so_called_message_common_logic_room_launch_permit ) ;
    static void receive ( so_called_message_common_logic_room_mesh_creation_finished ) ;
    static void receive ( so_called_message_common_logic_room_texture_creation_finished ) ;
    static void receive ( so_called_message_common_logic_room_update ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room > :: module shy_common_logic_room_scheduled ;
