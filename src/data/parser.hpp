template < typename _data_content >
class shy_data_parser_types
{
public :
    typedef _data_content data_content ;
} ;

template < typename data_parser_types >
class shy_data_parser
{
    typedef typename data_parser_types :: data_content data_content ;
    typedef typename data_parser_types :: data_content :: data_content_fract data_content_fract ;
    typedef typename data_parser_types :: data_content :: data_content_fract_container data_content_fract_container ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_action_command data_content_fsm_action_command ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_action_do data_content_fsm_action_do ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_actions data_content_fsm_actions ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_condition_command data_content_fsm_condition_command ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_condition_group data_content_fsm_condition_group ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_condition_group_container data_content_fsm_condition_group_container ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_condition_input data_content_fsm_condition_input ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_condition_state data_content_fsm_condition_state ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_machine data_content_fsm_machine ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_on_input data_content_fsm_on_input ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_state data_content_fsm_state ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_system data_content_fsm_system ;
    typedef typename data_parser_types :: data_content :: data_content_fsm_transition data_content_fsm_transition ;
    typedef typename data_parser_types :: data_content :: data_content_module data_content_module ;
    typedef typename data_parser_types :: data_content :: data_content_whole data_content_whole ;
    typedef typename data_parser_types :: data_content :: data_content_whole_container data_content_whole_container ;

