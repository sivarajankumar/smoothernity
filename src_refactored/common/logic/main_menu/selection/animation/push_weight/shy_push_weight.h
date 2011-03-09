class _shy_common_logic_main_menu_selection_animation_push_weight
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_controls_state_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_row_chosen ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
    static void receive ( so_called_message_common_logic_main_menu_void_chosen ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation_push_weight > :: module
    shy_common_logic_main_menu_selection_animation_push_weight_scheduled ;
