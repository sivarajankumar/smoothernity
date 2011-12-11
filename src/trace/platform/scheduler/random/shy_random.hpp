namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_scheduler_random" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_scheduler_random :: messages_queue_size_exceeds_maximum_size_error
    ( so_called_lib_std_int32_t current
    , so_called_lib_std_int32_t total
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Messages queue size of " ) ;
        so_called_platform_trace :: trace_const_int_32_error ( current ) ;
        so_called_platform_trace :: trace_string_error ( " exceeds maximum messages count of " ) ;
        so_called_platform_trace :: trace_const_int_32_error ( total ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_platform_scheduler_random :: modules_exceed_maximum_count_error
    ( so_called_lib_std_int32_t total
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Modules with scheduling exceed maximum count of " ) ;
        so_called_platform_trace :: trace_const_int_32_error ( total ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
