namespace shy_guts
{
    enum type_token_class
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

    enum type_state
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
        state_reading_action_name ,
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

    namespace consts
    {
        static const so_called_std_char brace_close = '}' ;
        static const so_called_std_char brace_open = '{' ;
        static const so_called_std_string command = "command" ;
        static const so_called_std_string consts = "consts" ;
        static const so_called_std_char divide = '/' ;
        static const so_called_std_string do_token = "do" ;
        static const so_called_std_string entry = "entry" ;
        static const so_called_std_string error_whole_line = "whole line: " ;
        static const so_called_std_string exit = "exit" ;
        static const so_called_std_string if_token = "if" ;
        static const so_called_std_string is = "is" ;
        static const so_called_std_string machine = "machine" ;
        static const so_called_std_char minus = '-' ;
        static const so_called_std_string next_line = "\n" ;
        static const so_called_std_string on = "on" ;
        static const so_called_std_char parenthesis_close = ')' ;
        static const so_called_std_char parenthesis_open = '(' ;
        static const so_called_std_string state = "state" ;
        static const so_called_std_string system = "system" ;
        static const so_called_std_char terminator = '#' ;
        static const so_called_std_string to = "to" ;
        static const so_called_std_char underscore = '_' ;
    }

    namespace errors
    {
        static void expected_action_name_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_attribute_name_or_consts_or_system_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_brace_open_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_brace_open_or_identifier_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_command_name_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_consts_or_system_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_denominator_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_divide_or_identifier_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_do_or_command_or_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_entry_or_exit_or_brace_open_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_if_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_input_name_or_parenthesis_open_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_input_name_or_parenthesis_open_or_brace_close_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_is_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_machine_name_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_machine_or_command_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_machine_or_system_or_consts_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_module_name_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_numerator_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_parenthesis_close_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_state_name_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_state_or_machine_or_system_or_consts_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_system_name_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void expected_to_instead_of ( so_called_std_string & , so_called_std_string ) ;
        static void unknown_fract_attribute_in_module ( so_called_std_string & , so_called_std_string attribute , so_called_std_string ) ;
        static void unknown_fsm_action ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
        static void unknown_fsm_input ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
        static void unknown_fsm_system ( so_called_std_string & , so_called_std_string ) ;
        static void unknown_module ( so_called_std_string & , so_called_std_string ) ;
        static void unknown_whole_attribute_in_module ( so_called_std_string & , so_called_std_string attribute , so_called_std_string ) ;
    }

    static so_called_std_string attribute_denominator_sign ;
    static so_called_std_string attribute_denominator_value ;
    static so_called_std_string attribute_name ;
    static so_called_std_string attribute_numerator_sign ;
    static so_called_std_string attribute_numerator_value ;
    static so_called_std_bool continue_parsing = so_called_std_false ;
    static so_called_std_bool continue_reading_next_token = so_called_std_false ;
    static so_called_type_loadable_fsm_content_action_command current_fsm_action_command ;
    static so_called_type_loadable_fsm_content_actions * current_fsm_actions = 0 ;
    static so_called_type_loadable_fsm_content_condition_group * current_fsm_condition_group = 0 ;
    static so_called_type_loadable_fsm_content_condition_group_container * current_fsm_condition_group_container = 0 ;
    static so_called_type_loadable_fsm_content_condition_state current_fsm_condition_state ;
    static so_called_type_loadable_fsm_content_machine * current_fsm_machine = 0 ;
    static so_called_type_loadable_fsm_content_on_input * current_fsm_on_input = 0 ;
    static so_called_type_loadable_fsm_content_state * current_fsm_state = 0 ;
    static so_called_type_loadable_fsm_content_system * current_fsm_system = 0 ;
    static so_called_std_string current_fsm_system_name ;
    static so_called_type_loadable_fsm_content_transition * current_fsm_transition = 0 ;
    static so_called_std_string error ;
    static so_called_std_bool input_actions_conditions_selected = so_called_std_false ;
    static so_called_std_locale locale ;
    static so_called_std_string module_name ;
    static so_called_std_string remaining_line ;
    static type_state state = state_none ;
    static so_called_std_string token ;
    static type_token_class token_class = token_class_none ;
    static so_called_std_bool transition_conditions_selected = so_called_std_false ;
    static so_called_std_string whole_line ;

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
    static void handle_state_reading_action_name ( ) ;
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
    static void store_error ( std :: string ) ;
    static void store_module_name ( std :: string ) ;
    static void store_attribute_name ( std :: string ) ;
    static void store_attribute_numerator_sign ( std :: string ) ;
    static void store_attribute_numerator_value ( std :: string ) ;
    static void store_attribute_denominator_sign ( std :: string ) ;
    static void store_attribute_denominator_value ( std :: string ) ;
    static void store_system_name ( std :: string ) ;
    static void store_machine_name ( std :: string ) ;
    static void store_state_name ( std :: string ) ;
    static void store_action_name ( std :: string ) ;
    static void store_action_command_name ( std :: string ) ;
    static void store_action_command_machine_name ( std :: string ) ;
    static void store_action_command ( ) ;
    static void store_transition_state_name ( std :: string ) ;
    static void store_input_condition ( std :: string ) ;
    static void store_state_condition_machine_name ( std :: string ) ;
    static void store_state_condition_state_name ( std :: string ) ;
    static void store_state_condition ( ) ;
    static void store_command_condition_command_name ( std :: string ) ;
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
    static void first_char ( so_called_std_char & ) ;
    static void any_chars_in_line ( so_called_std_bool & ) ;
}

