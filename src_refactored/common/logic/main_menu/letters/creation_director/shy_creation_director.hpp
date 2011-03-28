namespace shy_guts
{
    static void add_letter ( so_called_type_common_logic_text_letter_id ) ;
    static void next_row ( ) ;
    static void text_create_finished ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_creation_director > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: add_letter ( so_called_type_common_logic_text_letter_id )
{
}

void shy_guts :: next_row ( )
{
}

void shy_guts :: text_create_finished ( )
{
}

void _shy_common_logic_main_menu_letters_creation_director :: receive ( so_called_message_common_logic_main_menu_letters_create )
{
}
