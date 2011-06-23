namespace shy_guts
{
    namespace logic_salutation_letters_meshes_creator_create_state
    {
        static so_called_type_platform_math_num_whole letter_index ;
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_salutation_letters_text_storage_letter_state
    {
        static so_called_type_common_logic_text_letter_id letter_id ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_letter_index ;
    }

    static void proceed_with_creation ( ) ;
    static void request_letters_text_storage_letter ( ) ;
    static void send_create_reply ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_creator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_letters_text_storage_letter ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_text_storage_letter_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_text_storage_letter_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: send_create_reply ( ) ;
    }
}

void shy_guts :: request_letters_text_storage_letter ( )
{
    so_called_type_platform_math_num_whole letter_index ;
    letter_index = shy_guts :: logic_salutation_letters_meshes_creator_create_state :: letter_index ;

    shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested_letter_index = letter_index ;

    so_called_message_common_logic_salutation_letters_text_storage_letter_request msg ;
    msg . letter_index = letter_index ;
    so_called_sender_common_logic_salutation_letters_text_storage_letter_request :: send ( msg ) ;
}

void shy_guts :: send_create_reply ( )
{
    so_called_message_common_logic_salutation_letters_meshes_creator_create_reply msg ;
    msg . letter_index = shy_guts :: logic_salutation_letters_meshes_creator_create_state :: letter_index ;
    so_called_sender_common_logic_salutation_letters_meshes_creator_create_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_text_storage_letter_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_message_common_logic_salutation_letters_meshes_creator_create_request msg )
{
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: letter_index = msg . letter_index ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_message_common_logic_salutation_letters_text_storage_letter_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested_letter_index , msg . letter_index )
       )
    {
        shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_text_storage_letter_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_salutation_letters_text_storage_letter_state :: letter_id = msg . letter_id ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_creator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
