namespace shy_guts
{
    enum token_class_type
    {
        token_class_none ,
        token_class_terminator ,
        token_class_identifier ,
        token_class_number ,
        token_class_divide ,
        token_class_minus ,
        token_class_brace_open ,
        token_class_brace_close ,
        token_class_parenthesis_open ,
        token_class_parenthesis_close ,
        token_class_unknown
    } ;

    enum state_type
    {
        state_none ,
        state_error ,
        state_reading_module_name ,
        state_reading_attribute_name ,
        state_reading_attribute_numerator_sign ,
        state_reading_attribute_numerator_value ,
        state_reading_attribute_denominator_sign ,
        state_reading_attribute_denominator_value ,
        state_determining_value_format ,
        state_reading_system_name ,
        state_reading_machine_token ,
        state_reading_machine_name ,
        state_reading_state_token ,
        state_reading_state_name ,
        state_reading_state_content ,
        state_reading_event_type ,
        state_reading_action_token ,
        state_reading_action_do_name ,
        state_reading_action_discard_input_name ,
        state_reading_action_command_name ,
        state_reading_action_command_to_token ,
        state_reading_action_command_machine_name ,
        state_reading_first_condition_group ,
        state_reading_next_condition_group ,
        state_reading_first_condition_in_group ,
        state_reading_next_condition_in_group ,
        state_reading_parametric_condition_token ,
        state_reading_state_condition_machine_name ,
        state_reading_state_condition_is_token ,
        state_reading_state_condition_state_name ,
        state_reading_state_condition_parenthesis_close ,
        state_reading_command_condition_command_name ,
        state_reading_command_condition_parenthesis_close ,
        state_reading_transition_state_name ,
        state_reading_transition_if_token
    } ;

    static so_called_lib_std_string attribute_denominator_sign ;
    static so_called_lib_std_string attribute_denominator_value ;
    static so_called_lib_std_string attribute_name ;
    static so_called_lib_std_string attribute_numerator_sign ;
    static so_called_lib_std_string attribute_numerator_value ;
    static so_called_lib_std_bool continue_parsing = so_called_lib_std_false ;
    static so_called_lib_std_bool continue_reading_next_token = so_called_lib_std_false ;
    static so_called_loadable_fsm_content_action_command_type current_fsm_action_command ;
    static so_called_loadable_fsm_content_actions_type * current_fsm_actions = 0 ;
    static so_called_loadable_fsm_content_condition_group_type * current_fsm_condition_group = 0 ;
    static so_called_loadable_fsm_content_condition_group_container_type * current_fsm_condition_group_container = 0 ;
    static so_called_loadable_fsm_content_condition_state_type current_fsm_condition_state ;
    static so_called_loadable_fsm_content_machine_type * current_fsm_machine = 0 ;
    static so_called_loadable_fsm_content_on_input_type * current_fsm_on_input = 0 ;
    static so_called_loadable_fsm_content_state_type * current_fsm_state = 0 ;
    static so_called_loadable_fsm_content_system_type * current_fsm_system = 0 ;
    static so_called_lib_std_string current_fsm_system_name ;
    static so_called_loadable_fsm_content_transition_type * current_fsm_transition = 0 ;
    static so_called_lib_std_bool error = so_called_lib_std_false ;
    static so_called_lib_std_bool input_actions_conditions_selected = so_called_lib_std_false ;
    static so_called_lib_std_locale locale ;
    static so_called_lib_std_string module_name ;
    static so_called_lib_std_string remaining_line ;
    static state_type state = state_none ;
    static so_called_lib_std_string token ;
    static token_class_type token_class = token_class_none ;
    static so_called_lib_std_bool transition_conditions_selected = so_called_lib_std_false ;
    static so_called_lib_std_string whole_line ;

