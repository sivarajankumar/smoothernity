namespace shy_guts
{
    namespace logic_salutation_letters_meshes_creator_create_state
    {
        static so_called_common_logic_salutation_letters_meshes_creator_create_request_message msg_request ;
        static void on_request ( ) ;
    }

    namespace logic_salutation_letters_text_storage_letter_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_text_storage_letter ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_text_letter_mesh_create_state
    {
        static so_called_common_engine_taker_helper ( logic_text_letter_mesh_create ) taker ;
        static void on_reply ( ) ;
    }

    static void add_mesh_to_storage ( ) ;
    static void reply_finish_of_creation ( ) ;
    static void request_letter_from_storage ( ) ;
    static void request_mesh_creation ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_creator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_request ( )
{
    shy_guts :: request_letter_from_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_text_storage_letter_state :: on_reply ( )
{
    shy_guts :: request_mesh_creation ( ) ;
}

void shy_guts :: logic_text_letter_mesh_create_state :: on_reply ( )
{
    shy_guts :: add_mesh_to_storage ( ) ;
    shy_guts :: reply_finish_of_creation ( ) ;
}

void shy_guts :: request_letter_from_storage ( )
{
    so_called_platform_math_num_whole_type letter_index ;
    letter_index = shy_guts :: logic_salutation_letters_meshes_creator_create_state :: msg_request . letter_index ;

    shy_guts :: logic_salutation_letters_text_storage_letter_state :: taker . msg_request . letter_index = letter_index ;
    shy_guts :: logic_salutation_letters_text_storage_letter_state :: taker . request ( ) ;
}

void shy_guts :: request_mesh_creation ( )
{
    so_called_common_logic_text_letter_id_type letter ;

    letter = shy_guts :: logic_salutation_letters_text_storage_letter_state :: taker . msg_reply . letter_id ;

    so_called_common_logic_text_letter_mesh_create_request_message msg ;
    msg . letter = letter ;
    msg . size = so_called_common_logic_salutation_letters_meshes_consts :: mesh_size ;
    msg . color_r = so_called_common_logic_salutation_letters_meshes_consts :: color_r ;
    msg . color_g = so_called_common_logic_salutation_letters_meshes_consts :: color_g ;
    msg . color_b = so_called_common_logic_salutation_letters_meshes_consts :: color_b ;
    msg . color_a = so_called_common_logic_salutation_letters_meshes_consts :: color_a ;

    shy_guts :: logic_text_letter_mesh_create_state :: taker . msg_request = msg ;
    shy_guts :: logic_text_letter_mesh_create_state :: taker . request ( ) ;
}

void shy_guts :: add_mesh_to_storage ( )
{
    so_called_common_logic_salutation_letters_meshes_storage_add_mesh_message msg ;
    msg . mesh = shy_guts :: logic_text_letter_mesh_create_state :: taker . msg_reply . mesh ;
    so_called_common_logic_salutation_letters_meshes_storage_add_mesh_sender :: send ( msg ) ;
}

void shy_guts :: reply_finish_of_creation ( )
{
    so_called_common_logic_salutation_letters_meshes_creator_create_reply_message msg ;
    msg . letter_index = shy_guts :: logic_salutation_letters_meshes_creator_create_state :: msg_request . letter_index ;
    so_called_common_logic_salutation_letters_meshes_creator_create_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_salutation_letters_text_storage_letter_state :: taker . init ( ) ;
    shy_guts :: logic_text_letter_mesh_create_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_common_logic_salutation_letters_meshes_creator_create_request_message msg )
{
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: msg_request = msg ;
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_common_logic_salutation_letters_text_storage_letter_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_text_storage_letter_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_text_storage_letter_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: receive ( so_called_common_logic_text_letter_mesh_create_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_text_letter_mesh_create_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_text_letter_mesh_create_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_creator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
