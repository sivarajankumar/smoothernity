class _shy_common_logic_blanket
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_blanket_creation_permit_message ) ;
    static void receive ( so_called_common_logic_blanket_mesh_creation_finished_message ) ;
    static void receive ( so_called_common_logic_blanket_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket > :: module shy_common_logic_blanket_scheduled ;
