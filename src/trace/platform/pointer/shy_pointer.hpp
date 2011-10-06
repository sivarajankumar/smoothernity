namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_pointer" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_pointer :: _check_data_uninitialized ( so_called_lib_std_bool uninitialized )
{
    if ( shy_guts :: consts :: trace_enabled && uninitialized )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Uninitialized pointer value." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
