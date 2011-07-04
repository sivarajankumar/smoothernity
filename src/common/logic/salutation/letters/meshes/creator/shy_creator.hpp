namespace shy_guts
{
    namespace logic_salutation_letters_meshes_creator_create_state
    {
        static so_called_type_platform_math_num_whole letter_index ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_text_storage_letter_state
    {
        static so_called_type_common_logic_text_letter_id letter_id ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_letter_index ;
        static void on_replied ( ) ;
    }

    namespace logic_text_letter_mesh_create_state
    {
        static so_called_type_common_engine_render_mesh_id mesh ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_common_logic_text_letter_id requested_letter ;
        static void on_replied ( ) ;
    }

    static void add_mesh_to_storage ( ) ;
    static void reply_finish_of_creation ( ) ;
    static void request_letter_from_storage ( ) ;
    static void request_mesh_creation ( ) ;
    static void update_state ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_creator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: update_state ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_text_storage_letter_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_text_storage_letter_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_text_storage_letter_state :: on_replied ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_mesh_create_state :: replied ) )
    {
        shy_guts :: logic_text_letter_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_text_letter_mesh_create_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_requested ( )
{
    shy_guts :: request_letter_from_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_text_storage_letter_state :: on_replied ( )
{
    shy_guts :: request_mesh_creation ( ) ;
}

void shy_guts :: logic_text_letter_mesh_create_state :: on_replied ( )
{
    shy_guts :: add_mesh_to_storage ( ) ;
    shy_guts :: reply_finish_of_creation ( ) ;
}

void shy_guts :: request_letter_from_storage ( )
{
    so_called_type_platform_math_num_whole letter_index ;
    letter_index = shy_guts :: logic_salutation_letters_meshes_creator_create_state :: letter_index ;

    shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_text_storage_letter_state :: requested_letter_index = letter_index ;

    so_called_message_common_logic_salutation_letters_text_storage_letter_request msg ;
    msg . letter_index = letter_index ;
    so_called_sender_common_logic_salutation_letters_text_storage_letter_request :: send ( msg ) ;
}

void shy_guts :: request_mesh_creation ( )
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

void shy_guts :: add_mesh_to_storage ( )
{
    so_called_message_common_logic_salutation_letters_meshes_storage_add_mesh msg ;
    msg . mesh = shy_guts :: logic_text_letter_mesh_create_state :: mesh ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_add_mesh :: send ( msg ) ;
}

void shy_guts :: reply_finish_of_creation ( )
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
    shy_guts :: update_state ( ) ;
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
        shy_guts :: update_state ( ) ;
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
        shy_guts :: update_state ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_creator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
