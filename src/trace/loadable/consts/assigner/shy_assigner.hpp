namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "loadable_consts_assigner" ;
    }
}

void shy_trace_loadable_consts_assigner :: no_value_assigned_to_module_attribute_fract_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute 
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. No value has been assigned to fract attribute " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( attribute ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " of module " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( module ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_consts_assigner :: no_value_assigned_to_module_attribute_whole_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute 
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. No value has been assigned to whole attribute " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( attribute ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " of module " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( module ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}
