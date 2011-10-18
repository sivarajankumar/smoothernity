namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_vector" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_vector :: check_data_uninitialized ( so_called_platform_vector_data_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_vector_insider :: data_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized vector value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_vector :: check_zero_length ( so_called_platform_vector_data_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_float x = 0 ;
        so_called_lib_std_float y = 0 ;
        so_called_lib_std_float z = 0 ;
        so_called_platform_vector_insider :: x_get ( x , value ) ;
        so_called_platform_vector_insider :: y_get ( y , value ) ;
        so_called_platform_vector_insider :: z_get ( z , value ) ;
        if ( x == so_called_lib_std_float ( 0 ) && y == so_called_lib_std_float ( 0 ) && z == so_called_lib_std_float ( 0 ) )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Zero length vector." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}
