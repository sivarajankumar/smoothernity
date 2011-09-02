class _shy_common_logic_main_menu_letters_animation_selection_push
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_controls_state_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_selection_push_transform_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_update_message ) ;
    static void receive ( so_called_common_logic_main_menu_void_chosen_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation_selection_push > :: module shy_common_logic_main_menu_letters_animation_selection_push_scheduled ;
