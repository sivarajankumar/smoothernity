class _shy_common_engine_rasterizer
{
public :
    static void receive ( so_called_common_engine_rasterizer_draw_ellipse_in_rect_message ) ;
    static void receive ( so_called_common_engine_rasterizer_draw_rect_message ) ;
    static void receive ( so_called_common_engine_rasterizer_draw_triangle_message ) ;
    static void receive ( so_called_common_engine_rasterizer_finalize_request_message ) ;
    static void receive ( so_called_common_engine_rasterizer_use_texel_message ) ;
    static void receive ( so_called_common_engine_rasterizer_use_texture_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_engine_rasterizer 
    , so_called_common_engine_rasterizer_consts :: max_messages 
    > :: module
    shy_common_engine_rasterizer_scheduled ;  
