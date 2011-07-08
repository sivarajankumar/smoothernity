namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "loadable_parser" ;
    }
}

void shy_trace_loadable_parser_worker :: expected_action_discard_input_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected input name, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_action_do_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected action name, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_attribute_name_or_consts_or_system_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected attribute name or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"consts\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"system\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_brace_open_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"{\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_brace_open_or_identifier_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"{\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or identifier, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_command_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected command name, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_consts_or_system_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"consts\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"system\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_denominator_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected denominator, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_divide_or_identifier_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"/\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or identifier, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_do_or_discard_or_command_or_on_or_to_or_state_or_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"do\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"discard\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"command\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"on\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"to\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"state\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"machine\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"system\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"consts\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_entry_or_exit_or_brace_open_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"entry\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"exit\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"{\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_input_name_or_parenthesis_open_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected input name or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"(\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_input_name_or_parenthesis_open_or_brace_close_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected input name or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"(\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"}\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_is_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"is\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_machine_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected machine name, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_machine_or_command_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"machine\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"command\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"machine\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"system\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"consts\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_module_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected module name, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_numerator_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected numerator, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_on_or_to_or_state_or_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"on\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"to\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"state\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"machine\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"system\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"consts\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_parenthesis_close_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\")\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_state_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected state name, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_state_or_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"state\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"machine\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"system\"" ) ;
    so_called_platform_trace :: trace_string_error ( " or " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"consts\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_system_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected system name, but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: expected_to_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"to\"" ) ;
    so_called_platform_trace :: trace_string_error ( ", but got " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( token ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " instead." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: unknown_fract_attribute_in_module_error
    ( const so_called_lib_std_char * attribute
    , const so_called_lib_std_char * module
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. There is no attribute " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( attribute ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " in module " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( module ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: unknown_fsm_action_error
    ( const so_called_lib_std_char * action
    , const so_called_lib_std_char * system
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. There is no action " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( action ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " in FSM system " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( system ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: unknown_fsm_input_error
    ( const so_called_lib_std_char * input
    , const so_called_lib_std_char * system
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. There is no input " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( input ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( " in FSM system " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( system ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: unknown_fsm_system_error
    ( const so_called_lib_std_char * system
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. There is no FSM system " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( system ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: unknown_module_error
    ( const so_called_lib_std_char * module
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. There is no consts module " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( module ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_loadable_parser_worker :: whole_line_containing_error
    ( const so_called_lib_std_char * line
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Whole line containing error: " ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_name_error ( line ) ;
    so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}
