namespace shy_guts
{
    namespace logic_salutation_letters_meshes_cleaner_clean_state
    {
        static so_called_platform_math_num_whole_type mesh_current ;
        static void on_request ( ) ;
    }

    namespace logic_salutation_letters_meshes_cleaner_update
    {
        static so_called_platform_math_num_whole_type enabled ;
        static so_called_platform_math_num_fract_type time ;
        static void on_request ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_mesh_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_storage_mesh ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_size_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_storage_size ) taker ;
        static void on_reply ( ) ;
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
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_cleaner > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: on_request ( )
{
    shy_guts :: request_meshes_amount_in_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_cleaner_update :: on_request ( )
{
    shy_guts :: advance_time ( ) ;
    shy_guts :: clean_by_time ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_reply ( )
{
    shy_guts :: clean_replied_mesh ( ) ;
    shy_guts :: clean_by_time ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_reply ( )
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
    so_called_common_engine_render_mesh_delete_message msg ;
    msg . mesh = shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . msg_reply . mesh ;
    so_called_common_engine_render_mesh_delete_sender :: send ( msg ) ;
}

void shy_guts :: clean_meshes_storage ( )
{
    so_called_common_logic_salutation_letters_meshes_storage_clean_sender :: send ( so_called_common_logic_salutation_letters_meshes_storage_clean_message ( ) ) ;
}

void shy_guts :: clean_by_time ( )
{
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type time_to_clean ;

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
    so_called_platform_math_num_whole_type mesh_current ;
    so_called_platform_math_num_whole_type meshes_total ;

    mesh_current = shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: mesh_current ;
    meshes_total = shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . msg_reply . size ;

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
    so_called_platform_math_num_whole_type mesh_index ;
    mesh_index = shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: mesh_current ;

    so_called_platform_math :: inc_whole
        ( shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: mesh_current
        ) ;

    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . msg_request . index = mesh_index ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . request ( ) ;
}

void shy_guts :: advance_time ( )
{
    so_called_common_engine_math_stateless :: add_frame_to_time
        ( shy_guts :: logic_salutation_letters_meshes_cleaner_update :: time
        ) ;
}

void shy_guts :: send_clean_finished ( )
{
    so_called_common_logic_salutation_letters_meshes_cleaner_clean_finished_sender :: send ( so_called_common_logic_salutation_letters_meshes_cleaner_clean_finished_message ( ) ) ;
}

void shy_guts :: request_meshes_amount_in_storage ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . request ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_salutation_letters_meshes_cleaner_update :: enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_common_logic_salutation_letters_meshes_cleaner_clean_message )
{
    shy_guts :: logic_salutation_letters_meshes_cleaner_clean_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_common_logic_salutation_letters_meshes_cleaner_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_cleaner_update :: enabled ) )
        shy_guts :: logic_salutation_letters_meshes_cleaner_update :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_common_logic_salutation_letters_meshes_storage_mesh_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: receive ( so_called_common_logic_salutation_letters_meshes_storage_size_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_cleaner :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
