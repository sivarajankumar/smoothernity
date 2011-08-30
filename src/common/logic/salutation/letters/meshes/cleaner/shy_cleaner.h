class _shy_common_logic_salutation_letters_meshes_cleaner
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_cleaner_clean_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_cleaner_update_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_storage_mesh_reply_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_storage_size_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_meshes_cleaner 
    > :: module 
    shy_common_logic_salutation_letters_meshes_cleaner_scheduled ;
