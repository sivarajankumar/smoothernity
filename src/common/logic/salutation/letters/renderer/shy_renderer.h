class _shy_common_logic_salutation_letters_renderer
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_animation_transform_reply ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_meshes_storage_mesh_reply ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_reply ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_renderer_render_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_renderer 
    > :: module 
    shy_common_logic_salutation_letters_renderer_scheduled ;
