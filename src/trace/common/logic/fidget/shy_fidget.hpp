namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "common_logic_fidget" ;
    }
}

void shy_trace_common_logic_fidget :: edges_out_of_range_error
    ( so_called_type_platform_math_num_whole edges 
    , so_called_type_platform_math_num_whole edges_min
    , so_called_type_platform_math_num_whole edges_max
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Edges count of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( edges ) ;
    so_called_platform_trace :: trace_string_error ( " is out of acceptable range from " ) ;
    so_called_platform_trace :: trace_num_whole_error ( edges_min ) ;
    so_called_platform_trace :: trace_string_error ( " to " ) ;
    so_called_platform_trace :: trace_num_whole_error ( edges_max ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}
