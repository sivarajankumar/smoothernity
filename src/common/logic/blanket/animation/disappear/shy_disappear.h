class _shy_common_logic_blanket_animation_disappear
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_blanket_animation_disappear_start ) ;
    static void receive ( so_called_message_common_logic_blanket_animation_disappear_transform_request ) ;
    static void receive ( so_called_message_common_logic_blanket_update ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation_disappear > :: module shy_common_logic_blanket_animation_disappear_scheduled ;
