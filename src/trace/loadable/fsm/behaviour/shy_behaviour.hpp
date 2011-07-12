namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "loadable_fsm_behaviour" ;
    }
}

void shy_trace_loadable_fsm_behaviour :: machine_state_action_command 
    ( const so_called_lib_std_char * machine 
    , const so_called_lib_std_char * state
    , const so_called_lib_std_char * command_name
    , const so_called_lib_std_char * command_machine
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Machine " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( machine ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " in state " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( state ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " issues command " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( command_name ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " to machine " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( command_machine ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_fsm_behaviour :: machine_state_action_discard
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    , const so_called_lib_std_char * input
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Machine " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( machine ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " in state " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( state ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " discards input " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( input ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_fsm_behaviour :: machine_state_action_do 
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    , const so_called_lib_std_char * action
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Machine " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( machine ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " in state " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( state ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " sends message " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( action ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_fsm_behaviour :: machine_state_on_entry
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Machine " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( machine ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " enters state " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( state ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_fsm_behaviour :: machine_state_on_exit
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Machine " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( machine ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " leaves state " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( state ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_fsm_behaviour :: machine_state_on_input
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Machine " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( machine ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( " handles input in state " ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string_name ( state ) ;
    so_called_platform_trace :: trace_string_name ( "\"" ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_fsm_behaviour :: tick_all_fsms ( )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "All machines do tick." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}
