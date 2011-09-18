class _shy_common_logic_salutation_animation_zoom
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_animation_zoom_rewind_message ) ;
    static void receive ( so_called_common_logic_salutation_animation_zoom_step_message ) ;
    static void receive ( so_called_common_logic_salutation_animation_zoom_transform_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_animation_zoom 
    > :: module 
    shy_common_logic_salutation_animation_zoom_scheduled ;
