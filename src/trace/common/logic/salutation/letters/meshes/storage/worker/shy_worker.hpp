namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "common_logic_salutation_letters_meshes_storage" ;
    }
}

void shy_trace_common_logic_salutation_letters_meshes_storage_worker :: entries_in_use 
    ( so_called_type_platform_math_num_whole current 
    , so_called_type_platform_math_num_whole total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Entries in use: " ) ;
    so_called_platform_trace :: trace_num_whole ( current ) ;
    so_called_platform_trace :: trace_string ( " of " ) ;
    so_called_platform_trace :: trace_num_whole ( total ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_logic_salutation_letters_meshes_storage_worker :: entries_overflow_error ( )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Entries overflow error." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_logic_salutation_letters_meshes_storage_worker :: entry_index_is_out_of_range_error
    ( so_called_type_platform_math_num_whole index 
    , so_called_type_platform_math_num_whole max_index
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Entry index " ) ;
    so_called_platform_trace :: trace_num_whole ( index ) ;
    so_called_platform_trace :: trace_string ( " exceeds container size of " ) ;
    so_called_platform_trace :: trace_num_whole ( max_index ) ;
    so_called_platform_trace :: trace_string ( " elements error." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}
