class _shy_common_logic_door
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_door_creation_permit_message ) ;
    static void receive ( so_called_common_logic_door_launch_permit_message ) ;
    static void receive ( so_called_common_logic_door_mesh_creation_finished_message ) ;
    static void receive ( so_called_common_logic_door_texture_creation_finished_message ) ;
    static void receive ( so_called_common_logic_door_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door > :: module shy_common_logic_door_scheduled ;
