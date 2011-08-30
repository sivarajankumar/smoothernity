class _shy_common_logic_text_letter_mesh
{
public :
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_text_letter_big_tex_coords_reply_message ) ;
    static void receive ( so_called_common_logic_text_letter_mesh_create_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler 
    :: scheduled_context < _shy_common_logic_text_letter_mesh > :: module 
    shy_common_logic_text_letter_mesh_scheduled ;
