class _shy_common_logic_amusement
{
public :
    static void receive ( so_called_message_common_logic_amusement_creation_permit ) ;
    static void receive ( so_called_message_common_logic_amusement_launch_permit ) ;
    static void receive ( so_called_message_common_logic_amusement_update ) ;
    static void receive ( so_called_message_common_logic_blanket_animation_appear_finished ) ;
    static void receive ( so_called_message_common_logic_blanket_animation_disappear_finished ) ;
    static void receive ( so_called_message_common_logic_blanket_creation_finished ) ;
    static void receive ( so_called_message_common_logic_door_creation_finished ) ;
    static void receive ( so_called_message_common_logic_room_creation_finished ) ;
    static void receive ( so_called_message_common_logic_room_finished ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_amusement > :: module shy_common_logic_amusement_scheduled ;
