class _shy_common_logic_blanket_animation_appear
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_blanket_animation_appear_start ) ;
    static void receive ( so_called_message_common_logic_blanket_animation_appear_transform_request ) ;
    static void receive ( so_called_message_common_logic_blanket_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation_appear > :: module shy_common_logic_blanket_animation_appear_scheduled ;