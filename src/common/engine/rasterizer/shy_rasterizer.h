class _shy_common_engine_rasterizer
{
public :
    static void receive ( so_called_message_common_engine_rasterizer_draw_ellipse_in_rect ) ;
    static void receive ( so_called_message_common_engine_rasterizer_draw_rect ) ;
    static void receive ( so_called_message_common_engine_rasterizer_draw_triangle ) ;
    static void receive ( so_called_message_common_engine_rasterizer_finalize_request ) ;
    static void receive ( so_called_message_common_engine_rasterizer_use_texel ) ;
    static void receive ( so_called_message_common_engine_rasterizer_use_texture ) ;
    static void receive ( so_called_message_common_init ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_engine_rasterizer 
    , so_called_common_engine_rasterizer_consts :: max_messages 
    > :: module
    shy_common_engine_rasterizer_scheduled ;  
