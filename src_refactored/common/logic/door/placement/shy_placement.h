class _shy_common_logic_door_placement
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_door_animation_transform_reply ) ;
    static void receive ( so_called_message_common_logic_door_place ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_placement > :: module shy_common_logic_door_placement_scheduled ;
