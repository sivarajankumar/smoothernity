namespace shy_guts
{
    class type_entry
    {
    public :
        so_called_type_common_engine_render_mesh_id mesh ;
    } ;

    namespace consts
    {
        static const so_called_type_platform_math_num_whole trace_enabled = so_called_platform_math_consts :: whole_true ;
    }

    static so_called_type_platform_static_array_data < type_entry , so_called_common_logic_salutation_letters_consts :: max_letters_int > entries_data ;
    static so_called_type_platform_math_num_whole entries_count ;

    static void trace_entries_in_use ( ) ;
    static void trace_entries_overflow_error ( ) ;
    static void trace_entry_index_is_out_of_range_error ( so_called_type_platform_math_num_whole ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_storage > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: trace_entries_in_use ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_trace
            ( so_called_trace_common_logic_salutation_letters_meshes_storage :: entries_in_use
                ( shy_guts :: entries_count
                , so_called_common_logic_salutation_letters_consts :: max_letters
                )
            ) ;
    }
}

void shy_guts :: trace_entries_overflow_error ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
        so_called_trace ( so_called_trace_common_logic_salutation_letters_meshes_storage :: entries_overflow_error ( ) ) ;
}

void shy_guts :: trace_entry_index_is_out_of_range_error ( so_called_type_platform_math_num_whole index )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_trace
            ( so_called_trace_common_logic_salutation_letters_meshes_storage :: entry_index_is_out_of_range_error
                ( index
                , shy_guts :: entries_count
                )
            ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_init )
{
    shy_guts :: entries_count = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_add_mesh msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: entries_count , so_called_common_logic_salutation_letters_consts :: max_letters ) )
    {
        so_called_type_platform_pointer_data < shy_guts :: type_entry > entry ;
        so_called_platform_static_array :: element_ptr ( entry , shy_guts :: entries_data , shy_guts :: entries_count ) ;
        entry . get ( ) . mesh = msg . mesh ;
        so_called_platform_math :: inc_whole ( shy_guts :: entries_count ) ;
        shy_guts :: trace_entries_in_use ( ) ;
    }
    else
        shy_guts :: trace_entries_overflow_error ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_clean )
{
    shy_guts :: entries_count = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: trace_entries_in_use ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_mesh_request msg )
{
    so_called_type_common_engine_render_mesh_id mesh ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . index , shy_guts :: entries_count ) )
    {
        so_called_type_platform_pointer_data < shy_guts :: type_entry > entry ;
        so_called_platform_static_array :: element_ptr ( entry , shy_guts :: entries_data , msg . index ) ;
        mesh = entry . get ( ) . mesh ;
    }
    else
    {
        mesh = so_called_common_engine_render_consts :: null_mesh ;
        shy_guts :: trace_entry_index_is_out_of_range_error ( msg . index ) ;
    }

    so_called_message_common_logic_salutation_letters_meshes_storage_mesh_reply reply_msg ;
    reply_msg . index = msg . index ;
    reply_msg . mesh = mesh ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_mesh_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_request )
{
    so_called_message_common_logic_salutation_letters_meshes_storage_size_reply msg ;
    msg . size = shy_guts :: entries_count ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_size_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
