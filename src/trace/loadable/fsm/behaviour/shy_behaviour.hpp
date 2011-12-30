namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "loadable_fsm_behaviour" ;
        static const so_called_lib_std_bool trace_action = so_called_lib_std_false ;
        static const so_called_lib_std_bool trace_entry = so_called_lib_std_true ;
        static const so_called_lib_std_bool trace_exit = so_called_lib_std_true ;
        static const so_called_lib_std_bool trace_input = so_called_lib_std_false ;
        static const so_called_lib_std_bool trace_tick = so_called_lib_std_false ;
    }
}

void shy_trace_loadable_fsm_behaviour :: machine_state_action_command 
    ( const so_called_lib_std_char * machine 
    , const so_called_lib_std_char * state
    , const so_called_lib_std_char * command_name
    , const so_called_lib_std_char * command_machine
    )
{
    if ( shy_guts :: consts :: trace_action )
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
}

void shy_trace_loadable_fsm_behaviour :: machine_state_action_discard
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    , const so_called_lib_std_char * input
    )
{
    if ( shy_guts :: consts :: trace_action )
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
}

void shy_trace_loadable_fsm_behaviour :: machine_state_action_do 
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    , const so_called_lib_std_char * action
    )
{
    if ( shy_guts :: consts :: trace_action )
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
}

void shy_trace_loadable_fsm_behaviour :: machine_state_on_entry
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    )
{
    if ( shy_guts :: consts :: trace_entry )
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
}

void shy_trace_loadable_fsm_behaviour :: machine_state_on_exit
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    )
{
    if ( shy_guts :: consts :: trace_exit )
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
}

void shy_trace_loadable_fsm_behaviour :: machine_state_on_input
    ( const so_called_lib_std_char * machine
    , const so_called_lib_std_char * state
    )
{
    if ( shy_guts :: consts :: trace_input )
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
}

void shy_trace_loadable_fsm_behaviour :: tick_all_fsms ( )
{
    if ( shy_guts :: consts :: trace_tick )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "All machines do tick." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