void shy_guts :: errors :: expected_action_name_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected action name, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_attribute_name_or_consts_or_system_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected attribute name or 'consts' or 'system', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_brace_open_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected '{', but got '" ) + token + ( "'" ) ;
}

void shy_guts :: errors :: expected_brace_open_or_identifier_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected '{' or identifier, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_command_name_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected command name, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_consts_or_system_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'consts' or 'system', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_denominator_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected denominator, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_divide_or_identifier_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected '/' or identifier, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_do_or_command_or_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'do' or 'command' or 'on' or 'to' or 'state' or 'machine' or 'system' or 'consts', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_entry_or_exit_or_brace_open_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'entry' or 'exit' or '{', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_if_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'if', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_input_name_or_parenthesis_open_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected input name or '(', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_input_name_or_parenthesis_open_or_brace_close_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected input name or '(' or '}', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_is_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'is', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_machine_name_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected machine name, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_machine_or_command_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'machine' or 'command', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_machine_or_system_or_consts_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'machine' or 'system' or 'consts', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_module_name_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected module name, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_numerator_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected numerator, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'on' or 'to' or 'state' or 'machine' or 'system' or 'consts' instead of '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_parenthesis_close_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected ')', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_state_name_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected state name, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_state_or_machine_or_system_or_consts_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected 'state' or 'machine' or 'system' or 'consts', but got'" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_system_name_instead_of ( so_called_std_string & error , so_called_std_string token )
{
    error = so_called_std_string ( "expected system name, but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: expected_to_instead_of ( so_called_std_string & error , so_called_std_string token ) 
{
    error = so_called_std_string ( "expected 'to', but got '" ) + token + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: unknown_fract_attribute_in_module ( so_called_std_string & error , so_called_std_string attribute , so_called_std_string module )
{
    error = so_called_std_string ( "unknown fract attribute '" ) + attribute + so_called_std_string ( "' in module '" ) + module + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: unknown_fsm_action ( so_called_std_string & error , so_called_std_string fsm_action , so_called_std_string fsm_system ) 
{
    error = so_called_std_string ( "unknown fsm action '" ) + fsm_action + so_called_std_string ( "' in fsm system '" ) + fsm_system + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: unknown_fsm_input ( so_called_std_string & error , so_called_std_string fsm_input , so_called_std_string fsm_system ) 
{
    error = so_called_std_string ( "unknown fsm input '" ) + fsm_input + so_called_std_string ( "' in fsm system '" ) + fsm_system + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: unknown_fsm_system ( so_called_std_string & error , so_called_std_string fsm_system )
{
    error = so_called_std_string ( "unknown fsm system '" ) + fsm_system + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: unknown_module ( so_called_std_string & error , so_called_std_string module )
{
    error = so_called_std_string ( "unknown module '" ) + module + so_called_std_string ( "'" ) ;
}

void shy_guts :: errors :: unknown_whole_attribute_in_module ( so_called_std_string & error , so_called_std_string attribute , so_called_std_string module ) 
{
    error = so_called_std_string ( "unknown whole attribute '" ) + attribute + so_called_std_string ( "' in module '" ) + module + so_called_std_string ( "'" ) ;
}

void shy_guts :: handle_token_class_none ( )
{
}

void shy_guts :: handle_token_class_identifier ( )
{
}

void shy_guts :: handle_token_class_number ( )
{
}

void shy_guts :: handle_token_class_terminator ( )
{
}

void shy_guts :: handle_token_class_divide ( )
{
}

void shy_guts :: handle_token_class_minus ( )
{
}

void shy_guts :: handle_token_class_brace_open ( )
{
}

void shy_guts :: handle_token_class_brace_close ( )
{
}

void shy_guts :: handle_token_class_parenthesis_open ( )
{
}

void shy_guts :: handle_token_class_parenthesis_close ( )
{
}

void shy_guts :: handle_token_class_unknown ( )
{
}

void shy_guts :: handle_state_none ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == shy_guts :: consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == shy_guts :: consts :: system )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_system_name ;
    }
    else
    {
        so_called_std_string error ;
        shy_guts :: errors :: expected_consts_or_system_instead_of ( error , shy_guts :: token ) ;
        shy_guts :: store_error ( error ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_error ( )
{
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
        so_called_std_string error ;
        shy_guts :: errors :: expected_module_name_instead_of ( error , shy_guts :: token ) ;
        shy_guts :: store_error ( error ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_attribute_name ( )
{
    if ( shy_guts :: token_class == shy_guts :: token_class_terminator )
        shy_guts :: continue_parsing = so_called_std_false ;
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == shy_guts :: consts :: consts )
    {
        shy_guts :: read_next_token ( ) ;
        shy_guts :: state = shy_guts :: state_reading_module_name ;
    }
    else if ( shy_guts :: token_class == shy_guts :: token_class_identifier && shy_guts :: token == shy_guts :: consts :: system )
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
        so_called_std_string error ;
        shy_guts :: errors :: expected_attribute_name_or_consts_or_system_instead_of ( error , shy_guts :: token ) ;
        shy_guts :: store_error ( error ) ;
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
        shy_guts :: store_attribute_numerator_sign ( so_called_std_string ( ) ) ;
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
        so_called_std_string error ;
        shy_guts :: errors :: expected_numerator_instead_of ( error , shy_guts :: token ) ;
        shy_guts :: store_error ( error ) ;
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
        shy_guts :: store_attribute_denominator_sign ( so_called_std_string ( ) ) ;
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
        so_called_std_string error ;
        shy_guts :: errors :: expected_denominator_instead_of ( error , token ) ;
        shy_guts :: store_error ( error ) ;
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
        so_called_std_string error ;
        shy_guts :: errors :: expected_divide_or_identifier_instead_of ( error , shy_guts :: token ) ;
        shy_guts :: store_error ( error ) ;
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
        so_called_std_string error ;
        shy_guts :: errors :: expected_system_name_instead_of ( error , shy_guts :: token ) ;
        shy_guts :: store_error ( error ) ;
        shy_guts :: state = shy_guts :: state_error ;
    }
}

void shy_guts :: handle_state_reading_machine_token ( )
{
}

void shy_guts :: handle_state_reading_machine_name ( )
{
}

void shy_guts :: handle_state_reading_state_token ( )
{
}

void shy_guts :: handle_state_reading_state_name ( )
{
}

void shy_guts :: handle_state_reading_state_content ( )
{
}

void shy_guts :: handle_state_reading_event_type ( )
{
}

void shy_guts :: handle_state_reading_action_token ( )
{
}

void shy_guts :: handle_state_reading_action_name ( )
{
}

void shy_guts :: handle_state_reading_action_command_name ( )
{
}

void shy_guts :: handle_state_reading_action_command_to_token ( )
{
}

void shy_guts :: handle_state_reading_action_command_machine_name ( )
{
}

void shy_guts :: handle_state_reading_first_condition_group ( )
{
}

void shy_guts :: handle_state_reading_next_condition_group ( )
{
}

void shy_guts :: handle_state_reading_first_condition_in_group ( )
{
}

void shy_guts :: handle_state_reading_next_condition_in_group ( )
{
}

void shy_guts :: handle_state_reading_parametric_condition_token ( )
{
}

void shy_guts :: handle_state_reading_state_condition_machine_name ( )
{
}

void shy_guts :: handle_state_reading_state_condition_is_token ( )
{
}

void shy_guts :: handle_state_reading_state_condition_state_name ( )
{
}

void shy_guts :: handle_state_reading_state_condition_parenthesis_close ( )
{
}

void shy_guts :: handle_state_reading_command_condition_command_name ( )
{
}

void shy_guts :: handle_state_reading_command_condition_parenthesis_close ( )
{
}

void shy_guts :: handle_state_reading_transition_state_name ( )
{
}

void shy_guts :: handle_state_reading_transition_if_token ( )
{
}

void shy_guts :: store_error ( std :: string )
{
}

void shy_guts :: store_module_name ( std :: string )
{
}

void shy_guts :: store_attribute_name ( std :: string )
{
}

void shy_guts :: store_attribute_numerator_sign ( std :: string )
{
}

void shy_guts :: store_attribute_numerator_value ( std :: string )
{
}

void shy_guts :: store_attribute_denominator_sign ( std :: string )
{
}

void shy_guts :: store_attribute_denominator_value ( std :: string )
{
}

void shy_guts :: store_system_name ( std :: string )
{
}

void shy_guts :: store_machine_name ( std :: string )
{
}

void shy_guts :: store_state_name ( std :: string )
{
}

void shy_guts :: store_action_name ( std :: string )
{
}

void shy_guts :: store_action_command_name ( std :: string )
{
}

void shy_guts :: store_action_command_machine_name ( std :: string )
{
}

void shy_guts :: store_action_command ( )
{
}

void shy_guts :: store_transition_state_name ( std :: string )
{
}

void shy_guts :: store_input_condition ( std :: string )
{
}

void shy_guts :: store_state_condition_machine_name ( std :: string )
{
}

void shy_guts :: store_state_condition_state_name ( std :: string )
{
}

void shy_guts :: store_state_condition ( )
{
}

void shy_guts :: store_command_condition_command_name ( std :: string )
{
}

void shy_guts :: select_entry_actions_container ( )
{
}

void shy_guts :: select_exit_actions_container ( )
{
}

void shy_guts :: select_input_actions_container ( )
{
}

void shy_guts :: select_input_actions_conditions ( )
{
}

void shy_guts :: select_input_actions_condition_group_container ( )
{
}

void shy_guts :: select_transition_conditions ( )
{
}

void shy_guts :: select_transition_condition_group_container ( )
{
}

void shy_guts :: add_on_input_event ( )
{
}

void shy_guts :: add_transition ( )
{
}

void shy_guts :: add_condition_group ( )
{
}

void shy_guts :: set_whole_value ( )
{
}

void shy_guts :: set_fract_value ( )
{
}

void shy_guts :: read_next_token ( )
{
}

void shy_guts :: trim_first_char ( )
{
}

void shy_guts :: trim_whitespaces ( )
{
}

void shy_guts :: append_first_char_to_token ( )
{
}

void shy_guts :: move_first_char_to_token ( )
{
}

void shy_guts :: first_char ( so_called_std_char & )
{
}

void shy_guts :: any_chars_in_line ( so_called_std_bool & )
{
}

void shy_loadable_parser :: parse ( so_called_std_string line )
{
    shy_guts :: whole_line = line ;
    shy_guts :: remaining_line = line ;
    shy_guts :: continue_parsing = so_called_std_true ;
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
        else if ( shy_guts :: state == shy_guts :: state_reading_action_name )
            shy_guts :: handle_state_reading_action_name ( ) ;
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

void shy_loadable_parser :: get_error ( so_called_std_string & arg_error )
{
    arg_error = shy_guts :: error ;
}

void shy_loadable_parser :: terminate ( )
{
    parse ( so_called_std_string ( 1 , shy_guts :: consts :: terminator ) ) ;
}

