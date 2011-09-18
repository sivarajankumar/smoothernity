class _shy_common_logic_text
{
public :
    static void receive ( so_called_common_engine_rasterizer_finalize_reply_message ) ;
    static void receive ( so_called_common_engine_render_mesh_create_reply_message ) ;
    static void receive ( so_called_common_engine_render_texture_create_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_text_letter_big_tex_coords_request_message ) ;
    static void receive ( so_called_common_logic_text_letter_small_tex_coords_request_message ) ;
    static void receive ( so_called_common_logic_text_prepare_permit_message ) ;
    static void receive ( so_called_common_logic_text_render_request_message ) ;
    static void receive ( so_called_common_logic_text_update_message ) ;
    static void receive ( so_called_common_logic_text_use_text_texture_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_text > :: module shy_common_logic_text_scheduled ;
