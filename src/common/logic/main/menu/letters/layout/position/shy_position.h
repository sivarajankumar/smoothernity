class _shy_common_logic_main_menu_letters_layout_position
{
public :
    static void receive ( so_called_common_engine_render_aspect_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_boundaries_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_cols_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_layout_position_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_layout_position > :: module 
    shy_common_logic_main_menu_letters_layout_position_scheduled ;
