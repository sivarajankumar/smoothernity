class _shy_common_logic_salutation_letters_text_storage
{
public :
    static void receive ( so_called_message_common_init ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_text_storage_add_letter ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_text_storage_clean ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_text_storage_letter_request ) ;
    static void receive ( so_called_message_common_logic_salutation_letters_text_storage_size_request ) ;
    static void register_in_scheduler ( ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context 
    < _shy_common_logic_salutation_letters_text_storage 
    > :: module
    shy_common_logic_salutation_letters_text_storage_scheduled ;
