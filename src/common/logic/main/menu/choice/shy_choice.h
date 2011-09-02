class _shy_common_logic_main_menu_choice
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_controls_state_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_choice_row_selected_message ) ;
    static void receive ( so_called_common_logic_main_menu_choice_void_selected_message ) ;
    static void receive ( so_called_common_logic_main_menu_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_choice > :: module shy_common_logic_main_menu_choice_scheduled ;
