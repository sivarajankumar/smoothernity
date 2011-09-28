namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "loadable_parser" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_loadable_parser :: expected_action_discard_input_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected input name, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_action_do_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected action name, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_attribute_name_or_consts_or_system_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected attribute name or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: consts . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: system . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_brace_open_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_string brace_open ;
        brace_open = so_called_loadable_parser_consts :: brace_open ;

        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( brace_open . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_brace_open_or_identifier_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_string brace_open ;
        brace_open = so_called_loadable_parser_consts :: brace_open ;

        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( brace_open . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or identifier, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_command_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected command name, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_consts_or_system_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: consts . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: system . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_denominator_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected denominator, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_divide_or_identifier_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_string divide ;
        divide = so_called_loadable_parser_consts :: divide ;

        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( divide . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or identifier, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_do_or_discard_or_command_or_on_or_to_or_state_or_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: do_token . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: discard . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: command . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: on . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: to . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: state . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: machine . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: system . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: consts . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_entry_or_exit_or_brace_open_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_string brace_open ;
        brace_open = so_called_loadable_parser_consts :: brace_open ;

        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: entry . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: exit . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( brace_open . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_input_name_or_parenthesis_open_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_string parenthesis_open ;
        parenthesis_open = so_called_loadable_parser_consts :: parenthesis_open ;

        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected input name or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( parenthesis_open . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_input_name_or_parenthesis_open_or_brace_close_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_string brace_close ;
        so_called_lib_std_string parenthesis_open ;

        brace_close = so_called_loadable_parser_consts :: brace_close ;
        parenthesis_open = so_called_loadable_parser_consts :: parenthesis_open ;

        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected input name or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( parenthesis_open . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( brace_close . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_is_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: is . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_machine_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected machine name, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_machine_or_command_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: machine . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: command . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: machine . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: system . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: consts . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_module_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected module name, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_numerator_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected numerator, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_on_or_to_or_state_or_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: on . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: to . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: state . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: machine . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: system . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: consts . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_parenthesis_close_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_string parenthesis_close ;
        parenthesis_close = so_called_loadable_parser_consts :: parenthesis_close ;

        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( parenthesis_close . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_state_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected state name, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_state_or_machine_or_system_or_consts_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: state . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: machine . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: system . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " or " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: consts . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_system_name_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected system name, but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: expected_to_instead_of_token_error
    ( const so_called_lib_std_char * token
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Expected " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( so_called_loadable_parser_consts :: to . c_str ( ) ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( ", but got " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( token ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " instead." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: unknown_attribute_fract_in_module_error
    ( const so_called_lib_std_char * attribute
    , const so_called_lib_std_char * module
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. There is no fract attribute " ) ;
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
}

void shy_trace_loadable_parser :: unknown_attribute_whole_in_module_error
    ( const so_called_lib_std_char * attribute
    , const so_called_lib_std_char * module
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. There is no whole attribute " ) ;
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
}

void shy_trace_loadable_parser :: unknown_fsm_action_error
    ( const so_called_lib_std_char * action
    , const so_called_lib_std_char * system
    )
{
    if ( shy_guts :: consts :: trace_enabled )
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
}

void shy_trace_loadable_parser :: unknown_fsm_input_error
    ( const so_called_lib_std_char * input
    , const so_called_lib_std_char * system
    )
{
    if ( shy_guts :: consts :: trace_enabled )
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
}

void shy_trace_loadable_parser :: unknown_fsm_system_error
    ( const so_called_lib_std_char * system
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. There is no FSM system " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( system ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: unknown_module_error
    ( const so_called_lib_std_char * module
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. There is no consts module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_parser :: whole_line_containing_error
    ( const so_called_lib_std_char * line
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Whole line containing error: " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( line ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