    class _consts
    {
    public :
        static char brace_close ( ) { return '}' ; }
        static char brace_open ( ) { return '{' ; }
        static std :: string command ( ) { return "command" ; }
        static std :: string consts ( ) { return "consts" ; }
        static char divide ( ) { return '/' ; }
        static std :: string do_token ( ) { return "do" ; }
        static std :: string entry ( ) { return "entry" ; }
        static std :: string error_expected_action_name_instead_of ( std :: string token ) { return std :: string ( "expected action name, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_attribute_name_or_consts_or_system_instead_of ( std :: string token ) { return std :: string ( "expected attribute name or 'consts' or 'system', but got '" ) + token + std :: string ( "'" ) ; } 
        static std :: string error_expected_brace_open_instead_of ( std :: string token ) { return std :: string ( "expected '{', but got '" ) + token + ( "'" ) ; }
        static std :: string error_expected_brace_open_or_identifier_instead_of ( std :: string token ) { return std :: string ( "expected '{' or identifier, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_command_name_instead_of ( std :: string token ) { return std :: string ( "expected command name, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_consts_or_system_instead_of ( std :: string token ) { return std :: string ( "expected 'consts' or 'system', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_denominator_instead_of ( std :: string token ) { return std :: string ( "expected denominator, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_divide_or_identifier_instead_of ( std :: string token ) { return std :: string ( "expected '/' or identifier, but got '" ) + token + std :: string ( "'" ) ; } 
        static std :: string error_expected_do_or_command_or_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( std :: string token ) { return std :: string ( "expected 'do' or 'command' or 'on' or 'to' or 'state' or 'machine' or 'system' or 'consts', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_entry_or_exit_or_brace_open_instead_of ( std :: string token ) { return std :: string ( "expected 'entry' or 'exit' or '{', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_if_instead_of ( std :: string token ) { return std :: string ( "expected 'if', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_input_name_or_parenthesis_open_instead_of ( std :: string token ) { return std :: string ( "expected input name or '(', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_input_name_or_parenthesis_open_or_brace_close_instead_of ( std :: string token ) { return std :: string ( "expected input name or '(' or '}', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_is_instead_of ( std :: string token ) { return std :: string ( "expected 'is', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_machine_name_instead_of ( std :: string token ) { return std :: string ( "expected machine name, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_machine_or_command_instead_of ( std :: string token ) { return std :: string ( "expected 'machine' or 'command', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_machine_or_system_or_consts_instead_of ( std :: string token ) { return std :: string ( "expected 'machine' or 'system' or 'consts', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_module_name_instead_of ( std :: string token ) { return std :: string ( "expected module name, but got '" ) + token + std :: string ( "'" ) ; } 
        static std :: string error_expected_numerator_instead_of ( std :: string token ) { return std :: string ( "expected numerator, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( std :: string token ) { return std :: string ( "expected 'on' or 'to' or 'state' or 'machine' or 'system' or 'consts' instead of '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_parenthesis_close_instead_of ( std :: string token ) { return std :: string ( "expected ')', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_state_name_instead_of ( std :: string token ) { return std :: string ( "expected state name, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_state_or_machine_or_system_or_consts_instead_of ( std :: string token ) { return std :: string ( "expected 'state' or 'machine' or 'system' or 'consts', but got'" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_system_name_instead_of ( std :: string token ) { return std :: string ( "expected system name, but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_expected_to_instead_of ( std :: string token ) { return std :: string ( "expected 'to', but got '" ) + token + std :: string ( "'" ) ; }
        static std :: string error_unknown_fract_attribute_in_module ( std :: string attribute , std :: string module ) { return std :: string ( "unknown fract attribute '" ) + attribute + std :: string ( "' in module '" ) + module + std :: string ( "'" ) ; }
        static std :: string error_unknown_module ( std :: string module ) { return std :: string ( "unknown module '" ) + module + std :: string ( "'" ) ; }
        static std :: string error_unknown_whole_attribute_in_module ( std :: string attribute , std :: string module ) { return std :: string ( "unknown whole attribute '" ) + attribute + std :: string ( "' in module '" ) + module + std :: string ( "'" ) ; }
        static std :: string error_whole_line ( ) { return std :: string ( "whole line: " ) ; }
        static std :: string exit ( ) { return "exit" ; }
        static std :: string if_token ( ) { return "if" ; }
        static std :: string is ( ) { return "is" ; }
        static std :: string machine ( ) { return "machine" ; }
        static char minus ( ) { return '-' ; }
        static std :: string next_line ( ) { return "\n" ; }
        static std :: string on ( ) { return "on" ; }
        static char parenthesis_close ( ) { return ')' ; }
        static char parenthesis_open ( ) { return '(' ; }
        static std :: string state ( ) { return "state" ; }
        static std :: string system ( ) { return "system" ; }
        static char terminator ( ) { return '#' ; }
        static std :: string to ( ) { return "to" ; }
        static char underscore ( ) { return '_' ; }
    } ;

    enum _token_class_type
    {
        _token_class_none ,
        _token_class_terminator ,
        _token_class_identifier ,
        _token_class_number ,
        _token_class_divide ,
        _token_class_minus ,
        _token_class_brace_open ,
        _token_class_brace_close ,
        _token_class_parenthesis_open ,
        _token_class_parenthesis_close ,
        _token_class_unknown
    } ;

    enum _state_type
    {
        _state_none ,
        _state_error ,
        _state_reading_module_name ,
        _state_reading_attribute_name ,
        _state_reading_attribute_numerator_sign ,
        _state_reading_attribute_numerator_value ,
        _state_reading_attribute_denominator_sign ,
        _state_reading_attribute_denominator_value ,
        _state_determining_value_format ,
        _state_reading_system_name ,
        _state_reading_machine_token ,
        _state_reading_machine_name ,
        _state_reading_state_token ,
        _state_reading_state_name ,
        _state_reading_state_content ,
        _state_reading_event_type ,
        _state_reading_action_token ,
        _state_reading_action_name ,
        _state_reading_action_command_name ,
        _state_reading_action_command_to_token ,
        _state_reading_action_command_machine_name ,
        _state_reading_first_condition_group ,
        _state_reading_next_condition_group ,
        _state_reading_first_condition_in_group ,
        _state_reading_next_condition_in_group ,
        _state_reading_parametric_condition_token ,
        _state_reading_state_condition_machine_name ,
        _state_reading_state_condition_is_token ,
        _state_reading_state_condition_state_name ,
        _state_reading_state_condition_parenthesis_close ,
        _state_reading_command_condition_command_name ,
        _state_reading_command_condition_parenthesis_close ,
        _state_reading_transition_state_name ,
        _state_reading_transition_if_token
    } ;

public :
    shy_data_parser ( ) ;
    void set_content ( data_content & ) ;
    void parse ( std :: string ) ;
    std :: string error ( ) ;

private :
    void _handle_token_class_none ( ) ;
    void _handle_token_class_identifier ( ) ;
    void _handle_token_class_number ( ) ;
    void _handle_token_class_terminator ( ) ;
    void _handle_token_class_divide ( ) ;
    void _handle_token_class_minus ( ) ;
    void _handle_token_class_brace_open ( ) ;
    void _handle_token_class_brace_close ( ) ;
    void _handle_token_class_parenthesis_open ( ) ;
    void _handle_token_class_parenthesis_close ( ) ;
    void _handle_token_class_unknown ( ) ;
    void _handle_state_none ( ) ;
    void _handle_state_error ( ) ;
    void _handle_state_reading_module_name ( ) ;
    void _handle_state_reading_attribute_name ( ) ;
    void _handle_state_reading_attribute_numerator_sign ( ) ;
    void _handle_state_reading_attribute_numerator_value ( ) ;
    void _handle_state_reading_attribute_denominator_sign ( ) ;
    void _handle_state_reading_attribute_denominator_value ( ) ;
    void _handle_state_determining_value_format ( ) ;
    void _handle_state_reading_system_name ( ) ;
    void _handle_state_reading_machine_token ( ) ;
    void _handle_state_reading_machine_name ( ) ;
    void _handle_state_reading_state_token ( ) ;
    void _handle_state_reading_state_name ( ) ;
    void _handle_state_reading_state_content ( ) ;
    void _handle_state_reading_event_type ( ) ;
    void _handle_state_reading_action_token ( ) ;
    void _handle_state_reading_action_name ( ) ;
    void _handle_state_reading_action_command_name ( ) ;
    void _handle_state_reading_action_command_to_token ( ) ;
    void _handle_state_reading_action_command_machine_name ( ) ;
    void _handle_state_reading_first_condition_group ( ) ;
    void _handle_state_reading_next_condition_group ( ) ;
    void _handle_state_reading_first_condition_in_group ( ) ;
    void _handle_state_reading_next_condition_in_group ( ) ;
    void _handle_state_reading_parametric_condition_token ( ) ;
    void _handle_state_reading_state_condition_machine_name ( ) ;
    void _handle_state_reading_state_condition_is_token ( ) ;
    void _handle_state_reading_state_condition_state_name ( ) ;
    void _handle_state_reading_state_condition_parenthesis_close ( ) ;
    void _handle_state_reading_command_condition_command_name ( ) ;
    void _handle_state_reading_command_condition_parenthesis_close ( ) ;
    void _handle_state_reading_transition_state_name ( ) ;
    void _handle_state_reading_transition_if_token ( ) ;
    void _store_error ( std :: string ) ;
    void _store_module_name ( std :: string ) ;
    void _store_attribute_name ( std :: string ) ;
    void _store_attribute_numerator_sign ( std :: string ) ;
    void _store_attribute_numerator_value ( std :: string ) ;
    void _store_attribute_denominator_sign ( std :: string ) ;
    void _store_attribute_denominator_value ( std :: string ) ;
    void _store_system_name ( std :: string ) ;
    void _store_machine_name ( std :: string ) ;
    void _store_state_name ( std :: string ) ;
    void _store_action_name ( std :: string ) ;
    void _store_action_command_name ( std :: string ) ;
    void _store_action_command_machine_name ( std :: string ) ;
    void _store_action_command ( ) ;
    void _store_transition_state_name ( std :: string ) ;
    void _store_input_condition ( std :: string ) ;
    void _store_state_condition_machine_name ( std :: string ) ;
    void _store_state_condition_state_name ( std :: string ) ;
    void _store_state_condition ( ) ;
    void _store_command_condition_command_name ( std :: string ) ;
    void _select_entry_actions_container ( ) ;
    void _select_exit_actions_container ( ) ;
    void _select_input_actions_container ( ) ;
    void _select_input_actions_conditions ( ) ;
    void _select_input_actions_condition_group_container ( ) ;
    void _select_transition_conditions ( ) ;
    void _select_transition_condition_group_container ( ) ;
    void _add_on_input_event ( ) ;
    void _add_transition ( ) ;
    void _add_condition_group ( ) ;
    void _set_whole_value ( ) ;
    void _set_fract_value ( ) ;
    void _read_next_token ( ) ;
    void _trim_first_char ( ) ;
    void _trim_whitespaces ( ) ;
    void _append_first_char_to_token ( ) ;
    void _move_first_char_to_token ( ) ;
    char _first_char ( ) ;
    bool _any_chars_in_line ( ) ;

private :
    data_content * _content ;
    _state_type _state ;
    _token_class_type _token_class ;
    bool _continue_parsing ;
    bool _continue_reading_next_token ;
    bool _input_actions_conditions_selected ;
    bool _transition_conditions_selected ;
    std :: locale _locale ;
    std :: string _token ;
    std :: string _whole_line ;
    std :: string _remaining_line ;
    std :: string _error ;
    std :: string _module_name ;
    std :: string _attribute_name ;
    std :: string _attribute_numerator_sign ;
    std :: string _attribute_numerator_value ;
    std :: string _attribute_denominator_sign ;
    std :: string _attribute_denominator_value ;
    data_content_fsm_action_command _current_fsm_action_command ;
    data_content_fsm_actions * _current_fsm_actions ;
    data_content_fsm_condition_group * _current_fsm_condition_group ;
    data_content_fsm_condition_group_container * _current_fsm_condition_group_container ;
    data_content_fsm_condition_state _current_fsm_condition_state ;
    data_content_fsm_machine * _current_fsm_machine ;
    data_content_fsm_on_input * _current_fsm_on_input ;
    data_content_fsm_state * _current_fsm_state ;
    data_content_fsm_system * _current_fsm_system ;
    data_content_fsm_transition * _current_fsm_transition ;
} ;

template < typename data_parser_types >
shy_data_parser < data_parser_types > :: shy_data_parser ( )
: _content ( 0 )
, _state ( _state_none )
, _token_class ( _token_class_none )
, _continue_parsing ( false )
, _continue_reading_next_token ( false )
, _input_actions_conditions_selected ( false )
, _transition_conditions_selected ( false )
, _current_fsm_actions ( 0 )
, _current_fsm_condition_group ( 0 )
, _current_fsm_condition_group_container ( 0 )
, _current_fsm_machine ( 0 )
, _current_fsm_on_input ( 0 )
, _current_fsm_state ( 0 )
, _current_fsm_system ( 0 )
, _current_fsm_transition ( 0 )
{
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: set_content ( data_content & content )
{
    _content = & content ;
}

template < typename data_parser_types >
std :: string shy_data_parser < data_parser_types > :: error ( )
{
    return _error ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: parse ( std :: string line )
{
    _whole_line = line ;
    _remaining_line = line ;
    _continue_parsing = true ;
    _read_next_token ( ) ;
    while ( _continue_parsing && _token_class != _token_class_none )
    {
        if ( _state == _state_none )
            _handle_state_none ( ) ;
        else if ( _state == _state_reading_module_name )
            _handle_state_reading_module_name ( ) ;
        else if ( _state == _state_reading_attribute_name )
            _handle_state_reading_attribute_name ( ) ;
        else if ( _state == _state_reading_attribute_numerator_sign )
            _handle_state_reading_attribute_numerator_sign ( ) ;
        else if ( _state == _state_reading_attribute_numerator_value )
            _handle_state_reading_attribute_numerator_value ( ) ;
        else if ( _state == _state_determining_value_format )
            _handle_state_determining_value_format ( ) ;
        else if ( _state == _state_reading_attribute_denominator_sign )
            _handle_state_reading_attribute_denominator_sign ( ) ;
        else if ( _state == _state_reading_attribute_denominator_value )
            _handle_state_reading_attribute_denominator_value ( ) ;
        else if ( _state == _state_reading_system_name )
            _handle_state_reading_system_name ( ) ;
        else if ( _state == _state_reading_machine_token )
            _handle_state_reading_machine_token ( ) ;
        else if ( _state == _state_reading_machine_name )
            _handle_state_reading_machine_name ( ) ;
        else if ( _state == _state_reading_state_token )
            _handle_state_reading_state_token ( ) ;
        else if ( _state == _state_reading_state_name )
            _handle_state_reading_state_name ( ) ;
        else if ( _state == _state_reading_state_content )
            _handle_state_reading_state_content ( ) ;
        else if ( _state == _state_reading_event_type )
            _handle_state_reading_event_type ( ) ;
        else if ( _state == _state_reading_action_token )
            _handle_state_reading_action_token ( ) ;
        else if ( _state == _state_reading_action_name )
            _handle_state_reading_action_name ( ) ;
        else if ( _state == _state_reading_action_command_name )
            _handle_state_reading_action_command_name ( ) ;
        else if ( _state == _state_reading_action_command_to_token )
            _handle_state_reading_action_command_to_token ( ) ;
        else if ( _state == _state_reading_action_command_machine_name )
            _handle_state_reading_action_command_machine_name ( ) ;
        else if ( _state == _state_reading_first_condition_group )
            _handle_state_reading_first_condition_group ( ) ;
        else if ( _state == _state_reading_next_condition_group )
            _handle_state_reading_next_condition_group ( ) ;
        else if ( _state == _state_reading_first_condition_in_group )
            _handle_state_reading_first_condition_in_group ( ) ;
        else if ( _state == _state_reading_next_condition_in_group )
            _handle_state_reading_next_condition_in_group ( ) ;
        else if ( _state == _state_reading_parametric_condition_token )
            _handle_state_reading_parametric_condition_token ( ) ;
        else if ( _state == _state_reading_state_condition_machine_name )
            _handle_state_reading_state_condition_machine_name ( ) ;
        else if ( _state == _state_reading_state_condition_is_token )
            _handle_state_reading_state_condition_is_token ( ) ;
        else if ( _state == _state_reading_state_condition_state_name )
            _handle_state_reading_state_condition_state_name ( ) ;
        else if ( _state == _state_reading_state_condition_parenthesis_close )
            _handle_state_reading_state_condition_parenthesis_close ( ) ;
        else if ( _state == _state_reading_command_condition_command_name )
            _handle_state_reading_command_condition_command_name ( ) ;
        else if ( _state == _state_reading_command_condition_parenthesis_close )
            _handle_state_reading_command_condition_parenthesis_close ( ) ;
        else if ( _state == _state_reading_transition_state_name )
            _handle_state_reading_transition_state_name ( ) ;
        else if ( _state == _state_reading_transition_if_token )
            _handle_state_reading_transition_if_token ( ) ;
        else if ( _state == _state_error )
            _handle_state_error ( ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_none ( )
{
    if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_module_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: system ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_system_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_consts_or_system_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_module_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_module_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_module_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_name ( )
{
    if ( _token_class == _token_class_terminator )
        _continue_parsing = false ;
    else if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_module_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: system ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_system_name ;
    }
    else if ( _token_class == _token_class_identifier )
    {
        _store_attribute_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_numerator_sign ;
    }
    else
    {
        _store_error ( _consts :: error_expected_attribute_name_or_consts_or_system_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_numerator_sign ( )
{
    if ( _token_class == _token_class_minus )
    {
        _store_attribute_numerator_sign ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_numerator_value ;
    }
    else
    {
        _store_attribute_numerator_sign ( std :: string ( ) ) ;
        _state = _state_reading_attribute_numerator_value ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_numerator_value ( )
{
    if ( _token_class == _token_class_number )
    {
        _store_attribute_numerator_value ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_determining_value_format ;
    }
    else
    {
        _store_error ( _consts :: error_expected_numerator_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_determining_value_format ( )
{
    if ( _token_class == _token_class_divide )
    {
        _read_next_token ( ) ;
        _state = _state_reading_attribute_denominator_sign ;
    }
    else if ( _token_class == _token_class_identifier || _token_class == _token_class_terminator )
    {
        _set_whole_value ( ) ;
        _state = _state_reading_attribute_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_divide_or_identifier_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_denominator_sign ( )
{
    if ( _token_class == _token_class_minus )
    {
        _store_attribute_denominator_sign ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_denominator_value ;
    }
    else
    {
        _store_attribute_denominator_sign ( std :: string ( ) ) ;
        _state = _state_reading_attribute_denominator_value ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_attribute_denominator_value ( )
{
    if ( _token_class == _token_class_number )
    {
        _store_attribute_denominator_value ( _token ) ;
        _set_fract_value ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_attribute_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_denominator_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_system_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_system_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_machine_token ;
    }
    else
    {
        _store_error ( _consts :: error_expected_system_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_machine_token ( )
{
    if ( _token_class == _token_class_terminator )
        _continue_parsing = false ;
    else if ( _token_class == _token_class_identifier && _token == _consts :: machine ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_machine_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: system ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_system_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_module_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_machine_or_system_or_consts_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_machine_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_machine_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_state_token ;
    }
    else
    {
        _store_error ( _consts :: error_expected_machine_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_state_token ( )
{
    if ( _token_class == _token_class_terminator )
        _continue_parsing = false ;
    else if ( _token_class == _token_class_identifier && _token == _consts :: state ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_state_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: machine ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_machine_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: system ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_system_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_module_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_state_or_machine_or_system_or_consts_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_state_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_state_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_state_content ;
    }
    else
    {
        _store_error ( _consts :: error_expected_state_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_state_content ( )
{
    if ( _token_class == _token_class_terminator )
        _continue_parsing = false ;
    else if ( _token_class == _token_class_identifier && _token == _consts :: on ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_event_type ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: to ( ) )
    {
        _add_transition ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_transition_state_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: state ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_state_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: machine ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_machine_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: system ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_system_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_module_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_event_type ( )
{
    if ( _token_class == _token_class_identifier && _token == _consts :: entry ( ) )
    {
        _select_entry_actions_container ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_action_token ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: exit ( ) )
    {
        _select_exit_actions_container ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_action_token ;
    }
    else if ( _token_class == _token_class_brace_open )
    {
        _add_on_input_event ( ) ;
        _select_input_actions_container ( ) ;
        _select_input_actions_conditions ( ) ;
        _select_input_actions_condition_group_container ( ) ;
        _state = _state_reading_first_condition_group ;
    }
    else
    {
        _store_error ( _consts :: error_expected_entry_or_exit_or_brace_open_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_action_token ( )
{
    if ( _token_class == _token_class_terminator )
        _continue_parsing = false ;
    else if ( _token_class == _token_class_identifier && _token == _consts :: do_token ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_action_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: command ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_action_command_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: on ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_event_type ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: to ( ) )
    {
        _add_transition ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_transition_state_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: state ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_state_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: machine ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_machine_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: system ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_system_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: consts ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_module_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_do_or_command_or_on_or_to_or_state_or_machine_or_system_or_consts_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_action_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_action_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_action_token ;
    }
    else
    {
        _store_error ( _consts :: error_expected_action_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_action_command_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_action_command_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_action_command_to_token ;
    }
    else
    {
        _store_error ( _consts :: error_expected_command_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_action_command_to_token ( )
{
    if ( _token_class == _token_class_identifier && _token == _consts :: to ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_action_command_machine_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_to_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_action_command_machine_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_action_command_machine_name ( _token ) ;
        _store_action_command ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_action_token ;
    }
    else
    {
        _store_error ( _consts :: error_expected_machine_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_first_condition_group ( )
{
    if ( _token_class == _token_class_brace_open )
        _state = _state_reading_next_condition_group ;
    else
    {
        _store_error ( _consts :: error_expected_brace_open_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_next_condition_group ( )
{
    if ( _token_class == _token_class_brace_open )
    {
        _add_condition_group ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_first_condition_in_group ;
    }
    else if ( _token_class == _token_class_identifier && _input_actions_conditions_selected )
        _state = _state_reading_action_token ;
    else if ( _token_class == _token_class_identifier && _transition_conditions_selected )
        _state = _state_reading_state_content ;
    else
    {
        _store_error ( _consts :: error_expected_brace_open_or_identifier_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_first_condition_in_group ( )
{
    if ( _token_class == _token_class_identifier )
        _state = _state_reading_next_condition_in_group ;
    else if ( _token_class == _token_class_parenthesis_open )
        _state = _state_reading_next_condition_in_group ;
    else
    {
        _store_error ( _consts :: error_expected_input_name_or_parenthesis_open_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_next_condition_in_group ( )
{
    if ( _token_class == _token_class_parenthesis_open )
    {
        _read_next_token ( ) ;
        _state = _state_reading_parametric_condition_token ;
    }
    else if ( _token_class == _token_class_identifier )
    {
        _store_input_condition ( _token ) ;
        _read_next_token ( ) ;
    }
    else if ( _token_class == _token_class_brace_close )
    {
        _read_next_token ( ) ;
        _state = _state_reading_next_condition_group ;
    }
    else
    {
        _store_error ( _consts :: error_expected_input_name_or_parenthesis_open_or_brace_close_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_parametric_condition_token ( )
{
    if ( _token_class == _token_class_identifier && _token == _consts :: machine ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_state_condition_machine_name ;
    }
    else if ( _token_class == _token_class_identifier && _token == _consts :: command ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_command_condition_command_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_machine_or_command_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_state_condition_machine_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_state_condition_machine_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_state_condition_is_token ;
    }
    else
    {
        _store_error ( _consts :: error_expected_machine_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_state_condition_is_token ( )
{
    if ( _token_class == _token_class_identifier && _token == _consts :: is ( ) )
    {
        _read_next_token ( ) ;
        _state = _state_reading_state_condition_state_name ;
    }
    else
    {
        _store_error ( _consts :: error_expected_is_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_state_condition_state_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_state_condition_state_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_state_condition_parenthesis_close ;
    }
    else
    {
        _store_error ( _consts :: error_expected_state_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_state_condition_parenthesis_close ( )
{
    if ( _token_class == _token_class_parenthesis_close )
    {
        _store_state_condition ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_next_condition_in_group ;
    }
    else
    {
        _store_error ( _consts :: error_expected_parenthesis_close_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_command_condition_command_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_command_condition_command_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_command_condition_parenthesis_close ;
    }
    else
    {
        _store_error ( _consts :: error_expected_command_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_command_condition_parenthesis_close ( )
{
    if ( _token_class == _token_class_parenthesis_close )
    {
        _read_next_token ( ) ;
        _state = _state_reading_next_condition_in_group ;
    }
    else
    {
        _store_error ( _consts :: error_expected_parenthesis_close_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_transition_state_name ( )
{
    if ( _token_class == _token_class_identifier )
    {
        _store_transition_state_name ( _token ) ;
        _read_next_token ( ) ;
        _state = _state_reading_transition_if_token ;
    }
    else
    {
        _store_error ( _consts :: error_expected_state_name_instead_of ( _token ) ) ;
        _state = _state_error ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_reading_transition_if_token ( )
{
    if ( _token_class == _token_class_identifier && _token == _consts :: if_token ( ) )
    {
        _select_transition_conditions ( ) ;
        _select_transition_condition_group_container ( ) ;
        _read_next_token ( ) ;
        _state = _state_reading_first_condition_group ;
    }
    else
        _state = _state_reading_state_content ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_state_error ( )
{
    _continue_parsing = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _read_next_token ( )
{
    _token = std :: string ( ) ;
    _token_class = _token_class_none ;
    _trim_whitespaces ( ) ;
    _continue_reading_next_token = true ;
    while ( _any_chars_in_line ( ) && _continue_reading_next_token )
    {
        if ( _token_class == _token_class_none )
            _handle_token_class_none ( ) ;
        else if ( _token_class == _token_class_terminator )
            _handle_token_class_terminator ( ) ;
        else if ( _token_class == _token_class_number )
            _handle_token_class_number ( ) ;
        else if ( _token_class == _token_class_identifier )
            _handle_token_class_identifier ( ) ;
        else if ( _token_class == _token_class_divide )
            _handle_token_class_divide ( ) ;
        else if ( _token_class == _token_class_minus )
            _handle_token_class_minus ( ) ;
        else if ( _token_class == _token_class_brace_open )
            _handle_token_class_brace_open ( ) ;
        else if ( _token_class == _token_class_brace_close )
            _handle_token_class_brace_close ( ) ;
        else if ( _token_class == _token_class_parenthesis_open )
            _handle_token_class_parenthesis_open ( ) ;
        else if ( _token_class == _token_class_parenthesis_close )
            _handle_token_class_parenthesis_close ( ) ;
        else
            _handle_token_class_unknown ( ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_none ( )
{
    if ( std :: isdigit ( _first_char ( ) , _locale ) )
        _token_class = _token_class_number ;
    else if ( std :: isalpha ( _first_char ( ) , _locale ) )
        _token_class = _token_class_identifier ;
    else if ( _first_char ( ) == _consts :: terminator ( ) )
        _token_class = _token_class_terminator ;
    else if ( _first_char ( ) == _consts :: divide ( ) )
        _token_class = _token_class_divide ;
    else if ( _first_char ( ) == _consts :: minus ( ) )
        _token_class = _token_class_minus ;
    else if ( _first_char ( ) == _consts :: brace_open ( ) )
        _token_class = _token_class_brace_open ;
    else if ( _first_char ( ) == _consts :: brace_close ( ) )
        _token_class = _token_class_brace_close ;
    else if ( _first_char ( ) == _consts :: parenthesis_open ( ) )
        _token_class = _token_class_parenthesis_open ;
    else if ( _first_char ( ) == _consts :: parenthesis_close ( ) )
        _token_class = _token_class_parenthesis_close ;
    else
        _token_class = _token_class_unknown ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_number ( )
{
    if ( std :: isdigit ( _first_char ( ) , _locale ) )
        _move_first_char_to_token ( ) ;
    else
        _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_identifier ( )
{
    if ( std :: isalpha ( _first_char ( ) , _locale ) 
      || std :: isdigit ( _first_char ( ) , _locale )
      || _first_char ( ) == _consts :: underscore ( )
       )
    {
        _move_first_char_to_token ( ) ;
    }
    else
        _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_terminator ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_divide ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_minus ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_brace_open ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_brace_close ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_parenthesis_open ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_parenthesis_close ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _handle_token_class_unknown ( )
{
    _move_first_char_to_token ( ) ;
    _continue_reading_next_token = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _move_first_char_to_token ( )
{
    _append_first_char_to_token ( ) ;
    _trim_first_char ( ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _trim_whitespaces ( )
{
    while ( _any_chars_in_line ( ) && std :: isspace ( _first_char ( ) , _locale ) )
        _trim_first_char ( ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _trim_first_char ( )
{
    _remaining_line . erase ( _remaining_line . begin ( ) ) ;
}

template < typename data_parser_types >
char shy_data_parser < data_parser_types > :: _first_char ( )
{
    return _remaining_line . at ( 0 ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _append_first_char_to_token ( )
{
    _token += std :: string ( 1 , _first_char ( ) ) ;
}

template < typename data_parser_types >
bool shy_data_parser < data_parser_types > :: _any_chars_in_line ( )
{
    return ! _remaining_line . empty ( ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_error ( std :: string arg_error )
{
    _error = std :: string ( ) ;
    _error += arg_error ;
    _error += _consts :: next_line ( ) ;
    _error += _consts :: error_whole_line ( ) ;
    _error += _whole_line ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_module_name ( std :: string module_name )
{
    _module_name = module_name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_name ( std :: string attribute_name )
{
    _attribute_name = attribute_name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_numerator_sign ( std :: string attribute_numerator_sign )
{
    _attribute_numerator_sign = attribute_numerator_sign ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_numerator_value ( std :: string attribute_numerator_value )
{
    _attribute_numerator_value = attribute_numerator_value ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_denominator_sign ( std :: string attribute_denominator_sign )
{
    _attribute_denominator_sign = attribute_denominator_sign ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_attribute_denominator_value ( std :: string attribute_denominator_value )
{
    _attribute_denominator_value = attribute_denominator_value ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_system_name ( std :: string name )
{
    if ( _content -> fsm_systems . find ( name ) == _content -> fsm_systems . end ( ) )
        _content -> fsm_systems [ name ] = data_content_fsm_system ( ) ;
    _current_fsm_system = & ( _content -> fsm_systems [ name ] ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_machine_name ( std :: string name )
{
    if ( _current_fsm_system )
    {
        if ( _current_fsm_system -> machines . find ( name ) == _current_fsm_system -> machines . end ( ) )
            _current_fsm_system -> machines [ name ] = data_content_fsm_machine ( ) ;
        _current_fsm_machine = & ( _current_fsm_system -> machines [ name ] ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_state_name ( std :: string name )
{
    if ( _current_fsm_machine )
    {
        if ( _current_fsm_machine -> states . find ( name ) == _current_fsm_machine -> states . end ( ) )
            _current_fsm_machine -> states [ name ] = data_content_fsm_state ( ) ;
        _current_fsm_state = & ( _current_fsm_machine -> states [ name ] ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_action_name ( std :: string name )
{
    if ( _current_fsm_actions )
    {
        data_content_fsm_action_do action_do ;
        action_do . action = name ;
        _current_fsm_actions -> actions . push_back ( action_do ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_action_command_name ( std :: string name )
{
    _current_fsm_action_command . command = name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_action_command_machine_name ( std :: string name )
{
    _current_fsm_action_command . machine = name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_action_command ( )
{
    if ( _current_fsm_actions )
        _current_fsm_actions -> commands . push_back ( _current_fsm_action_command ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_transition_state_name ( std :: string name )
{
    if ( _current_fsm_transition )
        _current_fsm_transition -> state = name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_input_condition ( std :: string input )
{
    if ( _current_fsm_condition_group )
    {
        data_content_fsm_condition_input condition ;
        condition . input = input ;
        _current_fsm_condition_group -> inputs . push_back ( condition ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_state_condition_machine_name ( std :: string name )
{
    _current_fsm_condition_state . machine = name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_state_condition_state_name ( std :: string name )
{
    _current_fsm_condition_state . state = name ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_state_condition ( )
{
    if ( _current_fsm_condition_group )
        _current_fsm_condition_group -> states . push_back ( _current_fsm_condition_state ) ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _store_command_condition_command_name ( std :: string name )
{
    if ( _current_fsm_condition_group )
    {
        data_content_fsm_condition_command condition ;
        condition . command = name ;
        _current_fsm_condition_group -> commands . push_back ( condition ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _select_entry_actions_container ( )
{
    if ( _current_fsm_state )
        _current_fsm_actions = & _current_fsm_state -> on_entry ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _select_exit_actions_container ( )
{
    if ( _current_fsm_state )
        _current_fsm_actions = & _current_fsm_state -> on_exit ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _select_input_actions_container ( )
{
    if ( _current_fsm_on_input )
        _current_fsm_actions = & _current_fsm_on_input -> actions ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _select_input_actions_condition_group_container ( )
{
    if ( _current_fsm_on_input )
        _current_fsm_condition_group_container = & _current_fsm_on_input -> condition_groups ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _select_transition_condition_group_container ( )
{
    if ( _current_fsm_transition )
        _current_fsm_condition_group_container = & _current_fsm_transition -> condition_groups ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _select_input_actions_conditions ( )
{
    _input_actions_conditions_selected = true ;
    _transition_conditions_selected = false ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _select_transition_conditions ( )
{
    _input_actions_conditions_selected = false ;
    _transition_conditions_selected = true ;
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _add_on_input_event ( )
{
    if ( _current_fsm_state )
    {
        _current_fsm_state -> on_input . push_back ( data_content_fsm_on_input ( ) ) ;
        _current_fsm_on_input = & _current_fsm_state -> on_input . back ( ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _add_transition ( )
{
    if ( _current_fsm_state )
    {
        _current_fsm_state -> transitions . push_back ( data_content_fsm_transition ( ) ) ;
        _current_fsm_transition = & _current_fsm_state -> transitions . back ( ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _add_condition_group ( )
{
    if ( _current_fsm_condition_group_container )
    {
        _current_fsm_condition_group_container -> push_back ( data_content_fsm_condition_group ( ) ) ;
        _current_fsm_condition_group = & _current_fsm_condition_group_container -> back ( ) ;
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _set_whole_value ( )
{
    typename data_content :: data_content_module_container :: iterator module_i ;
    module_i = _content -> modules . find ( _module_name ) ;
    if ( module_i == _content -> modules . end ( ) )
        _error = _consts :: error_unknown_module ( _module_name ) ;
    else
    {
        data_content_module & module = module_i -> second ;
        typename data_content_whole_container :: iterator whole_i ;
        whole_i = module . name_to_whole . find ( _attribute_name ) ;
        if ( whole_i == module . name_to_whole . end ( ) )
            _error = _consts :: error_unknown_whole_attribute_in_module ( _attribute_name , _module_name ) ;
        else
        {
            data_content_whole & whole = whole_i -> second ;
            whole . sign = _attribute_numerator_sign ;
            whole . value = _attribute_numerator_value ;
        }
    }
}

template < typename data_parser_types >
void shy_data_parser < data_parser_types > :: _set_fract_value ( )
{
    typename data_content :: data_content_module_container :: iterator module_i ;
    module_i = _content -> modules . find ( _module_name ) ;
    if ( module_i == _content -> modules . end ( ) )
        _error = _consts :: error_unknown_module ( _module_name ) ;
    else
    {
        data_content_module & module = module_i -> second ;
        typename data_content_fract_container :: iterator fract_i ;
        fract_i = module . name_to_fract . find ( _attribute_name ) ;
        if ( fract_i == module . name_to_fract . end ( ) )
            _error = _consts :: error_unknown_fract_attribute_in_module ( _attribute_name , _module_name ) ;
        else
        {
            data_content_fract & fract = fract_i -> second ;
            fract . numerator_sign = _attribute_numerator_sign ;
            fract . numerator_value = _attribute_numerator_value ;
            fract . denominator_sign = _attribute_denominator_sign ;
            fract . denominator_value = _attribute_denominator_value ;
        }
    }
}

