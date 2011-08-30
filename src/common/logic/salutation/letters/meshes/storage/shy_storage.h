class _shy_common_logic_salutation_letters_meshes_storage
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_storage_add_mesh_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_storage_clean_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_storage_mesh_request_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_storage_size_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context
    < _shy_common_logic_salutation_letters_meshes_storage 
    > :: module
    shy_common_logic_salutation_letters_meshes_storage_scheduled ;
