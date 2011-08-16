class _shy_common_logic_main_menu_letters_meshes_creator
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_cols_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_letter_reply ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_create_next ) ;
    static void receive ( so_called_message_common_logic_main_menu_letters_rows_reply ) ;
    static void receive ( so_called_message_common_logic_text_letter_mesh_create_reply ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler 
    :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creator > :: module 
    shy_common_logic_main_menu_letters_meshes_creator_scheduled ;
