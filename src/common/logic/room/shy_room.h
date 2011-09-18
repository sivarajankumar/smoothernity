class _shy_common_logic_room
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_room_creation_permit_message ) ;
    static void receive ( so_called_common_logic_room_launch_permit_message ) ;
    static void receive ( so_called_common_logic_room_mesh_creation_finished_message ) ;
    static void receive ( so_called_common_logic_room_texture_creation_finished_message ) ;
    static void receive ( so_called_common_logic_room_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room > :: module shy_common_logic_room_scheduled ;
