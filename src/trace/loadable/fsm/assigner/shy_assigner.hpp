namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "loadable_fsm_assigner" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_loadable_fsm_assigner :: no_initial_state_in_machine_of_system_error
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * system 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. No state " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_fsm_consts :: state_initial . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " in machine " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( machine ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of FSM system " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( system ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
