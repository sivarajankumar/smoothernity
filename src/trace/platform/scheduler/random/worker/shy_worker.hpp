namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_scheduler_random" ;
    }
}

void shy_trace_platform_scheduler_random_worker :: messages_queue_size_exceeds_maximum_size_error
    ( so_called_lib_std_int32_t current
    , so_called_lib_std_int32_t total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Messages queue size of " ) ;
    so_called_platform_trace :: trace_const_int_32_error ( current ) ;
    so_called_platform_trace :: trace_string_error ( " exceeds maximum messages count of " ) ;
    so_called_platform_trace :: trace_const_int_32_error ( total ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}
