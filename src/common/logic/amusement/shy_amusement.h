class _shy_common_logic_amusement
{
public :
    static void receive ( so_called_common_logic_amusement_creation_permit_message ) ;
    static void receive ( so_called_common_logic_amusement_launch_permit_message ) ;
    static void receive ( so_called_common_logic_amusement_update_message ) ;
    static void receive ( so_called_common_logic_blanket_animation_appear_finished_message ) ;
    static void receive ( so_called_common_logic_blanket_animation_disappear_finished_message ) ;
    static void receive ( so_called_common_logic_blanket_creation_finished_message ) ;
    static void receive ( so_called_common_logic_door_creation_finished_message ) ;
    static void receive ( so_called_common_logic_room_creation_finished_message ) ;
    static void receive ( so_called_common_logic_room_finished_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_amusement > :: module shy_common_logic_amusement_scheduled ;
