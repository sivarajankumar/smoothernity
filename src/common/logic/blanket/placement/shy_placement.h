class _shy_common_logic_blanket_placement
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_blanket_animation_transform_reply_message ) ;
    static void receive ( so_called_common_logic_blanket_place_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_placement > :: module shy_common_logic_blanket_placement_scheduled ;
