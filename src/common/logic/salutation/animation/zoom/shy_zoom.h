class _shy_common_logic_salutation_animation_zoom
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_salutation_animation_update ) ;
    static void receive ( so_called_message_common_logic_salutation_animation_zoom_play ) ;
    static void receive ( so_called_message_common_logic_salutation_animation_zoom_transform_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_animation_zoom 
    > :: module 
    shy_common_logic_salutation_animation_zoom_scheduled ;
