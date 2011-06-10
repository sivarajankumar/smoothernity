namespace shy_guts
{
    static void add_letter ( so_called_type_common_logic_text_letter_id ) ;
    static void finish ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_text_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: add_letter ( so_called_type_common_logic_text_letter_id )
{
}

void shy_guts :: finish ( )
{
    so_called_sender_common_logic_salutation_letters_text_generator_generate_finished :: send ( so_called_message_common_logic_salutation_letters_text_generator_generate_finished ( ) ) ;
}

void _shy_common_logic_salutation_letters_text_generator :: receive ( so_called_message_common_logic_salutation_letters_text_generator_generate )
{
    typedef so_called_common_logic_text_consts :: alphabet_english eng ;
    shy_guts :: add_letter ( eng :: S ) ;
    shy_guts :: add_letter ( eng :: M ) ;
    shy_guts :: add_letter ( eng :: O ) ;
    shy_guts :: add_letter ( eng :: O ) ;
    shy_guts :: add_letter ( eng :: T ) ;
    shy_guts :: add_letter ( eng :: H ) ;
    shy_guts :: add_letter ( eng :: E ) ;
    shy_guts :: add_letter ( eng :: R ) ;
    shy_guts :: add_letter ( eng :: N ) ;
    shy_guts :: add_letter ( eng :: I ) ;
    shy_guts :: add_letter ( eng :: T ) ;
    shy_guts :: add_letter ( eng :: Y ) ;
    shy_guts :: finish ( ) ;
}

void _shy_common_logic_salutation_letters_text_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
