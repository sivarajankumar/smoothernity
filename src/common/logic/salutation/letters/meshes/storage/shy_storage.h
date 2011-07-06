class _shy_common_logic_salutation_letters_meshes_storage
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_meshes_storage_add_mesh ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_meshes_storage_mesh_request ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context
    < _shy_common_logic_salutation_letters_meshes_storage 
    > :: module
    shy_common_logic_salutation_letters_meshes_storage_scheduled ;
