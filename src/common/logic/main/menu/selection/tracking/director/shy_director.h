class _shy_common_logic_main_menu_selection_tracking_director
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_appear_finished_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_select_finished_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_animation_unselect_finished_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_track_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_track_row_selected_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_track_void_selected_message ) ;
    static void receive ( so_called_common_logic_main_menu_selection_tracking_director_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_tracking_director > :: module
    shy_common_logic_main_menu_selection_tracking_director_scheduled ;
