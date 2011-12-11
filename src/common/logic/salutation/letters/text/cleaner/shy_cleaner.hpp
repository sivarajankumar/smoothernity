namespace shy_guts
{
    static void send_clean_storage ( ) ;
    static void send_clean_finished ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_text_cleaner > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: send_clean_storage ( )
{
    so_called_common_logic_salutation_letters_text_storage_clean_sender :: send ( so_called_common_logic_salutation_letters_text_storage_clean_message ( ) ) ;
}

void shy_guts :: send_clean_finished ( )
{
    so_called_common_logic_salutation_letters_text_cleaner_clean_finished_sender :: send ( so_called_common_logic_salutation_letters_text_cleaner_clean_finished_message ( ) ) ;
}

void _shy_common_logic_salutation_letters_text_cleaner :: receive ( so_called_common_logic_salutation_letters_text_cleaner_clean_message )
{
    shy_guts :: send_clean_storage ( ) ;
    shy_guts :: send_clean_finished ( ) ;
}

void _shy_common_logic_salutation_letters_text_cleaner :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
