class _shy_common_logic_salutation_renderer
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_ortho_planes_reply ) ;
    static void receive ( so_called_message_common_logic_salutation_animation_transform_reply ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_renderer_render_reply ) ;
    static void receive ( so_called_message_common_logic_salutation_renderer_render ) ;
    static void receive ( so_called_message_common_logic_text_use_text_texture_reply ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_renderer 
    > :: module 
    shy_common_logic_salutation_renderer_scheduled ;
