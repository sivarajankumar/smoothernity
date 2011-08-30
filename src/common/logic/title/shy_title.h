class _shy_common_logic_title
{
public :
    static void receive ( so_called_common_engine_render_aspect_reply_message ) ;
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_core_use_ortho_projection_reply_message ) ;
    static void receive ( so_called_common_logic_fidget_render_reply_message ) ;
    static void receive ( so_called_common_logic_text_letter_big_tex_coords_reply_message ) ;
    static void receive ( so_called_common_logic_text_use_text_texture_reply_message ) ;
    static void receive ( so_called_common_logic_title_launch_permit_message ) ;
    static void receive ( so_called_common_logic_title_render_message ) ;
    static void receive ( so_called_common_logic_title_update_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_title > :: module shy_common_logic_title_scheduled ;
