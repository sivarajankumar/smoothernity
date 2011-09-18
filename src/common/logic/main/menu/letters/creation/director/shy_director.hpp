namespace shy_guts
{
    static void add_letter ( so_called_common_logic_text_letter_id_type ) ;
    static void next_row ( ) ;
    static void text_create_finished ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_creation_director > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: add_letter ( so_called_common_logic_text_letter_id_type letter )
{
    so_called_common_logic_main_menu_letters_letter_add_message msg ;
    msg . letter = letter ;
    so_called_common_logic_main_menu_letters_letter_add_sender :: send ( msg ) ;
}

void shy_guts :: next_row ( )
{
    so_called_common_logic_main_menu_letters_next_row_sender :: send ( so_called_common_logic_main_menu_letters_next_row_message ( ) ) ;
}

void shy_guts :: text_create_finished ( )
{
    so_called_common_logic_main_menu_letters_create_finished_sender :: send ( so_called_common_logic_main_menu_letters_create_finished_message ( ) ) ;
}

void _shy_common_logic_main_menu_letters_creation_director :: receive ( so_called_common_logic_main_menu_letters_create_message )
{
    typedef so_called_common_logic_text_consts :: alphabet_english eng ;
    so_called_common_logic_text_letter_id_type whitespace = so_called_common_logic_text_consts :: whitespace ;

    shy_guts :: add_letter ( eng :: N ) ;
    shy_guts :: add_letter ( eng :: E ) ;
    shy_guts :: add_letter ( eng :: W ) ;
    shy_guts :: add_letter ( whitespace ) ;
    shy_guts :: add_letter ( eng :: G ) ;
    shy_guts :: add_letter ( eng :: A ) ;
    shy_guts :: add_letter ( eng :: M ) ;
    shy_guts :: add_letter ( eng :: E ) ;
    
    shy_guts :: next_row ( ) ;
    shy_guts :: add_letter ( eng :: L ) ;
    shy_guts :: add_letter ( eng :: O ) ;
    shy_guts :: add_letter ( eng :: A ) ;
    shy_guts :: add_letter ( eng :: D ) ;
    shy_guts :: add_letter ( whitespace ) ;
    shy_guts :: add_letter ( eng :: G ) ;
    shy_guts :: add_letter ( eng :: A ) ;
    shy_guts :: add_letter ( eng :: M ) ;
    shy_guts :: add_letter ( eng :: E ) ;

    shy_guts :: next_row ( ) ;
    shy_guts :: add_letter ( eng :: O ) ;
    shy_guts :: add_letter ( eng :: P ) ;
    shy_guts :: add_letter ( eng :: T ) ;
    shy_guts :: add_letter ( eng :: I ) ;
    shy_guts :: add_letter ( eng :: O ) ;
    shy_guts :: add_letter ( eng :: N ) ;
    shy_guts :: add_letter ( eng :: S ) ;

    shy_guts :: next_row ( ) ;
    shy_guts :: add_letter ( eng :: E ) ;
    shy_guts :: add_letter ( eng :: X ) ;
    shy_guts :: add_letter ( eng :: I ) ;
    shy_guts :: add_letter ( eng :: T ) ;
    
    shy_guts :: text_create_finished ( ) ;
}

void _shy_common_logic_main_menu_letters_creation_director :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