    static void handle_token_class_none ( ) ;
    static void handle_token_class_identifier ( ) ;
    static void handle_token_class_number ( ) ;
    static void handle_token_class_terminator ( ) ;
    static void handle_token_class_divide ( ) ;
    static void handle_token_class_minus ( ) ;
    static void handle_token_class_brace_open ( ) ;
    static void handle_token_class_brace_close ( ) ;
    static void handle_token_class_parenthesis_open ( ) ;
    static void handle_token_class_parenthesis_close ( ) ;
    static void handle_token_class_unknown ( ) ;
    static void handle_state_none ( ) ;
    static void handle_state_error ( ) ;
    static void handle_state_reading_module_name ( ) ;
    static void handle_state_reading_attribute_name ( ) ;
    static void handle_state_reading_attribute_numerator_sign ( ) ;
    static void handle_state_reading_attribute_numerator_value ( ) ;
    static void handle_state_reading_attribute_denominator_sign ( ) ;
    static void handle_state_reading_attribute_denominator_value ( ) ;
    static void handle_state_determining_value_format ( ) ;
    static void handle_state_reading_system_name ( ) ;
    static void handle_state_reading_machine_token ( ) ;
    static void handle_state_reading_machine_name ( ) ;
    static void handle_state_reading_state_token ( ) ;
    static void handle_state_reading_state_name ( ) ;
    static void handle_state_reading_state_content ( ) ;
    static void handle_state_reading_event_type ( ) ;
    static void handle_state_reading_action_token ( ) ;
    static void handle_state_reading_action_do_name ( ) ;
    static void handle_state_reading_action_discard_input_name ( ) ;
    static void handle_state_reading_action_command_name ( ) ;
    static void handle_state_reading_action_command_to_token ( ) ;
    static void handle_state_reading_action_command_machine_name ( ) ;
    static void handle_state_reading_first_condition_group ( ) ;
    static void handle_state_reading_next_condition_group ( ) ;
    static void handle_state_reading_first_condition_in_group ( ) ;
    static void handle_state_reading_next_condition_in_group ( ) ;
    static void handle_state_reading_parametric_condition_token ( ) ;
    static void handle_state_reading_state_condition_machine_name ( ) ;
    static void handle_state_reading_state_condition_is_token ( ) ;
    static void handle_state_reading_state_condition_state_name ( ) ;
    static void handle_state_reading_state_condition_parenthesis_close ( ) ;
    static void handle_state_reading_command_condition_command_name ( ) ;
    static void handle_state_reading_command_condition_parenthesis_close ( ) ;
    static void handle_state_reading_transition_state_name ( ) ;
    static void handle_state_reading_transition_if_token ( ) ;
    static void store_module_name ( so_called_lib_std_string ) ;
    static void store_attribute_name ( so_called_lib_std_string ) ;
    static void store_attribute_numerator_sign ( so_called_lib_std_string ) ;
    static void store_attribute_numerator_value ( so_called_lib_std_string ) ;
    static void store_attribute_denominator_sign ( so_called_lib_std_string ) ;
    static void store_attribute_denominator_value ( so_called_lib_std_string ) ;
    static void store_system_name ( so_called_lib_std_string ) ;
    static void store_machine_name ( so_called_lib_std_string ) ;
    static void store_state_name ( so_called_lib_std_string ) ;
    static void store_action_do_name ( so_called_lib_std_string ) ;
    static void store_action_discard_input_name ( so_called_lib_std_string ) ;
    static void store_action_command_name ( so_called_lib_std_string ) ;
    static void store_action_command_machine_name ( so_called_lib_std_string ) ;
    static void store_action_command ( ) ;
    static void store_transition_state_name ( so_called_lib_std_string ) ;
    static void store_input_condition ( so_called_lib_std_string ) ;
    static void store_state_condition_machine_name ( so_called_lib_std_string ) ;
    static void store_state_condition_state_name ( so_called_lib_std_string ) ;
    static void store_state_condition ( ) ;
    static void store_command_condition_command_name ( so_called_lib_std_string ) ;
    static void select_entry_actions_container ( ) ;
    static void select_exit_actions_container ( ) ;
    static void select_input_actions_container ( ) ;
    static void select_input_actions_conditions ( ) ;
    static void select_input_actions_condition_group_container ( ) ;
    static void select_transition_conditions ( ) ;
    static void select_transition_condition_group_container ( ) ;
    static void add_on_input_event ( ) ;
    static void add_transition ( ) ;
    static void add_condition_group ( ) ;
    static void set_whole_value ( ) ;
    static void set_fract_value ( ) ;
    static void read_next_token ( ) ;
    static void trim_first_char ( ) ;
    static void trim_whitespaces ( ) ;
    static void append_first_char_to_token ( ) ;
    static void move_first_char_to_token ( ) ;
    static void first_char ( so_called_lib_std_char & ) ;
    static void any_chars_in_line ( so_called_lib_std_bool & ) ;
    static void process_syntax_error ( ) ;
}

