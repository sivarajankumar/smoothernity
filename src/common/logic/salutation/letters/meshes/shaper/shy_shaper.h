class _shy_common_logic_salutation_letters_meshes_shaper
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_meshes_shaper_shape_request ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_text_storage_letter_reply ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_meshes_shaper 
    > :: module 
    shy_common_logic_salutation_letters_meshes_shaper_scheduled ;