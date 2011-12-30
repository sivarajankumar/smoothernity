class _shy_common_logic_main_menu_letters_animation
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_appear_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_disappear_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_idle_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_selection_push_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_selection_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_selection_weight_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_transform_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_unselection_weight_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_animation > :: module shy_common_logic_main_menu_letters_animation_scheduled ;
