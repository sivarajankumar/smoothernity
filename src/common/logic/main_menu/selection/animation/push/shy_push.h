class _shy_common_logic_main_menu_selection_animation_push
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_controls_state_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_push_transform_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
    static void receive ( so_called_message_common_logic_main_menu_void_chosen ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_push > :: module
    shy_common_logic_main_menu_selection_animation_push_scheduled ;