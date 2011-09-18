class _shy_common_logic_salutation_letters_text_storage
{
public :
    static void receive ( so_called_common_init_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_text_storage_add_letter_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_text_storage_clean_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_text_storage_letter_request_message ) ;
    static void receive ( so_called_common_logic_salutation_letters_text_storage_size_request_message ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_text_storage 
    > :: module
    shy_common_logic_salutation_letters_text_storage_scheduled ;
