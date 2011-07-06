namespace shy_guts
{
    namespace logic_salutation_letters_meshes_cleaner_clean_state
    {
        static so_called_type_platform_math_num_whole letter_current ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_meshes_cleaner_work
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

    static void send_clean_finished ( ) ;
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_cleaner_work :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_cleaner_work :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_cleaner_work :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: on_requested ( )
{
    shy_guts :: send_clean_finished ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_cleaner_work :: on_requested ( )
{
}

void shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_replied ( )
{
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( )
{
}

void shy_guts :: send_clean_finished ( )
{
    so_called_sender_common_logic_salutation_letters_meshes_cleaner_clean_finished :: send ( so_called_message_common_logic_salutation_letters_meshes_cleaner_clean_finished ( ) ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_cleaner_work :: enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_cleaner_work :: requested = so_called_platform_math_consts :: whole_false ;
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
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_reply )
{
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