void shy_guts :: handle_token_class_none ( )
{
    so_called_lib_std_char ch ;
    shy_guts :: first_char ( ch ) ;
    if ( so_called_lib_std_isdigit ( ch , shy_guts :: locale ) )
        shy_guts :: token_class = shy_guts :: token_class_number ;
    else if ( so_called_lib_std_isalpha ( ch , shy_guts :: locale ) )
        shy_guts :: token_class = shy_guts :: token_class_identifier ;
    else if ( ch == so_called_loadable_parser_consts :: terminator )
        shy_guts :: token_class = shy_guts :: token_class_terminator ;
    else if ( ch == so_called_loadable_parser_consts :: divide )
        shy_guts :: token_class = shy_guts :: token_class_divide ;
    else if ( ch == so_called_loadable_parser_consts :: minus )
        shy_guts :: token_class = shy_guts :: token_class_minus ;
    else if ( ch == so_called_loadable_parser_consts :: brace_open )
        shy_guts :: token_class = shy_guts :: token_class_brace_open ;
    else if ( ch == so_called_loadable_parser_consts :: brace_close )
        shy_guts :: token_class = shy_guts :: token_class_brace_close ;
    else if ( ch == so_called_loadable_parser_consts :: parenthesis_open )
        shy_guts :: token_class = shy_guts :: token_class_parenthesis_open ;
    else if ( ch == so_called_loadable_parser_consts :: parenthesis_close )
        shy_guts :: token_class = shy_guts :: token_class_parenthesis_close ;
    else
        shy_guts :: token_class = shy_guts :: token_class_unknown ;
}

void shy_guts :: handle_token_class_identifier ( )
{
    so_called_lib_std_char ch ;
    shy_guts :: first_char ( ch ) ;
    if ( so_called_lib_std_isalpha ( ch , shy_guts :: locale ) 
      || so_called_lib_std_isdigit ( ch , shy_guts :: locale )
      || ch == so_called_loadable_parser_consts :: underscore
       )
    {
        shy_guts :: move_first_char_to_token ( ) ;
    }
    else
        shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_number ( )
{
    so_called_lib_std_char ch ;
    shy_guts :: first_char ( ch ) ;
    if ( so_called_lib_std_isdigit ( ch , shy_guts :: locale ) )
        shy_guts :: move_first_char_to_token ( ) ;
    else
        shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_terminator ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_divide ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_minus ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_brace_open ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_brace_close ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_parenthesis_open ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_parenthesis_close ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_token_class_unknown ( )
{
    shy_guts :: move_first_char_to_token ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_false ;
}

void shy_guts :: handle_state_none ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: system )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_system_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_consts_or_system_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_error ( )
{
    shy_guts :: continue_parsing = so_called_lib_std_false ;
}

void shy_guts :: handle_state_reading_module_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_module_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_module_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_attribute_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_terminator )
        shy_guts :: continue_parsing = so_called_lib_std_false ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: system )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_system_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_attribute_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_numerator_sign ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_attribute_name_or_consts_or_system_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_attribute_numerator_sign ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_minus )
    {
        shy_guts :: store_attribute_numerator_sign ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_numerator_value ;
    }
    else
    {
        shy_guts :: store_attribute_numerator_sign ( so_called_lib_std_string ( ) ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_numerator_value ;
    }
}

void shy_guts :: handle_state_reading_attribute_numerator_value ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_number )
    {
        shy_guts :: store_attribute_numerator_value ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_determining_value_format ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_numerator_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_attribute_denominator_sign ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_minus )
    {
        shy_guts :: store_attribute_denominator_sign ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_denominator_value ;
    }
    else
    {
        shy_guts :: store_attribute_denominator_sign ( so_called_lib_std_string ( ) ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_denominator_value ;
    }
}

