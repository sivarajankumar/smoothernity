class _shy_common_logic_text_letter_mesh
{
public :
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_text_letter_mesh_create_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler 
    :: scheduled_context < _shy_common_logic_text_letter_mesh > :: module 
    shy_common_logic_text_letter_mesh_scheduled ;
