class _shy_common_logic_main_menu_letters_meshes_creator
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_cols_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_letter_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_mesh_create_next_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_rows_reply_message ) ;
    static void receive ( so_called_common_logic_text_letter_mesh_create_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler 
    :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creator > :: module 
    shy_common_logic_main_menu_letters_meshes_creator_scheduled ;
