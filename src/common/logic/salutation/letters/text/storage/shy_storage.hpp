namespace shy_guts
{
    class entry_type
    {
    public :
        so_called_common_logic_text_letter_id_type letter ;
    } ;

    static so_called_platform_static_array_data_type < entry_type , so_called_common_logic_salutation_letters_consts :: max_letters_int > entries_data ;
    static so_called_platform_math_num_whole_type entries_count ;

    static void trace_entries_in_use ( ) ;
    static void trace_entries_overflow_error ( ) ;
    static void trace_entry_index_is_out_of_range_error ( so_called_platform_math_num_whole_type ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_text_storage > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: trace_entries_in_use ( )
{
    so_called_trace
        ( so_called_trace_common_logic_salutation_letters_text_storage :: entries_in_use
            ( shy_guts :: entries_count
            , so_called_common_logic_salutation_letters_consts :: max_letters
            )
        ) ;
}

void shy_guts :: trace_entries_overflow_error ( )
{
    so_called_trace ( so_called_trace_common_logic_salutation_letters_text_storage :: entries_overflow_error ( ) ) ;
}

void shy_guts :: trace_entry_index_is_out_of_range_error ( so_called_platform_math_num_whole_type index )
{
    so_called_trace
        ( so_called_trace_common_logic_salutation_letters_text_storage :: entry_index_is_out_of_range_error
            ( index
            , shy_guts :: entries_count
            )
        ) ;
}

void _shy_common_logic_salutation_letters_text_storage :: receive ( so_called_common_init_message )
{
    shy_guts :: entries_count = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_salutation_letters_text_storage :: receive ( so_called_common_logic_salutation_letters_text_storage_add_letter_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: entries_count , so_called_common_logic_salutation_letters_consts :: max_letters ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: entry_type > entry ;
        so_called_platform_static_array :: element_ptr ( entry , shy_guts :: entries_data , shy_guts :: entries_count ) ;
        entry . get ( ) . letter = msg . letter ;
        so_called_platform_math :: inc_whole ( shy_guts :: entries_count ) ;
        shy_guts :: trace_entries_in_use ( ) ;
    }
    else
        shy_guts :: trace_entries_overflow_error ( ) ;
}

void _shy_common_logic_salutation_letters_text_storage :: receive ( so_called_common_logic_salutation_letters_text_storage_clean_message )
{
    shy_guts :: entries_count = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: trace_entries_in_use ( ) ;
}

void _shy_common_logic_salutation_letters_text_storage :: receive ( so_called_common_logic_salutation_letters_text_storage_letter_request_message msg )
{
    so_called_common_logic_text_letter_id_type letter_id ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . letter_index , shy_guts :: entries_count ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: entry_type > entry ;
        so_called_platform_static_array :: element_ptr ( entry , shy_guts :: entries_data , msg . letter_index ) ;
        letter_id = entry . get ( ) . letter ;
    }
    else
    {
        letter_id = so_called_common_logic_text_consts :: whitespace ;
        shy_guts :: trace_entry_index_is_out_of_range_error ( msg . letter_index ) ;
    }

    so_called_common_logic_salutation_letters_text_storage_letter_reply_message reply_msg ;
    reply_msg . letter_index = msg . letter_index ;
    reply_msg . letter_id = letter_id ;
    so_called_common_logic_salutation_letters_text_storage_letter_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_salutation_letters_text_storage :: receive ( so_called_common_logic_salutation_letters_text_storage_size_request_message )
{
    so_called_common_logic_salutation_letters_text_storage_size_reply_message msg ;
    msg . size = shy_guts :: entries_count ;
    so_called_common_logic_salutation_letters_text_storage_size_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_text_storage :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
