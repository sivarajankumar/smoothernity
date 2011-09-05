class _shy_common_logic_salutation_letters_animation_layout
{
public :
    static void receive ( so_called_common_engine_render_aspect_reply_message ) ;
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_animation_layout_transform_request_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_storage_size_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_animation_layout 
    > :: module 
    shy_common_logic_salutation_letters_animation_layout_scheduled ;
