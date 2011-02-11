class _shy_common_logic_text
{
public :
    static void receive ( so_called_message_common_engine_rasterizer_finalize_reply ) ;
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
    static void receive ( so_called_message_common_engine_render_texture_create_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_text_letter_big_tex_coords_request ) ;
    static void receive ( so_called_message_common_logic_text_letter_small_tex_coords_request ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_text > :: module shy_common_logic_text_scheduled ;
