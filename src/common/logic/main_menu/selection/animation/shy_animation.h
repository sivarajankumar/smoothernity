class _shy_common_logic_main_menu_selection_animation
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_appear_transform_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_disappear_transform_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_idle_attention_transform_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_idle_transform_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_push_attention_transform_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_push_transform_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_push_weight_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_select_transform_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_transform_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_unselect_transform_reply ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation > :: module shy_common_logic_main_menu_selection_animation_scheduled ;
