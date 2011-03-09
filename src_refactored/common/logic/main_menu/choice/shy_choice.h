class _shy_common_logic_main_menu_choice
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_controls_state_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_choice_row_selected ) ;
    static void receive ( so_called_message_common_logic_main_menu_choice_void_selected ) ;
    static void receive ( so_called_message_common_logic_main_menu_update ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_choice > :: module shy_common_logic_main_menu_choice_scheduled ;
