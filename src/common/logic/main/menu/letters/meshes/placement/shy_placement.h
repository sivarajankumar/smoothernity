class _shy_common_logic_main_menu_letters_meshes_placement
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_animation_transform_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_count_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_mesh_id_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_mesh_row_col_reply_message ) ;
    static void receive ( so_called_common_logic_main_menu_letters_meshes_place_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_placement > :: module shy_common_logic_main_menu_letters_meshes_placement_scheduled ;
