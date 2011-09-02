class _shy_common_logic_main_menu_letters_storage
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_boundaries_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_cols_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_letter_add_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_letter_request_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_next_row_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_rows_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_storage > :: module shy_common_logic_main_menu_letters_storage_scheduled ;
