namespace shy_guts
{
    namespace logic_salutation_letters_renderer_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_size_state
    {
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole size ;
        static void on_replied ( ) ;
    }

    static void request_meshes_amount_in_storage ( ) ;
    static void work ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: work ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_renderer_render_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_renderer_render_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_renderer_render_state :: on_requested ( )
{
    shy_guts :: request_meshes_amount_in_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( )
{
}

void shy_guts :: request_meshes_amount_in_storage ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_size_request :: send
        ( so_called_message_common_logic_salutation_letters_meshes_storage_size_request ( )
        ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested = so_called_platform_math_consts  :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied = so_called_platform_math_consts  :: whole_true ;
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: size = msg . size ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_logic_salutation_letters_renderer_render )
{
    shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: work ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
