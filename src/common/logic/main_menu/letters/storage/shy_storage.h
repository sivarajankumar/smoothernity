class _shy_common_logic_main_menu_letters_storage
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_boundaries_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_cols_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_letter_add ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_letter_request ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_next_row ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_rows_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_storage > :: module shy_common_logic_main_menu_letters_storage_scheduled ;