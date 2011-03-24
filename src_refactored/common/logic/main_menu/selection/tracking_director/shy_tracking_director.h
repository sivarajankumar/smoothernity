class _shy_common_logic_main_menu_selection_tracking_director
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_appear_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_select_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_animation_unselect_finished ) ;
    static void receive ( so_called_message_common_logic_main_menu_selection_track_reply ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_tracking_director > :: module
    shy_common_logic_main_menu_selection_tracking_director_scheduled ;
