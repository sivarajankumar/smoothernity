class _shy_common_logic_main_menu_letters_layout_row_rect
{
public :
    static void receive ( so_called_common_engine_render_aspect_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_boundaries_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_layout_row_rect_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_layout_row_rect > :: module 
    shy_common_logic_main_menu_letters_layout_row_rect_scheduled ;
