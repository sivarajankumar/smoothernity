class _shy_common_logic_salutation_letters_meshes_generator
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_generator_generate_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_generator_update_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_meshes_creator_create_reply_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_text_storage_size_reply_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_meshes_generator 
    > :: module 
    shy_common_logic_salutation_letters_meshes_generator_scheduled ;
