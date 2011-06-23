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

    namespace logic_text_letter_mesh_create_state
    {
        static so_called_type_common_engine_render_mesh_id mesh ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_common_logic_text_letter_id requested_letter ;
    }

    static void proceed_with_creation ( ) ;
    static void request_letters_text_storage_letter ( ) ;
    static void request_text_letter_mesh_create ( ) ;
    static void replied_text_letter_mesh_create ( ) ;
    static void reply_create ( ) ;
    static void send_storage_add_mesh ( ) ;
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
        shy_guts :: request_text_letter_mesh_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_mesh_create_state :: replied ) )
    {
        shy_guts :: logic_text_letter_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: replied_text_letter_mesh_create ( ) ;
    }
}

void shy_guts :: request_text_letter_mesh_create ( )
{
    so_called_type_common_logic_text_letter_id letter ;

    letter = shy_guts :: logic_salutation_letters_text_storage_letter_state :: letter_id ;

    shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_text_letter_mesh_create_state :: requested_letter = letter ;

    so_called_message_common_logic_text_letter_mesh_create_request msg ;
    msg . letter = letter ;
    msg . size = so_called_common_logic_salutation_letters_meshes_consts :: mesh_size ;
    msg . color_r = so_called_common_logic_salutation_letters_meshes_consts :: color_r ;
    msg . color_g = so_called_common_logic_salutation_letters_meshes_consts :: color_g ;
    msg . color_b = so_called_common_logic_salutation_letters_meshes_consts :: color_b ;
    msg . color_a = so_called_common_logic_salutation_letters_meshes_consts :: color_a ;
    so_called_sender_common_logic_text_letter_mesh_create_request :: send ( msg ) ;
}

void shy_guts :: replied_text_letter_mesh_create ( )
{
    shy_guts :: send_storage_add_mesh ( ) ;
    shy_guts :: reply_create ( ) ;
}

void shy_guts :: send_storage_add_mesh ( )
{
    so_called_message_common_logic_salutation_letters_meshes_storage_add_mesh msg ;
    msg . mesh = shy_guts :: logic_text_letter_mesh_create_state :: mesh ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_add_mesh :: send ( msg ) ;
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

void shy_guts :: reply_create ( )
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
    shy_guts :: logic_text_letter_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
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

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_message_common_logic_text_letter_mesh_create_reply msg )
{
    so_called_type_platform_math_num_whole letters_are_equal ;
    so_called_common_logic_text_stateless :: are_letters_equal ( letters_are_equal , shy_guts :: logic_text_letter_mesh_create_state :: requested_letter , msg . letter ) ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_mesh_create_state :: requested ) 
      && so_called_platform_conditions :: whole_is_true ( letters_are_equal )
       )
    {
        shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_text_letter_mesh_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_text_letter_mesh_create_state :: mesh = msg . mesh ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_creator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
