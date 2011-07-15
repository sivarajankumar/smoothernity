namespace shy_guts
{
    namespace logic_salutation_letters_meshes_cleaner_clean_state
    {
        static so_called_type_platform_math_num_whole mesh_current ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_meshes_cleaner_update
    {
        static so_called_type_platform_math_num_whole enabled ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_fract time ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_mesh_state
    {
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_index ;
        static so_called_type_common_engine_render_mesh_id mesh ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_size_state
    {
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole size ;
        static void on_replied ( ) ;
    }

    static void advance_time ( ) ;
    static void clean ( ) ;
    static void clean_by_time ( ) ;
    static void clean_meshes_storage ( ) ;
    static void clean_next_mesh ( ) ;
    static void clean_replied_mesh ( ) ;
    static void request_meshes_amount_in_storage ( ) ;
    static void send_clean_finished ( ) ;
    static void start_clean ( ) ;
    static void work ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_cleaner > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: work ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_cleaner_update :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_cleaner_update :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_cleaner_update :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: on_requested ( )
{
    shy_guts :: request_meshes_amount_in_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_cleaner_update :: on_requested ( )
{
    shy_guts :: advance_time ( ) ;
    shy_guts :: clean_by_time ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_replied ( )
{
    shy_guts :: clean_replied_mesh ( ) ;
    shy_guts :: clean_by_time ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( )
{
    shy_guts :: start_clean ( ) ;
}

void shy_guts :: start_clean ( )
{
    shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: mesh_current = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: logic_salutation_letters_meshes_cleaner_update :: enabled = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_meshes_cleaner_update :: time = so_called_platform_math_consts :: fract_0 ;
}

void shy_guts :: clean_replied_mesh ( )
{
    so_called_message_common_engine_render_mesh_delete msg ;
    msg . mesh = shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: mesh ;
    so_called_sender_common_engine_render_mesh_delete :: send ( msg ) ;
}

void shy_guts :: clean_meshes_storage ( )
{
    so_called_sender_common_logic_salutation_letters_meshes_storage_clean :: send ( so_called_message_common_logic_salutation_letters_meshes_storage_clean ( ) ) ;
}

void shy_guts :: clean_by_time ( )
{
    so_called_type_platform_math_num_fract time ;
    so_called_type_platform_math_num_fract time_to_clean ;

    time = shy_guts :: logic_salutation_letters_meshes_cleaner_update :: time ;
    time_to_clean = so_called_common_logic_salutation_letters_meshes_consts :: time_between_destruction ;

    if ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_to_clean ) )
    {
        so_called_platform_math :: sub_from_fract ( time , time_to_clean ) ;
        shy_guts :: logic_salutation_letters_meshes_cleaner_update :: time = time ;
        shy_guts :: clean ( ) ;
    }
}

void shy_guts :: clean ( )
{
    so_called_type_platform_math_num_whole mesh_current ;
    so_called_type_platform_math_num_whole meshes_total ;

    mesh_current = shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: mesh_current ;
    meshes_total = shy_guts :: logic_salutation_letters_meshes_storage_size_state :: size ;

    if ( so_called_platform_conditions :: whole_less_than_whole ( mesh_current , meshes_total ) )
        shy_guts :: clean_next_mesh ( ) ;
    else
    {
        shy_guts :: clean_meshes_storage ( ) ;
        shy_guts :: send_clean_finished ( ) ;
    }
}

void shy_guts :: clean_next_mesh ( )
{
    so_called_type_platform_math_num_whole mesh_index ;
    mesh_index = shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: mesh_current ;

    so_called_platform_math :: inc_whole
        ( shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: mesh_current
        ) ;

    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: requested_index = mesh_index ;

    so_called_message_common_logic_salutation_letters_meshes_storage_mesh_request msg ;
    msg . index = mesh_index ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_mesh_request :: send ( msg ) ;
}

void shy_guts :: advance_time ( )
{
    so_called_type_platform_math_num_fract time ;
    so_called_type_platform_math_num_fract time_step ;

    time = shy_guts :: logic_salutation_letters_meshes_cleaner_update :: time ;
    so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
    so_called_platform_math :: add_to_fract ( time , time_step ) ;

    shy_guts :: logic_salutation_letters_meshes_cleaner_update :: time = time ;
}

void shy_guts :: send_clean_finished ( )
{
    so_called_sender_common_logic_salutation_letters_meshes_cleaner_clean_finished :: send ( so_called_message_common_logic_salutation_letters_meshes_cleaner_clean_finished ( ) ) ;
}

void shy_guts :: request_meshes_amount_in_storage ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_size_request :: send
        ( so_called_message_common_logic_salutation_letters_meshes_storage_size_request ( )
        ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_cleaner_update :: enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_cleaner_update :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_message_common_logic_salutation_letters_meshes_cleaner_clean )
{
    shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: work ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_message_common_logic_salutation_letters_meshes_cleaner_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_cleaner_update :: enabled ) )
    {
        shy_guts :: logic_salutation_letters_meshes_cleaner_update :: requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_mesh_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: requested_index , msg . index )
       )
    {
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: mesh = msg . mesh ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: requested = so_called_platform_math_consts  :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: replied = so_called_platform_math_consts  :: whole_true ;
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: size = msg . size ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
