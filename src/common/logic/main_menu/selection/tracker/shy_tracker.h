class _shy_common_logic_main_menu_selection_tracker
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_controls_state_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_layout_row_rect_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_rows_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_track_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_tracker > :: module shy_common_logic_main_menu_selection_tracker_scheduled ;