void shy_guts :: handle_state_reading_attribute_denominator_value ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_number )
    {
        shy_guts :: store_attribute_denominator_value ( shy_guts :: token ) ;
        shy_guts :: set_fract_value ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_denominator_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_determining_value_format ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_divide )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_denominator_sign ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier || shy_guts :: token_class == shy_guts :: token_class_terminator )
    {
        shy_guts :: set_whole_value ( ) ;
        shy_guts :: state = shy_guts :: state_reading_attribute_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_divide_or_identifier_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_system_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_system_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_machine_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_system_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_machine_token ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_terminator )
        shy_guts :: continue_parsing = so_called_lib_std_false ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: machine )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_machine_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: system )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_system_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_machine_or_system_or_consts_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_machine_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_machine_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_machine_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_state_token ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_terminator )
        shy_guts :: continue_parsing = so_called_lib_std_false ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: state )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: machine )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_machine_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: system )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_system_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_state_or_machine_or_system_or_consts_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_state_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_state_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_content ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_state_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_state_content ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_terminator )
        shy_guts :: continue_parsing = so_called_lib_std_false ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: on )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_event_type ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: to )
    {
        shy_guts :: add_transition ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_transition_state_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: state )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: machine )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_machine_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: system )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_system_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_on_or_to_or_state_or_machine_or_system_or_consts_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_event_type ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: entry )
    {
        shy_guts :: select_entry_actions_container ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_token ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: exit )
    {
        shy_guts :: select_exit_actions_container ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_token ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_brace_open )
    {
        shy_guts :: add_on_input_event ( ) ;
        shy_guts :: select_input_actions_container ( ) ;
        shy_guts :: select_input_actions_conditions ( ) ;
        shy_guts :: select_input_actions_condition_group_container ( ) ;
        shy_guts :: state = shy_guts :: state_reading_first_condition_group ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_entry_or_exit_or_brace_open_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_action_token ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_terminator )
        shy_guts :: continue_parsing = so_called_lib_std_false ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: do_token )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_do_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: discard )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_discard_input_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: command )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_command_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: on )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_event_type ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: to )
    {
        shy_guts :: add_transition ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_transition_state_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: state )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: machine )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_machine_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: system )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_system_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else
    {
        so_called_trace
            ( so_called_trace_loadable_parser :: expected_do_or_discard_or_command_or_on_or_to_or_state_or_machine_or_system_or_consts_instead_of_token_error
                ( shy_guts :: token . c_str ( ) 
                ) 
            ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_action_do_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_action_do_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_action_do_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_action_discard_input_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_action_discard_input_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_action_discard_input_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_action_command_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_action_command_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_command_to_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_command_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_action_command_to_token ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: to )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_command_machine_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_to_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_action_command_machine_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_action_command_machine_name ( shy_guts :: token ) ;
        shy_guts :: store_action_command ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_action_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_machine_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_first_condition_group ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_brace_open )
        shy_guts :: state = shy_guts :: state_reading_next_condition_group ;
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_brace_open_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_next_condition_group ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_brace_open )
    {
        shy_guts :: add_condition_group ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_first_condition_in_group ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: input_actions_conditions_selected )
        shy_guts :: state = shy_guts :: state_reading_action_token ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: transition_conditions_selected )
        shy_guts :: state = shy_guts :: state_reading_state_content ;
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_brace_open_or_identifier_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_first_condition_in_group ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
        shy_guts :: state = shy_guts :: state_reading_next_condition_in_group ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_parenthesis_open )
        shy_guts :: state = shy_guts :: state_reading_next_condition_in_group ;
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_input_name_or_parenthesis_open_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_next_condition_in_group ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_parenthesis_open )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_parametric_condition_token ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_input_condition ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_brace_close )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_next_condition_group ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_input_name_or_parenthesis_open_or_brace_close_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_parametric_condition_token ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: machine )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_condition_machine_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: command )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_command_condition_command_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_machine_or_command_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_state_condition_machine_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_state_condition_machine_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_condition_is_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_machine_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_state_condition_is_token ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: is )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_condition_state_name ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_is_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_state_condition_state_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_state_condition_state_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_state_condition_parenthesis_close ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_state_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_state_condition_parenthesis_close ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_parenthesis_close )
    {
        shy_guts :: store_state_condition ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_next_condition_in_group ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_parenthesis_close_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_command_condition_command_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_command_condition_command_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_command_condition_parenthesis_close ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_command_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_command_condition_parenthesis_close ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_parenthesis_close )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_next_condition_in_group ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_parenthesis_close_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_transition_state_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
    {
        shy_guts :: store_transition_state_name ( shy_guts :: token ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_transition_if_token ;
    }
    else
    {
        so_called_trace ( so_called_trace_loadable_parser :: expected_state_name_instead_of_token_error ( shy_guts :: token . c_str ( ) ) ) ;
        shy_guts :: process_syntax_error ( ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_transition_if_token ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == so_called_loadable_parser_consts :: if_token )
    {
        shy_guts :: select_transition_conditions ( ) ;
        shy_guts :: select_transition_condition_group_container ( ) ;
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_first_condition_group ;
    }
    else
        shy_guts :: state = shy_guts :: state_reading_state_content ;
}

void shy_guts :: store_module_name ( so_called_lib_std_string name )
{
    shy_guts :: module_name = name ;
}

void shy_guts :: store_attribute_name ( so_called_lib_std_string name )
{
    shy_guts :: attribute_name = name ;
}

void shy_guts :: store_attribute_numerator_sign ( so_called_lib_std_string sign )
{
    shy_guts :: attribute_numerator_sign = sign ;
}

void shy_guts :: store_attribute_numerator_value ( so_called_lib_std_string value )
{
    shy_guts :: attribute_numerator_value = value ;
}

void shy_guts :: store_attribute_denominator_sign ( so_called_lib_std_string sign )
{
    shy_guts :: attribute_denominator_sign = sign ;
}

void shy_guts :: store_attribute_denominator_value ( so_called_lib_std_string value )
{
    shy_guts :: attribute_denominator_value = value ;
}

void shy_guts :: store_system_name ( so_called_lib_std_string name )
{
    so_called_loadable_fsm_content_system_container_type * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    if ( system_container -> find ( name ) == system_container -> end ( ) )
    {
        so_called_trace ( so_called_trace_loadable_parser :: unknown_fsm_system_error ( name . c_str ( ) ) ) ;
        shy_guts :: error = so_called_lib_std_true ;
        shy_guts :: current_fsm_system_name = so_called_lib_std_string ( ) ;
        shy_guts :: current_fsm_system = 0 ;
    }
    else
    {
        shy_guts :: current_fsm_system_name = name ;
        shy_guts :: current_fsm_system = & ( ( * system_container ) [ name ] ) ;
    }
}

void shy_guts :: store_machine_name ( so_called_lib_std_string name )
{
    if ( shy_guts :: current_fsm_system )
    {
        if ( shy_guts :: current_fsm_system -> machines . find ( name ) == shy_guts :: current_fsm_system -> machines . end ( ) )
            shy_guts :: current_fsm_system -> machines [ name ] = so_called_loadable_fsm_content_machine_type ( ) ;
        shy_guts :: current_fsm_machine = & ( shy_guts :: current_fsm_system -> machines [ name ] ) ;
    }
}

void shy_guts :: store_state_name ( so_called_lib_std_string name )
{
    if ( shy_guts :: current_fsm_machine )
    {
        if ( shy_guts :: current_fsm_machine -> states . find ( name ) == shy_guts :: current_fsm_machine -> states . end ( ) )
            shy_guts :: current_fsm_machine -> states [ name ] = so_called_loadable_fsm_content_state_type ( ) ;
        shy_guts :: current_fsm_state = & ( shy_guts :: current_fsm_machine -> states [ name ] ) ;
    }
}

void shy_guts :: store_action_do_name ( so_called_lib_std_string name )
{
    if ( shy_guts :: current_fsm_system && shy_guts :: current_fsm_system -> actions . count ( name ) == 0 )
    {
        so_called_trace ( so_called_trace_loadable_parser :: unknown_fsm_action_error ( name . c_str ( ) , shy_guts :: current_fsm_system_name . c_str ( ) ) ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
    else if ( shy_guts :: current_fsm_actions )
    {
        so_called_loadable_fsm_content_action_do_type action_do ;
        action_do . action = name ;
        shy_guts :: current_fsm_actions -> actions . push_back ( action_do ) ;
    }
}

void shy_guts :: store_action_discard_input_name ( so_called_lib_std_string name )
{
    if ( shy_guts :: current_fsm_system && shy_guts :: current_fsm_system -> inputs . count ( name ) == 0 )
    {
        so_called_trace ( so_called_trace_loadable_parser :: unknown_fsm_input_error ( name . c_str ( ) , shy_guts :: current_fsm_system_name . c_str ( ) ) ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
    else if ( shy_guts :: current_fsm_actions )
    {
        so_called_loadable_fsm_content_action_discard_type action_discard ;
        action_discard . input = name ;
        shy_guts :: current_fsm_actions -> discards . push_back ( action_discard ) ;
    }
}

void shy_guts :: store_action_command_name ( so_called_lib_std_string name )
{
    shy_guts :: current_fsm_action_command . command = name ;
}

void shy_guts :: store_action_command_machine_name ( so_called_lib_std_string name )
{
    shy_guts :: current_fsm_action_command . machine = name ;
}

void shy_guts :: store_action_command ( )
{
    if ( shy_guts :: current_fsm_actions )
        shy_guts :: current_fsm_actions -> commands . push_back ( shy_guts :: current_fsm_action_command ) ;
}

void shy_guts :: store_transition_state_name ( so_called_lib_std_string name )
{
    if ( shy_guts :: current_fsm_transition )
        shy_guts :: current_fsm_transition -> state = name ;
}

void shy_guts :: store_input_condition ( so_called_lib_std_string input )
{
    if ( shy_guts :: current_fsm_system && shy_guts :: current_fsm_system -> inputs . count ( input ) == 0 )
    {
        so_called_trace ( so_called_trace_loadable_parser :: unknown_fsm_input_error ( input . c_str ( ) , shy_guts :: current_fsm_system_name . c_str ( ) ) ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
    else if ( shy_guts :: current_fsm_condition_group )
    {
        so_called_loadable_fsm_content_condition_input_type condition ;
        condition . input = input ;
        shy_guts :: current_fsm_condition_group -> inputs . push_back ( condition ) ;
    }
}

void shy_guts :: store_state_condition_machine_name ( so_called_lib_std_string name )
{
    shy_guts :: current_fsm_condition_state . machine = name ;
}

void shy_guts :: store_state_condition_state_name ( so_called_lib_std_string name )
{
    shy_guts :: current_fsm_condition_state . state = name ;
}

void shy_guts :: store_state_condition ( )
{
    if ( shy_guts :: current_fsm_condition_group )
        shy_guts :: current_fsm_condition_group -> states . push_back ( shy_guts :: current_fsm_condition_state ) ;
}

void shy_guts :: store_command_condition_command_name ( so_called_lib_std_string name )
{
    if ( shy_guts :: current_fsm_condition_group )
    {
        so_called_loadable_fsm_content_condition_command_type condition ;
        condition . command = name ;
        shy_guts :: current_fsm_condition_group -> commands . push_back ( condition ) ;
    }
}

void shy_guts :: select_entry_actions_container ( )
{
    if ( shy_guts :: current_fsm_state )
        shy_guts :: current_fsm_actions = & shy_guts :: current_fsm_state -> on_entry ;
}

void shy_guts :: select_exit_actions_container ( )
{
    if ( shy_guts :: current_fsm_state )
        shy_guts :: current_fsm_actions = & shy_guts :: current_fsm_state -> on_exit ;
}

void shy_guts :: select_input_actions_container ( )
{
    if ( shy_guts :: current_fsm_on_input )
        shy_guts :: current_fsm_actions = & shy_guts :: current_fsm_on_input -> actions ;
}

void shy_guts :: select_input_actions_conditions ( )
{
    shy_guts :: input_actions_conditions_selected = so_called_lib_std_true ;
    shy_guts :: transition_conditions_selected = so_called_lib_std_false ;
}

void shy_guts :: select_input_actions_condition_group_container ( )
{
    if ( shy_guts :: current_fsm_on_input )
        shy_guts :: current_fsm_condition_group_container = & shy_guts :: current_fsm_on_input -> condition_groups ;
}

void shy_guts :: select_transition_conditions ( )
{
    shy_guts :: input_actions_conditions_selected = so_called_lib_std_false ;
    shy_guts :: transition_conditions_selected = so_called_lib_std_true ;
}

void shy_guts :: select_transition_condition_group_container ( )
{
    if ( shy_guts :: current_fsm_transition )
        shy_guts :: current_fsm_condition_group_container = & shy_guts :: current_fsm_transition -> condition_groups ;
}

void shy_guts :: add_on_input_event ( )
{
    if ( shy_guts :: current_fsm_state )
    {
        shy_guts :: current_fsm_state -> on_input . push_back ( so_called_loadable_fsm_content_on_input_type ( ) ) ;
        shy_guts :: current_fsm_on_input = & shy_guts :: current_fsm_state -> on_input . back ( ) ;
    }
}

void shy_guts :: add_transition ( )
{
    if ( shy_guts :: current_fsm_state )
    {
        shy_guts :: current_fsm_state -> transitions . push_back ( so_called_loadable_fsm_content_transition_type ( ) ) ;
        shy_guts :: current_fsm_transition = & shy_guts :: current_fsm_state -> transitions . back ( ) ;
    }
}

void shy_guts :: add_condition_group ( )
{
    if ( shy_guts :: current_fsm_condition_group_container )
    {
        shy_guts :: current_fsm_condition_group_container -> push_back ( so_called_loadable_fsm_content_condition_group_type ( ) ) ;
        shy_guts :: current_fsm_condition_group = & shy_guts :: current_fsm_condition_group_container -> back ( ) ;
    }
}

void shy_guts :: process_syntax_error ( )
{
    so_called_trace ( so_called_trace_loadable_parser :: whole_line_containing_error ( shy_guts :: whole_line . c_str ( ) ) ) ;
    shy_guts :: error = so_called_lib_std_true ;
}

void shy_guts :: set_whole_value ( )
{
    so_called_loadable_consts_content_module_container_type * module_container = 0 ;
    so_called_loadable_consts_content_module_container_type :: iterator module_i ;

    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    module_i = module_container -> find ( shy_guts :: module_name ) ;
    if ( module_i == module_container -> end ( ) )
    {
        so_called_trace ( so_called_trace_loadable_parser :: unknown_module_error ( shy_guts :: module_name . c_str ( ) ) ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
    else
    {
        so_called_loadable_consts_content_module_type & module = module_i -> second ;
        so_called_loadable_consts_content_value_whole_container_type :: iterator whole_i ;
        whole_i = module . name_to_whole . find ( shy_guts :: attribute_name ) ;
        if ( whole_i == module . name_to_whole . end ( ) )
        {
            so_called_trace ( so_called_trace_loadable_parser :: unknown_attribute_whole_in_module_error ( shy_guts :: attribute_name . c_str ( ) , shy_guts :: module_name . c_str ( ) ) ) ;
            shy_guts :: error = so_called_lib_std_true ;
        }
        else
        {
            so_called_loadable_consts_content_value_whole_type & whole = whole_i -> second ;
            whole . sign = shy_guts :: attribute_numerator_sign ;
            whole . value = shy_guts :: attribute_numerator_value ;
        }
    }
}

void shy_guts :: set_fract_value ( )
{
    so_called_loadable_consts_content_module_container_type * module_container = 0 ;
    so_called_loadable_consts_content_module_container_type :: iterator module_i ;

    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    module_i = module_container -> find ( shy_guts :: module_name ) ;
    if ( module_i == module_container -> end ( ) )
    {
        so_called_trace ( so_called_trace_loadable_parser :: unknown_module_error ( shy_guts :: module_name . c_str ( ) ) ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
    else
    {
        so_called_loadable_consts_content_module_type & module = module_i -> second ;
        so_called_loadable_consts_content_value_fract_container_type :: iterator fract_i ;
        fract_i = module . name_to_fract . find ( shy_guts :: attribute_name ) ;
        if ( fract_i == module . name_to_fract . end ( ) )
        {
            so_called_trace ( so_called_trace_loadable_parser :: unknown_attribute_fract_in_module_error ( shy_guts :: attribute_name . c_str ( ) , shy_guts :: module_name . c_str ( ) ) ) ;
            shy_guts :: error = so_called_lib_std_true ;
        }
        else
        {
            so_called_loadable_consts_content_value_fract_type & fract = fract_i -> second ;
            fract . numerator_sign = shy_guts :: attribute_numerator_sign ;
            fract . numerator_value = shy_guts :: attribute_numerator_value ;
            fract . denominator_sign = shy_guts :: attribute_denominator_sign ;
            fract . denominator_value = shy_guts :: attribute_denominator_value ;
        }
    }
}

void shy_guts :: read_next_token ( )
{
    shy_guts :: token = so_called_lib_std_string ( ) ;
    shy_guts :: token_class = shy_guts :: token_class_none ;
    shy_guts :: trim_whitespaces ( ) ;
    shy_guts :: continue_reading_next_token = so_called_lib_std_true ;
    
    so_called_lib_std_bool any_chars = so_called_lib_std_false ;
    shy_guts :: any_chars_in_line ( any_chars ) ;
    while ( any_chars && shy_guts :: continue_reading_next_token )
    {
        if ( shy_guts :: token_class == shy_guts :: token_class_none )
            shy_guts :: handle_token_class_none ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_terminator )
            shy_guts :: handle_token_class_terminator ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_number )
            shy_guts :: handle_token_class_number ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_identifier )
            shy_guts :: handle_token_class_identifier ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_divide )
            shy_guts :: handle_token_class_divide ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_minus )
            shy_guts :: handle_token_class_minus ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_brace_open )
            shy_guts :: handle_token_class_brace_open ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_brace_close )
            shy_guts :: handle_token_class_brace_close ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_parenthesis_open )
            shy_guts :: handle_token_class_parenthesis_open ( ) ;
        else if ( shy_guts :: token_class == shy_guts :: token_class_parenthesis_close )
            shy_guts :: handle_token_class_parenthesis_close ( ) ;
        else
            shy_guts :: handle_token_class_unknown ( ) ;

        shy_guts :: any_chars_in_line ( any_chars ) ;
    }
}

void shy_guts :: trim_first_char ( )
{
    shy_guts :: remaining_line . erase ( shy_guts :: remaining_line . begin ( ) ) ;
}

void shy_guts :: trim_whitespaces ( )
{
    for ( ; ; )
    {
        so_called_lib_std_bool any_chars ;
        shy_guts :: any_chars_in_line ( any_chars ) ;
        if ( any_chars )
        {
            so_called_lib_std_char ch ;
            shy_guts :: first_char ( ch ) ; 
            if ( so_called_lib_std_isspace ( ch , shy_guts :: locale ) )
            {
                shy_guts :: trim_first_char ( ) ;
                continue ;
            }
        }
        break ;
    }
}

void shy_guts :: append_first_char_to_token ( )
{
    so_called_lib_std_char ch ;
    shy_guts :: first_char ( ch ) ;
    shy_guts :: token += ch ;
}

void shy_guts :: move_first_char_to_token ( )
{
    shy_guts :: append_first_char_to_token ( ) ;
    shy_guts :: trim_first_char ( ) ;
}

void shy_guts :: first_char ( so_called_lib_std_char & ch )
{
    ch = shy_guts :: remaining_line . at ( 0 ) ;
}

void shy_guts :: any_chars_in_line ( so_called_lib_std_bool & any_chars )
{
    any_chars = ! shy_guts :: remaining_line . empty ( ) ;
}

void shy_loadable_parser :: prepare ( )
{
    shy_guts :: error = so_called_lib_std_false ;
}

void shy_loadable_parser :: parse ( so_called_lib_std_string line )
{
    shy_guts :: whole_line = line ;
    shy_guts :: remaining_line = line ;
    shy_guts :: continue_parsing = so_called_lib_std_true ;
    shy_guts :: read_next_token ( ) ;
    while ( shy_guts :: continue_parsing && shy_guts :: token_class != shy_guts :: token_class_none )
    {
        if ( shy_guts :: state == shy_guts :: state_none )
            shy_guts :: handle_state_none ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_module_name )
            shy_guts :: handle_state_reading_module_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_attribute_name )
            shy_guts :: handle_state_reading_attribute_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_attribute_numerator_sign )
            shy_guts :: handle_state_reading_attribute_numerator_sign ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_attribute_numerator_value )
            shy_guts :: handle_state_reading_attribute_numerator_value ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_determining_value_format )
            shy_guts :: handle_state_determining_value_format ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_attribute_denominator_sign )
            shy_guts :: handle_state_reading_attribute_denominator_sign ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_attribute_denominator_value )
            shy_guts :: handle_state_reading_attribute_denominator_value ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_system_name )
            shy_guts :: handle_state_reading_system_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_machine_token )
            shy_guts :: handle_state_reading_machine_token ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_machine_name )
            shy_guts :: handle_state_reading_machine_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_state_token )
            shy_guts :: handle_state_reading_state_token ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_state_name )
            shy_guts :: handle_state_reading_state_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_state_content )
            shy_guts :: handle_state_reading_state_content ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_event_type )
            shy_guts :: handle_state_reading_event_type ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_action_token )
            shy_guts :: handle_state_reading_action_token ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_action_do_name )
            shy_guts :: handle_state_reading_action_do_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_action_discard_input_name )
            shy_guts :: handle_state_reading_action_discard_input_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_action_command_name )
            shy_guts :: handle_state_reading_action_command_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_action_command_to_token )
            shy_guts :: handle_state_reading_action_command_to_token ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_action_command_machine_name )
            shy_guts :: handle_state_reading_action_command_machine_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_first_condition_group )
            shy_guts :: handle_state_reading_first_condition_group ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_next_condition_group )
            shy_guts :: handle_state_reading_next_condition_group ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_first_condition_in_group )
            shy_guts :: handle_state_reading_first_condition_in_group ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_next_condition_in_group )
            shy_guts :: handle_state_reading_next_condition_in_group ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_parametric_condition_token )
            shy_guts :: handle_state_reading_parametric_condition_token ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_state_condition_machine_name )
            shy_guts :: handle_state_reading_state_condition_machine_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_state_condition_is_token )
            shy_guts :: handle_state_reading_state_condition_is_token ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_state_condition_state_name )
            shy_guts :: handle_state_reading_state_condition_state_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_state_condition_parenthesis_close )
            shy_guts :: handle_state_reading_state_condition_parenthesis_close ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_command_condition_command_name )
            shy_guts :: handle_state_reading_command_condition_command_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_command_condition_parenthesis_close )
            shy_guts :: handle_state_reading_command_condition_parenthesis_close ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_transition_state_name )
            shy_guts :: handle_state_reading_transition_state_name ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_reading_transition_if_token )
            shy_guts :: handle_state_reading_transition_if_token ( ) ;
        else if ( shy_guts :: state == shy_guts :: state_error )
            shy_guts :: handle_state_error ( ) ;
    }
}

void shy_loadable_parser :: get_error ( so_called_lib_std_bool & arg_error )
{
    arg_error = shy_guts :: error ;
}

void shy_loadable_parser :: terminate ( )
{
    parse ( so_called_lib_std_string ( 1 , so_called_loadable_parser_consts :: terminator ) ) ;
}

